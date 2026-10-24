# Apple Watch / Apple Health / HealthKit / SensorKit

## Quick Facts

| Field | Details |
|---|---|
| Organization | Apple Inc. |
| Category | Consumer smartwatch + OS-level health data framework |
| Current status | Active |
| Platforms/devices | Apple Watch (Series/SE/Ultra lines; Series 12, SE 3 and Ultra 4 on sale in the US store, 2026-10-10), iPhone; data surfaced through the Health app on iOS |
| Open source | No (ResearchKit and CareKit are open source; HealthKit, SensorKit, watchOS are not) |
| Hosting/deployment | On-device HealthKit store on iPhone; **no Apple-operated cloud API for researchers**. Any cloud pipeline must be built by the research team inside their own iOS app. |
| Pricing model | Device purchase (US from 249 USD SE 3, 399 USD Series 12, 799 USD Ultra 4) plus the 99 USD annual Apple Developer Program fee, which approved nonprofits, accredited educational institutions and government entities can have waived; no subscription required for HealthKit data; no API fee. Approved studies can receive devices free through the Investigator Support Program. |
| Last verified | 2026-10-11 (vendor fact record); earlier passes 2026-08-21; ECG voltage access re-verified 2026-10-09; SensorKit sensor list, entitlement and Research app studies re-verified 2026-10-10; Cohen 2026 author disclosures read 2026-10-10 |

## Summary

- Apple is the single largest consumer wearable ecosystem, but it is architecturally the *least* like the other platforms in this module. There is no Apple server-side research API. Apple does not host participant data for researchers and does not offer an OAuth endpoint a researcher can call to pull a cohort's data. Instead, HealthKit is an **on-device datastore on the participant's iPhone**, and the only supported way to get data out at scale is to ship an iOS app (built by the research team or a vendor) that the participant installs, grants read permission to, and which then uploads to infrastructure the research team controls.

- This has two consequences that dominate every design decision:

1. **Data custody is favourable.** Because Apple is not in the loop, there is no vendor data-sharing agreement, no vendor rate limit, and no vendor retention policy on the research copy of the data. The researcher's own backend is the system of record. This holds for HealthKit. SensorKit is different, because its entitlement carries additional non-public use and handling terms (see Privacy).
2. **Engineering burden is high.** There is no "sign up, get a token, pull JSON" path. A study needs an iOS app, an Apple Developer account, App Store (or TestFlight/enterprise) distribution, and a backend. This is why Module 2 platforms (mindLAMP, Beiwe, RADAR-base, Ethica) and commercial middleware exist, they supply that app layer. Apple's own Study App Template lowers this burden for approved Investigator Support Program applicants. Apple says it needs "minimal to no coding" [14][17].

- A second, separate framework, **SensorKit**, exposes lower-level iPhone/Watch signals but is *explicitly restricted to research use* and requires a private entitlement approved by Apple per study. Its current sensor list (Apple documentation, Verified 2026-10-10) includes **photoplethysmogram and electrocardiogram sample streams (iOS 17.4+) and raw accelerometer (iOS 14+)**, so raw PPG is available from Apple, but only to Apple-approved studies and with an undocumented capture schedule and rate.

## Products / Platform Architecture

- Several distinct access surfaces, frequently conflated:

| Surface | What it is | Who can use it | Access mechanism |
|---|---|---|---|
| **HealthKit** | On-device health datastore; aggregates Watch, iPhone, and third-party app/device writes | Any iOS developer, for health, motion or fitness purposes | In-app API, per-type user permission |
| **Core Motion** | Motion sensor APIs, including `CMSensorRecorder` (50 Hz accelerometer archive) and workout-only batched sensors (800 Hz accelerometer, 200 Hz device motion) | Any iOS/watchOS developer | In-app API, motion usage permission; no research entitlement |
| **SensorKit** | Lower-level behavioural/ambient sensing from iPhone + Watch | Researchers only | Private entitlement, per-study Apple review, IRB approval required |
| **HealthKit Research Entitlement** | Removes the participant's 30-day history limit option and reduces access reminders (iOS 27.1+). Does not gate data types. | Health research apps, one unique study, IRB/IEC approval | Request by the Developer Program Account Holder, granted per bundle ID |
| **Background Health Research Task entitlement** | Lets a research app process HealthKit, SensorKit or Bluetooth device data in the background (iOS 17.1+) | Research apps that intend to publish findings, with IRB/IEC approval | Requested through the Investigator Support Program application |
| **Investigator Support Program** | Apple devices (mostly Apple Watch; Vision Pro and AirPods Pro where available) and app resources, including the Study App Template. No funding. | Approved studies | Application by email, three review cycles a year |
| **Health app export** | User-initiated export of the whole HealthKit store | The participant themselves | XML inside `Export.zip` (`apple_health_export/Export.xml`) |
| **Apple Research app** | Apple's own first-party study platform (as of 2026-10-10: Apple Health Study, Apple Women's Health Study, Apple Hearing Study) | Apple + named academic partners only | Not open to third parties |

- **ResearchKit** and **CareKit** are open-source frameworks Apple publishes for building consent flows, surveys, and active tasks in a study app. They are *app-building* toolkits, not data-access mechanisms, and they do not by themselves grant any additional data.

## Sensors and Data Streams

- Every Module 1 profile uses the same table so devices can be compared row by row. Rows are the sensors named in `CLAUDE.md`. "Present" is about the hardware; "Researcher access" is about what a study can actually obtain, which is the module's central question. "Unclear" means nothing current was verified. The convention is recorded in [`../../shared/profile-table-conventions.md`](../../shared/profile-table-conventions.md).

| Sensor | Present | Researcher access to underlying signal | Resolution or sampling | Notes |
|---|---|---|---|---|
| PPG | Yes | HealthKit: no raw PPG, derived HR and heartbeat series only. **SensorKit (research entitlement): `SRSensor.photoplethysmogram` "streams sample PPG sensor data" (optical, accelerometer and temperature samples per `SRPhotoplethysmogramSample`), iOS 17.4+.** | Derived (HealthKit); SensorKit rate not documented | Each SensorKit PPG sample carries a `usage` value (background system, deep breathing, foreground blood oxygen, foreground heart rate), so capture is tied to those contexts; the schedule and rate are not stated. Verified 2026-10-10 (Apple documentation JSON). |
| ECG | Series 4 and later, Ultra, region-gated | The voltage waveform of each recorded ECG. `HKElectrocardiogramQuery` returns each voltage measurement of a stored `HKElectrocardiogram` sample (Apple Developer docs, verified 2026-10-09). Whether that waveform counts as raw is in conflict, see Notes. SensorKit also lists `SRSensor.electrocardiogram`, "streams sample ECG sensor data", iOS 17.4+ (Verified 2026-10-10). No continuous ECG exists to read. | Single lead (Lead I-like), sampling frequency stored per sample | On-demand 30-second recordings only. **Conflict, Unclear (vendor fact record, 2026-10-10).** Apple's research FAQ says "You cannot access raw ECG data through HealthKit" [2]. Apple's HealthKit docs describe the per-lead voltage measurements [10]. Neither page defines "raw". Access to the voltages is not in dispute. Whether they are unfiltered sensor output or processed by the ECG app is. SensorKit's ECG sensor is the route Apple itself frames as sensor data. Ask Apple before calling the HealthKit waveform raw in a protocol. |
| Accelerometer | Yes | Not via HealthKit. Core Motion `CMSensorRecorder` (iOS 9+, watchOS 2+, not deprecated) has the system record 50 Hz accelerometer for up to 12 hours per call, even while the app is suspended or terminated. The data stays readable for up to three days. It needs only the motion usage permission, no entitlement [18]. Core Motion batched sensor APIs give 800 Hz during an active HealthKit workout session [19]. **SensorKit `accelerometer` (iOS 14+) and `rotationRate` under the research entitlement.** | 50 Hz (`CMSensorRecorder`); 800 Hz in workouts; SensorKit rate not stated | `CMMotionManager` for live in-app data. Verified 2026-10-10 (vendor fact record). |
| Gyroscope | Yes | Core Motion in-app via `CMMotionManager`. 200 Hz device motion through Core Motion batched sensor APIs during an active HealthKit workout session [19]. SensorKit `rotationRate` under the research entitlement. | 200 Hz device motion in workouts; otherwise Core Motion rates |  |
| Magnetometer | Unclear | Unclear | Unclear |  |
| Temperature | Series 8 and later, Ultra | HealthKit: derived sleeping-wrist temperature deviation, not a raw trace. SensorKit `wristTemperature` (iOS 17.0+) "provides wrist temperature while the user sleeps". | Nightly |  |
| SpO2 | Series 6 and later, Ultra | Blood oxygen samples where the feature is enabled. | Periodic | Since August 2025, Blood Oxygen on affected US units is calculated on the paired iPhone and shown in the Health app's Respiratory section [21]. Whether those samples reach HealthKit the same way was not checked. |
| GPS | Yes on GPS models | Route data via `HKWorkoutRoute` for workouts. | Workout routes |  |
| Barometer / altimeter | Yes | Derived flights climbed and elevation. | Derived |  |
| EDA | No | Not applicable | Not applicable | A real gap against Empatica for stress and arousal work. |
| Ambient light | iPhone, and Watch wear detection via SensorKit | SensorKit only | Unclear |  |
| Other | Unclear | Unclear | Unclear | Not verified against current documentation. |

**Verification.** PPG, ECG, accelerometer and temperature rows re-checked 2026-10-10 against Apple's SensorKit documentation, read through the `developer.apple.com/tutorials/data/documentation/sensorkit/*.json` endpoint (**Verified**). Other rows Corroborated: the 2026-08-21 pass could not render Apple's JavaScript documentation and drew on developer forum threads, the ResearchKit and CareKit consortium FAQ and published studies, per the notes below. ECG, accelerometer, gyroscope and SpO2 rows corrected 2026-10-11 against the vendor fact record (`facts/apple.yaml`).

### Notes from earlier verification passes

- Sensor complement varies substantially by Watch model and generation; check the specific SKU before assuming availability.

| Sensor | Present on Apple Watch (recent models) | Researcher access to underlying signal |
|---|---|---|
| PPG (optical heart) | Yes | **No raw PPG.** Only derived HR samples and heartbeat series. |
| ECG (single-lead) | Series 4+ / Ultra (region-gated) | `HKElectrocardiogram` samples. Access to per-sample **voltage** was recorded as disputed in the first pass; resolved 2026-10-09 in favour of access for recorded ECGs. Superseded 2026-10-11. Voltage access is not in dispute, but whether the waveform is raw is (see the table above and Open Questions). |
| Accelerometer | Yes | Not via HealthKit. Available in-app on watchOS via Core Motion (`CMMotionManager`, and `CMSensorRecorder`) while the app runs. Superseded 2026-10-11. `CMSensorRecorder` is current and records while the app is suspended or terminated (see the table above). |
| Gyroscope | Yes | Same as accelerometer, Core Motion, in-app only. Superseded 2026-10-11 (200 Hz device motion in workouts, see the table above). |
| Temperature (wrist) | Series 8+ / Ultra | Derived sleeping-wrist-temperature deviation; not a raw stream. |
| SpO2 | Series 6+ / Ultra, with a US availability disruption from a patent dispute (superseded 2026-10-11, see the table above) | Blood oxygen samples where the feature is enabled. |
| GPS | Yes (GPS models) | Route data via `HKWorkoutRoute` for workouts. |
| Barometer/altimeter | Yes | Derived flights climbed / elevation. |
| EDA | **No** | n/a, Apple Watch has no EDA sensor. This is a real gap versus Empatica for stress/arousal work. |
| Ambient light | iPhone (and Watch via SensorKit wear detection) | SensorKit only. |

- **Status: Corroborated.** Apple's developer documentation is JavaScript-rendered and was not directly retrievable during this session; the sensor/API mapping above is drawn from Apple developer forum threads, the ResearchKit/CareKit consortium FAQ (an Apple-affiliated resource), and secondary developer documentation. Re-verify against `developer.apple.com/documentation/healthkit` before publishing any consequential claim.

## Derived Metrics / Analytics

- HealthKit organises data as **quantity types** (numeric + unit, e.g. heart rate, steps, distance), **category types** (enumerated, e.g. sleep analysis stages), **characteristic types** (stable traits, e.g. date of birth, biological sex), **correlation types** (grouped samples, e.g. blood pressure), plus specialised types for workouts and ECG.

- Commonly used research-relevant outputs include: heart rate, resting heart rate, walking heart rate average, heart rate variability (SDNN), respiratory rate, sleep analysis with stages, step count, distance, active/basal energy, exercise minutes, stand hours, VO2max (cardio fitness), wrist temperature deviation, blood oxygen, and a family of mobility metrics (walking speed, step length, double support time, walking asymmetry, six-minute walk distance).

- Two nuances that matter for analysis:

- **HRV is SDNN, not RMSSD.** Apple's `heartRateVariabilitySDNN` is computed over ~60-second windows and sampled opportunistically (mostly during Breathe/Mindfulness sessions and irregularly through the day). It is not a continuous nocturnal RMSSD comparable to Oura's or WHOOP's headline HRV. Cross-device HRV comparison without this caveat is a methodological error.
- **Sampling is opportunistic and irregular.** Apple says higher-frequency heart rate is in HealthKit for samples collected during workouts and ECG sessions [2]. Apple also says Series 12 takes background heart rate readings every five seconds and measures HRV as often as every five minutes [20]. That is a device-side marketing figure. Whether HealthKit receives that cadence is not documented, and neither is whether Series 12 HRV is still SDNN. Missingness is structured, not random.

- `HKHeartbeatSeriesSample` stores the precise timestamps of individual heartbeats, which is the closest thing to beat-to-beat/IBI data in the ecosystem. It is generated during specific contexts (notably ECG sessions and some workout/breathe contexts) rather than continuously. Real-time heartbeat data is not available [2].

- Core Motion has a `CMHighFrequencyHeartRateData` class for heart rate collected at 1 Hz (watchOS 10+) [18]. When and how it is delivered was not checked.

- Core Motion's `CMMovementDisorderManager` gives resting Parkinsonian tremor (3 to 7 Hz) and choreiform dyskinesia measures. It needs an Apple entitlement, and Apple limits it to clinically diagnosed patients [18].

- Recent HealthKit additions include medications and menopause samples [19].

## Active Data Collection

- No native survey/EMA capability in HealthKit. ResearchKit provides open-source survey, informed-consent, and active-task modules (including validated-style tasks such as tapping speed, gait and balance, spatial memory, and audio tasks) that a study app can embed. Notifications are handled through standard iOS mechanisms.

## Researcher and Study Management Features

- **Little provided by Apple to third parties.** There is no Apple-run enrolment portal, adherence dashboard, participant roster, or device-management console for external researchers.
- The exception is the **Study App Template**. Apple gives it free to approved Investigator Support Program applicants. Apple says it needs "minimal to no coding" to build a study data collection app, and it exports collected data to the researcher's servers with built-in encryption [14][17]. Which monitoring or roster functions it includes was not checked. Anything it lacks must be built or bought.

- Apple's own Research app does provide these functions, but it is Apple's internal study platform for Apple-run studies with selected academic collaborators. As of 2026-10-10 Apple's Research app page lists the **Apple Health Study** ("Initiated in early 2025", continuing Apple's partnership with Brigham and Women's Hospital), the **Apple Women's Health Study** (with the Harvard T.H. Chan School of Public Health and NIEHS) and the **Apple Hearing Study** (with the University of Michigan). The earlier Apple Heart and Movement Study is no longer listed there. Its data collection has ended, and participants are invited to the Apple Health Study, which does not require an Apple Watch (Brigham and Women's study site, Corroborated) [26]. It is not a service researchers can procure.

## Data Access and Export

| Route | Mechanism | Granularity | Practical notes |
|---|---|---|---|
| Custom iOS app | HealthKit read authorisation, per data type | Sample-level, as stored | The only scalable route. Requires the participant to have an iPhone and to install and authorise the app. |
| SensorKit | Private entitlement (`com.apple.developer.sensorkit.reader.allow`) + IRB | Sample-level behavioural and ambient data, plus raw accelerometer, PPG and ECG sample streams | Research-only; per-study Apple approval; on-device, then uploaded by the study app. 7 days of prior data per active sensor, after a 24-hour holding period on new data [27]. |
| Core Motion `CMSensorRecorder` | In-app API, motion usage permission | 50 Hz accelerometer | Up to 12 hours per recording call, kept for up to three days. The app must read it before it expires [18]. |
| Study App Template | Apple study app for approved Investigator Support Program applicants | As collected by the template | Exports to the researcher's servers with built-in encryption [17]. |
| HealthKit clinical records | In-app API | FHIR resources from connected providers | The study app can read them from the HealthKit store [27]. |
| Participant self-export | Health app → Export All Health Data | Full store, sample-level | XML in a zip. Workable for small N or as a backstop; unwieldy at scale (files are large and the format is verbose). |
| Third-party middleware | Vendors that ship an SDK/app wrapping HealthKit | Varies | Shifts the engineering burden but adds a data processor to the IRB/DPA. |

- **Permission asymmetry is a documented trap:** HealthKit read permissions are deliberately opaque. An app cannot tell whether the user granted or denied *read* access to a type, a denied type simply returns no data, which is indistinguishable from a user who has no data of that type. Studies must therefore verify data flow empirically per participant rather than trusting a permissions check.

- **iOS 27 history limit.** From iOS 27, participants can limit an app's HealthKit read access to the past 30 days and get periodic reminders to review or revoke access. Research apps can apply for the HealthKit Research Entitlement (iOS 27.1+). New permission requests from those apps do not offer the 30-day option, and participants get fewer reminders [15]. Without the entitlement, HealthKit history goes back to a systemwide earliest permitted date. Old data is also periodically purged from Apple Watch itself [27].

## APIs, SDKs, and Extensibility

- HealthKit (iOS/watchOS), Core Motion, ResearchKit, CareKit, SensorKit.
- **No public server-to-server API. No OAuth. No bulk cohort export. No webhooks.** This is the defining constraint of the ecosystem.
- Apple Watch third-party apps run on watchOS with meaningful background-execution limits; continuous high-rate sensor capture on-watch is constrained by both OS policy and battery.
- Research apps can apply for the **Background Health Research Task entitlement** (iOS 17.1+). It lets the app process HealthKit, SensorKit or Bluetooth device data in the background. It is requested through the Investigator Support Program application. The study must have IRB or IEC approval and intend to make its findings public [16].
- There are no API rate limits, because HealthKit and SensorKit have no Apple-hosted web API. The practical limits are SensorKit's 7-day lookback and 24-hour hold, `CMSensorRecorder`'s 12-hour recordings and 3-day retention, and iOS background execution.

### SensorKit specifics

- Data categories in the current `SRSensor` list (developer.apple.com, read 2026-10-10, **Verified**): accelerometer, rotation rate, ambient light, ambient pressure, pedometer data, odometer, visits, device usage report, keyboard metrics, messages usage report, phone usage report, media events, face metrics, Siri speech metrics, telephony speech metrics, headphone motion, headphone settings, acoustic settings, on-wrist state, heart rate (iOS 17.0+), **electrocardiogram and photoplethysmogram (iOS 17.4+)**, wrist temperature (iOS 17.0+) and sleep sessions (listed from iOS 26.0). The 2026-08-21 list (ambient light, device usage, keyboard metrics, message metadata, call logs, visits and wear detection) came from the ResearchKit and CareKit consortium page and was incomplete. Watch-derived sensors need a paired Apple Watch.

- Access process, as documented by the ResearchKit & CareKit consortium:
- Submit a research proposal to `sensorkitrequest@apple.com`
- Pass Apple's review criteria
- Hold IRB / ethics board approval
- Accept additional terms and conditions
- **The submitting developer account must belong to the researcher or their institution**, an outside contractor cannot submit under their own account
- Apple first grants a development entitlement. The distribution entitlement follows once the study has IRB (or comparable) approval and is ready to launch. Standard App Store review still applies [1].

- Documented constraints: entitlement review can delay development; participants may decline to share these more sensitive streams; background execution is limited when the user is not interacting with the app; and data volumes are large enough to require deliberate storage planning.
- An app can read only 7 days of prior data for an active sensor. Newly recorded data is held for 24 hours before the app can read it, which gives the participant a chance to delete it [27].

- **Entitlement mechanics (Apple documentation, Verified 2026-10-10):** the entitlement `com.apple.developer.sensorkit.reader.allow` is "the necessary entitlement to access sensor data that's required by your app's preapproved research study". A team submits its study to Apple; if Apple approves it, the team can create a provisioning profile that signs the app with this entitlement, and the system closes an app whose code signature lacks it. Data are read on a per-team basis.

### Research program and academic data access (added 2026-10-10)

- **SensorKit is Apple's only research-specific data framework.** It is one of several research-specific routes open to outside teams (below). It is free beyond the Apple Developer Program fee, requires per-study approval by Apple and IRB approval, and yields on-device data that the study's own app uploads: behavioural sensors, raw accelerometer, and (iOS 17.4+) PPG and ECG sample streams. Rates and capture schedule are not documented. There is no Apple cloud copy or rate limit in the study's path. The entitlement does carry additional non-public use and handling terms. Funk et al. 2025 report that these bar public sharing of SensorKit data (Reported, from the paper's data availability statement) [1][24].
- **Investigator Support Program.** Apple awards devices, mostly Apple Watch, with Vision Pro and AirPods Pro where available, plus app development resources including the Study App Template. It provides no sponsorship or funding [14].
  - Proposals are judged on study design, product availability, use of Apple products and frameworks, feasibility and impact.
  - The institution must sign an Investigator Support Program Agreement and show ethics board approval before devices are awarded.
  - Applications go by email to research_proposals@apple.com. There are three review cycles a year, due January 5, April 5 and September 5. Decisions typically come 6 to 8 weeks after the due date.
  - There is no fixed device limit, but supply is limited and the quantity must be justified.
  - Awardees owe quarterly status reports and details of planned publications.
  - SensorKit data still needs its own entitlement request.
- **HealthKit Research Entitlement** (iOS 27.1+). It removes the 30-day history option from new permission requests and reduces reminders. It does not gate access to data types. It requires IRB or IEC approval and an app built exclusively for one health research study, and is granted per bundle ID [15].
- **Background Health Research Task entitlement** (iOS 17.1+), see APIs above [16].
- **HealthKit** is the same for academics and everyone else: derived samples, through a researcher-built iOS app, with no cloud API. From iOS 27 participants can limit an app to the past 30 days of history unless the app holds the HealthKit Research Entitlement [15].
- **ResearchKit and CareKit** are open-source toolkits, not data programmes.
- **The Apple Research app** runs Apple's own studies with named partners and cannot be procured by outside teams.
- **Active:** yes. The Investigator Support Program is accepting applications in three cycles a year and recently added Vision Pro and AirPods Pro [14]. The HealthKit Research Entitlement is new and requires iOS 27.1 [15]. Apple Heart and Movement Study data collection has ended [26]. SensorKit sensors were last extended in iOS 17.4 and iOS 26 (sleep sessions); the ResearchKit GitHub repository was last pushed 2026-09-23, latest release 3.2.0 on 2025-09-19 (GitHub API, 2026-10-10).

## Deployment and Infrastructure

- Entirely the research team's responsibility: iOS app development and maintenance, Apple Developer Program membership, App Store review (which applies *in addition to* SensorKit entitlement approval), distribution (public App Store, TestFlight, or Apple Business/Enterprise), and a backend for ingest and storage.
- App Review Guideline 5.1.3 requires any app conducting health-related human subject research to have independent ethics board approval [25].

## Participant Experience

- **Requires an iPhone.** This is the largest single feasibility constraint, it excludes Android users entirely and, in most countries, biases the sample toward higher socioeconomic status. Mixed-OS studies cannot use Apple Watch as a common device.
- Battery life on non-Ultra models is roughly a day, meaning **daily charging**. This creates a systematic gap in 24h coverage and forces a choice between nocturnal sleep data and daytime completeness unless charging is scheduled deliberately (a common protocol is charging during a fixed daily routine such as showering).
- Data syncs from Watch to iPhone automatically over Bluetooth/Wi-Fi; the Watch buffers when the phone is absent.
- Wear compliance is generally high because the device is a mainstream consumer product participants may already own and want to wear.

## Privacy, Security, and Compliance

- HealthKit data is stored in an encrypted on-device store; Apple's documented position is that HealthKit data is encrypted at rest on device and that apps may not use HealthKit data for advertising or sell it to data brokers.
- HealthKit data is stored locally on the device. Health data synced to iCloud is end-to-end encrypted, and Apple does not hold the keys [28].
- Because Apple does not receive the study's copy of the data, **HIPAA/GDPR analysis attaches to the research team's own infrastructure**, not to Apple. There is no Apple BAA or DPA to negotiate for the HealthKit path. This is a genuine structural advantage over API-mediated platforms.
- **No BAA is offered.** Apple's developer licence agreement bars using Apple software or services in any way that would make Apple a business associate. The iCloud terms bar using iCloud for protected health information [25]. Corroborated.
- **No DPA is published** for HealthKit, SensorKit or researcher use (not public, checked 2026-10-10). Apple does not receive study data on these routes.
- **SensorKit is the exception to "nothing to negotiate".** Its entitlement requires agreeing to additional terms on use and handling, and those terms are not public [1]. See the Funk et al. 2025 report on public sharing above [24].
- App Store review enforces health-data-specific policies (purpose strings, no advertising use, no selling of health data). Apps may not store personal health information in iCloud. No retention period is published [25].
- The developer licence agreement requires the developer to bar anyone receiving de-identified or coded data from re-identifying participants without consent [25].
- **AI and model training.** HealthKit data may be used only for health, motion or fitness services, or for health research with permission. Sharing personal data with third-party AI needs clear disclosure and explicit permission. No term found names model training of health data. Corroborated, since part of this is an absence finding [25].
- **Certifications.** ISO/IEC 27001 and 27018 cover listed Apple internet services including iCloud, with annual registrar attestation (Corroborated, certificate not retrieved). HealthKit and SensorKit are on-device frameworks and are not listed. No SOC 2 report for HealthKit, iCloud Health or the Research app was found (not public, 2026-10-10) [28].
- **GDPR.** For Apple's own services, EEA, UK and Swiss personal data is controlled by Apple Distribution International Limited in Ireland, with Standard Contractual Clauses for transfers. Study data collected through HealthKit is the researcher's responsibility [28].
- Apple says Research app data is stored in an Apple system designed to meet HIPAA technical safeguards. That covers Apple's own studies only [12].
- **FDA (openFDA, 12 records for applicant "Apple, Inc.", 2026-10-10)** [23].
  - ECG app. De Novo DEN180044 (2018-09-11) and 510(k) K201525 (2020-10-08, ECG app 2.0).
  - Irregular Rhythm Notification. De Novo DEN180042 (2018-09-11), 510(k) K212516 (2021-10-22) and K231173 (2023-07-21).
  - AFib History. 510(k) K213971 (2022-06-03). FDA has also qualified it as a Medical Device Development Tool, a biomarker test for AFib burden as a secondary endpoint in cardiac ablation device studies. That is a qualification, not a clearance.
  - Sleep Apnea Notification. 510(k) K240929 (2024-09-13).
  - Hypertension Notification. 510(k) K250507 (2025-09-11).
  - Not Apple Watch. Hearing Aid Feature for AirPods Pro, De Novo DEN230081 (2024-09-12). Digital Prism Correction, K242058 (2024-10-21) and K250143 (2025-06-23). Medical Imaging Calibration, K253582 (2026-04-01).

- **Do not infer** that using an Apple device makes a study HIPAA-compliant. Compliance is entirely a property of the study's own stack.

## Pricing

- No API fee, no per-call or per-participant fee, no research programme fee, no subscription needed for HealthKit data. ResearchKit, CareKit and (for approved applicants) the Study App Template are free [14][17].
- Costs are: device hardware, the Apple Developer Program annual fee, and, usually dominant, the engineering cost of building and maintaining the study app and backend.
- Device prices in the US store (2026-10-10) start at 249 USD for SE 3, 399 USD for Series 12 and 799 USD for Ultra 4. No education or research device discount was found [22].
- The Developer Program costs 99 USD per membership year. Approved nonprofits, accredited educational institutions and government entities can have the fee waived [22].
- Approved studies can receive devices free through the Investigator Support Program. It provides no funding [14].
- No device minimum or contract term is published, and no quote is needed. Investigator Support Program awardees owe quarterly status reports.
- Apple Fitness+ (workout content, optional) is 9.99 USD a month or 79.99 USD a year after a free month. It is not needed for health data [22].
- Because participants often already own an Apple Watch, BYOD designs can eliminate device cost entirely, at the price of device-generation heterogeneity in the sample.

## Research Evidence and Validation

- **Heart rate:** Apple Watch is among the better-validated consumer optical HR devices. A widely cited systematic review of steps, energy expenditure, and heart rate across commercial wearables found Apple among the most accurate brands for heart rate, with all major brands within roughly ±3% on average under controlled conditions.
- **Steps:** high validity in laboratory settings; free-living accuracy is materially worse across all brands.
- **Energy expenditure:** poor. The same review reported that **no brand** met acceptable accuracy limits for energy expenditure, with mean absolute percentage error above 30%. Energy expenditure from any consumer wearable should be treated as unsuitable for a primary endpoint.
- **Sleep staging:** mixed and study-dependent.
  - Chinoy-style single-night lab comparisons place Apple Watch competitively: in a 2024 Brigham and Women's Hospital study (n=35, funded by Oura but independently conducted and published in *Sensors*), four-stage sensitivity was 50.5 to 86.1% and precision 72.7 to 87.8% for Apple, versus 76.0 to 79.5% / 77.0 to 79.5% for Oura and 61.7 to 78.0% / 72.8 to 73.2% for Fitbit, i.e. Apple had the widest spread, strong on some stages and weak on others, while Oura was the most uniformly accurate. **Note the funding source when citing this.**
  - An independent 2025 six-device validation (Schyvens et al., *SLEEP Advances*, n=62) reported markedly lower agreement for most devices, with Apple Watch Series 8 first on overall four-stage agreement (κ 0.53) and WHOOP 4.0 fourth (κ 0.37). The often-quoted ~69.6% (WHOOP) and ~50.7% (Apple) are deep-sleep classification accuracies, not overall agreement (corrected 2026-10-09; see `validation-evidence.md`). Most devices differed significantly from PSG on total sleep time, sleep efficiency, WASO, and light sleep.
- **Hypertension notifications (added 2026-10-09):** validation exists only as vendor documents, Apple's September 2025 white paper and FDA 510(k) summary K250507 (cleared 2025-09-11). Pivotal study: 2,229 enrolled, 1,863 analysed, 30 days vs an FDA-cleared home cuff; sensitivity 41.2% (95% CI 37.2 to 45.3), specificity 92.3% (90.6 to 93.7), stage 2 sensitivity 53.7%; lower sensitivity under age 60 and at BMI ≤30; Fitzpatrick V-VI subgroup not significantly different. No peer-reviewed publication of the pivotal study located (PubMed, Europe PMC, 2026-10-09). Independent critique: Cohen et al. 2026, "Apple Watch for Hypertension Screening", *Hypertension* (DOI 10.1161/HYPERTENSIONAHA.125.26031), and a population-impact model, Cohen et al. 2026, "Impact of a Smartwatch Hypertension Notification Feature for Population Screening", *JAMA* (DOI 10.1001/jama.2025.26925); titles and DOIs confirmed in Europe PMC 2026-10-10. Author disclosures for the *Hypertension* critique were read 2026-10-10 in the NIH author manuscript (PMC12826266): two of six authors disclose Apple stock, S.P. Juraschek under $10k and E. Yang over $10k; a third, A.E. Schutte, discloses honoraria and advisory roles with other blood-pressure device makers including Omron and Aktiia. JAMA paper disclosures not read. **Verified** (FDA and Apple documents read).
- **SpO2 (added 2026-10-09):** Walzel et al. 2023 (*Sensors* 23(22):9164, independent): Apple Watch 8 had the lowest bias of three smartwatches vs Masimo Radical-7 under induced hypoxemia. Jiang et al. 2026 (*JMIR Form Res* 10:e85253): Apple Watch Series 7 Arms 5.82% below 88% SaO2 vs arterial blood gas, with overestimation. **Corroborated.**
  - These two results are not reconcilable as a simple ranking; they differ in device generation, sample, and scoring approach. Treat consumer sleep *staging* as exploratory and consumer sleep *timing/duration* as more defensible.
- A living systematic review and meta-analysis of Apple Watch accuracy has been published in *npj Digital Medicine* (2025) and is the best single entry point to this literature; it was paywall-gated during this session and its numbers have not been extracted here.

## Strengths

- Largest installed base of any research-relevant wearable, enabling low-cost BYOD recruitment.
- Best-in-class or near-best-in-class heart rate accuracy among consumer wrist devices.
- Rich, standardised, cross-app data model, HealthKit aggregates third-party devices and apps, so a single integration can capture data originating from non-Apple hardware.
- No vendor sits between the researcher and the data: no rate limits, no vendor retention policy, no data-processing agreement with Apple for the study copy. This holds for HealthKit. SensorKit carries additional non-public use and handling terms.
- Several research-specific routes beyond SensorKit. These are free devices and the Study App Template through the Investigator Support Program, the HealthKit Research Entitlement, and the Background Health Research Task entitlement.
- A 50 Hz background accelerometer archive through Core Motion `CMSensorRecorder` with no research entitlement.
- ECG and mobility metrics that most competitors lack.
- SensorKit offers behavioural/ambient signals unavailable anywhere else on iOS, and (iOS 17.4+) PPG and ECG sample streams, to approved studies.
- Strong participant acceptability and wear compliance.

## Limitations

- **No server API and little study-management tooling**, the highest engineering barrier of any platform in this module. The Study App Template, for approved Investigator Support Program applicants, is the one Apple-supplied shortcut.
- **iPhone-only**, which is a hard exclusion criterion, not an inconvenience.
- **No raw PPG and no raw accelerometer through HealthKit.** SensorKit does expose PPG, ECG and accelerometer samples, but only under a per-study Apple entitlement, with an undocumented capture schedule and rate. Core Motion `CMSensorRecorder` does keep a retrospective 50 Hz accelerometer archive with no entitlement. Each recording lasts at most 12 hours and expires after three days, so the app must keep restarting and collecting it. That makes it less turnkey than ActiGraph/Ametris.
- From iOS 27, participants can cap HealthKit history at 30 days unless the app holds the HealthKit Research Entitlement. SensorKit only ever looks back 7 days.
- HRV is SDNN on an opportunistic sampling schedule, not comparable to competitors' nocturnal HRV without careful handling.
- Daily charging burden creates structured missingness.
- No EDA sensor.
- Sleep staging validity is contested; energy expenditure is not fit for purpose.
- Sensor availability and feature enablement vary by model, region, and regulatory status, so a heterogeneous BYOD cohort will have heterogeneous data.

## Best-Fit Use Cases

- Large BYOD cohorts where participants already own the hardware and the team can fund app development.
- Cardiovascular and physical-activity research where HR accuracy and workout/route data matter.
- Studies that require the research team to hold sole custody of the data.
- Studies needing an integrated active (survey/task) and passive design on iOS, pairing ResearchKit with HealthKit.
- Behavioural/digital-phenotyping work on iOS where SensorKit's streams are the actual scientific target and the team can carry the entitlement process.

## Poor-Fit Use Cases

- Any study requiring Android inclusion on a single device platform.
- Studies needing raw PPG without going through Apple's per-study SensorKit approval. (50 Hz accelerometry is available without approval through `CMSensorRecorder`, in repeated 12-hour recordings that must be read within three days.)
- Small studies without software engineering capacity and without budget for middleware, unless they win Investigator Support Program support and use the Study App Template.
- Energy expenditure as a primary endpoint.
- Clinical sleep-staging endpoints.
- Fast-turnaround studies, SensorKit entitlement plus App Store review is a multi-month critical path.

## Open Questions

- **Whether the HealthKit ECG waveform counts as raw. Conflict, Unclear (vendor fact record, 2026-10-10).** Access to the voltages is Verified. Apple's research FAQ still says "You cannot access raw ECG data through HealthKit" [2], and neither Apple page defines "raw". The open point is whether the voltages are filtered or otherwise processed by the ECG app before storage. One question to Apple (sensorkitrequest@apple.com or the researchandcare.org FAQ contact) would settle it. Until then, do not call the HealthKit waveform raw in a protocol. The 2026-10-09 resolution below is kept for provenance.
- ~~Whether `HKElectrocardiogram` voltage measurements are retrievable by third-party apps.~~ **Resolved 2026-10-09 (Verified) for access only.** Apple's developer documentation, read through its JSON endpoint, states that `HKElectrocardiogramQuery` is "a query that returns the underlying voltage measurements for an electrocardiogram sample", calling a handler once per measurement, and that `HKElectrocardiogram` is "a collection of voltage values" with `samplingFrequency` and `numberOfVoltageMeasurements` properties. `HKElectrocardiogram` is available from iOS 14 and watchOS 7. HealthKit gives read-only access to ECGs saved by Apple Watch, with user authorization for the electrocardiogram type. The ResearchKit and CareKit FAQ still says "You cannot access raw ECG data through HealthKit" (re-read 2026-10-09, undated page). The two sources still disagree in wording. A study can retrieve the waveform of each on-demand 30-second recording a participant takes, not a continuous trace. The earlier reading of the FAQ line as only meaning "no continuous stream" was an inference and is withdrawn (2026-10-11).
- Whether iPhone-computed Blood Oxygen samples reach HealthKit the same way as before. Since August 2025, Blood Oxygen on affected US units is calculated on the paired iPhone [21]. Feature status has changed more than once; verify by model and region at study start.
- Whether SensorKit entitlement approval rates and timelines have changed. (Current data-category list re-read 2026-10-10, above.)
- At what rate, and how often, SensorKit records PPG and ECG samples (the `usage` field names the contexts but no schedule or rate is documented). For: Apple, via the SensorKit request process.
- Whether HealthKit receives the Series 12 device-side cadence (heart rate every five seconds, HRV as often as every five minutes) [20], and whether Series 12 HRV is still SDNN. Apple does not document either, and it materially affects missing-data modelling.
- The minimum iOS version for the Background Health Research Task entitlement. Apple's resource page says 17.1; a third-party summary said 17.0. Not checked.

## Vendor Fact Record

<!-- facts:begin -->
*Generated from the fact record by `tools/facts/generate.py`. Edit the record, not this block.*

**Research access**

| Fact | Value |
|---|---|
| Formal research or academic program (name, what it offers) | **Investigator Support Program:** Investigator Support Program: Apple devices (mostly Apple Watch; Apple Vision Pro and AirPods Pro where available) and app development resources, including the Study App Template, for approved studies. No funding. [V, 2026-10-24]<br>**Study App Template:** Study App Template: Apple study app for approved applicants, free, needing little or no coding; exports encrypted data to the researcher's servers [V, 2026-10-10]<br>**SensorKit:** SensorKit: research-only framework exposing extra iPhone and Apple Watch data types (including PPG, ECG, accelerometer, keyboard, phone and messages usage, visits) through a private entitlement reviewed per study [V, 2026-10-10]<br>**HealthKit Research Entitlement:** HealthKit Research Entitlement (iOS 27.1+): removes the 30-day history limit option from new HealthKit permission requests and reduces access reminders for health research apps. It does not gate access to data types. [V, 2026-10-10]<br>**Background Health Research Task:** Background Health Research Task entitlement (iOS 17.1+): lets a research app process HealthKit, SensorKit or Bluetooth device data in the background; requested through the Investigator Support Program application [V, 2026-10-10]<br>**ResearchKit and CareKit:** ResearchKit and CareKit: free open-source frameworks for consent, surveys and active tasks. They are app-building toolkits, not data programs. [V, 2026-10-10]<br>**Apple Research app:** Apple Research app: Apple's own studies with academic partners (Apple Health Study, Women's Health Study, Hearing Study) that individuals join as participants; not a route for outside investigators [V, 2026-10-10] |
| Who can join the research program | **Investigator Support Program:** Proposals judged on study design, product availability, use of Apple products and frameworks, feasibility and impact; the institution must sign an Investigator Support Program Agreement and show ethics board approval before devices are awarded [V, 2026-10-10]<br>**SensorKit:** Research uses only, reviewed per study; the entitlement goes to the researcher, institution or company, and the app must be published under that developer account, not an external developer's [V, 2026-10-10]<br>**HealthKit Research Entitlement:** IEC or IRB approval; app exclusively for health research and for one unique study [V, 2026-10-10]<br>**Background Health Research Task:** Research app must intend to publish or otherwise make findings public (plus IRB or IEC approval and an app exclusively for health research, per the same page) [V, 2026-10-10]<br>**App Store research apps (Guideline 5.1.3):** Any App Store app conducting health-related human subject research must have independent ethics board approval [V, 2026-10-10] |
| How to apply, and any approval or review step | **Investigator Support Program:** Application form emailed to research_proposals@apple.com; three review cycles a year (due January 5, April 5, September 5); decision typically 6 to 8 weeks after the due date; quarterly status reports after devices ship; SensorKit data needs a separate entitlement request [V, 2026-10-10]<br>**SensorKit:** Research proposal form emailed to sensorkitrequest@apple.com; development entitlement first, distribution entitlement after IRB approval; standard App Store review still applies [V, 2026-10-10]<br>**HealthKit Research Entitlement:** Entitlement request by the Apple Developer Program Account Holder, granted per bundle ID; app update and redistribution required after grant [V, 2026-10-10] |
| Whether the program is active, paused, renamed or closed | **Investigator Support Program:** Active; accepting applications in three cycles a year; Vision Pro and AirPods Pro recently added [V, 2026-10-10]<br>**HealthKit Research Entitlement:** New; requires iOS 27.1 or later [V, 2026-10-10]<br>**SensorKit:** Active; proposals accepted by email and reviewed against standard criteria [V, 2026-10-10]<br>**Apple Research app:** Apple Heart and Movement Study data collection has ended; participants are invited to the Apple Health Study (started early 2025), which does not require an Apple Watch [C, 2026-10-10] |
| Whether the general developer or API program is open to new applicants | Open: individuals or organizations can enrol in the Apple Developer Program after verification, agreeing to the licence agreement and paying the annual fee; HealthKit needs no separate approval beyond App Review and user consent [V, 2026-10-10] |
| Participant or user limits before approval or by tier | No fixed device limit in the Investigator Support Program, but supply is limited and quantity must be justified; no participant cap published for HealthKit or SensorKit [V, 2026-10-10] |
| How academic access differs from commercial or consumer access | HealthKit is open to any developer for health, motion or fitness purposes. SensorKit, the HealthKit Research Entitlement and the Background Health Research Task entitlement are for research apps only. Nonprofits, accredited educational institutions and government entities can request a Developer Program fee waiver. [V, 2026-10-10] |

**Pricing**

| Fact | Value |
|---|---|
| Device or hardware list price | **Apple Watch Series 12:** From 399 USD (US store) [V, 2026-10-10]<br>**Apple Watch Ultra 4:** From 799 USD (US store) [V, 2026-10-10]<br>**Apple Watch SE 3:** From 249 USD (US store) [V, 2026-10-10] |
| Consumer subscription or membership price | No subscription is needed for Health or HealthKit data. Optional Apple Fitness+ (workout content) is 9.99 USD a month or 79.99 USD a year after the free month. [V, 2026-10-10] |
| Research or academic pricing or discount | No published research discount on Apple Watch; devices can instead be awarded free through the Investigator Support Program (no funding). Developer Program fee waiver for approved nonprofits, accredited educational institutions and government entities. [V, 2026-10-10] |
| Fees for API, SDK, platform or data access | No per-call or per-participant fee for HealthKit or SensorKit (on-device frameworks); the cost is the 99 USD annual Developer Program membership. ResearchKit, CareKit and the Study App Template (for approved applicants) are free. [V, 2026-10-10] |
| Minimum order, term or commitment | Annual Developer Program membership; no device minimum or contract term published. Investigator Support Program awardees owe quarterly status reports. [V, 2026-10-10] |
| Whether pricing requires contacting sales | No. Device and membership prices are published; Investigator Support Program devices are by application, not quote. [V, 2026-10-10] |

**Data access and terms**

| Fact | Value |
|---|---|
| Raw signals available to researchers, and by which route | **SensorKit:** PPG and ECG sample streams, accelerometer, rotation rate, ambient light and pressure, and wrist temperature during sleep, through SensorKit with a research entitlement [V, 2026-10-10]<br>**HealthKit ECG:** Apple's research FAQ says raw ECG cannot be accessed through HealthKit; Apple's HealthKit documentation says HKElectrocardiogramQuery returns the underlying per-lead voltage measurements of each ECG sample saved by Apple Watch (conflict) [U, 2026-10-10]<br>**HealthKit heartbeat:** Beat-to-beat heartbeat series samples (HKHeartbeatSeriesSample) are stored in HealthKit; real-time heartbeat data is not available [V, 2026-10-10]<br>**Core Motion CMSensorRecorder:** 50 Hz accelerometer recorded by the system for up to 12 hours per call, even while the app is suspended or terminated, readable for up to three days; no research entitlement needed (motion usage permission only); iOS 9+ and watchOS 2+, not deprecated [V, 2026-10-10]<br>**Core Motion batched sensors (watchOS):** 800 Hz accelerometer and 200 Hz device motion through Core Motion batched sensor APIs, only during an active HealthKit workout session [V, 2026-10-10] |
| Derived or processed metrics available to researchers | **HealthKit:** HealthKit types include heart rate, resting heart rate, HRV (SDNN), respiratory rate, oxygen saturation, VO2 max, sleep stages (awake, core, deep, REM), activity, workouts and sleeping wrist temperature, among many others; recent additions include medications, mental well-being and menopause samples [V, 2026-10-10]<br>**SensorKit:** SensorKit metrics include device usage, keyboard metrics, messages and phone usage, visits, wrist detection and ambient light [V, 2026-10-10]<br>**Core Motion Movement Disorder API:** Resting Parkinsonian tremor (3 to 7 Hz) and choreiform dyskinesia measures through CMMovementDisorderManager; needs an Apple entitlement and is limited to clinically diagnosed patients [V, 2026-10-10] |
| Documented sampling rates or temporal resolution | **Core Motion:** Core Motion: 50 Hz accelerometer (CMSensorRecorder, up to 12 hours per call); 800 Hz accelerometer and 200 Hz device motion during workouts; a 1 Hz high-frequency heart rate class [V, 2026-10-10]<br>**HealthKit:** Heart rate is higher frequency only during workouts and ECG sessions; ECG sampling frequency is reported per sample; no background heart-rate interval or SensorKit PPG rate is documented [V, 2026-10-10]<br>**Apple Watch Series 12:** Series 12 takes background heart rate readings every five seconds and measures HRV as often as every five minutes (device-side); whether HealthKit receives that cadence is not documented [V, 2026-10-10] |
| How far back data can be retrieved | **HealthKit:** All on-device history back to a systemwide earliest permitted date; from iOS 27 participants can limit an app to the past 30 days unless it holds the HealthKit Research Entitlement; old data is periodically purged from Apple Watch itself [V, 2026-10-10]<br>**SensorKit:** 7 days of prior data for an active sensor, after a 24-hour holding period on new data [V, 2026-10-10]<br>**Core Motion CMSensorRecorder:** Recorded accelerometer data stays available for up to three days [V, 2026-10-10] |
| Export, API, SDK or file routes | **HealthKit and SensorKit:** On-device only: the study iOS app reads HealthKit (and SensorKit with the entitlement) after participant consent and uploads to the researcher's own server; no Apple cloud API. Participants can export all Health data as XML from the Health app. [V, 2026-10-10]<br>**Study App Template:** Apple's Study App Template exports collected data to the researcher's servers with built-in encryption (approved Investigator Support Program applicants) [V, 2026-10-10]<br>**HealthKit clinical records:** HealthKit clinical records (FHIR resources from connected providers) can be read by the app [V, 2026-10-10] |
| API rate limits | n/a |
| Terms on retaining, storing or deleting data | **HealthKit:** No retention period is published. Apps may not store personal health information in iCloud; recipients of de-identified data must be barred from re-identification. [V, 2026-10-10]<br>**SensorKit:** The SensorKit entitlement carries additional, non-public terms on use and handling; a 2025 study reports these bar public sharing of SensorKit data. The 24-hour hold lets users delete data before an app sees it. [R, 2026-10-10] |
| Terms on using data to train AI or ML models | HealthKit data may be used only for health, motion or fitness services, or for health research with permission; sharing personal data with third-party AI needs disclosure and explicit permission. No term names model training. [C, 2026-10-10] |
| Announced shutdowns, deprecations or migrations, with dates | **HealthKit (iOS 27):** No shutdowns announced. Migration: from iOS 27 participants can limit HealthKit read access to the past 30 days and get periodic access reminders; research apps can apply for the HealthKit Research Entitlement (iOS 27.1+) to remove the 30-day option. [V, 2026-10-10]<br>**Blood Oxygen (US):** Since August 2025, Blood Oxygen on affected US Apple Watch units is calculated on the paired iPhone and shown in the Health app's Respiratory section [V, 2026-10-10] |

**Compliance and regulatory**

| Fact | Value |
|---|---|
| Whether a HIPAA Business Associate Agreement is offered | No BAA is offered. Apple's developer and iCloud terms bar using Apple services in a way that would make Apple a business associate or to handle PHI. Not needed for HealthKit itself, since study data flows from the device to the researcher's server. [C, 2026-10-10] |
| Whether a data processing agreement is offered | Not public [2026-10-10] |
| Published HIPAA statement | Apple Research app data is stored in an Apple system designed to meet HIPAA technical safeguards. For third-party apps, Apple bars use of its services and iCloud for PHI. [C, 2026-10-10] |
| Published GDPR statement | EEA, UK and Swiss personal data is controlled by Apple Distribution International Limited (Ireland); international transfers use Standard Contractual Clauses [C, 2026-10-10] |
| ISO/IEC 27001 status and evidence | ISO/IEC 27001 and 27018 certified for listed Apple internet services including iCloud, with annual registrar attestation; certificates are in Coalfire's directory [C, 2026-10-10] |
| SOC 2 status and evidence | Not public [2026-10-10] |
| FDA clearances, from the FDA database | **ECG app:** De Novo granted: ECG App, DEN180044, decision 2018-09-11 [V, 2026-10-10]<br>**ECG app 2.0:** 510(k) cleared: ECG App, K201525, decision 2020-10-08 [V, 2026-10-10]<br>**Irregular Rhythm Notification:** De Novo granted: Irregular Rhythm Notification Feature, DEN180042, decision 2018-09-11 [V, 2026-10-10]<br>**Irregular Rhythm Notification (2021):** 510(k) cleared: IRNF App, K212516, decision 2021-10-22 [V, 2026-10-10]<br>**Irregular Rhythm Notification (2023):** 510(k) cleared: Irregular Rhythm Notification Feature (IRNF), K231173, decision 2023-07-21 [V, 2026-10-10]<br>**AFib History:** 510(k) cleared: Atrial Fibrillation History Feature, K213971, decision 2022-06-03 [V, 2026-10-10]<br>**AFib History (MDDT qualification):** FDA-qualified Medical Device Development Tool: the AFib History Feature can serve as a biomarker test for AFib burden, a secondary effectiveness endpoint in cardiac ablation device studies [V, 2026-10-10]<br>**Sleep Apnea Notification:** 510(k) cleared: Sleep Apnea Notification Feature (SANF), K240929, decision 2024-09-13 [V, 2026-10-10]<br>**Hypertension Notification:** 510(k) cleared: Hypertension Notification Feature (HTNF), K250507, decision 2025-09-11 [V, 2026-10-10]<br>**Hearing Aid Feature (AirPods Pro):** De Novo granted: Hearing Aid Feature (HAF), DEN230081, decision 2024-09-12 [V, 2026-10-10]<br>**Digital Prism Correction (not Apple Watch):** 510(k) cleared: Digital Prism Correction Feature (DPCF), K242058 (2024-10-21) and K250143 (2025-06-23) [V, 2026-10-10]<br>**Medical Imaging Calibration (not Apple Watch):** 510(k) cleared: Medical Imaging Calibration Feature (MICF), K253582, decision 2026-04-01 [V, 2026-10-10] |
| Where data is stored, and residency options | HealthKit data is stored on the device; iCloud Health sync is end-to-end encrypted with keys Apple does not hold; Research app data is stored in an Apple system; EEA personal data is controlled by Apple Distribution International (Ireland). Study data lives wherever the researcher's backend is. [V, 2026-10-10] |

<!-- facts:end -->

## Key Links

- Official site: https://www.apple.com/watch/
- Health / HealthKit developer documentation: https://developer.apple.com/documentation/healthkit
- SensorKit documentation: https://developer.apple.com/documentation/sensorkit
- ResearchKit & CareKit (consortium): https://www.researchandcare.org/
- SensorKit access guidance: https://www.researchandcare.org/resources/accessing-sensorkit-data/
- ResearchKit GitHub: https://github.com/ResearchKit/ResearchKit
- CareKit GitHub: https://github.com/carekit-apple/CareKit
- Apple Health privacy: https://www.apple.com/legal/privacy/data/en/health-app/
- SensorKit research requests: sensorkitrequest@apple.com
- Investigator Support Program: https://www.researchandcare.org/investigator-support-program/ (applications to research_proposals@apple.com)
- HealthKit Research Entitlement: https://www.researchandcare.org/resources/healthkit-research-entitlement/
- Apple Developer Program: https://developer.apple.com/programs/

## Sources

1. ResearchKit & CareKit, Accessing SensorKit Data. https://www.researchandcare.org/resources/accessing-sensorkit-data/ (accessed 2026-08-21). Establishes SensorKit data categories, entitlement process, IRB requirement, and documented constraints.
2. ResearchKit & CareKit, FAQ. https://www.researchandcare.org/faq/ (accessed 2026-08-21). States that raw ECG is not accessible via HealthKit (in conflict with (10), see Open Questions) and that higher-frequency HR is available during workouts/ECG sessions and via SensorKit.
3. 9to5Mac, "iOS 14: HealthKit expands ECGs with new API". https://9to5mac.com/2020/06/23/ios-14-healthkit-new-features-opens-ecg-symptoms-more/ (accessed 2026-08-21). Secondary source; conflicts with (2) on ECG voltage access.
4. Apple Developer Forums threads on `HKHeartbeatSeriesSample` and beat-to-beat capture. https://developer.apple.com/forums/thread/666206 , https://developer.apple.com/forums/thread/746218 (accessed 2026-08-21).
5. Fuller D. et al., "Reliability and Validity of Commercially Available Wearable Devices for Measuring Steps, Energy Expenditure, and Heart Rate: Systematic Review." *JMIR mHealth uHealth* 2020;8(9):e18694. https://mhealth.jmir.org/2020/9/e18694/
6. Chinoy/Brigham-affiliated four-stage sleep validation, *Sensors* 2024;24(20):6532. https://www.mdpi.com/1424-8220/24/20/6532, Oura-funded, independently conducted; n=35.
7. Schyvens A.-M. et al., "A performance validation of six commercial wrist-worn wearable sleep-tracking devices for sleep stage scoring compared to polysomnography." *SLEEP Advances* 2025;6(2):zpaf021. https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472, independent; n=62.
8. "The accuracy of Apple Watch measurements: a living systematic review and meta-analysis." *npj Digital Medicine* 2025. https://www.nature.com/articles/s41746-025-02238-1, identified but not extracted (access-gated at time of research).
9. Apple Health data export format (community/secondary). https://discussions.apple.com/thread/255037259 (accessed 2026-08-21).
10. Apple Developer Documentation, `HKElectrocardiogram` and `HKElectrocardiogramQuery`. https://developer.apple.com/documentation/healthkit/hkelectrocardiogram , https://developer.apple.com/documentation/healthkit/hkelectrocardiogramquery (read via the `developer.apple.com/tutorials/data/documentation/healthkit/*.json` endpoint, accessed 2026-10-09). **Primary.** Establishes per-measurement voltage access for stored ECG samples, the `samplingFrequency` and `numberOfVoltageMeasurements` properties, read-only access to Apple Watch ECGs, and availability from iOS 14 / watchOS 7. Supersedes (3) and conflicts in wording with (2).
11. Apple Developer Documentation, SensorKit `SRSensor`, `SRSensor.photoplethysmogram`, `SRSensor.electrocardiogram`, `SRSensor.accelerometer`, `SRPhotoplethysmogramSample`, and the `com.apple.developer.sensorkit.reader.allow` entitlement. https://developer.apple.com/documentation/sensorkit/srsensor (read via the `developer.apple.com/tutorials/data/documentation/*.json` endpoint, accessed 2026-10-10). **Primary.** Full sensor list with introduced-in versions; PPG and ECG iOS 17.4; accelerometer iOS 14.0; PPG sample fields and usage values; entitlement and per-study approval mechanics. Re-confirmed in the same session: `HKElectrocardiogram` lists iOS 14.0 and watchOS 7.0.
12. Apple, Research app. https://www.apple.com/ios/research-app/ (accessed 2026-10-10). Current studies: Apple Health Study (initiated early 2025, with Brigham and Women's Hospital), Apple Women's Health Study, Apple Hearing Study.
13. Europe PMC records for Cohen JB et al. 2026, *Hypertension* (PMID 41564145) and *JAMA* (PMID 41661624), read 2026-10-10. Titles and DOIs. *Hypertension* author disclosures read 2026-10-10 in the NIH author manuscript PMC12826266 (https://pmc.ncbi.nlm.nih.gov/articles/PMC12826266/); JAMA disclosures not read.
14. ResearchKit & CareKit, Investigator Support Program and FAQ. https://www.researchandcare.org/investigator-support-program/ , https://www.researchandcare.org/faq/ (accessed 2026-10-10, vendor fact record). Devices in kind, no funding, evaluation criteria, agreement and ethics approval, review cycles, quarterly reports, device supply.
15. ResearchKit & CareKit, HealthKit Research Entitlement. https://www.researchandcare.org/resources/healthkit-research-entitlement/ (accessed 2026-10-10, vendor fact record). iOS 27 30-day history option, entitlement effects, iOS 27.1 requirement, eligibility, per-bundle-ID grant.
16. ResearchKit & CareKit, Background Health Research Task entitlement. https://www.researchandcare.org/resources/background-health-research-task-entitlement/ (accessed 2026-10-10, vendor fact record). Background processing of HealthKit, SensorKit or Bluetooth data; iOS 17.1; publication intent.
17. ResearchKit & CareKit, Study App Template. https://www.researchandcare.org/resources/study-app-template/ (accessed 2026-10-10, vendor fact record). Free for approved applicants; encrypted export to the researcher's servers.
18. Apple Developer Documentation, Core Motion `CMSensorRecorder.recordAccelerometer(forDuration:)`, `CMHighFrequencyHeartRateData` and `CMMovementDisorderManager`. https://developer.apple.com/documentation/coremotion/cmsensorrecorder/recordaccelerometer(forduration:) , https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedata , https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager (read via the JSON endpoint, accessed 2026-10-10, vendor fact record). **Primary.**
19. Apple Developer Documentation, HealthKit updates. https://developer.apple.com/documentation/updates/healthkit , and WWDC23 session 10179, https://developer.apple.com/videos/play/wwdc2023/10179/ (accessed 2026-10-10, vendor fact record). 800 Hz accelerometer and 200 Hz device motion during workout sessions; new HealthKit data types.
20. Apple, Apple Watch Series 12. https://www.apple.com/apple-watch-series-12/ (accessed 2026-10-10, vendor fact record). Marketing page. Background heart rate every five seconds, HRV as often as every five minutes.
21. Apple Newsroom, "An update on Blood Oxygen for Apple Watch in the US" (August 2025). https://www.apple.com/newsroom/2025/08/an-update-on-blood-oxygen-for-apple-watch-in-the-us/ (accessed 2026-10-10, vendor fact record).
22. Apple Store and Apple Developer Program pricing. https://www.apple.com/shop/buy-watch/apple-watch , https://developer.apple.com/programs/enroll/ , https://developer.apple.com/help/account/membership/fee-waivers/ , https://www.apple.com/apple-fitness-plus/ (accessed 2026-10-10, vendor fact record).
23. FDA device records for applicant "Apple, Inc.". https://api.fda.gov/device/510k.json?search=applicant:%22Apple,%20Inc.%22&limit=100 (12 records), individual records on accessdata.fda.gov, and the AFib History MDDT qualification, https://www.fda.gov/media/178230/download (accessed 2026-10-10, vendor fact record).
24. Funk et al. 2025, *PLOS One* (Intern Health Study). https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0329707 (accessed 2026-10-10). Data availability statement reports that Apple's terms bar public sharing of SensorKit data. Reported.
25. Apple Developer Program License Agreement, App Store Review Guidelines and iCloud terms. https://developer.apple.com/support/terms/apple-developer-program-license-agreement/ , https://developer.apple.com/app-store/review/guidelines/ , https://www.apple.com/legal/internet-services/icloud/ (accessed 2026-10-10, vendor fact record). Business-associate and PHI bars, health data use limits, third-party AI disclosure, re-identification ban, Guideline 5.1.3.
26. Brigham and Women's Hospital, Apple Heart and Movement Study notice. https://appleheartandmovementstudy.bwh.harvard.edu/?p=2152 (accessed 2026-10-10, vendor fact record). Secondary. Data collection ended; Apple Health Study does not require an Apple Watch.
27. Apple Developer Documentation, HealthKit (`earliestPermittedSampleDate()`, About the HealthKit framework, Accessing health records, `HKHeartbeatSeriesSample`) and SensorKit (`SRSensorReader`, `SRFetchRequest`). https://developer.apple.com/documentation/healthkit , https://developer.apple.com/documentation/sensorkit/srsensorreader , https://developer.apple.com/documentation/sensorkit/srfetchrequest (read via the JSON endpoint, accessed 2026-10-10, vendor fact record). **Primary.** History depth, Watch purge, FHIR records, SensorKit 7-day lookback and 24-hour hold.
28. Apple privacy policy, certifications and iCloud data security. https://www.apple.com/legal/privacy/en-ww/ , https://support.apple.com/guide/certifications/apc34d2c0468b/web , https://support.apple.com/en-us/102651 , https://developer.apple.com/documentation/healthkit/protecting-user-privacy (accessed 2026-10-10, vendor fact record). GDPR controller and transfers, ISO/IEC 27001 and 27018 scope, end-to-end encryption of Health data, on-device storage.
