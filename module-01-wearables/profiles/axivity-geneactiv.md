# Axivity (AX3 / AX6) and GENEActiv, open research-grade accelerometers

## Quick Facts

| Field | Details |
|---|---|
| Organization | Axivity Ltd (UK, from Open Movement / Newcastle University); Activinsights Ltd (UK, GENEActiv) |
| Category | Research-grade raw-accelerometry logging sensors |
| Current status | Active |
| Platforms/devices | Axivity **AX3** (accelerometer), **AX6** (accelerometer + gyroscope); GENEActiv Original / Sleep |
| Open source | **Axivity: firmware and software BSD 2-clause; hardware and enclosure CC BY 3.0.** GENEActiv: proprietary device, open analysis ecosystem |
| Hosting/deployment | **None**, devices log to internal memory, downloaded by USB. No cloud, no account |
| Pricing model | Device purchase only; no subscription, no platform fee |
| Last verified | 2026-08-21 |

## Summary

- These are the devices behind the largest accelerometry cohorts in the world, and they represent the opposite pole from every consumer platform in this module: **no cloud, no API, no vendor account, no derived metrics, no algorithms, no subscription, just calibrated raw triaxial acceleration written to onboard flash.**

- The UK Biobank physical activity substudy used **Axivity AX3** devices to collect wrist-worn accelerometry in over 100,000 participants at **100 Hz, ±8 g, over seven days**. GENEActiv was used in the Whitehall II, Fenland, and Pelotas cohorts. Between them, these two devices underpin most of the modern open-science physical-activity literature and its analytical toolchain.

- They belong in this module because for a large class of research questions they are simply the correct answer, and because they set the price and openness benchmark against which ActiGraph/ Ametris and the consumer platforms should be judged.

## Products / Platform Architecture

- **Axivity AX3**, accelerometer-only logger. **Axivity AX6**, adds a gyroscope. Both derive from
- the Open Movement project at Newcastle University. **Verified** (github.com/digitalinteraction/openmovement/wiki/AX3).
- **GENEActiv Original / GENEActiv Sleep** (Activinsights), wrist-worn raw accelerometer with
- additional light and near-body temperature channels on the Original.

- There is no platform. The architecture is: configure device → participant wears it → return device → download file → analyze.

## Sensors and Data Streams

- Every Module 1 profile uses the same table so devices can be compared row by row. Rows are the sensors named in `CLAUDE.md`. "Present" is about the hardware; "Researcher access" is about what a study can actually obtain, which is the module's central question. "Unclear" means nothing current was verified. The convention is recorded in [`../../shared/profile-table-conventions.md`](../../shared/profile-table-conventions.md).

| Sensor | Present | Researcher access to underlying signal | Resolution or sampling | Notes |
|---|---|---|---|---|
| PPG | No | Not applicable | Not applicable |  |
| ECG | No | Not applicable | Not applicable |  |
| Accelerometer | Yes, all models | Raw, always | AX3 configurable rate and range; UK Biobank used 100 Hz at plus or minus 8 g | No vendor-derived metrics exist; every metric comes from the analyst's own pipeline. |
| Gyroscope | AX6 only | Raw | Configurable | Enables orientation and gait work. |
| Magnetometer | No | Not applicable | Not applicable |  |
| Temperature | GENEActiv Original | Raw near-body temperature | Unclear |  |
| SpO2 | No | Not applicable | Not applicable |  |
| GPS | No | Not applicable | Not applicable |  |
| Barometer / altimeter | No | Not applicable | Not applicable |  |
| EDA | No | Not applicable | Not applicable |  |
| Ambient light | GENEActiv Original | Raw light channel | Unclear | Useful for circadian work. |
| Other | Unclear | Unclear | Unclear | Not verified against current documentation. |

**Verification.** Verified for the AX3 UK Biobank configuration (UK Biobank Physical Activity Monitor documentation; Doherty et al., PLOS ONE 2017). See `../sources.md` entries S-AXV-01 through S-AXV-05.

### Notes from earlier verification passes

| Device | Streams | Notes |
|---|---|---|
| AX3 | Triaxial accelerometer | Configurable rate and range; UK Biobank used 100 Hz, ±8 g |
| AX6 | Triaxial accelerometer + triaxial gyroscope | Gyroscope enables orientation/gait work |
| GENEActiv Original | Triaxial accelerometer, light, near-body temperature | Light channel is useful for circadian work |

- **Verified** for the AX3 UK Biobank configuration (UK Biobank Physical Activity Monitor documentation; Doherty et al., PLOS ONE 2017).

- **All data is raw.** There are no vendor-derived metrics whatsoever. Counts, cut-points, sleep scoring, non-wear detection, and any digital biomarker are produced entirely by the analyst's own pipeline.

## Derived Metrics / Analytics

- This is the ecosystem's real strength, and it is external to the vendors:

- **GGIR** (R), the dominant open-source package for raw accelerometry: auto-calibration, non-wear
- detection, ENMO/MAD metrics, sleep detection, circadian metrics. Works with AX3, GENEActiv, and ActiGraph `.gt3x` files.
- **actipy** (Python, Oxford Wearables Group), SDK for processing wearable sensor data.
- **Verified** (github.com/OxWearables/actipy).
- **biobankAccelerometerAnalysis** (Oxford), the machine-learning activity classification pipeline
- used on UK Biobank data. **Verified** (biobankaccanalysis.readthedocs.io).
- **Open Movement software (OmGui)**, device configuration and download. BSD 2-clause.

- Because the analysis code is open and published, an Axivity/GENEActiv study is **reproducible in a way that no consumer-wearable study can be.** Every transformation from raw acceleration to endpoint is inspectable. This is the single strongest methodological argument for this device class.

## Active Data Collection

- None. These devices have no screen, no buttons of consequence, and no participant interaction.

## Researcher and Study Management Features

- None from the vendor. Enrollment, shipping, adherence, and data management are entirely the research team's problem. In practice, large cohorts handle this with postal logistics: UK Biobank dispatched devices by post configured to **start recording automatically at 10am two working days after dispatch** and run for seven days. **Verified.** That timed-start capability is precisely the feature that makes fully postal, zero-contact deployment work.

## Data Access and Export

- **USB download** of a raw binary file (`.cwa` for Axivity, `.bin` for GENEActiv).
- No API, no cloud, no latency, no rate limits, no retention policy other than yours.
- Data custody is 100% institutional from the moment of download.

## APIs, SDKs, and Extensibility

- No device API (none needed). Open firmware and hardware for Axivity means a sufficiently motivated group can modify the device itself, genuinely unique in this module. Source under BSD 2-clause; hardware/enclosure designs under CC BY 3.0. **Verified.**

## Deployment and Infrastructure

- None required. A laptop and OmGui (or equivalent) is the entire infrastructure. This is the cheapest and simplest deployment model of any option in Module 1.

## Participant Experience

- Small, sealed, screenless, waterproof pucks worn on a wrist strap (or thigh/hip with tape/belt).
- **No charging during the wear period**, battery is sized for the recording window. For UK
- Biobank's protocol, a single charge covered the full seven days at 100 Hz.
- No app, no phone, no account, no sync, no notifications. **Missing data from sync failure is
- structurally impossible.**
- Participant burden is close to zero; the burden is entirely logistical (posting devices out and
- getting them back).
- Device recovery is the main operational risk: unreturned devices are a direct financial loss.

## Privacy, Security, and Compliance

- **No third-party data processor exists.** No cloud, no vendor account, no terms of service
- governing the data. This is the simplest possible IRB/ethics story in the entire module.
- No PHI leaves the institution at any point.
- No HIPAA BAA required for the device vendor, because the vendor never touches data.
- GDPR analysis is trivial for the same reason.

## Pricing

- Device purchase only; no recurring cost. Public list pricing is limited; typical figures cited in the research community place AX3 and GENEActiv units in the low-to-mid hundreds of pounds/dollars each, well below ActiGraph. **Unclear**, no authoritative current price was verified in this pass. Both vendors quote directly and offer academic pricing.

- **The absence of any software licence or platform subscription is the key economic point**: unlike ActiGraph (ActiLife ~$1,695, CentrePoint ~$3,500/yr per third-party report), the analysis toolchain here is free and open.

## Research Evidence and Validation

- **UK Biobank**: AX3 accelerometry in 100,000+ participants, the largest such dataset in existence,
- with published methods (Doherty et al., PLOS ONE 2017). **Verified.**
- The AX3 "demonstrated equivalent signal vector magnitude output on multi-axis shaking tests to the
- GENEActiv accelerometer used in the Whitehall II, Fenland and Pelotas cohorts." **Verified** (UK Biobank / PLOS ONE methods).
- GENEActiv has its own substantial validation literature and cohort footprint.
- Cross-device comparability between AX3, GENEActiv, and ActiGraph at the raw-signal level is
- reasonably well established, which is why GGIR supports all three, a major practical advantage when harmonizing across cohorts.
- Neither device measures heart rate, so cardiovascular validation questions do not arise.

## Strengths

- **Fully open**: Axivity firmware/software BSD-licensed, hardware CC BY. Nothing else here is
- remotely this open.
- **Reproducible end-to-end**: raw data + open analysis pipelines (GGIR, actipy,
- biobankAccelerometerAnalysis) means every step from signal to endpoint is inspectable.
- Direct comparability with UK Biobank, Whitehall II, Fenland, Pelotas and the wider cohort
- literature.
- No cloud, no vendor, no data processor, trivial ethics and data-governance story.
- No sync dependency, no phone dependency, no participant app: structurally immune to the dominant
- failure mode of consumer wearable studies.
- Timed-start configuration enables fully postal deployment at scale.
- No subscription, no software licence, no platform fee.
- Cheaper than ActiGraph for equivalent (or better) raw-data capability.

## Limitations

- **Movement only.** No heart rate, HRV, SpO2, temperature (except GENEActiv's near-body
- temperature), or any cardiovascular signal.
- No real-time or near-real-time data, you learn nothing until the device comes back. **No
- adherence monitoring is possible during the wear period.**
- Fixed recording window bounded by battery and memory; not a continuous months-long instrument.
- Requires the research team to have real analytical capability (R/Python, GGIR competence). There
- is no "download a CSV of steps" path.
- Device recovery logistics and loss are a genuine cost.
- No study management, no participant engagement, no intervention capability.
- Cannot support any adaptive or feedback-based design.
- Public pricing is not available.

## Best-Fit Use Cases

- **Population-scale physical activity and sedentary behaviour epidemiology.**
- Any study needing harmonization with UK Biobank or comparable cohorts.
- Circadian rest, activity rhythm research (GENEActiv's light channel is valuable here).
- Studies with strict data-governance constraints that prohibit vendor clouds.
- Sleep, wake timing (not staging) over defined 7 to 14 day windows.
- Methods and algorithm development on raw accelerometry.
- Low-resource settings where phones, connectivity, and charging cannot be assumed.

## Poor-Fit Use Cases

- Anything requiring cardiovascular or autonomic measures.
- Real-time monitoring, adherence tracking during wear, or adaptive interventions.
- Continuous monitoring beyond the device's recording window.
- Studies without analytical capacity for raw signal processing.
- Studies wanting participant-facing feedback.
- Sleep-staging research.

## Open Questions

- Current list and academic pricing for AX3, AX6, and GENEActiv?
- Maximum recording duration at various sampling-rate/range configurations for each device?
- Current status and maintenance of the Open Movement project and OmGui?
- Is Activinsights' GENEActiv line still in active production and supply?
- What is the practical device-loss rate in postal deployments, and how do large cohorts mitigate it?

## Key Links

- Axivity: https://axivity.com/
- Axivity UK Biobank case study: https://axivity.com/case-studies/biobank
- **Open Movement AX3 wiki: https://github.com/digitalinteraction/openmovement/wiki/AX3**
- UK Biobank Physical Activity Monitor documentation: https://biobank.ndph.ox.ac.uk/ukb/ukb/docs/PhysicalActivityMonitor.pdf
- Doherty et al. PLOS ONE 2017: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0169649
- actipy (Python SDK): https://github.com/OxWearables/actipy
- biobankAccelerometerAnalysis methods: https://biobankaccanalysis.readthedocs.io/en/latest/methods.html

## Sources

- See `../sources.md` entries S-AXV-01 through S-AXV-05.
