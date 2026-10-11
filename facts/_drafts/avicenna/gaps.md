# Gap hunt: avicenna (Avicenna Research, formerly Ethica Data)

Run date: 2026-10-11. Scope: everything outside the official docs the two researchers cover, plus the
vendor's forum blog, release notes, comparison pages and product-ideas board, which the profile has
not mined. Every quote below returned "exact" from `tools/facts/quote_probe.py`. Where a page was
probed through a different fetch URL, it is noted as `--fetch-url`.

KB files compared: `module-02-digital-phenotyping/profiles/avicenna-research-ethica.md` (profile),
`module-02-digital-phenotyping/comparison-matrix.md` (matrix), `facts/avicenna.yaml` (every field
still `unresearched`, so "yaml: no" applies to every entry and is not repeated).

## Contradictions

### 1. hosting_options: on-premise deployments exist (KB says vendor SaaS only)

- **Found:** the vendor's own security post says it patches "on-premise servers", two of its
  comparison pages sell "on-premise installations" as a differentiator, a product-ideas card is
  titled "Improve on-premise deployments", and the 2026-09-22 Garmin blog says SDK data goes to
  "Avicenna or institution server". On-premise looks like a real but unpriced, unadvertised option.
- **Quotes:**
  - https://forum.avicennaresearch.com/t/security-and-compliance/1267 : "This includes on-premise servers running Rocky Linux 9.x" (post updated 2025-11-08)
  - https://forum.avicennaresearch.com/t/1475 : "flexible deployment options including on-premise installations" (Compared to REDCap, 2025-12-30)
  - https://forum.avicennaresearch.com/t/1225 : "the on-premise deployment and API-based access make Avicenna the winner" (Compared to mEMA, 2025-06-14)
  - https://forum.avicennaresearch.com/t/1009 : "All on-premise deployment subdomains must go directly to the login page" (product idea, 2025-05-21)
  - https://forum.avicennaresearch.com/t/1645 : "including an institution’s own Avicenna infrastructure where applicable" (blog, 2026-09-22)
- **Source type:** vendor_page (forum blog and comparison pages), vendor_docs (security post).
- **Third-party echo:** the third-party ESM tool overview `ghxm/esm-tool-overview-static` `_tools/avicenna.md`, lists hosting "cloud-based" and "on premise" (secondary, not probed).
- **KB:** **contradicts.** Profile line 12 ("Vendor SaaS only ... No self-hosting"), line 85, line 128
  ("vendor-hosted only, no self-hosting"), line 142; matrix line 73 ("Vendor SaaS only"). Note the
  distinction still holds for *self*-hosting from open source: this is a vendor-installed,
  closed-source on-premise instance, terms unknown.

### 2. export_routes: a working export API is used by third-party code (KB says no export API exists)

- **Found:** NiDB (the open-source Neuroinformatics Database, `gbook/nidb`) has an Avicenna importer
  that POSTs to an Avicenna API endpoint with an API-key header, requests a participation export,
  polls for its status and downloads the file. Commits touching it are dated 2026-08-06, 2026-08-25
  ("capture status from avicenna surveys") and 2026-08-27. A data-source API importer is stubbed but
  commented out. Combined with the vendor's own "API-based access" claim (entry 1, mEMA comparison),
  an authenticated, export-job API evidently exists but is undocumented publicly. The roadmap card
  "Export Data with API" (t/1406, still in the "To Do" category id 10) may mean a public or
  documented version.
- **Quotes** (probed against https://github.com/gbook/nidb/blob/master/src/nidb/moduleRemoteImport.cpp
  with `--fetch-url` the raw.githubusercontent.com copy):
  - "URL should be https://avicennaresearch.com/api/v1/filter/export/"
  - "Requests a participation export from Avicenna, polls until ready"
  - "Authorization: ApiKey %2:%3"
- **Date:** code read 2026-10-11; last commit 2026-08-27.
- **Source type:** repository (plus vendor_page for the mEMA quote).
- **KB:** **contradicts.** Profile lines 76, 81 ("No export API exists yet"), 130, 143, 151
  ("Answered 2026-10-10: no"); `shared/unresolved-questions.md` line 294 (#90, "Avicenna has no
  export API"). Suggest status `conflict` or `unclear`, and a vendor question: is the
  `/api/v1/filter/export/` key route available to any customer, and on which licence?

### 3. data_residency: "Canada only" is not the whole story

- **Found:** the security post says all data are in Canada, but the legal page claims an
  "infrastructure-agnostic approach" for residency, the Garmin blog routes SDK data to an
  institution's server (entry 1), and a "Server Region" product-ideas card (t/1031) was edited
  2026-08-12 to read "Closed epic: OP-9223" while still filed in the "To Do" category. Whether
  regions other than Canada (or on-premise only) are now offered is unclear.
- **Quotes:**
  - https://forum.avicennaresearch.com/t/security-and-compliance/1267 : "Avicenna stores all data on servers physically located in Canada"
  - https://avicennaresearch.com/legal/ : "Our infrastructure-agnostic approach enables flexibility in meeting data residency and regulatory requirements"
  - https://forum.avicennaresearch.com/t/1031 : "Closed epic: OP-9223"
- **Source type:** vendor_docs, vendor_legal, vendor_page.
- **KB:** partly. Profile line 101 records Canada and the UK/EEA wording as found; matrix lines 73
  and 158 say "data in Canada". The infrastructure-agnostic and server-region items are **no**.

## Missing programs and offerings

### 4. White-label study apps are a working, high-volume service (KB lists it as an open question)

- **Found:** the App Store seller "Avicenna Research Inc." (artist id 1137173051) publishes 33
  study-branded iOS apps besides the main app, 13 of them first released in 2026 (for example
  GAMMA Research Study, SWIPE STUDY, Project VIIBE, MoodMetrics Study, Understanding Sleep), most
  updated 2026-10-07. Separately, a 2025 paper used an Avicenna app "customized into a smartphone app
  called" Sesikhona on Google Play (entry 13). The SensorKit approval guide (entry 9) shows Avicenna
  builds a separate app and Bundle ID per SensorKit study.
- **Quotes:**
  - https://apps.apple.com/us/developer/avicenna-research-inc/id1137173051 : "SWIPE STUDY"
  - https://apps.apple.com/us/app/gamma-research-study/id6747886728 : "Avicenna Research Inc."
- **Date:** iTunes lookup 2026-10-11.
- **Source type:** app_store.
- **KB:** **no.** Profile line 154 ("Under what circumstances is the 'white-label' option available
  ... still open"); lines 26 and 123 only name the feature. Cost still unknown.

### 5. Avicenna Keyboard: a separate iOS keyboard app for keystroke data

- **Found:** a standalone iOS keyboard app for study participants, released 2025-12-16, updated
  2026-09-01; release notes say it moved from TestFlight to the App Store with 75 languages. Bears on
  the "Keyboard" stream, which the profile marks Unclear on both platforms.
- **Quote:** https://apps.apple.com/us/app/avicenna-keyboard/id6745755643 : "Avicenna Keyboard is a custom iOS keyboard app designed exclusively for research participants enrolled in health research studies"
- **Source type:** app_store.
- **KB:** **no.** Profile line 50 (Keyboard: Unclear / Unclear).

## Compliance evidence beyond the vendor's own claims

### 6. NHS Data Security and Protection Toolkit: independent registry entry

- **Found:** Avicenna Research Inc (Canada), organisation code AVRESC001, published a 2025-26
  (version 8) DSPT assessment with "Standards met" on 25 November 2025. This is a self-assessment
  published on an NHS England register, not an audit certificate, but it is independent of the
  vendor's site. The vendor's security post claims DSPT compliance.
- **Quotes:**
  - https://www.dsptoolkit.nhs.uk/OrganisationSearch/AVRESC001 : "2025-26 (version 8) - Standards met 25 November 2025"
  - https://www.dsptoolkit.nhs.uk/OrganisationSearch/AVRESC001 : "Organisation code: AVRESC001"
  - https://forum.avicennaresearch.com/t/security-and-compliance/1267 : "Avicenna is fully compliant with the Data Security and Protection Toolkit (DSPT)"
- **Source type:** certificate (registry entry), vendor_docs.
- **Field:** compliance group; nearest are gdpr_statement and data_residency (UK NHS data). No
  schema field for DSPT.
- **KB:** **no.** Profile lines 97-107 and matrix line 158 mention ISO, HIPAA, GDPR, PIPEDA and the
  ICO register but not DSPT.

### 7. iso27001: surveillance audit announced in release notes

- **Found:** the 2025-11-18 release notes announce the passed ISO 27001 surveillance audit. Still a
  vendor statement; the UKAS CertCheck page remains behind a CAPTCHA and was not attempted.
- **Quote:** https://forum.avicennaresearch.com/t/1443 : "We passed the ISO 27001 Surveillance Audit with flying colors, no non-conformities or improvement suggestions were found"
- **Source type:** vendor_page.
- **KB:** **yes** (profile line 99, legal-page wording). Adds a dated second vendor source only.

## Changes in the last 12 months

### 8. Wearable and sensor catalogue is much larger than the KB records

- **Found (release notes and blog):** Oura Ring integration (2026-01-06), Mira hormone monitor
  (2026-03-31), Buzud CGM (2026-09-08), WHOOP integration migrated to API v2 after v1 deprecation
  (2025-11-18). The Garmin blog gives SDK raw streams and rates: accelerometer 25 Hz, gyroscope
  32 Hz, beat-to-beat intervals, skin temperature, wrist status, zero crossing, HR or SpO2 sampling
  configurable from 1 s to 1 h, and the SDK route requires Garmin Connect to be uninstalled.
  Reference topics also exist for Fitbit, Polar, Hexoskin, BACtrack Skyn, SwitchBot, HealthKit,
  SensorKit, Weather, Environmental Sensors, Motion Sensors, Screen State, Battery, Keyboard, App
  Usage and Web Activity (titles seen in the forum Reference category; the doc researchers should
  confirm contents).
- **Quotes:**
  - https://forum.avicennaresearch.com/t/1482 : "Avicenna is integrated with Oura Ring"
  - https://forum.avicennaresearch.com/t/1508 : "Avicenna is now integrated with Mira"
  - https://forum.avicennaresearch.com/t/1618 : "We added support for Buzud continuous glucose monitoring (CGM)"
  - https://forum.avicennaresearch.com/t/1443 : "As WHOOP’s v1 APIs have been deprecated, we have migrated our integration to WHOOP API v2"
  - https://forum.avicennaresearch.com/t/1645 : "This can include 3-axis accelerometer data (25 Hz), gyroscope data (32 Hz), beat-to-beat intervals (inter-beat intervals/IBI), skin temperature, wrist status, and zero crossing"
  - https://forum.avicennaresearch.com/t/1645 : "You can also configure sampling rates for metrics such as heart rate or SpO2 from every 1 second to once an hour"
  - https://forum.avicennaresearch.com/t/1645 : "Requires Garmin Connect uninstalled; pairs directly with Avicenna"
- **Fields:** raw_streams, sampling_rates, deprecations (WHOOP v1).
- **Source type:** vendor_page (release notes, blog).
- **KB:** **no.** Matrix line 115 ("Wearables integrated per vendor; Garmin Health SDK ... confirmed");
  profile lines 34-55 (every phone stream except GPS and Bluetooth Unclear), line 153.

### 9. SensorKit access is brokered per study, with Apple approval

- **Found:** a 2026-07-20 guide: Apple grants the SensorKit entitlement per study and per app,
  Avicenna builds the study app and Bundle ID, the institution needs an Apple Developer
  Organization account whose Account Holder signs the SensorKit Addendum, and the Distribution
  entitlement needs ethics approval, consent text using Apple's descriptions and Apple committee
  review. This is a real gate on iOS passive data (device usage, keyboard metrics, phone and messages
  usage, speech metrics, visits).
- **Quotes:**
  - https://forum.avicennaresearch.com/t/1563 : "Apple reviews every request and grants the entitlement for a single study and a single app"
  - https://forum.avicennaresearch.com/t/1563 : "Build the study app and assign the Bundle ID"
- **Fields:** program_application (Apple-side approval), raw_streams.
- **Source type:** vendor_docs.
- **KB:** **no.** Profile has no SensorKit mention.

### 10. iOS app usage now collected via Screen Time

- **Found:** 2026-04-14 release added an iOS App Usage data source with hourly Screen Time-based
  summaries (app and website usage, notifications, pickups, no content).
- **Quote:** https://forum.avicennaresearch.com/t/1512 : "which collects hourly Screen Time–based usage summaries"
- **Field:** raw_streams. **Source type:** vendor_page.
- **KB:** **no.** Profile line 43 (App usage: Unclear / Unclear).

### 11. Derived metrics exist: nightly GPS mobility features and an Analysis page

- **Found:** a 2025-12-16 reference post (updated 2026-08-29) describes nightly computation of daily
  distance, radius of gyration, location entropy, time at home and daily location clusters; the
  2026-03-31 release added an Analysis page for data quality, engagement and retention.
- **Quotes:**
  - https://forum.avicennaresearch.com/t/1460 : "All of this runs in a nightly batch process"
  - https://forum.avicennaresearch.com/t/1460 : "Total distance travelled during the day Radius of gyration Location entropy Time spent at home"
  - https://forum.avicennaresearch.com/t/1508 : "We introduced the Analysis page in the researcher dashboard"
- **Field:** derived_metrics. **Source type:** vendor_docs, vendor_page.
- **KB:** **no.** Profile line 63 ("Not verified in any pass to date").

### 12. Pricing detail: SMS is billed at Twilio cost plus 30 percent

- **Found:** a 2026-06-01 blog (updated 2026-06-23) states SMS is off by default, enabled through
  support, and billed at Twilio's rate plus a 30% markup, including number-lease fees. The only
  published price mechanism found; licence prices are still non-public.
- **Quotes:**
  - https://forum.avicennaresearch.com/t/1540 : "The cost passed on to your study is the cost Twilio charges Avicenna for delivering each message plus 30% markup"
  - https://forum.avicennaresearch.com/t/1540 : "SMS notifications are not enabled by default"
- **Field:** api_platform_fees (usage fees). **Source type:** vendor_page.
- **KB:** **no.** Profile line 111 and matrix line 134 cover the trial only.

### 13. retention_terms and ai_training_terms

- **Found:** the legal page sets a minimum two-year retention after contract termination unless
  deletion is requested. No clause on AI or model training was found in the legal page (searched
  "train", "artificial", "machine learning", "OpenAI"). An experimental LLM "survey chatbot" built on
  TeleVisit chat was announced 2025-06-30 (updated 2026-09-06), not on the dashboard; the model
  provider and data flow are not stated.
- **Quotes:**
  - https://avicennaresearch.com/legal/ : "Avicenna Research will retain your data for a minimum period of two (2) years following contract termination"
  - https://forum.avicennaresearch.com/t/1295 : "This feature isn’t available on your researcher dashboard yet"
  - https://forum.avicennaresearch.com/t/1295 : "Participants will have conversations with AI as a way to respond to survey questions"
- **Source type:** vendor_legal, vendor_page.
- **KB:** **no.** Neither retention nor AI appears in the profile. ai_training_terms is a candidate
  `not_public` with the legal page in sources.

### 14. Android foreground notification is the collection keepalive

- **Found:** a 2026-08-11 participant guide (updated 2026-09-10) says Android shows a permanent,
  non-dismissable notification that is the main thing keeping the app alive; it can be switched off
  in-app. This is an on-device foreground service, not the server-triggered keepalive the KB
  question #107 asks about, so it does not overturn the KB finding, but the profile's flat "No
  phone-app keepalive" could mislead.
- **Quotes:**
  - https://forum.avicennaresearch.com/t/1574 : "Android shows a permanent Avicenna notification that cannot be swiped away"
  - https://forum.avicennaresearch.com/t/1574 : "it is the main thing keeping the app from being closed"
- **Field:** none in schema (matrix Table 8). **Source type:** vendor_docs.
- **KB:** partial. Profile line 93 and matrix line 180 say "No phone-app keepalive"; the foreground
  service is not mentioned.

## How researchers actually got the data (papers)

### 15. Recent deployments; one gives completeness and a data hand-off route

- **Sesikhona, rural South Africa** (JMIR mHealth uHealth 2025, 10.2196/67519, PMC12377519):
  white-labelled Android app, GPS every 30 min, hourly upload to an Avicenna-hosted server, then
  transferred to the institute's own MySQL database; only 28.4% of expected weekly points;
  frequent app terminations.
  - "customized into a smartphone app called" (probed at https://doi.org/10.2196/67519, `--fetch-url` Europe PMC full text)
  - "The data were then transferred from Avicenna to a MySQL database at AHRI" (same)
  - "on average, participants collected 95.3 out of the expected 336 points (28.4%) weekly" (same)
  - "the app was prone to frequent app terminations resulting in missing location data" (same)
  - **KB:** in the Module 3 scan list only (`module-03-applied-studies/_across-the-board-scan-2026-09.md` line 115); **no** in the profile or Module 2 literature library.
- **Stoma QoL EMA, Leeds** (JMIR 2025, 10.2196/57427, PMC12239683): chose the app for data
  protection compliance. Quote: "This app was selected due to its compliance with data protection regulations" (doi.org, `--fetch-url` Europe PMC). **KB: no.**
- **Hunger and glucose excursions, Texas A&M** (JMIR Form Res 2026, 10.2196/85897, PMC13251861):
  still cited as "Ethica Data", 6 prompts a day for 14 days. Quote: "Compliance was monitored throughout the study period using the Ethica platform" (doi.org, `--fetch-url` Europe PMC). **KB: no.**
- Other 2025-26 uses found but not probed: Pain 2026 (10.1097/j.pain.0000000000004020, Leiden),
  Suicide Life Threat Behav 2026 (10.1111/sltb.70136, UC Irvine), BMC Public Health 2025 protocol
  (10.1186/s12889-025-24461-x), BMJ Open 2026 protocol with ActiGraph (10.1136/bmjopen-2025-113370,
  in the Module 3 recency scan), JMIR mHealth 2025 weight management (10.2196/65260, in the Module 3
  recency scan). All are survey/EMA-only uses.
- **Source type:** paper. **Fields:** export_routes (hand-off), app_availability (white-label).

## Searched, nothing found

- Press releases, funding or acquisition news for Avicenna Research or Ethica Data, 2025-26 (web search): none.
- Job postings for Avicenna Research: none found.
- Partner or integrator pages (Fitabase, Labfront, Terra, Thryve) naming Avicenna or Ethica: none.
- openFDA 510(k) by applicant "avicenna" or "ethica": only an unrelated laser company (Avicenna Laser Technology); no clearance for this platform. fda_clearances is likely `not_applicable`.
- Avicenna or Ethica GitHub organisation with platform code: `avicennaresearch` has one repo (`ema_software_map`, last push 2024-07-25); no SDK or client.
- Forum search for "api key", "ApiKey", "api/v1", "REST", "programmatic", "self-host", "price", "pricing", "academic discount", "data residency", "server region": no public API docs and no price list.
- Legal page for AI or model-training terms: none.
- Academic or non-profit pricing programme: none found in the forum, FAQ or web search.
- UKAS CertCheck certificate: not attempted (CAPTCHA), per the rules.
- `acthealth.avicennaresearch.com` mirrors the main marketing site under an "ACT Health" title; purpose unclear, not pursued.
