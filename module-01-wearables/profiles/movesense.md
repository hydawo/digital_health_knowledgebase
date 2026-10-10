# Movesense (Suunto)

## Quick Facts

| Field | Details |
|---|---|
| Organization | Movesense (Suunto / Amer Sports, Finland) |
| Category | Open, programmable research-grade sensor platform |
| Current status | Active |
| Platforms/devices | Movesense MD, Movesense Flash, Movesense HR2, Movesense HR+; CardioRTHM clinical solution |
| Open source | **No.** Developer tools and APIs are free of charge, but the SDK is licensed under a proprietary 12-month "SDK License and Evaluation Agreement" for evaluation and development only; custom sensor firmware permitted under it (re-verified 2026-10-10) |
| Hosting/deployment | **None required**, BLE to your own app, or onboard logging |
| Pricing model | Device purchase (Movesense MD €349 ex VAT for 1 to 49 units); developer kits; volume pricing on request; **no software licence fee**; free sensors for selected academic projects (Movesense Academic Program) |
| Last verified | 2026-08-21; SDK licence, MD price and Academic Program re-verified 2026-10-10 |

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

- **512 Hz ECG and a 1.6 kHz IMU are research-instrument specifications, not consumer ones.** For comparison: Polar H10 tops out at 130 Hz ECG and 200 Hz accelerometry; Samsung's Health Sensor SDK (formerly the Privileged Health SDK) gives 25 Hz continuous accelerometry. The Axivity AX3 logger goes higher still for accelerometry alone (up to 3,200 Hz; see `axivity-geneactiv.md`). Movesense's IMU ceiling is roughly 8× the Polar Verity Sense's SDK-mode maximum and 64× Samsung's.

## Derived Metrics / Analytics

- Essentially none from the vendor, by design, this is a signal source, not an insights platform. Heart rate and R, R intervals are provided; everything else is the analyst's.

- Third-party analytics ecosystem exists: **Kubios**, the standard HRV analysis software in the research literature, has an integration with Movesense. **Reported.**

## Active Data Collection

- None. No survey or EMA layer. (Note that **Labfront** supports Movesense HR2 alongside Garmin and Dexcom, and Labfront does provide EMA, see `data-intermediaries.md`.)

## Researcher and Study Management Features

- None natively. Available indirectly through Labfront.
- **Movesense Academic Program** (movesense.com/movesense-academic-program, read 2026-10-10). "Movesense supplies the selected research teams with a limited number of Movesense sensors and associated accessories such as heart rate straps", sized to the project, plus technical support; no charge is mentioned. Researchers apply by online form with a project description, timeline and planned use. Movesense reviews applications monthly and "invites up to three projects per quarter". Selection criteria include innovativeness, "Potential of commercial applications of the project results", potential to build awareness for Movesense, and "Additional non-published criteria". Selected teams must mention Movesense in publications and allow Movesense to list the project. The page says the program "started on November, 2019 and is open until further notice", but the latest cohort it lists is Q1 2023. At least one validation study (Martín Gómez 2024, below) received sensors through it. **Verified** that the page exists and says this; whether the program is still selecting projects is **Unclear**.
- **What academics get:** the same data any developer gets (raw ECG, IMU and R-R over BLE or onboard logging, no cloud, no user caps or data-use terms from Movesense), under the same SDK licence. The program changes the hardware cost, not the data.

## Data Access and Export

- **BLE streaming** to a researcher-built or third-party app.
- **Onboard logging** on Movesense Flash, 128 MB, phone-free.
- No cloud, no API keys, no rate limits, no retention policy but yours.
- Data custody is 100% institutional.

## APIs, SDKs, and Extensibility

- Movesense states the platform provides "powerful, low-cost tools for creating your own sensor firmware or compatible mobile app," with **"no license cost involved."** Open APIs, sample code, a **desktop simulator**, and documentation are provided. Software repositories are hosted on Bitbucket. Firmware can be uploaded to the sensor through the Movesense Showcase mobile app. **Verified** (movesense.com/get-started/).
- **SDK licence (read 2026-10-10, Verified).** The licence file in the official `movesense-device-lib` repository is the proprietary "Movesense Software Development ("SDK") License and Evaluation Agreement" with Movesense Ltd. It is not an open-source licence.
  - "Purpose" means "the Licensees' evaluation, testing and potential development of a software application"; "possible commercialization of the Application ... is subject to a separate agreement".
  - "the Licensee shall not incorporate or integrate the Licensed Technology or any part thereof in any products or services", and may not reverse engineer it.
  - The agreement runs for twelve months from signature; either party may terminate on 30 days' notice, and on termination the licensee must destroy or return the Licensed Technology within five days.
  - No fee clause appears, consistent with "no license cost".
  - For a study, institutional legal review should decide whether a deployed study app or custom firmware counts as evaluation and development or needs a separate agreement with Movesense.

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
| Individual sensor retail | **Movesense MD: €349 per unit (VAT 0%) for 1 to 49 units, €344 for 50 to 99**, "Add to cart" on movesense.com; other models also listed in the web shop | **Verified** (2026-10-10; corrected from "not publicly listed") |
| Volume pricing | Business customers only; sales@movesense.com | **Corroborated** |

- The absence of any licence fee, combined with published unit prices and the Academic Program's free sensors for selected projects, makes Movesense's total cost of ownership structurally low.

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
- software company, not Movesense. **Corroborated** (abstracts; the Heart2Save shareholding comes from an earlier read and the paper's COI statement was not re-read on 2026-10-10, since the article is not open access).
- **What is still missing:** no free-living, multi-day validation, no clinical-population ECG
- validation beyond AF screening, and no validation of the MD variant's medical-grade claims by a
- notified-body-independent group was located. IMU validation covers step timing in running only.

## Strengths

- **512 Hz single-lead ECG and a 13 Hz, 1.6 kHz 9-axis IMU**, the highest ECG and IMU sampling
- specifications in this module (the Axivity AX3 accelerometer alone reaches 3,200 Hz; corrected 2026-10-10).
- 1 ms R, R interval resolution.
- **Custom sensor firmware permitted, with no licence cost**, unique here (under a proprietary evaluation licence; see APIs).
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
- Licence is a proprietary 12-month evaluation agreement that bars incorporating the technology in products or services without a separate agreement.
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
- ~~Unit pricing.~~ Movesense MD €349 ex VAT (2026-10-10). Developer-kit pricing and whether the Academic Program still selects projects remain open.
- Battery life at various sampling configurations; exact IMU ranges; water-resistance rating.
- ~~What licence governs the SDK and firmware source?~~ Resolved 2026-10-10: the proprietary Movesense SDK License and Evaluation Agreement (see APIs). Still open: whether a deployed research app needs Movesense's separate agreement.
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
