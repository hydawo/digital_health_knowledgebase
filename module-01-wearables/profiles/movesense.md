# Movesense (Suunto)

## Quick Facts

| Field | Details |
|---|---|
| Organization | Movesense (Suunto / Amer Sports, Finland) |
| Category | Open, programmable research-grade sensor platform |
| Current status | Active |
| Platforms/devices | Movesense MD, Movesense Flash, Movesense HR2, Movesense HR+; CardioRTHM clinical solution |
| Open source | Open APIs and developer tools with **no licence cost**; custom sensor firmware permitted |
| Hosting/deployment | **None required** — BLE to your own app, or onboard logging |
| Pricing model | Device purchase; developer kits; volume pricing on request; **no software licence fee** |
| Last verified | 2026-08-21 |

## Summary

Movesense was missing from the first research pass and should not have been. It is the closest thing
in this module to a *programmable* research sensor: a small coin-shaped device with a 9-axis IMU and
a single-lead ECG front end, an open API, no licence fee, and — uniquely here — **the explicit
ability to write and flash your own firmware onto the sensor**.

Where Polar gives you an open SDK to *read* a fixed device, Movesense lets you change what the
device does. For methods research, unusual protocols, or on-sensor processing to save power and
bandwidth, that is a categorical difference.

It also holds something no other device in this module does at this price point: **Movesense MD is a
Class IIa medical device under EU MDR 2017/745.**

## Products / Platform Architecture

| Product | ECG | Onboard memory | Regulatory | Notes |
|---|---|---|---|---|
| **Movesense MD** | Clinical-grade single-channel | — | **Class IIa Medical Device, MDR 2017/745** | The regulated variant; includes non-medical temperature sensor |
| **Movesense Flash** | Clinical-grade single-channel | **128 MB internal memory for autonomous logging** | Non-medical | The phone-free option |
| **Movesense HR2** | 1-lead (non-medical) | — | Non-medical | 9.4 g; water and shock resistant |
| **Movesense HR+** | Heart rate | — | Non-medical | Entry sensor |
| **CardioRTHM** | — | — | Clinical solution | Short and long-term heart rhythm monitoring product built on the platform |

**Verified** (movesense.com/specifications/).

Company positioning covers three audiences: healthcare professionals (CardioRTHM), med-tech
companies integrating the MD sensor, and sport-tech companies using the Sport family.

## Sensors and Data Streams

| Stream | Specification | Confidence |
|---|---|---|
| **ECG** | **125 Hz to 512 Hz**, single-lead | **Corroborated** |
| **R–R intervals** | **1 ms accuracy and resolution** | **Verified** |
| **IMU — 9-axis** | Accelerometer + gyroscope + magnetometer, all triaxial. **13 Hz to 1.6 kHz** | **Corroborated** |
| Temperature | Non-medical sensor on MD and Flash | **Verified** |
| Heart rate | Standard BLE heart rate profile | **Verified** |
| Connectivity | Bluetooth Low Energy | **Verified** |

**512 Hz ECG and a 1.6 kHz IMU are research-instrument specifications, not consumer ones.** For
comparison: Polar H10 tops out at 130 Hz ECG and 200 Hz accelerometry; Samsung's Privileged SDK
gives 25 Hz accelerometry. Movesense's IMU ceiling is roughly 8× the Polar Verity Sense's SDK-mode
maximum and 64× Samsung's.

## Derived Metrics / Analytics

Essentially none from the vendor, by design — this is a signal source, not an insights platform.
Heart rate and R–R intervals are provided; everything else is the analyst's.

Third-party analytics ecosystem exists: **Kubios**, the standard HRV analysis software in the
research literature, has an integration with Movesense. **Reported.**

## Active Data Collection

None. No survey or EMA layer. (Note that **Labfront** supports Movesense HR2 alongside Garmin and
Dexcom, and Labfront does provide EMA — see `data-intermediaries.md`.)

## Researcher and Study Management Features

None natively. Available indirectly through Labfront.

## Data Access and Export

- **BLE streaming** to a researcher-built or third-party app.
- **Onboard logging** on Movesense Flash — 128 MB, phone-free.
- No cloud, no API keys, no rate limits, no retention policy but yours.
- Data custody is 100% institutional.

## APIs, SDKs, and Extensibility — the differentiator

Movesense states the platform provides "powerful, low-cost tools for creating your own sensor
firmware or compatible mobile app," with **"no license cost involved."** Open APIs, sample code, a
**desktop simulator**, and documentation are provided. Software repositories are hosted on
Bitbucket. Firmware can be uploaded to the sensor through the Movesense Showcase mobile app.
**Verified** (movesense.com/get-started/).

Development requires C++ tooling for sensor-side apps and native iOS/Android tooling for mobile.
Third-party SDK wrappers exist (e.g. a .NET/Xamarin SDK).

**Custom firmware is the capability nothing else here offers.** Practical uses: on-sensor feature
extraction to cut BLE bandwidth and battery; custom sampling schedules; event-triggered
high-rate capture; bespoke signal conditioning. This turns the device from an instrument into a
platform.

## Deployment and Infrastructure

None. Buy the sensor, write or adopt an app, collect data.

## Participant Experience

Coin-sized sensor (9.4 g for HR2) attached via chest strap or accessory mounts. Comfortable relative
to a full chest strap harness but still a chest-worn device for the ECG products — session-wear or
short-duration rather than a 30-day continuous instrument. Water and shock resistant.

The Flash variant's onboard logging means no phone is needed during collection, which is a genuine
advantage for field, occupational, and sports protocols.

## Privacy, Security, and Compliance

- **No vendor data processor exists** in the BLE/onboard-logging path. Same trivial governance story
  as Polar's SDK path and Axivity/GENEActiv.
- **Movesense MD carries Class IIa MDR 2017/745 certification** — genuine EU medical device status.
  This is a stronger EU regulatory position than any consumer wearable in this module.
- FDA status: not established. **Unclear.**

## Pricing

| Item | Detail | Confidence |
|---|---|---|
| Developer kits | Sensor + chest strap + mounting accessories; **free access to developer tools, sample code and documentation** | **Verified** |
| SDK / firmware tooling | **No licence cost** | **Verified** |
| Individual sensor retail | Not publicly listed | **Unclear** |
| Volume pricing | Business customers only; sales@movesense.com | **Corroborated** |

The absence of any licence fee, combined with the openness, makes Movesense's total cost of
ownership structurally low even though unit prices are unpublished.

## Research Evidence and Validation

- **Movesense MD's Class IIa MDR certification** is the substantive regulatory claim and is stronger
  than a marketing "clinical-grade" assertion.
- Kubios integration signals acceptance in the HRV methods community. **Reported.**
- Movesense sensors appear in human movement analysis and machine-learning work published by the
  company and by users. **Reported.**
- **No independent head-to-head validation of Movesense against ECG or PSG references was located in
  this pass.** **Unclear** — this is the platform's main evidentiary gap, and it is a real one given
  how strong the hardware specifications are.

## Strengths

- **512 Hz single-lead ECG and a 13 Hz–1.6 kHz 9-axis IMU** — the highest sampling specifications of
  any device in this module.
- 1 ms R–R interval resolution.
- **Custom sensor firmware permitted, with no licence cost** — unique here.
- **Class IIa EU medical device certification** on the MD variant.
- 128 MB onboard logging on Flash for phone-free deployment.
- No cloud, no vendor processor, trivial data governance.
- Desktop simulator and sample code lower the development barrier meaningfully.
- Supported by Labfront, which supplies the study-management and EMA layer Movesense lacks.

## Limitations

- **No independent validation literature located** — a striking gap for a device with these specs.
- Chest-worn ECG products are session-wear; not a continuous multi-week instrument.
- No derived metrics, no analytics, no dashboards, no participant management from the vendor.
- Requires C++ competence for firmware work and mobile development for the app, unless routed
  through Labfront.
- Unit pricing not public; business-customer sales model.
- Detailed specification tables (battery, water rating, exact IMU ranges) are behind gated PDF
  downloads rather than on the web page.
- Much smaller research community than Polar or ActiGraph, so fewer worked examples.

## Best-Fit Use Cases

- Methods and algorithm development requiring high-rate ECG or IMU.
- Biomechanics and human movement analysis (1.6 kHz IMU is genuinely differentiating).
- Cardiac autonomic research needing true R–R intervals at 1 ms.
- Protocols requiring on-sensor processing or non-standard sampling schedules.
- EU studies wanting a certified medical device without clinical-trial-vendor pricing.
- Field and occupational research where phone-free onboard logging matters.
- Paired with Labfront when study management and EMA are also needed.

## Poor-Fit Use Cases

- Multi-week continuous free-living monitoring.
- Sleep-architecture research.
- Studies without embedded or mobile engineering capacity (unless using Labfront).
- Studies that need an established validation literature to satisfy reviewers.
- BYOD recruitment — negligible consumer install base.

## Open Questions

- **Is there any independent peer-reviewed validation of Movesense ECG or IMU against reference
  instruments?** This is the most important gap.
- Unit and developer-kit pricing.
- Battery life at various sampling configurations; exact IMU ranges; water-resistance rating.
- What licence governs the SDK and firmware source specifically? ("No licence cost" is stated;
  the licence identity is not.)
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

See `../sources.md` entries S-MVS-01 through S-MVS-04.
