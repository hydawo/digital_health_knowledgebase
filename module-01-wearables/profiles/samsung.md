# Samsung (Galaxy Watch / Galaxy Ring / Samsung Health SDK Suite)

## Quick Facts

| Field | Details |
|---|---|
| Organization | Samsung Electronics |
| Category | Consumer wearable ecosystem with an unusually research-oriented SDK suite |
| Current status | Active |
| Platforms/devices | Galaxy Watch4 and later (Wear OS powered by Samsung), Galaxy Ring, Galaxy phones; **Android only** |
| Open source | Partly — **Samsung Health Research Stack is open source** (GitHub: S-HealthStack); the SDKs themselves are not |
| Hosting/deployment | On-device SDK access; Research Stack backend is self-hosted by the researcher |
| Pricing model | Device purchase; no documented SDK fee; access gated by partner-programme approval |
| Last verified | 2026-08-21 |

## Summary

Samsung is the **most under-appreciated platform in this module for researchers who need raw signals from a consumer device.** The Samsung Privileged Health SDK (part of the Samsung Health SDK Suite, announced September 2024) exposes **raw sensor data from the BioActive sensor** — accelerometer, PPG, ECG, and heart rate with inter-beat intervals — directly to approved partner applications running on the watch. No other mainstream consumer smartwatch vendor offers this. Apple does not expose raw PPG; Fitbit, Garmin, Oura, and WHOOP expose neither raw PPG nor raw accelerometry.

Samsung pairs this with **Samsung Health Research Stack**, an open-source end-to-end research platform (app SDK + backend + web portal) that the research team self-hosts. Taken together, Samsung offers something close to "research-grade access on consumer hardware with an open-source study platform" — a combination nobody else provides.

The costs are equally clear: **Android only** (no iOS), the access model is on-device rather than a cloud cohort API, partner-programme approval is required, and the validation literature is far thinner than Fitbit's or Apple's.

## Products / Platform Architecture

The Samsung Health SDK Suite has four components:

| Component | What it does | Research relevance |
|---|---|---|
| **Sensor SDK / Samsung Privileged Health SDK** | Raw and processed sensor data from the BioActive sensor, on-watch | The core reason to consider Samsung |
| **Data SDK** | Integrated health data across Galaxy Watch, Galaxy Ring, phones, and third-party devices | Aggregation layer, added from October 2024 |
| **Accessory SDK** | Connectivity to accessories | Peripheral |
| **Samsung Health Research Stack** | Open-source app SDK + backend service + web portal for study design and data analysis | Full study platform, self-hosted |

Data flow for the Sensor SDK is **on-device**: a Wear OS app you build runs on the watch, subscribes to sensor trackers, and receives data locally. Notably, the SDK **operates independently and does not share data with Samsung Health** — meaning the research app's data path is separate from Samsung's consumer cloud. From a data-custody perspective this resembles the Apple/HealthKit model (researcher controls the pipeline) but with far better sensor access.

There is **no Samsung cloud REST API** for pulling a cohort's data the way Fitbit, Garmin, Oura, and WHOOP offer. On Android, Samsung Health data can also flow into **Health Connect**, the OS-level aggregation layer, which is a separate integration path exposing processed data types only.

## Sensors and Data Streams

Samsung Privileged Health SDK trackers:

**Continuous trackers:**
| Tracker | Detail |
|---|---|
| Accelerometer | **25 Hz** |
| Heart rate | Including **IBI (inter-beat intervals)** for HRV computation |
| PPG | Raw photoplethysmogram; a notable update added **continuous access to PPG Infrared (IR) and Red LED data for the first time** (previously green only) |
| Skin temperature | Continuous |

**On-demand trackers:**
| Tracker | Detail |
|---|---|
| ECG | Raw electrocardiogram |
| BIA | Bioelectrical impedance analysis (body composition) |

**Constraint:** only one on-demand tracker type can be used at a time. Supported tracker types also **vary by watch model and software version**, so a heterogeneous device fleet will have heterogeneous capability — verify per model before purchasing.

Other sensors present on Galaxy Watch hardware (SpO2, barometer, GPS on LTE/GPS models, gyroscope, ambient light) are exposed through standard Wear OS/Android sensor APIs rather than the privileged SDK; researchers should not assume the privileged SDK is the only route.

**Galaxy Ring** is Samsung's ring-form competitor to Oura, integrated through the Data SDK. Its raw-data access story is **not established** and should not be assumed to match the watch.

## Derived Metrics / Analytics

Through the Data SDK and Samsung Health: steps, sleep with stages, heart rate, stress, blood oxygen, body composition, energy score, and workouts. These are consumer-processed metrics comparable to competitors'.

The research value, though, is that Samsung lets you **bypass** the derived layer entirely and compute your own metrics from raw PPG/ECG/ACC — which means metric definitions are under the researcher's control and are not silently changed by a firmware update. That is a genuine methodological advantage for longitudinal work.

## Active Data Collection

**Samsung Health Research Stack** provides the survey/task layer: it includes an app SDK for building study apps, a backend service managing collected data, and a web portal for research design and data analysis. This is the only vendor-published, open-source, end-to-end research platform among the major consumer wearable manufacturers.

Version history: Health Stack Alpha (2022) → Health Stack 1.0 (2023) → **Samsung Health Research Stack 2.0 Beta (September 2024)**, rebranded to emphasise research, with the 2.0 line integrating data from the Sensor and Data SDKs. Code is at the S-HealthStack GitHub organisation.

## Researcher and Study Management Features

Provided by the Research Stack's web portal — study design, participant data management, and analysis support — rather than by a Samsung-operated SaaS. Because the researcher hosts the backend, they also own the study console. This is functionally similar to the Module 2 self-hosted platform model (Beiwe, RADAR-base) rather than the consumer-wearable SaaS model.

## Data Access and Export

| Route | Mechanism | Notes |
|---|---|---|
| Privileged Health SDK | On-watch app subscribes to trackers | Raw signals; requires partner approval |
| Data SDK | On-device integrated health data | Processed metrics, multi-source |
| Health Connect | Android OS aggregation layer | Processed types only; separate integration |
| Research Stack | Self-hosted backend | Researcher controls storage, export, and retention |
| Participant self-export | Samsung Health app export | Available; format/completeness not verified |

**No cloud cohort-pull API.** Everything routes through code you deploy to the device.

## APIs, SDKs, and Extensibility

- Samsung Privileged Health SDK (Wear OS, Kotlin/Java).
- Samsung Health Data SDK.
- Samsung Health Research Stack (open source).
- Health Connect (Android platform-level).
- Wear OS / Android standard sensor APIs.

**Access process for the Privileged Health SDK:**
1. Download the SDK from Samsung's developer portal.
2. Enable developer mode for testing and debugging (testing only — not for deployment).
3. **Submit a partnership request to the Samsung Partner Program** to distribute publicly, supplying the app's package name and SHA-256 signature.
4. Apps that are unregistered or whose signature does not match receive `SDK_POLICY_ERROR`.

This signature-binding is worth flagging operationally: **the approved app build is cryptographically pinned.** Changing signing keys, or distributing a rebuilt variant, requires going back through registration.

## Deployment and Infrastructure

- Sensor access: on-device, no infrastructure needed for capture — but capture is only half the problem; the study must move data off the watch.
- Research Stack backend: self-hosted (containerised deployment via the S-HealthStack repositories). This means the research team needs cloud/DevOps capability, comparable to running a Module 2 platform.
- Data residency and compliance are consequently under the researcher's control — an advantage for EU/GDPR studies and for institutions that will not permit vendor cloud storage.

## Participant Experience

- **Android only, and specifically Galaxy.** Requires a Galaxy Watch4 or later; the SDK does not support phones or emulators. This is a hard exclusion of iPhone users and of non-Samsung Android users for the watch component.
- Battery life on Galaxy Watch is roughly 1–2 days in normal use; **continuous raw sensor capture will reduce this substantially** (raw PPG/ACC subscription is power-hungry). Any study using the privileged SDK must pilot battery life under its actual sampling configuration, and should expect charging burden closer to Apple Watch than Garmin.
- Requires the participant to install the study app and grant permissions.
- Galaxy Watch is a mainstream, well-accepted consumer device with good comfort and wear compliance.

## Privacy, Security, and Compliance

- The privileged SDK's separation from Samsung Health means the study's data does not flow into Samsung's consumer cloud — the research pipeline is the researcher's own.
- Because the Research Stack is self-hosted, **HIPAA/GDPR analysis attaches to the researcher's infrastructure**, not to Samsung. As with Apple, there is no vendor DPA to negotiate for the study copy of the data.
- Samsung Partner Program terms, and any restrictions they place on research use or publication, were **not retrieved** in this session and are an open question.

## Pricing

- No SDK licence fee is documented. The gate is partner-programme approval, not payment.
- Costs: Galaxy Watch hardware (mid-range consumer pricing, generally below Apple Watch), plus the engineering and hosting cost of the Wear OS app and Research Stack backend.
- No consumer subscription is required for the data.
- **Not established:** whether the Samsung Partner Program imposes any commercial terms on academic applicants.

## Research Evidence and Validation

- The systematic review of steps/energy expenditure/heart rate found **Apple and Samsung had the highest validity for step count**, and that Samsung measured steps accurately in laboratory settings.
- Energy expenditure: unacceptable across all brands including Samsung (MAPE >30%).
- **Sleep staging:** Samsung was **not** included in either of the two major recent PSG validations (the 2024 *Sensors* three-device study or the 2025 Schyvens six-device study). Its sleep-staging validity against PSG is therefore **not established** by the strongest available comparative evidence — a real gap.
- The much more important point for research: because raw ECG/PPG/ACC are accessible, **a study does not have to rely on Samsung's derived metrics at all.** Validation of Samsung's consumer algorithms becomes largely irrelevant if the researcher computes their own outputs from the raw signal using published, validated methods. This inverts the usual validation problem.
- Third-party research tooling exists — e.g. the CLAID framework (ETH Zurich) publishes a Galaxy Watch collector — indicating the platform is in genuine academic use.

## Strengths

- **Raw PPG (green, IR, red), raw ECG, raw accelerometer at 25 Hz, and IBI on consumer hardware** — unmatched among mainstream consumer wearables.
- Researcher can define and compute their own metrics, insulating a longitudinal study from vendor algorithm drift.
- **Open-source, self-hosted, end-to-end research platform** (Research Stack) published by the manufacturer.
- Full data custody; no vendor cloud in the study's data path; data residency under researcher control.
- No subscription, no API fee.
- Good step-count validity.
- Galaxy Ring available for ring-form designs within the same ecosystem.

## Limitations

- **Android/Galaxy only.** Cannot support iPhone users, which is disqualifying for many representative-sample designs and for most US general-population studies.
- **No cloud cohort API** — all access requires deploying and maintaining a Wear OS app.
- High technical burden: Wear OS development plus self-hosted backend. Comparable to running a Module 2 platform.
- Battery cost of continuous raw capture is significant and must be piloted.
- Tracker availability varies by watch model and software version.
- Only one on-demand tracker (ECG or BIA) at a time.
- Partner-programme approval required, with cryptographic app-signature pinning that complicates build management.
- Sleep staging validity against PSG not established.
- Thin comparative validation literature relative to Fitbit and Apple.
- Galaxy Ring raw-data access unverified.

## Best-Fit Use Cases

- Studies that need **raw physiological signals** but cannot afford or justify research-grade hardware (Empatica, ActiGraph/Ametris) for every participant.
- Cardiovascular and autonomic research needing raw ECG and IBI from a device participants will actually wear all day.
- Signal-processing and algorithm-development research — building and validating new digital biomarkers on consumer hardware.
- Studies requiring full data custody and self-hosted infrastructure for institutional or regulatory reasons.
- Android-only cohorts, or studies already provisioning Android devices.
- Longitudinal studies that must protect metric definitions from vendor algorithm changes.

## Poor-Fit Use Cases

- Any study requiring iOS participants on the same device platform.
- Teams without Android/Wear OS development capacity and backend/DevOps capability.
- Studies wanting a quick, low-effort cohort data pull.
- Studies depending on Samsung's derived sleep-stage outputs as validated endpoints.
- BYOD designs in populations where Galaxy Watch penetration is low.

## Open Questions

*(Directed to Samsung: https://developer.samsung.com/health — Samsung Partner Program request.)*

- What are the eligibility criteria, timeline, and terms of the Samsung Partner Program for **academic** applicants? Are universities routinely approved?
- Do the Partner Program terms restrict publication, data sharing, or open deposition of raw-signal data?
- What are the actual maximum sampling rates and configurability for each tracker (is accelerometer fixed at 25 Hz, or is that a default)? What is the raw PPG sampling rate?
- Measured battery life under continuous raw PPG + ACC subscription, per model.
- Which trackers are available on which specific Galaxy Watch generations and software versions?
- Does the Galaxy Ring expose raw data, and through which SDK?
- Current maintenance status and production-readiness of Samsung Health Research Stack 2.0 (is it still Beta?).
- On-device buffering and offline behaviour: how much raw data can the watch hold if the phone is absent?
- Samsung's HIPAA/GDPR posture for any component that does touch Samsung infrastructure.

## Key Links

- Samsung Health developer hub: https://developer.samsung.com/health
- Samsung Health Sensor SDK overview: https://developer.samsung.com/health/sensor/overview.html
- Privileged Health SDK FAQ: https://developer.samsung.com/health/privileged/faq.html
- Sensor SDK API reference: https://developer.samsung.com/health/sensor/api-reference/overview-summary.html
- Samsung Health Research Stack: https://developer.samsung.com/health/s-healthstack
- Research Stack GitHub organisation: https://github.com/S-HealthStack
- Research Stack backend: https://github.com/S-HealthStack/backend-system
- Research Stack release notes: https://developer.samsung.com/health/research/release-notes/v11.html
- SDK Suite announcement: https://news.samsung.com/global/samsungs-new-health-software-development-kit-suite-powers-advancements-in-healthcare-innovation
- Health Connect (Android): https://developer.android.com/health-and-fitness/health-connect

## Sources

1. Samsung Privileged Health SDK FAQ. https://developer.samsung.com/health/privileged/faq.html (accessed 2026-08-21). **Primary.** Establishes continuous trackers (accelerometer 25 Hz, heart rate with IBI, PPG, skin temperature), on-demand trackers (ECG, BIA, one at a time), Galaxy Watch4+ Wear OS exclusivity, no phone/emulator support, the partner-request process with package name and SHA-256 signature, `SDK_POLICY_ERROR` behaviour, model/version-dependent tracker availability, and that the SDK does not share data with Samsung Health.
2. Samsung Health Sensor SDK overview. https://developer.samsung.com/health/sensor/overview.html (accessed 2026-08-21).
3. Samsung Mobile Press — Health SDK Suite announcement, September 2024. https://www.samsungmobilepress.com/articles/samsungs-new-health-software-development-kit-suite-powers-advancements-in-healthcare-innovation (accessed 2026-08-21). Establishes the four-component suite, raw BioActive sensor access, first-time continuous PPG IR and Red LED access, the Data SDK from October, and Research Stack 2.0 integration plans.
4. Samsung Newsroom — Samsung Health Research Stack. https://news.samsung.com/global/samsung-electronics-unveils-samsung-health-research-stack (accessed 2026-08-21). Establishes the open-source app SDK + backend + web portal architecture and the Alpha → 1.0 → 2.0 Beta timeline.
5. Samsung Health Research Stack GitHub. https://github.com/S-HealthStack (accessed 2026-08-21).
6. Fuller D. et al. *JMIR mHealth uHealth* 2020;8(9):e18694. https://mhealth.jmir.org/2020/9/e18694/ — Samsung among highest step-count validity; energy expenditure unacceptable across brands.
7. CLAID framework Galaxy Watch collector (ETH Zurich). https://claid.ethz.ch/framework_components/Packages/data_collection/GalaxyWatchCollector/ (accessed 2026-08-21). Evidence of academic tooling.
