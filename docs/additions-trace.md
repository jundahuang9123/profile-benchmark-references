# Do the profiles' additions stem from the requirements?

Two questions per case, answered on 14 November 2026:

1. Is the stored profile the original profile built from this requirement source?
2. Does each addition the profile makes to its base trace back to a requirement atom?

An addition is a class or property the profile adds to its base release, or an obligation it raises above the base. GeoDCAT-AP defines no terms, so its additions are its bindings: the terms it assigns to INSPIRE and ISO 19115 elements. The tables are in [`analysis/additions/`](../analysis/additions/), one row per addition, with the atoms it traces to and the reason.

## Summary

| Case | Original profile for this source? | Additions | Traced to an atom | Traced only through a profile-level rule or as a supporting term | Not from the requirements |
|---|---|---|---|---|---|
| statdcat | Yes | 6 | 6 | 0 | 0 |
| geodcat | Yes | 24 | 24 | 0 | 0 |
| mobilitydcat | Yes | 69 | 37 | 11 | 21: 17 taken from GeoDCAT-AP 2.0.0, 4 untraced |
| healthdcat | Yes, but the source was written after the profile | 51 | 38, plus 6 partly | 0 | 7 untraced |
| jrc-research | Partly: the profile is a later, extended edition | 71 | 38 | 0 | 33: 24 answer requirements the paper does not have, 9 have no requirement |

## Categories

| Category | Meaning |
|---|---|
| `traced` | A content atom asks for what the addition provides. |
| `partly` | An atom asks for it in a narrower scope; the profile applies it more widely. |
| `supporting` | A property of a class the profile adds for a traced need, such as the date of an assessment. |
| `profile_rule` | Only a profile-level atom covers it, for example "consider all CMC metadata elements". |
| `inherited` | Taken from another profile the specification names as a starting point; no atom asks for it. |
| `other_requirement` | The specification links it to a requirement of its own that is not in the reference source. |
| `untraced` | Neither an atom nor the specification gives a requirement for it. |

The tracing was done by reading the atom statements against each addition's definition and usage note. RQ1's row coding (`cases/rq1-row-coding.csv`) and the terms named in atom notes were used as a first pass. The decisions are Claude's reading and have not been reviewed by a person; the `note` column gives the reason for each.

## Per case

### statdcat: yes, and all six additions trace

StatDCAT-AP 1.0.0 is the first release, and the requirement source is its own development report. Section 7.2 names each extension next to the requirement that led to it: `stat:dimension`, `stat:attribute`, `dqv:hasQualityAnnotation`, `dct:type` on Distribution, `stat:numSeries` and `stat:statUnitMeasure` (atoms S-1 to S-6). The report raises no obligation of DCAT-AP 1.1.

Limit: requirements and profile come from the same document, so the trace confirms the report's own account rather than an independent one.

### geodcat: yes, and all 24 bindings trace

GeoDCAT-AP 1.0 is the first release, and its requirements are its own design criteria and the INSPIRE and ISO 19115 elements it sets out to cover. Every binding in Table 2 (Core) and Table 3 (Extended) that goes beyond DCAT-AP 1.1 answers one of those elements, and each element is an atom. Four bindings give a new use to a property DCAT-AP 1.1 already has, such as `dct:conformsTo` for the coordinate reference system.

Same limit as statdcat: one document holds both.

### mobilitydcat: yes, but a third of the additions do not come from the requirements

The specification presents itself as the initial release built on preparatory work, of which the requirement analysis is the first step. That analysis is a separate document from 2022, so this is the only case where requirements and profile are independent.

- **37 traced**, including all of the profile's own `mobilitydcatap:` terms except two.
- **6 through a profile-level rule.** `applicationLayerProtocol` and `communicationMethod` are elements of the Coordinated Metadata Catalogue (Annex B), and the requirements ask the profile to consider all of them (Req-11.1, Req-16.1). The other four rest on general rules: identifiers (Req-33.1) and distributions described in detail (Req-2.6).
- **5 supporting**: the properties of the Assessment and Quality Annotation classes, and `skos:inScheme` on a category.
- **17 inherited from GeoDCAT-AP 2.0.0**: contact details for agents (`foaf:phone`, `foaf:workplaceHomepage`, `org:memberOf`, `locn:address`), the Address class with its five properties, and six `vcard:` properties of Kind. The change log says the document was written starting from DCAT-AP 2.0.1 and GeoDCAT-AP 2.0.0; Req-12.1 asks only to consider existing extensions. `foaf:mbox` is also raised to mandatory, which neither source asks for.
- **4 untraced**: `foaf:firstName`, `foaf:surname`, and mandatory `foaf:homepage` and `dct:spatial` on the catalogue.

### healthdcat: yes, but the source was written after the profile

The draft was designed by the pilot's technical working group in 2023 and delivered in April 2024 (D6.1). D6.2, the requirement source, is dated September 2024. Its methodology section reports the requirements the working group identified, and section 5.2 says the new properties were introduced to address them. So D6.2 records the requirements of this profile, but after the fact; 44 of its atoms are proposals for further development.

- **38 traced**: all 18 of the draft's new health, privacy and quality properties (`healthdcatap:`, `dpv:`, `dqv:`), and 20 of the 26 obligations it raises.
- **6 partly**: the requirement concerns datasets and the draft also makes the property mandatory for catalogues, series or distributions (applicable legislation, temporal coverage), or makes a sample mandatory for every dataset where D6.2 asks it for non-public ones; `dcat:isVersionOf` against a requirement for version designation.
- **7 untraced**: `dct:alternative`, the DCAT 3 series navigation properties (`dcat:prev`, `dcat:next`, `dcat:first`, `dcat:last`, `dcat:seriesMember`) and a recommended `dcat:inSeries`.

The draft also lowers three obligations of DCAT-AP 3.0.0 (description of a dataset series and of a distribution, availability of a distribution); these are not additions and are left out of the table.

In the other direction, 34 of the 78 Health content atoms that ask for more than the base have no counterpart in the draft, among them the data dictionary in CSVW, the EHDS quality label and intellectual-property rights. This matches D6.2's role as a recommendation for further development.

### jrc-research: partly; many additions come from requirements the paper does not state

The 2016 paper describes the requirements of the JRC metadata profile then in use. Version 1 (2019) has its own requirements section, which says that part of its requirements was described in the paper, and every property table names the requirement the property serves. Seven of its sixteen requirement sections correspond to the paper's atoms. The other nine (catalogue endpoints, dataset collections, other resources, acronyms, dataset status, the dataset–catalogue relation, access restrictions, contributors' order, spatial code lists) do not appear in the paper.

- **38 traced**, by the specification's own requirement links to the seven sections that match the paper: authors and their names and identifiers, usage notes, publications and their bibliographic properties, identifiers, distribution type and function, data policy.
- **24 answer other requirements of Version 1**: everything about endpoints and other resources, collection identifiers, acronyms, `adms:status`, `dct:isPartOf` to the catalogue and access restrictions on distributions.
- **9 without a requirement link**: the name, acronym, home page and parent of an organisation, email and page of a contact point, `dc:publisher` on a publication, and status and identifier of a catalogue record.

Measured against the 2016 requirements, about half of Version 1's additions are not derived from them. This adds to the limits already recorded for this case.

## What this means for the benchmark

- statdcat and geodcat: every addition is grounded, but by the same document that states the requirements, so the benchmark tests whether a method recovers what the authors wrote down as the reason.
- mobilitydcat is the cleanest independent case. A reference delta should keep the 17 inherited GeoDCAT-AP additions and the 4 untraced ones apart, or a method is scored against additions no requirement asks for.
- healthdcat: the 7 untraced additions and the 6 partly traced ones need the same treatment. The 34 unanswered atoms show that the requirement set is larger than the profile.
- jrc-research: scoring Version 1's full delta against the paper's atoms would count 33 additions that the paper cannot motivate.

Splitting the reference delta by these categories is a decision for the experiment; the tables give what is needed to do it.
