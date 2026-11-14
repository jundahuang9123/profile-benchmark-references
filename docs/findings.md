# Findings

Everything found while building and checking this repository (13–14 November 2026), in one list. Each item links to the page with the details and evidence. The checks are Claude's work and have not been reviewed by a person.

## Versions and bases

Details: [versions.md](versions.md), [bases/README.md](../bases/README.md).

1. Every profile release is the one that goes with the requirement source RQ1 froze. The base of each case is the one RQ1's runs pin (`base_profile_id`): DCAT-AP 1.1 for jrc-research, statdcat and geodcat, 2.0.1 for mobilitydcat, 3.0.0 for healthdcat. The three registries in `bases/rq1-registries/` have the digests the runs record.
2. The terms RQ1 coded for the requirements are in the stored profiles: jrc-research 5 of 5, mobilitydcat 58 of 58, healthdcat 31 of 34. The 3 Health terms missing are in D6.2 but in no state of the draft from April 2024 to September 2025.
3. jrc-research: the requirements are from a 2016 paper, the earliest public specification is Version 1 of July 2019, and nothing from 2016 was found. Version 1 names DCAT-AP 1.2.1 as its base, while RQ1 uses 1.1, so a delta against 1.1 also holds what DCAT-AP gained up to 1.2.1.
4. healthdcat: the draft has no version numbers and is taken by date (20 September 2024). Its tables are the same on 30 October 2024. Its first SHACL shapes date from February 2025.
5. DCAT-AP 1.1: the PDF the SEMIC repository serves has 2017 document metadata; RQ1 uses the archived 2015 final PDF. The SEMIC 1.1 shapes declare version 1.2 and have no `sh:targetClass`; the 2016 set uses a draft of SHACL, the 2017 set `sh:NodeShape` and `sh:path`.
6. RQ1's DCAT-AP 3.0.0 registry models the 15 main classes only and lacks `time:hasBeginning`, `time:hasEnd` and `dct:isPartOf` on Catalogue; used alone, it makes supporting classes look like additions.

## Origin of the profiles and their additions

Details: [additions-trace.md](additions-trace.md), tables in [`analysis/additions/`](../analysis/additions/).

7. statdcat and geodcat: the profile is the first release, built from the requirements in its own document. All additions trace (6 of 6, 24 of 24 bindings). Because one document holds both, this confirms the authors' own account, not an independent one.
8. mobilitydcat: the first release, built after the independent 2022 requirement analysis. Of 69 additions, 37 trace to content atoms and 11 more only through a general requirement or as a supporting property. 17 are taken from GeoDCAT-AP 2.0.0, which the change log names as a starting point. 4 have no source.
9. Two Mobility additions, `applicationLayerProtocol` and `communicationMethod`, are elements of the Coordinated Metadata Catalogue (CMC) that no content requirement asks for. Req-11.1 tells the profile to consider all CMC elements.
10. healthdcat: the draft was designed from the working group's 2023 requirements and delivered in April 2024. D6.2 reports those requirements in September 2024, after the draft, and adds 44 proposals. Of 51 additions, 38 trace, 6 trace in a narrower scope and 7 have no source (alternative title and the DCAT 3 series properties). The draft also lowers three obligations of DCAT-AP 3.0.0.
11. In the other direction, 34 of the 78 Health content atoms that ask for more than the base have nothing in the draft, among them the CSVW data dictionary, the EHDS quality label and intellectual-property rights.
12. jrc-research: Version 1 links each property to one of its own 16 requirement sections; 7 correspond to the paper. Of 71 additions, 38 trace to the paper, 24 answer Version 1 requirements the paper does not have (endpoints, collections, other resources, acronyms, status and more), and 9 have no requirement.
13. For the benchmark: reference deltas for mobilitydcat, healthdcat and jrc-research should keep inherited and unsourced additions apart, or a method is scored on additions no requirement asks for. Whether to split them is open.

## Machine-readable form of the profiles

Details: the case pages under [cases/](../cases/).

14. At the frozen versions, only mobilityDCAT-AP 1.0.0 has SHACL shapes. StatDCAT-AP 1.0.0 has an RDF description whose usage notes give obligation and cardinality in words, with no `rdfs:domain`. GeoDCAT-AP 1.0, the Health draft and DCAT-AP-JRC Version 1 exist only as tables, so their deltas have to be built from those tables.
15. mobilityDCAT-AP 1.0.0 upstream inconsistencies: the SHACL shapes spell `intentedInformationService` where the vocabulary has `intendedInformationService`; one shape targets the property IRI `mobilityDataStandard` instead of the class; the three serialisations of the vocabulary differ in triple count.
16. The Health draft uses the prefix `healthdcatap:` for 14 terms without giving its namespace IRI, and spells some of them with varying capitalisation (`dqv:hasQualityannotation`).
17. DCAT-AP-JRC Version 1 is ReSpec source; its example files are snippets that do not parse on their own. Its tables mark which specification each term comes from and which requirement it serves.

## Requirement atoms as input

Details: [data-dictionary.md](data-dictionary.md), [`cases/term-check.csv`](../cases/term-check.csv).

18. No atom statement carries an IRI or a prefixed name. Two system atoms name their target profile: G-46.1 and Req-39.2.
19. Several other atom fields quote the profile or name its terms (`anchor_quote`, `notes`, `adopted_resolution`, `table1_text` and others), so only `statement` is safe to show a method.
20. For the prototype's atom contract: `subject` can be filled from `standard_form.resource` for the 201 content atoms only, and `modality` needs a mapping from the sources' own wordings to must, should and may.
21. RQ1's row coding (`cases/rq1-row-coding.csv`) is the only record linking requirements to answering terms. It covers 75 of 188 rows, works on rows rather than atoms, was made by one AI coder and has no geodcat terms.
