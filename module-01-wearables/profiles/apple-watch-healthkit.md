# Apple Watch / Apple Health / HealthKit / SensorKit

## Quick Facts

| Field | Details |
|---|---|
| Organization | Apple Inc. |
| Category | Consumer smartwatch + OS-level health data framework |
| Current status | Active |
| Platforms/devices | Apple Watch (Series/SE/Ultra lines), iPhone; data surfaced through the Health app on iOS |
| Open source | No (ResearchKit and CareKit are open source; HealthKit, SensorKit, watchOS are not) |
| Hosting/deployment | On-device HealthKit store on iPhone; **no Apple-operated cloud API for researchers**. Any cloud pipeline must be built by the research team inside their own iOS app. |
| Pricing model | Device purchase only; no subscription required for core health metrics; no API fee |
| Last verified | 2026-08-21; ECG voltage access re-verified 2026-10-09; SensorKit sensor list, entitlement and Research app studies re-verified 2026-10-10 |

## Summary

- Apple is the single largest consumer wearable ecosystem, but it is architecturally the *least* like the other platforms in this module. There is no Apple server-side research API. Apple does not host participant data for researchers and does not offer an OAuth endpoint a researcher can call to pull a cohort's data. Instead, HealthKit is an **on-device datastore on the participant's iPhone**, and the only supported way to get data out at scale is to ship an iOS app (built by the research team or a vendor) that the participant installs, grants read permission to, and which then uploads to infrastructure the research team controls.

- This has two consequences that dominate every design decision:

1. **Data custody is favourable.** Because Apple is not in the loop, there is no vendor data-sharing agreement, no vendor rate limit, and no vendor retention policy on the research copy of the data. The researcher's own backend is the system of record.
2. **Engineering burden is high.** There is no "sign up, get a token, pull JSON" path. A study needs an iOS app, an Apple Developer account, App Store (or TestFlight/enterprise) distribution, and a backend. This is why Module 2 platforms (mindLAMP, Beiwe, RADAR-base, Ethica) and commercial middleware exist, they supply that app layer.

- A second, separate framework, **SensorKit**, exposes lower-level iPhone/Watch signals but is *explicitly restricted to research use* and requires a private entitlement approved by Apple per study. Its current sensor list (Apple documentation, Verified 2026-10-10) includes **photoplethysmogram and electrocardiogram sample streams (iOS 17.4+) and raw accelerometer (iOS 14+)**, so raw PPG is available from Apple, but only to Apple-approved studies and with an undocumented capture schedule and rate.

## Products / Platform Architecture

- Three distinct access surfaces, frequently conflated:

| Surface | What it is | Who can use it | Access mechanism |
|---|---|---|---|
| **HealthKit** | On-device health datastore; aggregates Watch, iPhone, and third-party app/device writes | Any iOS developer | In-app API, per-type user permission |
| **SensorKit** | Lower-level behavioural/ambient sensing from iPhone + Watch | Researchers only | Private entitlement, per-study Apple review, IRB approval required |
| **Health app export** | User-initiated export of the whole HealthKit store | The participant themselves | XML inside `Export.zip` (`apple_health_export/Export.xml`) |
| **Apple Research app** | Apple's own first-party study platform (as of 2026-10-10: Apple Health Study, Apple Women's Health Study, Apple Hearing Study) | Apple + named academic partners only | Not open to third parties |

- **ResearchKit** and **CareKit** are open-source frameworks Apple publishes for building consent flows, surveys, and active tasks in a study app. They are *app-building* toolkits, not data-access mechanisms, and they do not by themselves grant any additional data.

## Sensors and Data Streams

- Every Module 1 profile uses the same table so devices can be compared row by row. Rows are the sensors named in `CLAUDE.md`. "Present" is about the hardware; "Researcher access" is about what a study can actually obtain, which is the module's central question. "Unclear" means nothing current was verified. The convention is recorded in [`../../shared/profile-table-conventions.md`](../../shared/profile-table-conventions.md).

| Sensor | Present | Researcher access to underlying signal | Resolution or sampling | Notes |
|---|---|---|---|---|
| PPG | Yes | HealthKit: no raw PPG, derived HR and heartbeat series only. **SensorKit (research entitlement): `SRSensor.photoplethysmogram` "streams sample PPG sensor data" (optical, accelerometer and temperature samples per `SRPhotoplethysmogramSample`), iOS 17.4+.** | Derived (HealthKit); SensorKit rate not documented | Each SensorKit PPG sample carries a `usage` value (background system, deep breathing, foreground blood oxygen, foreground heart rate), so capture is tied to those contexts; the schedule and rate are not stated. Verified 2026-10-10 (Apple documentation JSON). |
| ECG | Series 4 and later, Ultra, region-gated | Yes for recorded ECGs. `HKElectrocardiogramQuery` returns each voltage measurement of a stored `HKElectrocardiogram` sample (Apple Developer docs, verified 2026-10-09). SensorKit also lists `SRSensor.electrocardiogram`, "streams sample ECG sensor data", iOS 17.4+ (Verified 2026-10-10). No continuous ECG exists to read. | Single lead (Lead I-like), sampling frequency stored per sample | On-demand 30-second recordings only. The ResearchKit and CareKit FAQ line saying raw ECG is not accessible conflicts with Apple's own API documentation, which is the authoritative source. |
| Accelerometer | Yes | Not via HealthKit. In-app on watchOS via Core Motion while the app runs. **SensorKit `accelerometer` (iOS 14+) and `rotationRate` under the research entitlement.** | Core Motion rates; SensorKit rate not stated | `CMMotionManager`, historically `CMSensorRecorder`. |
| Gyroscope | Yes | Same as accelerometer, Core Motion in-app only. | Core Motion rates |  |
| Magnetometer | Unclear | Unclear | Unclear |  |
| Temperature | Series 8 and later, Ultra | HealthKit: derived sleeping-wrist temperature deviation, not a raw trace. SensorKit `wristTemperature` (iOS 17.0+) "provides wrist temperature while the user sleeps". | Nightly |  |
| SpO2 | Series 6 and later, Ultra | Blood oxygen samples where the feature is enabled. | Periodic | US availability disrupted by a patent dispute, see Open Questions. |
| GPS | Yes on GPS models | Route data via `HKWorkoutRoute` for workouts. | Workout routes |  |
| Barometer / altimeter | Yes | Derived flights climbed and elevation. | Derived |  |
| EDA | No | Not applicable | Not applicable | A real gap against Empatica for stress and arousal work. |
| Ambient light | iPhone, and Watch wear detection via SensorKit | SensorKit only | Unclear |  |
| Other | Unclear | Unclear | Unclear | Not verified against current documentation. |

**Verification.** PPG, ECG, accelerometer and temperature rows re-checked 2026-10-10 against Apple's SensorKit documentation, read through the `developer.apple.com/tutorials/data/documentation/sensorkit/*.json` endpoint (**Verified**). Other rows Corroborated: the 2026-08-21 pass could not render Apple's JavaScript documentation and drew on developer forum threads, the ResearchKit and CareKit consortium FAQ and published studies, per the notes below.

### Notes from earlier verification passes

- Sensor complement varies substantially by Watch model and generation; check the specific SKU before assuming availability.

| Sensor | Present on Apple Watch (recent models) | Researcher access to underlying signal |
|---|---|---|
| PPG (optical heart) | Yes | **No raw PPG.** Only derived HR samples and heartbeat series. |
| ECG (single-lead) | Series 4+ / Ultra (region-gated) | `HKElectrocardiogram` samples. Access to per-sample **voltage** was recorded as disputed in the first pass; resolved 2026-10-09 in favour of access for recorded ECGs, see Open Questions. |
| Accelerometer | Yes | Not via HealthKit. Available in-app on watchOS via Core Motion (`CMMotionManager`, and historical `CMSensorRecorder`) while the app runs. |
| Gyroscope | Yes | Same as accelerometer, Core Motion, in-app only. |
| Temperature (wrist) | Series 8+ / Ultra | Derived sleeping-wrist-temperature deviation; not a raw stream. |
| SpO2 | Series 6+ / Ultra, with a US availability disruption from a patent dispute (see Open Questions) | Blood oxygen samples where the feature is enabled. |
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
- **Sampling is opportunistic and irregular.** Background heart rate is sampled at variable intervals (roughly every few minutes at rest, far more frequently during workouts). Missingness is structured, not random.

- `HKHeartbeatSeriesSample` stores the precise timestamps of individual heartbeats, which is the closest thing to beat-to-beat/IBI data in the ecosystem. It is generated during specific contexts (notably ECG sessions and some workout/breathe contexts) rather than continuously.

## Active Data Collection

- No native survey/EMA capability in HealthKit. ResearchKit provides open-source survey, informed-consent, and active-task modules (including validated-style tasks such as tapping speed, gait and balance, spatial memory, and audio tasks) that a study app can embed. Notifications are handled through standard iOS mechanisms.

## Researcher and Study Management Features

- **None provided by Apple to third parties.** There is no Apple-run enrolment portal, adherence dashboard, participant roster, or device-management console for external researchers. Every one of these must be built or bought.

- Apple's own Research app does provide these functions, but it is Apple's internal study platform for Apple-run studies with selected academic collaborators. As of 2026-10-10 Apple's Research app page lists the **Apple Health Study** ("Initiated in early 2025", continuing Apple's partnership with Brigham and Women's Hospital), the **Apple Women's Health Study** (with the Harvard T.H. Chan School of Public Health and NIEHS) and the **Apple Hearing Study** (with the University of Michigan). The earlier Apple Heart and Movement Study is no longer listed there. It is not a service researchers can procure.

## Data Access and Export

| Route | Mechanism | Granularity | Practical notes |
|---|---|---|---|
| Custom iOS app | HealthKit read authorisation, per data type | Sample-level, as stored | The only scalable route. Requires the participant to have an iPhone and to install and authorise the app. |
| SensorKit | Private entitlement (`com.apple.developer.sensorkit.reader.allow`) + IRB | Sample-level behavioural and ambient data, plus raw accelerometer, PPG and ECG sample streams | Research-only; per-study Apple approval; on-device, then uploaded by the study app. |
| Participant self-export | Health app → Export Health Data | Full store, sample-level | XML in a zip. Workable for small N or as a backstop; unwieldy at scale (files are large and the format is verbose). |
| Third-party middleware | Vendors that ship an SDK/app wrapping HealthKit | Varies | Shifts the engineering burden but adds a data processor to the IRB/DPA. |

- **Permission asymmetry is a documented trap:** HealthKit read permissions are deliberately opaque. An app cannot tell whether the user granted or denied *read* access to a type, a denied type simply returns no data, which is indistinguishable from a user who has no data of that type. Studies must therefore verify data flow empirically per participant rather than trusting a permissions check.

## APIs, SDKs, and Extensibility

- HealthKit (iOS/watchOS), Core Motion, ResearchKit, CareKit, SensorKit.
- **No public server-to-server API. No OAuth. No bulk cohort export. No webhooks.** This is the defining constraint of the ecosystem.
- Apple Watch third-party apps run on watchOS with meaningful background-execution limits; continuous high-rate sensor capture on-watch is constrained by both OS policy and battery.

### SensorKit specifics

- Data categories in the current `SRSensor` list (developer.apple.com, read 2026-10-10, **Verified**): accelerometer, rotation rate, ambient light, ambient pressure, pedometer data, odometer, visits, device usage report, keyboard metrics, messages usage report, phone usage report, media events, face metrics, Siri speech metrics, telephony speech metrics, headphone motion, headphone settings, acoustic settings, on-wrist state, heart rate (iOS 17.0+), **electrocardiogram and photoplethysmogram (iOS 17.4+)**, wrist temperature (iOS 17.0+) and sleep sessions (listed from iOS 26.0). The 2026-08-21 list (ambient light, device usage, keyboard metrics, message metadata, call logs, visits and wear detection) came from the ResearchKit and CareKit consortium page and was incomplete. Watch-derived sensors need a paired Apple Watch.

- Access process, as documented by the ResearchKit & CareKit consortium:
- Submit a research proposal to `sensorkitrequest@apple.com`
- Pass Apple's review criteria
- Hold IRB / ethics board approval
- Accept additional terms and conditions
- **The submitting developer account must belong to the researcher or their institution**, an outside contractor cannot submit under their own account

- Documented constraints: entitlement review can delay development; participants may decline to share these more sensitive streams; background execution is limited when the user is not interacting with the app; and data volumes are large enough to require deliberate storage planning.

- **Entitlement mechanics (Apple documentation, Verified 2026-10-10):** the entitlement `com.apple.developer.sensorkit.reader.allow` is "the necessary entitlement to access sensor data that's required by your app's preapproved research study". A team submits its study to Apple; if Apple approves it, the team can create a provisioning profile that signs the app with this entitlement, and the system closes an app whose code signature lacks it. Data are read on a per-team basis.

### Research program and academic data access (added 2026-10-10)

- **SensorKit is Apple's only research-specific data programme open to outside academics.** It is free beyond the Apple Developer Program fee, requires per-study approval by Apple and IRB approval, and yields on-device data that the study's own app uploads: behavioural sensors, raw accelerometer, and (iOS 17.4+) PPG and ECG sample streams. Rates and capture schedule are not documented. There is no Apple cloud copy, rate limit or Apple retention term in the study's path.
- **HealthKit** is the same for academics and everyone else: derived samples, full on-device history the participant authorises, through a researcher-built iOS app, with no cloud API.
- **ResearchKit and CareKit** are open-source toolkits, not data programmes.
- **The Apple Research app** runs Apple's own studies with named partners and cannot be procured by outside teams.
- **Active:** yes. SensorKit sensors were last extended in iOS 17.4 and iOS 26 (sleep sessions); the ResearchKit GitHub repository was last pushed 2026-09-23, latest release 3.2.0 on 2025-09-19 (GitHub API, 2026-10-10).

## Deployment and Infrastructure

- Entirely the research team's responsibility: iOS app development and maintenance, Apple Developer Program membership, App Store review (which applies *in addition to* SensorKit entitlement approval), distribution (public App Store, TestFlight, or Apple Business/Enterprise), and a backend for ingest and storage.

## Participant Experience

- **Requires an iPhone.** This is the largest single feasibility constraint, it excludes Android users entirely and, in most countries, biases the sample toward higher socioeconomic status. Mixed-OS studies cannot use Apple Watch as a common device.
- Battery life on non-Ultra models is roughly a day, meaning **daily charging**. This creates a systematic gap in 24h coverage and forces a choice between nocturnal sleep data and daytime completeness unless charging is scheduled deliberately (a common protocol is charging during a fixed daily routine such as showering).
- Data syncs from Watch to iPhone automatically over Bluetooth/Wi-Fi; the Watch buffers when the phone is absent.
- Wear compliance is generally high because the device is a mainstream consumer product participants may already own and want to wear.

## Privacy, Security, and Compliance

- HealthKit data is stored in an encrypted on-device store; Apple's documented position is that HealthKit data is encrypted at rest on device and that apps may not use HealthKit data for advertising or sell it to data brokers.
- Health data synced to iCloud is covered by Apple's encryption regime (and by Advanced Data Protection where enabled by the user).
- Because Apple does not receive the study's copy of the data, **HIPAA/GDPR analysis attaches to the research team's own infrastructure**, not to Apple. There is no Apple BAA or DPA to negotiate for the HealthKit path. This is a genuine structural advantage over API-mediated platforms.
- App Store review enforces health-data-specific policies (purpose strings, no advertising use, no selling of health data).

- **Do not infer** that using an Apple device makes a study HIPAA-compliant. Compliance is entirely a property of the study's own stack.

## Pricing

- No API fee, no research programme fee, no subscription needed for the core metrics used in most research.
- Costs are: device hardware (Apple Watch SE through Ultra spans a wide range at retail), the Apple Developer Program annual fee, and, usually dominant, the engineering cost of building and maintaining the study app and backend.
- Because participants often already own an Apple Watch, BYOD designs can eliminate device cost entirely, at the price of device-generation heterogeneity in the sample.

## Research Evidence and Validation

- **Heart rate:** Apple Watch is among the better-validated consumer optical HR devices. A widely cited systematic review of steps, energy expenditure, and heart rate across commercial wearables found Apple among the most accurate brands for heart rate, with all major brands within roughly ±3% on average under controlled conditions.
- **Steps:** high validity in laboratory settings; free-living accuracy is materially worse across all brands.
- **Energy expenditure:** poor. The same review reported that **no brand** met acceptable accuracy limits for energy expenditure, with mean absolute percentage error above 30%. Energy expenditure from any consumer wearable should be treated as unsuitable for a primary endpoint.
- **Sleep staging:** mixed and study-dependent.
  - Chinoy-style single-night lab comparisons place Apple Watch competitively: in a 2024 Brigham and Women's Hospital study (n=35, funded by Oura but independently conducted and published in *Sensors*), four-stage sensitivity was 50.5 to 86.1% and precision 72.7 to 87.8% for Apple, versus 76.0 to 79.5% / 77.0 to 79.5% for Oura and 61.7 to 78.0% / 72.8 to 73.2% for Fitbit, i.e. Apple had the widest spread, strong on some stages and weak on others, while Oura was the most uniformly accurate. **Note the funding source when citing this.**
  - An independent 2025 six-device validation (Schyvens et al., *SLEEP Advances*, n=62) reported markedly lower agreement for most devices, with Apple Watch Series 8 first on overall four-stage agreement (κ 0.53) and WHOOP 4.0 fourth (κ 0.37). The often-quoted ~69.6% (WHOOP) and ~50.7% (Apple) are deep-sleep classification accuracies, not overall agreement (corrected 2026-10-09; see `validation-evidence.md`). Most devices differed significantly from PSG on total sleep time, sleep efficiency, WASO, and light sleep.
- **Hypertension notifications (added 2026-10-09):** validation exists only as vendor documents, Apple's September 2025 white paper and FDA 510(k) summary K250507 (cleared 2025-09-11). Pivotal study: 2,229 enrolled, 1,863 analysed, 30 days vs an FDA-cleared home cuff; sensitivity 41.2% (95% CI 37.2 to 45.3), specificity 92.3% (90.6 to 93.7), stage 2 sensitivity 53.7%; lower sensitivity under age 60 and at BMI ≤30; Fitzpatrick V-VI subgroup not significantly different. No peer-reviewed publication of the pivotal study located (PubMed, Europe PMC, 2026-10-09). Independent critique: Cohen et al. 2026, "Apple Watch for Hypertension Screening", *Hypertension* (DOI 10.1161/HYPERTENSIONAHA.125.26031), and a population-impact model, Cohen et al. 2026, "Impact of a Smartwatch Hypertension Notification Feature for Population Screening", *JAMA* (DOI 10.1001/jama.2025.26925); titles and DOIs confirmed in Europe PMC 2026-10-10. Author disclosures were not read (publisher page returned 403); the earlier note that two authors hold Apple stock could not be confirmed and is withdrawn until the disclosures are read. **Verified** (FDA and Apple documents read).
- **SpO2 (added 2026-10-09):** Walzel et al. 2023 (*Sensors* 23(22):9164, independent): Apple Watch 8 had the lowest bias of three smartwatches vs Masimo Radical-7 under induced hypoxemia. Jiang et al. 2026 (*JMIR Form Res* 10:e85253): Apple Watch Series 7 Arms 5.82% below 88% SaO2 vs arterial blood gas, with overestimation. **Corroborated.**
  - These two results are not reconcilable as a simple ranking; they differ in device generation, sample, and scoring approach. Treat consumer sleep *staging* as exploratory and consumer sleep *timing/duration* as more defensible.
- A living systematic review and meta-analysis of Apple Watch accuracy has been published in *npj Digital Medicine* (2025) and is the best single entry point to this literature; it was paywall-gated during this session and its numbers have not been extracted here.

## Strengths

- Largest installed base of any research-relevant wearable, enabling low-cost BYOD recruitment.
- Best-in-class or near-best-in-class heart rate accuracy among consumer wrist devices.
- Rich, standardised, cross-app data model, HealthKit aggregates third-party devices and apps, so a single integration can capture data originating from non-Apple hardware.
- No vendor sits between the researcher and the data: no rate limits, no vendor retention policy, no data-processing agreement with Apple for the study copy.
- ECG and mobility metrics that most competitors lack.
- SensorKit offers behavioural/ambient signals unavailable anywhere else on iOS, and (iOS 17.4+) PPG and ECG sample streams, to approved studies.
- Strong participant acceptability and wear compliance.

## Limitations

- **No server API and no study-management tooling**, the highest engineering barrier of any platform in this module.
- **iPhone-only**, which is a hard exclusion criterion, not an inconvenience.
- **No raw PPG and no raw accelerometer through HealthKit.** SensorKit does expose PPG, ECG and accelerometer samples, but only under a per-study Apple entitlement, with an undocumented capture schedule and rate. Core Motion gives in-app motion data but not a retrospective raw archive comparable to ActiGraph/Ametris.
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
- Studies needing raw PPG or raw continuous accelerometry without going through Apple's per-study SensorKit approval.
- Small studies without software engineering capacity and without budget for middleware.
- Energy expenditure as a primary endpoint.
- Clinical sleep-staging endpoints.
- Fast-turnaround studies, SensorKit entitlement plus App Store review is a multi-month critical path.

## Open Questions

- ~~Whether `HKElectrocardiogram` voltage measurements are retrievable by third-party apps.~~ **Resolved 2026-10-09 (Verified).** Apple's developer documentation, read through its JSON endpoint, states that `HKElectrocardiogramQuery` is "a query that returns the underlying voltage measurements for an electrocardiogram sample", calling a handler once per measurement, and that `HKElectrocardiogram` is "a collection of voltage values" with `samplingFrequency` and `numberOfVoltageMeasurements` properties. `HKElectrocardiogram` is available from iOS 14 and watchOS 7. HealthKit gives read-only access to ECGs saved by Apple Watch, with user authorization for the electrocardiogram type. The ResearchKit and CareKit FAQ still says "You cannot access raw ECG data through HealthKit" (re-read 2026-10-09, undated page). The two sources still disagree in wording; Apple's API reference is treated as current, and the FAQ line is best read as meaning there is no continuous or background ECG stream, which is true. A study can retrieve the waveform of each on-demand 30-second recording a participant takes, not a continuous trace.
- Current SpO2 availability on US-sold Apple Watches following the ongoing patent dispute and Apple's software workarounds. Feature status has changed more than once; verify by model and region at study start.
- Whether SensorKit entitlement approval rates and timelines have changed. (Current data-category list re-read 2026-10-10, above.)
- At what rate, and how often, SensorKit records PPG and ECG samples (the `usage` field names the contexts but no schedule or rate is documented). For: Apple, via the SensorKit request process.
- Exact background sampling cadence for heart rate and HRV, Apple does not publish it, and it materially affects missing-data modelling.

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

## Sources

1. ResearchKit & CareKit, Accessing SensorKit Data. https://www.researchandcare.org/resources/accessing-sensorkit-data/ (accessed 2026-08-21). Establishes SensorKit data categories, entitlement process, IRB requirement, and documented constraints.
2. ResearchKit & CareKit, FAQ. https://www.researchandcare.org/faq/ (accessed 2026-08-21). Establishes that raw ECG is not accessible via HealthKit and that higher-frequency HR is available during workouts/ECG sessions and via SensorKit.
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
13. Europe PMC records for Cohen JB et al. 2026, *Hypertension* (PMID 41564145) and *JAMA* (PMID 41661624), read 2026-10-10. Titles and DOIs only; disclosures not read.
