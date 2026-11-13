# Fork notes

What this repository took from the RQ1 reference library, what it left behind and what it added.

- Forked from: `requirements-benchmark-references`, commit `38ea67150aa159686ed30b4da7cef03df09e4fd8` (12 November 2026), with its history.
- Of the 352 files at that commit, 20 were moved, 330 removed and 2 stayed in place (`README.md`, rewritten, and `.gitignore`).
- Nothing is lost: `git show 38ea671:<old path>` prints any removed file, and `git log --follow <new path>` follows a moved one into the RQ1 history.

## Moved, bytes unchanged

| RQ1 path under `benchmark-data/` | Here |
|---|---|
| `reference-sets-v3/<case>.json` (5 files) | `cases/<case>/requirements/reference-set.json` |
| `geodcat/reference-requirements/geo-final.pdf` | `cases/geodcat/profile/geodcat-ap_1.0.pdf` |
| `statdcat/reference-requirements/stat-final.pdf` | `cases/statdcat/profile/statdcat-ap_version_1.0.0_0.pdf` |
| `mobilitydcat/reference-requirements/mob-final.html` | `cases/mobilitydcat/profile/index.html` |
| `healthdcat/reference-requirements/d6.2-requirements-and-profile.pdf` | `cases/healthdcat/requirements/d6.2-requirements-and-profile.pdf` |
| `healthdcat/reference-requirements/d6.1-profile-delivery.pdf` | `cases/healthdcat/provenance/d6.1-profile-delivery.pdf` |
| `healthdcat/provenance/health-d61-deposit.json`, `health-d62-deposit.json` | `cases/healthdcat/provenance/d6.1-zenodo-deposit.json`, `d6.2-zenodo-deposit.json` |
| `geodcat/provenance/dcat-ap-1.1-later-snapshot.pdf` | `bases/dcat-ap-1.1/dcat-ap_1.1.pdf` |
| `reference-sets-v3/history/v1-comparison-2026-10-22/reference-requirements-coding.csv` | `cases/rq1-row-coding.csv` |

The three profile documents and the DCAT-AP 1.1 PDF got their upstream file names back; each was compared with the file at the upstream commit RQ1 had pinned and has the same bytes. The case READMEs and `THIRD-PARTY-NOTICES.md` were moved as well and then rewritten.

The reference sets are the RQ1 files, byte for byte:

```sh
git diff --stat 38ea671:benchmark-data/reference-sets-v3/geodcat.json HEAD:cases/geodcat/requirements/reference-set.json
```

prints nothing, for each of the five cases.

## Removed

| What | RQ1 path | Files | Why |
|---|---|---|---|
| Extraction inputs | `benchmark-data/<case>/input-raw/`, `input-preconsolidation/`, `runtime-inputs.json`, `mobilitydcat/use-cases.json` | 39 | RQ2 starts from atoms, not from source documents. This includes the DCAT-AP 2.0.0, 2.1.0 and 2.1.1 PDFs, the GeoDCAT-AP 1.0.1 PDF and the W3C DCAT pages, which were inputs and not targets. |
| Input provenance | `benchmark-data/<case>/provenance/` (manifests, citation records, gaps) | 49 | They describe the inputs. What still applies is in `benchmark.json` and the case READMEs. |
| Version-1 row files | `benchmark-data/<case>/reference-requirements/*.json` | 5 | Superseded: the version-3 sets hold all 75 rows under the same identifiers. |
| EPOS case | `benchmark-data/epos/` | 9 | Exploratory in RQ1, with no reference requirements, so nothing to generate a profile from. |
| Mock benchmark | `reference-sets-v3/mock-benchmark/` | 29 | Results of an RQ1 development exercise. |
| Build history | `reference-sets-v3/history/` | 42 | How the sets were built. One file of it was kept (see above). |
| Trace | `reference-sets-v3/trace/` | 64 | Step-by-step record of the curation. |
| Review records | `reference-sets-v3/evidence-review/`, `base-relation-review/`, `standard-form/`, `case-roles/`, and `docs/reviews/` | 15 | Their outcomes are fields of the atoms (`input_evidence`, `relation_review`, `standard_form`); the roles are in `benchmark.json`. |
| Paper material | `reference-sets-v3/supplement/`, `benchmark-data/figures/` | 16 | Tables and figures of the RQ1 paper. |
| Curation documents and tables | `reference-sets-v3/` (README, `ATOM-TYPES.md`, `INDEPENDENT-CHECK.md`, `CODEX-REVIEW-2026-10-23.md`, `atoms-review.csv`, `reference-coverage.csv`, `coverage-ledger.csv`, `counts.json`, `VALIDATION.json`), `benchmark-data/` (README, `BENCHMARK-METHODOLOGY.md`, `REFERENCE-COVERAGE-TEMPLATE.csv`, `VALIDATION-REPORT.json`), `docs/import/` | 16 | RQ1's documentation of method and checks. The definitions that RQ2 needs are summarised in [data-dictionary.md](data-dictionary.md). |
| Tooling | `tools/`, `validate_corpus.py`, `validate_v3.py` | 44 | They check or rebuild the removed material. |
| Import and export | `IMPORT-PROVENANCE.json`, `ANONYMIZATION.md` | 2 | Digests of the removed layout; instructions for an anonymous copy of the RQ1 library. |

## Added

- The published profiles and the DCAT-AP bases, fetched from their upstream repositories at pinned commits (`benchmark.json`, `tools/fetch_upstream.py`): 68 new files beside the 4 that RQ1 already held, plus the 6 unpacked shapes files of DCAT-AP 1.1.
- The three base registries RQ1's runs pin, and the 2015 PDF of DCAT-AP 1.1 behind one of them, from the RQ1 workbench (`bases/rq1-registries/`).
- Generated views of the atoms: `atoms.csv` per case and for all cases, `counts.json`, `term-check.csv` (`tools/build_views.py`).
- `SHA256SUMS` and `tools/validate.py`.
- This documentation.

## Carried over from RQ1, still true here

- The sets are merged reference sets with a provisional adjudication of the reviewed items; they are not adjudicated independently as a whole. `status` in each set says so.
- The anchor quotes of jrc-research and mobilitydcat come from live documents that are not stored.
- jrc-research and statdcat were development cases of the RQ1 workflow; outputs of healthdcat had been looked at under a restriction. This matters when atoms extracted by that workflow are used as input.
- The RQ1 library keeps curator names and upstream identifiers out of its files, for a later anonymous copy. The files added here follow that habit, but the history and the hosting account identify the project, and there is no export tool here.

## Not carried over

- The tag `ref-trace-baseline` and the trace checker that needs it.
- The branches of the RQ1 library other than `main`.
