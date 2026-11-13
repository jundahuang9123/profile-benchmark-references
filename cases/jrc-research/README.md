# DCAT-AP-JRC (`jrc-research`)

Requirements for research-data metadata from a 2016 workshop paper of the Joint Research Centre, and the first published specification of the profile that paper describes. RQ1 role: development case. Profile and base were checked against RQ1; two limits are listed at the end.

## Requirements

| File | Content |
|---|---|
| `requirements/reference-set.json` | 11 rows and 18 atoms, as in RQ1 version 3 |
| `requirements/atoms.csv` | flat view of the atoms, generated |

- 17 content atoms and 1 system atom. 9 are requirements; 9 are issues the paper leaves open.
- Source: Perego, Friis-Christensen, Vaccari and Tsinaraki, *Using DCAT-AP for research data*, SDSVoc workshop, November 2016, <https://www.w3.org/2016/11/sdsvoc/SDSVoc16_paper_27>. Cited only: no redistribution licence was established, so there is no copy here.
- The anchor quotes of this case were read from the live page and not checked against a stored copy (`anchor_check`).
- The paper states the needs and also the terms chosen for them. Five rows carry those terms in `adopted_resolution`. They are answers and stay on the evaluator's side.
- The paper does not use the name DCAT-AP-JRC. It speaks of the JRC metadata schema and its core profile, an extension of DCAT-AP, and mentions one DCAT-AP version, 1.1, as the current one (as read on 13 November 2026).

## Published profile

DCAT-AP-JRC, Version 1, dated 3 July 2019. Source: `ec-jrc/dcat-ap-jrc`, folder `docs/1.0`, commit `c2101b0` (31 May 2024). Licence: CC BY 4.0.

| File in `profile/` | Content |
|---|---|
| `index.html`, `config.js` | the specification as ReSpec source; `config.js` holds the date, the editors and the references |
| `img/` | class diagram (PNG, SVG, XML) |
| `registers/` | four code lists published with the profile, as RDF/XML, with two HTML pages |
| `examples/` | 18 example files that the page includes; the RDF/XML ones are snippets, not complete documents |

- No RDF vocabulary and no SHACL shapes were published with Version 1. Classes and properties are in HTML tables with the columns label, obligation, maximum cardinality, RDF property, range, code list, scope and specification.
- The specification column names the specification in which a term is first defined: DCAT-AP, GeoDCAT-AP, StatDCAT-AP or DCAT-AP-JRC.
- A browser needs network access to render `index.html`, because the page loads ReSpec from w3.org. The tables can be read from the source without it.

## Base

DCAT-AP 1.1 ([`bases/dcat-ap-1.1`](../../bases/README.md)). RQ1 records it in the reference set and pins the registry `dcat-ap-1.1.0` in every run of this case.

## Checked against RQ1, and two limits

All five terms RQ1 coded for the published rows (`dct:creator`, `dct:provenance`, `vann:usageNote`, `dct:isReferencedBy`, `dct:source`) and all four terms named in atom notes are in Version 1.

1. **The profile is later than the requirements.** Version 1 was published two years and eight months after the paper. Its requirements section says that part of them was described in the paper. No artefact of the profile from 2016 was found; the repository starts in May 2019. The first published state of Version 1 is commit `a78efb7` (4 July 2019); the copy here has the editorial and ReSpec fixes made since.
2. **The profile names a later base.** Version 1 lists DCAT-AP 1.2.1 (May 2019), GeoDCAT-AP 1.0.1 (August 2016) and StatDCAT-AP 1.0.1 (May 2019) as the specifications it is based on. Measured against DCAT-AP 1.1, the difference also contains what DCAT-AP gained between 1.1 and 1.2.1. The specification column of the tables shows which terms DCAT-AP-JRC itself introduced.

A newer DCAT-AP-JRC, aligned with DCAT-AP 3, is in the same repository under `docs/`. It is not used.
