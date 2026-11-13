# Bases

The DCAT-AP releases that the profiles of the cases extend. A profile is compared with its base to find what it adds or tightens; a method that generates a profile may be given the base.

All files come from `SEMICeu/DCAT-AP` at commit `4470b8e` (16 June 2026), unchanged and under their upstream names. `benchmark.json` lists them per release; `SHA256SUMS` has their digests.

| Folder | Release | Base of | Specification | RDF description | SHACL shapes |
|---|---|---|---|---|---|
| `dcat-ap-1.1` | 1.1, title page 23 Oct 2015 | jrc-research, statdcat, geodcat | PDF | yes | yes, in two early dialects |
| `dcat-ap-1.2.1` | 1.2.1, 28 May 2019 | none as recorded in RQ1 | PDF | yes | yes |
| `dcat-ap-2.0.1` | 2.0.1, 8 June 2020 | mobilitydcat | PDF | yes | yes |
| `dcat-ap-3.0.0` | 3.0.0, 14 June 2024 | healthdcat | HTML | no | yes |

## dcat-ap-1.1

- `dcat-ap_1.1.pdf`: the specification. Its title page and footers are dated 2015-10-23 and its document metadata 2017-02-24. RQ1 notes that the bytes published in 2015 were not recovered. These are the same bytes RQ1 held as `dcat-ap-1.1-later-snapshot.pdf`.
- `dcat-ap_1.1.rdf`: one entry per term, with a label of the form "class - property" and a usage note that begins with the obligation.
- `dcat-ap_1.1.jsonld`: JSON-LD context.
- `shacl-201608.zip` and `shacl-201706.zip`: the shapes as upstream ships them. `shacl-201608/` and `shacl-201706/` hold the same files unpacked, bytes unchanged; a `.gitignore` inside the 2016 archive is left out.
- Each archive has three files: `dcat-ap.shapes.ttl`, `dcat-ap-mandatory-classes.shapes.ttl` and `dcat-ap-mdr-vocabularies.shapes.ttl`.
- The 2016 shapes follow a draft of SHACL: shapes are typed `sh:Shape` and property shapes use `sh:predicate`. The 2017 shapes use `sh:NodeShape` and `sh:path`.
- In both sets a node shape has the IRI of its class (`dcat:Dataset` is itself the shape) and no `sh:targetClass`. A tool that looks for explicit targets finds none.

## dcat-ap-1.2.1

Kept for one open point: Version 1 of DCAT-AP-JRC names DCAT-AP 1.2.1 as the release it is based on, while RQ1 records 1.1 for that case (see [cases/jrc-research](../cases/jrc-research/README.md)). The PDF, the RDF description, the JSON-LD context and three shapes files; these shapes use `sh:targetClass`.

## dcat-ap-2.0.1

- `DCAT_AP_2.0.1.pdf`: the specification. `README.md`: upstream release notes.
- `dcat-ap_2.0.1.rdf`: RDF description, built like the one of 1.1.
- `dcat-ap_2.0.1.jsonld`, `dcat-ap_lang_2.0.1.jsonld`: JSON-LD contexts.
- `dcat-ap_2.0.1_shacl_shapes.ttl`: existence, domain, range and cardinality (16 node shapes).
- `dcat-ap_2.0.1_shacl_mdr-vocabularies.shape.ttl`: use of controlled vocabularies.
- `dcat-ap_2.0.1_shacl_deprecateduris.ttl`: detects two property IRIs that 2.0.1 replaced.

## dcat-ap-3.0.0

- `index.html`: the specification as ReSpec source; a browser needs network access to render it. `CHANGELOG.md`: upstream change log.
- `context/dcat-ap.jsonld`: JSON-LD context.
- `shacl/dcat-ap-SHACL.ttl` and `.jsonld`: the SHACL template the specification links to (42 node shapes; both files hold the same graph).
- `html/shacl/shapes.ttl`: existence, domain, literal range and cardinality (17 node shapes). `html/shacl/range.ttl`: object ranges. `html/shacl/shapes_recommended.ttl`: existence of recommended properties. `html/shacl/mdr-vocabularies.shape.ttl`: use of controlled vocabularies. `imports.ttl`, `mdr_imports.ttl`, `deprecateduris.ttl`: imports and deprecated IRIs.
- The two sets of shapes are not the same graph. Which one a comparison uses is a choice to record with the result.

## Not copied

Word, OpenDocument and Enterprise Architect files, class diagrams, example records and draft folders of each release. `benchmark.json` names them per source under `not_included`. The W3C DCAT vocabulary itself is not here either.
