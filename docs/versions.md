# Versions: which release, and why

Rule: each case uses the profile release that goes with its requirement source, as the RQ1 library froze it, and the DCAT-AP release that profile extends. A later release is never substituted. The requirements were read from documents of a given date; a later release answers later requirements as well.

Evidence levels, as in `benchmark.json`:

- **confirmed**: RQ1 records the release and the specification states it.
- **consistent**: RQ1 records the release or its source, and what RQ1 recorded about the requirements agrees with the stored files. The specification does not state the release.
- **rq1**: taken from RQ1, which is the standard here by the curator's instruction of 13 November 2026. The stored specification names a different release.

## Summary

| Case | Requirement source | Profile release | | Base | |
|---|---|---|---|---|---|
| jrc-research | workshop paper, Nov 2016 | DCAT-AP-JRC Version 1, 3 Jul 2019 | consistent | DCAT-AP 1.1 | rq1 |
| statdcat | StatDCAT-AP 1.0.0 report, 15 Dec 2016 | StatDCAT-AP 1.0.0, 15 Dec 2016 | confirmed | DCAT-AP 1.1 | confirmed |
| geodcat | GeoDCAT-AP 1.0 specification, 23 Dec 2015 | GeoDCAT-AP 1.0, 23 Dec 2015 | confirmed | DCAT-AP 1.1 | consistent |
| healthdcat | HealthData@EU D6.2, 30 Sep 2024 | pilot draft as of 20 Sep 2024 | consistent | DCAT-AP 3.0.0 | confirmed |
| mobilitydcat | NAPCORE requirement analysis v1.0, Jun 2022 | mobilityDCAT-AP 1.0.0, 16 Oct 2023 | confirmed | DCAT-AP 2.0.1 | confirmed |

## What RQ1 pins

Every run of the RQ1 workbench records the id and SHA-256 of its base registry (`base_profile_id`, `base_profile_sha256`). The run store has `dcat-ap-1.1.0` for all jrc-research, statdcat and geodcat runs, `dcat-ap-2.0.1` for mobilitydcat and `dcat-ap-3.0.0` for healthdcat. The three registries are copied to `bases/rq1-registries/` and have the recorded digests.

The terms RQ1 recorded for the requirements were looked up in the stored profiles (`cases/rq1-row-coding.csv`, and the terms named in atom notes and anchor quotes):

| Case | Coded terms found | Terms in notes and anchors found |
|---|---|---|
| jrc-research | 5 of 5 | 4 of 4 |
| healthdcat | 31 of 34 | 20 of 23 |
| mobilitydcat | 58 of 58 | 28 of 28 |

The healthdcat terms not found are `healthdcatap:reviewDate` (coded as proposed only), `csvw:Schema`, `oa:bodyText` and `oa:motivation`. They are in D6.2 and in no state of the draft from April 2024 to September 2025. The statdcat rows were coded from the report that is the profile; geodcat rows carry no terms.

## Evidence

### statdcat

- Profile. RQ1's manifest pins `Release 1.0/statdcat-ap_version_1.0.0_0.pdf` of `SEMICeu/StatDCAT-AP` at commit `12a2424`. The file fetched from that commit has the same bytes as RQ1's copy. Its title page reads Version 1.0.0, date 2016-12-15.
- Base. Section 7.1 calls the profile an extension of DCAT-AP version 1.1 and says it conforms fully to that version.

### geodcat

- Profile. RQ1's manifest pins `releases/1.0.0/geodcat-ap_1.0.pdf` of `SEMICeu/GeoDCAT-AP` at commit `7e7d6a8`. Same bytes as RQ1's copy. Every page footer reads GeoDCAT-AP v1.0, 2015-12-23.
- Base. The reference list cites DCAT-AP as a document of 2015, without a version. Annex II maps lineage to `dct:provenance` "following DCAT-AP" and says DCAT-AP recommends `dct:accessRights`; the change log of DCAT-AP 1.1 marks both properties as new. Against that, one row of the mapping table marks `foaf:page` on a dataset as not in DCAT-AP, and the same change log marks that property as new too. Two of the three signs point to DCAT-AP 1.1 and one to the release before it.

### mobilitydcat

- Profile. RQ1's manifest pins `releases/1.0.0/index.html` of `mobilityDCAT-AP/mobilityDCAT-AP` at commit `fc6cb37`. Same bytes as RQ1's copy. The header reads Version 1.0.0, NAPCORE Recommendation 16 October 2023.
- Base. Section 1.3 says the DCAT-AP version the document is based on is 2.0.1 of 8 June 2020. Annex A.2 lists what the profile adds to that version.
- The requirement source of 2022 predates the profile by 16 months and calls it napDCAT-AP. Release 1.0.0 is the first Recommendation; the document history of release 1.1.0 lists only a working draft of May 2023 before it.

### healthdcat

- Profile. D6.1 (30 April 2024) says the deliverable is published at healthdcat-ap.github.io. D6.2 (30 September 2024) says the draft is available there. The site's repository has no tags, and the date in the page's settings does not change through 2024. The copy is therefore taken by date: commit `ecabf8c` of 20 September 2024, the last on or before the date of D6.2; the next commit is of 11 October.
- How much the choice of date matters: the profile's own 14 terms are the same in every state of `index.html` from 29 April 2024 to 5 December 2024. The 24 tables are identical on 20 September and 30 October. Between 29 April and 20 September about 500 lines of the page differ. The D6.2 PDF was produced on 14 November 2024, six weeks after its cover date.
- D6.2 also recommends changes that the draft did not have yet. The shapes that separate open, protected and sensitive data were added to the repository from 26 February 2025.
- Base. D6.2 refers to DCAT-AP 3.0 throughout. The draft says its requirements are compatible with DCAT-AP 2 and with DCAT-AP 3.0.0, and shows a class diagram for each.

### jrc-research

- Profile. The 2016 paper is not redistributable. As read on 13 November 2026, it speaks of the JRC metadata schema and its core profile, an extension of DCAT-AP, and does not use the name DCAT-AP-JRC. The repository `ec-jrc/dcat-ap-jrc` starts on 2 May 2019. Its Version 1 is dated 3 July 2019 in `config.js` and has the paper's four authors. Its requirements section says part of the requirements was described in the paper. Whether the profile changed between 2016 and 2019 cannot be told from these files.
- Base. RQ1 records DCAT-AP 1.1, and its row coding compares against 1.1. The paper mentions one DCAT-AP version, 1.1, as the current one. Version 1 names DCAT-AP 1.2.1 (May 2019), GeoDCAT-AP 1.0.1 (August 2016) and StatDCAT-AP 1.0.1 (May 2019) as the specifications it is based on.
- Decision, with RQ1 as the standard: Version 1 is the profile and DCAT-AP 1.1 the base. The difference between the two then also contains what DCAT-AP gained between 1.1 and 1.2.1; a comparison has to say so. The "Spec." column of Version 1 marks which terms the profile itself introduced.

## Bases

| Base | Dated by | Date |
|---|---|---|
| DCAT-AP 1.1 | title page and footers of the PDF. The SEMIC copy has document metadata of 2017-02-24; the archived final PDF RQ1 uses (`bases/rq1-registries/dcat-ap-1.1-source/`) says 2015-10-23, status Final | 2015-10-23 |
| DCAT-AP 2.0.1 | document metadata of the PDF | 2020-06-08 |
| DCAT-AP 3.0.0 | settings of the HTML page; committed upstream on 17 June 2024 | 2024-06-14 |

## Later releases, not used

| Profile | Later than the release used here | Seen in |
|---|---|---|
| DCAT-AP-JRC | a version aligned with DCAT-AP 3, since 26 January 2024 | upstream repository, `docs/` |
| StatDCAT-AP | 1.0.1 | upstream repository, `Release 1.0.1` |
| GeoDCAT-AP | 1.0.1 (2 Aug 2016), 2.0.0 (23 Dec 2020), 3.0.0 (4 Oct 2024), 3.1.0 (12 Feb 2026) | upstream `releases/README.md` |
| HealthDCAT-AP | later states of the pilot draft, up to 5 Sep 2025; numbered releases on the European Commission's platform, which the upstream README points to (Release 5) | upstream repository; not examined further |
| mobilityDCAT-AP | 1.0.1 (4 Apr 2024), 1.1.0 (17 Jan 2025); the repository also has a tag `v3.0.0` | document history of release 1.1.0; upstream tags |
| DCAT-AP | 1.2, 1.2.1, 2.0.0, 2.1.0, 2.1.1, 3.0.1 | upstream `releases/` |

## Adding or changing a release

Every stored file is described by a source entry in `benchmark.json`: repository, commit, folder and file list. To add a release, add a source entry and a folder, run `python3 tools/fetch_upstream.py --source <id>`, then `python3 tools/validate.py --write-checksums`. The files are read from the pinned commit, so the result does not depend on the current state of the upstream repository.
