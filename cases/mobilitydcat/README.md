# mobilityDCAT-AP (`mobilitydcat`)

Requirements for a metadata profile for mobility data, consolidated by NAPCORE in 2022, and the first release of the profile that followed. RQ1 role: test case. Release and base are confirmed. This is the only case whose profile comes with SHACL shapes.

## Requirements

| File | Content |
|---|---|
| `requirements/reference-set.json` | 40 rows and 98 atoms, as in RQ1 version 3 |
| `requirements/atoms.csv` | flat view of the atoms, generated |

- 40 content, 47 profile and 11 system atoms, all with the status requirement. One content atom is merged into another for scoring (`Req-24.1` into `Req-19.7`).
- Source: Table 1 of *NAPCORE Requirements Analysis for a new Metadata Specification*, v1.0 (cover date 14 June 2022, final release 20 June 2022), <https://napcore.eu/wp-content/uploads/2022/08/NAPCORE-4.4.2.1-Requirement-analysis_v1.0.pdf>. Cited only: no redistribution licence was established, so there is no copy here.
- The rows keep all 40 identifiers of Table 1. Each atom's `mobility` block keeps the type and importance NAPCORE gave the row and the modal verb of its wording.
- The report calls the planned profile napDCAT-AP. That name appears in `table1_text` of the rows and in one atom statement (`Req-39.2`).
- The anchor quotes of this case were read from the live document and not checked against a stored copy (`anchor_check`).

## Published profile

mobilityDCAT-AP 1.0.0, a NAPCORE Recommendation of 16 October 2023. Source: `mobilityDCAT-AP/mobilityDCAT-AP`, folder `releases/1.0.0`, commit `fc6cb37` (5 October 2026). Licence: CC BY 4.0.

| File in `profile/` | Content |
|---|---|
| `index.html` | the specification as exported by ReSpec; style sheet and logos load from the web; the same bytes RQ1 held as `mob-final.html` |
| `mobilitydcat-ap.ttl`, `.rdf`, `.jsonld` | the vocabulary: 2 classes and 12 properties in the namespace `http://w3id.org/mobilitydcat-ap#` |
| `mobilitydcat-ap_shacl_shapes.ttl` | SHACL shapes: 14 node shapes with a target class each |
| `README.md` | upstream release note with the licence |

- The specification says that it extends DCAT-AP 2.0.1 with 2 classes and 48 properties, some of them used on several classes. The vocabulary files define the 2 classes and 12 properties that are its own.
- Upstream changed the folder after the publication date: `index.html` last on 10 November 2023, the SHACL shapes on 29 January 2024.
- The upstream repository was restructured after the pinned commit. Its main branch no longer has a `releases/` folder; the pinned commit still serves the files.

Inconsistencies in the upstream files, kept as published:

- The SHACL shapes spell one property `mobilitydcatap:intentedInformationService`. The vocabulary files spell it `intendedInformationService`; the specification has both spellings.
- The shape for the mobility data standard targets `mobilitydcatap:mobilityDataStandard`, which is the IRI of the property. The vocabulary names the class `mobilitydcatap:MobilityDataStandard`.
- The three serialisations of the vocabulary are not identical in triples: Turtle and JSON-LD parse to 675, RDF/XML to 682.

## Base

DCAT-AP 2.0.1 ([`bases/dcat-ap-2.0.1`](../../bases/README.md)). Section 1.3 of the specification says the DCAT-AP version it is based on is 2.0.1 of 8 June 2020.

## Notes

- Later releases: 1.0.1 (4 April 2024, bug fixes) and 1.1.0 (17 January 2025). They are not used.
