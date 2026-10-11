# Axivity (AX3 / AX6) and GENEActiv, open research-grade accelerometers

## Quick Facts

| Field | Details |
|---|---|
| Organization | Axivity Ltd (UK, from Open Movement / Newcastle University); Activinsights Ltd (UK, GENEActiv; styles itself "ActivInsights"; US office in Texas since June 2025) |
| Category | Research-grade raw-accelerometry logging sensors. Activinsights also sells a behaviour-classifying wearable (ActivInsights Band) and cloud data services |
| Current status | Active, both vendors (vendor fact records, 2026-10-11) |
| Platforms/devices | Axivity **AX3** (accelerometer), **AX6** (accelerometer + gyroscope), both also recording light, internal temperature and battery; **GENEActiv** (hardware revisions 1.1, 1.2 and 1.3; 1.3, shipped 2026, adds Bluetooth adherence sync); ActivInsights Band (covered here only where it bears on GENEActiv studies) |
| Open source | **Axivity: firmware and software BSD 2-clause; hardware and enclosure CC BY 3.0.** GENEActiv: proprietary device; open R packages (GENEAread, GENEAclassify, GENEAcore, GPL); SDKs under licence; vendor R Markdown tools non-commercial only |
| Hosting/deployment | **Axivity: none.** Devices log to flash and are read over USB; no vendor cloud or account. **Activinsights: USB-local by default, cloud optional.** GENEActiv .bin files can stay local or be uploaded to an Azure-hosted platform (Study Management Hub, Device Manager, per-study APIs); the Band uploads to that cloud through the ActivInsights Companion app |
| Pricing model | **Axivity publishes list prices** (AX3 from £139, AX6 from £199, ex VAT), one-time purchase, no platform fee. **GENEActiv by quote only**, minimum order values apply; Activinsights cloud APIs, SDK licences, Study Management Hub and Study Services are priced on request |
| Last verified | 2026-10-11 (vendor fact records, `facts/axivity.yaml` and `facts/activinsights-geneactiv.yaml`); earlier passes 2026-08-21, 2026-10-09 and 2026-10-10 |

## Summary

- These are the devices behind the largest accelerometry cohorts in the world. They sit at the opposite pole from the consumer platforms in this module, with calibrated raw triaxial acceleration written to onboard flash and analysed in open pipelines.
- **The two vendors' data paths now differ (vendor fact records, 2026-10-11).**
  - **Axivity** is USB-only. No vendor cloud, no API service, no account, no subscription. Axivity never receives study data. Its free OmGui software does include simple open analysis (signal vector magnitude, cut-points, wear time, sleep), run on the researcher's own computer.
  - **Activinsights** can still be used the same way (GENEActiv plus a USB cradle, files kept locally), but it now also runs an Azure-hosted cloud with configurable APIs, a Study Management Hub with real-time device and adherence status, the ActivInsights Band, paid Study Services offering 150+ digital measures, and Bluetooth adherence sync on GENEActiv 1.3. A study that uses any of these puts data with Activinsights.
- The UK Biobank physical activity substudy used **Axivity AX3** devices to collect wrist-worn accelerometry in over 100,000 participants at **100 Hz, ±8 g, over seven days**. GENEActiv was used in the Whitehall II, Fenland, and Pelotas cohorts. Between them, these two devices underpin most of the modern open-science physical-activity literature and its analytical toolchain.
- They belong in this module because for a large class of research questions they are the correct answer, and because they set the price and openness benchmark against which ActiGraph/Ametris and the consumer platforms should be judged.

## Products / Platform Architecture

- **Axivity AX3**, triaxial accelerometer logger (Analog Devices ADXL345). **Axivity AX6**, adds a triaxial gyroscope (Bosch BMI160). Both also always record light, internal device temperature and battery voltage. Both derive from the Open Movement project at Newcastle University. **Verified** (Open Movement AX3 FAQ and auxiliary-data docs, github.com/openmovementproject/openmovement; vendor fact record, 2026-10-11).
- **Axivity hardware changes (vendor fact record, 2026-10-11).** The AX3v2 replaced the original AX3 enclosure (datasheet dated 18/04/2023) and is described as functionally identical; the AX3 v1 datasheet link now returns 404. No end-of-life has been announced for AX3 or AX6. The WAX3 and WAX9 wireless sensors are no longer in the store, and the Multi Dock page returns 404. **Corroborated** (axivity.com/files/resources/AX3v2_Datasheet.pdf; axivity.com/products).
- **GENEActiv** (Activinsights), wrist-worn raw accelerometer with ambient light, near-body temperature and an event button. Older pages name GENEActiv Original and GENEActiv Sleep; the current product page names a single "GENEActiv".
  - **Hardware revisions.** The IFU (Rev.010) tabulates versions 1.1, 1.2 and 1.3. **GENEActiv 1.3**, supported in the GENEActiv Software and the ActivInsights Companion app from 2026, adds Bluetooth adherence sync during wear and drops the 30, 40, 60, 66.7, 75 and 85.7 Hz options. Support for the oldest units (serials starting 0) is by request. **Verified** (IFU-GENEActiv-Rev.010.pdf; App Store release notes; vendor fact record, 2026-10-11).
  - **Device lifetime.** The IFU states 50 charging cycles or 2 years from purchase. **Verified** (IFU Rev.010).
  - **Regulatory transition.** GENEActiv is moving from the EU Medical Device Directive to the EU MDR under the Regulation 2023/607 transition. **Verified** (GENEActiv product page).
- **GENEActiv supply status (re-checked 2026-10-09 and 2026-10-11).** Activinsights still sells GENEActiv by quotation. No discontinuation or end-of-life notice appears. Activinsights Ltd is the only copyright holder listed for the GENEAcore R package (version 1.2.0, CRAN, 2026-04-02). Manufacturing status and lead times are not stated publicly; ask Activinsights (info@activinsights.com) when ordering.
- **Activinsights platform components (vendor fact record, 2026-10-11).**
  - GENEActiv Software (Windows and macOS, free), for device setup and USB extraction to .bin.
  - ActivInsights Device Manager, which uploads .bin files to the Study Management Hub.
  - Study Management Hub (demo by request), real-time device, participant and adherence status.
  - ActivInsights Companion app (iOS, Android, Windows; formerly the Band uploader), now serving both the Band and GENEActiv 1.3.
  - Azure-hosted raw data management, analysis and API platform.
  - ActivInsights Band, which classifies behaviour on the device and uploads behavioural events; no raw sensor output is documented.
- **Architecture.** For Axivity, and for GENEActiv used by USB alone, there is no platform: configure device → participant wears it → return device → download file → analyse. Activinsights adds an optional cloud layer on top of that path.

## Sensors and Data Streams

- Every Module 1 profile uses the same table so devices can be compared row by row. Rows are the sensors named in `CLAUDE.md`. "Present" is about the hardware; "Researcher access" is about what a study can actually obtain, which is the module's central question. "Unclear" means nothing current was verified. The convention is recorded in [`../../shared/profile-table-conventions.md`](../../shared/profile-table-conventions.md).

| Sensor | Present | Researcher access to underlying signal | Resolution or sampling | Notes |
|---|---|---|---|---|
| PPG | No | Not applicable | Not applicable |  |
| ECG | No | Not applicable | Not applicable |  |
| Accelerometer | Yes, all models | Raw, always | **AX3: 12.5 to 3,200 Hz, ±2/4/8/16 g, 10-bit packed or 13-bit unpacked. AX6: 12.5 to 1,600 Hz, ±2/4/8/16 g. GENEActiv: 10 to 100 Hz, ±8 g, 12 bit; version 1.3 offers 10, 20, 25, 50 and 100 Hz only.** UK Biobank used 100 Hz at ±8 g, a protocol setting, not the device limit | Verified 2026-10-11 (axivity.com product pages; axivity.com/help/22; GENEActiv Product Information Sheet Rev.002 and IFU Rev.010). Axivity sensors keep their own timing, so the actual rate varies slightly from nominal; resample if a fixed rate is needed. |
| Gyroscope | AX6 only | Raw | 12.5 to 1,600 Hz; ±125/250/500/1000/2000 dps, configurable | Verified 2026-10-11. Enables orientation and gait work. |
| Magnetometer | No | Not applicable | Not applicable |  |
| Temperature | Yes, all models | Raw. AX3 and AX6 record internal device temperature; GENEActiv records near-body temperature | AX3 and AX6: sampled at 1 Hz, stored once per data sector. GENEActiv: at least every 30 s | AX temperature is mainly for accelerometer auto-calibration and is affected by skin, coupling and environment. OmGui, cwa-convert and the Axivity help pages used different conversion formulas until the maintainer settled the correct one in July 2023 (openmovement GitHub issue 11); convert older absolute readings. Verified 2026-10-11 (ax3-auxiliary.md; GENEActiv Product Information Sheet). |
| SpO2 | No | Not applicable | Not applicable |  |
| GPS | No | Not applicable | Not applicable |  |
| Barometer / altimeter | No | Not applicable | Not applicable |  |
| EDA | No | Not applicable | Not applicable |  |
| Ambient light | Yes, all models | Raw. AX3 and AX6 give a relative light level; GENEActiv gives a light channel in the .bin file | AX3 and AX6: 1 Hz, stored once per sector. GENEActiv: Unclear | AX light reads through the case and is a relative indicator, not calibrated lux. GENEActiv 1.2 and later need the light calibration added in GGIRread 1.0.11 (September 2026); older GGIRread versions read it uncalibrated. Verified 2026-10-11. |
| Other | Yes | Raw | AX3 and AX6: battery voltage at 1 Hz; internal clock drifts about ±2 s per day. GENEActiv: event-button presses | Verified 2026-10-11 (ax3-auxiliary.md, ax3-faq.md; GENEActiv product page). |

**Verification.** Verified for the AX3 UK Biobank configuration (UK Biobank Physical Activity Monitor documentation; Doherty et al., PLOS ONE 2017). See `../sources.md` entries S-AXV-01 through S-AXV-05. The accelerometer, temperature, ambient light and other rows were updated 2026-10-11 from the vendor fact records (`facts/axivity.yaml`, `facts/activinsights-geneactiv.yaml`). Earlier versions of this table listed temperature and light as GENEActiv-only; the AX3 and AX6 have both channels.

### Notes from earlier verification passes

| Device | Streams | Notes |
|---|---|---|
| AX3 | Triaxial accelerometer; also light, internal temperature and battery (corrected 2026-10-11) | Configurable rate and range; UK Biobank used 100 Hz, ±8 g |
| AX6 | Triaxial accelerometer + triaxial gyroscope; also light, internal temperature and battery (corrected 2026-10-11) | Gyroscope enables orientation/gait work |
| GENEActiv Original | Triaxial accelerometer, light, near-body temperature | Light channel is useful for circadian work |

- **Verified** for the AX3 UK Biobank configuration (UK Biobank Physical Activity Monitor documentation; Doherty et al., PLOS ONE 2017).

- **The devices store raw data only and compute nothing on board** (corrected 2026-10-11; the ActivInsights Band is the exception, see below). Derived metrics come from three places, all described under Derived Metrics / Analytics.
  - Axivity's OmGui, which has built-in open analysis run locally.
  - Activinsights' software, Sleep Toolkits and paid analysis service.
  - Third-party open pipelines such as GGIR.

## Derived Metrics / Analytics

- **Axivity OmGui built-in analysis (vendor fact record, 2026-10-11).** OmGui, through omconvert, derives signal vector magnitude epochs, MET cut-point time in activity intensity bands, wear-time validation and a simple sleep-period detector. These are published, open algorithms run on the researcher's own computer. No step count is offered. **Verified** (github.com/openmovementproject/openmovement/wiki/AX3-GUI; axivity.com/downloads/ax3).
- **Activinsights analysis (vendor fact record, 2026-10-11).**
  - The GENEActiv Software produces epoch summaries (epoch CSV and AWD).
  - The web Actigraphy Sleep Toolkit (free) and the Advanced Sleep Toolkit (free up to 10 participants) score total sleep, sleep onset latency, sleep efficiency, WASO and naps.
  - The vendor advertises 150+ digital measures (activity intensity, sedentary vs movement, posture changes, sleep/wake, sleep events) delivered through its analysis service. The data acquisition page says 50+ measures are regularly used. **Verified** as vendor statements (activinsights.com GENEActiv product page; advance_sleeptoolkit page).
  - The ActivInsights Band classifies about 12 activities on the device (including sleep, sedentary, standing, walking, running, cycling, swimming, exercise and non-wear) and estimates steps and energy expenditure. **Verified** (activinsights.com/resources/activinsights-band-support/).
  - The vendor's R Markdown analysis tools are licensed for non-commercial analysis of raw data only and restricted to the Activinsights ecosystem. The CRAN packages are GPL with no such restriction. **Verified** (activinsights.com/resources/geneactiv-support-1-2/).
- **Third-party open pipelines**, the ecosystem's main analytical strength.
  - **GGIR** (R), the dominant open-source package for raw accelerometry: auto-calibration, non-wear detection, ENMO/MAD metrics, sleep detection, circadian metrics. Works with AX3, GENEActiv, and ActiGraph `.gt3x` files. Open for commercial users and for AX6 data.
  - **actipy** (Python, Oxford Wearables Group), SDK for processing wearable sensor data. **Verified** (github.com/OxWearables/actipy).
  - **biobankAccelerometerAnalysis** (Oxford), the machine-learning activity classification pipeline used on UK Biobank data. **Verified** (biobankaccanalysis.readthedocs.io). **Corrected 2026-10-11.** It is under an Academic Use Licence that excludes commercial businesses, and the Open Movement docs say it is not currently compatible with AX6 data. **Verified** (ax3-research.md; github.com/OxWearables/biobankAccelerometerAnalysis/blob/master/LICENSE.md).
- **Open Movement software (OmGui)**, device configuration, download and simple analysis. BSD 2-clause.
- **Maintenance status (re-checked 2026-10-09, Verified from the GitHub repository; firmware labels corrected 2026-10-11).** The project now lives at `github.com/openmovementproject/openmovement` (the old `digitalinteraction/openmovement` URL redirects). It is not archived. The repository was last pushed on 2026-08-18, mostly documentation and FAQ edits, and the separate `libomapi` library was updated on 2026-07-21.
  - The last OmGui (AX3 GUI) release is **version 45, dated 2022-10-31**.
  - AX3 firmware **V50** (dated 2020-05-19) is labelled "experimental", an alternative generic and WinUSB interface build. **V48 is the newest standard AX3 release.** The newest AX6 firmware is **V56, dated 2019-12-09**. **Verified** (Downloads/AX3/AX3-Firmware.md, 2026-10-11).
  - A browser-based configurator, AX Config (`config.openmovement.dev`, repository `openmovement-axconfig`), was last pushed 2025-09-09. It configures one device at a time and **cannot download data**. **Verified** (ax3-research.md, 2026-10-11).
  - Read this as maintained but mature. Plan on OmGui 45 (Windows, .NET 3.5) or the cross-platform command-line converters for download, with the web configurator for setup only.

- Because the open analysis code is published, a study that runs its pipeline in OmGui, GGIR or similar is **reproducible in a way that no consumer-wearable study can be.** Every transformation from raw acceleration to endpoint is inspectable. This does not extend automatically to measures bought from the Activinsights analysis service or to Band outputs, whose algorithms the record does not show to be published.

## Active Data Collection

- Essentially none. These devices have no screen and no participant interaction. GENEActiv has an event button whose presses are recorded as markers in the data. **Verified** (GENEActiv product page, 2026-10-11).

## Researcher and Study Management Features

- **Axivity: none from the vendor.** Enrollment, shipping, adherence, and data management are the research team's job. AX-Deploy supports mass deployment with per-device configuration, but it is not compatible with AX6 gyroscopes. **Verified** (ax3-research.md, 2026-10-11).
- **Activinsights: optional.** The Study Management Hub (demo by request) gives real-time device and participant status and adherence, fed by Device Manager uploads and, on GENEActiv 1.3, by Bluetooth adherence sync. Paid, quoted Study Services cover study design, logistics and deployment, GENEActiv and R Markdown training, data acquisition and analysis, and algorithm development. **Verified** (activinsights.com/demo-request-study-management-hub/; activinsights.com/research-study-services/; vendor fact record, 2026-10-11).
- In practice, large cohorts handle logistics by post. UK Biobank dispatched devices configured to **start recording automatically at 10am two working days after dispatch** and run for seven days. **Verified.** That timed-start capability is the feature that makes fully postal, zero-contact deployment work.

## Data Access and Export

- **Axivity, USB only (vendor fact record, 2026-10-11).**
  - The device mounts as a USB drive holding `CWA-DATA.CWA`, in the open `.cwa` format. Download takes about 6 minutes per 7 days of data.
  - OmGui (Windows only) downloads and exports CSV or WAV. omconvert and cwa-convert do the same from the command line on Mac and Linux.
  - The file loads directly into GGIR, openmovement-python, pampro and MATLAB.
  - libOMAPI (C) and the third-party axR R package let teams build their own configuration and download software.
  - No wireless sync, phone app or cloud. No rate limits. **Verified** (github.com/openmovementproject/openmovement/wiki/AX3-GUI; ax3-research.md).
- **GENEActiv, USB route (vendor fact record, 2026-10-11).**
  - The free GENEActiv Software (Windows, macOS) extracts recordings over a USB cradle that holds 4 devices, saving a `.bin` file. It also converts to raw CSV, epoch CSV or epoch AWD (for Actiware-style scoring or the Sleep Toolkit). The open R packages read `.bin` directly.
  - Plugging a recording device into the cradle ends the recording. **Verified** (IFU Rev.010).
- **GENEActiv 1.3, Bluetooth adherence route.** A background app (Windows, macOS, Android; iOS for adherence only) extracts adherence data roughly every five hours during wear, and each sync erases the adherence data on the device. Bluetooth 5 is required. Raw data still come off by USB. **Verified** (IFU Rev.010).
- **Activinsights cloud route (optional).** The ActivInsights Device Manager uploads `.bin` files to the Study Management Hub. Band data upload wirelessly through the Companion app. Data come out through the Band Clinic App, reports, or per-study configurable APIs (raw, event, summary, health, management and quality data). No public API reference exists, and rate limits are not public. **Verified** (activinsights.com/research-study-services/apps-software/; /data-infrastructure/).
- **Retention.**
  - Axivity: recordings never reach the vendor, so retention is the researcher's own. Axivity's privacy policy covers only customer and order data, kept for 6 years. **Verified** (axivity.com/privacy).
  - Activinsights: the GENEActiv and Band privacy notices set a 10-year review retention period for personal data. USB-extracted GENEActiv data stay in the study's own store unless sent to Activinsights. The Google Play data-safety label for the Companion app says data cannot be deleted, which sits awkwardly with the erasure rights in the privacy notices. **Verified** (activinsights.com privacy notices; play.google.com listing for com.activinsights.banduploader).

## APIs, SDKs, and Extensibility

- **Axivity (corrected 2026-10-11).** There is a documented local USB device API. libOMAPI (C) can be used to build custom configuration and download software, and the third-party axR package (Circadia Lab, r-universe v0.1.3, not on CRAN) exposes device discovery, configuration and download from R. No registration is needed. This is a device API, not a cloud web API. Open firmware and hardware mean a motivated group can modify the device itself, which is unique in this module. Source under BSD 2-clause; hardware/enclosure designs under CC BY 3.0. **Verified** (ax3-research.md; github.com/openmovementproject/libomapi; circadia-bio.r-universe.dev/axR).
- **Activinsights (vendor fact record, 2026-10-11).** No self-serve developer program, developer portal or public API reference. SDKs are provided under licence on contact; the licence terms are not published, and the product page's "open SDKs" wording conflicts with the apps page's "under licence". Cloud APIs are configured per study. The GPL R packages GENEAread, GENEAclassify and GENEAcore read and process `.bin` files. **Verified** (activinsights.com/research-study-services/apps-software/; cran.r-project.org/package=GENEAcore).

## Deployment and Infrastructure

- **Axivity, and GENEActiv by USB alone.** None required beyond a laptop with OmGui or the GENEActiv Software (plus a USB cradle for GENEActiv). This is the cheapest and simplest deployment model of any option in Module 1.
- **Activinsights cloud.** Using the Study Management Hub, Device Manager uploads, Bluetooth adherence or the Band adds the vendor's Azure-hosted platform (region not stated) and, for GENEActiv 1.3 adherence, a background app on a Bluetooth 5 computer or Android phone. **Corroborated** (activinsights.com/research-study-services/data-infrastructure/).

## Participant Experience

- Small, sealed, screenless, waterproof pucks worn on a wrist strap (or thigh/hip with tape/belt).
- **Axivity recording duration (re-verified 2026-10-10; conflict recorded 2026-10-11).**
  - **AX3, Axivity's own figures disagree (Unclear).** The AX3v2 datasheet description says "up to 21 days" with no rate attached, while the same datasheet's spec table and the product page say 30 days at 12.5 Hz and 14 days at 100 Hz. The 14 days at 100 Hz figure agrees across sources. **Conflict** (AX3v2_Datasheet.pdf v1.8; axivity.com/product/ax3).
  - The Open Movement FAQ (by the team that designed the devices) gives a fuller table of approximate maximum duration on one charge: AX3 packed mode 13.5 days at 100 Hz, 27 days at 50 Hz, about 48 days at 25 Hz and about 65 days at 12.5 Hz (battery-limited; storage would allow 110); AX3 unpacked 9, 18 and 36.5 days at 100, 50 and 25 Hz; AX6 accelerometer-only 18.3, 36.5, 73 and 146 days at 100, 50, 25 and 12.5 Hz; AX6 with gyroscope 7 to 9 days at 25 to 100 Hz. The FAQ marks some low-rate figures as uncertain. The g-range does not affect duration.
  - **AX6.** About 7 days at 100 Hz with gyroscope; 31+ days at 50 Hz and up to 140 days at 12.5 Hz accelerometer only. **Verified** (axivity.com/product/ax6; AX6_Datasheet.pdf).
  - UK Biobank's activity monitor document (v2.0, 2025) reports 17% incomplete kits in season 1 of its repeat study, attributed to battery performance in reused devices. Plan for shorter windows on old units. **Reported** (UK Biobank document, cited in the vendor fact record; not re-probed).
- **GENEActiv recording duration (vendor fact record, 2026-10-11): vendor documents conflict (Unclear).**
  - The Product Information Sheet and the IFU's specification table give 14 days at 100 Hz and 60 days at 20 Hz.
  - The IFU's own per-version table gives, for versions 1.2 and 1.3, 14 days at 100 Hz, 44 at 20 Hz and 56 at 10 Hz (version 1.1: 7 and 30).
  - The FAQ gives 7 days at 100 Hz and 30 at 20 Hz, matching the version 1.1 column.
  - Most likely reading: 14 days at 100 Hz holds for 1.2 and 1.3; plan on 44 days at 20 Hz until the vendor confirms. A start delay cuts the achievable period by about 5% per week (IFU). The product page still says "Up to 2 months battery life". **Conflict** (Product-Information-Sheet-Rev.002.pdf; IFU-GENEActiv-Rev.010.pdf; activinsights.com/resources/faqs/).
- **No charging during the wear period**; battery is sized for the recording window. For UK Biobank's protocol, a single charge covered the full seven days at 100 Hz.
- **Axivity, and GENEActiv 1.1 and 1.2 used by USB:** no app, no phone, no account, no sync, no notifications. Missing data from sync failure is structurally impossible. **GENEActiv 1.3** adds an optional Bluetooth adherence sync roughly every five hours during wear; raw data still depend only on device return (corrected 2026-10-11).
- Participant burden is close to zero; the burden is mainly logistical (posting devices out and getting them back).
- Device recovery is the main operational risk: unreturned devices are a direct financial loss.

## Privacy, Security, and Compliance

- **Axivity (vendor fact record, 2026-10-11).**
  - Axivity never receives, hosts or processes participant data. Recordings stay on the device until the researcher downloads them over USB, so data residency is wherever the research team keeps the files. **Verified** (ax3-faq.md; AX3-GUI wiki).
  - Not a business associate or a processor for study data, so no BAA or DPA is needed for the data path; none is mentioned on any page checked. If a third-party service handles collection or analysis, the question moves to that party.
  - The privacy policy cites UK GDPR bases for customer and website data only. No HIPAA statement, ISO 27001, ISO 13485 or SOC 2 claim was found; there is no hosted service they would apply to. **Corroborated** (axivity.com/privacy).
  - No AI or ML training terms; Axivity never receives sensor data.
  - **Regulatory.** openFDA 510(k), registration-listing and UDI searches for Axivity returned no matches on 2026-10-11. The datasheets cite CE under the EMC Directive 2014/30/EU and FCC Part 15 Class B, not medical device regulation; the AX3v2 is presented as a research logger. **Corroborated** (api.fda.gov; AX3v2_Datasheet.pdf).
- **Activinsights (vendor fact record, 2026-10-11).**
  - **USB route.** Raw GENEActiv data extracted by USB go to the study's own local store and never reach the vendor. **Corroborated** (activinsights.com/research-study-services/apps-software/).
  - **Cloud route.** Uploading `.bin` files to the Study Management Hub or the Advanced Sleep Toolkit, using Bluetooth adherence sync, or using the Band moves data to the vendor's cloud, which makes Activinsights a processor. The platform is hosted on Microsoft Azure (region not stated), data services are UK-based under GDPR, the privacy notices list GB as the processing country, and directly identifying data are held outside the cloud in study-specific systems. No US or EU residency option is documented. **Corroborated** (vendor statements; activinsights.com/research-study-services/data-infrastructure/).
  - **No BAA, HIPAA statement or DPA is published**, despite the 2025 US office. The privacy notices describe processing by Coelition members on the controller's instructions. Activinsights is ICO-registered (ZA258669). **Verified** for the absence (activinsights.com/legal-data-protection/, 2026-10-11).
  - **ISO 27001: unclear.** The only published certificate (British Assessment Bureau 239005, ISO/IEC 27001:2017) expired on 31 October 2025, while the company page and sleep toolkit pages still claim certification. A current certificate may exist unpublished; ask the vendor before relying on it. No SOC 2 claim. **Unclear** (activinsights.com certificate PDF, read 2026-10-11).
  - **AI training.** No term addresses AI or ML training. The privacy notices allow use of data to support health and medical research, and the algorithm-development page describes permissioned data access with machine learning as a method, so secondary use for algorithm work is neither ruled in nor out. Ask the vendor.
  - **Regulatory.** GENEActiv is listed with FDA, not cleared: establishment registration 3014083954, product code IKK (isokinetic testing and evaluation system, 21 CFR 890.1925), class 2, 510(k) exempt, listed 2018-01-04. No 510(k), De Novo or PMA. The vendor's own class statements do not match the listing: IFU Rev.010 cites FDA Class II under 21 CFR 882.1400 and 882.5050 and calls GENEActiv EU MDR Class IIa, while the product page calls it MDD Class I. A sleep-assessment claim (product code LEL under 882.5050) would need a 510(k), so the IKK listing does not cover that use (inference). The Band has no FDA listing. **Verified** (accessdata.fda.gov registration listing for owner/operator 10056642; openFDA).
- The simplest IRB/ethics story in the module remains available for Axivity, and for GENEActiv used by USB alone. It no longer describes Activinsights as a whole.

## Pricing

- **Axivity (vendor fact record, 2026-10-11).**
  - AX3 puck £139.00, with wrist band £149.00; AX6 puck £199.00, with wrist band £209.00; all ex VAT, sold online with "Add to cart". A micro USB cable is £3.50 extra. **Verified** (axivity.com/product/ax3, /ax6, /products).
  - Prices rose £10 during 2025 (AX3 was £129.00, AX6 £189.00 in Internet Archive captures); third-party guides still quote £129. Postage is extra and international buyers pay customs duties. The hardware warranty is one year and excludes software.
  - No academic, research or volume discount appears on any page. Large UK institutional buys have gone through public contracts (a 2021 Newcastle University award for AX6 devices, £200,000, no unit price), which suggests negotiated pricing exists but is not posted. **Not public**; ask info@axivity.com.
  - No subscription, platform fee or software fee.
- **Activinsights (vendor fact record, 2026-10-11).**
  - GENEActiv is priced by quotation only, in GB pounds unless agreed otherwise, with quotes valid 90 days. Minimum order values apply (amount not published) and products must be ordered in the price list's pack sizes. **Verified** (Activinsights Terms and Conditions, 2024).
  - A competitor's guides (Fibion) put GENEActiv at about £425 to £510 per device. **Reported** only; the source sells competing devices and its figures may predate the current 2.0 GB devices. A USB cradle is also needed.
  - One-year warranty; a recycling programme gives £5 off a replacement GENEActiv per device returned. No academic discount found.
  - The GENEActiv Software and the web Actigraphy Sleep Toolkit are free; the Advanced Sleep Toolkit is free up to 10 participants, with no published price beyond that.
  - Cloud API, SDK licence, Study Management Hub and Study Services pricing is not public. The Band price is not public; Band software access for up to one year is included, then renewed annually at an unpublished price.
- **Research program and academic data access (corrected 2026-10-11).**
  - **Axivity** has no named research or academic program and needs none: researchers buy devices at list price and get the full raw signal by USB. The Open Movement research guide names third parties offering paid help (McRoberts for data collection and processing; Vincent van Hees, the GGIR author, for consulting). The McRoberts link redirected to its homepage on 2026-10-11, so whether that service is still offered is unclear. **Corroborated**.
  - **Activinsights** also has no named program, discount or device-loan scheme, but research is its core market, served through quoted device sales and paid Study Services. Devices are supplied to healthcare professionals, researchers and clinical trial organisations. **Verified** (activinsights.com/research-study-services/).
  - **Activinsights terms of sale, clause 24 (all customers).** The customer may not publish or release any materials about the operation or use of the product without Activinsights' prior written consent. This is relevant to methods papers and device documentation; whether it is enforced against academic publications is unknown. **Verified** (Activinsights-Terms-and-Conditions.pdf).

- **The absence of any software licence or platform subscription is the key economic point** for Axivity and for GENEActiv used by USB: unlike ActiGraph (ActiLife ~$1,695, CentrePoint ~$3,500/yr per third-party report), the core toolchain is free and open. Exceptions are biobankAccelerometerAnalysis (academic use only) and Activinsights' R Markdown tools (non-commercial only).

## Research Evidence and Validation

- **UK Biobank**: AX3 accelerometry in 100,000+ participants, the largest such dataset in existence, with published methods (Doherty et al., PLOS ONE 2017). **Verified.**
- Axivity's case studies also cite **INTERVAL** (6,000 participants, AX3 band). **Verified** as a vendor statement (axivity.com/case-studies/biobank, vendor fact record 2026-10-11).
- The AX3 "demonstrated equivalent signal vector magnitude output on multi-axis shaking tests to the GENEActiv accelerometer used in the Whitehall II, Fenland and Pelotas cohorts." **Verified** (UK Biobank / PLOS ONE methods).
- GENEActiv has its own substantial validation literature and cohort footprint.
- Cross-device comparability between AX3, GENEActiv, and ActiGraph at the raw-signal level is reasonably well established, which is why GGIR supports all three, a major practical advantage when harmonizing across cohorts.
- Neither device measures heart rate, so cardiovascular validation questions do not arise.

## Strengths

- **Fully open (Axivity)**: firmware/software BSD-licensed, hardware CC BY, documented device API. Nothing else here is remotely this open.
- **Reproducible end-to-end** when analysed with open pipelines (OmGui, GGIR, actipy): every step from signal to endpoint is inspectable.
- Direct comparability with UK Biobank, Whitehall II, Fenland, Pelotas and the wider cohort literature.
- **Axivity, and GENEActiv by USB:** no cloud, no vendor in the data path, no data processor, the simplest ethics and data-governance story in the module.
- No sync dependency, no phone dependency, no participant app on the USB route: structurally immune to the dominant failure mode of consumer wearable studies.
- **GENEActiv 1.3 adds optional in-wear adherence monitoring** by Bluetooth, with a Study Management Hub view, while keeping raw data on the USB route. No other raw logger in this profile offers this.
- Timed-start configuration enables fully postal deployment at scale.
- No subscription, software licence or platform fee for Axivity or for GENEActiv used by USB.
- Cheaper than ActiGraph for equivalent (or better) raw-data capability, at least for Axivity's published prices.

## Limitations

- **Movement plus light and temperature only.** No heart rate, HRV, SpO2 or any cardiovascular signal. AX3 and AX6 temperature is internal device temperature, mainly for calibration; GENEActiv's is near-body.
- No real-time raw data; you learn nothing about the signal until the device comes back. **Adherence monitoring during wear is impossible on Axivity and on GENEActiv 1.1 and 1.2**; it is possible on GENEActiv 1.3 through Bluetooth sync roughly every five hours (corrected 2026-10-11).
- Fixed recording window bounded by battery and memory; not a continuous months-long instrument. Both vendors publish conflicting duration figures (AX3; GENEActiv at 20 Hz), so pilot the chosen rate.
- Requires the research team to have real analytical capability (R/Python, GGIR competence) for anything beyond OmGui's simple outputs. There is no step count from Axivity; OmGui exports SVM epochs, cut-point time, wear time and sleep periods.
- Device recovery logistics and loss are a genuine cost.
- **Axivity has no study management**; Activinsights offers a Study Management Hub and paid services. Neither offers participant engagement or intervention capability.
- Cannot support any adaptive or feedback-based design.
- Public pricing is available for Axivity (AX3 £139 to £149, AX6 £199 to £209, ex VAT) but not for GENEActiv (quote only, minimum order values).
- Activinsights terms of sale restrict publishing material about the product's operation or use without consent (clause 24).
- Activinsights' ISO 27001 status is unclear (certificate expired 2025-10-31), and no BAA, HIPAA statement or DPA is published for its cloud.

## Best-Fit Use Cases

- **Population-scale physical activity and sedentary behaviour epidemiology.**
- Any study needing harmonization with UK Biobank or comparable cohorts.
- Circadian rest, activity rhythm research (GENEActiv's light channel is valuable here; AX3 and AX6 light is relative only).
- Studies with strict data-governance constraints that prohibit vendor clouds (Axivity, or GENEActiv by USB alone).
- Raw-data studies that want in-wear adherence checks without a smartphone app on the participant's side (GENEActiv 1.3).
- Sleep, wake timing (not staging) over defined 7 to 14 day windows.
- Methods and algorithm development on raw accelerometry.
- Low-resource settings where phones, connectivity, and charging cannot be assumed.

## Poor-Fit Use Cases

- Anything requiring cardiovascular or autonomic measures.
- Real-time monitoring or adaptive interventions; in-wear adherence tracking except on GENEActiv 1.3.
- Continuous monitoring beyond the device's recording window.
- Studies without analytical capacity for raw signal processing.
- Studies wanting participant-facing feedback.
- Sleep-staging research.

## Open Questions

- ~~Current list pricing for AX3 and AX6?~~ Resolved 2026-10-10 (see Pricing). Still open: GENEActiv price, and whether either vendor offers academic or volume pricing (not public as of 2026-10-11).
- ~~Maximum recording duration for AX3 and AX6?~~ Partly resolved 2026-10-10; reopened 2026-10-11 because the AX3v2 datasheet's "up to 21 days" conflicts with its own spec table. GENEActiv now has an official per-version table (IFU Rev.010), but it conflicts with the product sheet (44 vs 60 days at 20 Hz). Ask both vendors.
- ~~Current status and maintenance of the Open Movement project and OmGui?~~ Resolved 2026-10-09: active repository, OmGui last released 2022-10-31 (v45), AX3 firmware V48 standard (V50 experimental), AX6 firmware V56; see Derived Metrics / Analytics.
- Is Activinsights' GENEActiv line still in active production and supply? Largely resolved 2026-10-11: on sale, with the 1.3 revision shipped in 2026; lead times need Activinsights to confirm.
- Does Activinsights hold a current ISO 27001 certificate? (Only published one expired 2025-10-31.)
- Does Activinsights enforce terms-of-sale clause 24 against academic methods papers?
- What are the Activinsights SDK licence terms, and which Azure region hosts its cloud?
- Does McRoberts still offer Axivity data collection and processing services?
- What is the practical device-loss rate in postal deployments, and how do large cohorts mitigate it?

## Vendor Fact Record

### Axivity

<!-- facts:begin axivity -->
*Generated from the fact record by `tools/facts/generate.py`. Edit the record, not this block.*

**Research access**

| Fact | Value |
|---|---|
| Formal research or academic program (name, what it offers) | Not public [2026-10-11] |
| Who can join the research program | n/a |
| How to apply, and any approval or review step | n/a |
| Whether the program is active, paused, renamed or closed | n/a |
| Whether the general developer or API program is open to new applicants | No developer program or registration is needed. The device communication is documented and a C device API (libOMAPI) can be used to build custom configuration and download software; firmware, software and file-format readers are open source under a BSD 2-clause licence. A third-party R wrapper, axR (Circadia Lab, r-universe), exposes device discovery, configuration and download from R. [V, 2026-10-11] |
| Participant or user limits before approval or by tier | n/a |
| How academic access differs from commercial or consumer access | Axivity publishes no academic vs commercial distinction. Everyone pays the same list prices and gets the same BSD 2-clause software. One third-party analysis package the Open Movement docs point to, Oxford's biobankAccelerometerAnalysis, is under an Academic Use Licence that excludes commercial users, and it cannot read AX6 data. [C, 2026-10-11] |

**Pricing**

| Fact | Value |
|---|---|
| Device or hardware list price | **AX3:** AX3 puck GBP 139.00, or GBP 149.00 with wrist band (ex VAT). Cable not included (micro USB cable GBP 3.50). [V, 2026-10-11]<br>**AX6:** AX6 puck GBP 199.00, or GBP 209.00 with wrist band (ex VAT). Cable not included. [V, 2026-10-11] |
| Consumer subscription or membership price | n/a |
| Research or academic pricing or discount | Not public [2026-10-11] |
| Fees for API, SDK, platform or data access | None. Firmware, OmGui, the device API and file-format tools are open source under a BSD 2-clause licence and free to use. [V, 2026-10-11] |
| Minimum order, term or commitment | Not public [2026-10-11] |
| Whether pricing requires contacting sales | No for standard purchases. List prices are published and orders go through the web store. No quote route for volume or academic pricing is published. [V, 2026-10-11] |

**Data access and terms**

| Fact | Value |
|---|---|
| Raw signals available to researchers, and by which route | Raw, unfiltered triaxial acceleration (AX3: Analog Devices ADXL345; AX6: Bosch BMI160) plus triaxial gyroscope on the AX6, each block timestamped. Both devices also always record low-rate auxiliary channels: light level, internal device temperature and battery voltage. All stored raw on device flash in the open .CWA format and read over USB by the researcher. No vendor cloud. [V, 2026-10-11] |
| Derived or processed metrics available to researchers | The device stores raw data only and computes nothing. OmGui (through omconvert) has built-in, open analysis run by the researcher locally, which derives signal vector magnitude epochs, MET cut-point time in activity intensity bands, wear-time validation and a simple sleep-period detector. Richer metrics come from third-party open-source tools the docs recommend, chiefly GGIR. [V, 2026-10-11] |
| Documented sampling rates or temporal resolution | **AX3:** Accelerometer 12.5 to 3200 Hz configurable, range +/-2/4/8/16 g, 10-bit packed or 13-bit unpacked modes. OmGui default is 100 Hz, +/-8 g. [V, 2026-10-11]<br>**AX6:** Accelerometer and gyroscope 12.5 to 1600 Hz configurable; gyroscope +/-125 to 2000 dps. [V, 2026-10-11]<br>**AX3 and AX6 auxiliary channels and clock:** Light, temperature and battery are sampled internally at 1 Hz and stored once per data sector (every 40 to 120 movement samples, by mode). The internal clock is set from the configuring computer and drifts by about +/-2 seconds per day. [V, 2026-10-11] |
| How far back data can be retrieved | **AX3:** One recording is bounded by battery and memory, and Axivity's own figures disagree. The AX3v2 datasheet description says up to 21 days; the same datasheet's spec table and the product page say 30 days at 12.5 Hz and 14 days at 100 Hz; the Open Movement FAQ gives about 13.5 days at 100 Hz and about 65 days at 12.5 Hz (packed mode). There is no vendor-side history; downloaded files are held by the researcher. (conflict) [U, 2026-10-11]<br>**AX6:** About 7 days at 100 Hz with gyroscope; 31+ days at 50 Hz and up to 140 days at 12.5 Hz accelerometer only. No vendor-side history. [V, 2026-10-11] |
| Export, API, SDK or file routes | USB only. The device mounts as a USB drive holding CWA-DATA.CWA. OmGui (Windows) downloads it and exports CSV or WAV; omconvert and cwa-convert do the same from the command line; the file loads directly into GGIR, openmovement-python, pampro, MATLAB and others. libOMAPI (C) and the third-party axR (R) let teams build their own download software. AX-Deploy handles mass deployment with per-device configuration but not AX6 gyroscopes; the web configurator AX Config configures one device at a time and cannot download. [V, 2026-10-11] |
| API rate limits | n/a |
| Terms on retaining, storing or deleting data | Sensor recordings never reach Axivity, so there are no vendor terms on retaining study data; retention is the researcher's own. The website privacy policy covers only customer and order data, kept for 6 years. [V, 2026-10-11] |
| Terms on using data to train AI or ML models | n/a |
| Announced shutdowns, deprecations or migrations, with dates | Not public [2026-10-11] |

**Compliance and regulatory**

| Fact | Value |
|---|---|
| Whether a HIPAA Business Associate Agreement is offered | n/a |
| Whether a data processing agreement is offered | n/a |
| Published HIPAA statement | Not public [2026-10-11] |
| Published GDPR statement | **Website and order data:** The privacy policy cites UK GDPR lawful bases for customer and website data. It does not address study or participant data, which Axivity does not receive. [C, 2026-10-11] |
| ISO/IEC 27001 status and evidence | Not public [2026-10-11] |
| SOC 2 status and evidence | Not public [2026-10-11] |
| FDA clearances, from the FDA database | Not public [2026-10-11] |
| Where data is stored, and residency options | No vendor storage. Recordings stay on the device's flash memory until a researcher downloads them over USB to their own computer, so residency is wherever the research team keeps the files. [V, 2026-10-11] |

<!-- facts:end -->

### Activinsights (GENEActiv)

<!-- facts:begin activinsights-geneactiv -->
*Generated from the fact record by `tools/facts/generate.py`. Edit the record, not this block.*

**Research access**

| Fact | Value |
|---|---|
| Formal research or academic program (name, what it offers) | No named academic or research access program. Research is the core market, served by device sales on quotation plus paid, quoted Study Services (study design, logistics and deployment, GENEActiv and R Markdown training, data acquisition and analysis, algorithm development), and by free sleep tools (Actigraphy Sleep Toolkit; Advanced Sleep Toolkit free up to 10 participants). [V, 2026-10-11] |
| Who can join the research program | No eligibility rules published. Devices are supplied to healthcare professionals, researchers and clinical trial organisations; the GENEActiv IFU names healthcare professionals as intended users. [V, 2026-10-11] |
| How to apply, and any approval or review step | No application or approval step. Buyers request a quotation through a web form; the Study Management Hub is offered by demo request. [V, 2026-10-11] |
| Whether the program is active, paused, renamed or closed | Active. GENEActiv and the ActivInsights Band are on sale; the GENEActiv 1.3 hardware revision, the macOS GENEActiv Software and the ActivInsights Companion app were updated in 2026; GENEAcore was published on CRAN in April 2026; a US office opened in Texas in June 2025. [C, 2026-10-11] |
| Whether the general developer or API program is open to new applicants | No self-serve developer program, developer portal or public API reference. SDKs are provided under licence on contact; the open R packages GENEAread, GENEAclassify and GENEAcore (GPL) read and process GENEActiv .bin files. [V, 2026-10-11] |
| Participant or user limits before approval or by tier | **Advanced Sleep Toolkit:** The Advanced Sleep Toolkit is free for up to 10 participants; the price beyond that is not published. [V, 2026-10-11]<br>**GENEActiv and ActivInsights Band hardware:** n/a |
| How academic access differs from commercial or consumer access | No separate academic tier or price. The vendor positions GENEActiv for academic researchers wanting raw data. Its R Markdown analysis tools are licensed for non-commercial analysis of raw data only and restricted to the Activinsights ecosystem; the CRAN packages are GPL with no such restriction. [V, 2026-10-11]<br>**Terms of sale, all customers:** Terms of sale clause 24 (Confidentiality), applying to every customer, academic or commercial: the customer may not publish or release, or permit publication of, any materials about the operation or use of the product without Activinsights' prior written consent. Relevant to methods papers and device documentation. [V, 2026-10-11] |

**Pricing**

| Fact | Value |
|---|---|
| Device or hardware list price | **GENEActiv:** No vendor list price (quotation only). A competitor's guides put GENEActiv at about GBP 425 to 510 per device. Stated device lifetime: 50 charging cycles or 2 years. A USB charging cradle (holds 4) is needed as well. [R, 2026-10-11]<br>**ActivInsights Band:** Not public [2026-10-11] |
| Consumer subscription or membership price | **GENEActiv:** No subscription. The GENEActiv Software is a free download, and the web Actigraphy Sleep Toolkit is free. [V, 2026-10-11]<br>**ActivInsights Band:** Band software access for up to one year is included with the Band purchase; unlimited lifestyle reports are then provided on an annual, renewable basis at an unpublished price. [V, 2026-10-11] |
| Research or academic pricing or discount | Not public [2026-10-11] |
| Fees for API, SDK, platform or data access | **Sleep Toolkits:** The Actigraphy Sleep Toolkit is free with no software or licensing fees; the Advanced Sleep Toolkit is free for up to 10 participants. [V, 2026-10-11]<br>**Cloud API, SDK licence, Study Management Hub and Study Services:** Not public [2026-10-11] |
| Minimum order, term or commitment | Minimum order values apply (amount not published); products must be ordered in the pack sizes on the price list. [V, 2026-10-11] |
| Whether pricing requires contacting sales | Yes. Products and services are priced by quotation, in GB pounds unless agreed otherwise, valid 90 days. [V, 2026-10-11] |

**Data access and terms**

| Fact | Value |
|---|---|
| Raw signals available to researchers, and by which route | **GENEActiv:** Raw, unfiltered tri-axial acceleration in SI units (+/- 8 g, 12 bit), ambient light, near-body temperature and event-button presses, stored on the device and extracted to an open-format .bin file over the USB cradle. GENEActiv 1.3 also sends adherence data over Bluetooth during wear; raw data still come off by USB. [V, 2026-10-11]<br>**ActivInsights Band:** No raw sensor output documented. The Band classifies behaviour on the device and uploads behavioural events (open COEL atom format) through the companion app. [C, 2026-10-11] |
| Derived or processed metrics available to researchers | **GENEActiv:** No on-device metrics. The vendor advertises 150+ digital measures (activity intensity, sedentary vs movement, posture changes, sleep/wake, sleep events) delivered by its analysis service; the GENEActiv Software produces epoch summaries; the Sleep Toolkits score sleep (total sleep, onset latency, efficiency, WASO, naps); open R packages are available. [V, 2026-10-11]<br>**ActivInsights Band:** Behavioural events (about 12 activity classes including sleep, sedentary, standing, walking, running, cycling, swimming, exercise and non-wear), steps, energy expenditure, sleep/wake patterns and event markers, delivered in reports, the Band Clinic App or by API. [V, 2026-10-11] |
| Documented sampling rates or temporal resolution | **GENEActiv:** Acceleration selectable from 10 to 100 Hz (+/- 8 g, 12 bit); temperature at least every 30 s. GENEActiv 1.3 offers 10, 20, 25, 50 and 100 Hz only (the IFU table marks the intermediate rates N/A). [V, 2026-10-11]<br>**ActivInsights Band:** Not public [2026-10-11] |
| How far back data can be retrieved | **GENEActiv:** On-device recording length at a given rate is stated three ways. The product sheet and the IFU's specification table give 14 days at 100 Hz and 60 days at 20 Hz; the IFU's own per-version table gives, for versions 1.2 and 1.3, 14 days at 100 Hz, 44 at 20 Hz and 56 at 10 Hz (version 1.1, 7 and 30); the FAQ gives 7 days at 100 Hz and 30 at 20 Hz. Once extracted, files sit in the study's own storage with no vendor limit. (conflict) [U, 2026-10-11]<br>**ActivInsights Band:** The Band monitors for 6 months to a year without charging and should upload at least weekly; cloud-held data fall under a 10-year review retention period. [V, 2026-10-11] |
| Export, API, SDK or file routes | **GENEActiv:** USB route: the free GENEActiv Software (Windows, macOS) extracts .bin files over the 4-unit USB cradle and converts them to raw CSV, epoch CSV or epoch AWD (for Actiware-style scoring or the Sleep Toolkit); the open R packages read .bin. GENEActiv 1.3 adds Bluetooth adherence extraction by a background app (Windows, macOS, Android; iOS adherence only), repeating roughly every five hours. Optional cloud route: the ActivInsights Device Manager uploads .bin files to the Study Management Hub. [V, 2026-10-11]<br>**ActivInsights Band and cloud platform:** Wireless upload through the ActivInsights Companion app (iOS, Android, Windows) to the Azure-hosted cloud; data come out through the Band Clinic App, reports, or configurable APIs (raw, event, summary, health, management and quality data). SDKs under licence. [V, 2026-10-11] |
| API rate limits | Not public [2026-10-11] |
| Terms on retaining, storing or deleting data | Personal data are kept as long as the original purpose needs, with a 10-year review retention period, in the GENEActiv and Band privacy notices. GENEActiv raw data extracted by USB stay in the study's own store unless sent to Activinsights. [V, 2026-10-11] |
| Terms on using data to train AI or ML models | Not public [2026-10-11] |
| Announced shutdowns, deprecations or migrations, with dates | No product shutdown announced. GENEActiv is moving from the EU Medical Device Directive to the EU MDR under the Regulation 2023/607 transition. A GENEActiv 1.3 hardware revision (Bluetooth adherence) shipped in 2026. The Band uploader app was rebranded ActivInsights Companion and now supports both devices. Support for the oldest GENEActiv units (serials starting 0) is by request. [V, 2026-10-11] |

**Compliance and regulatory**

| Fact | Value |
|---|---|
| Whether a HIPAA Business Associate Agreement is offered | Not public [2026-10-11] |
| Whether a data processing agreement is offered | Not public [2026-10-11] |
| Published HIPAA statement | Not public [2026-10-11] |
| Published GDPR statement | Data services are UK-based and operated under GDPR; Activinsights is registered with the ICO (ZA258669); privacy notices follow the COEL consent model and list GB as the processing country. [C, 2026-10-11] |
| ISO/IEC 27001 status and evidence | Unclear |
| SOC 2 status and evidence | Not public [2026-10-11] |
| FDA clearances, from the FDA database | **GENEActiv:** No 510(k), De Novo or PMA. Listed, not cleared, with FDA under establishment registration 3014083954 (owner/operator 10056642, Activinsights Ltd.), product code IKK, isokinetic testing and evaluation system, 21 CFR 890.1925, device class 2, 510(k) exempt; listed 2018-01-04. [V, 2026-10-11]<br>**ActivInsights Band:** Not public [2026-10-11] |
| Where data is stored, and residency options | **ActivInsights Band and cloud platform:** Cloud raw-data management, analysis and API platform hosted on Microsoft Azure (region not stated), data services based in the UK, privacy notices list GB as the processing country; directly identifying data are held outside the cloud in study-specific systems. [C, 2026-10-11]<br>**GENEActiv:** With the USB route, raw data are extracted to the study's own local store and never reach the vendor; uploading .bin files to the Study Management Hub or Advanced Sleep Toolkit moves them to the vendor cloud. [C, 2026-10-11] |

<!-- facts:end -->

## Key Links

- Axivity: https://axivity.com/
- Axivity UK Biobank case study: https://axivity.com/case-studies/biobank
- Axivity AX3v2 datasheet: https://axivity.com/files/resources/AX3v2_Datasheet.pdf
- Axivity AX6 datasheet: https://axivity.com/files/resources/AX6_Datasheet.pdf
- Axivity privacy policy: https://axivity.com/privacy
- **Open Movement repository: https://github.com/openmovementproject/openmovement** (the old `github.com/digitalinteraction/openmovement` links redirect here)
- Open Movement research guide: https://github.com/openmovementproject/openmovement/blob/master/Docs/ax3/ax3-research.md
- OmGui (AX3 GUI) wiki: https://github.com/openmovementproject/openmovement/wiki/AX3-GUI
- OmGui revision history: https://github.com/openmovementproject/openmovement/blob/master/Downloads/AX3/AX3-GUI-revisions.md
- AX3 firmware notes: https://github.com/openmovementproject/openmovement/blob/master/Downloads/AX3/AX3-Firmware.md
- libOMAPI: https://github.com/openmovementproject/libomapi
- AX Config web configurator: https://config.openmovement.dev
- GENEActiv product page: https://activinsights.com/digital-health-technologies/professional-wearables/geneactiv/
- GENEActiv IFU Rev.010: https://activinsights.com/wp-content/uploads/2026/02/IFU-GENEActiv-Rev.010.pdf
- Activinsights apps and software: https://activinsights.com/research-study-services/apps-software/
- Activinsights data infrastructure: https://activinsights.com/research-study-services/data-infrastructure/
- Activinsights Study Management Hub demo: https://activinsights.com/demo-request-study-management-hub/
- Activinsights terms and conditions: https://activinsights.com/wp-content/uploads/2024/11/Activinsights-Terms-and-Conditions.pdf
- Activinsights quote request: https://activinsights.com/sales-quote-geneactiv-2/
- UK Biobank Physical Activity Monitor documentation: https://biobank.ndph.ox.ac.uk/ukb/ukb/docs/PhysicalActivityMonitor.pdf
- Doherty et al. PLOS ONE 2017: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0169649
- actipy (Python SDK): https://github.com/OxWearables/actipy
- biobankAccelerometerAnalysis methods: https://biobankaccanalysis.readthedocs.io/en/latest/methods.html

## Sources

- See `../sources.md` entries S-AXV-01 through S-AXV-05, and S-AXV-07 through S-AXV-13.
- Added 2026-10-10 (rows for `../sources.md` proposed to the coordinator):
  - Axivity, AX3 product page. https://axivity.com/product/ax3 (accessed 2026-10-10). **Primary.** £139/£149 ex VAT; 12.5 to 3,200 Hz; ±2 to 16 g; 30 days at 12.5 Hz, 14 days at 100 Hz.
  - Axivity, AX6 product page. https://axivity.com/product/ax6 (accessed 2026-10-10). **Primary.** £199/£209 ex VAT; 12.5 to 1,600 Hz; ±2 to 16 g; gyroscope ±125 to 2000 dps.
  - Open Movement, AX3 FAQ (recording duration table). https://github.com/openmovementproject/openmovement/blob/master/Docs/ax3/ax3-faq.md (accessed 2026-10-10). **Primary (device designers).**
  - CRAN, GENEAcore package page. https://cran.r-project.org/package=GENEAcore (accessed 2026-10-10). **Primary.** Version 1.2.0, published 2026-04-02, Activinsights Ltd [cph].
  - Activinsights, GENEActiv product page. https://activinsights.com/digital-health-technologies/professional-wearables/geneactiv/ (accessed 2026-10-10). **Primary.** "Request a Quote"; "Up to 2 months battery life".
- Added 2026-10-11 from the vendor fact records (`../../facts/axivity.yaml`, `../../facts/activinsights-geneactiv.yaml`; exact quotes held there):
  - Axivity AX3v2 datasheet. https://axivity.com/files/resources/AX3v2_Datasheet.pdf **Primary.** "Up to 21 days" vs 30 days at 12.5 Hz / 14 days at 100 Hz; EMC Directive; FCC Class B.
  - Axivity AX6 datasheet. https://axivity.com/files/resources/AX6_Datasheet.pdf **Primary.** 7 days IMU at 100 Hz; up to 140 days accelerometer at 12.5 Hz.
  - Axivity privacy policy. https://axivity.com/privacy **Primary.** 6-year retention of customer data; UK GDPR bases.
  - Axivity help pages. https://axivity.com/help/3 and https://axivity.com/help/22 **Primary.** Open API; 10-bit and 13-bit modes.
  - Open Movement research guide. https://github.com/openmovementproject/openmovement/blob/master/Docs/ax3/ax3-research.md **Primary.** Device API; AX-Deploy and web configurator limits; biobankAccelerometerAnalysis licence and AX6 incompatibility; third-party services.
  - Open Movement auxiliary data. https://github.com/openmovementproject/openmovement/blob/master/Docs/ax3/ax3-auxiliary.md **Primary.** Light, temperature and battery always recorded at 1 Hz.
  - OmGui wiki. https://github.com/openmovementproject/openmovement/wiki/AX3-GUI **Primary.** USB download; SVM, cut-points, wear time, sleep; Windows requirement.
  - AX3 firmware notes. https://github.com/openmovementproject/openmovement/blob/master/Downloads/AX3/AX3-Firmware.md **Primary.** V50 experimental.
  - Open Movement issue 11 (read only). https://github.com/openmovementproject/openmovement/issues/11 **Primary (maintainer).** Temperature conversion formula.
  - libOMAPI. https://github.com/openmovementproject/libomapi **Primary.**
  - axR. https://circadia-bio.r-universe.dev/axR **Secondary (third-party package).**
  - biobankAccelerometerAnalysis licence. https://github.com/OxWearables/biobankAccelerometerAnalysis/blob/master/LICENSE.md **Primary.** Academic use only.
  - openFDA searches for Axivity. https://api.fda.gov/device/510k.json?search=applicant:axivity **Primary (regulator).** No matches.
  - GENEActiv IFU Rev.010. https://activinsights.com/wp-content/uploads/2026/02/IFU-GENEActiv-Rev.010.pdf **Primary.** Per-version duration table; Bluetooth adherence; device lifetime; FDA and MDR class statements.
  - GENEActiv Product Information Sheet Rev.002. https://activinsights.com/wp-content/uploads/2026/02/Product-Information-Sheet-Rev.002.pdf **Primary.** 10 to 100 Hz; ±8 g; temperature every 30 s; 60 days at 20 Hz.
  - Activinsights FAQs. https://activinsights.com/resources/faqs/ **Primary.** 7 days at 100 Hz, 30 at 20 Hz.
  - Activinsights apps and software. https://activinsights.com/research-study-services/apps-software/ **Primary.** SDKs under licence; Band Clinic App and API; local sovereign extraction.
  - Activinsights data infrastructure. https://activinsights.com/research-study-services/data-infrastructure/ **Primary (vendor statement).** Azure hosting; configurable APIs; pseudonymisation; UK GDPR.
  - Activinsights Study Services. https://activinsights.com/research-study-services/ **Primary.**
  - Activinsights Advanced Sleep Toolkit. https://activinsights.com/digital-health-technologies/advance_sleeptoolkit/ **Primary.** Free to 10 participants; Device Manager upload.
  - Activinsights GENEActiv support and licence page. https://activinsights.com/resources/geneactiv-support-1-2/ **Primary.** R Markdown tools non-commercial only.
  - Activinsights Band support. https://activinsights.com/resources/activinsights-band-support/ **Primary.**
  - Activinsights Terms and Conditions (2024). https://activinsights.com/wp-content/uploads/2024/11/Activinsights-Terms-and-Conditions.pdf **Primary.** Quotes valid 90 days; minimum order values; clause 24.
  - Activinsights privacy notices. https://activinsights.com/privacy-policies/privacy-policy-for-geneactiv/ and https://activinsights.com/privacy-policies/privacy-policy-for-activinsights-band/ **Primary.** 10-year review retention; GB processing.
  - Activinsights legal and data protection. https://activinsights.com/legal-data-protection/ **Primary.** ICO ZA258669; Coelition.
  - Activinsights ISO 27001 certificate (expired). https://activinsights.com/wp-content/uploads/2023/08/Activinsights-ISO-27001-Certificate-BAB-Exp.-Oct-2025-1.pdf **Primary (certificate, image only).**
  - FDA registration listing, owner/operator 10056642. https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfRL/rl.cfm?start_search=1&ownerOperatorNumber=10056642 **Primary (regulator).** IKK, 510(k) exempt.
  - App Store and Google Play listings. https://apps.apple.com/us/app/activinsights-companion/id1579732913 , https://apps.apple.com/us/app/geneactiv-software/id1658154045 , https://play.google.com/store/apps/details?id=com.activinsights.banduploader **Primary (vendor release notes).** GENEActiv 1.3 support; Companion rebrand; data-safety label.
  - GGIRread 1.0.11 release. https://github.com/wadpac/GGIRread/releases/tag/1.0.11 **Primary (package maintainers).** GENEActiv 1.2+ light calibration.
  - Fibion price guides. https://web.fibion.com/articles/best-accelerometers-circadian-rhythm-research/ **Secondary (competitor).** GENEActiv £425 to £510.
