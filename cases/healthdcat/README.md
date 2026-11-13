# HealthDCAT-AP (`healthdcat`)

Requirements for describing health datasets for secondary use, taken from deliverable D6.2 of the HealthData@EU pilot, and the pilot's draft of the profile as it stood when D6.2 was written. RQ1 role: test case. The choice of the draft's state is open; see the end.

## Requirements

| File | Content |
|---|---|
| `requirements/reference-set.json` | 69 rows and 121 atoms, as in RQ1 version 3 |
| `requirements/atoms.csv` | flat view of the atoms, generated |
| `requirements/d6.2-requirements-and-profile.pdf` | the source: D6.2, 98 pages |

- 91 content, 11 profile and 19 system atoms. 76 are requirements, 44 are proposals and 1 is deferred.
- D6.2 gives the rationale of the profile and recommends how to develop it further. The 44 proposals (38 of them content atoms) are such recommendations. A proposal need not have a counterpart in the draft of that time: `healthdcatap:reviewDate` and `healthdcatap:qualityAnnotation`, for example, are named in D6.2 and absent from the draft.
- Source: *HealthData@EU Pilot, Deliverable 6.2, HealthDCAT-AP: Recommendations on further development and deployment for possible EU-wide uptake*, dated 30 September 2024, <https://zenodo.org/records/15085025>. The PDF file itself was produced on 14 November 2024.
- Licence: CC BY 4.0 according to the Zenodo deposit (`provenance/d6.2-zenodo-deposit.json`). The front matter of the PDF still says all rights reserved; RQ1 keeps both statements on record.

## Published profile

The pilot published the profile as a draft at healthdcat-ap.github.io, without version numbers. D6.1 and D6.2 both name that site as the place of publication. The copy here is the whole repository `HealthDCAT-AP/HealthDCAT-AP.github.io` at commit `ecabf8c` of 20 September 2024, the last commit on or before the date of D6.2. Licence: CC BY 4.0 (stated in `index.html`).

| File in `profile/` | Content |
|---|---|
| `index.html` | the draft specification as ReSpec source; a browser needs network access to render it |
| `HealthDCAT-AP 3.0.0.drawio.png`, `HealthDCAT-AP 2.1.1.drawio.png` | class diagrams, one extending DCAT-AP 3.0 and one extending DCAT-AP 2.x |
| `README.md`, `logo.png`, `Co-funded_by_the_European_Union.png` | the rest of the repository at that commit |

- No RDF vocabulary and no SHACL shapes existed at that date. Classes and properties are in 18 HTML tables with the columns property, range, cardinality, definition, usage, DCAT and reuse, the layout DCAT-AP 3.0.0 uses.
- The draft uses 14 terms with the prefix `healthdcatap:`, some spelt with varying capitalisation. Its namespace table gives no IRI for that prefix.
- The date in the page's ReSpec settings stays 22 December 2023 from April to December 2024, so it does not date the content.
- `provenance/d6.1-profile-delivery.pdf` is deliverable D6.1 (30 April 2024, 3 pages). It delivers the profile by pointing to the site. Its licence evidence is `provenance/d6.1-zenodo-deposit.json`.
- The site was taken offline on 22 September 2025 and the specification moved to the European Commission's platform, where it has numbered releases. Those are later documents and are not used.

## Base

DCAT-AP 3.0.0 ([`bases/dcat-ap-3.0.0`](../../bases/README.md)), as RQ1 records; D6.2 refers to DCAT-AP 3.0 throughout. The draft says its requirements are compatible with DCAT-AP 2 and with DCAT-AP 3.0.0.

## Open point

**Which state of the draft answers D6.2.** The options, all commits of the same repository:

| State | Commit | What differs |
|---|---|---|
| 29 April 2024, one day before the date of D6.1 | `be9853d` | Same 14 terms of its own; about 500 lines of `index.html` differ from the September state |
| **20 September 2024, copied here** | `ecabf8c` | |
| 30 October 2024, last change of `index.html` before the D6.2 PDF was produced | `7670f98` | Three class diagrams by access level replace the two by DCAT-AP version; one sentence and one example changed; the tables are the same |
| 5 September 2025, last state before the site went offline | `084e2fb` | Adds SHACL shapes for open, protected and sensitive data (uploaded from 26 February 2025) and one more term; 11 months after D6.2 |

To copy another state, change the commit and the file list of the source `healthdcat-ap-2024-09` in `benchmark.json`, run `tools/fetch_upstream.py` and then `tools/validate.py --write-checksums`.
