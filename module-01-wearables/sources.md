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
| S-APL-03 | ResearchKit & CareKit FAQ | researchandcare.org | https://www.researchandcare.org/faq/ | FAQ | **Direct** | HealthKit access model; higher-frequency HR only in Workouts/ECG sessions; statement that raw ECG is not accessible; Study App Template |
| S-APL-04 | HKElectrocardiogram | Apple | https://developer.apple.com/documentation/healthkit/hkelectrocardiogram | Developer docs | Search summary | ECG samples are voltage collections; `HKElectrocardiogramQuery` returns individual measurements; sampling frequency and count properties |
| S-APL-05 | Investigator Support Program | researchandcare.org | https://www.researchandcare.org/investigator-support-program/ | Program page | Search summary | Apple provides devices and development resources to researchers |
| S-APL-06 | Apple Heart & Movement Study FAQ | Brigham and Women's Hospital | https://appleheartandmovementstudy.bwh.harvard.edu/frequently-asked-questions/ | Study site | Search summary | Study design; Apple-sponsored; AHA and BWH partners; data types collected |
| S-APL-07 | Apple debuts Apple Watch Series 11 | Apple Newsroom | https://www.apple.com/newsroom/2025/09/apple-debuts-apple-watch-series-11-featuring-groundbreaking-health-insights/ | Press release | Secondary | Sept 2025 launch; hypertension notifications; sleep score; sensor complement |
| S-APL-08 | Introducing Apple Watch Ultra 3 | Apple Newsroom | https://www.apple.com/newsroom/2025/09/introducing-apple-watch-ultra-3/ | Press release | Secondary | Ultra 3 sensors incl. depth gauge and water temperature |

## Fitbit / Google

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-FIT-01 | Fitbit Web API reference | Google/Fitbit | https://dev.fitbit.com/build/reference/web-api/ | API docs | **Direct** | 24 endpoint categories; intraday definition; **September 2026 legacy API deprecation notice** |
| S-FIT-02 | Application Design | Google/Fitbit | https://dev.fitbit.com/build/reference/web-api/developer-guide/application-design/ | API docs | **Direct** | Personal/Client/Server app types; **150 req/hr per consented user**; rate-limit headers; intraday approval process |
| S-FIT-03 | Intraday | Google/Fitbit | https://dev.fitbit.com/build/reference/web-api/intraday/ | API docs | Search summary | 1s/1min/5min/15min detail levels; **24-hour retrieval limit on intraday HR, degrading to summary** |
| S-FIT-04 | About the Google Health API | Google | https://developers.google.com/health/about | Developer docs | **Direct** | Successor to Fitbit Web API; data type roadmap Q2/Q3 2026; all Fitbit + Pixel devices; Google OAuth 2.0; **all scopes Restricted**; Reconciled Stream |
| S-FIT-05 | Google Health API REST reference | Google | https://developers.google.com/health/reference/rest | API reference | **Direct** | v4 resources: subscribers, subscriptions, users, dataTypes.dataPoints (incl. rollUp, dailyRollUp, reconcile, exportExerciseTcx), pairedDevices; endpoint `health.googleapis.com` |
| S-FIT-06 | Introducing the next phase of the Fitbit Web API | Fitbit Community | https://community.fitbit.com/t5/Web-API-Development/Introducing-the-next-phase-of-the-Fitbit-Web-API/td-p/5821061 | Vendor forum | Search summary | Migration announcement |
| S-FIT-07 | Fitbit to Google Health API Developer Transition Guide | Validic | https://help.validic.com/space/VCS/5513478151/Fitbit+to+Google+Health+API+Developer+Transition+Guide | Vendor guide | Secondary | Migration mechanics; **mandatory user re-consent** |
| S-FIT-08 | Fitbit Web API Shutdown | Sahha | https://sahha.ai/blog/fitbit-api-sunset-migration/ | Vendor blog | Secondary | Side-by-side window May–30 Sept 2026 |
| S-FIT-09 | Fitbit API Deprecation | Thryve | https://www.thryve.health/blog/fitbit-api-deprecation | Vendor blog | Secondary | Corroborates re-consent and OAuth change |
| S-FIT-10 | Health Connect data types | Google/Android | https://developer.android.com/health-and-fitness/health-connect/data-types | Developer docs | Search summary | 50+ data types; Record subclasses; Medical Records in FHIR; Google Fit supported to end of 2026 |
| S-FIT-11 | The All of Us Research Program's wearables dataset | NIH / *Nature Medicine* | https://www.nature.com/articles/s41591-026-04352-3 | Peer-reviewed | Search summary | 59,000+ participants; 14 years; 39M step, 31M sleep observations; 46% multi-modal linkage |
| S-FIT-12 | Resources for Using Fitbit Data | All of Us | https://support.researchallofus.org/hc/en-us/articles/20281023493908-Resources-for-Using-Fitbit-Data | User support | Search summary | Seven BigQuery tables; minute-level HR and steps; not OMOP CDM |
| S-FIT-13 | The Importance of Data Quality Control in Using Fitbit Device Data From the All of Us Research Program | *JMIR mHealth uHealth* 2023 | https://mhealth.jmir.org/2023/1/e45103 | Peer-reviewed | Search summary | Wear-time and completeness filtering materially affect results |

## Garmin

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-GRM-01 | Health API | Garmin | https://developer.garmin.com/gc-developer-program/health-api/ | Developer docs | **Direct** | Data summaries; Ping/Pull or Push; JSON; commercial use requires licence fee; connect-support@developer.garmin.com |
| S-GRM-02 | Health SDKs Overview | Garmin | https://developer.garmin.com/health-sdk/ | Developer docs | **Direct** | **Live accelerometer, HR, Pulse Ox, respiration, stress streaming**; Standard vs Companion; Standard described as HIPAA-compliant; evaluation free, commercial requires licence fee or device MOQ |
| S-GRM-03 | Health SDK Questions & Answers | Garmin | https://developer.garmin.com/health-sdk/questions-answers/ | Developer FAQ | **Direct** | Real-time streaming + configurable logged data; enterprise framing; contact-gated specifics |
| S-GRM-04 | Program FAQ | Garmin | https://developer.garmin.com/gc-developer-program/program-faq/ | Developer FAQ | **Direct** | Application reviewed in 2 business days; integration 1–4 weeks; no licensing/maintenance fees but some metrics may require a licence fee; "only for business use" |
| S-GRM-05 | Enable Digital Phenotyping with Garmin Devices | Center for Technology and Behavioral Health, Dartmouth | https://www.c4tbh.org/research-tools/enable-digital-phenotyping-with-garmin-devices-in-your-longitudinal-research-studies/ | Academic center | **Direct** | Independent confirmation that the Companion SDK yields **raw accelerometer, beat-to-beat intervals, respiration**; academic partnership with Garmin exists |
| S-GRM-06 | Garmin data source documentation | Rook | https://docs.tryrook.io/data-sources/garmin/ | Integrator docs | Secondary | 16 data types; backfill types on first connect |

## Oura

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-OUR-01 | Oura API Documentation (2.0) | Oura | https://cloud.ouraring.com/v2/docs | API docs | **Direct (browser)** | Full route inventory; OAuth 2.0 only; **PAT deprecation Dec 2025**; scopes; **10-user application cap**; two-tier rate limits; 5,000 req/5 min; webhooks ~30s; **sleep syncs only on user app-open**; 403 on expired subscription; API free for personal and commercial use |
| S-OUR-02 | Error Handling | Oura | https://cloud.ouraring.com/docs/error-handling | API docs | Search summary | Rate-limit behaviour |
| S-OUR-03 | Oura for Organizations | Oura | https://ouraring.com/business | Product page | Search summary | Enterprise offering; 200+ customers incl. USAF, Navy, Army, NASA, universities |
| S-OUR-04 | Explore the Technology in Oura Ring 4 / Smart Sensing | Oura | https://ouraring.com/blog/technology-in-oura-ring-4/ · https://ouraring.com/blog/smart-sensing/ | Vendor blog | Search summary | 18-pathway PPG; IR alignment sensor; NTC thermistor; vendor-claimed signal-quality improvements |
| S-OUR-05 | Study from Top US Hospital Finds Oura Ring Most Accurate | Oura | https://ouraring.com/blog/2024-sensors-oura-ring-validation-study/ | Vendor blog on peer-reviewed work | Search summary | Robbins 2024 kappa figures as promoted by Oura |
| S-OUR-06 | The Oura API | Oura Member Care | https://support.ouraring.com/hc/en-us/articles/4415266939155-The-Oura-API | Support | Search summary | Consumer-facing API description |

## WHOOP

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-WHP-01 | **WHOOP API Terms of Use** | WHOOP | https://developer.whoop.com/api-terms-of-use/ | Legal | **Direct** | **No permanent copies / databases**; no marketing/selling/licensing/leasing data even with consent; **no HIPAA representation**; non-compete; deletion on termination; encryption obligations |
| S-WHP-02 | WHOOP Developer Platform introduction | WHOOP | https://developer.whoop.com/docs/introduction/ | Developer docs | **Direct** | v2 API; v1 webhooks removed; Recovery/Sleep/Strain/Workouts; app approval required |
| S-WHP-03 | API Rate Limiting | WHOOP | https://developer.whoop.com/docs/developing/rate-limiting/ | Developer docs | Search summary | **100 req/min, 10,000 req/day per client**; rate-limit headers; increases on request |
| S-WHP-04 | Getting Started | WHOOP | https://developer.whoop.com/docs/developing/getting-started/ | Developer docs | Search summary | Six scopes: recovery, cycles, workout, sleep, profile, body_measurement |
| S-WHP-05 | Whoop 5.0 vs Whoop MG | Wareable | https://www.wareable.com/wearable-tech/whoop-5-vs-whoop-mg-which-membership-explained | Trade press | Secondary | Membership tiers and pricing; MG ECG and BP insights; sensor claims |
| S-WHP-06 | WHOOP Unite / Ashley Addiction Treatment partnership | Business Wire | https://www.businesswire.com/news/home/20221110005420/en | Press release | Secondary | WHOOP Unite exists and has been used in a clinical research partnership |

## Samsung

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-SAM-01 | Privileged Health SDK FAQ | Samsung | https://developer.samsung.com/health/privileged/faq.html | Developer FAQ | **Direct** | **Accelerometer 25 Hz, HR with IBI, PPG, skin temperature continuous; BIA and ECG on-demand, one at a time**; Watch4+ Wear OS powered by Samsung; Partner Program request; package name + SHA-256; `SDK_POLICY_ERROR`; **does not share data with Samsung Health** |
| S-SAM-02 | Samsung Health SDK Suite announcement | Samsung Mobile Press | https://www.samsungmobilepress.com/articles/samsungs-new-health-software-development-kit-suite-powers-advancements-in-healthcare-innovation | Press release | Search summary | Sept 2024 SDK Suite; Sensor/Data/Accessory/Research components; **continuous PPG IR and Red LED access for the first time** |
| S-SAM-03 | Samsung Electronics Unveils Samsung Health Research Stack | Samsung Newsroom | https://news.samsung.com/global/samsung-electronics-unveils-samsung-health-research-stack | Press release | Search summary | Open-source; SDK + backend + web portal; Alpha 2022 → 1.0 2023 → Research Stack 2024 → 2.0 Beta; available to companies and medical institutions; used in domestic and international clinical studies |
| S-SAM-04 | Research Stack overview / FAQ / release notes | Samsung | https://developer.samsung.com/health/research/overview.html | Developer docs | Search summary | Research Stack structure; Galaxy Watch5+ compatibility statement (**conflicts with S-SAM-01's Watch4+**) |
| S-SAM-05 | Health features on the Galaxy Watch8 | Samsung | https://www.samsung.com/ie/support/mobile-devices/health-features-on-the-galaxy-watch8-and-watch8-classic/ | Support | Search summary | Watch8 sensor complement and health features |
| S-SAM-06 | Samsung's Expanded Wearables Portfolio | Samsung Newsroom | https://news.samsung.com/global/samsungs-expanded-wearables-portfolio-unlocks-intelligent-health-experiences-for-all | Press release | Search summary | Antioxidant Index; Vascular Load; Bedtime Guidance; Galaxy Ring |

## Polar

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-POL-01 | polar-ble-sdk | Polar (GitHub) | https://github.com/polarofficial/polar-ble-sdk | Open-source SDK | **Direct** | Device/stream support matrix; Android and iOS. **Note: this README matrix is incomplete and partly misleading — it omits H10 accelerometry and Verity Sense gyro/magnetometer, and implies ECG for Verity Sense. Superseded by the per-product docs S2-POL-01/02** |
| S-POL-02 | Research tools | Polar | https://www.polar.com/en/science/research-tools/ | Vendor research page | **Direct** | H10 raw ECG and 3D acceleration; Verity Sense PPG and acceleration; built-in memory; Open AccessLink; Team Pro API; 600+ studies (H10, 2022–23), 180 (Team Pro), 1,000+ papers/yr |
| S-POL-03 | PolarH10.md / PolarVeritySense.md | Polar (GitHub) | https://github.com/polarofficial/polar-ble-sdk/blob/master/documentation/products/PolarH10.md | SDK product docs | Not retrieved | Per-device sampling rates — **outstanding** |
| S-POL-04 | Let's Build Products Together | Polar | https://www.polar.com/us-en/developers | Developer portal | Search summary | AccessLink description |

## Withings

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-WTH-01 | **Advanced Research API** | Withings | https://developer.withings.com/developer-guide/v3/withings-solutions/research-apis/ | Developer docs | **Direct** | ScanWatch only; 3-axis accelerometer 25 Hz default **up to 100 Hz**; PPG with 3 LEDs (green/red/IR) or 1 (green); gated program |
| S-WTH-02 | **Raw data** | Withings | https://developer.withings.com/developer-guide/v3/integration-guide/public-health-data-api/data-api/raw-data/ | Developer docs | **Direct** | PPG 3 wavelengths; accelerometer ±4 g; **both ≈24.824 Hz** (conflicts with S-WTH-01); contracted partners only; **activation disables all other watch features**; **battery 4–7× faster drain, 3–4 days**; ECG not listed |
| S-WTH-03 | Research & clinical trials | Withings Health Solutions | https://www.withings.com/us/en/health-solutions/research-clinical-trials | Vendor page | **Direct (browser)** | Medical-grade clinically validated devices; flexible retrieval via cellular, mobile app, RPM platform, or API; partnership model; study index |
| S-WTH-04 | Partner Hub | Withings | https://developer.withings.com/ | Developer portal | Direct (gated) | Detailed API reference is behind login |
| S-WTH-05 | Medable–Withings partnership | Business Wire | https://www.businesswire.com/news/home/20220721005032/en/ | Press release | Secondary | DCT integration precedent |

## Empatica

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-EMP-01 | Health Monitoring Platform for Research Studies | Empatica | https://www.empatica.com/en-eu/platform/research-studies/ | Vendor page | **Direct** | Sensors (optical PPG, ventral EDA, accelerometer, digital temperature); **18 validated biomarkers named**; raw CSV via Care Portal; **no real-time streaming**; studies/sites/unlimited participant credentials; multiple sessions per device; live wear-time tracking |
| S-EMP-02 | Raw Data | Empatica | https://www.empatica.com/rawdata/ | Vendor page | **Direct** | Raw streams: accelerometer, temperature, EDA, steps, BVP, systolic peaks, user tags; **Avro format**; "no black box algorithms"; configurable sensor modes and sampling frequencies; FDA-cleared and CE |
| S-EMP-03 | Understanding your Empatica Health Monitoring Platform Plan | Empatica Support | https://support.empatica.com/hc/en-us/articles/17721117772317 | Support | Search summary (direct fetch 403) | Care app = Enterprise; Care Lab app = Academic & Basic Research; standard vs complete suite |
| S-EMP-04 | EmbracePlus specifications | Empatica (via Tec de Monterrey mirror) | https://ifelldh.tec.mx/sites/g/files/vgjovo1101/files/Empatica_EmbracePlus.pdf | Spec sheet | Search summary | **EDA 4 Hz, PPG 64 Hz, accelerometer 64 Hz** |
| S-EMP-05 | Empatica Actigraphy | Empatica | https://www.empatica.com/embraceplus/actigraphy | Vendor page | Search summary | **7-day battery with raw 64 Hz accelerometry; 14-day extended mode**; actigraphy counts |
| S-EMP-06 | Empatica Health Monitoring Platform receives FDA clearance | Empatica | https://www.empatica.com/blog/the-empatica-health-monitoring-platform-receives-fda-clearance | Vendor blog | Search summary | Nov 2022 clearance; EDA, SpO2, skin temperature, movement during sleep |
| S-EMP-07 | New FDA clearance for cardiac digital biomarkers | Empatica / PR Newswire | https://www.empatica.com/blog/empatica-receives-new-fda-clearance-for-cardiac-digital-biomarkers/ | Press release | Search summary | Subsequent cardiac biomarker clearance |

## Ametris (formerly ActiGraph)

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-AMT-01 | CentrePoint | Ametris | https://ametris.com/centrepoint | Product page | **Direct** | Cloud platform for clinical investigations; LEAP and Insight Watch; **"future-proof raw sensor data reprocessed indefinitely"**; CentrePoint API; wear-compliance portal; cellular gateway or mobile app; 70+ countries; "Ametris, a Signant Health Company" |
| S-AMT-02 | Ametris home | Ametris | https://ametris.com/ | Company site | **Direct** | Device and platform inventory (LEAP, Insight Watch, wGT3X-BT, Connect, CentrePoint, ActiLife, Algorithm Marketplace); measurement domains; FDA-cleared medical-grade framing; services |
| S-AMT-03 | ActiGraph Rebrands as Ametris | Ametris | https://blog.ametris.com/news/actigraph-rebrands-as-ametris | Press release | Search summary | **Rebrand 25 June 2025**; Biofourmis Connect acquisition Jan 2025; Biovitals and RhythmAnalytics SaMD |
| S-AMT-04 | Signant Health Acquires Ametris | Signant Health / PR Newswire | https://signanthealth.com/company/news/signant-health-acquires-ametris | Press release | Search summary | **Acquisition announced May 2026** |
| S-AMT-05 | ActiGraph pricing guides | Fibion (competitor) | https://web.fibion.com/articles/actigraph-pricing-information-guide/ | Third-party marketing | Search summary | Indicative and dated figures: GT3X+/wGT3X-BT $325–1,016; GT9X ~$500 and EOL; CentrePoint Hub ~$600 or ~$300/yr; ActiLife ~$1,695; CentrePoint software ~$3,500/yr. **Competitor source — treat with caution** |

## Axivity / GENEActiv

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-AXV-01 | AX3 | Open Movement / Newcastle University | https://github.com/digitalinteraction/openmovement/wiki/AX3 | Open-source project | Search summary | AX3 accelerometer, AX6 accel+gyro; **firmware/software BSD 2-clause; hardware and enclosure CC BY 3.0** |
| S-AXV-02 | UK Biobank Physical Activity Monitor | UK Biobank | https://biobank.ndph.ox.ac.uk/ukb/ukb/docs/PhysicalActivityMonitor.pdf | Cohort documentation | Search summary | AX3 chosen 2012; **100 Hz, ±8 g, 7 days**; timed postal start at 10am two working days after dispatch |
| S-AXV-03 | Large Scale Population Assessment of Physical Activity Using Wrist Worn Accelerometers | Doherty et al., *PLOS ONE* 2017 | https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0169649 | Peer-reviewed | Search summary | 100,000+ participants; **equivalence with GENEActiv on multi-axis shaking tests**; Whitehall II, Fenland, Pelotas comparison |
| S-AXV-04 | actipy | Oxford Wearables Group | https://github.com/OxWearables/actipy | Open-source SDK | Search summary | Python processing SDK |
| S-AXV-05 | Methods — accelerometer documentation | Oxford | https://biobankaccanalysis.readthedocs.io/en/latest/methods.html | Documentation | Search summary | Open ML activity classification pipeline used on UK Biobank |
| S-AXV-06 | Axivity | Axivity Ltd | https://axivity.com/ · https://axivity.com/case-studies/biobank | Vendor site | Search summary | Commercial supplier; UK Biobank case study |

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

## Validation and evidence (cross-platform)

| ID | Title | Authors / Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-VAL-01 | Accuracy of Three Commercial Wearable Devices for Sleep Tracking in Healthy Adults | Robbins et al., *Sensors* 2024;24(20):6532 | https://www.mdpi.com/1424-8220/24/20/6532 · open mirror: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11511193/ | Peer-reviewed | Search summary | N=35, single night, PSG. **4-stage kappa: Oura 0.65, Apple Watch 0.60, Fitbit Sense 0.55**; Oura deep-sleep sensitivity 79.5% |
| S-VAL-02 | A performance validation of six commercial wrist-worn wearable sleep-tracking devices for sleep stage scoring compared to polysomnography | Schyvens et al., *SLEEP Advances* 2025;6(2):zpaf021 | https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472 · open mirror: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12038347/ | Peer-reviewed | Search summary | N=62. Devices: Fitbit Charge 5, Fitbit Sense, **Withings ScanWatch**, Garmin Vivosmart 4, Whoop 4.0, Apple Watch Series 8. Most differed significantly from PSG on TST, SE, WASO, light sleep. **Deep-sleep sensitivity: Whoop 69.6%, Apple 50.7%, Fitbit Sense 48.3%, Charge 5 43.3%, Garmin 32.1%** |
| S-VAL-03 | Reliability and Validity of Commercially Available Wearable Devices for Measuring Steps, Energy Expenditure, and Heart Rate: Systematic Review | Fuller et al., *JMIR mHealth uHealth* 2020;8(9):e18694 | https://mhealth.jmir.org/2020/9/e18694/ | Peer-reviewed | Search summary | **Apple and Samsung highest step validity; Apple, Fitbit, Garmin accurate ~50% of the time; no brand within acceptable limits for energy expenditure** |
| S-VAL-04 | Accuracy and Precision of Energy Expenditure, Heart Rate, and Steps Measured by Combined-Sensing Fitbits Against Reference Measures | Chevance et al., *JMIR mHealth uHealth* 2022;10(4):e35626 | https://mhealth.jmir.org/2022/4/e35626 | Peer-reviewed | Search summary | Fitbit **underestimates** HR, EE, and steps; acceptable on average for steps and HR; EE may be inaccurate for research |
| S-VAL-05 | Keeping Pace with Wearables: A Living Umbrella Review of Systematic Reviews | (umbrella review) | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11560992/ | Peer-reviewed | Search summary | HR mean bias ±3%; steps MAPE −9 to 12%; EE mean bias −3 kcal/min, range −21.3% to +14.8%; pervasive methodological heterogeneity |
| S-VAL-06 | Feasibility and acceptability of collecting passive phone usage and sensor data via Apple SensorKit | (medRxiv / PMC) | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12349082/ | Peer-reviewed / preprint | Search summary | Empirical SensorKit deployment experience |
| S-VAL-07 | Analysis and postprocessing of ECG or heart rate data from wearable devices beyond the proprietary cloud and app infrastructure of the vendors | (ScienceDirect) | https://www.sciencedirect.com/science/article/pii/S2666693621001158 | Peer-reviewed | Search summary | Apple Watch 1-lead ECG voltage measurements and classification retrievable via HealthKit libraries |

---

## Sources sought but not obtained

| Target | URL | Outcome |
|---|---|---|
| Garmin Health API summaries reference | https://developer.garmin.com/gc-developer-program/health-api/summaries/ | **404** — full data-type list unobtained |
| Oura developer docs (alt host) | https://developer.ouraring.com/docs | **404** |
| Withings research page (direct fetch) | https://www.withings.com/us/en/health-solutions/research-clinical-trials | **403** — retrieved via browser instead |
| Empatica plan support article (direct fetch) | https://support.empatica.com/hc/en-us/articles/17721117772317 | **403** — retrieved via search summary |
| Apple HealthKit documentation body | https://developer.apple.com/documentation/healthkit | JS-rendered; only title returned |
| Polar per-product SDK sampling rates | https://github.com/polarofficial/polar-ble-sdk/blob/master/documentation/products/ | Not retrieved this session |

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
| S2-GHA-03 | Data types | https://developers.google.com/health/data-types | **Direct** | Interval / Sample / Session / Daily Aggregate record types; **Heart Rate is a Sample type with no documented interval**; HRV, SpO2, respiratory rate, RHR as Daily Aggregates; ECG and Irregular Rhythm as Sessions |
| S2-GHA-04 | Scopes | https://developers.google.com/health/scopes | **Direct** | 17 scopes under `googleapis.com/auth/googlehealth`, `.readonly`/`.writeonly` variants |
| S2-GHA-05 | Migration guide | https://developers.google.com/health/migration | **Direct** | Tokens cannot be transferred; re-consent UX guidance; backfill after re-auth; data gaps for non-re-authenticating users; **no turndown date stated** |
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
| S2-LAB-01 | Labfront pricing | https://www.labfront.com/pricing | **Direct** | **Tester free (5 participants, 30-day window); Basic $500/yr (20, +$10 each); Advanced $1,250/yr (20, +$25 each, all integrations, customisable high-resolution sampling)**; analytics add-ons from $2,000; EMA in all tiers; grants programme |
| S2-LAB-02 | Labfront compatible devices | https://www.labfront.com/compatible-devices | **Direct** | Garmin vívosmart 5 / vívoactive 5 (BBI, steps, HR, SpO2, respiration, accelerometer), **Movesense HR2 (RR, ECG, IMU, accel, gyro, magnetometer)**, Garmin Index BPM and S2 scale, Dexcom G7 |
| S2-LAB-03 | Labfront–Garmin collaboration | https://www.labfront.com/blog/labfront-and-garmin-collaboration | Search summary | Labfront configures Garmin devices via the Health SDKs to **increase sensor resolution beyond stock** |

### Movesense

| ID | Title | URL | Retrieval | Establishes |
|---|---|---|---|---|
| S-MVS-01 | Specifications | https://www.movesense.com/specifications/ | **Direct** | MD is **Class IIa Medical Device MDR 2017/745**; Flash has **128 MB internal memory**; RR intervals at **1 ms** accuracy and resolution; 9-axis IMU across the range; HR2 9.4 g |
| S-MVS-02 | Get started | https://www.movesense.com/get-started/ | **Direct** | Open APIs; **custom sensor firmware supported**; desktop simulator; Bitbucket repositories; firmware upload via Showcase app |
| S-MVS-03 | Movesense home | https://www.movesense.com/ | **Direct** | Product families: CardioRTHM, Movesense Medical, Movesense Sport |
| S-MVS-04 | HR2 / MD product pages and search summary | https://www.movesense.com/product/movesense-sensor-hr2/ | Search summary | **ECG 125–512 Hz**; **IMU 13 Hz–1.6 kHz**; **no licence cost**; business-customer sales, sales@movesense.com; Kubios integration |

### Emerging platforms

| ID | Title | URL | Retrieval | Establishes |
|---|---|---|---|---|
| S-EMG-01 | UltraSignal | https://www.ultrahuman.com/ultrasignal/ | **Direct** | **Raw PPG, temperature and accelerometer** exposed; loaner developer kit; application reviewed |
| S-EMG-02 | Accessing the Ultrahuman Partnership API | https://www.ultrahuman.com/blog/accessing-the-ultrahuman-partnership-api/ | Search summary | **Whitelist-only**, token from partner.ultrahuman.com, discretionary approval taking days |
| S-EMG-03 | Biostrap research | https://biostrap.com/research/ | **Direct** | Multi-device framework; **raw and/or processed PPG, gyroscope, accelerometer**; **customisable sampling rates**; integrated surveys; FDA-cleared Thermo Patch ±0.1 °C |
| S-EMG-04 | Biostrap science / validation | https://biostrap.com/science/ · https://biostrap.com/validation/ | Search summary | Vendor-compiled "14 publications and 22 clinical studies"; NCT05279066 |
| S-EMG-05 | Verily and Samsung collaboration | https://verily.com/perspectives/verily-and-samsung-collaborate-to-accelerate-clinical-research-with-the-galaxy-watch-and-pre-platform | Search summary | **March 2026**; Galaxy Watch 8 into Verily **Pre** / **Viewpoint Evidence**; **raw PPG and accelerometer/gyroscope motion signals** to researchers |
| S-EMG-06 | Verily Study Watch coverage | https://www.mobihealthnews.com/news/verilys-research-wearable-lands-fda-clearance-demand-ecg | Search summary | On-demand ECG 510(k); irregular pulse 510(k); Parkinson's motor exam rejected; records ECG, HR, **EDA**, inertial; weeks of onboard raw storage; never sold to consumers |
| S-EMG-07 | Samsung Health Research Stack GitHub | https://github.com/S-HealthStack | Search summary | **Apache 2.0**; `backend-system`, `app-sdk`, `web-portal` repositories |
| S-EMG-08 | Ultrahuman privacy review | https://www.mozillafoundation.org/en/nothing-personal/ultrahuman-ring-privacy-review/ | Search summary | Independent privacy assessment of Ring AIR |

### Device generations and pricing

| ID | Title | URL | Retrieval | Establishes |
|---|---|---|---|---|
| S2-DEV-01 | Apple Watch Series 11 tech specs | https://www.apple.com/apple-watch-series-11/specs/ | **Direct** | Full sensor list **including depth gauge to 6 m and water temperature sensor on Series 11**; battery 24 h / 38 h Low Power; 0–80% in ~30 min; Blood Oxygen wellness-only wording, no stated geographic restriction |
| S2-DEV-02 | Oura Ring product page | https://ouraring.com/product/rings | **Direct** | **Oura Ring 5 exists**; membership **$5.99/mo or $69.99/yr**, first month free; feature inventory |
| S2-DEV-03 | Oura Ring 5 launch | https://www.businesswire.com/news/home/20260528686853/en/ · https://techcrunch.com/2026/05/28/oura-unveils-its-ring-5-with-a-thinner-lighter-design-starting-at-399/ | Search summary | Announced 28 May 2026, shipping 4 June 2026; **$399 / $499**; 40% smaller, 2.28 mm thick, from 2 g; 12 signal pathways; **Health Radar (Blood Pressure Signals, Nighttime Breathing)**, GLP-1 insights; Blood Pressure Signals gives **no systolic/diastolic values** |
| S2-DEV-04 | Fitbit Air launch coverage | https://www.androidcentral.com/wearables/fitbit/fitbit-air-launch-specs-price · https://www.forbes.com/sites/forbes-personal-shopper/2026/05/07/google-fitbit-air-launch-2026/ | Search summary | **Launched 7 May 2026, $99.99**, shipping 26 May; screenless, 12 g; PPG + red/IR SpO2 + skin temp + 3-axis accel + gyroscope; **HR saved at 2-second intervals**; 7-day battery; Google Health app |
| S2-DEV-05 | Fitbit app → Google Health rebrand | https://www.androidcentral.com/wearables/fitbit/the-old-fitbit-app-is-becoming-google-health · https://www.thurrott.com/google/336407/ | Search summary | **Rebranded 19 May 2026**, rollout complete 26 May; Fitbit Premium → Google Health Premium with Gemini Health Coach; badges, DMs and Sleep Profile removed; Google Fit sunsets end of 2026 |
| S2-DEV-06 | WHOOP membership tiers | https://www.whoop.com/us/en/membership/ (403 to fetch; via trade coverage) | Search summary | **One $199/yr, Peak $239/yr, Life $359/yr**; Life includes **WHOOP MG**; hardware included in all tiers |
| S2-DEV-07 | Empatica Academic & Basic Research plan store page | https://www.empatica.com/store/platform-professional/ | **Direct** | **Device from $1,166.40; 3-yr bundle $2,332.80 list / $1,749.60 academic; 5-yr $2,916 / $2,187 academic**; "11+ digital biomarkers"; volume discounts at 5+ |
| S2-DEV-08 | Withings watch lineup | https://www.withings.com/us/en/watches · https://www.withings.com/us/en/scanwatch-nova | Search summary | ScanWatch Light (no ECG), ScanWatch 2, ScanWatch Nova (~$599), Nova Brilliant; Nova multi-wavelength PPG with 16 optical channels; ~30-day battery |

### Fitbit-to-Google migration timeline (third-party corroboration)

| ID | Title | URL | Retrieval | Establishes |
|---|---|---|---|---|
| S2-MIG-01 | General FAQs for the Fitbit to Google Health Migration | https://help.validic.com/space/VCS/5436309513/ | Search summary | New `google_health` integration available from May 2026; recommendation not to launch before late May |
| S2-MIG-02 | Google Health Community thread on API availability | https://support.google.com/googlehealth/thread/439040688/ | Search summary | Side-by-side operation to **30 September 2026** |


---

## Link check — 2026-08-21

All URLs above were checked with an HTTP request on 2026-08-21.

- **200 OK:** all primary vendor documentation links cited as Verified.
- **403 (bot-blocked, not dead):** `withings.com` research pages, `academic.oup.com`, `mdpi.com`.
  These load normally in a browser; open PMC mirrors are given for the two papers.
- **404 (genuinely unavailable):** `developer.garmin.com/gc-developer-program/health-api/summaries/`
  and `developer.ouraring.com/docs`. Both are recorded in "Sources sought but not obtained" above.

### Second-pass retrieval notes (2026-08-21)

- PMC mirrors of both PSG papers were read **in full**; this corrected several first-pass claims.
- The Garmin Enhanced BBI PDF was downloaded and read page by page.
- `withings.com` and `whoop.com/membership` return **403** to automated fetch but load in a browser;
  their content here comes from browser rendering or trade coverage and is labelled accordingly.
- `developers.google.com/health/*` pages were all retrievable directly and are the strongest sources
  added in this pass.
- Movesense's detailed datasheets sit behind a survey-gated PDF download; the specification page and
  product pages were used instead, so exact battery and IMU range figures remain **Unclear**.
