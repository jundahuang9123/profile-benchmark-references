# Data dictionary

What each file under `cases/` holds, field by field. Definitions are RQ1's; where RQ1 wrote none, this page says so.

The reference sets are the RQ1 files, unchanged. Some of their fields point at files by path (`record`, `source`, `path`). Those paths belong to the RQ1 library at commit `38ea671`, which is in this repository's history: `git show 38ea671:<path>` prints the file.

## Files

| File | Made by | Use |
|---|---|---|
| `cases/<case>/requirements/reference-set.json` | RQ1, version 3 | the full record: rows, atoms and everything known about them |
| `cases/<case>/requirements/atoms.csv` | `tools/build_views.py` | one line per atom, the fields a run or an alignment needs |
| `cases/atoms.csv` | `tools/build_views.py` | the same lines for all cases |
| `cases/counts.json` | `tools/build_views.py` | counts per case |
| `cases/term-check.csv` | `tools/build_views.py` | atom statements that carry a term or name their target profile |
| `cases/rq1-row-coding.csv` | RQ1, 22 October 2026 | earlier coding of the 75 published rows against profile terms |

A row is a requirement as the source states it, often compound. An atom is one need split from a row. Every atom belongs to exactly one row; atom identifiers are the row identifier plus a number (`H-5.3`).

## What may be shown to a method

Only `statement`. It is written in a standard form without IRIs, prefixed names or obligation words. Two system atoms name their target profile (see `term-check.csv`).

`resource`, `modality`, `status_in_source` and `stratum` contain no terms either. Whether a run passes them on is a decision of the experiment, not of this repository.

Everything else is evaluator-side. `anchor_quote`, `notes`, `source_locator`, `derived_from`, `applicability`, `table1_text`, `adopted_resolution` and the review blocks quote the profile's specification or name its terms. `relation_to_base` says how much of the answer the base already has.

## `reference-set.json`

Top level: `schema_version` (`rq1-reference-set-3`), `case`, `reference_document`, `base`, `status`, `built_from`, `decisions`, `adjudication`, `merge_rules`, `scoring`, `counts`, `requirements` (rows) and `atoms`.

### Atom fields

The requirement:

| Field | Meaning |
|---|---|
| `id`, `parent_id` | atom and its row |
| `statement` | the need in standard form: "Users can ..." for content atoms, "The profile ..." for profile atoms, the system or role the source names for system atoms |
| `statement_before_standard` | the wording before the standard form |
| `standard_form` | the parts of the sentence (`actor`, `verb`, `information`, `resource`, `scope`, `condition`, `hint`) and the record of who drafted and reviewed it; `hint` holds design choices and vocabulary names taken out of the sentence |
| `stratum` | the atom's type: `content` (information a catalogue record should carry), `profile` (how the profile is specified: principles, scope, reuse and alignment, obligation levels, code lists, documentation) or `system` (systems and processes around the profile: governance, validation, interfaces, exchange, review) |
| `status_in_source` | `requirement`, `proposed`, `deferred`, `open_issue` or `guidance` |
| `modality` | the source's own obligation wording, not normalised; the values differ per case (`mandatory`, `optional`, `capability`, `proposed_mandatory`, `source_table_obligation`, ...) |
| `applicability` | the resources or conditions the need applies to, where the source limits it |
| `mobility` | mobilitydcat only: NAPCORE's `type` and `importance` of the row and the modal verb of its wording |
| `geo` | geodcat content atoms only: INSPIRE and ISO 19115 obligation levels and the DCAT-AP coverage the specification's tables give |

Relation to the base:

| Field | Meaning |
|---|---|
| `relation_to_base` | `restates_base`, `tightens_base`, `extends_base`, `partly_base`, `beyond_base`, `not_term_level` or `unresolved`, measured against the DCAT-AP release the case cites |
| `restates_dcat_ap` | true exactly when `relation_to_base` is `restates_base` |
| `relation_review` | on the 18 atoms adjudicated on 11 November 2026: the code before, the blind review's code, the decision and the final code |
| `reuse_or_alignment_rule` | true for rules on reuse of and alignment with other vocabularies |

RQ1 has no written definition of the seven relation codes. The nearest record is the rule that derived them for the 75 published rows from the response codes of `rq1-row-coding.csv`: new class, property or code list gives `beyond_base`; existing term expanded gives `extends_base`; existing term constrained gives `tightens_base`; already in the base gives `restates_base`; no term-level response gives `not_term_level`. The review of 11 November adds one rule: an atom whose source asks more strongly than the base, or adds a condition, is `tightens_base`. `partly_base` was introduced later and has no written rule.

Identity and overlap:

| Field | Meaning |
|---|---|
| `overlaps`, `overlap_review` | atoms that state closely related needs, and the classification of each pair (`equivalent`, `subsumes`, `subsumed_by`, `related`) |
| `merged_into`, `merged_from`, `scoring_unit_rows` | an atom equivalent to an atom of another row counts once, through the canonical atom |
| `umbrella_of` | an atom that only bundles atoms counted separately |
| `split_from` | an atom split off another during adjudication |

Trace to the source:

| Field | Meaning |
|---|---|
| `source_locator` | section, table or page of the reference document |
| `anchor_quote`, `anchor_page`, `anchor_check` | the passage the atom rests on, and whether it was checked against a stored copy (`verbatim_in_source_text`) or read from the live document (`from_web_fetch_not_verified_locally`; all jrc-research and mobilitydcat atoms) |
| `derived_from`, `origin` | where the source says the need comes from; `origin` codes: `std` prior standard, `proj` project report or literature, `exp` expert or working-group deliberation, `prac` practitioner experience, `law` legal or policy text, `tech` technical considerations |
| `source_flags`, `notes` | inconsistencies in the source, recorded and not resolved; curator notes |

Curation record: `provenance` (which earlier pass found the atom), `adjudication_status`, `adjudication`, `statement_before_adjudication`, `status_in_source_before_adjudication`, `pr45_pdf_pages`.

Fields that only RQ1 needs:

| Field | Meaning |
|---|---|
| `scored_by_default` | RQ1's default selection: content atoms that are not deferred, not merged and not an umbrella |
| `input_evidence` | whether RQ1's extraction inputs support the atom, with quotes from those inputs and the adjudicated labels. The inputs are not in this repository. |

### Row fields

`id`, `statement`, `statement_kind`, `source_locator`, `level` (the row's type, as `stratum`), `status_in_source`, `relation_to_base`, `reuse_or_alignment_rule`, `origin`, `derived_from`, `atom_ids`, and `added_in` (`v1`: one of the 75 published rows; `v2`, `v3`: added in the completion passes).

`problem` is the user problem the row serves: `P1` discover, `P2` access, `P3` understand and assess, `P4` identify, link and attribute, `P5` legal and regulatory context, `P6` manage metadata records, `P7` engineer and interoperate the profile.

`adopted_resolution`, on 12 rows of jrc-research and statdcat, is the term the source itself adopted. mobilitydcat rows also carry NAPCORE's `type`, `importance` and short excerpts of Table 1 (`table1_text`); geodcat rows carry the obligation levels of the specification's tables.

## `atoms.csv`

One line per atom. Every value is copied from the reference set; nothing is reworded.

| Column | From |
|---|---|
| `case`, `atom_id`, `row_id` | file, `id`, `parent_id` |
| `stratum`, `statement`, `status_in_source`, `modality`, `applicability` | the fields of the same name |
| `resource` | `standard_form.resource`: the kind of resource a content atom is about (`dataset`, `distribution`, `catalogue record`, `service`, `resource`); empty for profile and system atoms |
| `relation_to_base`, `restates_dcat_ap`, `reuse_or_alignment_rule` | the fields of the same name |
| `scored_by_default` | RQ1's default selection |
| `merged_into`, `umbrella_of`, `overlaps` | the fields of the same name; several atoms are joined with `;` |
| `source_locator` | the field of the same name |

## `counts.json`

Per case: `reference_document`, `base`, `rows`, `atoms`, atoms by `stratum`, by `status_in_source` and by `relation_to_base`, the number of atoms that restate the base and of reuse or alignment rules, and RQ1's default selection with and without restatements. `all` sums the cases.

## `term-check.csv`

The atom statements that fail one of two checks. `iri_or_prefixed_name`: the statement contains `http://`, `https://`, `urn:` or a prefixed name. `own_profile_name`: the statement contains a name of the case's target profile. No statement fails the first check; two fail the second.

## `rq1-row-coding.csv`

A coding of the 75 published rows (the `v1` rows) made in RQ1 on 22 October 2026, before the rows were split into atoms. It is the only record in the RQ1 library that links requirements to the profile terms that answer them.

| Column | Meaning |
|---|---|
| `id`, `case`, `statement_curator_paraphrase`, `source_locator` | the row as it stood then; the statement of `H-3` has since been corrected in the reference set |
| `level`, `problem`, `derived_from` | type, user problem and origin of the row, written out |
| `response`, `response_group` | how the profile answers the row: new class or property (minted or imported), new code lists, existing term expanded or constrained, already in base, no term-level response, proposed or not addressed |
| `terms` | the profile terms that answer the row, as `term [class] (kind)`, separated by `;`. Kinds: `new, minted`; `new, imported`; `existing, on a new class`; `existing, constrained`; `existing, as is`; `code list extended`; `proposed only`; `not covered` |
| `confidence`, `note` | the coder's confidence and remark |
| `items_in_row`, `reuse_or_alignment_rule`, `napcore_*` | number of needs in the row, reuse rule flag, NAPCORE's own labels |

Limits: one AI coder (Claude), whose model and prompt RQ1 records as not recorded; no review by a person; 75 of the 188 rows, and rows rather than atoms; 45 rows name terms (106 entries) and none of the geodcat rows does. It is starting material for an alignment of atoms to profile elements, not gold.

## The atom contract of the generation prototype

The prototype's input contract asks for `id`, `statement`, `subject`, `modality` (`must`, `should`, `may`, `unspecified`) and a source reference. What the reference sets offer for each:

| Contract field | In the reference set | Open |
|---|---|---|
| `id`, `statement` | `id`, `statement` | nothing; all 320 statements pass the contract's pattern |
| `subject` | `standard_form.resource` | filled for the 201 content atoms and empty for the 119 profile and system atoms; nine values name two resources ("dataset or service", "dataset or distribution") |
| `modality` | `modality`, `status_in_source` | the source wordings are not normalised to must, should and may; a mapping has to be decided |
| source reference | `reference_document`, `source_locator` | for statdcat, geodcat and healthdcat the locator points into a document that also specifies the target profile |
