#!/usr/bin/env python3
"""Check that the repository is complete and consistent. Offline.

    python3 tools/validate.py                      # run every check
    python3 tools/validate.py --write-checksums    # rewrite SHA256SUMS, then run every check

Checks
  1  index       benchmark.json points at files and folders that exist
  2  upstream    profile/ and bases/ folders hold the listed upstream files and nothing else
  3  checksums   SHA256SUMS lists every data file under cases/ and bases/, with the right digest
  4  sets        each reference set is well formed and agrees with its own counts
  5  views       the generated views match the reference sets
  6  rdf         every Turtle and RDF/XML document parses (skipped if rdflib is not installed)
  7  links       relative links in the Markdown files resolve

Standard library only, apart from the optional rdflib. Exit status 1 if a check fails.
tools/fetch_upstream.py --check compares the upstream files with their source (needs network).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import urllib.parse
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_views  # noqa: E402

DATA_FOLDERS = ("cases", "bases")
SUMS = ROOT / "SHA256SUMS"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def data_files() -> list[Path]:
    """Every file under cases/ and bases/ except the pages written for this repository."""
    pages = set(own_markdown())
    files = []
    for folder in DATA_FOLDERS:
        files += [p for p in (ROOT / folder).rglob("*") if p.is_file() and p not in pages]
    return sorted(files, key=lambda p: p.relative_to(ROOT).as_posix())


def write_checksums() -> None:
    lines = [f"{sha256(path)}  {path.relative_to(ROOT).as_posix()}\n" for path in data_files()]
    SUMS.write_text("".join(lines), encoding="utf-8")
    print(f"SHA256SUMS written: {len(lines)} files")


def check_index(index: dict) -> list[str]:
    errors = []
    source_ids = {source["id"] for source in index["sources"]}
    base_ids = {base["id"] for base in index["bases"]}
    for case in index["cases"]:
        name = case["id"]
        if not (ROOT / case["requirements"]["reference_set"]).is_file():
            errors.append(f"{name}: reference set missing")
        for source in case["requirements"]["sources"]:
            if source["availability"] == "included" and not (ROOT / source["path"]).is_file():
                errors.append(f"{name}: requirement source missing: {source['path']}")
            evidence = source.get("licence_evidence")
            if evidence and not (ROOT / evidence).is_file():
                errors.append(f"{name}: licence evidence missing: {evidence}")
        if not (ROOT / case["profile"]["directory"]).is_dir():
            errors.append(f"{name}: profile folder missing")
        if case["profile"]["source"] not in source_ids:
            errors.append(f"{name}: unknown profile source {case['profile']['source']}")
        for key in ("id", "alternative"):
            base = case["base"].get(key)
            if base and base not in base_ids:
                errors.append(f"{name}: unknown base {base}")
        for block in (case["profile"], case["base"]):
            if block["status"] not in index["status_values"]:
                errors.append(f"{name}: unknown status {block['status']}")
    for base in index["bases"]:
        if base["source"] not in source_ids:
            errors.append(f"{base['id']}: unknown source {base['source']}")
        for user in base["used_by"]:
            if user not in {case["id"] for case in index["cases"]}:
                errors.append(f"{base['id']}: used_by names an unknown case {user}")
    return errors


def check_upstream(index: dict) -> list[str]:
    errors = []
    expected: dict[Path, set[str]] = {}
    for source in index["sources"]:
        folder = ROOT / source["local_directory"]
        listed = expected.setdefault(folder, set())
        for name in source["files"]:
            listed.add(name)
            if not (folder / name).is_file():
                errors.append(f"{source['id']}: missing {source['local_directory']}/{name}")
        for unpacked in source.get("extracted", {}).values():
            for path in (ROOT / unpacked).rglob("*"):
                if path.is_file():
                    listed.add(path.relative_to(folder).as_posix())
    for folder, listed in expected.items():
        present = {p.relative_to(folder).as_posix() for p in folder.rglob("*") if p.is_file()}
        for extra in sorted(present - listed):
            errors.append(f"not an upstream file: {folder.relative_to(ROOT).as_posix()}/{extra}")
    return errors


def check_checksums() -> list[str]:
    if not SUMS.is_file():
        return ["SHA256SUMS is missing (run with --write-checksums)"]
    errors, listed = [], {}
    for line in SUMS.read_text(encoding="utf-8").splitlines():
        digest, _, name = line.partition("  ")
        listed[name] = digest
    present = {path.relative_to(ROOT).as_posix(): path for path in data_files()}
    for name in sorted(set(listed) - set(present)):
        errors.append(f"listed but missing: {name}")
    for name in sorted(set(present) - set(listed)):
        errors.append(f"not listed: {name}")
    for name in sorted(set(listed) & set(present)):
        if sha256(present[name]) != listed[name]:
            errors.append(f"digest differs: {name}")
    return errors


def check_sets(index: dict) -> list[str]:
    errors = []
    for case in index["cases"]:
        name = case["id"]
        data = json.loads((ROOT / case["requirements"]["reference_set"]).read_text(encoding="utf-8"))
        rows, atoms = data["requirements"], data["atoms"]
        row_ids, atom_ids = [r["id"] for r in rows], [a["id"] for a in atoms]
        if data["case"] != name:
            errors.append(f"{name}: the set says it is {data['case']}")
        if data["reference_document"] != case["rq1"]["reference_document"] or data["base"] != case["rq1"]["base"]:
            errors.append(f"{name}: benchmark.json and the set disagree on reference document or base")
        for label, ids in (("row", row_ids), ("atom", atom_ids)):
            for duplicate, n in Counter(ids).items():
                if n > 1:
                    errors.append(f"{name}: duplicate {label} id {duplicate}")
        listed_under_rows = [a for r in rows for a in r["atom_ids"]]
        if sorted(listed_under_rows) != sorted(atom_ids):
            errors.append(f"{name}: rows and atoms do not list the same atoms")
        for atom in atoms:
            if atom["parent_id"] not in row_ids:
                errors.append(f"{name}: {atom['id']} has no row {atom['parent_id']}")
            if atom["restates_dcat_ap"] != (atom["relation_to_base"] == "restates_base"):
                errors.append(f"{name}: {atom['id']} restates_dcat_ap disagrees with relation_to_base")
            for other in list(atom.get("overlaps", [])) + [atom.get("merged_into")] + list(atom.get("umbrella_of", [])):
                if other and other not in atom_ids:
                    errors.append(f"{name}: {atom['id']} points at unknown atom {other}")
        stored = data["counts"]
        scored = [a for a in atoms if a["scored_by_default"]]
        actual = {
            "rows": len(rows),
            "atoms": len(atoms),
            "scored_by_default": len(scored),
            "scored_by_default_without_dcat_ap_restatements": sum(not a["restates_dcat_ap"] for a in scored),
        }
        for key, value in actual.items():
            if stored.get(key) != value:
                errors.append(f"{name}: counts.{key} is {stored.get(key)}, the atoms give {value}")
        if stored.get("atoms_by_stratum") != dict(Counter(a["stratum"] for a in atoms)):
            errors.append(f"{name}: counts.atoms_by_stratum disagrees with the atoms")
    return errors


def check_views() -> list[str]:
    errors = []
    for path, text in build_views.build().items():
        if not path.is_file() or path.read_text(encoding="utf-8") != text:
            errors.append(f"out of date: {path.relative_to(ROOT).as_posix()} (run tools/build_views.py)")
    return errors


def check_rdf(index: dict) -> list[str] | None:
    try:
        from rdflib import Graph
    except ImportError:
        return None
    import logging
    logging.getLogger("rdflib").setLevel(logging.ERROR)
    # Snippets that a specification page includes are not documents of their own.
    fragments = tuple(
        f"{source['local_directory']}/{prefix}"
        for source in index["sources"] for prefix in source.get("rdf_fragments", [])
    )
    errors = []
    formats = {".ttl": "turtle", ".rdf": "xml"}
    for path in data_files():
        if path.relative_to(ROOT).as_posix().startswith(fragments):
            continue
        if path.suffix in formats:
            try:
                Graph().parse(str(path), format=formats[path.suffix])
            except Exception as error:  # rdflib raises many kinds of parse error
                errors.append(f"{path.relative_to(ROOT).as_posix()}: {type(error).__name__}: {str(error)[:120]}")
    return errors


LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")


def own_markdown() -> list[Path]:
    """Markdown written for this repository, not the upstream files kept beside it."""
    files = [p for p in ROOT.glob("*.md")] + list((ROOT / "docs").glob("*.md"))
    files += [ROOT / "bases" / "README.md"] + list((ROOT / "cases").glob("*/README.md"))
    return sorted(p for p in files if p.is_file())


def check_links() -> list[str]:
    errors = []
    for path in own_markdown():
        for target in LINK.findall(path.read_text(encoding="utf-8")):
            if re.match(r"[a-z]+:", target) or target.startswith("#"):
                continue
            local = urllib.parse.unquote(target.split("#")[0])
            if not (path.parent / local).exists():
                errors.append(f"{path.relative_to(ROOT).as_posix()}: broken link {target}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--write-checksums", action="store_true", help="rewrite SHA256SUMS first")
    args = parser.parse_args()
    if args.write_checksums:
        write_checksums()

    index = json.loads((ROOT / "benchmark.json").read_text(encoding="utf-8"))
    checks = [
        ("index", check_index(index)),
        ("upstream", check_upstream(index)),
        ("checksums", check_checksums()),
        ("sets", check_sets(index)),
        ("views", check_views()),
        ("rdf", check_rdf(index)),
        ("links", check_links()),
    ]
    failed = 0
    for name, errors in checks:
        if errors is None:
            print(f"skip  {name} (rdflib is not installed)")
        elif errors:
            failed += 1
            print(f"FAIL  {name}")
            for error in errors:
                print(f"        {error}")
        else:
            print(f"ok    {name}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
