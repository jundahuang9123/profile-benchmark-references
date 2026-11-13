# GeoDCAT-AP (`geodcat`)

Requirements for a geospatial extension of DCAT-AP, taken from the GeoDCAT-AP 1.0 specification, and that release of the profile. RQ1 role: test case. The release is confirmed; the base is the one RQ1 records and the specification is consistent with it.

## Requirements

| File | Content |
|---|---|
| `requirements/reference-set.json` | 46 rows and 56 atoms, as in RQ1 version 3 |
| `requirements/atoms.csv` | flat view of the atoms, generated |

- 37 content, 17 profile and 2 system atoms, all with the status requirement.
- Source: the GeoDCAT-AP 1.0 specification itself (`profile/geodcat-ap_1.0.pdf`): its design criteria (sections 1.1, 4.1 and 4.2) and the metadata elements it sets out to cover (Annex I and Annex II).
- The 37 content atoms each state one metadata element of INSPIRE or of the ISO 19115 core profile. Their `geo` block keeps the obligation levels and the DCAT-AP coverage the specification's tables give.
- 17 atoms restate the base (`restates_dcat_ap`): the element is already in DCAT-AP 1.1, so it adds nothing to the difference between profile and base.

## Published profile

GeoDCAT-AP 1.0 of 23 December 2015. Source: `SEMICeu/GeoDCAT-AP`, folder `releases/1.0.0`, commit `7e7d6a8` (28 April 2026); the files have not changed since the folder was created on 24 December 2020. Licence: ISA Open Metadata Licence v1.1.

| File in `profile/` | Content |
|---|---|
| `geodcat-ap_1.0.pdf` | the specification, 87 pages; the same bytes RQ1 held as `geo-final.pdf` |
| `geodcat-ap_1.0.docx` | the same specification as a Word file, kept because its tables are easier to extract |
| `README.md` | upstream release note with the licence |

- Release 1.0 has no RDF vocabulary and no SHACL shapes. Upstream publishes those from release 2.0.0 (23 December 2020) on.
- The specification defines two levels, GeoDCAT-AP Core and GeoDCAT-AP Extended (section 5), and gives the mappings as tables, with details per element in Annex II.
- Section 4.1 says that this release defines no new terms. Everything the profile adds to its base is a term reused from another vocabulary or a rule on an existing one.

## Base

DCAT-AP 1.1 ([`bases/dcat-ap-1.1`](../../bases/README.md)), as RQ1 records. The specification cites DCAT-AP as a 2015 document without a version number. It treats `dct:provenance` and `dct:accessRights` as DCAT-AP properties, and both are new in DCAT-AP 1.1. One mapping row marks `foaf:page` on a dataset as not in DCAT-AP, although DCAT-AP 1.1 added it.

## Notes

- Later releases in the same upstream repository: 1.0.1 (2 August 2016), 2.0.0, 3.0.0 (4 October 2024) and 3.1.0 (12 February 2026). They are not used.
