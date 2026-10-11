# AWARE Framework: judgement, 2026-10-11

Inputs: `A.yaml`, `B.yaml`, `gaps.md`, and the starter `facts/aware.yaml` (all `unresearched`). Output: `facts/aware.yaml`, 37 entries (21 stated, 11 not_public, 5 not_applicable, 0 conflict), 14 watched pages. All 77 quotes matched "exact" with `quote_probe.py` on 2026-10-11 (one gap-hunter quote was on the Narrator GitHub repo, not the website page A cited; re-sourced). `validate.py --file facts/aware.yaml`: 0 errors, 0 unresearched. `weekly.py --only aware --no-state`: 49 pages, 0 quotes missing, 0 reworded, 0 dead links. No scratch copy was needed.

## Fields where A and B disagreed

| Field | A | B | Decision and reason |
|---|---|---|---|
| research_program | not_applicable | not_applicable, with the Support page as nearest analogue | **stated**, departing from both. RADAR-base's record set the precedent: where there is no access program, the researcher-facing paid offering is recorded here. AWARE's Support page offers paid study support and hosting by contact. The value says plainly that there is no access program. |
| program_status | stated, used for the project's own status | not_applicable, project status in a note | **not_applicable** (coordinator point 8). The schema defines it as the status of a program. Project status (maintainers, releases) moved to developer_program_status, whose subject is the open developer route, and the rename and archive history to deprecations. |
| developer_program_status | Open source, Discord | Open source, release 4.7.3.beta | Merged, plus A's team and origin quotes from program_status. |
| confidence on not_public fields (user_cap, academic_pricing, minimum_commitment, hosting_price, ai_training_terms, baa, dpa, hipaa, iso27001, soc2) | Corroborated | Verified | Corroborated. These are absences on a small academic site, checked by page reading and a WordPress search, not by any statement. |
| history_depth | stated, Corroborated | not_applicable | stated, Corroborated. The question has an answer (no vendor-held copy); it is an inference, which the note says. |
| retention_terms | Corroborated | Verified | Corroborated. The source is a 2019 policy that names Play Store clients that no longer exist. |
| raw_streams (iOS) | One iOS entry from AWAREFramework-iOS | HealthKit via V2 App Store text, mixed into one entry | Split into three scopes: Android, iOS V3, iOS V2 and framework. See point 1 below. |
| derived_metrics | RAPIDS, Narrator, Communication | RAPIDS (AGPL-3.0), plugins | Merged, with the RAPIDS licence verified on its repo. |
| licence | Apache 2.0; iOS app repo has no LICENSE file | Quoted the iOS app README's Apache 2.0 text | Both right. No LICENSE file (GitHub API reports none), but the README states Apache 2.0. Record says both. |
| app_availability (iOS) | V2 only | V2 only | Both missed V3. See point 1. |
| deprecations | Legacy, archive, dashboard, Google Fit | Legacy, archive, dashboard | A's fuller entry kept. |
| user_cap, academic_vs_commercial, subscription_price, api_platform_fees, quote_required, sampling_rates, export_routes, rate_limits, hosting_options, gdpr_statement, fda_clearances, data_residency | Agreed in substance | Agreed in substance | Merged quotes and detail. B's device_price source dropped (A's plain not_applicable is enough). |

## Points the coordinator asked me to settle

1. **iOS apps.** Both are live on the App Store under seller Yuuki Nishiyama (iTunes lookup API, 2026-10-11). V2 (`com.yuukinishiyama.app.aware-client-ios-v2`): 1.14.2, 2025-07-10, iOS 12+. V3 (`com.awareframework.app.ios.yxnlab.AwareClient`): released 2026-06-28, 1.7.0 on 2026-07-23, iOS 16.6+. The gap hunter is right. V3's listing describes HealthKit (including ECG and audiograms), Apple Watch, AirPods motion, activity labels, a bundled custom keyboard, music, photos, iBeacon, Shortcuts and notifications, with ambient noise added in a version update. GitHub confirms about 40 `com.awareframework.ios.sensor.*` repos, many created 2026-06-11 and pushed 2026-07-07. No public source repo for the V3 app itself exists (searched the org, tetujin's account and GitHub search). awareframework.com still links only V2 and has no page mentioning V3. Scoping: `app_availability` iOS names V3 as current and V2 as still listed and the one the site links; `raw_streams` has separate V3 and V2 entries. V3's keyboard and notification streams are not the Android equivalents (own keyboard only; own pushes only), and V3's listing does not mention ESM. Calling V3 "current" is my judgement from recency and bundle ID; flagged in the note.
2. **Paid hosting and support.** Confirmed on the Support page, quotes exact. Contact-only via Dr Simon D'Alfonso, no price. `hosting_options` stated (self-hosted or paid managed), `hosting_price` not_public, `quote_required` stated.
3. **Maintainers and status.** Team page, Background Primer and README all confirm the Melbourne team. GitHub API: 4.2.1 released 2025-05-26, 4.7.3.beta 2026-08-07. The ecosystem-changes post (2025-01-13) confirms the AWARE-Light rename; denzilferreira/aware-client archived 2023-06-18. Recorded in developer_program_status and deprecations.
4. **The 2019 privacy policy.** GDPR section kept, Corroborated (self-claim cap). Still current: local-first storage, direct upload to the researcher's server, withdrawal. Stale: the Play Store scope, the free hosted dashboard, and the 15-minute ping. I checked the current Android source (`aware-client` main and beta, `Aware.java`): the ping posts to `api.awareframework.com/index.php/awaredev/alive` only when the `aware_donate_usage` setting is "true", and that preference is commented out of `aware_preferences.xml`. `api.awareframework.com` returned NXDOMAIN on 2026-10-11. So the ping is effectively dead on Android; iOS behaviour was not checked. All of this is in the gdpr_statement note.
5. **Android sideloading.** Homepage quote and the Play Protect post both exact. The `com.aware.phone` Play listing is cited with `expect_absent`.
6. **Licences.** Apache 2.0 confirmed for aware-client, AWARE Micro, the configurator and AWAREFramework-iOS. The iOS V2 app repo has no LICENSE file but its README states Apache 2.0. New iOS sensor repos mostly have no detected licence (calendar is MIT). RAPIDS is AGPL-3.0 (carissalow/rapids).
7. **Screentext passwords.** Quote exact on the Screentext page, which also says the sensor "does not record password inputs" in general. Added to the Android raw_streams note with issue 31 (open since 2024-02-28) and the keyboard and screenshot capture quotes. A `fix/screen_text/extra_protect_for_password` branch exists and is fully merged into main and beta, but its commits are 2024 screentext fixes and the issue stays open, so the risk stands.
8. **program_status.** See the table: not_applicable, project status moved to developer_program_status.

## Gap hunter findings

| Finding | Decision | Why |
|---|---|---|
| 1. Paid hosting at Melbourne | Accepted | Quote exact. hosting_options, hosting_price, quote_required, data_residency, research_program. |
| 2. Paid support | Accepted | Quote exact. |
| 3. Melbourne team | Accepted | Quotes exact. developer_program_status. |
| 4. Open Collective negligible | Accepted as a note | Secondary source; figure in developer_program_status note. |
| 5. iOS Client V3 | Accepted | Every quote exact on the live listing; dates from the iTunes API. |
| 6. New Swift sensor repos | Accepted | Repo READMEs quoted (keyboard, notification); dates from the GitHub API. |
| 7. 2019 privacy policy and ping | Accepted | Quotes exact; went further and checked the Android source (point 4). |
| 8. AWARE-Light rename | Accepted | Quote exact. |
| 9. Dashboard gone | Accepted | Gap hunter said timeout; DNS now gives NXDOMAIN, so recorded as no longer resolving. |
| 10. AWARE Micro details | Accepted in part | Docker and capacity quotes used; Vert.x version detail not needed. |
| 11. Direct-to-MySQL, root credentials | Accepted | Quotes exact; root-credential point in the export_routes note. The guess that DB credentials sit in the shared config file was not confirmed and is left out. |
| 12. Duplicate records | Accepted | Quote exact. |
| 13. Accessibility for special sensors | Accepted | Quote exact. |
| 14. Screenshot, keyboard, issue 31 | Accepted | Quotes exact; issue still open per GitHub API. |
| 15. Google Fit | Accepted | Both quotes exact. |
| 16. Play Protect, versions | Accepted | Quotes exact. |
| 17. Narrator and Google Maps | Accepted | Quote is on the GitHub repo, not the website page. |
| 18. RAPIDS AGPL-3.0 | Accepted | Quote exact. |
| 19. Licences not uniform | Accepted | GitHub API listing re-run 2026-10-11. |
| 20. Orygen access | Note only (research_program) | Secondary, informal partnership, not a program. |
| 21. PR 64, issue 56 | Issue 56 in a note; PR 64 not used | PR was closed unmerged, so it changes nothing shipped. |
| 22. Discord, UBISS workshop | Discord accepted; workshop rejected | Workshop is a one-off 2025 event with no schema field. |
| 23. V3 privacy label | Note only | Developer self-declaration that Apple says is unverified. |

## Statements in the profile or matrix that the record contradicts

| File | Line | What it says | What the record says |
|---|---|---|---|
| module-02-digital-phenotyping/profiles/aware-framework.md | 7 | Organization is an "International academic collaboration (originated University of Oulu)" | Managed by a team in Melbourne's School of Computing and Information Systems; created by Denzil Ferreira's PhD |
| module-02-digital-phenotyping/profiles/aware-framework.md | 12, 127 | "Self-hosted backend only; no managed/SaaS hosting found"; self-hosting "the only deployment path" | A paid hosting service at the University of Melbourne exists, by contact |
| module-02-digital-phenotyping/profiles/aware-framework.md | 13, 25, 146, 163, 186 | Free; no paid tier; Open Collective as the sustainability model | Paid support and hosting exist (unpriced); Open Collective has raised USD 16.82 in total |
| module-02-digital-phenotyping/profiles/aware-framework.md | 11, 185 | Apache-2.0, not every repo checked | Apache-2.0 for the main repos; many new iOS sensor repos have no licence, one is MIT; V2 app repo has no LICENSE file; RAPIDS is AGPL-3.0 |
| module-02-digital-phenotyping/profiles/aware-framework.md | 40 | "No OS activity labels" | V3 iOS has activity recognition (walking, running, cycling, driving, stationary) |
| module-02-digital-phenotyping/profiles/aware-framework.md | 49, 161, 173 | Keyboard iOS "No"; keyboard Android only | V3 iOS has a keyboard stream, limited to AWARE's own bundled keyboard, metadata only by default |
| module-02-digital-phenotyping/profiles/aware-framework.md | 50 | Audio/microphone Unclear on both | iOS V3 has ambient noise (decibels and sound labels); V2 lists ambient noise features |
| module-02-digital-phenotyping/profiles/aware-framework.md | 51 | Notifications Android "Unclear", iOS "No" | Android Notifications sensor exists (needs Accessibility); iOS V3 records the app's own pushes only |
| module-02-digital-phenotyping/profiles/aware-framework.md | 117 | Wearables: Fitbit and Apple Watch only | Also HealthKit (V2 and V3) and AirPods motion (V3) |
| module-02-digital-phenotyping/profiles/aware-framework.md | 101 | Derived metrics not verified | RAPIDS (separate, AGPL-3.0), AWARE Narrator, some context in Communication and iOS activity labels |
| module-02-digital-phenotyping/profiles/aware-framework.md | 113, 184 | Data access and export not verified; backend requirements open | Direct upload to researcher's MySQL 5.x (Android) or AWARE Micro (iOS); local SQLite copy |
| module-02-digital-phenotyping/profiles/aware-framework.md | 142 | Privacy not verified | 2019 policy with a GDPR section (self-claim, partly stale) |
| module-02-digital-phenotyping/profiles/aware-framework.md | 9, 125 | Android history notes only the archived repo | AWARE-Light became main AWARE in January 2025; original is AWARE Legacy |
| module-02-digital-phenotyping/profiles/aware-framework.md | 125 | Sideloading noted | Also the Play Protect "unsafe app blocked" warning and the advice to pin one version |
| module-02-digital-phenotyping/comparison-matrix.md | 31 | Organization "International academic collaboration (originated University of Oulu)" | Melbourne team |
| module-02-digital-phenotyping/comparison-matrix.md | 50, 114 | Keyboard Android only; iOS module list from the website catalogue | V3 iOS adds keyboard (own keyboard), HealthKit, Apple Watch, AirPods, activity labels, ambient noise |
| module-02-digital-phenotyping/comparison-matrix.md | 72, 84 to 86 | Hosted option "None found"; "AWARE has none"; four public-source platforms with a hosted route | Paid Melbourne hosting exists, price not stated, so five |
| module-02-digital-phenotyping/comparison-matrix.md | 133 | Pricing "Own infrastructure; Open Collective donations", paid tier "None" | Paid support and hosting by contact |
| module-02-digital-phenotyping/comparison-matrix.md | 157 | Privacy "Not established", "Not located" | 2019 GDPR section, Corroborated, partly stale |
| module-03-applied-studies/feasibility-matrix.md | 103 | Treats AWARE-Light as a separate platform (per the gap hunter; not re-read) | AWARE-Light is now the main Android AWARE |

## For the coordinator to check by hand

- Whether V3 should replace V2 as the site's iOS client. The site has not announced V3; only D'Alfonso's team or Nishiyama can say whether V2 is being retired.
- Whether the iOS clients still send any usage ping (only Android source was checked).
- The hosted service's terms (DPA, BAA, residency detail, price) are a question for Dr Simon D'Alfonso.
