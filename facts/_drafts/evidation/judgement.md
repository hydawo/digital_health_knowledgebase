# Evidation: judgement (baseline run, 2026-10-11)

Final record: `facts/evidation.yaml`. 43 facts: 23 stated, 13 not_public, 5 not_applicable, 2 unclear, 0 conflict.
15 watched pages. Started fresh from A.yaml, B.yaml and gaps.md (the record was still the seeded template). All 65
quotes rechecked on their live pages on 2026-10-11 with the same fetch and `match_quote` as `quote_probe.py`; every one
came back `exact`. `validate.py --file facts/evidation.yaml`: 0 errors, 43/43 researched. `weekly.py --only evidation
--no-state`: 43 pages, 0 quotes missing, 0 reworded, 0 dead, 0 check by hand. Neither tool needed the scratch-copy
fallback.

help.evidation.com answered the project's normal fetcher (its own honest user agent, no workaround) with 200 on every
request today, so help-centre quotes were checked like any other. Where the website FAQ says the same thing, the
website page is cited instead, in case the 403s the coordinator saw come back.

## Where A and B disagreed

| Field | A | B | Decision |
|---|---|---|---|
| developer_program_status | stated, Reported: no program, but the terms mention "our API documentation" | not_public, Corroborated | **not_public, Verified.** The API clause is boilerplate in both the member terms and the November 2021 website terms; it does not show an open program. Kept apis.io as a quoted secondary source and B's note on the unresolved developer subdomains. |
| academic_vs_commercial | stated, Corroborated: academics grouped under non-profit | not_public | **A.** The non-profit page says in so many words that its offerings cover academic institutions, which is a stated fact; "no separate tier" rests on absence, so Corroborated. B's case-study list went into the note. |
| api_platform_fees | stated, "pricing model only, no prices" | not_public | **not_public** (precedent from the Activinsights judge: a value that says "not published" is not a stated fact). The pricing model went into the note. |
| subscription_price | evidationapp.com "free insights" quote | App Store "Free" plus the $10 per 10,000 points rule | **B**, better sources. |
| history_depth | unclear | stated, two scopes (30 days before connection; self-export covers the last year) | **B's two scopes, both quotes exact**, plus a third scope, Sponsor datasets, not_public, keeping A's point that the "historical" data offered to sponsors has no stated depth. A's two-week points rule dropped: it governs points, not data. |
| sampling_rates sync wording | "every 4-6 hours", website FAQ | "every 4-5 hours", help centre | **Both are right; Evidation's two pages disagree.** Website FAQ: "Data syncs happen approximately every 4-6 hours and can take up to 24 hours to appear on your account." Help article: "Data will sync approximately every 4-5 hours and can take up to 24 hours to appear on your Evidation account". Both quoted under sampling_rates (not_public). Not a `conflict` entry, because sync cadence is not the field's subject. |
| deprecations, help article date | updated 2026-04-07 | updated 2026-10-03 | **A.** The article page reads "April 07, 2026 22:09 Updated". |
| program_status | proteomics cohort; join-research shows all three studies closed | adds a March 2026 dermatology cohort, the GLP-1 release and the Research tab | Merged. The dermatology cohort is not on the newsroom page and B gave no quote for it, so it is left out. |
| soc2 | unclear (BARR badge) | not_public | **not_public.** See point 2 below. |
| licence | Verified | Corroborated | **Verified**, scoped to the licensed platform. "License Evidation's platform" states it directly. |
| data_residency | Corroborated | Verified | **Corroborated.** Every source is Evidation's own notice (follows the Activinsights and Withings judges). Added the website notice's wording, which drops "primarily". |
| raw_streams | datasets list, connected apps from the Google Fit article, EHR FAQ | full help-centre app list, "not directly from the wearable" | Merged on B's list; EHR linkage cited to the 1upHealth press release (gap 5) instead of the points FAQ. |
| retention_terms | A's three quotes | adds RESHAPE consent: archived study data is not deleted | Merged, plus gap 8's per-consent retention quote. |
| program_application | one entry | sponsor and member scopes | B's two scopes, adding A's contact-page quote. |

Smaller wording differences (spelling, which quote to lead with) were settled by taking the better-sourced entry.

## The coordinator's points

1. **Platform fields.** Licence, hosting_options and app_availability are stated for the Research & Engagement
   Platform; hosting_price is not_public. Each is scoped. Licence, hosting_options and hosting_price have a second
   entry, scope "Data licensing, insights and recruitment engagements", status not_applicable, because Evidation runs
   no software for the sponsor there. app_availability is split differently: the Evidation member app is what
   participants use in data and recruitment deals too, so it stays stated for those; a second stated entry,
   Corroborated, covers sponsor-branded apps on the licensed platform (quote: "4.6 average rating of customer apps
   that use our licensed platform"). Whether Our Future Health still runs on Evidation in 2026 is unconfirmed: a web
   search found only the November 2023 announcements, and Dr. Khan's appointment release says he came from Our Future
   Health without saying anything about the platform. This is noted under licence, app_availability and
   program_status.
2. **Compliance badges.** The our-solutions page's HTML carries these alt texts, read from the raw page: "HIPAA
   Compliant logo for Evidation", "GDPR Logo", "FDA 21 CFR Part 1 Logo for Evidation", "barr ceritfications logo",
   "cyber essentials certified plus logo", "CCPA CPRA Logo" (and a Digital Medicine Society logo). There is no text
   statement, and alt text does not appear in extracted page text, so nothing can be quoted. Decisions:
   - hipaa_statement and gdpr_statement: **unclear**, Unclear. The vendor does assert something about these two
     frameworks by name, so "not published" would be wrong; a badge gives no scope, so "stated" would be too.
   - soc2 and iso27001: **not_public**, Verified. Neither framework is named anywhere. The BARR badge names no
     framework, and reading it as SOC 2 would be a guess. Cyber Essentials Plus is in the soc2 note; a web search
     found no IASME register entry, and I did not query the register itself.
   - fda_clearances: not_public from openFDA; the badge is recorded verbatim in the note as "Part 1", probably Part 11.
   - baa and dpa: not_public.
3. **Wearable level, sampling and history.** Level and sampling are not documented (raw_streams value; sampling_rates
   not_public). Sync wording: see the table. History: B's two findings are confirmed on the pages, so history_depth is
   stated in two scopes, with A's unclear point kept as a third, not_public, scope for sponsor datasets.
4. **AI terms.** Stated, Verified: the member notice's machine-learning clause plus its "Last Updated : July 13,
   2026" line; the member-terms ban on "Artificial Intelligence Purposes"; Evidation's own foundation models; no
   published sponsor AI terms.
5. **Routes for outside researchers.** A second research_program entry, scope "Outside researchers seeking existing
   Evidation data", records exactly what each route offers: the registry codes data for "research partners" with no
   criteria; WAVE (NCT06207929; BARDA collaborator; 18,157 actual enrolment; 2024-01-21 to 2024-08-07, read from the
   ClinicalTrials.gov API) plans sharing but marks it UNDECIDED and "not yet finalized"; the July 2026 GLP-1 release
   offers data and on-demand analyses through partner@evidation.com, which is a commercial route. None is an open
   academic route.
6. **Leadership dates.** Not a schema field. See the contradictions table.
7. **Google Fit.** deprecations is stated from the help article. The App Store quote "Sync supported apps and
   wearables like Apple Health, Fitbit, Samsung Health, Google Fit, and Oura." is exact on both store listings and is
   cited as a second source, and the help-centre list is in raw_streams; the note flags the contradiction. Android
   status is not stated anywhere.
8. **quote_required.** **stated, Corroborated**, value "Yes in practice", following the MetricWire record. The two
   quotes state the contact routes (the contact page and partner@evidation.com "to discuss available data, on-demand
   analyses"); the "Yes" is inferred from no price being published, and the note says so. If the coordinator wants
   inference-from-absence to be not_public across all records, MetricWire should change too.
9. **help.evidation.com.** Not an issue today (see the top). No workaround was used.

## Gap findings

| # | Finding | Decision |
|---|---|---|
| 1 | CEO 2025-03-06, CMO 2025-12-02 | Accepted as a profile contradiction (no schema field). Both release quotes exact. |
| 2 | Our Future Health deployment | Accepted into licence, hosting_options, app_availability, gdpr_statement, dpa and data_residency notes. Both quotes exact. 2026 status unconfirmed. |
| 3 | Everyone Registry coded data to research partners | Accepted (research_program, outside-researcher scope). Both quotes exact. |
| 4 | WAVE study NCT06207929 | Accepted (same entry). Quote exact via the API `fetch_url`; enrolment, dates and collaborator read from the same JSON. |
| 5 | 1upHealth Patient Connect for EHR | Accepted (raw_streams). |
| 6 | GLP-1 cohort data plus on-demand analyses | Accepted (research_program, export_routes, quote_required, api_platform_fees note). |
| 7 | Member Privacy Notice dated 2026-07-13, ML and AI use | Accepted (ai_training_terms). |
| 8 | Retention set per study consent | Accepted (retention_terms). |
| 9 | US data centres in the member notice | Accepted (data_residency). |
| 10 | security.txt with vuln@evidation.com | Note only (soc2). It is a disclosure contact, not certification evidence. |

## A new issue for the coordinator: evidation.com's terms forbid scraping

The website Terms of Service (evidation.com/terms, "Last Updated: November 2021") bar users from using "manual or
automated software, devices, scripts robots, other means or processes to access, “scrape,” “crawl” or “spider” the
Site". The member terms have the same clause. robots.txt allows the pages in this record; it disallows only some
program and campaign paths. This is the same situation as Activinsights (see `facts/_drafts/activinsights-geneactiv/judgement.md`
point 7), where the options were (a) ask for written consent, (b) add evidation.com (and possibly help.evidation.com)
to `TERMS_BLOCKED_HOSTS` in `tools/facts/common.py` and re-check by hand, or (c) accept the risk. I did not edit
`common.py`. The weekly job would fetch about 35 evidation.com and help.evidation.com URLs each Monday.

## Profile and matrix statements the record contradicts

| File | Line | Says | Record says |
|---|---|---|---|
| module-02-digital-phenotyping/profiles/evidation.md | 9 | "a new chief executive and chief medical officer appointed in 2026" | CEO Leslie Oley Wilberforce appointed 2025-03-06; CMO Dr. Ghazanfar Khan appointed 2025-12-02 (Evidation press releases) |
| profiles/evidation.md | 12, 107 | "Sponsors deploy nothing"; "Vendor-hosted SaaS in the United States" | Partly true. Sponsors can also license the Research & Engagement Platform, which Evidation runs for them as a branded app and infrastructure, as chosen by Our Future Health in the UK (2023) |
| profiles/evidation.md | 154, 168 | International availability Unclear; "Studies outside the United States" is a poor fit | True for Evidation's own US-only member base, but the licensed platform was chosen for a UK national cohort (2026 status unconfirmed) |
| profiles/evidation.md | 97, 176 | Everyone Registry: does not say whether outside researchers can access it | Coded data are shared with "research partners" (registry page, 2025-12-18); who qualifies is not stated |
| profiles/evidation.md | 122 | The app's privacy notice was not fetched; app-specific handling Unclear | Member Privacy Notice (2026-07-13): primarily US data centres, 30 days of earlier data pulled on connection, ML and AI use for certain services, retention per study consent |
| profiles/evidation.md | 123, 174 | No HIPAA or GDPR statement on the pages fetched | Still no statement, but the our-solutions page shows HIPAA, GDPR, FDA 21 CFR Part 11 (written "Part 1"), BARR, Cyber Essentials Plus and CCPA/CPRA badges. Record: hipaa and gdpr unclear; soc2 and iso27001 not_public |
| profiles/evidation.md | 128 | Pricing through "the vendor's form" | Also partner@evidation.com, which offers existing cohort data and on-demand analyses as well as studies |
| profiles/evidation.md | 66 | Steps reach sponsors "daily and intraday minute-level, per the six-cohort paper" | Not documented by the vendor; the paper and ALiR show what some studies got, not a delivery standard |
| profiles/evidation.md | 46, 120 (matrix) | Google Fit named as a connected source | Withdrawn on iOS and the website (help article updated 2026-04-07); still named in store listings and the help list |
| profiles/evidation.md | (none) | WAVE study and BARDA funding absent | NCT06207929, BARDA collaborator, 18,157 enrolled, data sharing undecided |
| profiles/evidation.md | 94, 98 | Format, delivery and latency of sponsor data undocumented | Still undocumented; the record adds the published models (one-time extract or subscription, analysis-ready datasets, reports, on-demand analyses) |
| module-02-digital-phenotyping/comparison-matrix.md | 78 | "Vendor runs the studies on its member base; sponsors deploy nothing" | As profile line 12: licensed platform option exists |
| comparison-matrix.md | 139 | "No program on vendor pages" | Holds. Add the registry, WAVE and GLP-1 routes as limited or commercial, not academic |
| comparison-matrix.md | 163 | "No security or trust page ... compliance Unclear" | Still holds; badges exist without statements (see above) |

## Check by hand

- Whether Our Future Health still runs on Evidation's platform (the OFH app store listing's publisher, or OFH's
  current supplier pages).
- The IASME Cyber Essentials register for an Evidation certificate.
- The evidation.com terms question above, before the next Monday run.
- Android Google Fit status, which no page states.
