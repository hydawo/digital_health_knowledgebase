# mindLAMP: judgement, 2026-10-11

Inputs: `A.yaml`, `B.yaml`, `gaps.md`, and the starter `facts/mindlamp.yaml` (all `unresearched`). Output: `facts/mindlamp.yaml`, 39 entries (24 stated, 11 not_public, 2 not_applicable, 2 conflict), 15 watched pages. All 91 quotes matched "exact" with `quote_probe.py` on 2026-10-11. `validate.py --file facts/mindlamp.yaml`: 0 errors, 39 of 39 researched. `weekly.py --only mindlamp --no-state`: 48 pages, 0 quotes missing, 0 reworded, 0 dead, 0 validation errors. Both ran against the real repo; the scratch copy was not needed, because the other records being edited did not break either script. GitHub issues and PRs were read only, through the API and web pages.

## Fields where A and B disagreed

| Field | A | B | Decision and reason |
|---|---|---|---|
| Get Started fetch_url (many fields) | Docusaurus chunk `bf7df328.1cccf923.js` | `src/pages/get-started.tsx` (raw) | The repo source file. I downloaded both and checked every FAQ quote against each. All were present in both, so the source file's text matches the deployed page. The chunk's hashed name changes on every rebuild, which would break the weekly check. |
| Confidence on not_public fields | Unclear | Verified | Verified, as in the committed Beiwe and RADAR-base records: "not published" is a dated, checked observation. |
| history_depth | stated, Corroborated | unclear | stated, Corroborated. The API reference does document arbitrary from/to timestamps and a 1,000-entry page. The value says "no look-back limit is documented" and adds B's two unknowns (hosted retention, HealthKit first-sync depth). |
| rate_limits | stated, Reported (adds `rateLimitMax: 1000` from unreleased server code) | stated, Verified (page size only) | stated, Verified on the documented page size. A's code finding goes in the note, with the source kept and quoted. It is Reported only, because the code is merged but not released. |
| retention_terms | stated, Verified (Play label in note) | conflict, Unclear | conflict, Unclear, widened to three sources: the live 90-day promise, the Play "Data can't be deleted" label, and the maintainers' own correction in open PR 939 (gap 3). I opened the PR and its draft text, and every quote is exact. |
| licence | One unscoped conflict, Verified | Three scoped entries (dashboard stated; SDKs stated; server and apps conflict, Unclear) | B's per-component split, as the coordinator asked, with A's extra sources (LAMP-js licence, server repo). Licence states rechecked with the GitHub API. Dashboard relicensing commit 8e6ad0f0 is dated 2026-08-05. |
| deprecations | One entry: auth upgrade, sensors, v1 app, relicensing | One entry: sensors, v1, Cortex features, Data Portal | Two scoped entries. Authentication upgrade (A plus gap 9 plus the coordinator's points). Sensor identifiers and legacy components (B). Relicensing moved out to `licence`, since it is not a deprecation. |
| app_availability | One combined entry | Two scoped entries (iOS, Android) | B's two scopes, plus A's Get Started quote and the developer name on both listings. |
| hosting_options | configure page plus AWS blog | BIDMC services page plus Docker Swarm | Merged. The newest server release (2023.7.27) and the draft status of the self-hosting docs are added. |
| data_residency | Corroborated, AWS blog (aws.amazon.com) | Verified, aws-news.com aggregator | Corroborated, citing the AWS blog itself. The aggregator was dropped because it is a summary of the original. The stack evidence is a secondary source. |
| program_status | Cites the auth blog and the LAMP-server repo | Forum NXDOMAIN | Merged, plus PR 930 for the retirement of the consortium (gap 8). I confirmed the NXDOMAIN myself. Site-count disagreement goes in the note only (coordinator point 7). |
| research_program, program_eligibility, program_application, developer_program_status, api_platform_fees, quote_required, raw_streams, derived_metrics, sampling_rates, export_routes, hosting_price (both scopes), hipaa_statement, gdpr_statement, baa, dpa, iso27001, soc2, fda_clearances, ai_training_terms, user_cap, academic_vs_commercial, minimum_commitment, academic_pricing | Agreed in substance | Agreed in substance | Merged quotes and detail from both. Self-hosting cost kept at Reported, since the docs page is an unpublished draft. |

## Gap hunter findings

| Finding | Decision | Why |
|---|---|---|
| 1. Docs privacy page makes a HIPAA safeguards claim; July 2025 pen test | Accepted (hipaa_statement, Corroborated) | Quotes exact. Self-claim cap applies. |
| 2. Licence: "no licensing restrictions" vs unlicensed repos; issue 943 unanswered | Accepted (licence, three scopes) | Issue 943 opened 2026-07-22, 0 comments, open (API). One correction: the dashboard relicensing date is 2026-08-05 (commit 8e6ad0f0 and release 2026.08.05). 2026-08-25 is the date of the 2026.08.05.2 release note that mentions it. LAMP-worker is unlicensed per the API. LAMP-platform, LAMP-data-reports, LAMP-raphe and LAMP-oauth-server are not in the scoped list, since they are not runtime components a study deploys. |
| 3. Deletion: the maintainers' PR 939 calls the 90-day claims inaccurate | Accepted (retention_terms conflict) | PR 939 is open, unmerged, by MattMatt27, opened 2026-03-16. Its title is "Update Security & Privacy Policy page", and the body has "Fix inaccurate data deletion claims". Draft branch text quoted. |
| 4. Audit logging claimed while issue 910 and LAMP-server PR 264 are open | Accepted (hipaa_statement value and note) | Both open per the API. Correction: PR 264 is titled "910 changes". "Add Basic Audit Logging" is the title of issue 910. No schema field fits exactly, so it went under hipaa_statement, whose value lists audit logs. |
| 5. Cortex is not legacy; RAPHE | Accepted, partly (derived_metrics note) | Cortex BSD-3-Clause, pushed 2026-05-18, and central in current docs. RAPHE repo created 2026-09-29, with no licence per the API. Its README text was not quoted. |
| 6. Four different scale figures | Note only (program_status) | Not a decision fact, as instructed. Core "50+", AWS "65 sites, 42 projects, 17 countries" and the gallery's "36 Projects", "16 Countries", "9 Active" all seen on the live pages. |
| 7. Text features iOS SensorKit only; no Android call-log or SMS permission | Accepted (raw_streams) | Telephony quote exact. I read the manifest on master: READ_PHONE_STATE only, no READ_CALL_LOG or READ_SMS. The Health Connect permission-removal detail (7c) was not checked and is not in the record. |
| 8. Consortium retired; forum archived | Accepted (program_status) | PR 930 quote exact, merged. Forum NXDOMAIN confirmed by `host`. PR 891 named in the note without a quote. |
| 9. Authentication upgrade | Accepted (deprecations, Authentication upgrade) | Blog quotes exact. PR 284 merged 2026-09-30 from `zagaran/auth-refactor`. Newest server release 2023.7.27 (2023-07-27). |
| 10. Released server is from 2023 | Accepted (deprecations, hosting_options) | Release list read from the API. Dashboard production-branch details not used. |
| 11. Named outside deployments (Mount Sinai, McLean, Army Level Up) | Rejected for the record | Not needed for any field, and not opened. Worth a profile line if wanted. |
| 12. Survey branching inert at run time | Accepted (raw_streams note, with quoted source) | Release 2026.08.05.3 quote exact. No schema field fits. |
| 13. iOS TestFlight builds; App Store still 2023 | Accepted (app_availability iOS) | Issue 944 shows TestFlight builds 2025.4.2 (509 and 511). The iTunes lookup gives 2023.5.2 released 2023-05-26, seller John Torous. The contractor names (Zco, Zagaran) are left out of the record. |
| 14. Amazon Research Award; NIH DIGITS grant; job posting | Rejected for the record | No schema field. The grant abstract does not name mindLAMP. |
| 15. BIDMC hosting on ECS Fargate and DocumentDB | Accepted (hosting_options, data_residency) | AWS blog quotes exact. Region not stated anywhere I read. |

## Coordinator's points

1. Licence: three scoped entries. Dashboard AGPL-3.0-only since 2026-08-05 (stated). Cortex and SDKs BSD-3-Clause (stated). Server, iOS and Android apps, LAMP-activities and LAMP-worker are a conflict, Unclear: no licence file, the privacy page says "no licensing restrictions", and issue 943 is unanswered.
2. Deletion: one conflict entry. It records the live 90-day terms, the Play label and PR 939's correction, each with exact quotes.
3. Authentication: its own deprecations entry. Mandatory 2FA or OAuth for staff, API keys for LAMP-py, password scripts stop working, merged 2026-09-30, not released, newest release 2023.7.27.
4. Audit logging: under hipaa_statement, with issue 910 and PR 264.
5. Hosting: shared or dedicated on BIDMC AWS (ECS Fargate, DocumentDB, region not stated), or self-hosting. Self-hosting costs kept at Reported.
6. Get Started: every FAQ quote now uses `raw.githubusercontent.com/.../src/pages/get-started.tsx` as fetch_url. The text was checked against the live chunk.
7. Site counts: note only.
8. Consortium and forum: program_status. The interest form is the only route in (program_application).
9. SensorKit-only text features, no Android call-log or SMS permission, branching inert: raw_streams.
10. iOS 2023.5.2 and TestFlight-only newer builds; John Torous as developer on both stores: app_availability.

## Statements in the profile or matrix that the record contradicts

| File | Line | What it says | What the record says |
|---|---|---|---|
| module-02-digital-phenotyping/profiles/mindlamp.md | 11, 93, 134, 153 | Server and both apps unlicensed; dashboard AGPL-3.0 | Consistent. LAMP-activities and LAMP-worker are also unlicensed. The vendor's privacy page claims "no licensing restrictions" and issue 943 is unanswered; the profile has neither. The dashboard licence is AGPL-3.0-only from 2026-08-05 |
| module-02-digital-phenotyping/profiles/mindlamp.md | 27, 39 | "LAMP-cortex (legacy)" with LAMP-toolkit as its successor | Cortex is the current, documented analytics layer (BSD-3-Clause, maintained) |
| module-02-digital-phenotyping/profiles/mindlamp.md | 77 | Derived metrics "Not verified in any pass to date" | Cortex primary and secondary features documented (derived_metrics) |
| module-02-digital-phenotyping/profiles/mindlamp.md | 48 to 67 | Most streams "Unclear"; gyroscope a separate stream; calls Android "Yes"; SMS "Unclear"; GPS raw "Unclear"; sampling "Unclear" | 9 phone sensors and 10 HealthKit or Health Connect types documented. Gyroscope and magnetometer folded into device_motion. Android has call-state only, with no call-log or SMS permission. Text features are iOS SensorKit only. GPS raw and unhashed. Accelerometer 5 Hz and GPS 1 Hz, configurable through the API |
| module-02-digital-phenotyping/profiles/mindlamp.md | 55 | Steps, sleep and heart rate "from a paired wearable" | Wearables are reached only through HealthKit or Health Connect; "mindLAMP does not connect directly to wearable devices" |
| module-02-digital-phenotyping/profiles/mindlamp.md | 81 | Branching sophistication not benchmarked | Survey branching is configurable but inert at run time (dashboard release 2026.08.05.3) |
| module-02-digital-phenotyping/profiles/mindlamp.md | 89 | Data access and export not verified | REST API, Python and JS SDKs, R via reticulate, JSONata, Cortex, Data Portal; 1,000 entries per request |
| module-02-digital-phenotyping/profiles/mindlamp.md | 97, 112 | Core offers audit logs; no caveat | Request-level audit logging is an open work item (issue 910, PR 264 unmerged) |
| module-02-digital-phenotyping/profiles/mindlamp.md | 97, 183 | "50+ active sites" | Figures vary: 65 sites in 17 countries (AWS blog), 36 projects in 16 countries (docs gallery) |
| module-02-digital-phenotyping/profiles/mindlamp.md | 98 | LAMP-server "actively maintained" | Commits are active, but the newest release is 2023.7.27. The authentication rewrite was merged 2026-09-30 and is unreleased |
| module-02-digital-phenotyping/profiles/mindlamp.md | 112, 155 | Privacy page makes no HIPAA, SOC 2 or GDPR claim (checked digitalpsych.org) | docs.lamp.digital/privacy claims HIPAA Security Rule safeguards and reports a July 2025 pen test. The architecture docs claim HIPAA, COPPA and GDPR compliant encryption. All are self-claims (Corroborated) |
| module-02-digital-phenotyping/profiles/mindlamp.md | 104 to 114 | Nothing on deletion or retention | 90-day soft delete published, contradicted by the Play label and by the maintainers' open PR 939 |
| module-02-digital-phenotyping/profiles/mindlamp.md | 157 | Open question: is a newer iOS build distributed another way? | Yes: 2025.4.2 builds through TestFlight for testers only (issue 944) |
| module-02-digital-phenotyping/profiles/mindlamp.md | 166, 176, 179 | Publications link dead; forum DNS failure, no explanation | Consortium and publications/users pages removed in PR 930 (October 2025); forum archived for lack of use (PR 891) |
| module-02-digital-phenotyping/profiles/mindlamp.md | (absent) | Nothing on the authentication upgrade | Mandatory staff 2FA or OAuth and API keys for LAMP-py; password scripts will stop working on release |
| module-02-digital-phenotyping/comparison-matrix.md | 30 | Licence column lists server and apps as unlicensed | Consistent; add LAMP-activities and LAMP-worker, and the vendor's "no licensing restrictions" claim |
| module-02-digital-phenotyping/comparison-matrix.md | 49 | iOS "Unclear" for parity; App Store build from 2023 | iOS build note now explained (TestFlight only). The per-OS split is now documented (see raw_streams) |
| module-02-digital-phenotyping/comparison-matrix.md | 96 | Branching depth "not benchmarked" | Branching is inert at run time |
| module-02-digital-phenotyping/comparison-matrix.md | 113 | Streams "without a per-OS breakdown"; wearable devices not itemized | Per-sensor docs exist; wearables only through HealthKit or Health Connect; text features iOS SensorKit only |
| module-02-digital-phenotyping/comparison-matrix.md | 156 | "No HIPAA, SOC 2 or GDPR claim" | HIPAA and GDPR self-claims exist on docs.lamp.digital (Corroborated); no SOC 2 |
| module-02-digital-phenotyping/comparison-matrix.md | 156, 178 | Core includes audit logs | Unconfirmed in the code record (issue 910, PR 264 open) |
| module-02-digital-phenotyping/comparison-matrix.md | 178 | "Core claims 50+ active sites" | Figures vary by source (see above) |

## For the coordinator to check by hand

- **PR 939 draft branch.** The retention conflict cites the draft file on branch `docs/update-security-privacy-policy`. When the PR merges, the branch may be deleted and those two sources will go dead. Re-read the live privacy page then and resolve the conflict.
- **Server release.** Once a LAMP-server release after 2023.7.27 appears, update deprecations (Authentication upgrade), rate_limits (the API-key cap becomes live) and hosting_options.
- **Licence.** Issue 943 is the place an answer would appear. Watched.
- **Audit logging.** Only the Core team can say whether BIDMC hosting logs requests at the infrastructure level. Worth adding to `shared/unresolved-questions.md` along with the deletion question.
