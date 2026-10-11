# Movesense

## Quick Facts

| Field | Details |
|---|---|
| Organization | Movesense Ltd (Vantaa, Finland); independent of Suunto since a management buy-out effective 1 October 2021 ([news post](https://www.movesense.com/news/2021/09/movesense-grows-independent-from-suunto/); [Terms](https://www.movesense.com/terms/), 2026-10-11) |
| Category | Open, programmable research-grade sensor platform |
| Current status | Active |
| Platforms/devices | Movesense MD, Movesense Flash, Movesense HR2, Movesense HR+; CardioRTHM clinical solution |
| Open source | **No.** Developer tools and APIs are free of charge, but the SDK is licensed under a proprietary 12-month "SDK License and Evaluation Agreement" for evaluation and development only; custom sensor firmware permitted under it (re-verified 2026-10-10). The Showcase app and sample source in the mobile library are Apache 2.0, and sbem-tools is MIT (repository READMEs, 2026-10-11) |
| Hosting/deployment | **None required**, BLE to your own app, or onboard logging |
| Pricing model | Device purchase (Movesense MD €349 ex VAT for 1 to 49 units); developer kits €249 to €399; volume pricing on request; **no software licence fee**; no general academic pricing; free sensors for selected academic projects (Movesense Academic Program) |
| Last verified | 2026-10-11 (vendor fact record) |

## Summary

- Movesense was missing from the first research pass and should not have been. It is the closest thing in this module to a *programmable* research sensor: a small coin-shaped device with a 9-axis IMU and a single-lead ECG front end, an open API, no licence fee, and, uniquely here, **the explicit ability to write and flash your own firmware onto the sensor**.

- Where Polar gives you an open SDK to *read* a fixed device, Movesense lets you change what the device does. For methods research, unusual protocols, or on-sensor processing to save power and bandwidth, that is a categorical difference.

- It also holds something no other device in this module does at this price point: **Movesense MD is a Class IIa medical device under EU MDR 2017/745.**

- The two are alternatives on the MD, not a combination. Firmware a team writes itself is not covered by the MD's MDR registration; a study that relies on medical-device status must run certified Movesense firmware ([MDR news post, 2023](https://www.movesense.com/news/2023/02/movesense-medicals-mdr-registration-approaches-what-does-it-mean-for-movesense-md-customers/); [medical_sw docs](https://movesense.com/docs/medical/medical_sw/), 2026-10-11).

## Products / Platform Architecture

| Product | ECG | Onboard memory | Regulatory | Notes |
|---|---|---|---|---|
| **Movesense MD** | Clinical-grade single-channel | | **Class IIa Medical Device, MDR 2017/745** (product number MS060222000; older SS050341000 stock is MDD 93/42/EEC) | The regulated variant; Class IIa only with certified Movesense firmware. IP68 water and shock proof; user-replaceable Maxell CR2025 coin cell ([MD FAQ news post, 2024-06-17](https://www.movesense.com/news/2024/06/faq-regarding-movesense-md-medical-sensor/), read 2026-10-11) |
| **Movesense Flash** | Clinical-grade single-channel | **128 MB internal memory for autonomous logging** | Non-medical | The phone-free option |
| **Movesense HR2** | 1-lead (non-medical) | | Non-medical | 9.4 g; water and shock resistant |
| **Movesense HR+** | Heart rate | | Non-medical | Entry sensor |
| **CardioRTHM** | | | Clinical solution | Short and long-term heart rhythm monitoring product built on the platform |

- **Verified** (movesense.com/specifications/).

- Company positioning covers three audiences: healthcare professionals (CardioRTHM), med-tech companies integrating the MD sensor, and sport-tech companies using the Sport family.

## Sensors and Data Streams

- Every Module 1 profile uses the same table so devices can be compared row by row. Rows are the sensors named in `CLAUDE.md`. "Present" is about the hardware; "Researcher access" is about what a study can actually obtain, which is the module's central question. "Unclear" means nothing current was verified. The convention is recorded in [`../../shared/profile-table-conventions.md`](../../shared/profile-table-conventions.md).

| Sensor | Present | Researcher access to underlying signal | Resolution or sampling | Notes |
|---|---|---|---|---|
| PPG | No | Not applicable | Not applicable |  |
| ECG | Yes, single lead | Raw | 125, 128, 200, 250, 256, 500 or 512 Hz | Verified (FAQ, 2026-10-11). Movesense advises against streaming above 256 Hz over BLE. |
| Accelerometer | Yes | Raw | From 13 Hz; maximum is a vendor conflict (1666 Hz in API reference examples, 416 Hz on the Flash Developer Kit spec, 833 Hz on the HR2 page) | Conflicting documentation (2026-10-11). Part of the 9-axis IMU. |
| Gyroscope | Yes | Raw | Same conflict as accelerometer | Conflicting documentation. |
| Magnetometer | Yes | Raw | Same conflict as accelerometer | Conflicting documentation. |
| Temperature | Yes, all models | Raw, internal device temperature, non-medical | Unclear | Verified (API reference, 2026-10-11). |
| SpO2 | No | Not applicable | Not applicable |  |
| GPS | No | Not applicable | Not applicable |  |
| Barometer / altimeter | Unclear | Unclear | Unclear |  |
| EDA | No | Not applicable | Not applicable |  |
| Ambient light | No | Not applicable | Not applicable |  |
| Other | R-R intervals; heart rate over the standard BLE profile | Raw | 1 ms accuracy and resolution for R-R | Verified. Connectivity is Bluetooth Low Energy. |

**Verification.** Vendor fact record, 2026-10-11 ([FAQ](https://www.movesense.com/faq/), [API reference](https://www.movesense.com/docs/esw/api_reference/), [Flash Developer Kit](https://www.movesense.com/product/movesense-flash-developer-kit/), [HR2 page](https://www.movesense.com/product/movesense-sensor-hr2/)). 512 Hz ECG is a research-instrument specification. The 1666 Hz IMU figure appears only in example API responses, not on any product spec sheet, and Movesense warns the highest rates may be limited by BLE bandwidth; whether it works on every model and over BLE needs vendor confirmation.

### Notes from earlier verification passes

| Stream | Specification | Confidence |
|---|---|---|
| **ECG** | **125 Hz to 512 Hz**, single-lead | **Corroborated** |
| **R, R intervals** | **1 ms accuracy and resolution** | **Verified** |
| **IMU, 9-axis** | Accelerometer + gyroscope + magnetometer, all triaxial. From 13 Hz; maximum 416, 833 or 1666 Hz depending on the vendor source | **Conflict** (corrected 2026-10-11 from "13 Hz to 1.6 kHz, Corroborated") |
| Temperature | Non-medical internal temperature sensor, all models | **Verified** (corrected 2026-10-11 from "MD and Flash") |
| Heart rate | Standard BLE heart rate profile | **Verified** |
| Connectivity | Bluetooth Low Energy | **Verified** |

- **512 Hz ECG and an IMU of at least 416 Hz on every published spec are research-instrument specifications, not consumer ones.** For comparison, Polar H10 tops out at 130 Hz ECG and 200 Hz accelerometry; Samsung's Health Sensor SDK (formerly the Privileged Health SDK) gives 25 Hz continuous accelerometry. The Axivity AX3 logger goes higher for accelerometry alone (up to 3,200 Hz; see `axivity-geneactiv.md`). If the 1666 Hz API figure holds, Movesense's IMU ceiling is roughly 8× the Polar Verity Sense's SDK-mode maximum and 64× Samsung's; on the 416 Hz spec sheet figure it is roughly 2× and 16×.

## Derived Metrics / Analytics

- Essentially none from the vendor, by design, this is a signal source, not an insights platform. Heart rate and R, R intervals are provided; everything else is the analyst's.

- Standard firmware computes average heart rate and R-R intervals at 1 ms on the sensor; nothing else. The Movesense ECG Recorder app (v2.1 and later) adds ECG and HRV visualizations and two ECG analysis reports ([App Store](https://apps.apple.com/us/app/movesense-ecg-recorder/id6443902831), 2026-10-11).
- **Kubios** HRV use is a file workflow (record in the Showcase app, save CSV, open in Kubios HRV), not an integration (corrected 2026-10-11; [Movesense Kubios post](https://www.movesense.com/news/2022/08/kubios-and-movesense-combine-advanced-ecg-and-hrv-analysis-tools/)). Fibion resells the Flash sensor as an HRV research kit with Kubios-ready export.

## Active Data Collection

- None. No survey or EMA layer. (Note that **Labfront** supports Movesense Medical, HR2 and Flash alongside Garmin and Dexcom, and Labfront does provide EMA, see `data-intermediaries.md`. On Labfront, participants must start each Movesense recording manually through a task, which bears on adherence; [Labfront help](https://help.labfront.com/movesense-overview), 2026-10-11.)

## Researcher and Study Management Features

- No study management, participant management or dashboards. Movesense does publish free recording tools: the Showcase app (CSV, JSON), a Python client for the GATT SensorData Protocol in the default firmware, the Movesense ECG Recorder app for the MD, and a Python datalogger for Flash offline logging ([five free tools post, 2025-11](https://www.movesense.com/news/2025/11/recording-data-with-movesense-sensors-five-free-tools-to-get-you-started/), 2026-10-11). Study management is available indirectly through Labfront.
- **Movesense Academic Program** (movesense.com/movesense-academic-program, read 2026-10-10). "Movesense supplies the selected research teams with a limited number of Movesense sensors and associated accessories such as heart rate straps", sized to the project, plus technical support; no charge is mentioned. Researchers apply by online form with a project description, timeline and planned use. The review cadence is a vendor conflict: the program page says applications are reviewed monthly, the application form says weekly (both read 2026-10-11); both say Movesense "invites up to three projects per quarter". Selection criteria include innovativeness, "Potential of commercial applications of the project results", potential to build awareness for Movesense, and "Additional non-published criteria". Selected teams must mention Movesense in publications and allow Movesense to list the project. The page says the program "started on November, 2019 and is open until further notice", but the latest cohort it lists is Q1 2023. At least one validation study (Martín Gómez 2024, below) received sensors through it. **Verified.** The program is **active**: a December 2025 news post announced a Ca' Foscari University of Venice project joining it ([news post](https://www.movesense.com/news/2025/12/university-of-venice-studies-seismocardiography-with-movesense-md-sensors/), read 2026-10-11), so only the page's project list is stale (corrected 2026-10-11 from "Unclear").
- **What academics get:** the same data any developer gets (raw ECG, IMU and R-R over BLE or onboard logging, no cloud, no user caps or data-use terms from Movesense), under the same SDK licence. The program changes the hardware cost, not the data.

## Data Access and Export

- **BLE streaming** to a researcher-built or third-party app.
- **Laptop collection without custom firmware** through the GATT SensorData Protocol in the default firmware and its Python client.
- **Onboard logging** on Movesense Flash, 128 MB, phone-free; the memory stops writing when full. Movesense says it holds up to five days of single-channel ECG, over four months of heart rate intervals, or almost 19 hours of 52 Hz 9-axis motion ([March 2026 news post](https://www.movesense.com/news/2026/03/improved-ecg-imu-data-logger-for-movesense-flash-now-available/), read 2026-10-11). HR2, HR+ and MD have 384 kB EEPROM used as a ring buffer that overwrites the oldest data ([hardware variants](https://www.movesense.com/docs/system/hw_variants/)).
- Export formats: CSV and JSON (Showcase app); CSV, PDF and, for the MD, EDF+ (ECG Recorder app), plus .fit export of heart rate intervals.
- No cloud, no API keys, no rate limits, no retention policy but yours.
- Data custody is 100% institutional on the own-app and developer-tool route; data does not go to Movesense servers ([FAQ](https://www.movesense.com/faq/)).
- **Exception, the Movesense ECG Recorder app.** It stores recordings locally and makes an anonymized backup to Movesense servers, in countries not stated. Movesense is the controller, keeps personal data while the user has an app username or as long afterwards as it deems necessary, and may use anonymized ECG data for "product development, research etc." ([app data protection statement](https://www.movesense.com/movesense-ecg-recorder-app-data-protection-statement/), 2026-10-11).

## APIs, SDKs, and Extensibility

- Movesense states the platform provides "powerful, low-cost tools for creating your own sensor firmware or compatible mobile app," with **"no license cost involved."** Open APIs, sample code, a **desktop simulator**, and documentation are provided. Software repositories are hosted on Bitbucket. Firmware can be uploaded to the sensor through the Movesense Showcase mobile app. **Verified** (movesense.com/get-started/).
- **SDK licence (read 2026-10-10, Verified).** The licence file in the official `movesense-device-lib` repository is the proprietary "Movesense Software Development ("SDK") License and Evaluation Agreement" with Movesense Ltd. It is not an open-source licence.
  - "Purpose" means "the Licensees' evaluation, testing and potential development of a software application"; "possible commercialization of the Application ... is subject to a separate agreement".
  - "the Licensee shall not incorporate or integrate the Licensed Technology or any part thereof in any products or services", and may not reverse engineer it.
  - The agreement runs for twelve months from signature; either party may terminate on 30 days' notice, and on termination the licensee must destroy or return the Licensed Technology within five days.
  - No fee clause appears, consistent with "no license cost".
  - The Terms page carries a parallel twelve-month Limited Evaluation Licence Agreement with the same bar on incorporation, and says "A separate Commercial License agreement" is available for commercial use; its terms are not published ([Terms](https://www.movesense.com/terms/), 2026-10-11).
  - Not everything is under this licence: the Showcase app and sample source in the mobile library are Apache 2.0, and sbem-tools is MIT (repository READMEs, 2026-10-11). The FAQ's "open and free to use" describes access and cost, not an open-source licence.
  - For a study, institutional legal review should decide whether a deployed study app or custom firmware counts as evaluation and development or needs a separate agreement with Movesense.

- Development requires C++ tooling for sensor-side apps and native iOS/Android tooling for mobile. Third-party SDK wrappers exist (e.g. a .NET/Xamarin SDK).

- **Custom firmware through a supported SDK is Movesense's distinguishing capability.** It is not unique in this module: Axivity's AX3/AX6 firmware source is published under a BSD 2-clause licence (Open Movement repository README, read 2026-10-10; see `axivity-geneactiv.md`), though that tree has had no firmware feature release in years, while Movesense supports sensor-side app development as a product. Practical uses: on-sensor feature extraction to cut BLE bandwidth and battery; custom sampling schedules; event-triggered high-rate capture; bespoke signal conditioning. This turns the device from an instrument into a platform.
- **Custom firmware takes the MD out of its MDR registration.** Teams must validate and certify their own solution; certified medical firmware comes from a separate Movesense Medical repository, with access on request to info@movesense.com. The last firmware certified for medical use before June 2025 was 2.1.5; 2.3.1 brought later features to medical use ([MD product page](https://www.movesense.com/product/movesense-medical-mdr/); [2.3.1 release post](https://www.movesense.com/news/2025/06/movesense-sensor-firmware-2-3-1-released-a-major-upgrade-for-medical-use/), 2026-10-11).
- Developer-facing migrations to plan for: the Logbook JSON format changed in firmware 2.2, and `/Component/Led` PUT is deprecated in favour of `/Component/Leds` ([migration notes](https://www.movesense.com/docs/esw/migration_21/), 2026-10-11).

## Deployment and Infrastructure

- None. Buy the sensor, write or adopt an app, collect data.

## Participant Experience

- Coin-sized sensor (9.4 g for HR2) attached via chest strap or accessory mounts. Comfortable relative to a full chest strap harness but still a chest-worn device for the ECG products. Multi-day ECG is possible on Flash (up to five days of logging; heart rate intervals for over four months, with a battery change about once a month), but chest wear limits tolerance for long continuous use. Water and shock resistant; the MD is rated IP68 and runs on a user-replaceable Maxell CR2025 coin cell ([MD FAQ news post, 2024-06-17](https://www.movesense.com/news/2024/06/faq-regarding-movesense-md-medical-sensor/), read 2026-10-11). Battery life at given sampling configurations is not published.

- The Flash variant's onboard logging means no phone is needed during collection, which is a genuine advantage for field, occupational, and sports protocols.

## Privacy, Security, and Compliance

- **No vendor data processor exists** in the BLE/onboard-logging path. Same trivial governance story
- as Polar's SDK path and Axivity/GENEActiv.
- **Movesense MD carries Class IIa MDR 2017/745 certification**, genuine EU medical device status, only when running certified Movesense firmware. Older MD stock (SS050341000) is MDD-certified, so buyers should check the SKU ([conformity](https://www.movesense.com/conformity)).
- This is a stronger EU regulatory position than any consumer wearable in this module.
- Manufactured under ISO 13485:2016 (quality management, not an information security certification). No ISO 27001, SOC 2, HIPAA statement, BAA or customer DPA is published (checked 2026-10-11).
- GDPR: Movesense Ltd is controller for its own services and the ECG Recorder app, names a DPO contact, and uses SCCs or adequacy decisions for transfers outside the EU/EEA ([privacy policy](https://www.movesense.com/privacy-policy/)). A study using the ECG Recorder app gets no processor relationship by default.
- FDA status: **no FDA clearance** found in openFDA (510(k), PMA, registration and listing, GUDID; searched 2026-10-11). Movesense says "FDA 510k is on the roadmap" ([MD FAQ news post](https://www.movesense.com/news/2024/06/faq-regarding-movesense-md-medical-sensor/)). (Corrected from "Unclear".)

## Pricing

| Item | Detail | Confidence |
|---|---|---|
| Developer kits | MD Developer Kit €399 (on sale from €479), Flash Developer Kit €379, HR+ Developer Kit €249, Debugger + Programming Jig V2 €649 (VAT 0%); **free access to developer tools, sample code and documentation**; kits sold to business customers only | **Verified** (2026-10-11, [shop](https://www.movesense.com/shop/)) |
| SDK / firmware tooling | **No licence cost**, including custom firmware programmed on the production line; NRE applies to a custom production SKU | **Verified** |
| Individual sensor retail | **Movesense MD: €349 per unit (VAT 0%) for 1 to 49 units, €344 for 50 to 99, €339 for 100 to 199**; Flash €249/244/239; HR+ €119/114/109; HR2 €99/94/89 at the same tiers; CardioRTHM consumer kit €349.90 incl. tax | **Verified** (2026-10-11; corrected from "not publicly listed" on 2026-10-10) |
| Academic pricing | None in general; Movesense will issue an official quote for university procurement | **Verified** (2026-10-11, [FAQ](https://www.movesense.com/faq/)) |
| Volume pricing | Business customers only; substantial price step at 200 sensors; sales@movesense.com | **Verified** (2026-10-11, FAQ) |
| Minimums | None for standard sensors (from one unit). Custom logo labels from 100; custom branding and firmware on the production line from 200; custom SKU worthwhile from about 500 a year. Shop orders are binding and cannot be cancelled | **Verified** (2026-10-11, [OEM services](https://www.movesense.com/oem-services/), [Terms](https://www.movesense.com/terms/)) |
| Subscription | None. Movesense has said some advanced ECG Recorder features will move into a premium subscription; no price found | **Verified** (2026-10-11) |

- The absence of any licence fee, combined with published unit prices and the Academic Program's free sensors for selected projects, makes Movesense's total cost of ownership structurally low.

## Research Evidence and Validation

- **Movesense MD's Class IIa MDR certification** is the substantive regulatory claim and is stronger
- than a marketing "clinical-grade" assertion.
- Kubios HRV accepts Movesense data through a CSV export and import workflow, not an integration; Rogers 2022 (below) used Movesense ECG with Kubios. (Corrected 2026-10-11.)
- Movesense sensors appear in human movement analysis and machine-learning work published by the
- company and by users. **Reported.**
- ~~No independent head-to-head validation of Movesense against ECG or PSG references was located in
- this pass.~~ **Corrected 2026-10-09.** A PubMed search (`movesense[tiab]`, 18 hits) found independent
- validation against reference instruments for both the ECG and the IMU. No vendor authors and no
- vendor cash funding in any of the four studies below, but **Movesense supplied the sensors free of
- charge for both ECG validations** (in-kind support, disclosed in each paper's funding statement). All
- are small (N=14 to 21) healthy-adult samples.

| Study | Device | Reference | Key result | Funding / COI | Confidence |
|---|---|---|---|---|---|
| Rogers B et al. 2022, *Sensors* 22(5):2032, doi:10.3390/s22052032 | Movesense Medical chest belt, single-lead ECG | 12-lead ECG, N=21, rest and incremental cycling ramp | RR and HRV (meanRR, SDNN, RMSSD) r=0.98 to 1.0; DFA a1 r=0.95 to 0.97; meanRR bias 0.0 to 0.4 ms at rest, 6.0 to 11.2 ms during exercise | "Movesense provided the sensors for the study"; authors declare no commercial or financial relationships | **Verified** (funding and COI read in the PDF; figures as reported in the abstract) |
| Martín Gómez R et al. 2024, *Sensors* 24(17):5713, doi:10.3390/s24175713 | Movesense HR+ ECG | 3-lead ECG, N=21, running and cycling to exhaustion | R-peak sensitivity 99.7%, precision 99.6%; RR mean difference 0.23 ms at rest, 0.38 ms during exercise; Garmin HRM-Pro far worse on the same protocol | Sensors "provided by Movesense Ltd. ... as part of the Movesense Academic Program"; "Movesense had no role in the design of the study" | **Verified** (funding and COI read in the PDF; figures as reported in the abstract) |
| Rogers B et al. 2022, *Sensors* 22(19):7156, doi:10.3390/s22197156 | Movesense Medical ECG + Kubios | Gas-exchange respiratory frequency, N=21 | ECG-derived respiratory rate r=0.95, closer to reference than Polar H10 (r=0.85) | No commercial relationships declared | **Corroborated** (abstract) |
| Martín Gómez R et al. 2025, *J Biomech* 190:112873, doi:10.1016/j.jbiomech.2025.112873 | Movesense IMU, chest, 208 Hz, custom firmware | Force plate, N=14, 33,477 steps | Step time mean difference 0 ± 6 ms (r=0.97); 100% of foot strikes correctly lateralised | No competing interests | **Corroborated** (abstract; not OA) |

- Also relevant: Sabioni M et al. 2025, *Physiol Meas* 46(8), doi:10.1088/1361-6579/adece4, bench test
- with synthetic ECG: Movesense had the shortest RR-interval latency (0.4 s median) of four Bluetooth
- chest straps (Polar H10 2.6 s). And Hartikainen S et al. 2019, *Am J Cardiol* 123(10):1643, a
- Movesense chest-strap ECG read by cardiologists and algorithms for AF detection against Holter
- (N=220; algorithm sensitivity 95.3 to 96.3%); several co-authors hold shares in Heart2Save, an ECG
- software company, not Movesense. **Corroborated** (abstracts; the Heart2Save shareholding comes from an earlier read and the paper's COI statement was not re-read on 2026-10-10, since the article is not open access).
- **What is still missing:** no free-living, multi-day validation, no clinical-population ECG
- validation beyond AF screening, and no validation of the MD variant's medical-grade claims by a
- notified-body-independent group was located. IMU validation covers step timing in running only.
- **Applied deployment (Module 3).** [Helmer et al. 2025, Support trial](../../module-03-applied-studies/profiles/movesense-palliative-support-trial.md): continuous wearable monitoring in hospitalised palliative patients, terminated early for recruitment failure (N=7 analyzed). That profile flags that the paper describes the devices generically, so the Movesense model is not yet confirmed; do not cite it as evidence about Movesense performance until it is.

## Strengths

- **512 Hz single-lead ECG and a 9-axis IMU at 416 Hz or more** (vendor sources disagree on the maximum: 416, 833 or 1666 Hz), the highest ECG and among the highest IMU sampling
- specifications in this module (the Axivity AX3 accelerometer alone reaches 3,200 Hz; corrected 2026-10-10 and 2026-10-11).
- 1 ms R, R interval resolution.
- **Custom sensor firmware permitted, with no licence cost**, unique here (under a proprietary evaluation licence; see APIs).
- **Class IIa EU medical device certification** on the MD variant, with certified Movesense firmware; not combinable with custom firmware.
- 128 MB onboard logging on Flash for phone-free deployment (up to five days of ECG).
- No cloud, no vendor processor, trivial data governance (outside the ECG Recorder app).
- Desktop simulator, sample code and free recording tools lower the development barrier meaningfully.
- Supported by Labfront (MD, HR2 and Flash), which supplies the study-management and EMA layer Movesense lacks.

## Limitations

- Independent validation literature exists but is thin: four small lab studies (2022 to 2025) cover ECG R-R/HRV and running step timing, see Research Evidence. No free-living or long-duration validation. (Corrected 2026-10-09; the earlier "none located" claim was wrong.)
- Chest-worn ECG products suit sessions or a few days; Flash logs up to five days of ECG, but this is not a continuous multi-week ECG instrument.
- No derived metrics, no analytics, no dashboards, no participant management from the vendor.
- Requires C++ competence for firmware work and mobile development for the app, unless using
- Movesense's free recording tools or routing through Labfront (where participants start each recording manually).
- Licence is a proprietary 12-month evaluation agreement that bars incorporating the technology in products or services without a separate agreement.
- Battery life at given sampling configurations is not published, and the maximum IMU rate differs
- between vendor sources. (Water rating and battery type are published: IP68 and a CR2025 cell on the MD; corrected 2026-10-11.)
- No FDA clearance (510(k) said to be on the roadmap).
- Much smaller research community than Polar or ActiGraph, so fewer worked examples.

## Best-Fit Use Cases

- Methods and algorithm development requiring high-rate ECG or IMU.
- Biomechanics and human movement analysis (high-rate IMU; confirm the usable maximum with Movesense before relying on rates above 416 Hz).
- Cardiac autonomic research needing true R, R intervals at 1 ms.
- Protocols requiring on-sensor processing or non-standard sampling schedules (not on a study that needs the MD's medical-device status).
- EU studies wanting a certified medical device without clinical-trial-vendor pricing, using certified Movesense firmware.
- Field and occupational research where phone-free onboard logging matters.
- Paired with Labfront (MD, HR2 or Flash) when study management and EMA are also needed.

## Poor-Fit Use Cases

- Multi-week continuous free-living monitoring.
- Sleep-architecture research.
- Studies without embedded or mobile engineering capacity (unless using Labfront or Movesense's free recording tools).
- US studies that need an FDA-cleared device.
- Studies that need an extensive validation literature to satisfy reviewers (what exists is a handful of small lab studies).
- BYOD recruitment, negligible consumer install base.

## Open Questions

- ~~Is there any independent peer-reviewed validation of Movesense ECG or IMU against reference
- instruments?~~ **Answered 2026-10-09: yes, for lab ECG/HRV and running step timing** (see Research
- Evidence). Remaining gap: free-living and clinical-population validation.
- ~~Unit pricing.~~ Movesense MD €349 ex VAT (2026-10-10). ~~Developer-kit pricing and whether the Academic Program still selects projects.~~ Answered 2026-10-11: kits €249 to €399; program active (December 2025 project).
- Battery life at various sampling configurations. Maximum usable IMU rate per model and over BLE (vendor conflict, 416 / 833 / 1666 Hz; info@movesense.com). ~~Water-resistance rating.~~ IP68 on the MD (2026-10-11).
- ~~What licence governs the SDK and firmware source?~~ Resolved 2026-10-10: the proprietary Movesense SDK License and Evaluation Agreement (see APIs). Still open: whether a deployed research app needs Movesense's separate agreement.
- ~~FDA regulatory status, if any.~~ Answered 2026-10-11: no FDA clearance; 510(k) said to be on the roadmap.
- ~~Maximum continuous logging duration on Flash's 128 MB at given rates.~~ Answered 2026-10-11 by Movesense's March 2026 post (five days of ECG; almost 19 hours of 52 Hz 9-axis motion).
- EUDAMED entry and notified-body certificate for MS060222000 (not located 2026-10-11).

## Vendor Fact Record

<!-- facts:begin -->
<!-- facts:end -->

## Key Links

- Official site: https://www.movesense.com/
- Specifications: https://www.movesense.com/specifications/
- Get started / developer: https://www.movesense.com/get-started/
- Documentation: https://www.movesense.com/docs/
- Movesense MD: https://www.movesense.com/product/movesense-medical-mdr/
- Movesense Flash: https://www.movesense.com/product/movesense-flash/
- Movesense HR2: https://www.movesense.com/product/movesense-sensor-hr2/
- Sales: sales@movesense.com
- Movesense Academic Program: https://www.movesense.com/movesense-academic-program/
- SDK licence (PDF): https://bitbucket.org/movesense/movesense-device-lib/raw/master/LICENSE.pdf

## Sources

- See `../sources.md` entries S-MVS-01 through S-MVS-04.
- Rogers B, Schaffarczyk M, Clauß M, Mourot L, Gronwald T. 2022. *Sensors* 22(5):2032. https://doi.org/10.3390/s22052032 (PMC8914935). PDF: `../literature/movesense/2022-rogers-sensors-movesense-medical-ecg-rr-hrv-validation.pdf` (accessed 2026-10-09).
- Martín Gómez R, Allevard E, Kamstra H, Cotter J, Lamb P. 2024. *Sensors* 24(17):5713. https://doi.org/10.3390/s24175713 (PMC11397956). PDF: `../literature/movesense/2024-martingomez-sensors-movesense-hr-plus-ecg-high-intensity.pdf` (accessed 2026-10-09).
- Rogers B, Schaffarczyk M, Gronwald T. 2022. *Sensors* 22(19):7156. https://doi.org/10.3390/s22197156 (PMC9573071) (abstract read 2026-10-09).
- Martín Gómez R et al. 2025. *J Biomech* 190:112873. https://doi.org/10.1016/j.jbiomech.2025.112873 (PMID 40694944; abstract read 2026-10-09; not OA).
- Sabioni M, Willén J, Dual SA, Jacobsson M. 2025. *Physiol Meas* 46(8). https://doi.org/10.1088/1361-6579/adece4 (PMID 40623430; abstract read 2026-10-09).
- Hartikainen S et al. 2019. *Am J Cardiol* 123(10):1643-1648. https://doi.org/10.1016/j.amjcard.2019.02.028 (PMID 30878151; abstract read 2026-10-09).
- Movesense, Movesense Academic Program. https://www.movesense.com/movesense-academic-program/ (accessed 2026-10-10). **Primary.** Program terms, monthly review, up to three projects per quarter, latest listed cohort Q1 2023.
- Movesense, Movesense MD Sensor product page. https://www.movesense.com/product/movesense-medical-mdr/ (accessed 2026-10-10). **Primary.** €349 VAT 0% (1 to 49 units), volume tiers.
- Movesense Ltd, Movesense Software Development ("SDK") License and Evaluation Agreement. https://bitbucket.org/movesense/movesense-device-lib/raw/master/LICENSE.pdf (accessed 2026-10-10). **Primary.**
- Movesense, vendor fact record `facts/movesense.yaml` (quotes probe-checked 2026-10-11). **Primary.** Sources added 2026-10-11 from it:
  - Movesense FAQ. https://www.movesense.com/faq/ . ECG rates, raw data access, no academic pricing, data not sent to Movesense servers.
  - Movesense Terms (Limited Evaluation Licence Agreement, Movesense Ltd). https://www.movesense.com/terms/
  - Movesense grows independent from Suunto (2021-09). https://www.movesense.com/news/2021/09/movesense-grows-independent-from-suunto/
  - Movesense Medical MDR registration post (2023-02). https://www.movesense.com/news/2023/02/movesense-medicals-mdr-registration-approaches-what-does-it-mean-for-movesense-md-customers/
  - Movesense Medical software docs. https://movesense.com/docs/medical/medical_sw/
  - Firmware 2.3.1 release post (2025-06). https://www.movesense.com/news/2025/06/movesense-sensor-firmware-2-3-1-released-a-major-upgrade-for-medical-use/
  - API reference. https://www.movesense.com/docs/esw/api_reference/ . IMU sample-rate examples, BLE bandwidth warnings, internal temperature.
  - Flash Developer Kit page. https://www.movesense.com/product/movesense-flash-developer-kit/ ; HR2 page. https://www.movesense.com/product/movesense-sensor-hr2/
  - Hardware variants. https://www.movesense.com/docs/system/hw_variants/ ; Flash data logger post (2026-03). https://www.movesense.com/news/2026/03/improved-ecg-imu-data-logger-for-movesense-flash-now-available/
  - Five free recording tools post (2025-11). https://www.movesense.com/news/2025/11/recording-data-with-movesense-sensors-five-free-tools-to-get-you-started/
  - Labfront Movesense overview. https://help.labfront.com/movesense-overview (secondary)
  - Movesense shop. https://www.movesense.com/shop/ ; OEM services. https://www.movesense.com/oem-services/
  - Movesense Academic Program application form. https://docs.google.com/forms/d/e/1FAIpQLSe4R4gB78sni_M-LH1VJOWL-1j_h4mEo55T7MY0gp1KcLXFXA/viewform ; December 2025 project post. https://www.movesense.com/news/2025/12/university-of-venice-studies-seismocardiography-with-movesense-md-sensors/
  - Conformity. https://www.movesense.com/conformity ; privacy policy. https://www.movesense.com/privacy-policy/ ; ECG Recorder app data protection statement. https://www.movesense.com/movesense-ecg-recorder-app-data-protection-statement/
  - openFDA 510(k), PMA, registration and GUDID searches for Movesense and CardioRTHM (no matches, 2026-10-11). https://api.fda.gov/device/510k.json?search=applicant:movesense
  - Mobile library README (Apache 2.0). https://bitbucket.org/movesense/movesense-mobile-lib/raw/master/README.md ; sbem-tools README (MIT). https://bitbucket.org/movesense/sbem-tools/raw/master/README.md
- Movesense, FAQ regarding Movesense MD medical sensor (2024-06-17). https://www.movesense.com/news/2024/06/faq-regarding-movesense-md-medical-sensor/ (read 2026-10-11). **Primary.** "Water (IP68) and shock proof construction"; user-replaceable Maxell CR2025 coin cell; FDA 510(k) on the roadmap. IP68 and the battery type are not in the fact record, which has no field for them.
- Movesense, Kubios and Movesense post (2022-08). https://www.movesense.com/news/2022/08/kubios-and-movesense-combine-advanced-ecg-and-hrv-analysis-tools/ (judge read 2026-10-11). Describes the CSV workflow.
