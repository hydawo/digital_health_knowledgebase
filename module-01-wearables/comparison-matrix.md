# Module 1, Wearables Comparison Matrix

**Rebuilt 2026-10-10 from the profiles.** Every cell below was rewritten from the current profiles in
`profiles/` (corrected and re-verified in commit c774edb) and from `validation-evidence.md`. Where a
profile says Unclear, the cell says Unclear. Nothing here is newer than the profile it comes from: if
a cell and a profile disagree, the profile wins and this file is out of date.

**Confidence markers in cells.** (C) = Corroborated, (R) = Reported, copied from the profile. A cell
with no marker repeats a profile statement that the profile marks Verified or leaves unmarked; check
the profile before relying on it for a decision. The 2026-08-21 and 2026-08-24 versions of this file
are superseded; the independent review of 2026-10-10 (`../shared/reviews/2026-10-10-independent-review.md`)
lists what was wrong with them.

Several tables are used deliberately. Do not read any single table as a ranking.

---

## Dated items to check before planning a study

| Date | Item | Source profile |
|---|---|---|
| 30 September 2026 | Google ended support for the legacy Fitbit Web API | `fitbit-google.md` |
| **30 October 2026** | **The legacy Fitbit Web API is turned off** and stops syncing data | `fitbit-google.md` |
| As of 2026-10-10 | **Google Health API is not onboarding new projects** ("While we are not onboarding new projects at this time..."); no reopening date | `fitbit-google.md` |
| Since spring 2026 | **Garmin Connect Developer Program access requests paused**, no reopening date (C) | `garmin.md` |
| **12 October 2026** | **Withings+ membership required** for participants whose Withings accounts are created on or after this date to share data with a Start for Free app, including via Apple Health or Google Health | `withings.md` |
| 6 October 2026 | WHOOP API Terms of Use in force: no permanent copies and no AI or ML training on WHOOP data, unless authorised by the data owner or by law | `whoop.md` |
| 8 June 2026 | Oura API and MCP Agreement in force: retain data only as long as strictly necessary, 72-hour deletion on request, no AI or ML training | `oura.md` |
| December 2025 | Oura personal access tokens retired; OAuth 2.0 only | `oura.md` |
| 24 October 2024 | Last code push to any Samsung Health Research Stack repository (checked 2026-10-10) | `samsung.md` |
| 14 May 2026 | Signant Health announced its acquisition of Ametris (agreement announced 16 April 2026) | `ametris-actigraph.md` |

---

## Table 1, Ecosystem orientation and access model

| Ecosystem | Primary orientation | Access model | Vendor cloud in data path? | Approval required? | Can a new study start today without vendor contact? |
|---|---|---|---|---|---|
| **Apple** | Consumer | HealthKit read by a researcher-built iOS app; SensorKit for research signals | **No.** Apple never receives the study copy | SensorKit only: per-study Apple approval plus IRB approval | HealthKit yes; SensorKit no |
| **Fitbit / Google** | Consumer | Google Health API (Google OAuth 2.0, REST). Legacy Fitbit Web API unsupported since 30 Sep 2026, **off 30 Oct 2026** | Yes | Most Google Health API scopes are Restricted; unverified apps capped at 100 users; verification and a CASA assessment above that; research apps file a Health Research Attestation | **No.** Google is not onboarding new projects (2026-10-10). Routes: an intermediary that already holds access, participant self-export, *All of Us* |
| **Garmin** | Consumer / athletic | Health API (cloud, push or ping/pull) or Health SDK, Standard or Companion (enterprise partners) | Health API yes; Standard SDK keeps data out of Garmin Connect | Business-use programme application; **new access requests paused since spring 2026 (C)** | **No.** Practical routes: Labfront, Fitabase or Fitrockr |
| **Oura** | Consumer | API v2 (OAuth 2.0 only) with webhooks; Oura for Organizations research offering | Yes | An API app is limited to 10 users until Oura approves it; research offering by contact | Yes, up to 10 users, under the API and MCP Agreement |
| **WHOOP** | Consumer | API v2 (OAuth 2.0) with webhooks | Yes | App approval; member tiers raised one step at a time by manual review | Yes, Sandbox tier only (10 members) |
| **Samsung** | Consumer | Samsung Health Sensor SDK (formerly Privileged Health SDK) on the watch; Research Stack, self-hosted, no code updates since Oct 2024 | **No** for the Sensor SDK path | SDK v1.4.1 is a public download; **Samsung Partner Program approval to distribute** the app (package name and SHA-256 registered) | Development and testing yes (developer mode); deployment no |
| **Polar** | Athletic / research | Open BLE SDK (GitHub), or AccessLink cloud API | **No** for BLE; yes for AccessLink | **None** for the BLE SDK; any registered Polar Flow user can create an AccessLink client | **Yes** |
| **Withings** | Connected health devices | Public Health Data API (Start for Free, Enterprise, Advanced Biomarkers plans); Advanced Research API for raw data | Yes; EU or US medical cloud | Raw data: contracted partners only; free plan above 10 users: Withings review | Yes on the free plan, up to 10 users; **Withings+ needed from 12 Oct 2026** for participants with new accounts |
| **Empatica** | Research / medical | Care Portal; CSV download; Amazon S3 data access keys | Yes | Academic plan bought from the store; academic discount by application with an institutional email | Yes for the academic plan; Enterprise by quote |
| **Ametris (ActiGraph)** | Clinical trials | CentrePoint platform and V3 API; legacy ActiLife desktop workflow | CentrePoint yes; ActiLife local | Quote; API access must be enabled by Ametris | No |
| **Axivity / GENEActiv** | Research | **USB download. No cloud, no API, no account** | **No** | **None** | Axivity yes (online shop); GENEActiv by quote |
| **Movesense** | Open sensor | BLE to the team's own app; onboard logging (Flash); custom firmware | **No** | None to develop; SDK under a proprietary 12-month evaluation licence, separate agreement for commercialisation | Yes |
| **Ultrahuman** | Consumer ring | UltraSignal (application, loaned developer kit) or Partner API (OAuth for approved apps) | Partner API yes | Yes for both routes | No |
| **Biostrap (now Sensor Bio)** | Research platform | RPM dashboard or custom pipelines; API or Bluetooth SDKs (R) | Unclear | Demo request only | No |
| **Verily Study Watch** | Clinical research only | Verily Pre and Viewpoint Evidence | Yes | Enterprise and pharma engagement | No; Study Watch status Unclear (no current product page found) |

---

## Table 2, Sensors present (hardware, device-dependent)

✓ = present on the named device. "some" = some models in the line. "No" = absent. "Unclear" = the
profile does not establish it. **Presence is not access**; see Table 3.

| Device | PPG | ECG | Accel | Gyro | Temp | SpO2 | GPS | Baro | EDA | BIA |
|---|---|---|---|---|---|---|---|---|---|---|
| Apple Watch (recent) | ✓ | ✓ (Series 4+, Ultra; region-gated) | ✓ | ✓ | ✓ (Series 8+, Ultra) | ✓ (Series 6+, Ultra) | ✓ (GPS models) | ✓ | No | No |
| Fitbit / Pixel Watch | ✓ | some (Sense, Sense 2, Charge 5 and 6) | ✓ | Unclear (Fitbit Air has one, C) | some | some | some | some | some (Sense, Sense 2) | No |
| Garmin | ✓ | some (Venu 3 and newer) | ✓ | some | some | some | ✓ (most models) | some | No | No |
| Oura Ring (Gen3, 4, 5) | ✓ | No | ✓ | Unclear (not documented as user-accessible) | ✓ | ✓ | No | No | No | No |
| WHOOP 4.0 / 5.0 / MG | ✓ | MG | ✓ | Unclear | ✓ (4.0+) | ✓ (4.0+) | No | Unclear | No | No |
| Samsung Galaxy Watch8 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | some (LTE and GPS models) | ✓ | **✓ (Watch8 and later)** | ✓ |
| Polar H10 | No | ✓ | ✓ | No | No | No | No | No | No | No |
| Polar Verity Sense | ✓ | No | ✓ | ✓ (plus magnetometer) | No | No | No | No | No | No |
| Polar 360 / Loop | ✓ | No | ✓ | Unclear | ✓ (skin) | Unclear | Unclear | Unclear | No | No |
| Movesense MD / Flash / HR2 | No | ✓ | ✓ | ✓ (plus magnetometer) | some (MD, Flash) | No | No | Unclear | No | No |
| Withings ScanWatch 2 | ✓ | ✓ | ✓ | Unclear | ✓ | ✓ | Unclear | ✓ | No (Body Scan scale has EDA) | No (Body Scan scale has segmental impedance) |
| Ultrahuman Ring AIR | ✓ | Unclear | ✓ | Unclear | ✓ | Unclear (nightly SpO2 metric, R) | Unclear | Unclear | Unclear | Unclear |
| Biostrap / Sensor Bio wrist | ✓ | Unclear | ✓ | ✓ | Separate Thermo Patch (C) | Unclear | Unclear | Unclear | Unclear | Unclear |
| Verily Study Watch | Unclear (records heart rate, C) | ✓ (C) | ✓ (inertial, C) | Unclear | Unclear | Unclear | Unclear | Unclear | ✓ (C) | Unclear |
| Empatica EmbracePlus | ✓ | No | ✓ | ✓ (selected sensor modes) | ✓ | ✓ (FDA K221282, no-motion conditions only; academic-plan output Unclear) | No | Unclear | ✓ | No |
| Ametris LEAP | ✓ (green, red, IR) | No | ✓ | ✓ (IMU) | ✓ (skin) | No | No | ✓ | No | No |
| Ametris Insight Watch / wGT3X-BT | No | No | ✓ | No | Insight Watch (near-body) | No | No | No | No | No |
| Axivity AX3 / AX6 | No | No | ✓ | AX6 only | No | No | No | No | No | No |
| GENEActiv | No | No | ✓ | No | ✓ (near-body) | No | No | No | No | No |

Raw EDA has three routes in this module: Empatica, **Samsung Galaxy Watch8 and later (1 Hz, via
the Health Sensor SDK)** and the Verily Study Watch (C). Fitbit Sense has an EDA sensor but no EDA
data type in the Google Health API. Ambient light is also present on the GENEActiv and the
wGT3X-BT; Ametris LEAP also has a microphone, disabled by default.

---

## Table 3, Raw signal availability to researchers (the decisive table)

| Ecosystem | Raw accel | Raw PPG waveform | ECG | IBI / RR / BBI | Raw EDA | Route |
|---|---|---|---|---|---|---|
| **Apple** | **SensorKit only** (`accelerometer`, iOS 14+, research entitlement); Core Motion in-app; not via HealthKit | **SensorKit only** (`photoplethysmogram`, iOS 17.4+); rate and capture schedule undocumented; not via HealthKit | Per-recording voltage samples via `HKElectrocardiogramQuery` (Verified 2026-10-09); SensorKit `electrocardiogram` (iOS 17.4+); no continuous ECG | Context-limited: `HKHeartbeatSeriesSample` beat timestamps during ECG and some workout or Breathe sessions | n/a | HealthKit; SensorKit (Apple-approved study entitlement) |
| **Fitbit / Google** | No | No | Google Health API `electrocardiogram` session documented with raw waveform voltage samples per on-demand reading; not tested with a real pull | No (HRV as an RMSSD sample type) | No EDA data type in the API; treat as unavailable | Google Health API, **not onboarding new projects** |
| **Garmin** | **Health SDK only** (listed as "Accelerometer" for streaming and logging; rate not published); not via the Health API; Connect IQ in-app | No | Not documented via the Health API | **Enhanced BBI with per-beat confidence**: Health API (licence fee for commercial use) and Health SDK streaming and logging. Fitabase's API route captures it during sleep; Labfront's SDK route across the day (R). Garmin's 2023 technical note says it is measured during sleep; whether the Health API delivers it outside sleep is Unclear | n/a | Health SDK (enterprise partners), Health API (paused to new applicants), or Labfront / Fitabase / Fitrockr |
| **Oura** | No | No | n/a | No (HR at 5-minute increments; nightly HRV) | n/a | API v2, derived only |
| **WHOOP** | No | No | MG ECG feature exists; no ECG scope in the API | No | n/a | API v2, derived scores only |
| **Samsung** | **Yes, 25 Hz** | **Yes, green, IR and red: 25 Hz continuous, 100 Hz on demand** | **Yes, raw, 500 Hz on demand** (one on-demand tracker at a time, about 30 s) | **Yes, HR with IBI at 1 Hz** | **Yes, 1 Hz, Galaxy Watch8 and later** | Health Sensor SDK (partner registration to distribute); also via Verily Pre / Viewpoint Evidence (C) |
| **Polar H10** | **Yes, 25 / 50 / 100 / 200 Hz, ±2 / 4 / 8 g** | n/a | **Yes, 130 Hz in µV** (streaming only; internal memory logs HR only) | **Yes, RR in ms with HR at 1 Hz** | n/a | **Open BLE SDK, no registration**; AccessLink returns exercise RR when an H10 was used |
| **Polar Verity Sense** | **Yes, 52 Hz; SDK mode 26–416 Hz, ±2–16 g** | **Yes, SDK mode 28–176 Hz, 22-bit** | No | Yes (PPI), but not in SDK mode | n/a | Open BLE SDK |
| **Polar 360 / Loop** | Yes, 12–400 Hz online, 1–50 Hz offline | **Yes, 22 / 50 / 100 Hz online and offline, 24-bit, green** | No | PP interval and 24/7 PPI samples | n/a | Open BLE SDK; 15 MB storage shared with activity and sleep |
| **Movesense** | **Yes, 9-axis IMU 13 Hz to 1.6 kHz (C)** | n/a | **Yes, single lead, 125–512 Hz (C)** | **Yes, R-R at 1 ms resolution** | n/a | BLE or onboard logging (Flash, 128 MB); custom firmware; no licence fee, proprietary evaluation licence |
| **Withings** | Yes, ScanWatch, about 24.824 Hz in raw mode, ±4 g (overview page says "25 Hz by default (up to 100 Hz)"; no documented setting reaches 100 Hz) | Yes, green, red and IR, about 24.824 Hz | Not in the Raw Data API | Not documented | n/a | **Advanced Research API, contracted partners only**; raw mode disables all other watch features; battery falls to 3–4 days |
| **Ultrahuman** | Accelerometer "data stream" | PPG "data stream"; **raw format and rates undocumented** | n/a | Derived HRV via the Partner API | n/a | UltraSignal application with a loaned developer kit |
| **Biostrap / Sensor Bio** | Raw and/or processed, with gyroscope (vendor statement, C) | Raw PPG (vendor statement, C) | n/a | IBI (vendor statement, C) | n/a | RPM dashboard or custom pipelines; configurable sampling rates, no Hz figures published |
| **Empatica** | **Yes; Actigraphy Pro 64 Hz, Actigraphy Optimized 32 Hz, Gyroscope 100 mode 100 Hz (6-axis)** | Raw sensor data included in the academic plan; **per-mode PPG rate not published** | No | Unclear (pulse rate variability biomarker provided) | **Yes; rate not published** (the legacy E4's 4 Hz must not be assumed) | CSV download and S3 access keys; **no real-time streaming** |
| **Verily Study Watch** | Yes, inertial (C) | Unclear | Yes (C) | Unclear | **Yes (C)** | Verily Pre / Viewpoint Evidence, enterprise only |
| **Ametris** | **Yes; Insight Watch and LEAP 32–256 Hz, ±8 g; wGT3X-BT 30–100 Hz, ±8 g** | **LEAP: green 25 Hz and 100 Hz, red/IR 50 Hz**, "only available for certain devices, firmware versions, and study configuration, and ... subject to contract restrictions" | No | Not documented | n/a | CentrePoint API Data Access Files (CSV or AVRO); ActiLife `.gt3x` |
| **Axivity / GENEActiv** | **Yes; AX3 12.5–3,200 Hz, AX6 12.5–1,600 Hz, ±2–16 g, configurable** (UK Biobank used 100 Hz, ±8 g); GENEActiv raw, rate not in the profile | n/a | n/a | n/a | n/a | **USB, raw file, no vendor** |

### Sampling-rate reference, by signal

Rates are the maxima the profiles document. Cost of entry is the cheapest documented way to get that
rate; a blank price means the profile gives none.

| Signal | Device | Maximum documented rate | Cost of entry |
|---|---|---|---|
| ECG | Movesense | 512 Hz (C) | MD €349 ex VAT (1–49 units); no licence fee |
| ECG | Samsung Galaxy Watch | 500 Hz, on demand | Consumer watch; partner registration to distribute |
| ECG | Polar H10 | 130 Hz | **$104.95** (Polar US store, 2026-10-10); open SDK, no approval |
| Accelerometer | **Axivity AX3** | **3,200 Hz** | **£139 ex VAT**; no software cost |
| Accelerometer (IMU) | Movesense | 1.6 kHz, 9-axis (C) | €349 ex VAT |
| Accelerometer (with gyro) | Axivity AX6 | 1,600 Hz | £199 ex VAT |
| Accelerometer | Polar Verity Sense (SDK mode) | 416 Hz | ~$95 (2026-08-21 figure, not re-read) |
| Accelerometer | Polar 360 | 400 Hz online | Price not in profile |
| Accelerometer | Ametris Insight Watch / LEAP | 256 Hz | Quote only |
| Accelerometer | Polar H10 | 200 Hz | $104.95 |
| Accelerometer | Empatica EmbracePlus | 100 Hz (Gyroscope 100 mode); 64 Hz (Actigraphy Pro) | $1,749.60 academic 3-year bundle |
| Accelerometer | Samsung | 25 Hz | Partner registration |
| Accelerometer | Withings ScanWatch | ~24.8 Hz | Contract |
| Raw PPG | **Polar Verity Sense (SDK mode)** | **176 Hz, 22-bit** | ~$95 (not re-read) |
| Raw PPG | Samsung (green, IR, red) | 100 Hz on demand; 25 Hz continuous | Partner registration |
| Raw PPG | Polar 360 | 100 Hz, 24-bit | Price not in profile |
| Raw PPG | Ametris LEAP (green) | 100 Hz; subject to contract restrictions | Quote only |
| Raw PPG | Withings ScanWatch | ~24.8 Hz | Contract |
| Raw PPG | Empatica, Apple SensorKit, Ultrahuman | Not published | As above |
| EDA | Samsung Galaxy Watch8 | 1 Hz | Partner registration |
| EDA | Empatica | Not published | $1,749.60 academic 3-year bundle |
| EDA | Verily Study Watch | Not published | Enterprise only |

**Reading.** The highest documented raw rates in the module come from open sensors sold at modest
prices (Axivity AX3 accelerometry to 3,200 Hz, Movesense ECG to 512 Hz and IMU to 1.6 kHz, Polar
Verity Sense PPG to 176 Hz), not from the clinical-trial vendors. Samsung is the consumer exception
(ECG 500 Hz, PPG 100 Hz on demand). What the open sensors give up is form factor, wear duration,
derived metrics and study infrastructure.

---

## Table 4, API characteristics

| Ecosystem | Auth | Rate limit | Push / webhooks | Historical backfill | Latency driver |
|---|---|---|---|---|---|
| Apple | On-device permission | n/a | HealthKit background delivery | Full on-device history the participant authorises | iOS background execution limits |
| Fitbit Web API (legacy) | Fitbit OAuth 2.0 | 150 req/hr per consented user | Subscription API | Moot | **Unsupported since 30 Sep 2026; turned off 30 Oct 2026** |
| Google Health API | Google OAuth 2.0 | **300 req/min per user; 120,000 req/min and 86.4M req/day per project; unverified apps 250 QPS across at most 100 users** | `projects.subscribers` subscriptions | Backfill tools after re-consent; depth Unclear | Participant app sync; **not onboarding new projects** |
| Garmin Health API | Garmin OAuth consent | Not published | Push or ping/pull | Backfill tooling exists; 30 days before consent per one integrator (R) | Device to Garmin Connect sync; latency not published |
| Oura | **OAuth 2.0 only** (PATs no longer available) | Two layers, per token and per application; **numbers not published** (`X-RateLimit-*` headers). The 5,000 req / 5 min figure comes from a secondary source only | **Webhooks recommended**, about 30 s after app sync, 10 retries | One historical request on first connect; depth Unclear | **Sleep data reach the API only after the user opens the Oura app** |
| WHOOP | OAuth 2.0 | **100 req/min and 10,000 req/day per client**; increases on request | Yes (v2; v1 removed) | Not established | Device to cloud sync |
| Samsung | On-device SDK | n/a | n/a | From enrolment onward | Researcher's own pipeline |
| Polar BLE SDK | None | **None** | n/a | Device onboard memory | Bluetooth range |
| Polar AccessLink | OAuth 2.0 | 500 + 20 × users per 15 min; 5,000 + 100 × users per 24 h | Webhooks | **None before the user registers with the client**; exercises from the last 30 days only; activity 28-day default, no older than 365 days | Polar Flow sync |
| Withings | OAuth 2.0 | Enterprise and Advanced Biomarkers "1,500+ requests/minute"; Start for Free "Standard"; throttled calls return status 601 | Notification mechanism referenced, not verified | Not documented; sync by `lastupdate` | Cellular or app sync |
| Empatica | Portal login; S3 access keys | n/a | **No real-time streaming** | Full study history in Empatica Cloud | Batch upload |
| Ametris CentrePoint | OAuth 2.0 client credentials (tokens 3,600 s), enabled by Ametris | More than 500 req/min from one IP returns 429; 10 concurrent raw requests | Webhooks, including raw-processing-complete | Historical raw-file generation may carry fees | Cellular gateway or app |
| Ultrahuman Partner API | OAuth 2.0 for approved apps; tokens last about a week | Not published | Unclear | Unclear | Unclear |
| Axivity / GENEActiv | n/a | n/a | n/a | n/a | **Device return** |

---

## Table 5, Study operations and management

| Ecosystem | Researcher portal | Participant roster | Adherence / wear-time monitoring | Multi-site | Surveys / EMA | Device reuse |
|---|---|---|---|---|---|---|
| Apple | No (Apple Research app is Apple's own, not procurable) | No | No | No | Build with ResearchKit | n/a (BYOD) |
| Fitbit / Google | No; via Fitabase (quote) or Fitrockr | Via platform | Via Fitabase (sync and battery status) | Via platform | Fitabase Engage apps "Preview · Summer 2026" | Via platform |
| Garmin | No; via Labfront, Fitabase or Fitrockr | Via platform | Via platform | Via platform | Labfront (all tiers); Fitrockr (paid add-on) | Via platform |
| Oura | **Oura for Organizations research dashboards** (vendor page; price not published) | Group and access-level management (vendor) | Adoption, attrition and engagement tracking (vendor) | Unclear | Tags only | Requires re-sizing |
| WHOOP | None in the public platform; WHOOP Unite is enterprise, terms not public | No | No | No | **Journal not exportable** (no Journal scope in the API) | Membership-bound |
| Samsung | Research Stack portal, self-hosted, **no code updates since Oct 2024** | Yes | Unclear | Unclear | Yes (Research Stack) | Unclear |
| Polar | No (Team Pro is team-sport) | No | No | No | No | Yes |
| Withings | Withings Health Solutions services model | Via partner or RPM platform | Via partner | Via Health Solutions | Via DCT partner; Advanced Biomarkers plan lists questionnaires | Yes |
| **Empatica** | **Care Portal** (Care Lab on the academic plan) | Yes, unlimited credentials; **academic account limited to 1 study, 1 site, 1,000 participants** | **Yes, live wear-time** | Yes (Enterprise); 1 site on the academic plan | None (event marking only) | **Yes, multiple participants per device** |
| **Ametris** | **CentrePoint** | Yes | **Yes, near-real-time and monthly reports** | **Yes, 70+ countries** | Signant eCOA integration is the stated direction; current availability not established | Yes, automated device assignment |
| Axivity / GENEActiv | **No** | No | **Impossible during wear** | No | No | Yes |
| Movesense | No; via Labfront (HR2) | Via Labfront | Via Labfront | Via Labfront | Via Labfront | Yes |
| Biostrap / Sensor Bio | Participant management dashboard (vendor) | Enrolment workflows (vendor) | Compliance notifications (vendor) | Unclear | Integrated surveys (vendor) | Unclear |

---

## Table 6, Participant experience and operational burden

| Ecosystem | Form factor | Battery | Charging conflict with sleep? | Phone required? | BYOD viable? |
|---|---|---|---|---|---|
| Apple | Watch | About a day (non-Ultra) | **Yes, significant** | Yes (iPhone) | **Yes**, iPhone owners only |
| Fitbit | Band / watch | Several days to a week or more (trackers); Fitbit Air up to 7 days (C) | Minor | Yes (Google Health app, iOS or Android) | Yes |
| Garmin | Watch | **One to three weeks**, some solar models longer | **No** | Yes (Garmin Connect) | Yes |
| Oura | **Ring** | About 4–7 days; 20–80 min charge | Minor | **Yes; sleep reaches the API only after the app is opened** | Partly (sizing kit; membership required) |
| WHOOP | Screenless band or apparel | Not stated in the profile; **charged on the wrist with a slide-on pack** | **No wear interruption** | Yes | Partly (membership) |
| Samsung | Watch / ring | About 1–2 days; **continuous raw capture reduces this substantially** (not measured by Samsung) | Yes | Yes (Android; Galaxy Watch4 or later) | Galaxy owners only |
| Polar H10 | Chest strap | Session wear | n/a | ECG and accelerometry need a phone; internal memory logs HR only | No |
| Polar Verity Sense | Armband | Session wear | n/a | No (offline recording) | No |
| Movesense | Chest-worn sensor | Unclear (datasheets gated) | n/a | Flash logs phone-free (128 MB) | No |
| Withings | Hybrid watch, scale, BP cuff, **under-mattress sleep mat** | ScanWatch about 30 days (3–4 days in raw mode) | No | **No for cellular devices** | Partly |
| Empatica | Wristband | Up to 14 days in Actigraphy Optimized mode (32 Hz); other modes not documented | No | Care / Care Lab app used; phone requirement not stated in the profile | No |
| Ametris | Research watch / puck | Insight Watch 30 days at 32 Hz; wGT3X-BT 25 days; LEAP 30 or 32 days (conflicting spec blocks, Unclear) | No | **No, cellular gateway option** | No |
| Axivity / GENEActiv | Sealed puck | AX3 14 days at 100 Hz, 30 days at 12.5 Hz (vendor); AX6 7+ days at 100 Hz with gyro; GENEActiv "up to 2 months"; **no charging during wear** | **No** | **No** | No |

---

## Table 7, Cost structure

| Ecosystem | Device cost | Recurring per participant | API / platform fee | Pricing public? |
|---|---|---|---|---|
| Apple | Consumer retail | **None** | No API fee; Apple Developer Program annual fee | Devices yes; the main cost is app engineering |
| Fitbit / Google | Fitbit Air $99.99 (C); trackers among the cheapest research-viable wearables | Premium generally not required; $99.99/yr (R) | No documented API fee; CASA assessment $500–$4,500 if verification is needed; Fitabase by quote | Partly |
| Garmin | Wide retail range (no figure in profile) | **None** | Programme free, business use only; **Enhanced BBI: licence fee for commercial use**; SDK: evaluation free, commercial licence fee or device MOQ; a $5,000 admin fee is Reported and unconfirmed | Devices only |
| Oura | Ring 5 $399–$499 (C, launch press) | **$5.99/month or $69.99/year (US), mandatory for API data on Gen3 and later** | API free; research offering price not published | Ring and membership yes; research offering no |
| WHOOP | Included in membership | ONE ~$199, PEAK ~$239, LIFE ~$359 per year (R, secondary sources; whoop.com not readable) | API "currently provided at no charge" | Reported only |
| Samsung | Consumer retail | **None** | No SDK fee documented; Research Stack open source (engineering and hosting cost) | Devices only |
| **Polar** | **H10 $104.95** (US store, 2026-10-10); Verity Sense ~$95 (2026-08-21, not re-read) | **None** | **Free, open SDK**; AccessLink no fee | **Yes** |
| **Movesense** | **MD €349 ex VAT (1–49 units), €344 (50–99)**; free sensors for selected Academic Program projects | **None** | No licence cost | **Yes** (MD) |
| **Labfront** (Garmin, Movesense, Dexcom) | n/a | **Tester free (5 participants, 30-day window); Basic $500/yr (20 + $10 each); Advanced $1,250/yr (20 + $25 each)** | Analytics packages from $3,000 + $50 per participant | **Yes** |
| **Fitrockr** (many brands) | n/a | **Basic from €50/$55 per month; Pro from €150/$165 per month**; 5 device licences included, extra €1–€15 per device per month; 3-month minimum | Raw accelerometer and gyroscope +25%; API +20% | **Yes** |
| Withings | Consumer retail (no figure in profile) | **From 12 Oct 2026: Withings+ per participant** with a new account on the free plan (price not read); none on paid plans | Start for Free; Enterprise and Advanced Biomarkers custom; raw-data contract non-public | Plan structure yes; prices no |
| Empatica | **EmbracePlus $1,166.40; EmbraceMini $641.52** | Included in bundle | **3-year bundle: EmbracePlus $2,332.80 list / $1,749.60 academic; EmbraceMini $1,516.32 / $1,137.24. 5-year: EmbracePlus $2,916 / $2,187; EmbraceMini $1,953.72 / $1,465.29**; Enterprise quote | **Yes, academic plan** |
| Ametris | Not published ("calculated for each unique order"); GT3X+ / wGT3X-BT $325–1,016 (R, competitor source) | Non-public | ActiLife conflicting: ~$1,695 (R, competitor source, dated) or US$349 (Ngueleu 2022); CentrePoint ~$3,500/yr (R, competitor source, dated); academic pricing list on request | **No** |
| Axivity / GENEActiv | **AX3 £139 (£149 with band); AX6 £199 (£209 with band), ex VAT**; GENEActiv by quote | **None** | **None, open toolchain** | **Axivity yes; GENEActiv no** |
| Ultrahuman, Biostrap / Sensor Bio, Verily | Not disclosed | Not disclosed | Not disclosed | No |

---

## Table 8, Privacy, security and compliance posture

Every vendor compliance statement here is the vendor's own unless a certificate was checked, which
none was. Every "Unclear" is a vendor question, not an inference; see
`../shared/unresolved-questions.md`.

| Ecosystem | HIPAA / BAA | GDPR / DPA | SOC 2 / ISO | Regulatory clearance (FDA 510(k) unless stated) | Self-hosting / data custody |
|---|---|---|---|---|---|
| Apple | **N/A for HealthKit and SensorKit: Apple is not in the data path** | Researcher's obligation | n/a | Hypertension notifications K250507 (2025-09-11); other features not itemised in the profile | **Full; researcher holds all data** |
| Fitbit / Google | **No BAA published; PHI only with Google's prior written consent** | Health Research Policy: IRB approval or waiver, participant disclosure of retention and deletion, immediate de-identification; residency not established | Unclear | Not itemised in the profile | No |
| Garmin | Standard SDK "HIPAA-compliant" (vendor statement, C); no BAA mentioned | Unclear | Unclear | Not itemised in the profile | **Standard SDK keeps data out of Garmin Connect** |
| Oura | Trust centre: HIPAA "where we handle protected health information for a healthcare partner"; research page "processes PHI in accordance with HIPAA" (C); no BAA published | Research page says GDPR-compliant (C); API Agreement: retention only as strictly necessary, 72-hour deletion | HITRUST; annual independent audit under a SOC 2 heading (C); ISO 27001 not stated | None documented in the profile | No |
| WHOOP | **No HIPAA obligations unless agreed in writing; PHI only with prior written consent** | Unclear | Unclear | **ECG feature cleared, K243236 (2025-04-04). Blood Pressure Insights not cleared**: warning letter 14 Jul 2025; close-out 17 Jun 2026 says FDA does not intend to enforce for BPI as modified (general wellness) | No; **terms bar permanent copies and AI/ML training on WHOOP data** unless authorised by the data owner or by law |
| Samsung | Partner agreement has no HIPAA, BAA or DPA language; no Samsung server in the Sensor SDK path | Researcher's obligation for the study copy | Unclear | Not itemised in the profile | **Yes, on-device SDK; Research Stack self-hosted** |
| Polar | No HIPAA or BAA language (privacy notice) | Polar is controller for Flow and not responsible after transfer out; processor agreements only for Team Pro and GoFit | Not checked | None documented | **Yes, BLE path has no processor** |
| Withings | "HIPAA compliant" EU and US clouds (vendor, C); **BAA and DPA on Enterprise and Advanced Biomarkers only** | EU Medical Cloud "GDPR compliant" (C) | ISO 27001:2017 and HDS stated (C); no SOC 2 found | BP monitors K110872, K133125; Thermo K160544; Scan Monitor K201456, K230812; Sleep Rx K231667; ECG App K240795; BeamO K252474 | No self-hosting; **choice of EU (France) or US medical cloud** |
| Empatica | "HIPAA-compliant cloud infrastructure located in US, Virginia" (C); no BAA found | **Published DPA**; retention for the service plus 10 years | ISO/IEC 27001:2022, ISO 13485:2016, MDSAP, CE (C, certificates not opened); no SOC 2 found | **K221282, K230457, K242737, K260374, K252981; seizure products incl. K250515** | No |
| Ametris | No BAA or HIPAA statement found | **DPA with SCCs; EU-U.S. Data Privacy Framework** | ISO 13485:2016 with MDSAP; ISO/IEC 27001:2022 listed without a certificate (C); no SOC 2 found; Part 11 not stated in words | **K231532 (LEAP), K181077 (Insight Watch)** | CentrePoint cloud (Azure, AWS); ActiLife local |
| Axivity / GENEActiv | **N/A, no processor exists** | **Trivial, no processor** | n/a | GENEActiv moving from MDD Class I to EU MDR | **Full** |
| Movesense | **N/A, no processor in the BLE path** | Trivial | n/a | **MD: Class IIa, EU MDR 2017/745**; FDA status Unclear | **Full** |

---

## Table 9, Evidence and validation summary

Full extraction: `validation-evidence.md`. Robbins 2024 and Schyvens 2025 are the two largest PSG
comparisons of current-class devices, not the only ones: Miller 2022 and Grandner 2023 tested Oura
Gen2/V2 and WHOOP 3.0 under one protocol, and Lee 2023 and Searles 2026 add further Oura, Samsung,
Apple and Fitbit results (`validation-evidence.md` §3c).

### Sleep staging vs PSG

| Device | Robbins 2024 (N=35, healthy, **Oura-funded**) four-stage κ | Schyvens 2025 (N=62, independent) overall κ | Other PSG results |
|---|---|---|---|
| Oura | Gen3 **0.65** | not tested | Miller 2022 Gen2 four-stage κ 0.43 (WHOOP-supported lab); Lee 2023 Ring 3 κ 0.35 (authors from a competing app maker) |
| Apple Watch S8 | 0.60 | **0.53** (first of six) | Lee 2023 Apple Watch 8 κ 0.30 |
| Fitbit Sense / Sense 2 | 0.55 | 0.42 | Lee 2023 Sense 2 κ 0.42 |
| Fitbit Charge 5 | not tested | 0.41 | |
| WHOOP | not tested | 4.0: **0.37** | Miller 2022 WHOOP 3.0 four-stage κ 0.44 (tied with Oura) |
| Samsung | not tested | not tested | Lee 2023 Galaxy Watch 5 κ 0.42 |
| Withings ScanWatch | not tested | **0.22** (three-state output) | |
| Garmin Vivosmart 4 | not tested | **0.21** | |

### The findings that matter more than the ranking

| Finding | Detail |
|---|---|
| **Deep sleep and REM are unreliable on every device** | Robbins ICCs, deep sleep: Oura **0.32**, Fitbit 0.36, Apple **0.13**; REM: Oura **0.27**, Fitbit **0.13**, Apple 0.37. All poor. Stage-minute outcomes are largely device noise |
| **TST and SE are the defensible endpoints** | Robbins ICC 0.56–0.85 (Oura 0.74, Fitbit 0.56, Apple 0.85) |
| **Every device underestimates WASO** | Schyvens: −12 to −48 min. Fragmentation endpoints are systematically flattered |
| **High sensitivity, poor specificity** | Schyvens sleep detection 92–96%; specificity 29–52%; per-stage wake accuracy 27.6–52.2% |
| **Data loss is a real design risk** | Schyvens: Garmin failed **18/43** nights, Apple **15/35**, Withings **0/41**, in a supervised lab. Robbins: Oura 0/35, Fitbit 2/35, Apple 6/35. Oura was not in Schyvens |
| **Robbins 2024 has a declared conflict** | Funded by Oura; lead author on Oura's Medical Advisory Board and a paid consultant. Never cite κ=0.65 without it |
| **Resting HR and HRV: Oura ahead of WHOOP, directly measured** | Dial 2025 (AFRL-funded, no competing interests, **Verified**): 13 adults, 536 nights, Polar H10 reference. Resting HR CCC: Oura Gen4 0.98, Gen3 0.97, WHOOP 4.0 0.91, Polar Grit X Pro 0.86. HRV CCC: Oura Gen4 0.99, Gen3 0.97, WHOOP 0.94, Garmin Fenix 6 0.87, Polar 0.82. PSG sleep-stage comparison on current hardware is still missing |
| **No consumer brand is acceptable for energy expenditure** | Unchanged across six years of reviews |
| **Current hardware is largely untested** | Oura Ring 5, WHOOP 5.0/MG, Apple Series 11 and Fitbit Air postdate every PSG study here; Oura Gen4 has independent data only for resting HR and HRV |

### Non-sleep evidence positions

| Ecosystem | Strongest evidence asset, with its caveat |
|---|---|
| Apple | **Apple Heart Study** (419,297 participants), **itself Apple-sponsored**. Outside cardiac rhythm the independent record is mixed: VO2max MAPE 13.31%, HRV fails equivalence (MAPE 28.88%), wheelchair fall detection 4.7% sensitivity. Irregular-rhythm notification sensitivity 21.4–72% across studies, ECG app 94.8% pooled. Hypertension notifications: vendor validation only, sensitivity 41.2% |
| Fitbit / Google | Most-studied brand in the validation literature; HR tends to be underestimated; ***All of Us*** dataset, 59,000+ participants, minute-level, 46% linked to EHR and other data |
| Garmin | Enhanced BBI vs ECG: mean error 0.506 ms, SD 8.55 ms, r=0.975, but **N=1, one night, manufacturer-published**; Schyvens κ 0.21; Dial HRV CCC 0.87 |
| Oura | Robbins 2024 (Oura-funded) and Dial 2025 (independent, best resting HR and HRV of the devices tested). Independent PSG results are mixed (Miller 2022, Lee 2023); Searles 2026 found Gen3 underestimated TST by 75.5 min in older adults. 72% of 107 smart-ring studies in one review used Oura; 65% of the 107 had moderate-to-high risk of bias. SpO2 and temperature have no independent validation |
| WHOOP | Schyvens 2025 (independent): best deep-sleep accuracy (69.6%), fourth of six on κ (0.37). Dial 2025: behind Oura on resting HR and HRV. Berryhill 2020 is WHOOP-funded; Miller 2022 came from a WHOOP-supported lab. No WHOOP 5.0/MG validation located |
| Samsung | Lee 2023 Galaxy Watch 5 κ 0.42 (joint best wearable; competing-app authors); Byun 2023 (independent, OSA patients); Alavi 2026 sleep apnoea AUROC 0.94 (Samsung-funded); Browne 2024 SpO2 RMSE 2.54% (Samsung grant); Walzel 2023 met ISO SpO2 limit. Antioxidant Index and Vascular Load unvalidated |
| Polar | H10 is used as the criterion device in others' validations; watch-line metrics not in the major PSG comparisons |
| Withings | Cleared BP, thermometer, Sleep Rx and ECG devices; ScanWatch sleep staging poor (Schyvens κ 0.22, largest TST, SE and WASO biases) but zero data loss |
| Empatica | **FDA clearances listed in Table 8.** Wrist EDA agrees poorly with palmar or finger EDA in E4 studies (Hu 2024 ICC 0.09 for SCL); no EmbracePlus validation against a palmar reference |
| Movesense | **Independent lab validations exist**: Rogers 2022 vs 12-lead ECG (r=0.98–1.0 for RR and HRV), Martín Gómez 2024 R-peak sensitivity 99.7%, both N=21 with sensors supplied by Movesense; IMU step timing vs force plate (N=14). MD is Class IIa MDR |
| Verily | FDA 510(k)s including on-demand ECG and irregular pulse (C) |
| Ametris | **The actigraphy reference standard** for raw accelerometry and its pipelines; current Insight Watch and LEAP not shown equivalent to the legacy devices |
| Axivity / GENEActiv | **UK Biobank AX3, 100,000+ participants**; AX3 equivalent to GENEActiv on shaking tests; open reproducible toolchain |

---

## Table 10, Differentiators and key limitations

| Ecosystem | What it does that matters | Key limitation |
|---|---|---|
| **Apple** | No vendor in the data path, full on-device history at enrolment, and SensorKit behavioural signals plus PPG, ECG and accelerometer samples for approved studies | iPhone only; no server API or study tooling; SensorKit needs per-study Apple approval |
| **Fitbit / Google** | Deepest validation literature, devices among the cheapest, and an existing 59,000-participant *All of Us* dataset | **Legacy API off 30 Oct 2026; no new Google Health API projects as of 2026-10-10** |
| **Garmin** | Weeks of battery, no subscription, and Enhanced BBI with per-beat confidence | **New direct access paused (C)**; raw accelerometry only via the enterprise Health SDK; opaque licence terms |
| **Oura** | Nightly RMSSD and temperature deviation from a ring people keep on overnight; best resting HR and HRV agreement in Dial 2025; a research offering with dashboards | Mandatory membership; derived data only; **API Agreement limits retention and bars AI training** |
| **WHOOP** | Charged on the wrist, so no charging gap; screenless | Derived scores only; **terms bar permanent copies and AI/ML training**; 10-member Sandbox to start |
| **Samsung** | Raw PPG (green, IR, red), raw ECG at 500 Hz, IBI and **raw EDA at 1 Hz (Watch8)** from a mainstream watch, with no Samsung server in the path | Galaxy and Android only; partner registration to distribute; Research Stack unmaintained since Oct 2024 |
| **Polar** | Raw ECG and accelerometry from a $104.95 H10, and 22-bit PPG from Verity Sense, over an open SDK with no cloud, approval or fee | Session devices, not 24/7 wear; no study tooling |
| **Withings** | Cellular devices that remove the participant's phone from the data path; blood pressure, body composition and an under-mattress sleep mat | Raw data ScanWatch-only and by contract; worst Schyvens sleep biases; **Withings+ from 12 Oct 2026** |
| **Empatica** | Raw wrist EDA with an FDA-cleared EDA parameter, and a published-price, self-serve academic plan with study management | Per-mode PPG and EDA rates unpublished; no real-time streaming; academic account limited to 1 study and 1 site |
| **Ametris** | The actigraphy reference standard, raw data reprocessable later, regulated-trial operations in 70+ countries | Non-public pricing; corporate transition under Signant |
| **Axivity / GENEActiv** | Open firmware, software and hardware (Axivity), no vendor in the data path, and direct comparability with UK Biobank; AX3 up to 3,200 Hz | Movement only; nothing known until the device is returned |
| **Movesense** | Custom sensor firmware with no licence cost, 512 Hz ECG and 1.6 kHz IMU (C), Class IIa MDR on the MD | Proprietary 12-month evaluation licence; small validation base; session wear |
| **Ultrahuman** | The only published ring route to a PPG data stream found (UltraSignal), and ring plus CGM in one API (R) | Raw format and rates undocumented; selection-based loaner kits; no validation located |
| **Biostrap / Sensor Bio** | Raw PPG, configurable sampling, surveys and a participant dashboard in one product, plus a leg-worn Activity Pod (vendor statements) | Rebranded; no Hz figures or prices; validation counts vendor-compiled |
| **Verily Study Watch** | ECG, EDA and inertial data in one FDA-cleared research device with weeks of onboard raw storage (C) | Enterprise only; **current status Unclear** |
| **Labfront** | Published pricing (one of several intermediaries that publish), a free 5-participant tier, EMA at every tier, and higher Garmin resolution via the Health SDK | Garmin, Movesense and Dexcom only; no Fitbit |
| **Fitrockr** | Published per-device pricing across many brands, with Garmin research grants | Vendor compliance claims only; surveys and raw data are paid add-ons |

---

## Table 11, Study-operations platforms (the layer most vendors do not provide)

| | **Labfront** | **Fitabase** | **Fitrockr** | **Empatica Care Portal** | **Ametris CentrePoint** | **Samsung Research Stack** |
|---|---|---|---|---|---|---|
| Devices | Garmin, Movesense HR2, Dexcom G7 | **Fitbit**, Garmin | Claims 700+ wearables incl. Garmin, Fitbit, Apple, Oura, WHOOP, Samsung, Withings, Polar (R) | EmbracePlus, EmbraceMini | LEAP, Insight Watch | Galaxy Watch (Watch5 tested) |
| **Pricing public?** | **Yes** | No | **Yes** | **Yes (academic)** | No | Free, open source |
| Cost | Free (5 participants) / $500 (20) / $1,250 (20, all integrations) per year, + $10–25 per extra participant | Custom quote | From €50/$55 or €150/$165 per month, per device licence | $1,749.60 per EmbracePlus, 3 years, academic | Not published; CentrePoint ~$3,500/yr (R, competitor source) | $0 plus hosting |
| **EMA / surveys** | **Yes, all tiers** | Engage apps in preview, Summer 2026 | Paid add-on (+20%) | None | Signant eCOA direction; not established | **Yes** |
| Adherence monitoring | Yes | Yes (sync and battery) | Yes (R) | **Yes, live wear-time** | **Yes, near-real-time** | Unclear |
| Multi-site | Yes | Yes | Unclear | Enterprise yes; academic 1 site | **Yes, 70+ countries** | Unclear |
| Sampling resolution | **Raised via Garmin Health SDK partnership**; Advanced tier customisable | Enhanced BBI via Garmin OAuth, during sleep | Raw accelerometer 25 Hz, gyroscope 32 Hz (add-on) | Fixed sensor modes | 32–256 Hz | Full SDK control |
| Self-hosting | No | No | On-premise add-on | No | ActiLife local (legacy) | **Yes** |
| Free tier to pilot | **Yes** | No | 2-week trial | No | No | **Yes** |
| Maintenance | Active | Active | Active | Active | Active | **No code updates since 24 Oct 2024** |

**Practical read.** A Fitbit study starting now cannot open its own Google Health API project, so it
needs an intermediary that already holds access (Fitabase, or Fitrockr, which also lists Google and
Fitbit). A Garmin study cannot currently apply to Garmin directly (C); Labfront and Fitrockr publish
prices, Labfront includes EMA and a free five-participant pilot.

---

## Table 12, Choosing by research question

| If your primary endpoint is... | Use | Avoid | Why |
|---|---|---|---|
| **Physical activity / sedentary behaviour** | Axivity, GENEActiv, Ametris | Any device where energy expenditure is the metric | Raw accelerometry, open pipelines, cohort comparability |
| **Sleep timing / duration (not stages)** | Oura, Apple Watch, Fitbit, research actigraphy | Withings ScanWatch, Garmin Vivosmart 4 for TST | Robbins TST ICC 0.74 (Oura) and 0.85 (Apple); Fitbit TST bias not significant in Schyvens; Schyvens TST bias largest for ScanWatch (+39.9 min) and Vivosmart 4 (+38.4 min) |
| **Sleep architecture (stages)** | Reconsider the design; PSG or ambulatory EEG | **All consumer wearables** | Deep and REM ICC 0.13–0.36 on the best-studied devices |
| **Sleep fragmentation / WASO** | Reconsider; PSG | **All consumer wearables** | Every Schyvens device underestimated WASO by 12–48 min |
| **HRV, nocturnal** | Polar H10, Movesense, Garmin Enhanced BBI (via Labfront or Fitabase), Oura nightly RMSSD | Devices reporting only an opaque HRV score | Beat-level data or true ECG RR; Oura HRV CCC 0.97–0.99 in Dial 2025 |
| **HRV, daytime / during stressors** | Polar H10, Movesense, Samsung IBI, Garmin Health SDK | Garmin Enhanced BBI via the Health API or Fitabase (captured during sleep) | The SDK lists Enhanced BBI for real-time streaming; the API route is sleep-based |
| **Cardiac rhythm / AFib** | Apple Watch ECG, Withings ECG App, Movesense MD, Samsung raw ECG, Verily | Treating irregular-rhythm notifications as the ECG app | Cleared ECG features or raw ECG; notification sensitivity 21.4–72% vs ECG app 94.8% pooled (Apple) |
| **Electrodermal / arousal / stress** | **Empatica**, **Samsung Galaxy Watch8 (1 Hz)**, Verily Study Watch | Everything else | The only raw EDA routes found; wrist EDA agrees poorly with palmar EDA |
| **Energy expenditure** | Indirect calorimetry, doubly labelled water | **Every consumer wearable** | No brand within acceptable limits, six years running |
| **Custom algorithm development** | Movesense, Polar, Samsung, Axivity, Ametris | Oura, WHOOP, Fitbit | Requires documented raw signal (Biostrap and Ultrahuman claims are unproven) |
| **Data retention, deposit or ML training** | Polar BLE, Movesense, Axivity, Samsung Sensor SDK, Apple HealthKit (no vendor in the path) | **WHOOP and Oura APIs** without written agreement | Their API terms limit retention and bar AI/ML training |
| **Large N with no budget** | ***All of Us*** or **UK Biobank** secondary analysis | | Data already collected; no procurement, no API, no exposure to the Fitbit shutoff |
| **Regulated trial endpoint** | Ametris, Empatica, Withings cleared devices | Consumer platforms | Cleared devices and established trial operations |
| **Behaviour-change intervention** | Any consumer device; unified APIs acceptable | | The device is a tool, not an instrument; brand confounding is tolerable |
| **Minimal reactivity** | WHOOP, Oura, Fitbit Air, Ametris, Axivity | Feedback-rich smartwatches | Screenless devices show the participant nothing |
| **Fitbit study starting now** | An intermediary already holding Google Health API access; *All of Us* | A new direct Google Health API project | Google is not onboarding new projects; legacy API off 30 Oct 2026 |

---

## Table 13, Research programs and academic data access (added 2026-10-10)

| Ecosystem | Program or route | What academics get | User caps | Retention and AI-training terms | Cost | Status (2026-10-10) |
|---|---|---|---|---|---|---|
| **Apple** | **SensorKit** (Apple's only research-specific programme); HealthKit; ResearchKit and CareKit are toolkits; Apple Research app runs Apple's own studies only | SensorKit: behavioural sensors, raw accelerometer, PPG and ECG samples (iOS 17.4+), on-device, uploaded by the study app. HealthKit: derived samples with full authorised history | None from Apple | No Apple cloud copy or Apple retention term | Apple Developer Program fee | Active; ResearchKit pushed 2026-09-23 |
| **Fitbit / Google** | No academic tier. Google Health API with the **Health Research Policy** and **Research Pledge** (both effective 24 Mar 2026); Health Research Attestation | Same data types as commercial developers; no research-only data | 100 users until verification (CASA assessment, $500–$4,500) | Participants must be told the retention period and how to delete; immediate de-identification; no third-party sharing for new studies without consent; PHI only under an IRB-reviewed HIPAA authorisation. AI-training terms not covered in the profile | No documented API fee | **Not onboarding new projects. Legacy Fitbit Web API turned off 30 Oct 2026** |
| **Garmin** | No academic programme; Connect Developer Program is "only for business use"; Health SDK for enterprise partners; grants only through partners | Health API summaries, Enhanced BBI, second-level HR during activities; SDK accelerometer and BBI streaming | Not published | Not published | Programme free; Enhanced BBI licence fee for commercial use; SDK licence or MOQ; whether academic use is "commercial" not stated | **New access requests paused since spring 2026 (C)**. Fitrockr's Garmin grant (Asia 2026) closed 31 Mar 2026 |
| **Oura** | **Oura for Organizations, "Oura for research"**, plus the Oura Research participant app; public API v2 | Dashboards, group or individual download, "raw data" CSV/JSON export (meaning undefined), "premium metrics" for academics (vendor page) | API: 10 users until Oura approves; none after | **API and MCP Agreement (8 Jun 2026): keep data only as long as strictly necessary; delete within 72 h of a request; no AI/ML training (one clause has no consent exception); benchmarking needs consent; no research carve-out.** Whether research customers sign different terms is not public | Membership $69.99/yr per participant (mandatory for API data); research offering price not published | Active |
| **WHOOP** | No published academic programme (R); WHOOP Unite is enterprise, terms not public | Derived scores only | **Sandbox 10, Build 100, Growth 1,000, Scale 5,000, Production unlimited**; one tier at a time, 50% fill rule, manual review | **Terms (6 Oct 2026): no permanent copies; no AI/ML training or testing; both "unless expressly authorized by the WHOOP Data owner or by applicable law"; no research carve-out** | API no charge; membership ~$199–$359/yr (R) | Active |
| **Samsung** | No academic tier; Samsung Partner Program for the Health Sensor SDK; Research Stack (open source) | Raw and processed on-watch signals to the team's own app | None (no Samsung server) | None from Samsung; partner agreement has no HIPAA, BAA or DPA language | No fee documented | Sensor SDK active (v1.4.1); Research Stack dormant since 24 Oct 2024 |
| **Polar** | No formal programme; "Collaborate with us" contact | Open BLE SDK raw data; AccessLink derived data and exercise RR | None | BLE: none. AccessLink: Limited License Agreement (not summarised in the profile) | Free | Active (SDK 8.4.0, 2026-10-01) |
| **Withings** | **Advanced Research API** ("for research groups, universities"); **Advanced Biomarkers** plan ("Clinical studies & AI research"); Start for Free | Raw ScanWatch accelerometer and PPG by contract; free plan derived data | Free plan 10 users, more after review | **"AI model training contract" only on Advanced Biomarkers**; retention not published | Free plan, but **Withings+ per new-account participant from 12 Oct 2026**; paid plans custom; "Research partners" exemption terms unpublished | Active |
| **Empatica** | **Academic & Basic Research plan**, self-serve store; 25% academic discount by application (institutional email) | All EmbracePlus and EmbraceMini raw sensor data and a selection of biomarkers; S3 keys; no streaming; no SDK | **1 study, 1 site, 1,000 participants** per academic account | Participant data retained for the service plus 10 years (C); access after the 3- or 5-year window Unclear | EmbracePlus 3-year $1,749.60; EmbraceMini 3-year $1,137.24 (academic) | Active |
| **Ametris** | academic.ametris.com: pricing-list form, grant toolkit, dataset library; academic store for existing accounts | Same devices and data as sponsors; PPG files "subject to contract restrictions" | Not stated | Not stated; historical raw-file generation may carry fees | Not published | Active; part of Signant Health |
| **Axivity / GENEActiv** | None needed | Full raw signal by USB | None | None | AX3 from £139, AX6 from £199 (ex VAT); GENEActiv quote | Active |
| **Movesense** | **Movesense Academic Program**: free sensors and accessories for selected projects; monthly review, up to three projects per quarter; publications must credit Movesense | Same data as any developer | None | None from the vendor; SDK is a 12-month evaluation licence, deployed use may need a separate agreement | Free sensors if selected; MD €349 | Page says open "until further notice"; latest listed cohort Q1 2023, so **Unclear** |
| **Ultrahuman** | No academic programme; UltraSignal (loaned kit) or Partner API | PPG, temperature and accelerometer stream; derived ring and CGM metrics | Not published | Not read, **Unclear** | Not disclosed | Unclear |
| **Biostrap / Sensor Bio** | No separate programme; white-label platform by demo | Raw PPG and derived signals (vendor) | Not published | Not published | Not public | Rebranded to Sensor Bio |
| **Verily** | Enterprise engagement only | Not procurable by an academic group | n/a | n/a | Not public | Study Watch status Unclear |
| Intermediaries | Labfront grants programme; Fitrockr and Garmin grants; Fitabase quote | See Table 11 | Platform-specific | Thryve stores data 2 weeks (Start Up) or 1 month (Scale Up); Fitrockr Data Vault €150/month for post-project access | See Tables 7 and 11 | Active |
