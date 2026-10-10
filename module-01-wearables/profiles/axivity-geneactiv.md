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
| Pricing model | Device purchase only; no subscription, no platform fee. **Axivity publishes list prices** (AX3 from £139, AX6 from £199, ex VAT); GENEActiv by quote |
| Last verified | 2026-08-21; GENEActiv supply and Open Movement maintenance re-checked 2026-10-09; Axivity prices and specs, recording durations and GENEAcore re-verified 2026-10-10 |

## Summary

- These are the devices behind the largest accelerometry cohorts in the world, and they represent the opposite pole from every consumer platform in this module: **no cloud, no API, no vendor account, no derived metrics, no algorithms, no subscription, just calibrated raw triaxial acceleration written to onboard flash.**

- The UK Biobank physical activity substudy used **Axivity AX3** devices to collect wrist-worn accelerometry in over 100,000 participants at **100 Hz, ±8 g, over seven days**. GENEActiv was used in the Whitehall II, Fenland, and Pelotas cohorts. Between them, these two devices underpin most of the modern open-science physical-activity literature and its analytical toolchain.

- They belong in this module because for a large class of research questions they are simply the correct answer, and because they set the price and openness benchmark against which ActiGraph/ Ametris and the consumer platforms should be judged.

## Products / Platform Architecture

- **Axivity AX3**, accelerometer-only logger. **Axivity AX6**, adds a gyroscope. Both derive from
- the Open Movement project at Newcastle University. **Verified** (github.com/digitalinteraction/openmovement/wiki/AX3).
- **GENEActiv Original / GENEActiv Sleep** (Activinsights), wrist-worn raw accelerometer with
- additional light and near-body temperature channels on the Original.
- **GENEActiv supply status (re-checked 2026-10-09, Corroborated).** Activinsights still sells GENEActiv. Its product page was republished on 2026-01-29 with a "Request a Quote" route, a note that each order needs a USB cradle (up to 4 devices per cradle), "Up to 2 months battery life", and a statement that the device is moving from MDD 93/42/EEC Class I to EU MDR compliance. No discontinuation or end-of-life notice appears. The page names a single "GENEActiv" with no Original or Sleep variants, and the site lists a second wearable, the ActivInsights Band. Activinsights Ltd is the only copyright holder ("cph") listed for the GENEAcore R package for raw GENEActiv files, version 1.2.0, published on CRAN on 2026-04-02; its maintainer uses an activinsights.com address (CRAN, checked 2026-10-10; corrected from "co-owns"). Whether the device is in current manufacture, and the lead times, are not stated publicly; ask Activinsights (info@activinsights.com) when ordering. Re-checked 2026-10-10: still "Request a Quote", still "Up to 2 months battery life", no discontinuation notice; the site footer now styles the company "ActivInsights Ltd" (© 2026).

- There is no platform. The architecture is: configure device → participant wears it → return device → download file → analyze.

## Sensors and Data Streams

- Every Module 1 profile uses the same table so devices can be compared row by row. Rows are the sensors named in `CLAUDE.md`. "Present" is about the hardware; "Researcher access" is about what a study can actually obtain, which is the module's central question. "Unclear" means nothing current was verified. The convention is recorded in [`../../shared/profile-table-conventions.md`](../../shared/profile-table-conventions.md).

| Sensor | Present | Researcher access to underlying signal | Resolution or sampling | Notes |
|---|---|---|---|---|
| PPG | No | Not applicable | Not applicable |  |
| ECG | No | Not applicable | Not applicable |  |
| Accelerometer | Yes, all models | Raw, always | **AX3: 12.5 to 3,200 Hz, ±2/4/8/16 g, configurable. AX6: 12.5 to 1,600 Hz, ±2/4/8/16 g.** UK Biobank used 100 Hz at ±8 g, a protocol setting, not the device limit | Verified 2026-10-10 (axivity.com product pages). No vendor-derived metrics exist; every metric comes from the analyst's own pipeline. |
| Gyroscope | AX6 only | Raw | ±125/250/500/1000/2000 dps, configurable | Verified 2026-10-10. Enables orientation and gait work. |
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
- **Maintenance status (re-checked 2026-10-09, Verified from the GitHub repository).** The project now lives at `github.com/openmovementproject/openmovement` (the old `digitalinteraction/openmovement` URL redirects). It is not archived. The repository was last pushed on 2026-08-18, mostly documentation and FAQ edits, and the separate `libomapi` library was updated on 2026-07-21. The tools themselves change slowly. The last OmGui (AX3 GUI) release is **version 45, dated 2022-10-31**. The newest AX3 firmware is **V50** (a WinUSB/generic variant dated 2020-05-19, committed to the firmware source tree 2024-04-26 and added to the download notes 2026-03-11); the newest AX6 firmware is **V56, dated 2019-12-09**. A browser-based configurator, AX Config (`config.openmovement.dev`, repository `openmovement-axconfig`), was last pushed 2025-09-09. Read this as maintained but mature: the documentation and libraries get attention, while OmGui and the firmware have had no feature release in years. Plan on OmGui 45 (Windows, .NET 3.5) or the web configurator.

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
- **Recording duration (re-verified 2026-10-10).** Axivity's product pages state AX3 "30 days @ 12.5Hz; 14 days @ 100Hz" and AX6 "7+ days @ 100Hz, Accel & Gyro" and "31+ days @ 50Hz, Accel only". The Open Movement FAQ (by the team that designed the devices) gives a fuller table of approximate maximum duration on one charge: AX3 packed mode 13.5 days at 100 Hz, 27 days at 50 Hz, about 48 days at 25 Hz and about 65 days at 12.5 Hz (battery-limited; storage would allow 110); AX3 unpacked 9, 18 and 36.5 days at 100, 50 and 25 Hz; AX6 accelerometer-only 18.3, 36.5, 73 and 146 days at 100, 50, 25 and 12.5 Hz; AX6 with gyroscope 7 to 9 days at 25 to 100 Hz. The g-range does not affect duration. **Verified** for Axivity. GENEActiv: the vendor page says only "Up to 2 months battery life"; no official duration table was found (**Unclear**).
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

- Device purchase only; no recurring cost. **Corrected 2026-10-10: Axivity publishes list prices with online purchase.** AX3 puck £139.00, AX3 puck with wrist band (teal or black) £149.00, AX6 puck £199.00, AX6 puck with wrist band £209.00, all excluding VAT, with "Add to cart". **Verified** (axivity.com/product/ax3 and /ax6). The earlier statement that both vendors offer academic pricing is not supported: no academic discount appears on either vendor's pages (**Unclear** whether one exists). GENEActiv remains "Request a Quote" with no public price (**Verified**, activinsights.com, 2026-10-10).
- **Research program and academic data access.** None exists and none is needed: researchers buy the devices at the same list price as anyone, and get the full raw signal by USB with no account, API, user cap, retention rule or data-use terms. The only access difference between buyers is GENEActiv's quote route. **Verified** for Axivity (2026-10-10).

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
- Public pricing is available for Axivity (AX3 £139 to £149, AX6 £199 to £209, ex VAT) but not for GENEActiv (quote only).

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

- ~~Current list pricing for AX3 and AX6?~~ Resolved 2026-10-10 (see Pricing). Still open: GENEActiv price, and whether either vendor offers academic pricing.
- ~~Maximum recording duration for AX3 and AX6?~~ Resolved 2026-10-10 from the Open Movement FAQ (see Participant Experience). Still open: an official GENEActiv duration table.
- ~~Current status and maintenance of the Open Movement project and OmGui?~~ Resolved 2026-10-09: active repository, OmGui last released 2022-10-31 (v45), AX3 firmware V50, AX6 firmware V56; see Derived Metrics / Analytics.
- Is Activinsights' GENEActiv line still in active production and supply? Partly resolved 2026-10-09: still offered for sale by quote with a 2026 product page and no discontinuation notice; manufacturing status and lead times need Activinsights to confirm.
- What is the practical device-loss rate in postal deployments, and how do large cohorts mitigate it?

## Key Links

- Axivity: https://axivity.com/
- Axivity UK Biobank case study: https://axivity.com/case-studies/biobank
- **Open Movement AX3 wiki: https://github.com/digitalinteraction/openmovement/wiki/AX3** (redirects to `github.com/openmovementproject/openmovement`)
- OmGui revision history: https://github.com/openmovementproject/openmovement/blob/master/Downloads/AX3/AX3-GUI-revisions.md
- AX Config web configurator: https://config.openmovement.dev
- GENEActiv product page: https://activinsights.com/digital-health-technologies/professional-wearables/geneactiv/
- UK Biobank Physical Activity Monitor documentation: https://biobank.ndph.ox.ac.uk/ukb/ukb/docs/PhysicalActivityMonitor.pdf
- Doherty et al. PLOS ONE 2017: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0169649
- actipy (Python SDK): https://github.com/OxWearables/actipy
- biobankAccelerometerAnalysis methods: https://biobankaccanalysis.readthedocs.io/en/latest/methods.html

## Sources

- See `../sources.md` entries S-AXV-01 through S-AXV-05, and S-AXV-07 through S-AXV-09 (added 2026-10-09).
- Added 2026-10-10 (rows for `../sources.md` proposed to the coordinator):
  - Axivity, AX3 product page. https://axivity.com/product/ax3 (accessed 2026-10-10). **Primary.** £139/£149 ex VAT; 12.5 to 3,200 Hz; ±2 to 16 g; 30 days at 12.5 Hz, 14 days at 100 Hz.
  - Axivity, AX6 product page. https://axivity.com/product/ax6 (accessed 2026-10-10). **Primary.** £199/£209 ex VAT; 12.5 to 1,600 Hz; ±2 to 16 g; gyroscope ±125 to 2000 dps.
  - Open Movement, AX3 FAQ (recording duration table). https://github.com/openmovementproject/openmovement/blob/master/Docs/ax3/ax3-faq.md (accessed 2026-10-10). **Primary (device designers).**
  - CRAN, GENEAcore package page. https://cran.r-project.org/package=GENEAcore (accessed 2026-10-10). **Primary.** Version 1.2.0, published 2026-04-02, Activinsights Ltd [cph].
  - Activinsights, GENEActiv product page. https://activinsights.com/digital-health-technologies/professional-wearables/geneactiv/ (accessed 2026-10-10). **Primary.** "Request a Quote"; "Up to 2 months battery life".
