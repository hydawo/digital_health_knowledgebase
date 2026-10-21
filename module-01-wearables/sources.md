# Module 1 — Sources

All sources accessed **2026-08-21** unless otherwise noted. "Retrieval" records how the source was
consulted, because it determines the confidence label a claim can carry.

- **Direct** — page fetched and read in this session (supports **Verified**)
- **Search summary** — established via search result summarization of the named source (supports
  **Corroborated** at best)
- **Secondary** — third-party reporting about a primary source (supports **Reported**)

---

## Apple

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-APL-01 | HealthKit | Apple | https://developer.apple.com/documentation/healthkit | Developer docs | Direct (title only returned) | Framework exists; content not extractable |
| S-APL-02 | Accessing SensorKit Data | ResearchKit & CareKit (Apple-affiliated) | https://www.researchandcare.org/resources/accessing-sensorkit-data/ | Research guidance | **Direct** | SensorKit data categories; private entitlement; IRB requirement; sensorkitrequest@apple.com; institution-owned developer account; background execution limits |
| S-APL-03 | ResearchKit & CareKit FAQ | researchandcare.org | https://www.researchandcare.org/faq/ | FAQ | **Direct** | HealthKit access model; higher-frequency HR only in Workouts/ECG sessions; statement that raw ECG is not accessible; Study App Template Re-read 2026-10-09: still says "You cannot access raw ECG data through HealthKit" (undated page); outranked by S-APL-04 for recorded ECGs. |
| S-APL-04 | HKElectrocardiogram | Apple | https://developer.apple.com/documentation/healthkit/hkelectrocardiogram | Developer docs | Search summary | ECG samples are voltage collections; `HKElectrocardiogramQuery` returns individual measurements; sampling frequency and count properties **Re-read Direct 2026-10-09** via the `developer.apple.com/tutorials/data/documentation/healthkit/*.json` endpoint: `HKElectrocardiogramQuery` "returns the underlying voltage measurements for an electrocardiogram sample"; read-only access to Apple Watch ECGs; iOS 14 / watchOS 7. Resolves the conflict with S-APL-03 for discrete recordings. **Reopened 2026-10-11:** the fact record keeps it as a conflict over whether this waveform counts as raw (`../facts/apple.yaml` raw_streams, HealthKit ECG). |
| S-APL-05 | Investigator Support Program | researchandcare.org | https://www.researchandcare.org/investigator-support-program/ | Program page | Search summary | Apple provides devices and development resources to researchers |
| S-APL-06 | Apple Heart & Movement Study FAQ | Brigham and Women's Hospital | https://appleheartandmovementstudy.bwh.harvard.edu/frequently-asked-questions/ | Study site | Search summary | Study design; Apple-sponsored; AHA and BWH partners; data types collected |
| S-APL-07 | Apple debuts Apple Watch Series 11 | Apple Newsroom | https://www.apple.com/newsroom/2025/09/apple-debuts-apple-watch-series-11-featuring-groundbreaking-health-insights/ | Press release | Secondary | Sept 2025 launch; hypertension notifications; sleep score; sensor complement |
| S-APL-08 | Introducing Apple Watch Ultra 3 | Apple Newsroom | https://www.apple.com/newsroom/2025/09/introducing-apple-watch-ultra-3/ | Press release | Secondary | Ultra 3 sensors incl. depth gauge and water temperature |
| S-APL-09 | SensorKit SRSensor, SRPhotoplethysmogramSample, sensorkit.reader.allow entitlement | Apple | https://developer.apple.com/documentation/sensorkit/srsensor | Developer docs | **Direct** (JSON endpoint, 2026-10-10) | PPG and ECG iOS 17.4; accelerometer iOS 14; full sensor list; PPG sample fields and usage values; per-study approval and provisioning |
| S-APL-10 | Research app | Apple | https://www.apple.com/ios/research-app/ | Product page | **Direct** (2026-10-10) | Apple Health Study (initiated early 2025, BWH), Women's Health Study, Hearing Study |

## Fitbit / Google

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-FIT-01 | Fitbit Web API reference | Google/Fitbit | https://dev.fitbit.com/build/reference/web-api/ | API docs | **Direct** | 24 endpoint categories; intraday definition. **Support ended 30 Sep 2026, turned off 30 Oct 2026** (re-read 2026-10-10; see S-FIT-14). The 2026-08-21 reading recorded only a September 2026 deprecation notice |
| S-FIT-02 | Application Design | Google/Fitbit | https://dev.fitbit.com/build/reference/web-api/developer-guide/application-design/ | API docs | **Direct** | Personal/Client/Server app types; **150 req/hr per consented user**; rate-limit headers; intraday approval process |
| S-FIT-03 | Intraday | Google/Fitbit | https://dev.fitbit.com/build/reference/web-api/intraday/ | API docs | Search summary | 1s/1min/5min/15min detail levels; **24-hour retrieval limit on intraday HR, degrading to summary** |
| S-FIT-04 | About the Google Health API | Google | https://developers.google.com/health/about | Developer docs | **Direct** | Successor to Fitbit Web API; data type roadmap Q2/Q3 2026; all Fitbit + Pixel devices; Google OAuth 2.0; **most scopes Restricted** (corrected 2026-10-10 from "all"; app-verification page says "Most scopes"); Reconciled Stream. Re-read 2026-10-10: see S-FIT-14 for shutdown dates and the onboarding pause |
| S-FIT-05 | Google Health API REST reference | Google | https://developers.google.com/health/reference/rest | API reference | **Direct** | v4 resources: subscribers, subscriptions, users, dataTypes.dataPoints (incl. rollUp, dailyRollUp, reconcile, exportExerciseTcx), pairedDevices; endpoint `health.googleapis.com` |
| S-FIT-06 | Introducing the next phase of the Fitbit Web API | Fitbit Community | https://community.fitbit.com/t5/Web-API-Development/Introducing-the-next-phase-of-the-Fitbit-Web-API/td-p/5821061 | Vendor forum | Search summary | Migration announcement |
| S-FIT-07 | Fitbit to Google Health API Developer Transition Guide | Validic | https://help.validic.com/space/VCS/5513478151/Fitbit+to+Google+Health+API+Developer+Transition+Guide | Vendor guide | Secondary | Migration mechanics; **mandatory user re-consent** |
| S-FIT-08 | Fitbit Web API Shutdown | Sahha | https://sahha.ai/blog/fitbit-api-sunset-migration/ | Vendor blog | Secondary | Side-by-side window May–30 Sept 2026. **Superseded:** Google states support ended 30 Sep and the API is turned off 30 Oct 2026 (S-FIT-14) |
| S-FIT-09 | Fitbit API Deprecation | Thryve | https://www.thryve.health/blog/fitbit-api-deprecation | Vendor blog | Secondary | Corroborates re-consent and OAuth change |
| S-FIT-10 | Health Connect data types | Google/Android | https://developer.android.com/health-and-fitness/health-connect/data-types | Developer docs | Search summary | 50+ data types; Record subclasses; Medical Records in FHIR; Google Fit supported to end of 2026 |
| S-FIT-11 | The All of Us Research Program's wearables dataset | NIH / *Nature Medicine* | https://www.nature.com/articles/s41591-026-04352-3 | Peer-reviewed | Search summary | 59,000+ participants; 14 years; 39M step, 31M sleep observations; 46% multi-modal linkage |
| S-FIT-12 | Resources for Using Fitbit Data | All of Us | https://support.researchallofus.org/hc/en-us/articles/20281023493908-Resources-for-Using-Fitbit-Data | User support | Search summary | Seven BigQuery tables; minute-level HR and steps; not OMOP CDM |
| S-FIT-13 | The Importance of Data Quality Control in Using Fitbit Device Data From the All of Us Research Program | *JMIR mHealth uHealth* 2023 | https://mhealth.jmir.org/2023/1/e45103 | Peer-reviewed | Search summary | Wear-time and completeness filtering materially affect results |
| S-FIT-14 | About the Google Health API (site-wide notice) | Google | https://developers.google.com/health/about | Developer docs | **Direct** (2026-10-10) | Fitbit Web API support ended 30 Sep 2026, turned off 30 Oct 2026; "not onboarding new projects at this time" (2026-10-10); sentence removed by 2026-10-19, page now says "Get started now" (weekly check) |
| S-FIT-15 | Google Health API User Data and Health Research Policy | Google | https://developers.google.com/health/policies/health-api-user-data-and-research-policy | Policy | **Direct** (2026-10-10) | Effective 24 Mar 2026; Review Board approval or waiver; Health Research Attestation (intake form, IRB letter, accreditation, data rationale); disclosures incl. retention and deletion; immediate de-identification; no new-study sharing without consent; PHI only under IRB-reviewed HIPAA Authorization; notify Fitbit Publication Library |
| S-FIT-16 | Google Health API Research Pledge | Google | https://developers.google.com/health/policies/health-api-research-pledge | Policy | **Direct** (2026-10-10) | Effective 24 Mar 2026; consent, ethics review, minimisation, Certificate of Confidentiality, no sale or re-identification |
| S-FIT-17 | Google Health API data types and Vitals guide | Google | https://developers.google.com/health/data-types ; https://developers.google.com/health/data-types/vitals | Developer docs | **Direct** (2026-10-10; updated 2026-10-06) | Heart Rate Sample at 1 s storage resolution; HRV Sample; SpO2 Sample at 1 min; ECG session with raw waveform voltage samples; no Readiness, Sleep Score or Stress type; Fitbit Air listed |
| S-FIT-18 | Google Health API Developer Terms | Google | https://developers.google.com/health/policies/health-api-developer-terms-and-conditions | Terms | **Direct** (2026-10-10; updated 2026-09-25) | HIPAA use limitation; no BAA offered |
| S-FIT-19 | Unverified apps (internal-use exception) | Google Cloud Help | https://support.google.com/cloud/answer/13464323 | Help page | **Direct** (2026-10-10) | Internal Use apps limited to the owning Workspace/Cloud Identity organization; exempt from 100-user cap |

## Garmin

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-GRM-01 | Health API | Garmin | https://developer.garmin.com/gc-developer-program/health-api/ | Developer docs | **Direct** | Data summaries; Ping/Pull or Push; JSON; commercial use requires licence fee; connect-support@developer.garmin.com |
| S-GRM-02 | Health SDKs Overview | Garmin | https://developer.garmin.com/health-sdk/ | Developer docs | **Direct** | **Live accelerometer, HR, Pulse Ox, respiration, stress streaming**; Standard vs Companion; Standard described as HIPAA-compliant; evaluation free, commercial requires licence fee or device MOQ |
| S-GRM-03 | Health SDK Questions & Answers | Garmin | https://developer.garmin.com/health-sdk/questions-answers/ | Developer FAQ | **Direct** | Real-time streaming + configurable logged data; enterprise framing; contact-gated specifics |
| S-GRM-04 | Program FAQ | Garmin | https://developer.garmin.com/gc-developer-program/program-faq/ | Developer FAQ | **Direct** | Application reviewed in 2 business days; integration 1–4 weeks; no licensing/maintenance fees but some metrics may require a licence fee; "only for business use". Re-read 2026-10-10: wording unchanged, but stale while new access requests are paused (S-GRM-07 to S-GRM-09) |
| S-GRM-05 | Enable Digital Phenotyping with Garmin Devices | Center for Technology and Behavioral Health, Dartmouth | https://www.c4tbh.org/research-tools/enable-digital-phenotyping-with-garmin-devices-in-your-longitudinal-research-studies/ | Academic center | **Direct** | Independent confirmation that the Companion SDK yields **raw accelerometer, beat-to-beat intervals, respiration**; academic partnership with Garmin exists |
| S-GRM-06 | Garmin data source documentation | Rook | https://docs.tryrook.io/data-sources/garmin/ | Integrator docs | Secondary | 16 data types; backfill types on first connect |
| S-GRM-07 | Garmin Connect Developer Program overview | Garmin | https://developer.garmin.com/gc-developer-program/overview/ | Developer docs | **Direct** (2026-10-10) | No request link; "Stay tuned for more updates on the program" |
| S-GRM-08 | Developer forum thread on paused applications | Garmin forum | https://forums.garmin.com/developer/connect-iq/f/discussion/434798/cannot-access-developer-program-application-form-under-construction/2027757 | Forum | **Direct** (2026-10-10) | Quoted Garmin reply: "new access requests are temporarily paused" |
| S-GRM-09 | Garmin's Connect Developer Program is paused | Terra | https://tryterra.co/blog/garmin-connect-developer-program-pause | Vendor blog | Secondary | Dated 7 Sep 2026; form "Under Construction" by spring 2026; no reopening date |
| S-GRM-10 | Health SDK overview | Garmin | https://developer.garmin.com/health-sdk/overview/ | Developer docs | **Direct** (2026-10-10) | Enterprise partners only; evaluation free, commercial licence fee or MOQ; Accelerometer and Enhanced BBI streaming and logging; Standard SDK "HIPAA-compliant" vendor statement |
| S-GRM-11 | Historical Data Availability | Open Wearables | https://openwearables.io/docs/providers/historical-data | Integrator docs | Secondary | Garmin backfill limited to 30 days before consent; HISTORICAL_DATA_EXPORT permission |
| S-GRM-12 | Research Grants | Fitrockr | https://www.fitrockr.com/research/research-grants/ | Vendor page | **Direct** (2026-10-10) | Garmin Health x Fitrockr Asia 2026 grant closed 31 Mar 2026; no current grant |

## Oura

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-OUR-01 | Oura API Documentation (2.0) | Oura | https://cloud.ouraring.com/v2/docs | API docs | **Direct (browser)** | Full route inventory; OAuth 2.0 only; **PAT deprecation Dec 2025**; scopes; **10-user application cap**; two-tier rate limits; 5,000 req/5 min (**superseded 2026-10-11**: the OpenAPI 1.41 FAQ section does publish 5,000 per 5 minutes; only the newer Rate Limits section gives no number; see `../facts/oura.yaml` rate_limits); webhooks ~30s; **sleep syncs only on user app-open**; 403 on expired subscription; API free for personal and commercial use |
| S-OUR-02 | Error Handling | Oura | https://cloud.ouraring.com/docs/error-handling | API docs | Search summary | Rate-limit behaviour |
| S-OUR-03 | Oura for Organizations | Oura | https://ouraring.com/business | Product page | Search summary | Enterprise offering; 200+ customers incl. USAF, Navy, Army, NASA, universities |
| S-OUR-04 | Explore the Technology in Oura Ring 4 / Smart Sensing | Oura | https://ouraring.com/blog/technology-in-oura-ring-4/ · https://ouraring.com/blog/smart-sensing/ | Vendor blog | Search summary | 18-pathway PPG; IR alignment sensor; NTC thermistor; vendor-claimed signal-quality improvements |
| S-OUR-05 | Study from Top US Hospital Finds Oura Ring Most Accurate | Oura | https://ouraring.com/blog/2024-sensors-oura-ring-validation-study/ | Vendor blog on peer-reviewed work | Search summary | Robbins 2024 kappa figures as promoted by Oura |
| S-OUR-06 | The Oura API | Oura Member Care | https://support.ouraring.com/hc/en-us/articles/4415266939155-The-Oura-API | Support | Search summary | Consumer-facing API description |
| S-OUR-07 | Oura API v2 OpenAPI spec 1.41 | Oura | https://cloud.ouraring.com/v2/static/json/openapi-1.41.json | API spec | **Direct** (accessed 2026-10-10) | PATs retired; 10-user cap before approval; two-layer rate limits, no numbers; webhooks (30 s, 10 retries); HR in 5-min increments; 403 on expired membership; route list; no BP/GLP-1 route |
| S-OUR-08 | Oura API and MCP Agreement (effective 2026-06-08) | Oura | https://cloud.ouraring.com/legal/api-agreement | Legal terms | **Direct** (accessed 2026-10-10) | Retention "strictly necessary"; 72-hour deletion; AI/ML training bans (§4(a)(iii), §6(g)); benchmarking clause; aggregator approval |
| S-OUR-09 | Oura for research (Organizations) | Oura | https://organizations.ouraring.com/solutions/researchers | Vendor page | **Direct** (accessed 2026-10-10) | Research dashboards, group download, raw CSV/JSON export, API integration, premium metrics for academics, HIPAA/GDPR claim, contact only |
| S-OUR-10 | Oura membership | Oura | https://ouraring.com/membership | Pricing page | **Direct** (accessed 2026-10-10) | $5.99/month or $69.99/year (US, before tax) |
| S-OUR-11 | Oura trust centre | Oura | https://ouraring.com/trust-center | Security page | **Direct** (accessed 2026-10-10) | HITRUST; annual audit under SOC 2 heading; HIPAA for healthcare partners; encryption |
| S-OUR-12 | Oura Research app | Oura Health Oy | https://apps.apple.com/us/app/oura-research/id6748037636 | App Store listing | **Direct** (accessed 2026-10-10) | Participant research app; v1.0 (22 April) to v1.0.11 (15 September) |
| S-OUR-13 | Oura Ring 5 launch coverage | Pulse 2.0 | https://pulse2.com/oura-reveals-399-oura-ring-5-as-the-worlds-smallest-smart-ring/ | Press | Secondary (accessed 2026-10-10) | Ring 5 $399/$499, introduced 2026-05-28. Prices since read from the US store (`../facts/oura.yaml` device_price, 2026-10-10) |

## WHOOP

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-WHP-01 | **WHOOP API Terms of Use** | WHOOP | https://developer.whoop.com/api-terms-of-use/ | Legal | **Direct** | **No permanent copies / databases**; no marketing/selling/licensing/leasing data even with consent; **no HIPAA representation**; non-compete; deletion on termination; encryption obligations. **Superseded by S-WHP-07** (terms effective 2026-10-06, read in full 2026-10-10), which adds the AI/ML training ban |
| S-WHP-02 | WHOOP Developer Platform introduction | WHOOP | https://developer.whoop.com/docs/introduction/ | Developer docs | **Direct** | v2 API; v1 webhooks removed; Recovery/Sleep/Strain/Workouts; app approval required |
| S-WHP-03 | API Rate Limiting | WHOOP | https://developer.whoop.com/docs/developing/rate-limiting/ | Developer docs | Search summary | **100 req/min, 10,000 req/day per client**; rate-limit headers; increases on request |
| S-WHP-04 | Getting Started | WHOOP | https://developer.whoop.com/docs/developing/getting-started/ | Developer docs | Search summary | Six scopes: recovery, cycles, workout, sleep, profile, body_measurement |
| S-WHP-05 | Whoop 5.0 vs Whoop MG | Wareable | https://www.wareable.com/wearable-tech/whoop-5-vs-whoop-mg-which-membership-explained | Trade press | Secondary | Membership tiers and pricing; MG ECG and BP insights; sensor claims |
| S-WHP-06 | WHOOP Unite / Ashley Addiction Treatment partnership | Business Wire | https://www.businesswire.com/news/home/20221110005420/en | Press release | Secondary | WHOOP Unite exists and has been used in a clinical research partnership |
| S-WHP-07 | WHOOP API Terms of Use (effective 2026-10-06) | WHOOP | https://developer.whoop.com/api-terms-of-use/ | Legal terms | **Direct, full text** (accessed 2026-10-10) | Permanent-copy and AI/ML bans with data-owner exception; HIPAA clause; user cap; no charge; medical-device ban |
| S-WHP-08 | App Approval (member tiers) | WHOOP | https://developer.whoop.com/docs/developing/app-approval | Developer docs | **Direct** (accessed 2026-10-10) | Sandbox 10, Build 100, Growth 1,000, Scale 5,000, Production; 50% rule; manual review |
| S-WHP-09 | openFDA K243236 | FDA | https://api.fda.gov/device/510k.json?search=k_number:K243236 | Regulatory database | **Direct** (accessed 2026-10-10) | WHOOP ECG Feature (1.0), 2025-04-04, QDA; only WHOOP 510(k) |
| S-WHP-10 | Warning letter 709755 (2025-07-14) and close-out (2026-06-17) | FDA | https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/warning-letters/whoop-inc-709755-07142025 · https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/warning-letters/whoop-inc-709755-06172026 | Regulatory letters | **Direct** (accessed 2026-10-10) | BPI marketed without clearance; enforcement discretion for BPI as modified |
| S-WHP-11 | WHOOP Unite and Ashley Addiction Treatment | Business Wire | https://www.businesswire.com/news/home/20221110005420/en/ | Press release | Search summary (2026-10-10) | Unite and Gateway in a research partnership, Nov 2022 |

## Samsung

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-SAM-01 | Privileged Health SDK FAQ (SDK renamed **Samsung Health Sensor SDK**, v1.4.1; current FAQ at https://developer.samsung.com/health/sensor/faq.html, see S-SAM-08) | Samsung | https://developer.samsung.com/health/privileged/faq.html | Developer FAQ | **Direct** | **Accelerometer 25 Hz, HR with IBI, PPG, skin temperature continuous; BIA and ECG on-demand, one at a time**; Watch4+ Wear OS powered by Samsung; Partner Program request; package name + SHA-256; `SDK_POLICY_ERROR`; **does not share data with Samsung Health** Re-read 2026-10-09: page now titled Samsung Health Sensor SDK; still "Galaxy Watch4 and later". |
| S-SAM-02 | Samsung Health SDK Suite announcement | Samsung Mobile Press | https://www.samsungmobilepress.com/articles/samsungs-new-health-software-development-kit-suite-powers-advancements-in-healthcare-innovation | Press release | Search summary | Sept 2024 SDK Suite; Sensor/Data/Accessory/Research components; **continuous PPG IR and Red LED access for the first time** |
| S-SAM-03 | Samsung Electronics Unveils Samsung Health Research Stack | Samsung Newsroom | https://news.samsung.com/global/samsung-electronics-unveils-samsung-health-research-stack | Press release | Search summary | Open-source; SDK + backend + web portal; Alpha 2022 → 1.0 2023 → Research Stack 2024 → 2.0 Beta; available to companies and medical institutions; used in domestic and international clinical studies |
| S-SAM-04 | Research Stack overview / FAQ / release notes | Samsung | https://developer.samsung.com/health/research/overview.html | Developer docs | Search summary | Research Stack structure; Galaxy Watch5+ compatibility statement (**conflicts with S-SAM-01's Watch4+**) **Re-read Direct 2026-10-09:** "The Galaxy Watch 5 has been extensively tested"; "Other devices may work but have not been officially tested". Not a conflict with S-SAM-01: SDK minimum versus Research-Stack-tested device. |
| S-SAM-05 | Health features on the Galaxy Watch8 | Samsung | https://www.samsung.com/ie/support/mobile-devices/health-features-on-the-galaxy-watch8-and-watch8-classic/ | Support | Search summary | Watch8 sensor complement and health features |
| S-SAM-06 | Samsung's Expanded Wearables Portfolio | Samsung Newsroom | https://news.samsung.com/global/samsungs-expanded-wearables-portfolio-unlocks-intelligent-health-experiences-for-all | Press release | Search summary | Antioxidant Index; Vascular Load; Bedtime Guidance; Galaxy Ring |
| S-SAM-07 | Health Sensor Data Specifications | Samsung | https://developer.samsung.com/health/sensor/guide/data-specifications.html | Developer docs | **Direct** (2026-10-10) | ACC 25 Hz; EDA 1 Hz (Watch8+); HR+IBI 1 Hz; PPG 25 Hz continuous, 100 Hz on demand; ECG 500 Hz; MF-BIA Watch8+; on-demand about 30 s, one at a time |
| S-SAM-08 | Health Sensor SDK process and FAQ | Samsung | https://developer.samsung.com/health/sensor/process.html ; https://developer.samsung.com/health/sensor/faq.html | Developer docs | **Direct** (2026-10-10) | v1.4.1 public download; developer mode testing only; partner request with package name and SHA-256 before distribution |
| S-SAM-09 | Partner Service & SDK License Agreement | Samsung | https://developer.samsung.com/health/sensor/sdk-license-partner-service-agreement.html | Licence | **Direct** (2026-10-10) | No HIPAA, BAA or DPA language (text search) |
| S-SAM-10 | S-HealthStack repositories | GitHub API | https://api.github.com/orgs/S-HealthStack/repos | Repository metadata | **Direct** (2026-10-10) | Last pushes 2024-10-24 (starter-app 2024-08-20); none archived |
| S-SAM-11 | Alavi et al. 2026 metadata | Crossref / Europe PMC | https://api.crossref.org/works/10.1007/s44470-026-00159-8 | Bibliographic record | **Direct** (2026-10-10) | Funder Samsung (publisher-asserted); 152 enrolled, 147 both nights; AUROC 0.94 |

## Polar

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-POL-01 | polar-ble-sdk | Polar (GitHub) | https://github.com/polarofficial/polar-ble-sdk | SDK (source-available; corrected 2026-10-11 from "Open-source": the repository ships under Polar's proprietary SDK Limited License Agreement, per `../facts/polar.yaml`) | **Direct** | Device/stream support matrix; Android and iOS. **Note: this README matrix is incomplete and partly misleading: it omits H10 accelerometry and Verity Sense gyro/magnetometer, and implies ECG for Verity Sense. Superseded by the per-product docs S2-POL-01/02** Re-read 2026-10-09: the README no longer carries a device capability matrix and links per-product docs instead; `PolarH10.md` (last changed 2026-03-13) lists ACC at 25/50/100/200 Hz. |
| S-POL-02 | Research tools | Polar | https://www.polar.com/en/science/research-tools/ | Vendor research page | **Direct** | H10 raw ECG and 3D acceleration; Verity Sense PPG and acceleration; built-in memory; Open AccessLink; Team Pro API; 600+ studies (H10, 2022–23), 180 (Team Pro), 1,000+ papers/yr |
| S-POL-03 | PolarH10.md / PolarVeritySense.md | Polar (GitHub) | https://github.com/polarofficial/polar-ble-sdk/blob/master/documentation/products/PolarH10.md | SDK product docs | Not retrieved (2026-08-21 first pass) | Per-device sampling rates. **Retrieved in the second pass: see S2-POL-01 and S2-POL-02** |
| S-POL-04 | Let's Build Products Together | Polar | https://www.polar.com/us-en/developers | Developer portal | Search summary | AccessLink description |
| S-POL-05 | AccessLink API v3 | Polar | https://www.polar.com/accesslink-api/ | API docs | **Direct** (2026-10-10; changelog 13.01.2026) | Any Flow user can create client; RR ms with H6/H7/H9/H10; continuous HR 5 min; exercises last 30 days and post-registration only; activity 28-day default, 365-day max; 500+20×users/15 min, 5,000+100×users/24 h |
| S-POL-06 | Privacy notice | Polar | https://www.polar.com/en/legal/privacy-notice | Legal | **Direct** (2026-10-10) | Polar controller for Flow; not responsible after transfer out; processor for Team Pro and GoFit; no HIPAA |
| S-POL-07 | Polar360.md | Polar (GitHub) | https://github.com/polarofficial/polar-ble-sdk/blob/master/documentation/products/Polar360.md | SDK docs | **Direct** (2026-10-10) | ACC 12–400 Hz online, 1–50 Hz offline; PPG 22/50/100 Hz 24-bit; skin temp 1/2/4 Hz; 15 MB storage |
| S-POL-08 | Polar H10 US store page | Polar | https://www.polar.com/us-en/sensors/h10-heart-rate-sensor | Store | **Direct** (2026-10-10) | $104.95 |

## Withings

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-WTH-01 | **Advanced Research API** | Withings | https://developer.withings.com/developer-guide/v3/withings-solutions/research-apis/ | Developer docs | **Direct** | ScanWatch only; 3-axis accelerometer 25 Hz default **up to 100 Hz**; PPG with 3 LEDs (green/red/IR) or 1 (green); gated program Re-read 2026-10-09: wording unchanged. |
| S-WTH-02 | **Raw data** | Withings | https://developer.withings.com/developer-guide/v3/integration-guide/public-health-data-api/data-api/raw-data/ | Developer docs | **Direct** | PPG 3 wavelengths; accelerometer ±4 g; **both ≈24.824 Hz** (conflicts with S-WTH-01); contracted partners only; **activation disables all other watch features**; **battery 4–7× faster drain, 3–4 days**; ECG not listed Re-read 2026-10-09: wording unchanged; intro also says "approximately 25 Hz". Reconciled reading: 24.824 Hz is the effective raw-mode rate, "up to 100 Hz" is an undocumented hardware ceiling. |
| S-WTH-03 | Research & clinical trials | Withings Health Solutions | https://www.withings.com/us/en/health-solutions/research-clinical-trials | Vendor page | **Direct (browser)** | Medical-grade clinically validated devices; flexible retrieval via cellular, mobile app, RPM platform, or API; partnership model; study index |
| S-WTH-04 | Partner Hub | Withings | https://developer.withings.com/ | Developer portal | **Direct** | Developer portal; the API reference at https://developer.withings.com/api-reference/ is **public**, no login (checked 2026-10-10; see S-WTH-08). Recorded as behind login on 2026-08-21 |
| S-WTH-05 | Medable–Withings partnership | Business Wire | https://www.businesswire.com/news/home/20220721005032/en/ | Press release | Secondary | DCT integration precedent |
| S-WTH-06 | Withings API plans | Withings | https://developer.withings.com/developer-guide/v3/withings-solutions/withings-api-plans/ (content: https://static.withings.com/content/api/plans/plans.html) | Developer docs | **Direct** (2026-10-10) | Start for Free (10 users), Enterprise, Advanced Biomarkers; 1,500+ req/min paid; DPA and BAA on paid plans; Withings+ required from 12 Oct 2026 for new accounts on free plan, including via Apple/Google Health; exemption for Research partners |
| S-WTH-07 | Security and compliance | Withings | https://developer.withings.com/developer-guide/v3/withings-solutions/security-and-compliance/ | Developer docs | **Direct** (2026-10-10) | EU Medical Cloud: GDPR, HDS, HIPAA, ISO 27001:2017; US Medical Cloud: ISO 27001:2017, HIPAA (vendor statements). **Superseded 2026-10-11** for ISO: AFNOR certificates show ISO/IEC 27001:2022, ISO 27701 and HDS v2 (`../facts/withings.yaml` iso27001); this page is stale |
| S-WTH-08 | API reference | Withings | https://developer.withings.com/api-reference/ | API reference | **Direct** (2026-10-10, public) | Raw Data part of Advanced research API, "around 25Hz", ScanWatch only; status 601 throttling. Supersedes S-WTH-04's "behind login" |
| S-WTH-09 | openFDA 510(k), applicant Withings | FDA | https://api.fda.gov/device/510k.json?search=applicant:withings | Regulatory database | **Direct** (2026-10-10) | K110872, K133125, K160544, K201456, K230812, K231667, K240795, K252474. Applicant search only: blood pressure monitors listed under Transtek 510(k)s (K223374, K240102), the K201456 SpO2 scope, the Body Scan scope of K230812 and recall Z-1280-2023 are in `../facts/withings.yaml` (2026-10-11) |

## Empatica

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-EMP-01 | Health Monitoring Platform for Research Studies | Empatica | https://www.empatica.com/en-eu/platform/research-studies/ | Vendor page | **Direct** | Sensors (optical PPG, ventral EDA, accelerometer, digital temperature); **18 validated biomarkers named**; raw CSV via Care Portal; **no real-time streaming**; studies/sites/unlimited participant credentials; multiple sessions per device; live wear-time tracking Re-read 2026-10-09: URL now redirects to https://www.empatica.com/platform/research-studies/ ; no count stated, a 17-row biomarker table split by EmbracePlus (16) and EmbraceMini (12). Homepage and clinical-trials page now say "300+ digital measures", six FDA-cleared. |
| S-EMP-02 | Raw Data | Empatica | https://www.empatica.com/rawdata/ | Vendor page | **Direct** | Raw streams: accelerometer, temperature, EDA, steps, BVP, systolic peaks, user tags; **Avro format**; "no black box algorithms"; configurable sensor modes and sampling frequencies; FDA-cleared and CE |
| S-EMP-03 | Understanding your Empatica Health Monitoring Platform Plan | Empatica Support | https://support.empatica.com/hc/en-us/articles/17721117772317 | Support | Search summary (direct fetch 403) | Care app = Enterprise; Care Lab app = Academic & Basic Research; standard vs complete suite |
| S-EMP-04 | EmbracePlus specifications | Empatica (via Tec de Monterrey mirror) | https://ifelldh.tec.mx/sites/g/files/vgjovo1101/files/Empatica_EmbracePlus.pdf | Spec sheet | Search summary | **EDA 4 Hz, PPG 64 Hz, accelerometer 64 Hz.** Not relied on: these match the legacy E4, and `profiles/empatica.md` (re-verified 2026-10-10) says EmbracePlus per-mode PPG and EDA rates are not published |
| S-EMP-05 | Empatica Actigraphy | Empatica | https://www.empatica.com/embraceplus/actigraphy | Vendor page | Search summary | **7-day battery with raw 64 Hz accelerometry; 14-day extended mode**; actigraphy counts. Current reading (S-EMP-10, 2026-10-10): Actigraphy Pro 64 Hz, Actigraphy Optimized 32 Hz with up to 14 days battery |
| S-EMP-06 | Empatica Health Monitoring Platform receives FDA clearance | Empatica | https://www.empatica.com/blog/the-empatica-health-monitoring-platform-receives-fda-clearance | Vendor blog | Search summary | Nov 2022 clearance; EDA, SpO2, skin temperature, movement during sleep |
| S-EMP-07 | New FDA clearance for cardiac digital biomarkers | Empatica / PR Newswire | https://www.empatica.com/blog/empatica-receives-new-fda-clearance-for-cardiac-digital-biomarkers/ | Press release | Search summary | Subsequent cardiac biomarker clearance |
| S-EMP-08 | Academic & Basic Research plan store (re-read) | Empatica | https://www.empatica.com/store/platform-professional/ | Pricing page | **Direct** (accessed 2026-10-10) | EmbracePlus/EmbraceMini device, subscription and bundle prices; raw data access |
| S-EMP-09 | Apply for an Academic Discount | Empatica | https://lp.empatica.com/academic-discount-professional-plan | Vendor form page | **Direct** (accessed 2026-10-10) | Eligibility; institutional email; code by email |
| S-EMP-10 | Empatica Actigraphy blog | Empatica | https://empatica.com/blog/empatica-actigraphy-the-new-standard-to-measure-sleep-and-physical-activity | Vendor blog | **Direct** (accessed 2026-10-10) | Actigraphy Pro 64 Hz; Optimized 32 Hz, 14 days |
| S-EMP-11 | Legal and certifications | Empatica | https://www.empatica.com/legal/ | Vendor page | **Direct** (accessed 2026-10-10) | ISO/IEC 27001:2022, ISO 13485, MDSAP, CE, DPA. The ISO 27001 certificate itself (TÜV Rheinland 01 153 2117571, valid to 2028-10-30) was read on 2026-10-10 (`../facts/empatica.yaml` iso27001) |
| S-EMP-12 | Participant privacy policy | Empatica | https://www.empatica.com/privacy-participant/ | Privacy policy | **Direct** (accessed 2026-10-10) | US-Virginia HIPAA-compliant hosting; retention service plus 10 years |
| S-EMP-13 | openFDA 510(k)s and indications | FDA | https://api.fda.gov/device/510k.json?search=applicant:empatica | Regulatory database and PDFs | **Direct** (accessed 2026-10-10) | K221282, K230457, K242737, K260374, K252981, K250515 scopes |
| S-EMP-14 | llms.txt | Empatica | https://www.empatica.com/llms.txt | Vendor summary | **Direct** (accessed 2026-10-10) | 5-year subscription $1,749.60 |

## Ametris (formerly ActiGraph)

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-AMT-01 | CentrePoint | Ametris | https://ametris.com/centrepoint | Product page | **Direct** | Cloud platform for clinical investigations; LEAP and Insight Watch; **"future-proof raw sensor data reprocessed indefinitely"**; CentrePoint API; wear-compliance portal; cellular gateway or mobile app; 70+ countries; "Ametris, a Signant Health Company" |
| S-AMT-02 | Ametris home | Ametris | https://ametris.com/ | Company site | **Direct** | Device and platform inventory (LEAP, Insight Watch, wGT3X-BT, Connect, CentrePoint, ActiLife, Algorithm Marketplace); measurement domains; FDA-cleared medical-grade framing; services |
| S-AMT-03 | ActiGraph Rebrands as Ametris | Ametris | https://blog.ametris.com/news/actigraph-rebrands-as-ametris | Press release | Search summary | **Rebrand 25 June 2025**; Biofourmis Connect acquisition Jan 2025; Biovitals and RhythmAnalytics SaMD |
| S-AMT-04 | Signant Health Acquires Ametris | Signant Health / PR Newswire | https://signanthealth.com/company/news/signant-health-acquires-ametris | Press release | Search summary | **Acquisition announced May 2026.** Dates confirmed 2026-10-10: agreement 16 April (S-AMT-06), acquisition announced 14 May 2026 (S-AMT-07) |
| S-AMT-05 | ActiGraph pricing guides | Fibion (competitor) | https://web.fibion.com/articles/actigraph-pricing-information-guide/ | Third-party marketing | Search summary | Indicative and dated figures: GT3X+/wGT3X-BT $325–1,016; GT9X ~$500 and EOL; CentrePoint Hub ~$600 or ~$300/yr; ActiLife ~$1,695; CentrePoint software ~$3,500/yr. **Competitor source — treat with caution** |
| S-AMT-06 | Definitive agreement to acquire Ametris | Signant Health | https://signanthealth.com/company/news/signant-health-enters-definitive-agreement-to-acquire-ametris | Press release | **Direct** (accessed 2026-10-10) | Agreement 16 April 2026 |
| S-AMT-07 | Signant Health Acquires Ametris | PR Newswire | https://tools.prnewswire.com/en-us/live/20813/release/20260514EN58707 | Press release | **Direct** (accessed 2026-10-10) | Acquisition announced 14 May 2026 |
| S-AMT-08 | Device pages (CPIW, LEAP, wGT3X-BT, ActiLife) | Ametris | https://ametris.com/cpiw · https://ametris.com/actigraph-leap · https://ametris.com/actigraph-wgt3x-bt · https://ametris.com/actilife | Vendor pages | **Direct** (accessed 2026-10-10) | 32 to 256 Hz / 30 to 100 Hz; ±8 g; storage and battery; LEAP spec conflict (resolved 2026-10-11 in `../facts/ametris-actigraph.yaml`: 79 days / 1 GB at the 32 Hz default per the LEAP IFU Rev 3, Corroborated; the 30-day block is outdated); per-order pricing |
| S-AMT-09 | CentrePoint V3 API documentation | ActiGraph | https://github.com/actigraph/CentrePoint3APIDocumentation | API docs | **Direct** (accessed 2026-10-10) | OAuth client credentials; raw Data Access Files (accel, PPG, temperature, barometer, IMU); 500 req/min/IP; 10 concurrent raw requests; possible historical-file fees |
| S-AMT-10 | Compliance Center | Ametris | https://ametris.com/compliance | Vendor page | **Direct** (accessed 2026-10-10) | ISO 13485/MDSAP; DPA with SCCs; DPF; ISO 27001:2022 listed; Azure and AWS. Superseded 2026-10-11 for ISO 27001: the certificate itself (IA391-260410-001, Ignyte Assurance, to 2029-04-15) was read, per `../facts/ametris-actigraph.yaml` |
| S-AMT-11 | Academic research site and store | Ametris | https://academic.ametris.com/ · https://store.ametris.com/ | Vendor pages | **Direct** (accessed 2026-10-10) | Academic channel; pricing-list form; accessory store for existing academic accounts |

## Axivity / GENEActiv

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-AXV-01 | AX3 | Open Movement / Newcastle University | https://github.com/digitalinteraction/openmovement/wiki/AX3 | Open-source project | Search summary | AX3 accelerometer, AX6 accel+gyro; **firmware/software BSD 2-clause; hardware and enclosure CC BY 3.0** |
| S-AXV-02 | UK Biobank Physical Activity Monitor | UK Biobank | https://biobank.ndph.ox.ac.uk/ukb/ukb/docs/PhysicalActivityMonitor.pdf | Cohort documentation | Search summary | AX3 chosen 2012; **100 Hz, ±8 g, 7 days**; timed postal start at 10am two working days after dispatch |
| S-AXV-03 | Large Scale Population Assessment of Physical Activity Using Wrist Worn Accelerometers | Doherty et al., *PLOS ONE* 2017 | https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0169649 | Peer-reviewed | Search summary | 100,000+ participants; **equivalence with GENEActiv on multi-axis shaking tests**; Whitehall II, Fenland, Pelotas comparison |
| S-AXV-04 | actipy | Oxford Wearables Group | https://github.com/OxWearables/actipy | Open-source SDK | Search summary | Python processing SDK |
| S-AXV-05 | Methods — accelerometer documentation | Oxford | https://biobankaccanalysis.readthedocs.io/en/latest/methods.html | Documentation | Search summary | Open ML activity classification pipeline used on UK Biobank |
| S-AXV-06 | Axivity | Axivity Ltd | https://axivity.com/ · https://axivity.com/case-studies/biobank | Vendor site | Search summary | Commercial supplier; UK Biobank case study |
| S-AXV-07 | openmovementproject/openmovement repository | Open Movement | https://github.com/openmovementproject/openmovement | Open-source repository (GitHub API) | **Direct** (accessed 2026-10-09) | Moved from `digitalinteraction`; not archived; last push 2026-08-18; `libomapi` updated 2026-07-21; AX Config web tool (`openmovement-axconfig`, config.openmovement.dev) last pushed 2025-09-09 |
| S-AXV-08 | AX3 GUI revision history and AX3/AX6 firmware notes | Open Movement | https://github.com/openmovementproject/openmovement/blob/master/Downloads/AX3/AX3-GUI-revisions.md · https://github.com/openmovementproject/openmovement/blob/master/Downloads/AX3/AX3-Firmware.md | Release notes | **Direct** (accessed 2026-10-09) | Latest OmGui v45 (2022-10-31); latest AX3 firmware V50 (2020-05-19, WinUSB/generic); latest AX6 firmware V56 (2019-12-09) |
| S-AXV-09 | GENEActiv product page | Activinsights Ltd | https://activinsights.com/digital-health-technologies/professional-wearables/geneactiv/ | Vendor product page | **Direct** (accessed 2026-10-09) | Page dated 2026-01-29; sold via "Request a Quote"; USB cradle holds up to 4 devices; up to 2 months battery (superseded 2026-10-11: the IFU's own table gives 44 days at 20 Hz for v1.2/1.3, a conflict recorded in `../facts/activinsights-geneactiv.yaml`); MDD Class I transitioning to EU MDR; no discontinuation notice. GENEAcore R package 1.2.0 (CRAN, 2026-04-02), with Activinsights Ltd as the only copyright holder listed (corrected 2026-10-10 from "co-owned"; see S-AXV-13): https://cran.r-project.org/package=GENEAcore |
| S-AXV-10 | AX3 product page | Axivity | https://axivity.com/product/ax3 | Vendor shop | **Direct** (accessed 2026-10-10) | £139/£149 ex VAT; 12.5 to 3,200 Hz; ±2 to 16 g |
| S-AXV-11 | AX6 product page | Axivity | https://axivity.com/product/ax6 | Vendor shop | **Direct** (accessed 2026-10-10) | £199/£209 ex VAT; 12.5 to 1,600 Hz; gyroscope ±125 to 2000 dps |
| S-AXV-12 | AX3 FAQ (duration table) | Open Movement | https://github.com/openmovementproject/openmovement/blob/master/Docs/ax3/ax3-faq.md | Device docs | **Direct** (accessed 2026-10-10) | Maximum recording durations by rate and mode |
| S-AXV-13 | GENEAcore on CRAN | CRAN | https://cran.r-project.org/package=GENEAcore | Package page | **Direct** (accessed 2026-10-10) | v1.2.0, 2026-04-02, Activinsights Ltd [cph] |

## Data intermediaries

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-INT-01 | Fitabase | Fitabase | https://www.fitabase.com/ | Vendor site | **Direct** | Fitbit and Garmin; study-controlled or participant-owned; daily/hourly/**minute-level** CSV; monitoring dashboards; battery and sync status; tagging; de-identified profiles; **Engage suite Summer 2026**; 1,100+ studies |
| S-INT-02 | Fitabase Pricing | Fitabase | https://www.fitabase.com/how-it-works/pricing/ | Vendor page | **Direct** | **Custom pricing, not public**; Core vs add-ons (SMS, Aggregate Data API, custom); hello@fitabase.com |
| S-INT-03 | What is the Fitabase API? | Fitabase | https://www.fitabase.com/resources/knowledge-base/fitabase-api/what-is-the-fitabase-api/ | Knowledge base | Search summary | Programmatic export in JSON or CSV |
| S-INT-04 | Terra — Garmin integration | Terra | https://tryterra.co/integrations/garmin | Vendor site | Secondary | Unified API positioning |
| S-INT-05 | Rook — Garmin data source | Rook | https://docs.tryrook.io/data-sources/garmin/ | Integrator docs | Secondary | Unified API; Garmin data mapping |
| S-INT-06 | Open Wearables | Open Wearables | https://openwearables.io/ | Open-source project | Secondary | Open-source unified wearable API; Oura and WHOOP integrations as of 2026; MCP server |
| S-INT-07 | Apple HealthKitV2 Electrocardiogram Export Format | CareEvolution / MyDataHelps | https://support.mydatahelps.org/apple-healthkitv2-electrocardiogram-export-format | Platform docs | Search summary | Third-party research platform handling HealthKit ECG export |
| S-INT-08 | Data Types and Organization | All of Us | https://support.researchallofus.org/hc/en-us/articles/4619151535508-Data-Types-and-Organization | User support | Search summary | Researcher Workbench data organization |
| S-INT-09 | Fitabase research library | Fitabase | https://www.fitabase.com/research-library/ | Vendor page | **Direct** (2026-10-10) | 1,650 publications, updated 5 Oct 2026 |
| S-INT-10 | Fitabase Engage, FAQ, privacy, terms | Fitabase | https://www.fitabase.com/engage/ ; https://www.fitabase.com/resources/faq/ | Vendor pages | **Direct** (2026-10-10) | Engage apps "Preview · Summer 2026"; no HIPAA/BAA wording |
| S-INT-11 | Fitrockr research pricing and devices | Fitrockr | https://www.fitrockr.com/research/pricing ; https://www.fitrockr.com/compatible-devices/ | Vendor pages | **Direct** (2026-10-10) | Basic €50/$55, Pro €150/$165 per month; 5 licences; 3-month minimum; ACC 25 Hz/gyro 32 Hz +25% add-on; surveys +20%; vendor-claimed HIPAA/CASA/ISO |
| S-INT-12 | Terra pricing | Terra | https://tryterra.co/pricing | Vendor page | **Direct** (2026-10-10) | $499/mo or $399/mo annual; 100k credits; BAA on Enterprise |
| S-INT-13 | Thryve pricing | Thryve | https://www.thryve.health/pricing | Vendor page | **Direct** (2026-10-10) | €499/mo (500 users), €1,000/mo (5,000 users); storage 1 day / 2 weeks / 1 month; claims GDPR and HIPAA compliance |

## Validation and evidence (cross-platform)

| ID | Title | Authors / Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-VAL-01 | Accuracy of Three Commercial Wearable Devices for Sleep Tracking in Healthy Adults | Robbins et al., *Sensors* 2024;24(20):6532 | https://www.mdpi.com/1424-8220/24/20/6532 · open mirror: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11511193/ | Peer-reviewed | Search summary | N=35, single night, PSG. **4-stage kappa: Oura 0.65, Apple Watch 0.60, Fitbit Sense 0.55**; Oura deep-sleep sensitivity 79.5% |
| S-VAL-02 | A performance validation of six commercial wrist-worn wearable sleep-tracking devices for sleep stage scoring compared to polysomnography | Schyvens et al., *SLEEP Advances* 2025;6(2):zpaf021 | https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472 · open mirror: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12038347/ | Peer-reviewed | Search summary | N=62. Devices: Fitbit Charge 5, Fitbit Sense, **Withings ScanWatch**, Garmin Vivosmart 4, Whoop 4.0, Apple Watch Series 8. Most differed significantly from PSG on TST, SE, WASO, light sleep. **Deep-sleep sensitivity: Whoop 69.6%, Apple 50.7%, Fitbit Sense 48.3%, Charge 5 43.3%, Garmin 32.1%**. Not relied on: the full-text extraction (S2-VAL-01, `validation-evidence.md` §1) gives deep-sleep accuracy Whoop 69.63%, Charge 5 51.50%, Sense 50.86%, Apple 50.66%, Garmin 47.46%, and overall κ 0.37 to 0.53 |
| S-VAL-03 | Reliability and Validity of Commercially Available Wearable Devices for Measuring Steps, Energy Expenditure, and Heart Rate: Systematic Review | Fuller et al., *JMIR mHealth uHealth* 2020;8(9):e18694 | https://mhealth.jmir.org/2020/9/e18694/ | Peer-reviewed | Search summary | **Apple and Samsung highest step validity; Apple, Fitbit, Garmin accurate ~50% of the time; no brand within acceptable limits for energy expenditure** |
| S-VAL-04 | Accuracy and Precision of Energy Expenditure, Heart Rate, and Steps Measured by Combined-Sensing Fitbits Against Reference Measures | Chevance et al., *JMIR mHealth uHealth* 2022;10(4):e35626 | https://mhealth.jmir.org/2022/4/e35626 | Peer-reviewed | Search summary | Fitbit **underestimates** HR, EE, and steps; acceptable on average for steps and HR; EE may be inaccurate for research |
| S-VAL-05 | Keeping Pace with Wearables: A Living Umbrella Review of Systematic Reviews | (umbrella review) | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11560992/ | Peer-reviewed | Search summary | HR mean bias ±3%; steps MAPE −9 to 12%; EE mean bias −3 kcal/min, range −21.3% to +14.8%; pervasive methodological heterogeneity |
| S-VAL-06 | Feasibility and acceptability of collecting passive phone usage and sensor data via Apple SensorKit | (medRxiv / PMC) | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12349082/ | Peer-reviewed / preprint | Search summary | Empirical SensorKit deployment experience |
| S-VAL-07 | Analysis and postprocessing of ECG or heart rate data from wearable devices beyond the proprietary cloud and app infrastructure of the vendors | (ScienceDirect) | https://www.sciencedirect.com/science/article/pii/S2666693621001158 | Peer-reviewed | Search summary | Apple Watch 1-lead ECG voltage measurements and classification retrievable via HealthKit libraries |

---

## Sources sought but not obtained

| Target | URL | Outcome |
|---|---|---|
| Garmin Health API summaries reference | https://developer.garmin.com/gc-developer-program/health-api/ | The old `/health-api/summaries/` URL returns 404 (2026-08-21, again 2026-10-10); replaced by the Health API page, which lists the metric families (S-GRM-01, S2-GRM-02) |
| Oura developer docs (alt host) | https://developer.ouraring.com/docs | **404** (again 2026-10-10). The API docs live at https://cloud.ouraring.com/v2/docs (S-OUR-01, S-OUR-07) |
| Withings research page (direct fetch) | https://www.withings.com/us/en/health-solutions/research-clinical-trials | **403** — retrieved via browser instead |
| Empatica plan support article (direct fetch) | https://support.empatica.com/hc/en-us/articles/17721117772317 | **403** — retrieved via search summary |
| Apple HealthKit documentation body | https://developer.apple.com/documentation/healthkit | JS-rendered; only title returned |
| Polar per-product SDK sampling rates | https://github.com/polarofficial/polar-ble-sdk/blob/master/documentation/products/ | Not retrieved in the first pass; retrieved in the second (S2-POL-01, S2-POL-02) |
| Verily Study Watch product pages | https://verily.com/solutions/study-watch · https://verily.com/perspectives/verily-study-watch | **404** (2026-10-10); no current Study Watch page found (`profiles/emerging-platforms.md`) |

---

## Second-pass sources — added 2026-08-21

### Validation literature read in full

| ID | Title | URL | Retrieval | Establishes |
|---|---|---|---|---|
| S2-VAL-01 | Schyvens et al. 2025, *SLEEP Advances* 6(2):zpaf021 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12038347/ | **Direct, full text** | Complete per-device kappa, sensitivity/specificity, per-stage accuracy, TST/SE/WASO/SOL bias tables; **ScanWatch results**; device-failure counts (Garmin 18/43, Apple 15/35); VLAIO funding, no conflicts; limitations incl. skin tone not recorded |
| S2-VAL-02 | Robbins et al. 2024, *Sensors* 24(20):6532 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11511193/ | **Direct, full text** | Per-stage sensitivity/precision; four-stage and sleep–wake kappa; **ICCs showing poor deep/REM reliability**; **funding by Oura Ring Inc. and lead-author advisory-board conflict**; device failures |
| S2-VAL-03 | Garmin Enhanced BBI — An Example Night, Nov 2023 | https://www8.garmin.com/garminhealth/news/Garmin-Enhanced-BBI_Final.pdf | **Direct, PDF read** | BBI vs RRI definitions; per-beat confidence metric and its three failure causes; **"measured during the user's sleep interval"**; availability via Standard SDK **and Health API**; N=1 accuracy demo (0.506 ms mean error, 8.55 ms SD, r=0.975, 93.13% high-confidence) |

### Google Health API — access, limits, scopes, data types

| ID | Title | URL | Retrieval | Establishes |
|---|---|---|---|---|
| S2-GHA-01 | App verification | https://developers.google.com/health/app-verification | **Direct** | **100-user cap for unverified apps**; two-part verification; **CASA security assessment, Tier 2 2–3 wks, Tier 3 4–6 wks, $500–$4,500**; in-app disclosure requirements |
| S2-GHA-02 | Quotas and rate limits | https://developers.google.com/health/rate-limits | **Direct** | 86.4M req/day/project; 120,000 req/min/project; 300 req/min/user; unverified capped at 250 QPS |
| S2-GHA-03 | Data types | https://developers.google.com/health/data-types | **Direct** | Interval / Sample / Session / Daily Aggregate record types; **Heart Rate is a Sample type with no documented interval**; HRV, SpO2, respiratory rate, RHR as Daily Aggregates; ECG and Irregular Rhythm as Sessions. **Superseded by S-FIT-17** (catalogue updated 2026-10-06): Heart Rate 1-second storage resolution, HRV and SpO2 Sample types |
| S2-GHA-04 | Scopes | https://developers.google.com/health/scopes | **Direct** | 17 scopes under `googleapis.com/auth/googlehealth`, `.readonly`/`.writeonly` variants |
| S2-GHA-05 | Migration guide | https://developers.google.com/health/migration | **Direct** | Tokens cannot be transferred; re-consent UX guidance; backfill after re-auth; data gaps for non-re-authenticating users; **no turndown date stated** on 2026-08-21. Google now states both dates (S-FIT-14) |
| S2-GHA-06 | Restricted scope verification | https://developers.google.com/identity/protocols/oauth2/production-readiness/restricted-scope-verification | Search summary | Exception categories: personal use, dev/test/staging, service-owned data, **internal use within an organization**, domain-wide installation; annual assessment for third-party-server access |

### Polar — per-product SDK documentation

| ID | Title | URL | Retrieval | Establishes |
|---|---|---|---|---|
| S2-POL-01 | PolarH10.md | https://github.com/polarofficial/polar-ble-sdk/blob/master/documentation/products/PolarH10.md | **Direct** | HR+RR at 1 Hz; **ECG 130 Hz in µV**; **ACC 25/50/100/200 Hz at ±2/4/8 g**; internal recording HR-only at 1 s. **Resolves the H10 accelerometer contradiction** |
| S2-POL-02 | PolarVeritySense.md | https://github.com/polarofficial/polar-ble-sdk/blob/master/documentation/products/PolarVeritySense.md | **Direct** | PPG, PPI, ACC 52 Hz, **gyroscope 52 Hz**, **magnetometer 10–100 Hz**; offline recording; **SDK mode: ACC/gyro 26–416 Hz, PPG 28–176 Hz at 22-bit**; HR and PPI unavailable in SDK mode. **No ECG listed for this device** |

### Garmin / research platforms

| ID | Title | URL | Retrieval | Establishes |
|---|---|---|---|---|
| S2-GRM-01 | Collecting Enhanced BBI Using Garmin Devices | https://fitabase.com/resources/knowledge-base/learn-about-garmin-data/collecting-enhanced-beat-to-beat-interval-data-using-garmin-devices/ | **Direct** | Gen-4 sensor or higher; Vivosmart 5 / Venu 3 common; **since early 2025 collected via standard Garmin Connect app + OAuth, no chest strap, no custom app**; LOW/HIGH confidence; captured during sleep from the wrist |
| S2-GRM-02 | Health API page (metric list) | https://developer.garmin.com/gc-developer-program/health-api/ | **Direct, re-read** | Verbatim metrics: steps, heart rate, sleep, stress, intensity minutes, calories, pulse ox, Body Battery, body composition, respiration, blood pressure, **Enhanced Beat-To-Beat Interval** |
| S2-LAB-01 | Labfront pricing | https://www.labfront.com/pricing | **Direct** | **Tester free (5 participants, 30-day window); Basic $500/yr (20, +$10 each); Advanced $1,250/yr (20, +$25 each, all integrations, customisable high-resolution sampling)**; analytics add-ons from $2,000; EMA in all tiers; grants programme. Re-read 2026-10-10 (`profiles/data-intermediaries.md`): analytics from $3,000 plus $50 per participant; Developer Access from $4,000; Data Audit from $500 |
| S2-LAB-02 | Labfront compatible devices | https://www.labfront.com/compatible-devices | **Direct** | Garmin vívosmart 5 / vívoactive 5 (BBI, steps, HR, SpO2, respiration, accelerometer), **Movesense HR2 (RR, ECG, IMU, accel, gyro, magnetometer)**, Garmin Index BPM and S2 scale, Dexcom G7. Updated 2026-10-11 by `../facts/movesense.yaml`: Labfront supports Movesense Medical, HR2 and Flash, and participants start each recording manually |
| S2-LAB-03 | Labfront–Garmin collaboration | https://www.labfront.com/blog/labfront-and-garmin-collaboration | Search summary | Labfront configures Garmin devices via the Health SDKs to **increase sensor resolution beyond stock** |

### Movesense

| ID | Title | URL | Retrieval | Establishes |
|---|---|---|---|---|
| S-MVS-01 | Specifications | https://www.movesense.com/specifications/ | **Direct** | MD is **Class IIa Medical Device MDR 2017/745**; Flash has **128 MB internal memory**; RR intervals at **1 ms** accuracy and resolution; 9-axis IMU across the range; HR2 9.4 g |
| S-MVS-02 | Get started | https://www.movesense.com/get-started/ | **Direct** | Open APIs; **custom sensor firmware supported**; desktop simulator; Bitbucket repositories; firmware upload via Showcase app |
| S-MVS-03 | Movesense home | https://www.movesense.com/ | **Direct** | Product families: CardioRTHM, Movesense Medical, Movesense Sport |
| S-MVS-04 | HR2 / MD product pages and search summary | https://www.movesense.com/product/movesense-sensor-hr2/ | Search summary | **ECG 125 to 512 Hz**; **IMU 13 Hz to 1.6 kHz**; **no licence cost**; business-customer sales, sales@movesense.com; Kubios integration. Superseded 2026-10-11 by `../facts/movesense.yaml`: the maximum IMU rate is a vendor conflict (416, 833 or 1666 Hz by source), and Kubios use is a CSV file workflow, not an integration |
| S-MVS-05 | Movesense Academic Program (Movesense) | https://www.movesense.com/movesense-academic-program/ | **Direct** (accessed 2026-10-10) | Sensors for selected projects; monthly review; up to 3 per quarter; last cohort Q1 2023. Updated 2026-10-11 by `../facts/movesense.yaml`: the application form says weekly review (conflict), and a December 2025 news post shows the program still admitting projects |
| S-MVS-06 | Movesense MD Sensor (Movesense) | https://www.movesense.com/product/movesense-medical-mdr/ | **Direct** (accessed 2026-10-10) | €349 VAT 0% (1 to 49), €344 (50 to 99) |
| S-MVS-07 | SDK License and Evaluation Agreement (Movesense Ltd) | https://bitbucket.org/movesense/movesense-device-lib/raw/master/LICENSE.pdf | **Direct** (accessed 2026-10-10) | Proprietary; evaluation purpose; no incorporation in products; 12-month term |

### Emerging platforms

| ID | Title | URL | Retrieval | Establishes |
|---|---|---|---|---|
| S-EMG-01 | UltraSignal | https://www.ultrahuman.com/ultrasignal/ | **Direct** | **Raw PPG, temperature and accelerometer** exposed; loaner developer kit; application reviewed. Re-read 2026-10-10 (S-EMG-14): the page says "data stream", not "raw"; format and rates undocumented |
| S-EMG-02 | Accessing the Ultrahuman Partnership API | https://www.ultrahuman.com/blog/accessing-the-ultrahuman-partnership-api/ | **Direct** (accessed 2026-10-10) | OAuth 2.0 for approved apps; client ID and secret at partner onboarding; scopes `ring_data`, `cgm_data`, `profile`; no whitelist wording. (The 2026-08-21 search summary said whitelist-only with a token from partner.ultrahuman.com; not supported by the current post) |
| S-EMG-03 | Biostrap research | https://biostrap.com/research/ | **Direct** | Multi-device framework; **raw and/or processed PPG, gyroscope, accelerometer**; **customisable sampling rates**; integrated surveys; FDA-cleared Thermo Patch ±0.1 °C |
| S-EMG-04 | Biostrap science / validation | https://biostrap.com/science/ · https://biostrap.com/validation/ | Search summary | Vendor-compiled "14 publications and 22 clinical studies"; NCT05279066 |
| S-EMG-05 | Verily and Samsung collaboration | https://verily.com/perspectives/verily-and-samsung-collaborate-to-accelerate-clinical-research-with-the-galaxy-watch-and-pre-platform | Search summary | **March 2026**; Galaxy Watch 8 into Verily **Pre** / **Viewpoint Evidence**; **raw PPG and accelerometer/gyroscope motion signals** to researchers |
| S-EMG-06 | Verily Study Watch coverage | https://www.mobihealthnews.com/news/verilys-research-wearable-lands-fda-clearance-demand-ecg | Search summary | On-demand ECG 510(k); irregular pulse 510(k); Parkinson's motor exam rejected; records ECG, HR, **EDA**, inertial; weeks of onboard raw storage; never sold to consumers |
| S-EMG-07 | Samsung Health Research Stack GitHub | https://github.com/S-HealthStack | Search summary | **Apache 2.0**; `backend-system`, `app-sdk`, `web-portal` repositories |
| S-EMG-08 | Ultrahuman privacy review | https://www.mozillafoundation.org/en/nothing-personal/ultrahuman-ring-privacy-review/ | Search summary | Independent privacy assessment of Ring AIR |
| S-EMG-09 | RingConn will migrate from Google Fit to Health Connect | https://ringconn.com/blogs/news/ringconn-will-migrate-from-google-fit-to-health-connect | **Direct** (accessed 2026-10-09) | Published 2025-08-07; Google Fit sync ends 2025-10-01; Health Connect on Android 9+. No developer API or research programme found anywhere on ringconn.com |
| S-EMG-10 | RingConn and Shanghai Jiao Tong University npj Digital Medicine study (press release) | https://www.prnewswire.com/de/pressemitteilungen/ringconn-advances-wearable-health-research-with-new-study-in-nature-portfolio-journal-npj-digital-medicine-302849687.html | Search summary (accessed 2026-10-09) | Company-run academic collaboration; 1,810 participants, bilateral ring PPG; no data-access terms described |
| S-EMG-11 | Circular Ring app listing and circular.xyz | https://apps.apple.com/us/app/-/id1583942047 · https://www.circular.xyz/ | Search summary; circular.xyz/help returned 403 (accessed 2026-10-09) | Consumer ring app; no developer API, export or research programme found |
| S-EMG-12 | Zepp OS device-app sensor API (Accelerometer, HeartRate, BloodOxygen) | https://docs.zepp.com/docs/reference/device-app-api/newAPI/sensor/Accelerometer/ · .../HeartRate/ · .../BloodOxygen/ | **Direct** (accessed 2026-10-09) | Accelerometer x/y/z in cm/s² from API level 3.0 with low/normal/high frequency modes, no Hz published; heart rate as bpm and per-minute day array; SpO2 results; no raw PPG |
| S-EMG-13 | Zepp and Amazfit aggregator integrations | https://tryterra.co/integrations/zepp · https://www.thryve.health/features/connections/zepp-amazfit-integration | Search summary (accessed 2026-10-09) | Third-party normalised summaries; Terra lists "Activity, Daily and Sleep" data types (re-read 2026-10-10). **Thryve URL dead (404, 2026-10-10).** No Zepp-run research API found |
| S-EMG-14 | UltraSignal | https://www.ultrahuman.com/ultrasignal/ | **Direct** (accessed 2026-10-10) | PPG, temperature, accelerometer "data stream"; application and loaned kit |
| S-EMG-15 | Sensor Bio home page | https://sensorbio.com/ | **Direct** (accessed 2026-10-10) | Biostrap rebrand; "Full access to raw PPG and derived physiological signals" |
| S-EMG-16 | Biostrap home page | https://biostrap.com/ | **Direct** (accessed 2026-10-10) | "Biostrap is now Sensor Bio"; raw PPG and IBI |
| S-EMG-17 | Zepp Health data analytics | https://www.zepp.com/data-analytics | **Direct** (accessed 2026-10-10) | Research partnerships (end-2020 figure), no access terms |

### Device generations and pricing

| ID | Title | URL | Retrieval | Establishes |
|---|---|---|---|---|
| S2-DEV-01 | Apple Watch Series 11 tech specs | https://www.apple.com/apple-watch-series-11/specs/ | **Direct** | Full sensor list **including depth gauge to 6 m and water temperature sensor on Series 11**; battery 24 h / 38 h Low Power; 0–80% in ~30 min; Blood Oxygen wellness-only wording, no stated geographic restriction |
| S2-DEV-02 | Oura Ring product page | https://ouraring.com/product/rings | **Direct** | **Oura Ring 5 exists**; membership **$5.99/mo or $69.99/yr**, first month free; feature inventory |
| S2-DEV-03 | Oura Ring 5 launch | https://www.businesswire.com/news/home/20260528686853/en/ · https://techcrunch.com/2026/05/28/oura-unveils-its-ring-5-with-a-thinner-lighter-design-starting-at-399/ | Search summary | Announced 28 May 2026, shipping 4 June 2026; **$399 / $499**; 40% smaller, 2.28 mm thick, from 2 g; 12 signal pathways; **Health Radar (Blood Pressure Signals, Nighttime Breathing)**, GLP-1 insights; Blood Pressure Signals gives **no systolic/diastolic values** |
| S2-DEV-04 | Fitbit Air launch coverage | https://www.androidcentral.com/wearables/fitbit/fitbit-air-launch-specs-price (dead link, 404, checked 2026-10-10) · https://www.forbes.com/sites/forbes-personal-shopper/2026/05/07/google-fitbit-air-launch-2026/ | Search summary | **Launched 7 May 2026, $99.99**, shipping 26 May; screenless, 12 g; PPG + red/IR SpO2 + skin temp + 3-axis accel + gyroscope; **HR saved at 2-second intervals**; 7-day battery; Google Health app |
| S2-DEV-05 | Fitbit app → Google Health rebrand | https://www.androidcentral.com/wearables/fitbit/the-old-fitbit-app-is-becoming-google-health · https://www.thurrott.com/google/336407/ | Search summary | **Rebranded 19 May 2026**, rollout complete 26 May; Fitbit Premium → Google Health Premium with Gemini Health Coach; badges, DMs and Sleep Profile removed; Google Fit sunsets end of 2026 |
| S2-DEV-06 | WHOOP membership tiers | https://www.whoop.com/us/en/membership/ (403 to fetch; via trade coverage) | Search summary | **One $199/yr, Peak $239/yr, Life $359/yr**; Life includes **WHOOP MG**; hardware included in all tiers. US prices confirmed on the live vendor page in a browser, 2026-10-10 (`../facts/whoop.yaml` subscription_price) |
| S2-DEV-07 | Empatica Academic & Basic Research plan store page | https://www.empatica.com/store/platform-professional/ | **Direct** | **Device from $1,166.40; 3-yr bundle $2,332.80 list / $1,749.60 academic; 5-yr $2,916 / $2,187 academic**; "11+ digital biomarkers"; volume discounts at 5+ |
| S2-DEV-08 | Withings watch lineup | https://www.withings.com/us/en/watches · https://www.withings.com/us/en/scanwatch-nova | Search summary | ScanWatch Light (no ECG), ScanWatch 2, ScanWatch Nova (~$599), Nova Brilliant; Nova multi-wavelength PPG with 16 optical channels; ~30-day battery |

### Fitbit-to-Google migration timeline (third-party corroboration)

| ID | Title | URL | Retrieval | Establishes |
|---|---|---|---|---|
| S2-MIG-01 | General FAQs for the Fitbit to Google Health Migration | https://help.validic.com/space/VCS/5436309513/ | Search summary | New `google_health` integration available from May 2026; recommendation not to launch before late May |
| S2-MIG-02 | Google Health Community thread on API availability | https://support.google.com/googlehealth/thread/439040688/ | Search summary | Side-by-side operation to **30 September 2026**. Superseded: support ended 30 Sep, API turned off 30 Oct 2026 (S-FIT-14) |


---

## Link check — 2026-08-21

All URLs above were checked with an HTTP request on 2026-08-21.

- **200 OK:** all primary vendor documentation links cited as Verified.
- **403 (bot-blocked, not dead):** `withings.com` research pages, `academic.oup.com`, `mdpi.com`.
  These load normally in a browser; open PMC mirrors are given for the two papers.
- **404 (genuinely unavailable):** `developer.garmin.com/gc-developer-program/health-api/summaries/`
  and `developer.ouraring.com/docs`. Both are recorded in "Sources sought but not obtained" above,
  with their working replacements (2026-10-10).

### Second-pass retrieval notes (2026-08-21)

- PMC mirrors of both PSG papers were read **in full**; this corrected several first-pass claims.
- The Garmin Enhanced BBI PDF was downloaded and read page by page.
- `withings.com` and `whoop.com/membership` return **403** to automated fetch but load in a browser;
  their content here comes from browser rendering or trade coverage and is labelled accordingly.
- `developers.google.com/health/*` pages were all retrievable directly and are the strongest sources
  added in this pass.
- Movesense's detailed datasheets sit behind a survey-gated PDF download; the specification page and
  product pages were used instead, so exact battery and IMU range figures remain **Unclear**.
  Updated 2026-10-11: the MD's IP68 rating and CR2025 coin cell come from Movesense's 2024 MD FAQ
  news post (cited in `profiles/movesense.md`), and the maximum IMU rate is recorded as a vendor
  conflict in `../facts/movesense.yaml`. Battery life is still not published.


---

## Onnela Lab publications page (added 2026-08-31)

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-W-ONN-01 | Papers — Onnela Lab | Onnela Lab, Harvard T.H. Chan SPH | https://hsph.harvard.edu/research/onnela-lab/papers/ | Lab publication listing | **Direct** | **Primary/Verified.** Source of the 22 wearable-primary and Apple-ecosystem papers newly catalogued in `literature-library.md` — the Apple Women's Health Study family, the ActiGraph/GENEActiv ALS accelerometry series, a Fitbit-vs-actigraphy sleep validation, and an Oura Ring 3 longitudinal sleep cohort |
| S-W-ONN-02 | Europe PMC REST API (search / `resultType=core`) | EMBL-EBI | https://www.ebi.ac.uk/europepmc/webservices/rest/search | Bibliographic API | **Direct** | DOI, PMID, PMCID, journal, year, `isOpenAccess` flag and abstract for all 22 |

**Scope note.** This pass catalogued papers and stored PDFs. It did **not** extend
`research-library-wearables.md`'s Tier A/B/C sponsorship classification to any of them — no funding or
COI statement was read. The Oura Ring 3 freshmen sleep study (Soon et al., *Sleep* 2025) is the row
most likely to belong in that file's Oura section; it was deliberately left unadded rather than tiered
without evidence. Nothing in `comparison-matrix.md` or `validation-evidence.md` was re-labelled.

**Access barriers (2026-08-31):** four Apple-ecosystem papers marked open access by Europe PMC could
not be downloaded — the Europe PMC render service returned HTTP 500 and `pmc.ncbi.nlm.nih.gov` served
HTML rather than a PDF for the JAMA-family and two *AJOG*/*JCEM* titles. Recorded as an infrastructure
barrier, not a licensing one. The 2025 circadian rest-activity preprint returned HTTP 403 from
medRxiv.

---

## Additions and corrections, 2026-10-10

Rows S-APL-09 to S-APL-10, S-FIT-14 to S-FIT-19, S-GRM-07 to S-GRM-12, S-OUR-07 to S-OUR-13,
S-WHP-07 to S-WHP-11, S-SAM-07 to S-SAM-11, S-POL-05 to S-POL-08, S-WTH-06 to S-WTH-09,
S-EMP-08 to S-EMP-14, S-AMT-06 to S-AMT-11, S-AXV-10 to S-AXV-13, S-INT-09 to S-INT-13,
S-MVS-05 to S-MVS-07 and S-EMG-14 to S-EMG-17 were added to their device sections after the
profiles were re-verified against primary sources (commit c774edb). Several are re-reads of a URL
already registered under an older ID (for example S-FIT-14 and S-FIT-04, S-WHP-07 and S-WHP-01,
S-WHP-11 and S-WHP-06, S-EMP-08 and S2-DEV-07); the older row records what the page said on
2026-08-21 and the newer row what it says now. Older rows whose content is now superseded say so in
their "Establishes" cell. Dead links found by the independent review (R-252, R-253, R-258, R-259)
are marked where they appear.

---

## Additions and corrections, 2026-10-11

The batch-1 vendor fact records (`../facts/apple.yaml`, `fitbit-google.yaml`, `garmin.yaml`,
`oura.yaml`, `whoop.yaml`, `samsung.yaml`, `empatica.yaml`, `withings.yaml`) carry their own
sources, each with a quote and a retrieval date. They are not copied into this register. Where a
record corrected the comparison matrix or README on 2026-10-11, the older row above that it
supersedes says so in its "Establishes" cell (S-APL-04, S-OUR-01, S-OUR-13, S-WTH-07, S-WTH-09,
S-EMP-11, S2-DEV-06). The quote-backed summary is `../facts/_generated/research-and-access.md`.

The batch-2 records for Module 1 (`../facts/polar.yaml`, `ametris-actigraph.yaml`, `axivity.yaml`,
`activinsights-geneactiv.yaml`, `movesense.yaml`) work the same way and are not copied here either.
Rows they supersede say so in their "Establishes" or "Type" cell: S-POL-01, S-AMT-08, S-AMT-10,
S-AXV-09, S-MVS-04, S-MVS-05 and S2-LAB-02, plus the Movesense datasheet note above.
