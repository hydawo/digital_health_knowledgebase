# CARP gap hunt, 2026-10-11

Company: carp (CARP Mobile Sensing, Copenhagen Research Platform at DTU Health Tech, CARP Web Services).
Every quote below returned "exact" from `tools/facts/quote_probe.py` on 2026-10-11. Page dates come from the
carp.dk WordPress REST API (`/wp-json/wp/v2/posts` and `/pages`, `date` or `modified` field).

KB files checked: `module-02-digital-phenotyping/profiles/carp-mobile-sensing.md` (profile),
`module-02-digital-phenotyping/comparison-matrix.md` (matrix), `module-02-digital-phenotyping/README.md`,
`shared/unresolved-questions.md`, `facts/carp.yaml` (every field still `unresearched`).

The single most important source is **https://carp.dk/hosting/** ("Hosting at DTU", page modified 2026-08-23).
It is not in `facts/carp.yaml`'s watch list and is not cited anywhere in the KB. It carries a price list, the
eligibility rule and the data-processor terms for the hosted service.

---

## Contradictions

### 1. hosting_price / api_platform_fees / quote_required: the DTU-hosted service has a published price model
- **Found:** The hosting terms publish a price model. Normally the cost goes into the joint project budget; in
  smaller projects DTU applies "pay as you go" at actual cost plus 44% overhead, with a table of 2024 DKK prices:
  a one-time setup fee of 45.000 DKK (includes a disclosure agreement, not advanced data processing agreements)
  and hosting and maintenance at 1,250 DKK per study per month, plus staff time by role (student assistant to
  senior researcher). Invoiced typically once a year.
- **URL:** https://carp.dk/hosting/
- **Quotes (exact):**
  - "In smaller projects, we may apply a “pay as you go” price model, which follows the official DTU price model for research"
  - "we invoice for the actual cost plus a 44% overhead and include time spent monthly"
  - "The table below shows these prices (2024 prices in DKK)"
  - "Setting up a study incl. handling data disclosure" / "45.000 (one time)"
  - "General hosting, maintenance, and operation of studies on CAWS" / "1,250 pr. study"
  - "there is a monthly fee for operations and maintenance following the Computerome fee model"
  - "It includes making a disclosure agreement"
- **Date:** page modified 2026-08-23; prices labelled 2024. Note the "1,250 pr. study" cell sits in a column headed
  "Price pr. month"; the per-month reading comes from the column header, not the quoted cell.
- **Source type:** vendor_legal
- **KB:** **contradicts.** Profile line 13 "no price stated for the DTU-hosted service"; line 110 "No price is stated";
  line 131 "neither carp.dk page states a price"; matrix line 76 "**price not stated**", line 137 "price not stated";
  README lines 152-153 "Hosted-service prices are unpublished for ... CARP's DTU service".

### 2. program_eligibility / program_status: hosting is only for projects where DTU Health Tech is an active research partner
- **Found:** The hosting terms resolve the conflict the KB records between the CAWS page and "Three ways". The
  service is offered only when DTU Health Tech is an active research partner (helped initiate, fund, write the
  protocol, and publish). The 2026-09-28 app announcement says the same. Non-DTU researchers are therefore not
  excluded, but they must collaborate with DTU; it is not an open service.
- **URLs:** https://carp.dk/hosting/ ; https://carp.dk/new-carp-studies-app/ (posted 2026-09-28)
- **Quotes (exact):**
  - "this DTU hosting service is only provided for projects where we (DTU Health Tech) are an active research partner" (hosting)
  - "Researchers affiliated with DTU or cooperating with us can use this service" (hosting)
  - "Studies where DTU Health Tech is a research partner can use the CARP-hosted service at DTU" (new-carp-studies-app)
  - For comparison, CAWS page still says: "Researchers affiliated with DTU can use this service for creating CARP-based research projects" (https://carp.dk/caws, modified 2026-05-05)
- **Source type:** vendor_legal (hosting); vendor_page (news post)
- **KB:** **contradicts / resolves open item.** Profile line 95 "Conflict on who can use the hosted instance", line 177
  "Still open: whether non-DTU researchers can get accounts"; matrix line 220 "access terms conflict";
  README line 153 "contradictory on its own pages"; unresolved-questions.md line 130 (Q131). The hosting page
  is the controlling document and was not read.

### 3. app_availability: CARP Studies is on the Apple App Store (unlisted) since 2025
- **Found:** DTU published CARP Studies on the App Store as an unlisted app, which is why store search does not find
  it. Apple lookup API (id 1569798025, DK storefront) returns seller "Danmarks Tekniske Universitet", version 5.1.0,
  first release 2025-03-21, current version released 2026-10-06. Version 5 (rebuilt app) announced 2026-09-28
  for Android and iOS. In mainland China the iOS app is distributed via TestFlight and Android via a sideloaded APK.
- **URLs:** https://carp.dk/carp-studies-app-published-in-the-apple-app-store/ (posted 2025-04-22);
  https://apps.apple.com/dk/app/carp-studies/id1569798025 ; https://carp.dk/carp-studies-app/ ;
  https://carp.dk/new-carp-studies-app/ ; https://carp.dk/join/ (posted 2026-10-05)
- **Quotes (exact):**
  - "Note that this is an unlisted app and hence cannot be found using search in the app store" (app-store post)
  - "Danmarks Tekniske Universitet" and "CARP Studies" (App Store page)
  - "the CARP Studies app is available from the DTU account in the Apple App Store and Google PLAY" (carp-studies-app page)
  - "Version 5 is out now for Android and iOS" (new-carp-studies-app)
  - "The iOS app is not published in the China App Store, so iOS users there install through TestFlight" (join)
- **Source type:** vendor_page; app_store
- **KB:** **contradicts.** Profile line 10 "no App Store listing was found on 2026-10-10 (Unclear)"; matrix line 54
  "DTU's 'CARP Studies' app not found on the App Store (Unclear)" and "reference app on iOS Unclear".

### 4. academic_vs_commercial / adoption: CARP itself names Geneva as an international user
- **Found:** The 2023 Novo Nordisk Foundation grant post claims international use at Leuven and Geneva. The KB says
  only one non-DTU deployment (KU Leuven, m-Path Sense) was confirmed. Geneva is a vendor claim, not verified.
- **URL:** https://carp.dk/funding-from-the-novo-nordisk-foundation/ (posted 2023-05-30)
- **Quote (exact):** "CARP is also used internationally by research institutions like the Universities of Leuven and Geneva"
- **Source type:** vendor_page
- **KB:** **contradicts in part.** Profile lines 139-142 ("one confirmed production deployment ... outside DTU");
  unresolved-questions.md line 385 (Q94). Geneva not mentioned anywhere.

## Missing programs and terms

### 5. research_program: Novo Nordisk Foundation infrastructure grant (DKK 5 million) and Danish Life Science Infrastructure
- **Found:** NNF funds CARP to run as part of the Danish Life Science Infrastructure on Computerome, with the stated
  aim of serving researchers, companies and students, including training material, workshops and conferences.
  This is the funding basis of the hosted service.
- **URL:** https://carp.dk/funding-from-the-novo-nordisk-foundation/ (posted 2023-05-30)
- **Quotes (exact):**
  - "The Novo Nordisk Foundation (NNF) has recently decided to fund CARP with a DKK 5 million grant (EUR 700 000)"
  - "The goal is to make CARP available for researchers, companies, and students within digital health"
- **Source type:** vendor_page
- **KB:** **no.** Not in the profile or matrix. Note the tension with finding 2 (stated goal includes companies;
  hosting terms restrict to research with DTU as partner).

### 6. research_program: CAG DIGITAL clinical academic group (Greater Copenhagen Health Science Partners)
- **Found:** A new Clinical Academic Group on digital phenotyping for home-based care, with CARP as its
  infrastructure and testbed foundation.
- **URL:** https://carp.dk/cag-digital/ (posted 2025-09-24)
- **Quote (exact):** "The Copenhagen Research Platform (CARP) plays a central role in CAG DIGITAL"
- **Source type:** vendor_page
- **KB:** **no.**

### 7. dpa / baa: outside partners can become data processors under a DTU DPA; joint controllership possible; research-only use
- **Found:** On the hosted service DTU is controller and will not sign a processor contract as processor. But data
  can be shared three ways: aggregate only, disclosure of selected items under a small contract, or the outside
  partner becomes a data processor under a full DTU data processor agreement. In large funded projects a joint
  data controller setup is possible. The service cannot be used for clinical treatment or commercial services.
  No BAA or HIPAA mention.
- **URL:** https://carp.dk/hosting/
- **Quotes (exact):**
  - "Research partners outside of DTU can become Data Processors"
  - "a full data processor agreement needs to be in place between DTU and the outside partner"
  - "we may agree on a “Joint Data Controller” setup"
  - "this hosted service cannot be used for purposes other than research, such as in clinical treatment or for commercial services"
- **Source type:** vendor_legal
- **KB:** **partly.** Profile line 127 and matrix line 161 record "DTU cannot act as a data processor" and EU/EEA
  residency, from "Three ways". The reverse-direction DPA, joint controllership and research-only restriction are absent.

### 8. retention_terms / ai_training_terms: participant privacy policy sets minimum five-year retention and service-improvement use
- **Found:** The app privacy policy (covers CARP Studies, Neuropathy Tracker, mCAT, ICAT; modified 2026-10-05)
  keeps data for at least five years, allows use of personal data to improve apps and services, rules out sale,
  and keeps nothing permanently on the phone. No statement on AI or ML model training specifically.
- **URL:** https://carp.dk/privacy-policy-app/
- **Quotes (exact):**
  - "and for at least five years"
  - "We may use your personal data to improve our Applications and Services and to correct or modify software settings"
  - "We will never donate or sell your personal data to anyone during or after a Study"
  - "No data is stored permanently on the smartphone"
- **Source type:** vendor_legal
- **KB:** **no.** No retention or secondary-use terms in profile or matrix. Researcher-side policy
  (https://carp.dk/privacy-policy-service/, modified 2026-08-23) adds "The CARP server is hosted within the EU" (exact).

### 9. hosting_options / sla: no SLA of any kind on the hosted service
- **URL:** https://carp.dk/hosting/
- **Quote (exact):** "We do not provide any service-level agreements (SLAs) or any service guarantees whatsoever"
- **Source type:** vendor_legal
- **KB:** **yes, in substance** (profile line 110 "best-effort basis", from the CAWS page). Hosting page is stronger
  wording; worth citing.

### 10. deprecations: CAMS API 2.0 (April 2026) is a breaking redesign
- **Found:** Major version with restructured packages, multi-study client manager, persistent runtime state,
  executor states renamed ("resumed"/"paused"), configuration moved to the client only. GitHub release v2.0.0
  published 2026-04-27; previous release v1.4.0 (2023-11-26). New docs site docs.carp.dk; support moved to Discord.
- **URL:** https://carp.dk/carp-mobile-sensing-api-2-0-released/ (posted 2026-04-14)
- **Quotes (exact):**
  - "now at API level 2.0"
  - "Simplified configuration – now only the client and not the controller needs configuration"
  - "A new documentation site has been released alongside API 2.0"
  - "Community interaction and support are now handled via Discord"
- **Source type:** vendor_page; repository (GitHub releases API)
- **KB:** **no.** Profile does not mention API 2.0, docs.carp.dk or Discord; facts watch list lacks docs.carp.dk.

### 11. raw_streams / derived_metrics: CARP Studies v5 data catalogue, plus planned Gardener cloud-API route
- **Found:** The v5 announcement lists what the app collects today: location and mobility, activity, Apple Health /
  Health Connect (steps, distance, heart rate, sleep and stages, skin temperature), Polar and Movesense HR/ECG,
  microphone noise and recordings, photos/video, weather and air quality, battery, screen on/off, connectivity,
  surveys and cognitive tests (e.g. Flanker). Android asks to be exempt from battery optimisation; iOS uses "Always"
  location. Sign-in by QR or short code. English, Danish, Spanish. Server-fed weekly cards for steps, HR, sleep.
  Planned: Garmin, Fitbit, Withings, Dexcom via CARP Gardener.
- **URL:** https://carp.dk/new-carp-studies-app/ (posted 2026-09-28)
- **Quotes (exact):**
  - "Battery level, screen on/off, network connectivity"
  - "Steps, distance, heart rate, sleep and sleep stages, skin temperature"
  - "on Android, to be excluded from battery optimisation"
  - "Sign in by scanning a QR code or typing a short code"
  - "Android and iOS , in English, Danish and Spanish"
  - "Through the CARP Gardener framework, future studies will be able to collect health and activity data from"
- **Source type:** vendor_page
- **KB:** **no / partly.** Profile stream table (lines 43, 45, 53) has screen state, battery and notifications as
  Unclear; this post states screen and battery as collected (platform parity not stated). Active Data Collection
  (line 74) and Participant Experience (line 117) say "Not verified in any pass to date"; this post covers both.

### 12. export_routes / raw_streams: CARP Gardener (server-side wearable cloud APIs) exists as code
- **Found:** Repository supporting Fitbit, Garmin, Withings and Dexcom via OAuth, feeding CAWS. MIT, last push 2025-12-15.
- **URL:** https://github.com/carp-dk/carp-gardener
- **Quote (exact):** "CARP Gardener collects wearable activity and health data from third-party services"
- **Source type:** repository
- **KB:** **no.** Matrix line 118 integration list lacks Garmin, Fitbit, Withings, Dexcom cloud.

### 13. raw_streams: Apple Watch sampling package via AWARE watchOS
- **Found:** `carp_aware_package` (MIT, pushed 2026-10-08) wraps the AWARE watchOS framework for raw motion, HR,
  battery, location, heading, Bluetooth, ambient noise and sound classification from an Apple Watch. iOS/watchOS
  only, needs a companion watch app. Also a cross-platform link to the KB's AWARE profile.
- **URL:** https://github.com/carp-dk/carp_aware_package
- **Quotes (exact):**
  - "This library contains a sampling package for collecting passive sensor data from an Apple Watch"
  - "This package is iOS / watchOS only"
- **Source type:** repository
- **KB:** **no.**

### 14. derived_metrics: CARP DSP data-science pipeline framework
- **Found:** `carp-dsp` (MIT, pushed 2026-09-24): Kotlin Multiplatform pipelines with Python/conda execution over
  CARP data; companion `carp-dsp-portal` repo (pushed 2026-10-06). Relevant to the profile's "no Forest-comparable
  derived-metrics catalog" line.
- **URL:** https://github.com/carp-dk/carp-dsp
- **Quote (exact):** "A Kotlin Multiplatform framework for CARP (Copenhagen Research Platform) data science and analytics processing"
- **Source type:** repository
- **KB:** **no.** Profile line 70.

### 15. sampling_rates / data completeness: CARP's own coverage tests on Android 14 and iOS 18
- **Found:** DTU tests (CATCH project, GitHub issue #475) show both OSes pause or kill the app without user
  interaction; a connected BLE wearable gives full coverage; on iOS no data is collected overnight without
  interaction or a connected device.
- **URL:** https://carp.dk/coverage-analysis-on-android-14-and-ios-18/ (posted 2025-03-12)
- **Quotes (exact):**
  - "Android 14 and iOS 18 will aggressively try to pause or kill your app , if not used by the user"
  - "If the app is connected to a wearable device (like a HR monitor) using BLE, this will keep the app running in the background and give a 100% sampling coverage"
  - "But if there is no user interaction, no data is collected, such as during the 2nd night"
- **Source type:** vendor_page
- **KB:** **no.** Profile lines 119-123 cover the heartbeat measure and absence of a keepalive, but not these results.
  Directly relevant to unresolved-questions Q107 and Q111.

### 16. export_routes / deprecations: open upload bug can stall all uploads
- **Found:** Open issue #623 (updated 2026-09-21): CAWS accepts or rejects the whole multi-stream batch, so one
  rejected measurement causes the batch to be retried forever. Fix proposed in open PR #624. Data-completeness risk
  for current deployments.
- **URL:** https://github.com/carp-dk/carp.sensing-flutter/issues/623
- **Quote (exact):** "the same batch is retried forever - no data is ever uploaded again"
- **Source type:** repository
- **KB:** **no.** (Read only; nothing was opened or commented.)

### 17. Evidence of use: UbiLife study on CARP Studies (82 participants at UbiComp 2025; rerun Oct 2026)
- **URL:** https://carp.dk/ubilife/ (posted 2026-09-28)
- **Quotes (exact):**
  - "A total of 82 conference participants joined the study"
  - "In October 2026, we are running UbiLife again at UbiComp/ISWC 2026 in Shanghai, China"
- **Source type:** vendor_page
- **KB:** **no.** DTU-run, so it does not change the external-adoption reading; a Module 3 candidate once published.

---

## Searched, nothing found
- FDA 510(k)/De Novo or CE/MDR for CARP or CARP Studies: none found; the hosting terms rule out clinical treatment use, so `fda_clearances` is likely not_applicable.
- ISO 27001 / SOC 2 / trust portal for CARP or Computerome: none found (web search 2026-10-11; comparable Danish HPC centres such as SDU and GenomeDK are certified, Computerome not confirmed).
- HIPAA / BAA: no mention on hosting, CAWS or either privacy policy.
- Integrator pages (Fitabase, Labfront, Terra, Thryve): no CARP integration found; CARP integrates the other way via Gardener.
- Job postings: not searched in depth (no hits surfaced in general searches).
- Other carp.dk posts reviewed and not material here: live monitoring screens (2026-05-13), mCAT release (2026-09-22), Neuropathy Tracker release and validation (2026-03-24, 2026-06-03), team merch, Flutter course (2025-06-24).
- GitHub: 50 most recently updated issues/PRs in carp.sensing-flutter scanned (no deprecation or licence change; issue #607, #613, #630 are routine fixes); org repo list scanned (all core repos MIT; carp-docs-starlight, carp-dsp-portal and carp-app-site-ts have no licence declared).

## Suggested watch-list additions for facts/carp.yaml
- https://carp.dk/hosting/ (pricing, terms)
- https://carp.dk/privacy-policy-app/ and https://carp.dk/privacy-policy-service/ (terms)
- https://apps.apple.com/dk/app/carp-studies/id1569798025 and the Google Play listing (app_store)
- https://docs.carp.dk/carp-mobile-sensing/ (docs)
- https://github.com/carp-dk/carp-gardener (repository)
