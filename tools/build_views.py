#!/usr/bin/env python3
"""Rebuild the generated views of the reference requirements.

    python3 tools/build_views.py           # write the views
    python3 tools/build_views.py --check   # exit 1 if a view on disk is out of date

Reads   cases/<case>/requirements/reference-set.json   (never changed by this script)
Writes  cases/<case>/requirements/atoms.csv            one row per atom
        cases/atoms.csv                                the same rows for all cases
        cases/counts.json                              counts per case
        cases/term-check.csv                           atom statements that carry a term or a profile name

Every value in the views is copied from the reference set. Nothing is reworded,
re-labelled or inferred. Standard library only.
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

COLUMNS = [
    "case", "atom_id", "row_id", "stratum", "statement", "resource",
    "status_in_source", "modality", "applicability",
    "relation_to_base", "restates_dcat_ap", "reuse_or_alignment_rule",
    "scored_by_default", "merged_into", "umbrella_of", "overlaps", "source_locator",
]

# The statement rule of the RQ2 atom contract (vpe-rq2-prototype,
# requirement-reuse-service/schema/rq2_atom.linkml.yaml): no IRIs and no prefixed names.
TERM = re.compile(r"(https?://|urn:|\b[a-zA-Z][\w-]*:[A-Za-z_])")

# Names under which each case's own target profile appears in its sources.
OWN_PROFILE = {
    "jrc-research": r"DCAT-AP-JRC",
    "statdcat": r"StatDCAT",
    "geodcat": r"GeoDCAT",
    "healthdcat": r"HealthDCAT",
    "mobilitydcat": r"mobilityDCAT|napDCAT",
}


def case_ids() -> list[str]:
    index = json.loads((ROOT / "benchmark.json").read_text(encoding="utf-8"))
    return [case["id"] for case in index["cases"]]


def load(case: str) -> dict:
    path = ROOT / "cases" / case / "requirements" / "reference-set.json"
    return json.loads(path.read_text(encoding="utf-8"))


def flag(value: bool) -> str:
    return "true" if value else "false"


def atom_row(case: str, atom: dict) -> dict:
    return {
        "case": case,
        "atom_id": atom["id"],
        "row_id": atom["parent_id"],
        "stratum": atom["stratum"],
        "statement": atom["statement"],
        "resource": atom["standard_form"].get("resource", ""),
        "status_in_source": atom["status_in_source"],
        "modality": atom["modality"],
        "applicability": atom["applicability"],
        "relation_to_base": atom["relation_to_base"],
        "restates_dcat_ap": flag(atom["restates_dcat_ap"]),
        "reuse_or_alignment_rule": flag(atom["reuse_or_alignment_rule"]),
        "scored_by_default": flag(atom["scored_by_default"]),
        "merged_into": atom.get("merged_into", "") or "",
        "umbrella_of": ";".join(atom.get("umbrella_of", []) or []),
        "overlaps": ";".join(atom.get("overlaps", []) or []),
        "source_locator": atom["source_locator"],
    }


def to_csv(rows: list[dict], columns: list[str]) -> str:
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=columns, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue()


def counts(data: dict) -> dict:
    atoms = data["atoms"]
    scored = [a for a in atoms if a["scored_by_default"]]
    return {
        "reference_document": data["reference_document"],
        "base": data["base"],
        "rows": len(data["requirements"]),
        "atoms": len(atoms),
        "atoms_by_stratum": dict(sorted(Counter(a["stratum"] for a in atoms).items())),
        "atoms_by_status_in_source": dict(sorted(Counter(a["status_in_source"] for a in atoms).items())),
        "atoms_by_relation_to_base": dict(sorted(Counter(a["relation_to_base"] for a in atoms).items())),
        "atoms_restating_the_base": sum(a["restates_dcat_ap"] for a in atoms),
        "atoms_reuse_or_alignment_rule": sum(a["reuse_or_alignment_rule"] for a in atoms),
        "rq1_scored_by_default": len(scored),
        "rq1_scored_by_default_without_restatements": sum(not a["restates_dcat_ap"] for a in scored),
    }


def term_check(case: str, data: dict) -> list[dict]:
    found = []
    for atom in data["atoms"]:
        for check, pattern in (("iri_or_prefixed_name", TERM), ("own_profile_name", re.compile(OWN_PROFILE[case]))):
            match = pattern.search(atom["statement"])
            if match:
                found.append({
                    "case": case, "atom_id": atom["id"], "stratum": atom["stratum"],
                    "check": check, "matched": match.group(0), "statement": atom["statement"],
                })
    return found


def build() -> dict[Path, str]:
    outputs: dict[Path, str] = {}
    every_row, every_count, every_finding = [], {}, []
    for case in case_ids():
        data = load(case)
        rows = [atom_row(case, atom) for atom in data["atoms"]]
        outputs[ROOT / "cases" / case / "requirements" / "atoms.csv"] = to_csv(rows, COLUMNS)
        every_row += rows
        every_count[case] = counts(data)
        every_finding += term_check(case, data)
    total = Counter()
    for item in every_count.values():
        for key in ("rows", "atoms", "atoms_restating_the_base", "atoms_reuse_or_alignment_rule",
                    "rq1_scored_by_default", "rq1_scored_by_default_without_restatements"):
            total[key] += item[key]
    every_count["all"] = dict(total)
    outputs[ROOT / "cases" / "atoms.csv"] = to_csv(every_row, COLUMNS)
    outputs[ROOT / "cases" / "counts.json"] = json.dumps(every_count, indent=2, ensure_ascii=False) + "\n"
    outputs[ROOT / "cases" / "term-check.csv"] = to_csv(
        every_finding, ["case", "atom_id", "stratum", "check", "matched", "statement"])
    return outputs


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--check", action="store_true", help="compare with the files on disk; write nothing")
    args = parser.parse_args()
    stale = 0
    for path, text in build().items():
        name = path.relative_to(ROOT)
        if args.check:
            if not path.is_file() or path.read_text(encoding="utf-8") != text:
                print(f"out of date: {name}")
                stale += 1
        else:
            path.write_text(text, encoding="utf-8")
            print(f"written: {name}")
    if stale:
        print("run: python3 tools/build_views.py", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
