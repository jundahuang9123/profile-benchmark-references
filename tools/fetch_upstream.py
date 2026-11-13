#!/usr/bin/env python3
"""Download the upstream files listed in benchmark.json, or check the local copies against them.

    python3 tools/fetch_upstream.py --check            # compare every local copy with upstream
    python3 tools/fetch_upstream.py                    # download every listed file (overwrites)
    python3 tools/fetch_upstream.py --source geodcat-ap-1.0 [--check]

Each file is read from

    https://raw.githubusercontent.com/<repository>/<commit>/<upstream_directory>/<file>

so the result depends only on the pinned commit, not on what the upstream repository
looks like today. Standard library only. Exit status 1 if a file is missing upstream or
differs from the local copy.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = "https://raw.githubusercontent.com"


def upstream_url(source: dict, name: str) -> str:
    parts = [source["repository"], source["commit"]]
    if source["upstream_directory"]:
        parts.append(source["upstream_directory"])
    parts.append(name)
    return RAW + "/" + urllib.parse.quote("/".join(parts))


def download(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "profile-benchmark-references"})
    with urllib.request.urlopen(request, timeout=120) as response:
        return response.read()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--check", action="store_true", help="compare with the local copies; write nothing")
    parser.add_argument("--source", action="append", help="only this source id (repeatable)")
    args = parser.parse_args()

    index = json.loads((ROOT / "benchmark.json").read_text(encoding="utf-8"))
    sources = index["sources"]
    if args.source:
        unknown = set(args.source) - {s["id"] for s in sources}
        if unknown:
            print("unknown source id: " + ", ".join(sorted(unknown)), file=sys.stderr)
            return 2
        sources = [s for s in sources if s["id"] in args.source]

    problems = 0
    for source in sources:
        print(f"{source['id']}  ({source['repository']} @ {source['commit'][:10]})")
        for name in source["files"]:
            local = ROOT / source["local_directory"] / name
            url = upstream_url(source, name)
            try:
                data = download(url)
            except (urllib.error.URLError, TimeoutError) as error:
                print(f"  FAILED    {name}: {error}")
                problems += 1
                continue
            digest = hashlib.sha256(data).hexdigest()
            if args.check:
                if not local.is_file():
                    print(f"  MISSING   {name}")
                    problems += 1
                elif hashlib.sha256(local.read_bytes()).hexdigest() != digest:
                    print(f"  DIFFERS   {name}")
                    problems += 1
                else:
                    print(f"  same      {name}")
            else:
                local.parent.mkdir(parents=True, exist_ok=True)
                unchanged = local.is_file() and local.read_bytes() == data
                if not unchanged:
                    local.write_bytes(data)
                print(f"  {'same     ' if unchanged else 'written  '} {name}  {len(data)} bytes  sha256 {digest[:16]}")
    if problems:
        print(f"{problems} problem(s)", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
