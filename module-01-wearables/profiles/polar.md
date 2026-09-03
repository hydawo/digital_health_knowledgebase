# Polar

## Quick Facts

| Field | Details |
|---|---|
| Organization | Polar Electro Oy, Finland |
| Category | Sports/physiology sensor manufacturer; the closest thing to research-grade hardware sold at consumer prices |
| Current status | Active |
| Platforms/devices | Polar H10 / H9 chest straps, Verity Sense / OH1 optical armbands, Vantage and Grit X watch lines, Pacer, Ignite, Polar 360/Loop, Polar Team Pro |
| Open source | **SDK is open source** (Polar BLE SDK, GitHub); devices and cloud are not |
| Hosting/deployment | Direct BLE streaming to a researcher's own app (no cloud required), **or** Polar Flow cloud + AccessLink API |
| Pricing model | Device purchase; no subscription for core use; SDK free |
| Last verified | 2026-08-21 |

## Summary

- Polar occupies a distinct and important position: it is the only vendor here that **sells raw-signal access as a first-class, openly documented, free feature** on inexpensive consumer hardware. The **Polar BLE SDK is open source on GitHub**, streams raw ECG and accelerometer directly over Bluetooth to an app the researcher writes, and requires no partner programme, no approval, no fee, and no vendor cloud.

- The **Polar H10 chest strap** is, in practice, the field-standard reference device for heart rate and RR-interval measurement in exercise and physiology research. Polar states it was used in over 600 scientific studies in 2022 to 2023 and describes it as a gold-standard reference technology for HR in field settings, a vendor claim, but one broadly consistent with how the device is used in the literature.

- The trade-off is that Polar is a **sensor company, not a longitudinal-monitoring ecosystem**. The H10 and Verity Sense are session devices: they need a phone or watch nearby (or use limited internal memory), they are not 24/7 wearables, and Polar offers nothing resembling a research participant-management platform. For continuous free-living monitoring across weeks, Polar's watch line goes through the Polar Flow cloud and AccessLink API, which is a much more conventional (and more limited) consumer API.

## Products / Platform Architecture

- Two quite different access paths, frequently confused:

### Path 1, Polar BLE SDK (direct, raw, no cloud)
- An open-source Android/iOS SDK that connects directly to Polar sensors over Bluetooth LE and streams raw data. No account, no cloud, no API key. Data lands in the researcher's own app. This is the research-relevant path.

### Path 2, Polar Open AccessLink (cloud API)
- Polar's REST API providing access to data recorded by Polar consumer devices and synced to Polar Flow, basic user information, training sessions, daily activity, and (on supported devices) sleep and recharge data. Conventional OAuth consumer API; summary-level.

### Path 3, Polar Team Pro
- A team-sport system: sensors with GNSS positioning and IMU, real-time telemetry, and an API for exporting performance data to third-party analysis platforms. Polar reports it was used in 180 scientific studies in 2022 to 2023.

## Sensors and Data Streams

- Every Module 1 profile uses the same table so devices can be compared row by row. Rows are the sensors named in `CLAUDE.md`. "Present" is about the hardware; "Researcher access" is about what a study can actually obtain, which is the module's central question. "Unclear" means nothing current was verified. The convention is recorded in [`../../shared/profile-table-conventions.md`](../../shared/profile-table-conventions.md).

| Sensor | Present | Researcher access to underlying signal | Resolution or sampling | Notes |
|---|---|---|---|---|
| PPG | Verity Sense | Raw PPG, 22-bit in SDK mode | 28 to 176 Hz in SDK mode | In SDK mode, HR and PPI streaming are not available; it is raw PPG and IMU or Polar's derived pulse intervals, not both. |
| ECG | H10 | Raw, in microvolts | 130 Hz | Verified from `documentation/products/PolarH10.md`. Internal memory logs HR only, so a phone-free protocol captures HR, not ECG. |
| Accelerometer | H10 and Verity Sense | Raw, per axis in mG | H10 25, 50, 100 or 200 Hz at plus or minus 2 to 8 g; Verity Sense 52 Hz normal, 26 to 416 Hz in SDK mode | The first pass recorded a contradiction on H10 accelerometry; the product documentation settles it as available. |
| Gyroscope | Verity Sense | Raw | 52 Hz normal, 26 to 416 Hz in SDK mode, up to 2000 degrees per second |  |
| Magnetometer | Verity Sense | Raw | 10 to 100 Hz, plus or minus 50 Gauss |  |
| Temperature | Watch line via SDK | Unclear | Unclear | Per-device rates for the watch line were not retrieved. |
| SpO2 | Unclear | Unclear | Unclear |  |
| GPS | Watch line | Unclear | Unclear |  |
| Barometer / altimeter | Unclear | Unclear | Unclear |  |
| EDA | No | Not applicable | Not applicable |  |
| Ambient light | No | Not applicable | Not applicable |  |
| Other | Heart rate and R-R interval (H10); PPI (Verity Sense) | Raw over BLE | 1 Hz HR with RR in ms | Verity Sense also records offline. |

**Verification.** Verified from Polar's per-product SDK documentation (`PolarH10.md`, `PolarVeritySense.md`) in the 2026-08-21 second pass; see the notes below for the two corrections that pass made.

### Notes from earlier verification passes

- *(Rewritten 2026-08-21 second pass from the per-product SDK documentation, which resolves the contradiction previously recorded here.)*

### Polar H10, verified stream specifications

| Stream | Specification |
|---|---|
| Heart rate | BPM **and RR interval in ms**, sample rate **1 Hz** |
| **ECG** | **130 Hz, in µV** |
| **Accelerometer** | **25 / 50 / 100 / 200 Hz**, ranges **±2 / ±4 / ±8 g**, per-axis in mG |
| HR broadcast | Continuous BLE transmission (standard HR profile) |
| Internal recording | Onboard logging, **HR only, 1-second sample interval**; start/stop and retrieve stored sessions |

- **Verified** (`documentation/products/PolarH10.md`).

- **Contradiction resolved.** The first pass recorded a conflict between Polar's research-tools page (claiming H10 gives "raw sample data, such as ECG and 3D acceleration") and the SDK README's device matrix (which did not mark accelerometer for H10). The product documentation settles it: **the H10 does stream triaxial accelerometry, at up to 200 Hz and ±8 g.** The README matrix was incomplete.

- Note the asymmetry in onboard recording: the H10 can *stream* ECG and ACC over BLE, but its **internal memory logs heart rate only**. A phone-free H10 protocol therefore captures HR, not ECG.

### Polar Verity Sense, verified stream specifications

- Normal mode, with both online streaming and **offline recording**:

| Stream | Specification |
|---|---|
| Heart rate | BPM |
| **PPG** | Raw PPG values |
| **PPI** | Pulse-to-pulse interval in ms (PPG-derived) |
| Accelerometer | **52 Hz**, ±8 g, per-axis in mG |
| **Gyroscope** | **52 Hz**, ±2000 °/s |
| **Magnetometer** | 10 / 20 / 50 / 100 Hz, ±50 Gauss |

- **SDK mode** (firmware 1.1.5+) substantially expands this:

| Stream | Rates | Range | Resolution |
|---|---|---|---|
| Accelerometer | **26 to 416 Hz** | ±2 to ±16 g | 16-bit |
| Gyroscope | **26 to 416 Hz** | 250 to 2000 °/s | 16-bit |
| **PPG** | **28 to 176 Hz** | | **22-bit** |
| Magnetometer | 10 to 100 Hz | ±50 Gauss | 16-bit |

- **Verified** (`documentation/products/PolarVeritySense.md`).

- **Two corrections to the first pass.** (1) The Verity Sense **has a gyroscope and magnetometer**, which the README matrix omitted, it is a full 9-axis IMU plus optical sensor. (2) The first pass listed ECG for Verity Sense; **the product documentation does not list ECG for this device**, and it would be surprising for an optical armband. Treat Verity Sense as PPG-only for cardiac signal.

- **In SDK mode, HR and PPI streaming/recording are not available**, you get raw PPG and IMU, but lose Polar's derived pulse intervals. That is a real design choice a protocol must make up front: Polar's PPI algorithm, or your own from 22-bit raw PPG at up to 176 Hz, but not both simultaneously.

### Watch line (Vantage V3/M3, Grit X2/Pro, Pacer/Pacer Pro)

- Accelerometer, gyroscope, magnetometer and temperature via the SDK, plus HR. Per-device rates were not retrieved for these models. **Unclear.**

### Why this matters

- **22-bit raw PPG at up to 176 Hz from a ~$95 armband, with a 9-axis IMU at up to 416 Hz, over an open-source SDK with no registration, no approval, no cloud and no fee, is the single most permissive raw-signal offer in this entire module.** It beats Samsung's 25 Hz accelerometer, beats Withings' ~25 Hz, and is obtained without a partner programme. The trade-off is form factor and wear duration, not signal quality.

## Derived Metrics / Analytics

- Via Polar Flow / AccessLink: training session summaries, daily activity, sleep, and Polar's proprietary recovery metrics (Nightly Recharge, Sleep Plus Stages, Training Load Pro, Recovery Pro, Orthostatic Test). These are conventional consumer-grade derived metrics.

- Via the BLE SDK: essentially none, you get signals, and the analysis is yours. That is the point.

## Active Data Collection

- None. Polar has no survey/EMA capability. A study needing self-report must pair Polar sensors with a separate instrument or a Module 2 platform.

## Researcher and Study Management Features

- **None from Polar directly** for the SDK path. Team Pro provides a coaching-oriented management console for squads with real-time telemetry, which some field studies repurpose, but it is not a research participant-management system.

- There is no enrolment portal, adherence dashboard, or remote configuration. A study using the BLE SDK is building all of that itself, or using a third-party platform. Several third-party research tools integrate Polar sensors (e.g. Fibion's research offerings; Stanford's `wearipedia` includes a Polar H10 extraction guide).

## Data Access and Export

| Route | What you get | Constraints |
|---|---|---|
| **BLE SDK live stream** | Raw ECG, ACC, PPG, PPI, gyro, magnetometer, temperature (device-dependent) | Requires a phone/app within Bluetooth range and running; you write the app |
| **Device internal memory** | H10 and Verity Sense have built-in memory for offline recording | Capacity-limited; a session-recording model, not weeks of continuous capture |
| **Polar Flow export** | Session files, CSV/TCX exports | Consumer-grade, summary-level |
| **Open AccessLink API** | Training sessions, daily activity, sleep, user info | OAuth; conventional consumer API; not raw |
| **Team Pro API** | Performance data for third-party analysis platforms | Team-sport oriented |

- The internal-memory feature is important for field research: **Verity Sense and H10 can record without a phone present** and be offloaded later, which enables protocols (swimming, occupational settings, paediatric use) where carrying a phone is impossible. Recording duration is limited and should be checked per device.

## APIs, SDKs, and Extensibility

- **Polar BLE SDK**, open source, Android and iOS, at https://github.com/polarofficial/polar-ble-sdk. Community wrappers exist for Flutter/Dart, Python (`polar-python`), and CocoaPods.
- **Polar Open AccessLink**, REST + OAuth.
- **Team Pro API**.
- Standard Bluetooth Heart Rate Profile support means H10/Verity Sense also work with generic BLE HR tooling and with third-party research apps out of the box, a low-friction integration path.
- Devices also support ANT+ (H10, Verity Sense), broadening compatibility with gym and lab equipment.

## Deployment and Infrastructure

- For the SDK path: none required beyond the researcher's own app and storage. **No vendor cloud is involved at all**, which is unusual and valuable, there is no vendor DPA, no rate limit, no retention policy, no API deprecation risk on the raw-data path.

- For AccessLink: vendor cloud, OAuth, standard.

## Participant Experience

- **H10 chest strap:** high fidelity, but a chest strap is uncomfortable for continuous multi-day wear, can cause skin irritation, and requires wetting the electrodes. Adherence over weeks is poor. It is a **session device**.
- **Verity Sense / OH1 armband:** worn on the upper arm or forearm, better tolerated than a chest strap, better signal than a wrist for exercise, but still not a 24/7 device and not a sleep device.
- **Polar watches (Vantage, Grit X, Pacer, Ignite, 360/Loop):** conventional wrist wearables with good battery life; these are the option for continuous free-living monitoring, at the cost of losing raw ECG.
- Polar 360 is a screenless band aimed at organisational/health-programme deployments.
- iOS and Android both supported.
- Devices are inexpensive relative to research-grade alternatives, making per-participant provisioning realistic.

## Privacy, Security, and Compliance

- The BLE SDK path is the strongest privacy story in this module: **no data leaves the participant's device except by the researcher's own code.** Compliance attaches entirely to the researcher's stack.
- For the Polar Flow/AccessLink path, Polar is EU-based (Finland), which is generally favourable for GDPR, but specific DPA terms, data residency, HIPAA posture, and certifications were **not verified** in this session.

## Pricing

- **SDK: free and open source.** No partner programme, no approval gate, no licence fee. This is the cheapest path to raw physiological signal in the entire module.
- **Devices:** H10 and Verity Sense are inexpensive consumer sensors (roughly in the €80, €120 class at retail; verify current pricing). Watches span a wider range. Team Pro is a system-level purchase.
- **No subscription** for core functionality.
- Polar Flow / AccessLink: no documented API fee.
- **Cost per raw-ECG-capable participant is roughly an order of magnitude below Empatica and ActiGraph/Ametris.**

## Research Evidence and Validation

- **Polar H10 is the de facto field reference for HR and RR intervals.** Polar states it was used in over 600 scientific studies in 2022 to 2023 and describes it as a golden-standard reference technology for HR measurement in field settings. It is routinely used *as the criterion measure* when validating other wearables, which is itself the strongest evidence of its standing, though it also means the H10's own validation is somewhat circular in the applied literature.
- Polar reports Team Pro was used in 180 scientific studies over the same period and that over 1,000 peer-reviewed papers per year cite Polar technology. **These are vendor claims** (status: Reported) and the counting methodology is not stated.
- Polar's *watch-based* consumer metrics have not fared as well: Polar was not included in either the 2024 *Sensors* or 2025 Schyvens PSG comparisons, so its sleep-staging validity against PSG is **not established** by those benchmarks.
- The critical distinction: **Polar's raw-signal hardware is well validated; Polar's derived consumer metrics are not particularly better evidenced than any competitor's.** Use Polar for signals, not for scores.

## Strengths

- **Free, open-source SDK with raw ECG, accelerometer, PPG, and beat-to-beat intervals**, no approval, no fee, no vendor gatekeeping. Unique in this module.
- H10 is the accepted field reference for HR/RR and is cheap enough to deploy widely.
- HRV computed by the researcher from RR intervals, using published methods, full construct transparency, no vendor black box.
- No vendor cloud on the raw path: no rate limits, no retention policy, no API deprecation risk, minimal compliance surface.
- On-device memory enables phone-free recording in constrained settings.
- Standard BLE HR profile and ANT+ support give broad third-party compatibility.
- Very low cost per participant for raw-signal capability.
- iOS and Android.
- EU-based vendor, favourable for GDPR-sensitive studies.

## Limitations

- **Not a continuous-monitoring ecosystem.** Chest straps and armbands are session devices; adherence over weeks is poor.
- **No study management of any kind**, no enrolment, no adherence monitoring, no remote configuration.
- Requires the research team to write a mobile app for the SDK path (or adopt third-party tooling).
- The raw path requires a phone in Bluetooth range and running, or reliance on limited internal memory.
- Watch-line consumer metrics are unremarkable and their sleep staging is unvalidated against PSG in the major comparisons.
- Device capability matrix in the SDK documentation contains at least one apparent error; per-device verification is necessary.
- Sampling rates not documented at the top level of the SDK.
- No survey/EMA capability.
- AccessLink is a conventional summary-level consumer API, not a research API.

## Best-Fit Use Cases

- **HRV research** requiring genuine beat-to-beat intervals and researcher-computed metrics.
- Exercise physiology, sports science, and cardiac autonomic function research.
- Ambulatory/laboratory sessions, stress-reactivity protocols, and paced-breathing studies.
- Providing the **criterion measure** in a study validating another wearable.
- Studies needing raw signal on a small budget.
- Studies where no data may touch a vendor cloud.
- Occupational and field settings where a phone cannot be carried (using onboard memory).

## Poor-Fit Use Cases

- Multi-week or multi-month continuous free-living monitoring on a single device.
- Sleep staging research.
- Large remote cohorts needing adherence monitoring and automated data collection.
- Studies without mobile development capacity and without third-party tooling.
- Studies requiring integrated survey/EMA.
- Step count, energy expenditure, or general activity as primary endpoints (use a wrist device or research-grade actigraph instead).

## Open Questions

- *(Directed to Polar: https://www.polar.com/en/developers , research enquiries via https://www.polar.com/en/science/ )*

- ~~Resolve the device capability matrix~~, **RESOLVED from the per-product SDK docs.** H10 does
- stream accelerometry (25/50/100/200 Hz, ±2/4/8 g). Verity Sense does **not** list ECG, but does have gyroscope and magnetometer. The SDK README matrix is incomplete; the product docs govern.
- Documented sampling rates and configurable ranges for H10 ECG/ACC and Verity Sense PPG/ACC.
- Internal memory recording capacity and maximum continuous duration for H10 and Verity Sense.
- Battery life under continuous raw streaming for each sensor.
- Whether Open AccessLink exposes any beat-to-beat/RR data, or only session summaries.
- AccessLink rate limits, historical depth, and backfill.
- Polar Flow / AccessLink GDPR DPA terms, data residency, HIPAA posture, certifications.
- Methodology behind the "600 studies" and "1,000 papers per year" claims.
- Polar 360's data-access model, is it SDK-accessible or cloud-only?

## Key Links

- Official site: https://www.polar.com/
- Developers portal: https://www.polar.com/en/developers
- **Polar BLE SDK (GitHub, open source):** https://github.com/polarofficial/polar-ble-sdk
- H10 SDK documentation: https://github.com/polarofficial/polar-ble-sdk/blob/master/documentation/products/PolarH10.md
- Verity Sense SDK documentation: https://github.com/polarofficial/polar-ble-sdk/blob/master/documentation/products/PolarVeritySense.md
- Research tools: https://www.polar.com/en/science/research-tools/
- Polar science: https://www.polar.com/en/science
- Open AccessLink: https://www.polar.com/accesslink-api/
- Polar Team Pro: https://www.polar.com/en/business/team-pro
- Third-party extraction guide (Stanford wearipedia): https://wearipedia.readthedocs.io/en/latest/notebooks/polar_h10.html

## Sources

1. Polar BLE SDK repository. https://github.com/polarofficial/polar-ble-sdk (accessed 2026-08-21). **Primary.** Establishes open-source status, Android/iOS support, streamable data types (HR, ECG, ACC, PPG), and the per-device support matrix, the latter containing apparent errors, see body text.
2. Polar, Research tools. https://www.polar.com/en/science/research-tools/ (accessed 2026-08-21). **Primary (vendor).** Establishes H10 raw ECG and 3D acceleration access, Verity Sense PPG and acceleration with built-in memory and SDK connectivity, Open AccessLink's scope, Team Pro's GNSS/IMU/real-time telemetry and API, and the vendor claims of 600+ H10 studies, 180 Team Pro studies (2022 to 2023), and 1,000+ papers per year.
3. Polar developers portal. https://www.polar.com/us-en/developers (accessed 2026-08-21).
4. Polar H10 and Verity Sense per-product SDK documentation. https://github.com/polarofficial/polar-ble-sdk/blob/master/documentation/products/PolarH10.md ; .../PolarVeritySense.md (identified; **not retrieved in this session**, the source that should resolve the capability-matrix discrepancy).
5. Fibion, "Using Polar SDK & API in Research." https://web.fibion.com/articles/polar-sdk-api-research-fibion/ (accessed 2026-08-21). Secondary; corroborates real-time streaming of HR, RR intervals, and accelerometer from H10 and Verity Sense.
6. Stanford wearipedia, Polar H10 extraction guide. https://wearipedia.readthedocs.io/en/latest/notebooks/polar_h10.html (accessed 2026-08-21). Evidence of academic tooling.
7. Schyvens A.-M. et al. *SLEEP Advances* 2025;6(2):zpaf021. https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472, noted as **not** including Polar.
