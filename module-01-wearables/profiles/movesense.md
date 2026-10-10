# Movesense (Suunto)

## Quick Facts

| Field | Details |
|---|---|
| Organization | Movesense (Suunto / Amer Sports, Finland) |
| Category | Open, programmable research-grade sensor platform |
| Current status | Active |
| Platforms/devices | Movesense MD, Movesense Flash, Movesense HR2, Movesense HR+; CardioRTHM clinical solution |
| Open source | Open APIs and developer tools with **no licence cost**; custom sensor firmware permitted |
| Hosting/deployment | **None required**, BLE to your own app, or onboard logging |
| Pricing model | Device purchase; developer kits; volume pricing on request; **no software licence fee** |
| Last verified | 2026-08-21 |

## Summary

- Movesense was missing from the first research pass and should not have been. It is the closest thing in this module to a *programmable* research sensor: a small coin-shaped device with a 9-axis IMU and a single-lead ECG front end, an open API, no licence fee, and, uniquely here, **the explicit ability to write and flash your own firmware onto the sensor**.

- Where Polar gives you an open SDK to *read* a fixed device, Movesense lets you change what the device does. For methods research, unusual protocols, or on-sensor processing to save power and bandwidth, that is a categorical difference.

- It also holds something no other device in this module does at this price point: **Movesense MD is a Class IIa medical device under EU MDR 2017/745.**

## Products / Platform Architecture

| Product | ECG | Onboard memory | Regulatory | Notes |
|---|---|---|---|---|
| **Movesense MD** | Clinical-grade single-channel | | **Class IIa Medical Device, MDR 2017/745** | The regulated variant; includes non-medical temperature sensor |
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
| ECG | Yes, single lead | Raw | 125 Hz to 512 Hz | Corroborated. A research-instrument specification. |
| Accelerometer | Yes | Raw | 13 Hz to 1.6 kHz, part of the 9-axis IMU | Corroborated. |
| Gyroscope | Yes | Raw | 13 Hz to 1.6 kHz | Corroborated. |
| Magnetometer | Yes | Raw | 13 Hz to 1.6 kHz | Corroborated. |
| Temperature | MD and Flash | Raw, non-medical sensor | Unclear | Verified. |
| SpO2 | No | Not applicable | Not applicable |  |
| GPS | No | Not applicable | Not applicable |  |
| Barometer / altimeter | Unclear | Unclear | Unclear |  |
| EDA | No | Not applicable | Not applicable |  |
| Ambient light | No | Not applicable | Not applicable |  |
| Other | R-R intervals; heart rate over the standard BLE profile | Raw | 1 ms accuracy and resolution for R-R | Verified. Connectivity is Bluetooth Low Energy. |

**Verification.** From the Movesense developer documentation as recorded in the Module 1 passes. 512 Hz ECG and a 1.6 kHz IMU are research-instrument specifications; see the notes below for the comparison with Polar and Samsung.

### Notes from earlier verification passes

| Stream | Specification | Confidence |
|---|---|---|
| **ECG** | **125 Hz to 512 Hz**, single-lead | **Corroborated** |
| **R, R intervals** | **1 ms accuracy and resolution** | **Verified** |
| **IMU, 9-axis** | Accelerometer + gyroscope + magnetometer, all triaxial. **13 Hz to 1.6 kHz** | **Corroborated** |
| Temperature | Non-medical sensor on MD and Flash | **Verified** |
| Heart rate | Standard BLE heart rate profile | **Verified** |
| Connectivity | Bluetooth Low Energy | **Verified** |

- **512 Hz ECG and a 1.6 kHz IMU are research-instrument specifications, not consumer ones.** For comparison: Polar H10 tops out at 130 Hz ECG and 200 Hz accelerometry; Samsung's Privileged SDK gives 25 Hz accelerometry. Movesense's IMU ceiling is roughly 8× the Polar Verity Sense's SDK-mode maximum and 64× Samsung's.

## Derived Metrics / Analytics

- Essentially none from the vendor, by design, this is a signal source, not an insights platform. Heart rate and R, R intervals are provided; everything else is the analyst's.

- Third-party analytics ecosystem exists: **Kubios**, the standard HRV analysis software in the research literature, has an integration with Movesense. **Reported.**

## Active Data Collection

- None. No survey or EMA layer. (Note that **Labfront** supports Movesense HR2 alongside Garmin and Dexcom, and Labfront does provide EMA, see `data-intermediaries.md`.)

## Researcher and Study Management Features

- None natively. Available indirectly through Labfront.

## Data Access and Export

- **BLE streaming** to a researcher-built or third-party app.
- **Onboard logging** on Movesense Flash, 128 MB, phone-free.
- No cloud, no API keys, no rate limits, no retention policy but yours.
- Data custody is 100% institutional.

## APIs, SDKs, and Extensibility

- Movesense states the platform provides "powerful, low-cost tools for creating your own sensor firmware or compatible mobile app," with **"no license cost involved."** Open APIs, sample code, a **desktop simulator**, and documentation are provided. Software repositories are hosted on Bitbucket. Firmware can be uploaded to the sensor through the Movesense Showcase mobile app. **Verified** (movesense.com/get-started/).

- Development requires C++ tooling for sensor-side apps and native iOS/Android tooling for mobile. Third-party SDK wrappers exist (e.g. a .NET/Xamarin SDK).

- **Custom firmware is the capability nothing else here offers.** Practical uses: on-sensor feature extraction to cut BLE bandwidth and battery; custom sampling schedules; event-triggered high-rate capture; bespoke signal conditioning. This turns the device from an instrument into a platform.

## Deployment and Infrastructure

- None. Buy the sensor, write or adopt an app, collect data.

## Participant Experience

- Coin-sized sensor (9.4 g for HR2) attached via chest strap or accessory mounts. Comfortable relative to a full chest strap harness but still a chest-worn device for the ECG products, session-wear or short-duration rather than a 30-day continuous instrument. Water and shock resistant.

- The Flash variant's onboard logging means no phone is needed during collection, which is a genuine advantage for field, occupational, and sports protocols.

## Privacy, Security, and Compliance

- **No vendor data processor exists** in the BLE/onboard-logging path. Same trivial governance story
- as Polar's SDK path and Axivity/GENEActiv.
- **Movesense MD carries Class IIa MDR 2017/745 certification**, genuine EU medical device status.
- This is a stronger EU regulatory position than any consumer wearable in this module.
- FDA status: not established. **Unclear.**

## Pricing

| Item | Detail | Confidence |
|---|---|---|
| Developer kits | Sensor + chest strap + mounting accessories; **free access to developer tools, sample code and documentation** | **Verified** |
| SDK / firmware tooling | **No licence cost** | **Verified** |
| Individual sensor retail | Not publicly listed | **Unclear** |
| Volume pricing | Business customers only; sales@movesense.com | **Corroborated** |

- The absence of any licence fee, combined with the openness, makes Movesense's total cost of ownership structurally low even though unit prices are unpublished.

## Research Evidence and Validation

- **Movesense MD's Class IIa MDR certification** is the substantive regulatory claim and is stronger
- than a marketing "clinical-grade" assertion.
- Kubios integration signals acceptance in the HRV methods community. **Reported.**
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
- software company, not Movesense. **Corroborated** (abstracts).
- **What is still missing:** no free-living, multi-day validation, no clinical-population ECG
- validation beyond AF screening, and no validation of the MD variant's medical-grade claims by a
- notified-body-independent group was located. IMU validation covers step timing in running only.

## Strengths

- **512 Hz single-lead ECG and a 13 Hz, 1.6 kHz 9-axis IMU**, the highest sampling specifications of
- any device in this module.
- 1 ms R, R interval resolution.
- **Custom sensor firmware permitted, with no licence cost**, unique here.
- **Class IIa EU medical device certification** on the MD variant.
- 128 MB onboard logging on Flash for phone-free deployment.
- No cloud, no vendor processor, trivial data governance.
- Desktop simulator and sample code lower the development barrier meaningfully.
- Supported by Labfront, which supplies the study-management and EMA layer Movesense lacks.

## Limitations

- Independent validation literature exists but is thin: four small lab studies (2022 to 2025) cover ECG R-R/HRV and running step timing, see Research Evidence. No free-living or long-duration validation. (Corrected 2026-10-09; the earlier "none located" claim was wrong.)
- Chest-worn ECG products are session-wear; not a continuous multi-week instrument.
- No derived metrics, no analytics, no dashboards, no participant management from the vendor.
- Requires C++ competence for firmware work and mobile development for the app, unless routed
- through Labfront.
- Unit pricing not public; business-customer sales model.
- Detailed specification tables (battery, water rating, exact IMU ranges) are behind gated PDF
- downloads rather than on the web page.
- Much smaller research community than Polar or ActiGraph, so fewer worked examples.

## Best-Fit Use Cases

- Methods and algorithm development requiring high-rate ECG or IMU.
- Biomechanics and human movement analysis (1.6 kHz IMU is genuinely differentiating).
- Cardiac autonomic research needing true R, R intervals at 1 ms.
- Protocols requiring on-sensor processing or non-standard sampling schedules.
- EU studies wanting a certified medical device without clinical-trial-vendor pricing.
- Field and occupational research where phone-free onboard logging matters.
- Paired with Labfront when study management and EMA are also needed.

## Poor-Fit Use Cases

- Multi-week continuous free-living monitoring.
- Sleep-architecture research.
- Studies without embedded or mobile engineering capacity (unless using Labfront).
- Studies that need an extensive validation literature to satisfy reviewers (what exists is a handful of small lab studies).
- BYOD recruitment, negligible consumer install base.

## Open Questions

- ~~Is there any independent peer-reviewed validation of Movesense ECG or IMU against reference
- instruments?~~ **Answered 2026-10-09: yes, for lab ECG/HRV and running step timing** (see Research
- Evidence). Remaining gap: free-living and clinical-population validation.
- Unit and developer-kit pricing.
- Battery life at various sampling configurations; exact IMU ranges; water-resistance rating.
- What licence governs the SDK and firmware source specifically? ("No licence cost" is stated;
- the licence identity is not.)
- FDA regulatory status, if any.
- Maximum continuous logging duration on Flash's 128 MB at given rates.

## Key Links

- Official site: https://www.movesense.com/
- Specifications: https://www.movesense.com/specifications/
- Get started / developer: https://www.movesense.com/get-started/
- Documentation: https://www.movesense.com/docs/
- Movesense MD: https://www.movesense.com/product/movesense-medical-mdr/
- Movesense Flash: https://www.movesense.com/product/movesense-flash/
- Movesense HR2: https://www.movesense.com/product/movesense-sensor-hr2/
- Sales: sales@movesense.com

## Sources

- See `../sources.md` entries S-MVS-01 through S-MVS-04.
- Rogers B, Schaffarczyk M, Clauß M, Mourot L, Gronwald T. 2022. *Sensors* 22(5):2032. https://doi.org/10.3390/s22052032 (PMC8914935). PDF: `../literature/movesense/2022-rogers-sensors-movesense-medical-ecg-rr-hrv-validation.pdf` (accessed 2026-10-09).
- Martín Gómez R, Allevard E, Kamstra H, Cotter J, Lamb P. 2024. *Sensors* 24(17):5713. https://doi.org/10.3390/s24175713 (PMC11397956). PDF: `../literature/movesense/2024-martingomez-sensors-movesense-hr-plus-ecg-high-intensity.pdf` (accessed 2026-10-09).
- Rogers B, Schaffarczyk M, Gronwald T. 2022. *Sensors* 22(19):7156. https://doi.org/10.3390/s22197156 (PMC9573071) (abstract read 2026-10-09).
- Martín Gómez R et al. 2025. *J Biomech* 190:112873. https://doi.org/10.1016/j.jbiomech.2025.112873 (PMID 40694944; abstract read 2026-10-09; not OA).
- Sabioni M, Willén J, Dual SA, Jacobsson M. 2025. *Physiol Meas* 46(8). https://doi.org/10.1088/1361-6579/adece4 (PMID 40623430; abstract read 2026-10-09).
- Hartikainen S et al. 2019. *Am J Cardiol* 123(10):1643-1648. https://doi.org/10.1016/j.amjcard.2019.02.028 (PMID 30878151; abstract read 2026-10-09).
