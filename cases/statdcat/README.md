# StatDCAT-AP (`statdcat`)

Requirements for describing statistical datasets, taken from the StatDCAT-AP 1.0.0 report, and that release of the profile. RQ1 role: development case. Release and base are confirmed.

## Requirements

| File | Content |
|---|---|
| `requirements/reference-set.json` | 22 rows and 27 atoms, as in RQ1 version 3 |
| `requirements/atoms.csv` | flat view of the atoms, generated |

- 16 content, 9 profile and 2 system atoms. 20 are requirements, 4 are guidance and 3 are deferred to future work in the source.
- Source: the StatDCAT-AP 1.0.0 report itself (`profile/statdcat-ap_version_1.0.0_0.pdf`). One document holds the working group's requirements and the profile that answers them.
- Seven rows carry the terms the report adopted in `adopted_resolution`. They are answers and stay on the evaluator's side.

## Published profile

StatDCAT-AP 1.0.0 of 15 December 2016. Source: `SEMICeu/StatDCAT-AP`, folder `Release 1.0`, commit `12a2424` (2 June 2026); the files have not changed since 14 September 2018. Licence: ISA Open Metadata Licence v1.1 (rights page of the PDF).

| File in `profile/` | Content |
|---|---|
| `statdcat-ap_version_1.0.0_0.pdf` | the report and specification, 94 pages; the same bytes RQ1 held as `stat-final.pdf` |
| `statdcat-ap_version_1.0.0_0.ttl` | RDF description of the profile, dated 22 December 2016 |
| `statdcat-ap_version_1.0.0_0.png` | class diagram |

- The Turtle file declares 26 classes and 56 properties. Each property has usage notes that give its obligation and cardinality in words, for example "Mandatory property. Cardinality [1..n]".
- The file groups properties by class in comment headings only. It has no `rdfs:domain`, so the triples do not say which class a usage note belongs to; a property used on several classes carries several notes.
- No SHACL shapes were published with 1.0.0. The DOCX and the Enterprise Architect model of the release are not copied.

## Base

DCAT-AP 1.1 ([`bases/dcat-ap-1.1`](../../bases/README.md)). Section 7.1 of the report calls the profile an extension of DCAT-AP version 1.1.

## Notes

- A later release, StatDCAT-AP 1.0.1, is in the same upstream repository. It is not used.
