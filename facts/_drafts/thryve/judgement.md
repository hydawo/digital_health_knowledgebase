# Thryve judgement (baseline fact run)

Judge, 2026-10-21. Drafts A and B and the gap hunt are from 2026-10-11. Every quote in `facts/thryve.yaml` was re-probed
on 2026-10-21 and returned `exact`. `validate.py --file facts/thryve.yaml`: 41/41 facts researched, 0 errors.
`weekly.py --only thryve --no-state`: 0 quotes missing, 0 reworded, 2 pages changed (see the end).

Because the Fitbit cutoff is days away, the Thryve Fitbit blog, the docs source table and the Google Health integration
page were re-read in full today. None of the three had changed its dates or status wording since 2026-10-11 (blog still
"Last updated: 29 September 2026").

Coordinator update applied: Google's Health API About page no longer says it is not onboarding new projects. The record
does not say Google is closed; the Google Health export_routes entry notes route A appears open again (Corroborated,
per facts/fitbit-google.yaml).

## Disagreements between A and B, and how they were decided

| Field | A | B | Decision |
|---|---|---|---|
| research_program confidence | Verified | Corroborated | Verified for Thryve Research Partners: the vendor's own live page is the authoritative source for the program's existence. Terve gets its own entry at Corroborated because it is not live. |
| program_application, program_status confidence | Verified | Corroborated | Verified, same reasoning. |
| user_cap (Google Health) confidence | Verified | Corroborated | Verified, after adding Google's own app-verification page as a second source. |
| academic_vs_commercial, academic_pricing, soc2, rate_limits, fda_clearances confidence (not_public) | Verified | Unclear | Verified. The absence was re-checked on the listed pages today; that matches how other records (Oura, Labfront) grade not_public. |
| api_platform_fees, CASA | Folded into a note on the plans entry | Separate entry, Thryve figure only, Reported | Separate entry scoped to the Google Health route, with Google's own $500 to $4,500 range as the primary source and Thryve's "around €1,000 and upwards" labelled as Thryve's estimate. Corroborated. |
| minimum_commitment quote | "Monthly, cancel any time" (page has an em dash) | "cancellable monthly at any time" | B's, same page, avoids an em dash in the record. |
| raw_streams | One entry plus Apple Health heartbeat series and ECG | Adds ThryveBLE and a Google Health on-device entry | Merged both, plus a new Garmin Companion entry (gap C5). A's ThryveBLE quote from /wearable-api no longer appears on that page (probe "missing" today); replaced with the docs' direct Bluetooth page, which also shows ThryveBLE is in beta. |
| derived_metrics | Analytics on request | Foundational Analytics free since Dec 2025 | Both are true at different tiers; merged. |
| export_routes | Notes Google Health has no shared client | Adds m-Path JSON-in-CSV export | Merged; split Google Health's two routes into their own scoped entry. Dropped the m-Path line (an integrator's export, not a Thryve route). |
| retention_terms | Deletion from midnight UTC; configurable data types | Default deletion seven days ahead | Merged both. |
| deprecations, Fitbit | conflict, 29 vs 30 Oct | conflict, plus note on older 30 September paragraphs | conflict, with all three Thryve statements quoted (docs 29 Oct; blog header 30 Oct; same blog's "As of today, Google has not communicated an extension") and Google's own 30 Oct as a further source. Corroborated; recheck 2026-10-31. |
| deprecations, Google Health status | Not recorded | stated, with both quotes | Changed to conflict (integration page says fast-track ahead of full public release; blog says full integration released 15 August 2026). Unclear. |
| deprecations, Samsung | stated | Not recorded | Kept A's, added the SDK 5.2 reconnect quote from gap C3. |
| iso27001 | Homepage "Request Certificates" | 2025 recertification | Merged. |
| fda_clearances sources | Five openFDA queries incl. denovo | Three | Kept four, all re-run today (404 = no match). |
| Watch list | 15 incl. an openFDA URL | 13 incl. m-Path manual | 13: dropped openFDA, m-Path and the old fitbit-api-deprecation blog from the starter record; added terveresearch.com and the Garmin Companion docs page. |

## Gap findings

| Finding | Decision | Why |
|---|---|---|
| A1 Terve Research | Accepted | All three Thryve news quotes, the Huawei release quote and the three terveresearch.com quotes are exact today. Recorded as research_program and program_eligibility entries scoped to Terve. |
| A2 Terve launch status | Accepted as conflict | terveresearch.com still says "We're launching soon." on 2026-10-21; Huawei release says studies launch in September. No Terve app from mHealth Pioneers in the App Store (DE, GB, FI). Unclear. |
| A3 Research Partners route | Accepted | Same as A and B. |
| A4 Scale Up limited to startups under 10 years | Accepted | Quote exact; in api_platform_fees and the academic_vs_commercial note. |
| A5 CASA cost | Accepted, with Google primary | See table above. |
| B1 BAA and DPA every plan | Accepted at Corroborated, not Reported | The schema caps self-claims at Corroborated; it does not require Reported. |
| B2 ISO recertification 2025 | Accepted | Quote exact. |
| B3 Hosting, ISO 27017/27018, Terve on T Cloud Public | Accepted | In data_residency. |
| B4 Tokenization | Accepted | In hipaa_statement. |
| B5 not a medical device, suggest not_applicable | Partly | Kept not_public with the openFDA searches (the schema route for a negative FDA result); the "not a medical device" point is in the note. |
| C1 14-day backfill | Accepted | |
| C2 24-hour disconnect, history kept | Accepted | |
| C3 Samsung reconnect | Accepted | |
| C4 Shared OAuth clients request all scopes, shared rate limits | Accepted | In export_routes and rate_limits notes. |
| C5 Garmin Companion | Accepted, extended | The docs page now also says the customer requests a Garmin development licence through Thryve support, and the module cannot initialize without it. Whether a production or commercial licence or a Garmin fee is also needed is unstated. |
| C6 Fitbit sparse epoch data | Accepted | In sampling_rates. |
| C7 Foundation analytics free | Accepted | In api_platform_fees and derived_metrics. |
| D1 Pulsatio iOS last updated March 2023 | Accepted as a note | Confirmed via iTunes Search API today (3.9.8, 2023-03-24). |
| D2 REMIT, D3 Corona-Datenspende | Not added | Evidence of use, not a schema field. Module 3 candidates for the coordinator. |
| "No public GTC reachable" | Rejected | The site footer links the GTC PDF as "General Terms & Conditions" (checked on /pricing today), so v1.2 is still the linked terms. |

## Profile and matrix statements the record contradicts

1. `module-01-wearables/profiles/data-intermediaries.md:20`: says Google is "not onboarding new projects" on the Google Health API. Google removed that sentence between 2026-10-12 and 2026-10-19 (facts/fitbit-google.yaml); the record treats the own-project route as apparently open.
2. `data-intermediaries.md:140`: describes Thryve only as an EU health data API that publishes Fitbit analysis (Reported). Record: Research Partners program, a clinical trial platform, Terve Research, Garmin Companion module.
3. `data-intermediaries.md:166`: "Scale Up from €1,000 per month for up to 5,000 users" with no restriction. Record: Scale Up is only for startups founded less than 10 years ago, extra users €999 per 10,000.
4. `data-intermediaries.md:166`: notes only a "Data processing / Business association agreement" row. Record: BAA and DPA standard on every plan (Corroborated).
5. `data-intermediaries.md:166`: "100% GDPR and HIPAA compliant" graded Reported. Record grades the HIPAA and GDPR statements Corroborated (vendor self-claim cap).
6. `data-intermediaries.md:166`, `:239`: no mention of the 14-day default backfill or the Start Up and Scale Up 14-day cap.
7. `data-intermediaries.md:220`: links https://www.thryve.health/blog/fitbit-api-deprecation (still live). The current, more specific source is the 29 September 2026 migration post.
8. `module-01-wearables/profiles/fitbit-google.md:65` and `:262`: CASA fee $500 to $4,500 is consistent with the record; the record adds Thryve's own "around €1,000 and upwards" as Thryve's estimate only. Not a contradiction.
9. `module-01-wearables/profiles/garmin.md:38`: Garmin Companion SDK "Available to Garmin Health enterprise partners". Thryve's docs describe a Garmin development licence requested through Thryve; not a contradiction, but a route the Garmin profile does not mention.
10. `module-01-wearables/comparison-matrix.md:413`: storage windows match the record. No contradiction.

## For the coordinator

- Fitbit date conflict is inside Thryve's own pages; Google's 30 October is Verified elsewhere. The Fitbit deprecations entry has recheck_by 2026-10-31.
- weekly.py reports two "pages changed" (Google's app-verification page and Thryve's Fitbit blog) against last week's fingerprints, with every quote intact. The blog's visible date and the three date statements are unchanged; the change is probably layout or the related-posts block. Worth a glance after the cutoff.
- Terve: check again in 30 days for launch, an app listing and whether the two announced studies are recruiting.
- Garmin Companion: whether a production Garmin licence or fee applies is a vendor question.
- Certificates for ISO 27001 and 9001 are behind a request form; this needs a request by hand (not done; no forms).
