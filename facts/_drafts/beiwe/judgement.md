# Beiwe and Forest: judgement (baseline run, 2026-10-10)

Inputs: `A.yaml`, `B.yaml`, `gaps.md`. Output: `facts/beiwe.yaml`. Every quote in the final record was
re-run through `tools/facts/quote_probe.py` on 2026-10-10 and returned `exact`. `validate.py --file
facts/beiwe.yaml`: 0 errors, 35 of 35 fields researched. `weekly.py --only beiwe --no-state`: 0 quotes
missing, 0 reworded. Its 7 "dead links" are expected: six openFDA searches (404 means no matches) and
the Google Play URL (the unconfirmed listing). The one unreachable page, the GitHub blob view of
`gunicorn_conf.py`, returned 503 to automated requests; the raw file returns 200.

No GitHub issue was opened, commented on or created. Issues were read only. Nothing from the private
`beiwe-discussions` repository is used.

## The pricing decision: superseded, not a conflict

Both researchers recorded `hosting_price` as `conflict`. I changed it to `stated` with the FY26 rates,
and kept the FY24 card in the note.

- `hsph.harvard.edu/research-resource/beiwe/use-beiwe/` shows "Fixed Monthly Cost: $2,640/month",
  "Variable Cost: $8.40/Active Participant Month" under "FY26 Example Pricing". Page metadata:
  published 2025-08-13, modified 2026-07-23.
- `hsph.harvard.edu/research/onnela-lab/beiwe-service-center/` shows "$1,937/month" and "$6/Active
  Participant Month" under "FY24 Example Pricing". Page metadata: published 2024-10-16, modified
  2025-10-21.
- Each page names its own fiscal year, so they are successive rate cards. The sources do not
  disagree about the same thing. The BSC home page (`research-resource/beiwe/`) links to use-beiwe,
  not to the old page.
- Current: FY26. Caveat for the coordinator: Harvard's FY26 ended 2026-06-30, so an FY27 card may
  exist. None was published on 2026-10-10, and use-beiwe was edited in July 2026 without changing it.
- The old page stays on the watch list (role `pricing`) so the monitor sees it if it is updated or
  removed.

This also settles `academic_vs_commercial`. The FY26 for-profit example ($73,440) reproduces from the
standard formula. The FY24 for-profit mismatch is history and sits in a note.

## Fields where A and B disagreed

| Field | A | B | Decision and reason |
|---|---|---|---|
| user_cap, minimum_commitment, rate_limits, ai_training_terms, baa, dpa, iso27001, soc2 | not_public, Verified | not_public, Unclear | Verified. Same status. The Oura pilot uses Verified for a checked "not public", and the pages were read. |
| academic_vs_commercial | unclear | stated, Corroborated | stated, Corroborated. With FY24 superseded, the only current card treats for-profit and university studies alike. The equality is arithmetic on an example, so not Verified. |
| academic_pricing | stated, Verified (FY26 rates only) | stated, Corroborated (no academic discount, plus About page per-subject-month figures) | Merged. Verified, because the rates are quoted directly. The About page figures are kept, flagged as undated. |
| quote_required | 30-day-notice quote absent | 30-day quote cited from the old FY24 page | Same quote is on use-beiwe; cited there (exact). |
| hosting_price | conflict | conflict | stated, as above. |
| raw_streams | Power state listed for both OSes | Power state listed under both and under Android only | Recorded as documented inconsistently, matching the profile's existing conflict. B's Technology-page stream list was not used because that page is stale. |
| export_routes | adds direct S3 access for self-hosters | adds study configuration JSON export/import | Kept S3 (follows from self-hosting). Dropped config export: B gave no quote for it. |
| retention_terms | stated: participant deletion exists (dashboard template) | not_public (mentions ParticipantDeletionEvent in a note) | stated, Corroborated. Both found the same deletion feature; the code quote is exact, and the gap hunter's `DATA_DELETION_USERTYPE` quote adds who may delete. No retention period is published; the value says so. |
| deprecations | Python 3.8 to 3.12, last-leg encryption, Tableau v0, AMI retired | same plus "no features expected to be removed" and "January 2025" for the Python swap | Merged. B's README quote kept. "January 2025" not used: no quote supplied. Added announcement #471 (gap 6). |
| licence | raw LICENSE files, four repos | GitHub page "BSD-3-Clause license" for forest, unquoted backend | A's four exact LICENSE quotes. |
| app_availability | two entries: App Store and APK stated; Google Play unclear | one stated entry, Play 404 in a note | A's split. Play availability is a separate, unconfirmed claim, and the gap hunter's target-SDK point belongs with it. |
| hipaa_statement | Deployment guide and privacy wiki quotes | README SSL quote and IRB FAQ "no access to identifiers" | A's quotes. B's IRB FAQ quote is about identifiers, not HIPAA. |
| gdpr_statement | unclear, with the last-leg page's passing "GDPR" | not_public | not_public, Verified. A reason for encryption on a sysadmin page is not a GDPR statement. The page is listed among the sources checked and mentioned in the note. |
| fda_clearances | five searches | five searches, partly different | Union of six searches. |
| data_residency | region not published | DNS shows eu-north-1, in a note | Region kept out of the value: it comes only from a DNS lookup and has no quotable page. It stays in the note, labelled as an unquoted observation that locates the web tier, not the data. B's quote "If you are using other regions, simply replace" was replaced by A's clearer region quote. |
| developer_program_status | notes the deployment guide's "first class support" line against the FAQ's no-support line | not noted | Not carried into the record (no exact quote supplied for "first class support"). Worth a look by hand. |

Everything else (research_program, program_eligibility, program_application, program_status,
api_platform_fees, derived_metrics, sampling_rates, history_depth, hosting_options) agreed in
substance; I kept the better-sourced quotes from each. B's Google Form quote for the separate
collaboration route was added to program_application. B's multi-line quotes that joined list items
were replaced with single-item quotes.

## Gap hunter findings

Every source below was opened and every quote re-probed on 2026-10-10.

| # | Finding | Decision |
|---|---|---|
| 1 | FY26 rates on use-beiwe vs FY24 on the old page | Accepted as superseded, not a conflict (see above). "Request a Quote" does not make `quote_required` yes: rates are public, the quote is for the contract. |
| 2 | Google Play build does not collect calls and SMS since 2.5.0 | Accepted. `app/build.gradle` on `main` (the default branch) says so in the 2.5.0 entry, and the `googlePlayStore` flavour (app name Beiwe2) is the only one not built with the `textsAndCallsStats` manifest. The 3.1.2 entry limits background location prompts to the other two builds. The BSC download links serve the `commStatsCustomUrl` APK, which does collect them. Added to raw_streams and the Play entry of app_availability. |
| 3 | Optional ambient audio on Android | Accepted. 3.1.0 changelog says optional and off by default, set per study; backend `database/study_models.py` on `main` has `ambient_audio` (default False), 10-minute on/off defaults, 24 kbps bitrate, 44.1 kHz. Added to raw_streams. Not checked: iOS support, and whether the BSC allows it. |
| 4 | Account lockout | Accepted, as a note under hipaa_statement (no schema field fits). `endpoints/login_endpoints.py` on `main`: `MAX_LOGIN_ATTEMPTS_BEFORE_LOCKOUT = 10`, "locked out for 10 minutes". `config/settings.py`: `INACTIVITY_LOCKOUT_DAYS` default 730, and `REQUIRE_SITE_ADMIN_MFA` default false. The old wiki IRB FAQ ("not currently implemented but it has been added to our feature request list") is superseded by the code. I did not re-check the 8 and 20 character password minimums or the 2025-11-18 commit date; those stay the gap hunter's. |
| 5 | BSC lists data deliverables and a four-week beta | Accepted; in research_program. |
| 6 | Announcement #471, data-processing bug from about March 2024 | Accepted. Opened 2026-03-06, still open, labelled ANNOUNCEMENT. Says the hourly-file merge step could discard already-processed data, raw data was not lost, and old data must be reprocessed. Added to deprecations (closest field) with a pointer from export_routes. The 25% to 100% figure is the maintainer's own observation, given in a note, not as a quote. |
| 7 | Participant data deletion | Accepted; in retention_terms. |
| 8 | zstd storage and Mano | Accepted; already in A's export_routes. |
| 9 | Android target SDK 33, last release 3.6.0 (June 2024), below Play's API floor | Accepted with the inference flagged. `targetSdkVersion 33` and the Google policy quote are exact; the last commits touching `build.gradle` are 2024-06-13 ([3.6.0]). That this explains the missing Play listing is inference and is labelled so. |
| 10 | Python 3.8 to 3.12 migration; #494 release block | Migration accepted (already in A). #494 quote exact; mentioned in the deprecations note only, since a blocked release pipeline is not a deprecation. |
| 11 | Forest DST bug #343 | Accepted; derived_metrics source and note. |
| 12 | Forest single v1.0 release, develop 506 commits ahead, JOSS review | Release facts accepted into the derived_metrics note. The JOSS review is not in the record (not a decision fact for this schema). |
| 13 | EU portal in eu-north-1 | Accepted only as an unquoted observation in the data_residency note, per the coordinator's instruction. Not a fact value. |
| 14 | iOS persistence depends on GPS; battery reports | Quotes exact. Not in the record: no schema field fits. For the profile's participant-experience section. Do not copy study names or participant IDs from #88. |
| 15 | Cross-OS re-registration blocked (#463) | Quote exact. Not in the record (no field). Profile material. |
| 16 | Long-running iOS file corruption and recovery script (#360) | Quote exact. Not in the record (no field). Relevant to Module 3 completeness figures for pre-2024 iOS data. |
| 17 | Last-leg encryption on older deployments | Accepted; already in deprecations, and referenced in the hipaa_statement note. |
| 18 | Harvard Technology page is stale | Accepted as a warning. The page is still cited, but only for the BSD-3 line and the raw-data line, which remain true. Its stale lines are noted under developer_program_status. |

## Profile and matrix statements the record contradicts

Not edited; for the coordinator.

| File | Line | Says | Record says |
|---|---|---|---|
| module-02-digital-phenotyping/profiles/beiwe.md | 13 | BSC rates $1,937 per month plus $6, examples FY24 | FY26: $2,640 plus $8.40; the FY24 page is superseded |
| profiles/beiwe.md | 146 | "$1,937 per month for the study duration plus $6 per Active Participant Month" | Same correction |
| profiles/beiwe.md | 216 | Pricing section built on the FY24 page, with the for-profit mismatch as a live concern | FY26 card on use-beiwe; for-profit example now fits the formula |
| profiles/beiwe.md | 236 | Resolved note quoting $1,937 + $6 | Same correction |
| profiles/beiwe.md | 249 | "fixed $1,937 per month fee" in poor-fit use cases | $2,640 |
| profiles/beiwe.md | 285 | Source 8 lists the FY24 rates as the BSC's figures | Old page; cite use-beiwe for current rates |
| profiles/beiwe.md | 24 | Beiwe2 apps "available on the App Store / Play Store" | Play listing unconfirmed (404 on 2026-10-10) |
| profiles/beiwe.md | 53 to 54 | Calls and SMS: Android "Yes", no build caveat | Only the lab-distributed builds; the Google Play build has not collected them since 2.5.0 |
| profiles/beiwe.md | 56 | Audio: "Active, not passive. No continuous audio capture." | Android has an optional ambient audio stream, off by default, set per study |
| profiles/beiwe.md | 125 | "the current BSC pages read 2026-10-10 do not list data deliverables" | use-beiwe lists "Access to both raw data and summary metrics" |
| profiles/beiwe.md | 27 | "a beta-testing phase" | A four-week beta-testing phase |
| profiles/beiwe.md | 135 | "Retention defaults and deletion procedures are not stated" | Retention still not stated; a participant deletion feature exists in the platform |
| profiles/beiwe.md | 209 | "There is no account lockout after failed attempts (on the feature request list)" | 10 failed logins lock an account for 10 minutes; idle accounts lock after 730 days by default |
| module-02-digital-phenotyping/comparison-matrix.md | 125 | Beiwe (BSC): "$1,937 per month fixed plus $6 per Active Participant Month", FY24 examples, for-profit mismatch | FY26: $2,640 plus $8.40; FY26 for-profit example fits |
| comparison-matrix.md | 107 | Android calls and SMS without a build caveat; "Audio only through audio surveys" | Calls and SMS only in lab-distributed builds; optional ambient audio on Android |
| comparison-matrix.md | 43 | Android row: calls and SMS Android only, no build caveat | Same build caveat |

Not contradictions but now answerable, for the profile's open questions: line 258 (where EU data are
stored) is still open, with the DNS observation as a lead only; line 259 (Play listing) is still open.
Gap 6 (#471) also bears on unresolved questions Q106, Q115 and Q124 in
`shared/unresolved-questions.md`, since completeness figures from data downloaded after about March
2024 may undercount.

## Check by hand

1. Whether an FY27 BSC rate card exists (Harvard's FY26 ended 2026-06-30).
2. Google Play listing for `org.beiwe.app` in a browser (automated requests get 404).
3. Whether the BSC allows ambient audio, and whether iOS has it.
4. The wiki deployment guide's "first class support" line against the FAQ's no-support line.
5. The EU data bucket's region and the processor entity, with the BSC (the DNS lookup locates only the
   web tier).
