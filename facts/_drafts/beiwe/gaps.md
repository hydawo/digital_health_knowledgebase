# Beiwe and Forest: gap hunter findings (baseline run, 2026-10-10)

Compared against `module-02-digital-phenotyping/profiles/beiwe.md` (profile),
`module-02-digital-phenotyping/comparison-matrix.md` (matrix) and `facts/beiwe.yaml` (every field still
`unresearched`, so every finding below is "no" for the yaml). Every quote was checked with
`tools/facts/quote_probe.py` and returned `exact` on 2026-10-10, except finding 13, which has no quotable
page and says so.

Abbreviations: KB = knowledge base. "Date" is the source's own date where it has one, else the read date.
GitHub issues were read only; nothing was opened, commented on or created. `onnela-lab/beiwe-discussions`
is a private repository, so nothing from it is used here (it cannot be cited or probed publicly, and its
issue titles carry participant IDs and study names).

## Contradictions

### 1. hosting_price / academic_pricing: a second Harvard page publishes FY26 BSC rates of $2,640 per month plus $8.40 per Active Participant Month
- **Found:** The Harvard Chan "Use Beiwe" page (part of the newer research-resource/beiwe site) publishes a higher rate card, headed FY26, than the Onnela Lab BSC page the KB cites. The old page still shows the FY24 card ($1,937 and $6), so two live Harvard pages disagree. All three FY26 examples reproduce exactly from the new formula, including the for-profit one ($73,440 = 24 x $2,640 + 1,200 x $8.40), which suggests the for-profit discrepancy the KB flags in the FY24 examples no longer applies. The page now ends in "Request a Quote or Platform Demo".
- **URL:** https://hsph.harvard.edu/research-resource/beiwe/use-beiwe/ (new); https://hsph.harvard.edu/research/onnela-lab/beiwe-service-center/ (old, still live)
- **Quotes:** "Fixed Monthly Cost: $2,640/month" / "Variable Cost: $8.40/Active Participant Month" / "FY26 Example Pricing" / "The total cost of the contract is $73,440." / "Request a Quote or Platform Demo"; old page: "Fixed Monthly Cost: $1,937/month" / "FY24 Example Pricing"
- **Date:** read 2026-10-10 (FY26 label on the page)
- **Source type:** vendor_page
- **In KB:** contradicts. Profile lines 13, 146, 216 and 249; matrix line 125 and the "only the BSC publishes rates" rows (matrix lines 80, 137, 211) all carry $1,937 plus $6. Record as `conflict` with both sources; the FY26 page is more likely current. Also check whether "Request a Quote" changes `quote_required`.

### 2. raw_streams: calls and SMS are not collected by the Google Play build of the Android app
- **Found:** The Android changelog in `app/build.gradle` says that since 2.5.0 the `googlePlayStore` variant (the one named Beiwe2) no longer asks for SMS/MMS or call-log permissions, because of Google policy; only the `onnelaLabServer` (and `commStatsCustomUrl`) builds collect them. Background location is likewise prompted only in the non-Play builds (3.1.2). So "Android: calls Yes, SMS Yes" holds only for a sideloaded or lab-distributed APK.
- **URL:** https://github.com/onnela-lab/beiwe-android/blob/main/app/build.gradle (probed at https://raw.githubusercontent.com/onnela-lab/beiwe-android/main/app/build.gradle)
- **Quotes:** "googlePlayStore build variants no longer ask for SMS/MMS and Call Log" / "build variants still collect SMS/MMS and Call Log data." / "Only prompts for background location permission in onnelaLabServer and"
- **Date:** changelog entry undated (2019 era, per its reference to a Google policy change); read 2026-10-10
- **Source type:** repository
- **In KB:** contradicts (partly). Profile lines 53 to 54 and matrix lines 43 and 107 list calls and SMS as Android "Yes" with no build caveat. Profile line 17 source already names the build flavours but not this consequence. This also bears on finding 4: the build whose listing the KB could not find is the one without calls and SMS.

### 3. raw_streams: Android has an optional ambient (continuous) audio stream
- **Found:** Android 3.1.0 added optional ambient audio collection, set per study and off by default. The backend still defines the stream and its settings on `main`: on/off duty cycle (default 10 minutes each), bitrate and a 44.1 kHz default sampling rate. The KB's own summary-statistics field list already includes "ambient audio" bytes, but the stream table says no continuous audio exists.
- **URL:** https://raw.githubusercontent.com/onnela-lab/beiwe-android/main/app/build.gradle ; https://raw.githubusercontent.com/onnela-lab/beiwe-backend/main/database/study_models.py
- **Quotes:** "Adds foreground service, and optional ambient audio collection feature" / "ambient audio can be enabled or disabled at the study level. It's disabled by default." / "ambient_audio = models.BooleanField(default=False)" / "ambient_audio_sampling_rate = models.PositiveIntegerField(default=44100"
- **Date:** read 2026-10-10
- **Source type:** repository
- **In KB:** contradicts. Profile line 56 ("Active, not passive. No continuous audio capture") and matrix line 107 ("Audio only through audio surveys"). Profile line 133 lists ambient audio bytes without comment. Which builds expose it, and whether the BSC permits it, are not stated.

### 4. security (closest fields: hipaa_statement, hosting_options): the portal does lock accounts after failed logins, and after two years idle
- **Found:** Backend `main` locks a researcher out for 10 minutes after 10 failed logins, and (since November 2025) blocks login for accounts idle longer than `INACTIVITY_LOCKOUT_DAYS`, default 730. Minimum password length is 8, raised to 20 for site admins; site-admin MFA is an opt-in deployment setting. A `DATA_DELETION_USERTYPE` setting governs who may delete participant data (see finding 7).
- **URL:** https://raw.githubusercontent.com/onnela-lab/beiwe-backend/main/endpoints/login_endpoints.py ; https://raw.githubusercontent.com/onnela-lab/beiwe-backend/main/config/settings.py ; https://raw.githubusercontent.com/onnela-lab/beiwe-backend/main/libs/endpoint_helpers/password_validation_helpers.py ; commit https://github.com/onnela-lab/beiwe-backend/commit/8c0396cfada9ca75b74ccc201b93667ff9967c04 (2025-11-18)
- **Quotes:** "MAX_LOGIN_ATTEMPTS_BEFORE_LOCKOUT = 10" / "is locked out for 10 minutes." / "duration, which defaults to a very lax 730 days (2 years)." / "for site admins it is 20" / "the absolute minimum is 8"
- **Date:** inactivity lockout 2025-11-18; read 2026-10-10
- **Source type:** repository
- **In KB:** contradicts. Profile line 209 says "There is no account lockout after failed attempts (on the feature request list)", taken from the older wiki privacy page. The code supersedes it. No schema field fits portal security; the judge may want a note in the profile rather than a fact.

### 5. research_program (BSC service scope): the current BSC page does list data deliverables and a four-week beta
- **Found:** The new "Use Beiwe" page lists what the BSC includes, among them access to raw data and summary metrics, and a four-week beta-testing phase.
- **URL:** https://hsph.harvard.edu/research-resource/beiwe/use-beiwe/
- **Quotes:** "Access to both raw data and summary metrics for in-depth insights" / "Four-week beta testing phase to ensure setup accuracy"
- **Date:** read 2026-10-10
- **Source type:** vendor_page
- **In KB:** contradicts. Profile line 125 says "the current BSC pages read 2026-10-10 do not list data deliverables". Profile line 27 has "a beta-testing phase" without the four-week length.

## Missing from the KB

### 6. deprecations / export_routes: a processing bug from about March 2024 left downloadable data incomplete until reprocessed
- **Found:** Backend announcement #471 (2026-03-06): the step that merges uploads into hourly files could discard already-processed data, so files from the Data Access API could be missing data, skewed towards the end of each hour. Raw uploads were kept; servers must be updated and old data reprocessed with a script. The maintainer reports seeing +25% to +100% more data after reprocessing (stated in the issue, not quoted here). A related iOS issue (#86, closed 2026-03-02) reported no data in the first part of every hour.
- **URL:** https://github.com/onnela-lab/beiwe-backend/issues/471
- **Quotes:** "There has been a bug in data processing" / "The earliest suspected date of affected data starts in roughly March of 2024." / "no data has been lost" / "Old data will have to be reprocessed."
- **Date:** 2026-03-06 (announcement), comments to 2026-03-12
- **Source type:** repository (developer issue tracker)
- **In KB:** no. This matters beyond the platform profile: any Beiwe completeness figure computed from data downloaded between about March 2024 and the fix (for example Zawada et al. 2025, monitoring March to November 2024, unresolved Q124 and Q106/Q115 at `shared/unresolved-questions.md` lines 120, 121, 385) may undercount, which runs against the "post-heartbeat" comparison those questions wait on. Self-hosted deployments that have not updated and reprocessed are still affected.

### 7. retention_terms: participant data deletion exists in the platform
- **Found:** The backend has a participant deletion queue that purges a participant's database records and versioned S3 objects (`libs/participant_purge.py`), and a deployment setting choosing which role may trigger it, defaulting to study researcher.
- **URL:** https://raw.githubusercontent.com/onnela-lab/beiwe-backend/main/config/settings.py ; https://github.com/onnela-lab/beiwe-backend/blob/main/libs/participant_purge.py
- **Quote:** "DATA_DELETION_USERTYPE: str = getenv('DATA_DELETION_USERTYPE', 'study_researcher')"
- **Date:** read 2026-10-10
- **Source type:** repository
- **In KB:** no. Profile line 135 says "Retention defaults and deletion procedures are not stated on the pages read." Still no stated retention period for BSC-hosted data.

### 8. export_routes: data are now stored and downloaded as zstd-compressed files, and Mano is the recommended download client
- **Found:** The wiki says raw data are stored as individually zstd-compressed `.zst` files (about one fifth of raw text size), delivered inside an uncompressed `.zip` wrapper, and recommends Mano for large downloads. Mano is the lab's BSD-3 Python library and CLI (on PyPI, 0.6.0) for listing studies and participants, reading device settings and incremental data sync; its README lists "Removal of the need for site passwords" as under development.
- **URL:** https://github.com/onnela-lab/beiwe-backend/wiki/Managing-ZSTD%E2%80%90Compressed-Data-From-The-Beiwe-Platform ; https://github.com/onnela-lab/mano
- **Quotes:** "it compresses your data down to 1/5th the raw text size" / "files are compressed individually, they are the raw form we store them in" / "If you are downloading many gigabytes of data you should use Mano." / (Mano) "Mano is a Python library and CLI tool that helps you write applications that interact with the"
- **Date:** read 2026-10-10 (wiki last edited 2026-08-06)
- **Source type:** vendor_docs; repository
- **In KB:** no. Profile lines 60, 129 and 233 describe hourly CSV downloads and the reference scripts only; Mano appears nowhere in the profile or matrix.

### 9. app_availability: the Android app's target SDK (33) is below Google Play's current floor, and its last release was June 2024
- **Found:** Every branch of `beiwe-android` targets SDK 33 (version 3.6.0 on `main`, 3.6.1 on `2026-updates`); the last tagged changelog entry is 3.6.0 (June 2024 commits). Google Play now requires new apps and updates to target API 36, and existing apps to target API 35 to stay visible to new users on newer Android. This is a likely, not confirmed, reason no Play listing could be found. Inference only.
- **URL:** https://raw.githubusercontent.com/onnela-lab/beiwe-android/main/app/build.gradle ; https://support.google.com/googleplay/android-developer/answer/11926878
- **Quotes:** "targetSdkVersion 33" / "3.6.0 - Adds new message receiving push notification feature" / (Google) "New apps and app updates must target Android 16 (API level 36) or higher to be submitted to Google Play" / "Existing apps must target Android 15 (API level 35) or higher to remain available to new users"
- **Date:** Google policy effective 2026-08-31; read 2026-10-10
- **Source type:** repository; secondary (platform policy, not the vendor)
- **In KB:** partly. Profile lines 10 and 259, matrix line 43 record Play availability as Unclear; the target-SDK constraint and the age of the last Android release are absent. Profile line 24 still says Beiwe2 apps are "available on the App Store / Play Store".

### 10. deprecations / hosting_options: self-hosted deployments must migrate from Python 3.8 on Amazon Linux 2 to Python 3.12 on Amazon Linux 2023
- **Found:** The wiki has a migration guide: the AWS Elastic Beanstalk platform moved from AL2 to AL2023, the deploy config could not support both, and a `python3.8-legacy` branch is kept for old environments. Separately, backend announcement #494 (2026-10-07) says a Forest performance problem had been blocking new backend releases to `main`; the last `main` commit message (2026-08-19) says staging "is still blocked". Self-hosters were therefore on a frozen `main` for months.
- **URL:** https://github.com/onnela-lab/beiwe-backend/wiki/Upgrading-Elastic-Beanstalk-from-Python-3.8-to-3.12 ; https://github.com/onnela-lab/beiwe-backend/issues/494
- **Quotes:** "AWS' \"Platform\" shifted from Amazon Linux 2 to Amazon Linux 2023" / "Python has 3.8 hit end-of-support in October 2024." / "was blocking us from releasing a new version of the beiwe-backend"
- **Date:** guide read 2026-10-10; #494 2026-10-07
- **Source type:** vendor_docs; repository
- **In KB:** no. Profile lines 145 to 147 describe AWS architecture and rolling releases without either point.

### 11. derived_metrics: open Forest bug puts daily summaries on the wrong day after a DST change
- **Found:** Forest issue #343 (open, 2026-10-01): Willow and Jasmine step fixed 86,400-second days from one local midnight, so after a daylight-saving change every daily row is labelled one day early. Totals are unaffected.
- **URL:** https://github.com/onnela-lab/forest/issues/343
- **Quotes:** "Forest is putting daily summary data on the wrong day." / "Any study running across a daylight saving change has everything after it labelled one day early."
- **Date:** 2026-10-01, open on 2026-10-10
- **Source type:** repository
- **In KB:** no. Relevant to the profile's Forest tables (lines 62 to 97) and to any BSC "final data analysis using production Forest packages".

### 12. licence / derived_metrics: Forest's only release is v1.0 (June 2025), 506 commits behind develop, and Forest is under JOSS review
- **Found:** Forest has one 1.0 release (GitHub v1.0 and PyPI `beiwe-forest` 1.0, 2025-06-30); `develop` is 506 commits ahead. A Journal of Open Source Software review opened 2026-04-30 and is still open, with reviewer comments being addressed in forest PR #341.
- **URL:** https://github.com/onnela-lab/forest/releases/tag/v1.0 ; https://pypi.org/pypi/beiwe-forest/json ; https://github.com/openjournals/joss-reviews/issues/10489 ; https://github.com/onnela-lab/forest/issues/341
- **Quotes:** "506 commits to develop since" / "Forest: A data analysis library for raw high-throughput digital phenotyping data" / "Fixes the reference problems raised in the JOSS review."
- **Date:** release 2025-06-30; review opened 2026-04-30; read 2026-10-10
- **Source type:** repository; paper (under review)
- **In KB:** partly. Profile line 257 leaves "How the metrics are versioned across releases" open; this answers part of it (a single PyPI release, so pip installs lag the docs and the backend).

### 13. data_residency: eu.beiwe.org is served from AWS eu-north-1 (Stockholm)
- **Found:** DNS for eu.beiwe.org is a CNAME to an Elastic Beanstalk load balancer in eu-north-1 (`awseb-...eu-north-1.elb.amazonaws.com`), and its address 13.53.70.214 sits in AWS's published eu-north-1 EC2 range; studies.beiwe.org resolves to us-east-1. This places the EU web tier in Sweden. It does not show where the S3 data bucket is, and no page states it.
- **URL:** none (DNS lookup and https://ip-ranges.amazonaws.com/ip-ranges.json, 2026-10-10)
- **Quote:** none. No published page says this; treat as Unclear supporting evidence only.
- **Date:** 2026-10-10
- **Source type:** secondary (technical observation)
- **In KB:** no. Partly answers profile line 258 and unresolved Q130 (`shared/unresolved-questions.md` line 124); the BSC should still confirm storage location and processor.

### 14. raw_streams / app_availability: iOS background persistence relies on keeping GPS on, with battery-drain reports in 2026
- **Found:** The pinned iOS 2.5 announcement (#56) says background persistence since 2.5 relies on GPS, which makes battery drain a concern. Issue #88 (opened 2026-08-24, closed 2026-09-24) records battery-drain reports from individual participants that the developers could not reproduce. Studies that switch GPS off on iOS should expect weaker persistence.
- **URL:** https://github.com/onnela-lab/beiwe-ios/issues/56 ; https://github.com/onnela-lab/beiwe-ios/issues/88
- **Quotes:** "Due to the persistence work and its reliance on GPS, battery drain suddenly becomes a big concern" / "A few participants have reported an issue with increased battery drain." / "Not widespread, individual participant users."
- **Date:** #56 2024-03-06; #88 2026-08-24 to 2026-09-24
- **Source type:** repository (developer issue tracker)
- **In KB:** no. Profile line 154 says battery impact was not benchmarked; the GPS dependency is not mentioned. (#88 names a study and participant IDs; do not copy those into the KB.)

### 15. raw_streams / program operations: switching a participant between iOS and Android is now blocked
- **Found:** Backend #463 (closed 2026-08-04): cross-OS re-registration on the same participant ID caused backend errors, so it was blocked; the remedy is a new participant ID.
- **URL:** https://github.com/onnela-lab/beiwe-backend/issues/463
- **Quotes:** "The solution is to retire that participant and place them on a new participant ID." / "I did the thing, this is now blocked."
- **Date:** 2026-08-04
- **Source type:** repository
- **In KB:** no. Profile line 193 covers moving to a new phone but not the cross-OS block.

### 16. raw_streams (data integrity): long-running iOS file-corruption bug, with a recovery script
- **Found:** Backend #360 (postmortem, closed) records an iOS race condition that left encryption keys missing or misplaced in uploaded files, fixed with the 2.5 rewrite; a recovery script decrypts the recoverable files. The wiki's compression guide pairs historical-data compression with running that legacy iOS recovery script.
- **URL:** https://github.com/onnela-lab/beiwe-backend/issues/360
- **Quotes:** "iOS has had a data corruption issue for a long time." / "We have more recoverable data than anticipated!"
- **Date:** opened 2024-03-06, final postmortem 2025-02
- **Source type:** repository
- **In KB:** no. Relevant to pre-2024 iOS completeness figures in Module 3, alongside finding 6.

### 17. hipaa_statement (transport security): older self-hosted deployments terminated TLS at the load balancer
- **Found:** A wiki page, "Enabling Last Leg Encryption On Older deployments", tells older self-hosted clusters to change the load-balancer mapping from 443-to-80 to 443-to-443, so traffic is encrypted between the load balancer and the servers too.
- **URL:** https://github.com/onnela-lab/beiwe-backend/wiki/Enabling-%22Last-Leg-Encryption%22-On-Older-deployments.
- **Quote:** "The port mapping of port 443 to port 80 should be changed to 443 to 443."
- **Date:** read 2026-10-10 (undated page)
- **Source type:** vendor_docs
- **In KB:** no. Profile line 207 says "Connections are TLS" without this caveat for older deployments.

### 18. other: the Harvard "Technology" page is stale and lists Power State without an OS restriction
- **Found:** The research-resource Technology page still says the backend is Python 3.6 and that Forest's first public release is "anticipated for early 2021". Its stream list includes Power State with no "Android only" tag, which sides with the iOS reading of the KB's Power State conflict, though the page is clearly outdated.
- **URL:** https://hsph.harvard.edu/research-resource/beiwe/technology/
- **Quotes:** "has been implemented primarily in Python 3.6" / "its first public release is anticipated for early 2021"
- **Date:** read 2026-10-10
- **Source type:** vendor_page
- **In KB:** no (page not cited). Low value; useful only as a warning not to cite this page for current facts. Profile lines 47 to 49 hold the Power State conflict.

## Searched, nothing found

- **FDA:** openFDA 510(k) search for "beiwe" or applicant "onnela": no matches. No CE/MDR status found. Beiwe is not marketed as a medical device.
- **Compliance evidence beyond self-claims:** no SOC 2 report, ISO 27001 certificate, trust portal, BAA or DPA found for the BSC or Onnela Lab LLC. A search snippet claimed the BSC is a "formal Harvard University Service Center" with an annually reviewed costing model, but that text was not found on any of the five Harvard Beiwe pages fetched, so it is not used.
- **NIH funding (RePORTER):** no active NIH project with Onnela as PI that funds Beiwe or Forest development in FY2024 to FY2026; the last clearly platform-related grant (R01MH122367, passive sensing of social isolation) ended 2025-02-28. Only one FY2024 grant from another PI mentions Beiwe. No quotable page (API result), so not a finding; possibly relevant to sustainability.
- **Job postings:** only a one-year Onnela Lab postdoc (network science, May 2026); no Beiwe engineering or BSC postings found.
- **Partners and integrators** (Fitabase, Labfront, Terra, Thryve): none integrate Beiwe. An OmniRing (research smart ring) storage PR to the backend (#408) was reviewed in 2025 but is not on `main`; no wearable integration exists in released code.
- **App Store:** Beiwe2 2.5.11 (2026-09-30), minimum iOS 15.0, seller Onnela Lab LLC; matches the KB. No other Beiwe listings.
- **Google Play:** no listing under `org.beiwe.app` or variant package names (404); web search found nothing current.
- **Press and newsroom:** no 2025 to 2026 press releases on Beiwe, the BSC or Forest found.
- **Recent papers on data access:** the 2024 to 2025 Beiwe papers found (Nurses' Health Study burst, NHS3/GUTS, HOPE) are already in Module 3.
- **Mano issues and Forest JOSS thread:** read; covered in findings 8 and 12.
