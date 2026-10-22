# Module 1, Wearables Comparison Matrix

**Rebuilt 2026-10-10 from the profiles.** Every cell below was rewritten from the current profiles in
`profiles/` (corrected and re-verified in commit c774edb) and from `validation-evidence.md`. Where a
profile says Unclear, the cell says Unclear. Nothing here is newer than the profile it comes from: if
a cell and a profile disagree, the profile wins and this file is out of date.

**Batch-1 correction, 2026-10-11.** Cells for Apple, Fitbit/Google, Garmin, Oura, WHOOP, Samsung,
Empatica and Withings were checked against the committed vendor fact records (`../facts/<company>.yaml`)
and corrected where they differed. For these eight vendors the record is the source of truth. Their
profiles carry the same facts in generated fact blocks.

**Batch-2 correction, 2026-10-11.** Cells for Polar, Ametris, Axivity, Activinsights (GENEActiv) and
Movesense were checked the same way against `../facts/polar.yaml`, `ametris-actigraph.yaml`,
`axivity.yaml`, `activinsights-geneactiv.yaml` and `movesense.yaml`. Axivity and GENEActiv still
share rows here; where the two vendors differ, the cell names each.

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
| As of 2026-10-19 | **Google Health API apparently open to new projects again** (C). The 2026-10-10 notice ("While we are not onboarding new projects at this time...") was removed by 2026-10-19, with no announcement. Approval needs Google's restricted-scope review and, above 100 users, verification and CASA | `fitbit-google.md` |
| Since spring 2026 | **Garmin Connect Developer Program access requests paused**, no reopening date (C) | `garmin.md` |
| **12 October 2026** | **Withings+ membership required** for participants whose Withings accounts are created on or after this date to share data with a Start for Free app, including via Apple Health or Google Health | `withings.md` |
| 6 October 2026 | WHOOP API Terms of Use in force: no permanent copies and no AI or ML training on WHOOP data, unless authorised by the data owner or by law | `whoop.md` |
| 8 June 2026 | Oura API and MCP Agreement in force: retain data only as long as strictly necessary, 72-hour deletion on request or subscription cancellation, no AI or ML training, and no use of the API to evaluate or prompt AI models outside the MCP Server | `oura.md` |
| December 2025 | Oura personal access tokens retired; OAuth 2.0 only | `oura.md` |
| 24 October 2024 | Last code push to any Samsung Health Research Stack repository (checked 2026-10-10) | `samsung.md` |
| 14 May 2026 | Signant Health announced its acquisition of Ametris (agreement announced 16 April 2026) | `ametris-actigraph.md` |

---

## Table 1, Ecosystem orientation and access model

| Ecosystem | Primary orientation | Access model | Vendor cloud in data path? | Approval required? | Can a new study start today without vendor contact? |
|---|---|---|---|---|---|
| **Apple** | Consumer | HealthKit read by a researcher-built iOS app; SensorKit for research signals | **No.** Apple never receives the study copy | SensorKit: per-study Apple approval plus IRB approval. Optional research entitlements (HealthKit Research Entitlement, Background Health Research Task) and Investigator Support Program devices are by request to Apple | HealthKit yes; SensorKit no |
| **Fitbit / Google** | Consumer | Google Health API (Google OAuth 2.0, REST). Legacy Fitbit Web API unsupported since 30 Sep 2026, **off 30 Oct 2026** | Yes | Most Google Health API scopes are Restricted; unverified apps capped at 100 users; verification and a CASA assessment above that; research apps file a Health Research Attestation | **Partly.** Google Health API apparently open to new projects again (C, 2026-10-21; Google was not onboarding them on 2026-10-10); approval needs Google's restricted-scope review and, above 100 users, verification and CASA. Other routes: Fitabase (own project; new-study capacity not stated), the on-device route via Apple Health or Health Connect with no Google Health API project (C), participant self-export, *All of Us*. Thryve and Validic need the customer's own project (C); Terra says it manages the Google Health credentials, with its review and CASA status not stated |
| **Garmin** | Consumer / athletic | Health API (cloud, push or ping/pull) or Health SDK, Standard or Companion (enterprise partners) | Health API yes; Standard SDK keeps data out of Garmin Connect | Business-use programme application; **new access requests paused since spring 2026 (C)** | **No.** Practical routes: Labfront, Fitabase or Fitrockr (Terra now needs the customer's own Garmin credentials) |
| **Oura** | Consumer | API v2 (OAuth 2.0 only) with webhooks; Oura for Organizations research offering | Yes | An API app is limited to 10 users until Oura approves it; research offering by contact | Yes, up to 10 users, under the API and MCP Agreement |
| **WHOOP** | Consumer | API v2 (OAuth 2.0) with webhooks | Yes | App approval; member tiers raised one step at a time by manual review | Yes, Sandbox tier only (10 members) |
| **Samsung** | Consumer | Samsung Health Sensor SDK (formerly Privileged Health SDK) on the watch; Research Stack, self-hosted, no code updates since Oct 2024 | **No** for the Sensor SDK path | SDK v1.4.1 is a public download; **Samsung Partner Program approval to distribute** the app (package name and SHA-256 registered) | Development and testing yes (developer mode); deployment no |
| **Polar** | Athletic / research | BLE SDK (GitHub, source-available under Polar's limited licence), or AccessLink cloud API | **No** for BLE; yes for AccessLink | **None** for the BLE SDK; any registered Polar Flow user can create an AccessLink client | **Yes** |
| **Withings** | Connected health devices | Public Health Data API (Start for Free, Enterprise, Advanced Biomarkers plans); Advanced Research API for raw data | Yes; EU or US medical cloud | Raw data: contracted partners only; free plan above 10 users: Withings review | Yes on the free plan, up to 10 users; **Withings+ needed from 12 Oct 2026** for participants with new accounts |
| **Empatica** | Research / medical | Care Portal (Care Lab Portal on the academic plan); CSV biomarker download; raw signal as Avro via Amazon S3 data access keys; Enterprise Cloud API | Yes | Academic plan bought from the store; academic discount by application with an institutional email | Yes for the academic plan; Enterprise by quote |
| **Ametris (ActiGraph)** | Clinical trials | CentrePoint platform and V3 API; legacy ActiLife desktop workflow | CentrePoint yes; ActiLife local | Quote; API access must be enabled by Ametris | No |
| **Axivity / GENEActiv** | Research | **Axivity: USB only**, no vendor cloud (local device API libOMAPI). **GENEActiv: USB by default**; optional Activinsights cloud (Azure) with per-study APIs and the Study Management Hub; GENEActiv 1.3 adds Bluetooth adherence sync | **No** for Axivity and for GENEActiv by USB; yes on the optional Activinsights cloud | **None** | Axivity yes (online shop); GENEActiv by quote |
| **Movesense** | Open sensor | BLE to the team's own app; onboard logging (Flash); custom firmware | **No** | None to develop; SDK under a proprietary 12-month evaluation licence, separate agreement for commercialisation | Yes |
| **Ultrahuman** | Consumer ring | Self-serve personal API token (own data plus users who link via Partner ID; daily metrics and raw PPG recordings); Partner OAuth (app registration self-serve, production approval undocumented); UltraSignal kit by application (V/C, fact record 2026-10-21) | Yes (API) | None for the personal token; UltraSignal yes; OAuth production approval unclear | Yes, via the personal token |
| **Biostrap (now Sensor Bio)** | Research platform | RPM dashboard export; REST API at developers.sensorbio.com (keys on request to an org administrator); Mobile SDK v0.17.0 (V) | Yes (AWS) | Contact sales; API keys on request | No |
| **Verily Study Watch** | Clinical research only | Verily Pre (Exchange and Workbench) and Viewpoint Evidence | Yes | Workbench Standard none (DUA per data collection); Viewpoint by sponsor engagement | Only to analyse existing Exchange collections (Workbench Standard, free, beta); Study Watch status conflict, R (device program wound down 2025) |

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
| Movesense MD / Flash / HR2 | No | ✓ | ✓ | ✓ (plus magnetometer) | ✓ (internal, non-medical) | No | No | Unclear | No | No |
| Withings ScanWatch 2 | ✓ | ✓ | ✓ | Unclear | ✓ | ✓ | Unclear | ✓ | No (Body Scan scale has EDA) | No (Body Scan scale has segmental impedance) |
| Ultrahuman Ring PRO / AIR | ✓ | Unclear | ✓ | Unclear | ✓ | ✓ (SpO2 in daily metrics API, V) | Unclear | Unclear | Unclear | Unclear |
| Biostrap / Sensor Bio wrist | ✓ | Unclear | ✓ | EVO (legacy) only; not on V2 (V) | ✓ skin temperature (V2, V); legacy Thermo Patch FDA claim has no FDA record | Planned, not live on V2 (V) | Unclear | Unclear | Unclear | Unclear |
| Verily Study Watch | ✓ 30 Hz (C) | ✓ (C) | ✓ (inertial, C) | Unclear | Unclear | Unclear | Unclear | Unclear | ✓ (C) | Unclear |
| Empatica EmbracePlus | ✓ | No | ✓ | ✓ (selected sensor modes) | ✓ | ✓ (FDA K221282, no-motion conditions only; SpO2 biomarker is Enterprise only, not on the academic list) | No | Unclear | ✓ | No |
| Ametris LEAP | ✓ (green, red, IR) | No | ✓ | ✓ (IMU) | ✓ (skin) | Investigational metric (Scientific Services; outside the 510(k)) | No | ✓ | No | No |
| Ametris Insight Watch / wGT3X-BT | No | No | ✓ | No | Insight Watch (near-body) | No | No | No | No | No |
| Axivity AX3 / AX6 | No | No | ✓ | AX6 only | ✓ (internal device temperature) | No | No | No | No | No |
| GENEActiv | No | No | ✓ | No | ✓ (near-body) | No | No | No | No | No |

Raw EDA has three routes in this module: Empatica, **Samsung Galaxy Watch8 and later (1 Hz, via
the Health Sensor SDK)** and the Verily Study Watch (C). Fitbit Sense has an EDA sensor but no EDA
data type in the Google Health API. Ambient light is also present on the GENEActiv, the Axivity
AX3/AX6 (relative level, not lux) and the wGT3X-BT; Ametris LEAP also has a microphone, disabled by default.

---

## Table 3, Raw signal availability to researchers (the decisive table)

| Ecosystem | Raw accel | Raw PPG waveform | ECG | IBI / RR / BBI | Raw EDA | Route |
|---|---|---|---|---|---|---|
| **Apple** | Not via HealthKit. **Core Motion `CMSensorRecorder` 50 Hz in the background, no entitlement** (12 h per call, 3-day retention); 800 Hz during workouts; SensorKit `accelerometer` (iOS 14+, research entitlement) | **SensorKit only** (`photoplethysmogram`, iOS 17.4+); rate and capture schedule undocumented; not via HealthKit | Per-recording voltage samples via `HKElectrocardiogramQuery`; whether these count as raw is in conflict (Apple's research FAQ says no raw ECG via HealthKit); SensorKit `electrocardiogram` (iOS 17.4+); no continuous ECG | Context-limited: `HKHeartbeatSeriesSample` beat timestamps during ECG and some workout or Breathe sessions | n/a | HealthKit; SensorKit (Apple-approved study entitlement) |
| **Fitbit / Google** | No | No | Google Health API `electrocardiogram` session documented with raw waveform voltage samples per on-demand reading; not tested with a real pull | No (HRV as an RMSSD sample type) | No EDA data type in the API; treat as unavailable | Google Health API, **apparently open to new projects again** (C, 2026-10-21) |
| **Garmin** | **Health SDK only** (listed as "Accelerometer" for streaming and logging; rate not published by Garmin; logging fixed at 25 Hz per two integrators, C); not via the Health API; Connect IQ in-app | No | Not documented via the Health API | **Enhanced BBI with per-beat confidence**: Health API (licence fee for commercial use) and Health SDK streaming and logging. Fitabase's API route captures it during sleep; Labfront's SDK route across the day (R). Fitabase also has a Garmin SDK route through its Engage app, daytime coverage and rate not stated (C). Garmin's 2023 technical note says it is measured during sleep; whether the Health API delivers it outside sleep is Unclear | n/a | Health SDK (enterprise partners), Health API (paused to new applicants), or Labfront / Fitabase / Fitrockr |
| **Oura** | No | No | n/a | No (HR at 5-minute increments; nightly HRV) | n/a | API v2, derived only |
| **WHOOP** | No | No | MG ECG feature exists; no ECG scope in the API | No | n/a | API v2, derived scores only; Unite research raw files with RR intervals (2023, R), current availability Unclear |
| **Samsung** | **Yes, 25 Hz** | **Yes, green, IR and red: 25 Hz continuous, 100 Hz on demand** | **Yes, raw, 500 Hz on demand** (one on-demand tracker at a time, about 30 s) | **Yes, HR with IBI at 1 Hz** | **Yes, 1 Hz, Galaxy Watch8 and later** | Health Sensor SDK (partner registration to distribute); also via Verily Pre / Viewpoint Evidence (R, press paraphrase only) |
| **Polar H10** | **Yes, 25 / 50 / 100 / 200 Hz, ±2 / 4 / 8 g** | n/a | **Yes, 130 Hz in µV** (streaming only; internal memory logs HR only) | **Yes, RR in ms with HR at 1 Hz** | n/a | **BLE SDK (Polar limited licence), no registration**; AccessLink returns exercise RR when an H10 was used |
| **Polar Verity Sense** | **Yes, 52 Hz; SDK mode 26 to 416 Hz, ±2 to 16 g** | **Yes, SDK mode 28 to 176 Hz, 22-bit** | No | Yes (PPI), but not in SDK mode | n/a | BLE SDK (Polar limited licence) |
| **Polar 360 / Loop** | Yes, 12 to 400 Hz online, 1 to 50 Hz offline | **Yes, 22 / 50 / 100 Hz online and offline, 24-bit, green** | No | PP interval; 24/7 PPI as automatically triggered sessions, schedule undocumented (C) | n/a | BLE SDK (Polar limited licence); 15 MB storage shared with activity and sleep |
| **Movesense** | **Yes, 9-axis IMU; maximum 416, 833 or 1666 Hz depending on the vendor source (conflict)**; the highest rates may be limited by BLE | n/a | **Yes, single lead, 125 to 512 Hz** (above 256 Hz not advised over BLE) | **Yes, R-R at 1 ms resolution** | n/a | BLE or onboard logging (Flash, 128 MB); custom firmware; no licence fee, proprietary evaluation licence |
| **Withings** | Yes, ScanWatch, about 24.824 Hz in raw mode, ±4 g (overview page says "25 Hz by default (up to 100 Hz)"; no documented setting reaches 100 Hz) | Yes, green, red and IR, about 24.824 Hz | Not in the Raw Data API | Not documented | n/a | **Advanced Research API, contracted partners only**; raw mode disables all other watch features; battery falls to 3–4 days |
| **Ultrahuman** | Named for UltraSignal kits only; no public endpoint | **Yes, typically 50 Hz**, gzip NDJSON, own Developer Mode recordings only (V) | n/a | Derived HRV via the API | n/a | PPG Recordings API with a personal token; UltraSignal kit by application |
| **Biostrap / Sensor Bio** | Yes, up to 100 Hz (V2, V); gyroscope on legacy EVO only | Yes, up to 100 Hz export (V2, V); whether enterprise tier is required is a conflict on Sensor Bio's own pages | n/a | Yes (V2 export and SDK, V) | n/a | RPM dashboard CSV/JSON or SDK live stream; 50 Hz default, 25 or 100 Hz per organisation; REST raw download EVO-only and deprecated |
| **Empatica** | **Yes; 64 / 64 / 32 / 64 / 100 Hz by sensor mode** (Pulse Rate Pro / Actigraphy Pro / Actigraphy Optimized / Gyroscope Max / Gyroscope 100), ±16 g; gyroscope in the two Gyroscope modes | **Yes; 64 Hz (Pulse Rate Pro) or 4 Hz infrared (Actigraphy Pro)**, off in other modes | No | Yes, raw systolic peaks (IBI) | **Yes; 4 Hz in Pulse Rate Pro and Actigraphy Pro**, off otherwise | Avro raw files and CSV biomarkers via S3 access keys; **no real-time streaming**; one mode per academic account (Pulse Rate Pro was the only academic mode until 16 Sep 2026) |
| **Verily Study Watch** | Yes, inertial, 30 Hz (C) | Captured at 30 Hz (C); whether raw reaches outside researchers is not stated | Yes (C) | Derived IBIs with a quality flag (C) | **Yes (C)** | De-identified PBHS data on approved request, or Exchange collections in Workbench under a DUA; device program wound down 2025 (R) |
| **Ametris** | **Yes; Insight Watch and LEAP 32 to 256 Hz, ±8 g; wGT3X-BT 30 to 100 Hz, ±8 g** | **LEAP: green 25 Hz and 100 Hz, red/IR 50 Hz**, "only available for certain devices, firmware versions, and study configuration, and ... subject to contract restrictions"; LEAP PPG also processed locally in ActiLife 7 | No | Not documented | n/a | CentrePoint API Data Access Files (CSV or AVRO); ActiLife `.gt3x` |
| **Axivity / GENEActiv** | **Yes; AX3 12.5 to 3,200 Hz, AX6 12.5 to 1,600 Hz, ±2 to 16 g, configurable** (UK Biobank used 100 Hz, ±8 g); GENEActiv 10 to 100 Hz, ±8 g, 12 bit (v1.3: 10, 20, 25, 50 or 100 Hz only) | n/a | n/a | n/a | n/a | **USB raw file** (Axivity, GENEActiv); optional Activinsights cloud API for GENEActiv |

### Sampling-rate reference, by signal

Rates are the maxima the profiles document. Cost of entry is the cheapest documented way to get that
rate; a blank price means the profile gives none.

| Signal | Device | Maximum documented rate | Cost of entry |
|---|---|---|---|
| ECG | Movesense | 512 Hz (above 256 Hz not advised over BLE) | MD €349 ex VAT (1 to 49 units), €339 (100 to 199); no licence fee |
| ECG | Samsung Galaxy Watch | 500 Hz, on demand | Consumer watch; partner registration to distribute |
| ECG | Polar H10 | 130 Hz | **$104.95** (Polar US store, 2026-10-11); free SDK under Polar's limited licence, no approval |
| Accelerometer | **Axivity AX3** | **3,200 Hz** | **£139 ex VAT**; no software cost |
| Accelerometer (IMU) | Movesense | 416 to 1666 Hz, 9-axis (vendor sources conflict) | €349 ex VAT |
| Accelerometer (with gyro) | Axivity AX6 | 1,600 Hz | £199 ex VAT |
| Accelerometer | Polar Verity Sense (SDK mode) | 416 Hz | $104.95 (Polar US store, 2026-10-11) |
| Accelerometer | Polar 360 / Loop | 400 Hz online | Loop $199.99 (US store, 2026-10-11); Polar 360 by B2B contact, no price published |
| Accelerometer | Ametris Insight Watch / LEAP | 256 Hz | Quote only |
| Accelerometer | Polar H10 | 200 Hz | $104.95 |
| Accelerometer | Empatica EmbracePlus | 100 Hz (Gyroscope 100); 64 Hz (Pulse Rate Pro, Actigraphy Pro, Gyroscope Max); 32 Hz (Actigraphy Optimized) | $1,749.60 academic 3-year bundle |
| Accelerometer | Samsung | 25 Hz | Partner registration |
| Accelerometer | Withings ScanWatch | ~24.8 Hz | Contract |
| Raw PPG | **Polar Verity Sense (SDK mode)** | **176 Hz, 22-bit** | $104.95 (Polar US store, 2026-10-11) |
| Raw PPG | Samsung (green, IR, red) | 100 Hz on demand; 25 Hz continuous | Partner registration |
| Raw PPG | Polar 360 / Loop | 100 Hz, 24-bit | Loop $199.99 (US store, 2026-10-11); Polar 360 by B2B contact, no price published |
| Raw PPG | Ametris LEAP (green) | 100 Hz; subject to contract restrictions | Quote only |
| Raw PPG | Empatica EmbracePlus | 64 Hz (Pulse Rate Pro); 4 Hz (Actigraphy Pro) | $1,749.60 academic 3-year bundle |
| Raw PPG | Withings ScanWatch | ~24.8 Hz | Contract |
| Raw PPG | Apple SensorKit | Not published | SensorKit entitlement |
| Raw PPG | Ultrahuman | Typically 50 Hz (V) | Personal API token, own Developer Mode recordings only; Ring PRO USD 479 |
| EDA | Empatica EmbracePlus | 4 Hz (Pulse Rate Pro, Actigraphy Pro) | $1,749.60 academic 3-year bundle |
| EDA | Samsung Galaxy Watch8 | 1 Hz | Partner registration |
| EDA | Verily Study Watch | Not published | Not procurable; device program wound down 2025 (R); historical PBHS data only |

**Reading.** The highest documented raw rates in the module come from open sensors sold at modest
prices (Axivity AX3 accelerometry to 3,200 Hz, Movesense ECG to 512 Hz and IMU to at least 416 Hz,
with vendor sources giving up to 1666 Hz, Polar Verity Sense PPG to 176 Hz), not from the clinical-trial vendors. Samsung is the consumer exception
(ECG 500 Hz, PPG 100 Hz on demand). What the open sensors give up is form factor, wear duration,
derived metrics and study infrastructure.

---

## Table 4, API characteristics

| Ecosystem | Auth | Rate limit | Push / webhooks | Historical backfill | Latency driver |
|---|---|---|---|---|---|
| Apple | On-device permission | n/a | HealthKit background delivery | On-device history back to the earliest permitted date; from iOS 27 participants can cap it at 30 days unless the app holds the HealthKit Research Entitlement | iOS background execution limits |
| Fitbit Web API (legacy) | Fitbit OAuth 2.0 | 150 req/hr per consented user | Subscription API | Moot | **Unsupported since 30 Sep 2026; turned off 30 Oct 2026** |
| Google Health API | Google OAuth 2.0 | **300 req/min per user; 120,000 req/min and 86.4M req/day per project; unverified apps 250 QPS across at most 100 users** | `projects.subscribers` subscriptions | All recorded history, no API limit; rollup queries capped at 14 or 90 days per request | Participant app sync; **apparently open to new projects again** (C, 2026-10-21) |
| Garmin Health API | Garmin OAuth consent | Not published (evaluation access throttled; the agreement refers to request-volume limits) | Push or ping/pull | Backfill tooling exists; 30 days before consent per one integrator (R) | Device to Garmin Connect sync; latency not published |
| Oura | **OAuth 2.0 only** (PATs no longer available) | **5,000 requests per 5 minutes** (OpenAPI 1.41 FAQ); two layers, per token and per application, split not stated; `X-RateLimit-*` headers; higher on request | **Webhooks recommended**, about 30 s after app sync, 10 retries | One historical request on first connect; no lookback limit documented | **Sleep data reach the API only after the user opens the Oura app** |
| WHOOP | OAuth 2.0 | **100 req/min and 10,000 req/day per client**; increases on request | Yes (v2; v1 removed) | No documented lower bound on start time; full history implied, not stated (C) | Device to cloud sync |
| Samsung | On-device SDK | n/a | n/a | Sensor SDK from enrolment onward; Data SDK reads whatever Samsung Health holds, no documented limit (C) | Researcher's own pipeline |
| Polar BLE SDK | None | **None** | n/a | Device onboard memory | Bluetooth range |
| Polar AccessLink | OAuth 2.0 | 500 + 20 × users per 15 min; 5,000 + 100 × users per 24 h | Webhooks | **None before the user registers with the client**; exercises from the last 30 days only; activity 28-day default, no older than 365 days | Polar Flow sync |
| Withings | OAuth 2.0 | Enterprise and Advanced Biomarkers "1,500+ requests/minute"; Start for Free "Standard"; throttled calls return status 601 | Webhooks | No maximum published; per-call windows (24 h intraday activity, 7 days on one sleep endpoint); sync by `lastupdate` | Cellular or app sync |
| Empatica | Portal login; S3 access keys | n/a | **No real-time streaming** | Full study history for the 3- or 5-year subscription (extendable yearly) and 60 days after termination | 30-minute batches; once a day in Actigraphy Optimized |
| Ametris CentrePoint | OAuth 2.0 client credentials (tokens 3,600 s), enabled by Ametris | More than 500 req/min from one IP returns 429; 10 concurrent raw requests, GT3X ranges of at most 15 days; V2 API daily limit unpublished | Webhooks, including raw-processing-complete | Historical raw-file generation may carry fees; no lookback limit published (Unclear) | Cellular gateway or app |
| Ultrahuman | Personal token (self-serve) or OAuth 2.0; token lifetime stated as both a week and 86400 s, plan for 1 day | 200 req/min on the PPG and blood-report APIs; no figure for daily metrics | Unclear | No maximum lookback documented; 7-day window per request | Unclear |
| Axivity / GENEActiv | n/a for USB (Activinsights cloud: per-study APIs, no public reference) | n/a (Activinsights: not published) | n/a | n/a | **Device return** (GENEActiv 1.3: adherence data by Bluetooth about every 5 h) |

---

## Table 5, Study operations and management

| Ecosystem | Researcher portal | Participant roster | Adherence / wear-time monitoring | Multi-site | Surveys / EMA | Device reuse |
|---|---|---|---|---|---|---|
| Apple | No (Apple Research app is Apple's own, not procurable); Study App Template free to approved Investigator Support Program applicants | No | No | No | Build with ResearchKit | n/a (BYOD) |
| Fitbit / Google | No; via Fitabase (quote) or Fitrockr | Via platform | Via Fitabase (sync and battery status) | Via platform | Fitabase Engage, relaunched April 2026; iPhone app live; pages still say "Preview · Summer 2026" (2026-10-21); unpriced | Via platform |
| Garmin | No; via Labfront, Fitabase or Fitrockr | Via platform | Via platform | Via platform | Labfront (all tiers); Fitrockr (paid add-on) | Via platform |
| Oura | **Oura for Organizations research dashboards** (vendor page; price not published) | Group and access-level management (vendor) | Adoption, attrition and engagement tracking (vendor) | Unclear | Tags only | Requires re-sizing |
| WHOOP | None in the public platform; a paid group-download web app is reported for research partners (R); Unite status Unclear | No | No | No | Journal not in the API; included in each member's own CSV export (R) | Membership-bound |
| Samsung | Research Stack portal, self-hosted, **no code updates since Oct 2024** | Yes | Unclear | Unclear | Yes (Research Stack) | Unclear |
| Polar | No (Team Pro is team-sport) | No | No | No | No | Yes |
| Withings | Withings Health Solutions services model | Via partner or RPM platform | Via partner | Via Health Solutions | Patient Insights questionnaires on BPM Pro 2 (Advanced Biomarkers plan); otherwise via DCT partner | Yes |
| **Empatica** | **Care Portal** (Care Lab on the academic plan) | Yes; **academic account limited to 1 study, 1 site, 1,000 participants, sensor mode fixed per account**; Enterprise minimum order 100 devices | **Yes, live wear-time** | Yes (Enterprise); 1 site on the academic plan | None (event marking only) | **Yes, multiple participants per device** |
| **Ametris** | **CentrePoint** | Yes | **Yes, near-real-time and monthly reports** | **Yes, 70+ countries** | Combined Ametris DHT and Signant eCOA offering for CNS trials announced 2026-03-10, for sponsors; integration depth not stated | Yes, automated device assignment |
| Axivity / GENEActiv | **Axivity no**; Activinsights Study Management Hub (demo by request) | Axivity no; Activinsights Hub | **Axivity and GENEActiv 1.1/1.2: impossible during wear**; GENEActiv 1.3: Bluetooth adherence about every 5 h | No | No | Yes |
| Movesense | No; via Labfront (MD, HR2, Flash; participants start each recording manually) | Via Labfront | Via Labfront | Via Labfront | Via Labfront | Yes |
| Biostrap / Sensor Bio | Participant management dashboard (vendor; legacy biostrap.com page, carry-over to V2 not stated) | Enrolment workflows (vendor, legacy page) | Compliance notifications (vendor, legacy page) | Unclear | Integrated surveys (vendor, legacy page) | Unclear |

---

## Table 6, Participant experience and operational burden

| Ecosystem | Form factor | Battery | Charging conflict with sleep? | Phone required? | BYOD viable? |
|---|---|---|---|---|---|
| Apple | Watch | About a day (non-Ultra) | **Yes, significant** | Yes (iPhone) | **Yes**, iPhone owners only |
| Fitbit | Band / watch | Several days to a week or more (trackers); Fitbit Air up to 7 days (C) | Minor | Yes (Google Health app, iOS or Android) | Yes |
| Garmin | Watch | **One to three weeks**, some solar models longer | **No** | Yes (Garmin Connect) | Yes |
| Oura | **Ring** | About 4–7 days; 20–80 min charge | Minor | **Yes; sleep reaches the API only after the app is opened** | Partly (sizing kit; membership required) |
| WHOOP | Screenless band or apparel | 14+ days for 5.0 and MG (R, vendor page capture 2026-10-02); **charged on the wrist with a slide-on pack** | **No wear interruption** | Yes | Partly (membership) |
| Samsung | Watch / ring | About 1 to 2 days; **continuous raw capture reduces this substantially** (not measured by Samsung) | Yes | Yes (Android; Galaxy Watch4 or later) | Galaxy Watch owners for the watch app; the phone-side Data SDK also runs on non-Samsung Android phones (Samsung Health 6.30.2+) |
| Polar H10 | Chest strap | Session wear | n/a | ECG and accelerometry need a phone; internal memory logs HR only | No |
| Polar Verity Sense | Armband | Session wear | n/a | No (offline recording per the product docs; a Polar staff reply says offline recording is H10-only, R) | No |
| Movesense | Chest-worn sensor | Battery life not published; MD runs on a user-replaceable CR2025 coin cell and is rated IP68 (vendor FAQ, 2024); Flash logs up to 5 days of ECG | n/a | Flash logs phone-free (128 MB) | No |
| Withings | Hybrid watch, scale, BP cuff, **under-mattress sleep mat** | ScanWatch about 30 days (3–4 days in raw mode) | No | **No for cellular devices** | Partly |
| Empatica | Wristband | EmbracePlus 2+ / 7+ / 14+ / 5+ / 5+ days by mode (Pulse Rate Pro about 2 days); EmbraceMini 7+ / 14+ / 3+ / 3+ (no Pulse Rate Pro); Enterprise "up to 28 days" matches no published mode | No | Care / Care Lab app used; phone requirement not stated in the profile | No |
| Ametris | Research watch / puck | Insight Watch 30 days at 32 Hz; wGT3X-BT 25 days; LEAP 1 to 32 days by configuration, about 32 at the 32 Hz default; LEAP storage 79 days / 1 GB (C) | No | **No, cellular gateway option** | No |
| Axivity / GENEActiv | Sealed puck | AX3 14 days at 100 Hz; 30 days at 12.5 Hz per the product page, but the datasheet also says "up to 21 days" (conflict); AX6 about 7 days at 100 Hz with gyro, up to 140 days at 12.5 Hz; GENEActiv 1.2/1.3 14 days at 100 Hz, 44 days at 20 Hz (product sheet says 60, conflict); **no charging during wear** | **No** | **No** | No |

---

## Table 7, Cost structure

| Ecosystem | Device cost | Recurring per participant | API / platform fee | Pricing public? |
|---|---|---|---|---|
| Apple | Series 12 from $399, SE 3 from $249, Ultra 4 from $799 (US store); no research discount, but devices free to approved Investigator Support Program studies | **None** | No API fee; Apple Developer Program $99/yr, waived for approved nonprofits, educational institutions and government | Devices yes; the main cost is app engineering |
| Fitbit / Google | Fitbit Air from $99.99; trackers among the cheapest research-viable wearables | Premium not required; $9.99/mo or $99/yr | No documented API fee; CASA assessment $500 to $4,500, renewed annually, if verification is needed (C); Fitabase by quote | Partly |
| Garmin | Launch prices $149.99 (vívosmart 5) to $349.99 (Forerunner 170 Music); CIRQA $199.99 | **None required** (optional Connect+ $6.99/mo or $69.99/yr) | Programme free, business use only; agreement s.10.1 says no fees are due, but Garmin may add API fees on 30 days' notice; **Enhanced BBI: licence fee for commercial use**; SDK: evaluation free, commercial licence fee or device MOQ; a $5,000 admin fee reported by third parties is unsupported | Devices only |
| Oura | Ring 5 $399 to $499, Ring 4 from $349 (US store) | **$5.99/month or $69.99/year (US), mandatory for API data on Gen3 and later** | API free today; the Agreement reserves the right to charge, including differentiated business pricing; research offering price not published | Ring and membership yes; research offering no |
| WHOOP | Included in membership | One $199, Peak $239, Life $359 per year (US vendor page, 2026-10-10) | API "currently provided at no charge"; research routes have carried extra fees (R) | Yes, consumer prices; research pricing not public |
| Samsung | Consumer retail | **None** | No SDK fee published, but the partner licence reserves Samsung's right to charge in future; Research Stack open source (engineering and hosting cost) | Devices only |
| **Polar** | **H10 $104.95, Verity Sense $104.95, Loop $199.99** (US store, 2026-10-11) | **None required** (optional Fitness Program EUR 9.99/month) | **SDK free under Polar's limited licence**; AccessLink free at present, agreement reserves the right to charge | **Yes** (devices); Polar 360 B2B by contact |
| **Movesense** | **MD €349 ex VAT (1 to 49 units), €344 (50 to 99), €339 (100 to 199)**; Flash €249, HR2 €99 (1 to 49); developer kits €249 to €399; free sensors for selected Academic Program projects | **None** | No licence cost; separate Commercial License unpublished | **Yes** (1 to 199 units; volume and custom firmware by contact) |
| **Labfront** (Garmin, Movesense, Dexcom) | n/a | **Tester free (5 participants, 30-day window); Basic $500/yr (20 + $10 each), no BBI or accelerometer; Advanced $1,250/yr (20 + $25 each)** | Analytics packages from $3,000 + $50 per participant | **Yes** |
| **Fitrockr** (many brands) | n/a | **Basic from €50/$55 per month; Pro from €150/$165 per month**; 5 device licences included, extra €1 to €15 per device per month; 3-month minimum (Reported, 2026-10-21; site blocks scripts) | Accelerometer and gyroscope +25%; API +20%; live streaming +20%; Data Vault €250/month | **Yes** |
| Withings | ScanWatch 2 $369.95, Light $249.95, Nova $599.95 (US store) | **From 12 Oct 2026: Withings+ per participant** with a new account on the free plan ($9.95/month; annual $99.50 or $99.95, vendor pages conflict); none on paid plans | Start for Free; Enterprise and Advanced Biomarkers custom; raw-data contract non-public | Devices and Withings+ yes; API plan prices no |
| Empatica | **EmbracePlus $1,166.40; EmbraceMini $641.52** | Included in the 3- or 5-year bundle; renewal from $388.80/yr (EmbracePlus), $291.60/yr (EmbraceMini); subscriptions sold only with Empatica devices | **3-year bundle: EmbracePlus $2,332.80 list / $1,749.60 academic; EmbraceMini $1,516.32 / $1,137.24. 5-year: EmbracePlus $2,916 / $2,187; EmbraceMini $1,953.72 / $1,465.29**; Enterprise quote, 100-device minimum | **Yes, academic plan** |
| Ametris | Not published ("calculated for each unique order"); GT3X+ / wGT3X-BT $325 to $1,016 (R, competitor source); one reseller quote (Czech Republic, 2025-07-17): LEAP CZK 15,625 each before a whole-order discount of about 30% (R) | Non-public | ActiLife licences perpetual since 2025-07-30, sold by activation tier; older figures conflict: ~$1,695 (R, competitor source, dated) or US$349 (Ngueleu 2022); the same Czech quote has a 3-year ActiLife 7 Single licence at CZK 136,750 (R); CentrePoint ~$3,500/yr (R, competitor source, dated); academic pricing list on request | **No** |
| Axivity / GENEActiv | **AX3 £139 (£149 with band); AX6 £199 (£209 with band), ex VAT**; GENEActiv by quote, with minimum order values (a competitor reports £425 to £510, R) | **None** for USB use; Activinsights cloud, SDK and services priced on request | **None for the open toolchain** (biobankAccelerometerAnalysis is academic use only; Activinsights R Markdown tools are non-commercial) | **Axivity yes; GENEActiv no** |
| Ultrahuman | Ring PRO USD 479; Ring AIR USD 349 (global) or GBP 329 (UK) | None for data; optional add-ons (Ultrahuman Max from USD 9.99/month) | No published fee; API Agreement says Sandbox and Production are unpaid (R) | Yes, devices |
| Biostrap / Sensor Bio | Not public (V2 sold through partnership) | Not public | Not public | No |
| Verily | No device price; not procurable | n/a | Workbench Standard free; Professional paid, unpriced; Viewpoint by demo | Partly (Standard tier free) |

---

## Table 8, Privacy, security and compliance posture

Every vendor compliance statement here is the vendor's own unless a certificate was checked. Only
Empatica's (TÜV Rheinland), Withings' (AFNOR) and Ametris's (Ignyte Assurance) ISO 27001 certificates
were read, all as vendor-hosted PDFs; Activinsights' only published certificate expired on 31 October
2025. Every "Unclear" is a vendor question, not an inference; see
`../shared/unresolved-questions.md`.

| Ecosystem | HIPAA / BAA | GDPR / DPA | SOC 2 / ISO | Regulatory clearance (FDA 510(k) unless stated) | Self-hosting / data custody |
|---|---|---|---|---|---|
| Apple | **N/A for HealthKit and SensorKit: Apple is not in the data path**; no BAA offered, and Apple's terms bar PHI on its services (C) | Researcher's obligation | n/a | 12 openFDA records under Apple: ECG app (DEN180044, K201525), Irregular Rhythm Notification (DEN180042 and two 510(k)s), AFib History K213971 (also an FDA-qualified MDDT), Sleep Apnea Notification K240929, Hypertension Notification K250507 (2025-09-11), plus three features not on the Watch; see profile | **Full; researcher holds all data** |
| Fitbit / Google | **No BAA under the API terms; PHI only with Google's prior written consent** (C); Enterprise BAA not public | Health Research Policy: IRB approval or waiver, participant disclosure of retention and deletion, immediate de-identification; data transferred to the US and other countries, no residency option documented (C) | Unclear | K200948 ECG App; K212372 Irregular Rhythm Notifications; Body Temperature Software DEN230050 and K243778; K242967 Loss of Pulse Detection | No |
| Garmin | Standard SDK "HIPAA-compliant" (vendor statement, C); no BAA published, availability Unclear | Garmin is an independent controller, no processor DPA; EU SCCs module one (C) | Not public (10-K cites NIST CSF only) | ECG App K221774 (2023-01-12) | **Standard SDK keeps data out of Garmin Connect** |
| Oura | Security page: HIPAA "where we handle protected health information for a healthcare partner"; research page "processes PHI in accordance with HIPAA" (C); BAA available to business customers and healthcare partners (C), no template published | Research page says GDPR-compliant (C); enterprise geo-specific residency options, regions not named (C); API Agreement: retention only as strictly necessary, 72-hour deletion, also on subscription cancellation | Annual SOC 2 examination and HITRUST (C, whitepaper); ISO 27001 not public | No FDA clearance; FDA registration lists Fertile Window (product code LHD, class U, no premarket number) | No |
| WHOOP | **No HIPAA obligations unless agreed in writing; PHI only with prior written consent**; no public BAA (C) | GDPR notice with EU and UK representatives; no DPA published; SCCs on request (R) | SOC 2 claimed only in a 2022 deck (R); ISO 27001 not public | **ECG feature cleared, K243236 (2025-04-04). Blood Pressure Insights not cleared**: warning letter 14 Jul 2025; close-out 17 Jun 2026 says FDA does not intend to enforce for BPI as modified (general wellness) | No; **terms bar permanent copies and AI/ML training on WHOOP data** unless authorised by the data owner or by law |
| Samsung | Partner agreement has no HIPAA, BAA or DPA language; no Samsung server in the Sensor SDK path, but the licence lets Samsung collect information about the service and its use, with user consent | Researcher's obligation for the study copy | Unclear | Galaxy Watch features, not the SDKs: ECG App K201168, K230292, K240909; Sleep Apnea Feature DEN230041, K261011 | **Yes, on-device SDK; Research Stack self-hosted** |
| Polar | No HIPAA or BAA language (privacy notice) (C) | Polar is controller for Flow and not responsible after transfer out; processor agreements only for Team Pro and GoFit; Flow and Team Pro data stored in the EU (Ireland, Sweden; AWS) (C) | ISO 9001 (Polar Electro Oy, to 2028-08-31) and ISO 14001 (Malaysia) only; ISO 27001 and SOC 2 not public | None in openFDA; the SDK licence says the SDK and devices are not for medical use | **Yes, BLE path has no processor** |
| Withings | "HIPAA compliant" EU and US clouds (vendor, C); **BAA and DPA on Enterprise and Advanced Biomarkers only** | EU Medical Cloud "GDPR compliant" (C) | ISO 27001:2022, ISO 27701 and HDS v2 (AFNOR certificates, vendor-hosted PDFs); no SOC 2 | BP monitors K110872, K133125, and via Transtek K223374, K240102; Thermo K160544; ScanWatch K201456 (ECG and spot-check SpO2; recall Z-1280-2023, Class II); Body Scan K230812; Sleep Rx K231667; ECG App K240795; BeamO K252474 | No self-hosting; **choice of EU (France) or US medical cloud** |
| Empatica | "HIPAA-compliant cloud infrastructure located in US, Virginia" (C); no BAA found | **Published DPA**; retention for the service plus 10 years | ISO/IEC 27001:2022, TÜV Rheinland certificate 01 153 2117571, valid to 2028-10-30 (vendor-hosted PDF); ISO 13485, MDSAP, CE; no SOC 2 found | **K221282, K230457, K242737 (adds an SpO2 algorithm change plan), K260374, K252981; seizure products incl. K250515**; PKG K140086, K161717, K211887 held by GKC Manufacturing; Care Lab is research use only | No |
| Ametris | No BAA published (C); HIPAA only as a "HIPAA Compliant" badge image, no written statement (Unclear) | **DPA with SCCs; EU-U.S. Data Privacy Framework** (C) | ISO 13485:2016 with MDSAP; **ISO/IEC 27001:2022 certificate IA391-260410-001** (Ignyte Assurance, to 2029-04-15); SOC 2 Type II reported for 2023 by an aggregator only, no current evidence (Unclear); Part 11 not stated in words | **K231532 (LEAP), K181077 (Insight Watch)**; K080545 (ActiTrainer, which Ametris maps to GT9X and wGT3X-BT, R); K040554 (AM7164, inactive) | CentrePoint cloud (Azure, AWS; regions not published); ActiLife local |
| Axivity / GENEActiv | **Axivity N/A** (never receives data); Activinsights: no BAA or HIPAA statement published | **Axivity: no processor.** Activinsights: processor when its cloud is used, no DPA published, UK/GB processing (C) | Axivity none claimed; Activinsights ISO 27001 certificate expired 2025-10-31 (Unclear); no SOC 2 | Axivity: no FDA records, CE under the EMC Directive only (C). GENEActiv: FDA-listed (product code IKK, 510(k) exempt), not cleared; EU class given as MDD Class I (web page) or MDR Class IIa (IFU), moving to EU MDR | **Full** for Axivity and GENEActiv by USB; Activinsights cloud on Azure, region not stated (C) |
| Movesense | **N/A, no processor in the BLE path**; no BAA or HIPAA statement published (C) | Trivial on the SDK path; Movesense is controller for its ECG Recorder app (C) | ISO 13485:2016 (quality, not security); no ISO 27001 or SOC 2 (C) | **MD: Class IIa, EU MDR 2017/745, only with certified Movesense firmware**; no FDA clearance in openFDA (2026-10-11), Movesense says a 510(k) is on its roadmap | **Full** |
| Ultrahuman | Not a HIPAA covered entity but "strive[s] to comply"; footer claims HIPAA compliance; no BAA published (C) | Claims UK and EU GDPR compliance, outsourced DPO (C); no customer DPA published | ISO 27001 claimed, certificate on request, none published (C); no SOC 2 | None; FDA listing for Fertile Window only (LHD, no premarket number); AFib Detection not marketed in the US | No; AWS, Snowflake and MongoDB Atlas in the US; API Agreement limits partner storage and bars redistribution |
| Sensor Bio | HIPAA claimed only on legacy biostrap.com pages (R); no BAA published | Privacy policy names a DPO but still cites the invalidated Privacy Shield; no DPA published (C) | None published | None; V2 is a general wellness device, "not FDA cleared or approved"; the legacy Thermo Patch claim has no FDA record | No; AWS, no residency option |
| Verily | Business associate for research sponsors when HIPAA applies (C); HIPAA audits claimed for other products, not Study Watch or Workbench | Data Privacy Framework, two Verily entities Active (V); no DPA published (Unclear) | SOC 2 Type II and ISO 27001 claimed for Study Watch & Hub and Workbench, reports possibly under NDA (C) | Study Watch K182456, K192415, K213357 (V) | Workbench region policies on GCP- and AWS-backed collections |

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
| **Current hardware is largely untested** | Oura Ring 5, WHOOP 5.0/MG, Apple Series 12 and Fitbit Air postdate every PSG study here; Oura Gen4 has independent data only for resting HR and HRV |

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
| Withings | Cleared BP, thermometer, Sleep Rx and ECG devices, including ScanWatch ECG and spot-check SpO2 (K201456); ScanWatch sleep staging poor (Schyvens κ 0.22, largest TST, SE and WASO biases) but zero data loss |
| Empatica | **FDA clearances listed in Table 8.** Wrist EDA agrees poorly with palmar or finger EDA in E4 studies (Hu 2024 ICC 0.09 for SCL); no EmbracePlus validation against a palmar reference |
| Movesense | **Independent lab validations exist**: Rogers 2022 vs 12-lead ECG (r=0.98 to 1.0 for RR and HRV), Martín Gómez 2024 R-peak sensitivity 99.7%, both N=21 with sensors supplied by Movesense; IMU step timing vs force plate (N=14). MD is Class IIa MDR with certified Movesense firmware |
| Verily | FDA 510(k)s K182456 (2019-01-17), K192415 (2020-01-17), K213357 (2022-07-19) (V); not evidence of current supply |
| Ametris | **The actigraphy reference standard** for raw accelerometry and its pipelines; current Insight Watch and LEAP not shown equivalent to the legacy devices |
| Axivity / GENEActiv | **UK Biobank AX3, 100,000+ participants**; AX3 equivalent to GENEActiv on shaking tests; open reproducible toolchain |

---

## Table 10, Differentiators and key limitations

| Ecosystem | What it does that matters | Key limitation |
|---|---|---|
| **Apple** | No vendor in the data path, on-device history at enrolment (participants can cap it at 30 days from iOS 27 unless the app holds the Research Entitlement), and SensorKit behavioural signals plus PPG, ECG and accelerometer samples for approved studies | iPhone only; no server API; little study tooling beyond the Study App Template; SensorKit needs per-study Apple approval |
| **Fitbit / Google** | Deepest validation literature, devices among the cheapest, and an existing 59,000-participant *All of Us* dataset | **Legacy API off 30 Oct 2026; Google Health API apparently open to new projects again (C, 2026-10-21)** |
| **Garmin** | Weeks of battery, no subscription required, and Enhanced BBI with per-beat confidence | **New direct access paused (C)**; raw accelerometry only via the enterprise Health SDK; opaque licence terms |
| **Oura** | Nightly RMSSD and temperature deviation from a ring people keep on overnight; best resting HR and HRV agreement in Dial 2025; a research offering with dashboards | Mandatory membership; derived data only; **API Agreement limits retention and bars AI training** |
| **WHOOP** | Charged on the wrist, so no charging gap; screenless | Derived scores only through the API (2023 Unite raw route, status Unclear); **terms bar permanent copies and AI/ML training**; 10-member Sandbox to start |
| **Samsung** | Raw PPG (green, IR, red), raw ECG at 500 Hz, IBI and **raw EDA at 1 Hz (Watch8)** from a mainstream watch, with no Samsung server in the path for sensor data | Galaxy and Android only; partner registration to distribute; Samsung may end the licence without cause on 30 business days' notice; Research Stack status Unclear, no code since Oct 2024 |
| **Polar** | Raw ECG and accelerometry from a $104.95 H10, and 22-bit PPG from Verity Sense, over a free, source-available SDK with no cloud, approval or fee | Session devices, not 24/7 wear; no study tooling; Polar can end the SDK licence on 90 days' notice |
| **Withings** | Cellular devices that remove the participant's phone from the data path; blood pressure, body composition and an under-mattress sleep mat | Raw data ScanWatch-only and by contract; worst Schyvens sleep biases; **Withings+ from 12 Oct 2026** |
| **Empatica** | Raw wrist EDA with an FDA-cleared EDA parameter, and a published-price, self-serve academic plan with study management | Sensor mode fixed per academic account (PPG and EDA only in 2 of 5 modes); no real-time streaming; academic account limited to 1 study and 1 site |
| **Ametris** | The actigraphy reference standard, raw data reprocessable later, regulated-trial operations in 70+ countries | Non-public pricing; corporate transition under Signant |
| **Axivity / GENEActiv** | Open firmware, software and hardware (Axivity), no vendor in the data path (Axivity; GENEActiv by USB), and direct comparability with UK Biobank; AX3 up to 3,200 Hz | Movement, light and temperature only; nothing known until the device is returned, except GENEActiv 1.3 adherence; Activinsights' terms of sale (clause 24) bar publishing about the product without its consent |
| **Movesense** | Custom sensor firmware with no licence cost, 512 Hz ECG, a high-rate IMU (maximum is a vendor conflict), and Class IIa MDR on the MD with certified firmware (custom firmware and Class IIa are alternatives, not a combination) | Proprietary 12-month evaluation licence; small validation base; no FDA clearance; session or multi-day wear (Flash logs up to 5 days of ECG) |
| **Ultrahuman** | Documented raw ring PPG (typically 50 Hz), and ring plus CGM in one API (R) | Raw PPG limited to the developer's own recordings; Ring AIR not sold in the US; API Agreement bars research against Ultrahuman; no validation located |
| **Biostrap / Sensor Bio** | Raw PPG, IBI and accelerometer up to 100 Hz with per-organisation sampling (V2, vendor specification); the leg-worn Activity Pod is legacy | Prices not public; a 15,000 samples/s press claim conflicts with the 100 Hz specification; raw-export tier gating conflicts; validation counts vendor-compiled |
| **Verily Study Watch** | ECG, EDA, PPG and inertial data in one FDA-cleared research device with up to a week of onboard raw storage (C) | Device program wound down 2025; **status conflict (R)** |
| **Labfront** | Published pricing (one of several intermediaries that publish), a free 5-participant tier, EMA at every tier, and higher Garmin resolution via the Health SDK | Garmin, Movesense and Dexcom only; no Fitbit |
| **Fitrockr** | Published per-device pricing across many brands, with Garmin research grants | Vendor compliance claims only (HIPAA "certified" with no certifier; ISO 27001 is the hosting centre's); BAA newly offered 2026-09-19 (R); surveys and raw data are paid add-ons |

---

## Table 11, Study-operations platforms (the layer most vendors do not provide)

| | **Labfront** | **Fitabase** | **Fitrockr** | **Empatica Care Portal** | **Ametris CentrePoint** | **Samsung Research Stack** |
|---|---|---|---|---|---|---|
| Devices | Garmin, Movesense MD, HR2 and Flash, Dexcom G7 | **Fitbit**, Garmin | Claims 700+ wearables incl. Garmin, Fitbit, Apple, Oura, WHOOP, Samsung, Withings, Polar (R) | EmbracePlus, EmbraceMini | LEAP, Insight Watch | Galaxy Watch (Watch5 tested) |
| **Pricing public?** | **Yes** | No | **Yes** | **Yes (academic)** | No | Free, open source |
| Cost | Free (5 participants) / $500 (20) / $1,250 (20, all integrations) per year, + $10–25 per extra participant | Custom quote | From €50/$55 or €150/$165 per month, per device licence (help centre still says user-based; conflict, R) | $1,749.60 per EmbracePlus, 3 years, academic | Not published; CentrePoint ~$3,500/yr (R, competitor source) | $0 plus hosting |
| **EMA / surveys** | **Yes, all tiers** | Engage relaunched April 2026; iPhone app live; general availability not stated | Paid add-on (+20%) | None | Combined Ametris DHT and Signant eCOA offering announced 2026-03-10 (sponsors, CNS trials) | **Yes** |
| Adherence monitoring | Yes | Yes (sync and battery) | Yes (R) | **Yes, live wear-time** | **Yes, near-real-time** | Unclear |
| Multi-site | Yes | Yes | Unclear | Enterprise yes; academic 1 site | **Yes, 70+ countries** | Unclear |
| Sampling resolution | **Raised via Garmin Health SDK partnership**; Advanced tier customisable; Basic has no BBI or accelerometer | Enhanced BBI via Garmin OAuth, during sleep; SDK route via Engage, rate not stated | Accelerometer 25 Hz, gyroscope 32 Hz fixed (add-on); BBI every beat via app sync | Fixed sensor modes | 32–256 Hz | Full SDK control |
| Self-hosting | No | No | On-premise add-on | No | ActiLife 7 local (labelled legacy, still updated 2026-05-08) | **Yes** |
| Free tier to pilot | **Yes** | No | 2-week trial | No | No | **Yes** |
| Maintenance | Active | Active | Active | Active | Active | **No code updates since 24 Oct 2024** |

**Practical read.** A Fitbit study starting now can apparently open its own Google Health API project
again (C, 2026-10-21), but approval needs Google's restricted-scope review and, above 100 users,
verification and CASA. Alternatives are Fitabase or Fitrockr (whether either can add new studies is not stated), or the on-device route
through Apple Health or Health Connect (C). Thryve and Validic need the study's own Google Cloud project and
CASA (C); Terra says it manages the Google Health credentials. A Garmin study cannot currently apply to Garmin directly (C); Labfront and Fitrockr publish
prices, Labfront includes EMA and a free five-participant pilot.

---

## Table 12, Choosing by research question

| If your primary endpoint is... | Use | Avoid | Why |
|---|---|---|---|
| **Physical activity / sedentary behaviour** | Axivity, GENEActiv, Ametris | Any device where energy expenditure is the metric | Raw accelerometry, open pipelines, cohort comparability |
| **Sleep timing / duration (not stages)** | Oura, Apple Watch, Fitbit, research actigraphy | Withings ScanWatch, Garmin Vivosmart 4 for TST | Robbins TST ICC 0.74 (Oura) and 0.85 (Apple); Fitbit TST bias not significant in Schyvens; Schyvens TST bias largest for ScanWatch (+39.9 min) and Vivosmart 4 (+38.4 min) |
| **Sleep architecture (stages)** | Reconsider the design; PSG or ambulatory EEG | **All consumer wearables** | Deep and REM ICC 0.13–0.36 on the best-studied devices |
| **Sleep fragmentation / WASO** | Reconsider; PSG | **All consumer wearables** | Every Schyvens device underestimated WASO by 12–48 min |
| **HRV, nocturnal** | Polar H10, Movesense, Garmin Enhanced BBI (via Labfront Advanced, not Basic, or Fitabase), Oura nightly RMSSD | Devices reporting only an opaque HRV score | Beat-level data or true ECG RR; Oura HRV CCC 0.97–0.99 in Dial 2025 |
| **HRV, daytime / during stressors** | Polar H10, Movesense, Samsung IBI, Garmin Health SDK | Garmin Enhanced BBI via the Health API or Fitabase's API route (captured during sleep); Fitabase's SDK route has unstated daytime coverage | The SDK lists Enhanced BBI for real-time streaming; the API route is sleep-based |
| **Cardiac rhythm / AFib** | Apple Watch ECG, Withings ECG App, Movesense MD, Samsung raw ECG, Verily | Treating irregular-rhythm notifications as the ECG app | Cleared ECG features or raw ECG; notification sensitivity 21.4–72% vs ECG app 94.8% pooled (Apple) |
| **Electrodermal / arousal / stress** | **Empatica**, **Samsung Galaxy Watch8 (1 Hz)**, Verily Study Watch | Everything else | The only raw EDA routes found; wrist EDA agrees poorly with palmar EDA |
| **Energy expenditure** | Indirect calorimetry, doubly labelled water | **Every consumer wearable** | No brand within acceptable limits, six years running |
| **Custom algorithm development** | Movesense, Polar, Samsung, Axivity, Ametris | Oura, WHOOP, Fitbit | Requires documented raw signal (Ultrahuman raw PPG is now documented, own recordings only; Sensor Bio V2 raw export is vendor-documented to 100 Hz, independent validation lacking) |
| **Data retention, deposit or ML training** | Polar BLE, Movesense, Axivity, Samsung Sensor SDK (Samsung may collect service-use information under the licence; the Data SDK and Health Connect routes read the consumer store, used for AI training on opt-in since July 2026), Apple HealthKit (no vendor in the path; SensorKit carries non-public terms) | **WHOOP and Oura APIs** without written agreement | Their API terms limit retention and bar AI/ML training |
| **Large N with no budget** | ***All of Us*** or **UK Biobank** secondary analysis | | Data already collected; no procurement, no API, no exposure to the Fitbit shutoff |
| **Regulated trial endpoint** | Ametris, Empatica, Withings cleared devices | Consumer platforms | Cleared devices and established trial operations |
| **Behaviour-change intervention** | Any consumer device; unified APIs acceptable | | The device is a tool, not an instrument; brand confounding is tolerable |
| **Minimal reactivity** | WHOOP, Oura, Fitbit Air, Ametris, Axivity | Feedback-rich smartwatches | Screenless devices show the participant nothing |
| **Fitbit study starting now** | Fitabase (every participant reauthorizes; 11 of 40 exports pending on 2026-10-14; projects extended to 2027-01-01); on-device collection via Apple Health or Health Connect (C); *All of Us*; the study's own Google Health API project, apparently possible again (C, 2026-10-21) | | Own project needs Google's restricted-scope review and, above 100 users, verification and CASA; legacy API off 30 Oct 2026 |

---

## Table 13, Research programs and academic data access (added 2026-10-10)

| Ecosystem | Program or route | What academics get | User caps | Retention and AI-training terms | Cost | Status (2026-10-10) |
|---|---|---|---|---|---|---|
| **Apple** | **SensorKit**, **Investigator Support Program** (devices and the Study App Template for approved studies, no funding), HealthKit Research Entitlement (iOS 27.1+), Background Health Research Task entitlement; ResearchKit and CareKit are toolkits; Apple Research app runs Apple's own studies only | SensorKit: behavioural sensors, raw accelerometer, PPG and ECG samples (iOS 17.4+), on-device, uploaded by the study app. HealthKit: derived samples; history can be capped at 30 days by participants from iOS 27 unless the app holds the Research Entitlement | None from Apple; Investigator Support Program devices and Study App Template | No Apple cloud copy. SensorKit carries non-public use and handling terms (public sharing barred, R) | $99/yr Developer Program fee, waivable for nonprofits, educational institutions and government | Active; Investigator Support Program takes applications in three cycles a year; ResearchKit pushed 2026-09-23 |
| **Fitbit / Google** | No academic tier. Google Health API with the **Health Research Policy** and **Research Pledge** (both effective 24 Mar 2026); Health Research Attestation | Same data types as commercial developers; no research-only data | 100 users until verification (CASA assessment, $500 to $4,500) | Participants must be told the retention period and how to delete; immediate de-identification; no third-party sharing for new studies without consent; PHI only under an IRB-reviewed HIPAA authorisation. Developer terms name no AI training (Limited Use confines data to the app's user-facing purpose); Google says it has used wearable data to train its own Health AI models, and users can consent to share data for research and product development | No documented API fee | **Not onboarding new projects on 2026-10-10; apparently open again by 2026-10-19 (C), with restricted-scope review. Legacy Fitbit Web API turned off 30 Oct 2026** |
| **Garmin** | No academic programme; Connect Developer Program is "only for business use"; Health SDK for enterprise partners; research grants run by Garmin Health with Fitrockr and with Labfront (Labfront x Garmin Health grant, deadline 2026-11-02); direct institutional deals (KCL EMBRACE, up to 40,000 participants) | Health API summaries, Enhanced BBI, second-level HR during activities; SDK accelerometer and BBI streaming | Not published | Retention per the agreement's SCC annex (account life or deletion request); no AI ban, but brand guidelines require Garmin attribution for AI/ML use; the China-entity agreement (s.15.10) requires an AI transparency statement and consent, and which version binds non-Chinese licensees is Unclear | Programme free; Enhanced BBI licence fee for commercial use; SDK licence or MOQ; whether academic use is "commercial" not stated | **New access requests paused since spring 2026 (C)**. Garmin Health x Fitrockr Asia 2026 grant closed 31 Mar 2026 |
| **Oura** | **Oura for Organizations, "Oura for research"**, plus the Oura Research participant app; public API v2 | Dashboards, group or individual download, "raw data" CSV/JSON export (meaning undefined), "premium metrics" for academics (vendor page) | API: 10 users until Oura approves; none after | **API and MCP Agreement (8 Jun 2026): keep data only as long as strictly necessary; delete within 72 h of a request or on subscription cancellation; no AI/ML training, evaluation or prompting via the API (s.4(d) and s.6(g) have no consent route; user consent cannot lift Prohibited Uses, s.4(c)); benchmarking needs consent; no research carve-out.** Enterprise Platform: participant withdrawal does not affect data already extracted; a Research Agreement is named in the business terms, its terms not public | Membership $69.99/yr per participant (mandatory for API data); API free today, Agreement reserves the right to charge; Enterprise Platform priced per Order, not published | Active |
| **WHOOP** | No named programme; Research Request Intake form; research page invites academic and industry partners, no criteria stated (C); Unite status Unclear | Derived scores only through the API; Unite partners received raw files with RR intervals in 2023 (R) | **Sandbox 10, Build 100, Growth 1,000, Scale 5,000, Production unlimited**; one tier at a time, 50% fill rule, manual review; upgrades reported to take 2 to 3+ months (R) | **Terms (6 Oct 2026): no permanent copies; no AI/ML training or testing; both "unless expressly authorized by the WHOOP Data owner or by applicable law"; no research carve-out** | API no charge; membership $199 to $359/yr (US vendor page, 2026-10-10); research fees not published | Active; intake form live |
| **Samsung** | No academic tier; invitation collaborations (Open Innovation Initiative) and, since June 2026, a sponsor route via Alcedis (Huma) (C); Samsung Partner Program for the Health Sensor SDK; Research Stack (open source) | Raw and processed on-watch signals to the team's own app | None (no Samsung server) | Sensor data none; Samsung may collect service-use information under the licence; partner agreement has no HIPAA, BAA or DPA language | No fee published; licence reserves future fees | Sensor SDK active (v1.4.1, 20 Aug 2025); Research Stack status Unclear, no code since 24 Oct 2024 |
| **Polar** | **Collaboration proposal route** ("Collaborate with us"): research plan of at most 10 pages, budget and support request to research@polar.com, judged partly on value to Polar, reply within two weeks, research agreement if accepted; no published eligibility rule (C) | BLE SDK raw data (Polar limited licence); AccessLink derived data, exercise RR, and watch spot-test ECG and SpO2 (Elixir, beta) | None | BLE SDK: licence ends on 90 days' notice, then SDK copies must be deleted. AccessLink: 30 days' notice or immediate suspension, all Polar data deleted on termination. AI-training terms for licensees not public (C) | SDK free; AccessLink free at present, fees reserved | Active (SDK 8.4.0, 2026-10-01); proposal route open (C) |
| **Withings** | **Advanced Research API** ("for research groups, universities"); **Advanced Biomarkers** plan ("Clinical studies & AI research"); Start for Free | Raw ScanWatch accelerometer and PPG by contract; free plan derived data | Free plan 10 users, more after review | **"AI model training contract" only on Advanced Biomarkers**; partner terms moved to the developer portal in the 13 October 2026 rewrite (not located); participant sharing covers only data after it is enabled; inactive accounts closed after 3, 5 or 10 years (vendor pages conflict) | Free plan, but **Withings+ per new-account participant from 12 Oct 2026**; paid plans custom; "Research partners" exemption terms unpublished | Active |
| **Empatica** | **Academic & Basic Research plan**, self-serve store; 25% academic discount by application (institutional email) | All EmbracePlus and EmbraceMini raw sensor data and a selection of biomarkers; S3 keys; no streaming; no SDK | **1 study, 1 site, 1,000 participants** per academic account | Participant data retained for the service plus 10 years; yearly extensions sold; data retrievable 60 days after termination; continued access may cost extra | EmbracePlus 3-year $1,749.60; EmbraceMini 3-year $1,137.24 (academic) | Active |
| **Ametris** | academic.ametris.com: pricing-list form, grant toolkit, dataset library; academic store for existing accounts; no application step. The Accelerant Partnership Program is for CROs and technology partners, not academics | Same devices and data as sponsors; PPG files "subject to contract restrictions"; CentrePoint API enabled per customer on request | None published for CentrePoint; ActiLife licences by activation tier | Ametris is processor for the study's controller; no fixed retention period published; AI-training terms not public (C); historical raw-file generation may carry fees | Not published; one reseller quote found (Table 7, R) | Active; part of Signant Health |
| **Axivity / GENEActiv** | None needed (Activinsights sells paid, quoted Study Services; no named program) | Full raw signal by USB | None (Activinsights Advanced Sleep Toolkit free to 10 participants) | Axivity: none, it never receives data. Activinsights: 10-year review retention for cloud data; AI-training terms not public; terms of sale clause 24 bars publishing about the product without consent | AX3 from £139, AX6 from £199 (ex VAT); GENEActiv quote | Active |
| **Movesense** | **Movesense Academic Program**: free sensors and accessories for selected projects; review monthly (program page) or weekly (application form), a conflict; up to three projects per quarter; publications must credit Movesense | Same data as any developer | None | None from the vendor on the SDK path; SDK is a 12-month evaluation licence, deployed use may need a separate agreement; the ECG Recorder app backs up anonymised data that Movesense may use for product development and research | Free sensors if selected; MD €349 | **Active** (December 2025 project announced; the page's own list stops at Q1 2023) |
| **Ultrahuman** | No academic programme with terms; Research Institutions partnership, Pulsomics collaboration (raw recordings stay with Ultrahuman), UltraSignal kit, self-serve personal token and OAuth | Raw PPG (own recordings); derived ring and CGM metrics | Not published | API Agreement: data remains Ultrahuman's, storage limited, no redistribution, bars research against Ultrahuman; no AI-training clause (C) | Ring PRO USD 479; API unpaid per the Agreement (R); Heroes pricing for researchers | Live (2026-10-21) |
| **Biostrap / Sensor Bio** | No separate programme; white-label platform by demo | Raw PPG and derived signals (vendor) | Not published | Retention configured per deployment; account deletion within 30 to 90 days; AI-training terms not published | Not public | Rebranded to Sensor Bio |
| **Verily** | Workbench Standard, free and self-serve (beta); Viewpoint by demo for sponsors | Exchange collections including PBHS Limited under a DUA; the device is not procurable | Standard tier 5 workspaces, 5 collaborators each | Privacy policy "as long as necessary"; Workbench trial data deletable at licence expiry; no AI-training clause (Unclear) | Standard free; Professional unpriced | Study Watch status conflict, R (device program wound down 2025) |
| Intermediaries | Labfront grants (three dated 2026 calls) and free Collaborator Program; Fitrockr and Garmin grants; Fitabase quote | See Table 11 | Platform-specific | Thryve stores data 2 weeks (Start Up) or 1 month (Scale Up); Fitrockr Data Vault €250/month for post-project access (R, 2026-10-21; was €150 in July); Terra keeps end-user data about 2 days, 6 months at most | See Tables 7 and 11 | Active |

Rows for Apple, Fitbit/Google, Garmin, Oura, WHOOP, Samsung, Empatica and Withings (batch 1) and
for Polar, Ametris, Axivity / GENEActiv and Movesense (batch 2) were corrected on 2026-10-11 from
the fact records. The generated, quote-backed version of this table is
`../facts/_generated/research-and-access.md`. It covers the batch-1 and batch-2 companies so far. This
hand-written table will be replaced by it once every company has been researched.
