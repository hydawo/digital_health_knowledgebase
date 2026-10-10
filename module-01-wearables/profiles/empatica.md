# Empatica

## Quick Facts

| Field | Details |
|---|---|
| Organization | Empatica Inc. (US/Italy) |
| Category | Research- and clinical-grade wearable with an FDA-cleared health monitoring platform |
| Current status | Active |
| Platforms/devices | **EmbracePlus** and **EmbraceMini** (current); **E4 wristband** (legacy predecessor, still widely cited in the literature) |
| Open source | No |
| Hosting/deployment | Empatica Cloud; Care Portal web console; AWS S3 data access keys |
| Pricing model | **Published, transparent bundle pricing for academic research**, unusual in this module |
| Last verified | 2026-08-21; biomarker counts re-checked 2026-10-09; pricing, academic discount, sensor modes, FDA clearances and compliance re-verified 2026-10-10 |

## Summary

- Empatica is the platform to reach for when the research question requires **raw physiological signal from a regulated, purpose-built device** rather than a consumer product with an API bolted on. Two things distinguish it:

1. **EDA (electrodermal activity).** Empatica's wrist EDA, available as raw signal with an FDA-cleared EDA parameter, is the reason the device exists for stress, arousal, emotion, seizure, and autonomic research. **Corrected 2026-10-10:** it is not the only EDA source in this module. Samsung's Health Sensor SDK documents a raw `EDA_CONTINUOUS` tracker at 1 Hz on Galaxy Watch8 and later (Samsung data specifications, **Verified**), and the Verily Study Watch records EDA (see `emerging-platforms.md`, **Corroborated**). Among those, Empatica remains the one with a published self-serve academic plan and an FDA-cleared EDA parameter. Apple, Fitbit, Garmin, Oura, WHOOP, Polar and Withings have no EDA route.
2. **FDA clearance of the platform**, including cleared digital biomarkers. The Empatica Health Monitoring Platform was cleared in November 2022 (K221282: peripheral skin temperature, EDA, SpO2 under no-motion conditions, activity associated with movement during sleep), with later clearances adding pulse rate and respiratory rate (K230457, K242737) and Parkinson's movement measures (K260374); EmbraceMini has its own clearance (K252981). See Privacy, Security, and Compliance. This is a materially different regulatory posture from every consumer platform here.

- Empatica also publishes **actual prices for an academic research plan**, which, after working through Garmin's "contact us", Withings' "contracted partners only", Fitabase's "we'll craft a plan", and Ametris' silence, is a significant practical advantage for grant budgeting.

## Products / Platform Architecture

- **EmbracePlus**, wrist-worn multi-sensor device, the current product.
- **EmbraceMini**, a smaller actigraphy-focused wearable sold alongside EmbracePlus (listed as "New" on Empatica's site), with its own FDA 510(k) K252981 (2025-12-22) for movement and sleep-movement monitoring. Its research-studies table covers 12 of the 17 named biomarkers, with no PPG, EDA or temperature measures. **Verified** (2026-10-10).
- **E4 wristband**, the legacy device. It appears in a very large volume of published EDA and stress research and remains the reference point in that literature. Studies replicating E4-based work should confirm signal comparability with EmbracePlus rather than assuming equivalence.
- **Empatica Cloud**, data storage and processing.
- **Care Portal**, web console for professionals to manage participants across sites and monitor digital biomarkers.
- **Care app** (Enterprise plan) / **Care Lab app** (Academic & Basic Research plan), the participant/operator-facing applications; note the plan-tier split.
- **Empatica Health Monitoring Platform**, the FDA-cleared regulatory entity encompassing device + algorithms + platform.

## Sensors and Data Streams

- Every Module 1 profile uses the same table so devices can be compared row by row. Rows are the sensors named in `CLAUDE.md`. "Present" is about the hardware; "Researcher access" is about what a study can actually obtain, which is the module's central question. "Unclear" means nothing current was verified. The convention is recorded in [`../../shared/profile-table-conventions.md`](../../shared/profile-table-conventions.md).

| Sensor | Present | Researcher access to underlying signal | Resolution or sampling | Notes |
|---|---|---|---|---|
| PPG | Yes, advanced optical | Clinically validated pulse rate and pulse rate variability; raw access per the data-access section | Unclear | Per-sensor rates for EmbracePlus were not published on the pages retrieved. |
| ECG | No | Not applicable | Not applicable |  |
| Accelerometer | Yes | Raw acceleration data | Set by sensor mode: **Actigraphy Pro 64 Hz**, **Actigraphy Optimized 32 Hz** (up to 14 days battery); "Gyroscope 100" mode gives "6-axis motion sensing at 100 Hz" | Sensor modes are "hardware configurations", not free rates. Rates for Standard and Gyroscope Max modes not published. Verified 2026-10-10 (Empatica blog and research-studies page). |
| Gyroscope | Yes, in selected sensor modes | Raw angular velocity ("with the gyroscope enabled in selected sensor modes") | 100 Hz in the Gyroscope 100 mode; otherwise not published | Verified 2026-10-10. |
| Magnetometer | Unclear | Unclear | Unclear |  |
| Temperature | Yes, digital skin temperature | Peripheral skin temperature | Unclear |  |
| SpO2 | Unclear | Unclear | Unclear |  |
| GPS | No | Not applicable | Not applicable |  |
| Barometer / altimeter | Unclear | Unclear | Unclear |  |
| EDA | Yes, ventral EDA | Electrical conductance at the skin surface | Unclear | The differentiating sensor. |
| Ambient light | Unclear | Unclear | Unclear |  |
| Other | Unclear | Unclear | Unclear | Not verified against current documentation. |

**Verification.** Empatica describes "optimized sampling rates" without publishing most of them; a significant documentation gap recorded in the notes below. **Updated 2026-10-10:** the research-studies page now lists five sensor modes (Standard, Actigraphy Pro, Actigraphy Optimized, Gyroscope Max, Gyroscope 100), and the actigraphy rates above are published. Per-mode PPG, EDA and temperature rates are still not on Empatica's pages; the legacy E4 values (BVP 64 Hz, EDA 4 Hz) must not be assumed for EmbracePlus. Empatica says "All Empatica Actigraphy measures are available with both sensor modes for our Enterprise clients", which implies some mode and measure combinations are Enterprise-only (**Reported**).

### Notes from earlier verification passes

| Sensor | Detail |
|---|---|
| **Advanced optical PPG** | Clinically validated pulse rate (PR) and pulse rate variability (PRV) |
| **Ventral EDA sensor** | Measures electrical conductance changes at the skin surface, the differentiating sensor |
| **Accelerometer** | Raw acceleration data |
| **Digital temperature sensor** | Peripheral skin temperature |

- Empatica describes the device as using "optimized sampling rates" to balance data quality against battery efficiency. **Specific per-sensor sampling rates for EmbracePlus were not published on the pages retrieved**, a significant documentation gap given that sampling rate is the whole point of buying a research device. (For reference, the legacy E4 sampled EDA at 4 Hz, PPG/BVP at 64 Hz, ACC at 32 Hz, and temperature at 4 Hz; **do not assume EmbracePlus matches these.**) Obtain the EmbracePlus sampling specification in writing before designing a study.

## Derived Metrics / Analytics

- Empatica supplies validated digital biomarkers computed on its platform. **The count is stated inconsistently across Empatica's own pages**, status: Unclear:
- The research-studies page lists **18 validated biomarkers**: sleep detection, pulse rate, pulse rate variability, respiratory rate, electrodermal activity (SCL), temperature, wearing detection, activity classification, steps, activity counts, actigraphy counts, MET, activity intensity, body position, and accelerometer magnitude standard deviation (among others).
- The store page for the Academic & Basic Research plan states **"over 11 digital biomarkers."**
- Another Empatica page refers to **"over 100 research-grade biomarkers."**

- The most likely reconciliation is that the tiers differ, the Academic & Basic Research plan gives "a standard suite of raw data and digital biomarkers" while the Enterprise plan gives "the complete suite." **Confirm exactly which biomarkers the academic plan includes before purchase**, because the differentiator (EDA-derived measures) may or may not be fully in the standard tier.

- **Re-checked 2026-10-09 (partly resolved).** All three figures above have changed or gone. Read as of today:
  - The research-studies page (now at https://www.empatica.com/platform/research-studies/, the `/en-eu/` path redirects) no longer states a count. It shows a table of **17 named digital biomarkers** with EmbracePlus and EmbraceMini columns: accelerometer magnitude standard deviation, acticounts, actigraphy counts, activity counts, activity classification, activity intensity, ambient light (EmbraceMini only), body position, EDA skin conductance level, METs/calories, pulse rate, pulse rate variability, respiratory rate, sleep detection, steps, skin temperature, and wearing detection. EmbracePlus covers 16 of them; EmbraceMini covers 12 (no PPG, EDA or temperature measures). **Verified.**
  - The Academic plan store page carries the same table and now says "a selection of digital biomarkers"; the "over 11" wording is gone. **Verified.**
  - The "over 100 research-grade biomarkers" line is no longer on the Care page. Empatica's homepage and clinical-trials page now say **"300+ digital measures"**, of which "Six measures carry direct FDA clearance" and the rest are described as research-grade. A November 2023 press release used 128. **Verified** for current wording.
  - Reading: the large figure is the clinical-trial measure library, and the research-studies table is what the self-serve academic product exposes. That reading is **Corroborated**, not stated by Empatica in so many words. Whether an Academic buyer can get any measure outside the 17-row table needs Empatica to confirm.
  - The same pages now list a second device, **EmbraceMini** (actigraphy-focused, FDA 510(k) for sleep, circadian rhythm and physical activity monitoring, 14+ days battery in its optimized mode). It was not profiled in the first pass.

- Notable in that list for methodological reasons: **actigraphy counts** and **activity counts** are provided, meaning EmbracePlus output can be made comparable to the enormous ActiGraph-based physical activity literature, a genuinely useful bridge.

## Active Data Collection

- Not a survey/EMA platform. Empatica is a sensing platform; self-report must come from elsewhere. The device's utility in seizure research does include participant/caregiver event marking, but a general EMA capability is not documented.

## Researcher and Study Management Features

- The Care Portal provides a real study console, one of only two platforms in this module (with Ametris/CentrePoint) that does:

- Create **studies, sites, and unlimited participant credentials**.
- Manage **multiple sessions across participants from one device**, meaning a single device can be recycled across participants, which materially changes the cost model for sequential-cohort designs.
- **Live tracking of participant wearing time** to minimise data loss, active adherence monitoring, not post-hoc discovery.
- Onboard and offboard participants in a few clicks.
- Multi-site management.

## Data Access and Export

| Route | Detail |
|---|---|
| **Raw data download** | **CSV format**, via the Care Portal |
| **Programmatic access** | **Data access keys via Amazon S3**, bulk, scriptable retrieval |
| **Care Portal visualisation** | Biomarkers viewable in the console |
| **Cloud storage** | Data held in Empatica Cloud with historical, timestamped retrieval |
| **Real-time streaming** | **Not available.** Empatica's FAQ: data are "not viewable in real-time. This means you cannot stream data live". Re-verified 2026-10-10. Real-time seizure alerting exists only in the separate EpiMonitor product (K250515), not in the research plan. |

- The absence of real-time streaming rules Empatica out for closed-loop or just-in-time adaptive intervention (JITAI) designs that need to act on physiology within minutes. For retrospective analysis it is irrelevant.

- The S3 access-key route is a good design: it means bulk export is a first-class capability rather than a per-participant portal click, which is where many platforms fall down at scale.

## APIs, SDKs, and Extensibility

- S3-based bulk data access.
- Care Portal.
- A general-purpose REST API for study/participant management was **not established** from the pages retrieved.
- No device SDK; EmbracePlus is not user-programmable. Empatica's FAQ: "We do not provide an SDK for academic research purposes." (**Verified** 2026-10-10.)
- The legacy E4 offered a real-time BLE streaming SDK; **EmbracePlus does not appear to**, which is a capability regression for lab-based real-time work and should be confirmed.

## Deployment and Infrastructure

- Vendor cloud (Empatica Cloud, AWS-based). No self-hosting option. Research team needs only the ability to pull from S3 and store data.

## Participant Experience

- Wrist-worn. Purpose-built for continuous wear including sleep.
- **Battery life and charging cadence were not stated on the pages retrieved**, an important omission for protocol design. Obtain this figure. (An extra charger is sold separately at $42.90, which implies charging is frequent enough that spares matter.)
- Silicone band loops are a separate accessory at $21.90.
- The device is a medical/research device rather than a consumer product, so it offers little participant-facing engagement value, participants wear it because the study asks them to, not because they want to. Expect adherence to depend on study contact rather than device appeal.
- Multi-session device reuse supports staggered enrolment designs.

## Privacy, Security, and Compliance

- **FDA clearances (re-verified 2026-10-10 in openFDA and the 510(k) indications for use).** FDA clearance of a platform is not a blanket endorsement of every output; cite the specific clearance.
  - **K221282** (2022-11-20), Empatica Health Monitoring Platform: for "trained healthcare professionals or researchers" to remotely monitor peripheral skin temperature, electrodermal activity, SpO2 under no-motion conditions, and activity associated with movement during sleep, in ambulatory adults 18 and older in home-healthcare settings.
  - **K230457** (2023-10-30) and **K242737** (2025-06-06), Health Monitoring Platform with EmbracePlus, Empatica Care and Care Portal: add pulse rate and respiratory rate (no-motion). K242737 is for "retrospective remote monitoring" and states "the platform does not provide real-time alerts".
  - **K260374** (2026-08-14), Health Monitoring Platform for Parkinson's Disease Monitoring (EmbracePlus, EmbraceMini, PKG Monitor): kinematics of tremor, bradykinesia and dyskinesia, ages 46 to 83.
  - **K252981** (2025-12-22), EmbraceMini: remote monitoring of limb or body movement and activity associated with movement during sleep.
  - Seizure products: Embrace (K172935, K181861) and EpiMonitor (K232915; **K250515**, 2025-06-19, EmbracePlus plus app, generalized tonic-clonic seizure alerts to a caregiver, ages 6 and up, prescription only).
  - **Verified** (openFDA, https://api.fda.gov/device/510k.json?search=applicant:empatica, and the 510(k) PDFs, 2026-10-10).
- **Security and data governance (read 2026-10-10).** Empatica's legal page lists ISO/IEC 27001:2022 ("performed by independent third-party auditors"), ISO 13485:2016 QMS certification, MDSAP and CE certificates, and a published "Empatica Health Monitoring Platform - Data Processing Agreement". The participant privacy policy says Empatica stores User Data "on HIPAA-compliant cloud infrastructure located in US, Virginia" and retains it during the service "plus a period of 10 years after the termination" of the contract. These are vendor statements; the ISO certificates are linked from the legal page but were not opened (**Corroborated**).
- **Not found:** any SOC 2 statement or published BAA. An academic "vendor documentation pack" is offered behind a form and was not read.

## Pricing

- **Corrected 2026-08-21: Empatica's academic pricing is public, contrary to the first pass.** Read directly from the Empatica store's Academic & Basic Research plan page. **Verified.**

| Item | List | **Academic (25% off)** |
|---|---|---|
| EmbracePlus device (from) | **$1,166.40** | |
| **3-year bundle** (device + charger + 3 yr Empatica Cloud & Care Portal + service and maintenance) | **$2,332.80** | **$1,749.60** |
| **5-year bundle** (as above, 5 yr data access) | **$2,916.00** | **$2,187.00** (25% off plus a further 10% on data access) |
| EmbraceMini device | **$641.52** | |
| EmbraceMini 3-year bundle | **$1,516.32** | **$1,137.24** |
| EmbraceMini 5-year bundle | **$1,953.72** | **$1,465.29** |

- **Re-verified 2026-10-10** (store page, primary). The EmbracePlus figures are unchanged. EmbraceMini rows added (R-217).
- **How the figures fit together.** Each "bundle" list price is the device plus a platform subscription: EmbracePlus $1,166.40 + 3-year subscription $1,166.40 = $2,332.80, and + 5-year subscription $1,749.60 = $2,916.00; EmbraceMini $641.52 + $874.80 = $1,516.32, and + $1,312.20 = $1,953.72. The store page's plan data list 3-year options at $1,166.40 and $874.80 and 5-year options at $1,749.60 and $1,312.20 without naming the device; assigning the lower pair to EmbraceMini is an inference, supported by the sums matching the bundle list prices exactly. The academic price is 25% off the bundle list. Empatica's `llms.txt` lists "5-year Platform Subscription: $1,749.60", which is the 5-year subscription alone at list price; it equals the academic 3-year EmbracePlus bundle price by coincidence, so the two figures do not conflict. Checked 2026-10-10.
- **The academic price is not automatic.** Empatica's academic-discount page says "University students and Academics" are eligible for a discount code, applicants fill in a form, "Only University institutional email addresses will be considered", and the code arrives by email. **Verified** (lp.empatica.com/academic-discount-professional-plan, 2026-10-10).

- Volume discounts apply automatically at **5+ devices**. Taxes and shipping additional.

- *(Superseded 2026-10-09: the store page no longer uses "11+"; see the re-check under Derived Metrics.)* The academic plan includes **"11+ digital biomarkers"** per the store page, note this conflicts with the 18 named on the research-studies page and the "over 100" claimed in platform marketing. Three different public figures. **Unclear** which biomarkers a purchaser actually receives; this is now the most consequential remaining commercial question about Empatica, because it determines whether the academic tier is sufficient for a given protocol.

- **Enterprise plan** pricing remains quote-only. **Unclear.**

### Research program and academic data access (checked 2026-10-10)

- **Program:** the **Academic & Basic Research plan**, sold self-serve on Empatica's store, with a 25% academic discount by application (above). Eligibility: university students and academics with an institutional email. Enterprise (pharma, CRO) is quote-only. **Verified.**
- **What academics get:** the device plus 3 or 5 years of Empatica Cloud data access and Care Lab Portal access, with "Access to all EmbracePlus and EmbraceMini sensor raw data and a selection of digital biomarkers across vital signs, sleep and activity" (store page). Data come by self-serve download and Amazon S3 data access keys; there is no real-time streaming and no SDK for academic research. The academic account is limited to 1 study, 1 site and 1,000 participants (research-studies page, 2026-10-09). **Verified.**
- **How it differs from Enterprise:** per earlier passes, Enterprise uses the Care app rather than Care Lab and gets the complete biomarker suite (support article, source 3, 2026-08-21), and Empatica's clinical-trial pages cite "300+ digital measures" (source 10, 2026-10-09). Empatica's blog adds that all actigraphy measures are available in both actigraphy modes "for our Enterprise clients" (**Reported**, 2026-10-10). Which measures are Enterprise-only is not published. **Unclear.**
- **Retention:** participant data retained during the service plus 10 years after contract end, per the participant privacy policy (**Corroborated**). What a team can still download after its 3- or 5-year access window ends is not stated. **Unclear.**
- **Status:** active (store page and academic-discount form live on 2026-10-10).

### What this means in practice

- At **~$1,750 per device for three years including cloud and support**, an EmbracePlus is roughly 4× an Oura Ring 5 with membership (~$470/yr) and roughly 5× a Garmin Vivosmart. That is expensive per unit, but the platform explicitly supports **running multiple participants sequentially on one device**, so in a study with, say, 2-week wear periods, a single $1,750 device can serve dozens of participants across three years. On a per-participant basis Empatica can be cheaper than a consumer-device study, provided the design is sequential rather than concurrent.

- For concurrent designs it is unambiguously the second-most expensive option here, after Ametris.

## Research Evidence and Validation

- Empatica describes its PR and PRV measurements as clinically validated and its digital biomarkers as validated; the FDA clearances lend these claims more weight than the marketing language of consumer vendors.
- The **E4 predecessor has a very large peer-reviewed footprint**, particularly in EDA/stress, affective computing, epilepsy/seizure detection, and autonomic research. Empatica's origins are in the seizure-detection domain (the Embrace line), which remains its deepest evidence base.
- **Empatica was not included in either the 2024 *Sensors* or 2025 Schyvens PSG sleep-staging comparisons.** Its sleep-detection validity relative to consumer devices is therefore not established by those benchmarks, though its FDA clearance covering "movement during sleep" biomarkers suggests a regulatory validation package exists.
- **EDA validation caveat that applies to the whole modality, not just Empatica:** wrist EDA is noisier and less well-standardised than palmar/finger EDA, is highly sensitive to motion artefact and ambient temperature, and produces substantial unusable data in free-living conditions. Studies should budget for aggressive artefact rejection and should not assume free-living wrist EDA behaves like laboratory EDA. **Quantified 2026-10-09:** against finger/palmar or laboratory references, E4 wrist EDA agrees poorly. Menghini et al. 2019 (*Psychophysiology* 56(11):e13441, N=40): wrist skin conductance "showed neither correlation nor visual resemblance with finger SC signal". Milstein and Gordon 2020 (*Front Behav Neurosci* 14:148, N=30): "The E4 failed to produce reliable EDA data". Hu et al. 2024 (*Behav Res Methods* 56(7), N=67): ICC 0.09 for skin conductance level and 0.38 for response count vs MindWare, with valid EDA about 41 to 43% of the time. No EmbracePlus validation against a palmar reference was located; Brandebusemeyer et al. 2026 (*Sensors* 26(14):4376) compared it only exploratorily with the E4. **Corroborated** (abstracts; Milstein PDF in `../literature/empatica/`).

## Strengths

- **Raw wrist EDA with an FDA-cleared EDA parameter and a self-serve academic plan**, still the most accessible EDA route in this module for stress, arousal, and seizure research (Samsung Galaxy Watch8 now also exposes raw EDA at 1 Hz through its partner-gated SDK; corrected 2026-10-10).
- **FDA-cleared platform** with cleared digital biomarkers, a regulatory posture no consumer platform matches.
- **Raw data access as a standard, documented feature** (CSV + S3 keys), not a gated partnership.
- **Published academic pricing**, genuinely rare and enormously helpful for grant writing.
- Real study-management console with **live wear-time monitoring**.
- **Device reuse across participants** dramatically improves cost efficiency in staggered designs.
- Actigraphy counts provide a bridge to the established physical activity literature.
- Purpose-built for research; no consumer-product compromises.
- Deep evidence base in epilepsy, stress, and affective research via the E4 lineage.

## Limitations

- **No real-time streaming**, rules out JITAI and closed-loop designs.
- **Most sampling rates not published** for EmbracePlus (accelerometer rates per actigraphy mode now are; PPG, EDA and temperature are not), which is a serious documentation gap for a research device.
- Biomarker count stated inconsistently across Empatica's own pages; academic-tier contents unclear.
- Cost per simultaneous participant is an order of magnitude above consumer devices.
- Battery life and charging burden not documented.
- Apparent loss of the E4's real-time BLE streaming SDK.
- No survey/EMA capability.
- No self-hosting; vendor cloud only.
- Not included in the major comparative sleep validations.
- Wrist EDA is intrinsically noisy in free-living conditions.
- Little participant-facing value, so adherence depends entirely on study contact.
- E4-to-EmbracePlus signal comparability is not established, complicating replication of the older literature.

## Best-Fit Use Cases

- **Stress, arousal, emotion, and autonomic research** requiring EDA.
- **Epilepsy and seizure detection/monitoring**, the platform's founding domain.
- Studies needing **raw multimodal physiological signal** (EDA + PPG + ACC + temperature) from a single validated device.
- **Regulated or clinical studies** where an FDA-cleared platform materially eases the regulatory pathway.
- **Staggered-enrolment designs** where devices rotate between participants, the cost model rewards this strongly.
- Multi-site clinical studies needing centralised participant management and wear-time monitoring.
- Studies that need to bridge to the ActiGraph activity-count literature while also capturing autonomic signals.

## Poor-Fit Use Cases

- Large simultaneous cohorts on a consumer-scale budget.
- Real-time or closed-loop intervention designs.
- Studies where participant engagement with the device is part of the intervention.
- Sleep staging as a primary endpoint (unvalidated in the major comparisons).
- Location or GPS-based research.
- Studies needing integrated surveys/EMA without a separate platform.

## Open Questions

- *(Directed to Empatica: https://www.empatica.com/ , support at https://support.empatica.com/)*

- **What are the exact per-sensor sampling rates for EmbracePlus in each sensor mode** (EDA, PPG/BVP, temperature; accelerometer is 64 Hz in Actigraphy Pro, 32 Hz in Actigraphy Optimized and 100 Hz in Gyroscope 100)? Rates are set by mode, not freely configurable.
- **Exactly which raw signals and which biomarkers are included in the Academic & Basic Research plan** versus Enterprise? Is EDA-derived biomarker output in the standard tier?
- ~~Reconcile the "18 biomarkers" / "over 11 biomarkers" / "over 100 research-grade biomarkers" discrepancy.~~ Partly resolved 2026-10-09: the academic pages now show one 17-row table and the clinical-trial pages say "300+ digital measures". Still to confirm with Empatica: can an Academic plan buyer access any measure outside that table?
- **What is EmbracePlus battery life, and what is the charging cadence?**
- Is there a real-time or near-real-time streaming option under any plan? Is the E4's BLE streaming SDK capability available in any form?
- Is there a REST API for study/participant management, or is the Care Portal the only interface?
- ~~Exact scope of each FDA clearance.~~ Resolved 2026-10-10; see Privacy, Security, and Compliance.
- BAA and SOC 2 (ISO 27001:2022, ISO 13485, a published DPA, US-Virginia hosting and 10-year retention are now documented).
- Signal comparability between E4 and EmbracePlus for replication studies.
- Volume/multi-device pricing and whether device-only (no cloud) purchase is possible.
- Data retention after the 3- or 5-year access window expires, what happens to the data?

## Key Links

- Official site: https://www.empatica.com/
- Research studies platform: https://www.empatica.com/en-eu/platform/research-studies/
- Clinical trials platform: https://www.empatica.com/en-eu/platform/clinical-trials/
- Empatica Care: https://www.empatica.com/care/
- **Academic & Basic Research store/pricing:** https://www.empatica.com/store/platform-professional/
- Academic discount application: https://lp.empatica.com/academic-discount-professional-plan
- Legal and certifications: https://www.empatica.com/legal/
- Participant privacy policy: https://www.empatica.com/privacy-participant/
- Plan explanation: https://support.empatica.com/hc/en-us/articles/17721117772317-Understanding-your-Empatica-Health-Monitoring-Platform-Plan
- FDA clearance (platform): https://www.empatica.com/blog/the-empatica-health-monitoring-platform-receives-fda-clearance
- FDA clearance (cardiac digital biomarkers): https://www.empatica.com/blog/empatica-receives-new-fda-clearance-for-cardiac-digital-biomarkers/
- Support: https://support.empatica.com/

## Sources

1. Empatica, Health Monitoring Platform for Research Studies. https://www.empatica.com/en-eu/platform/research-studies/ (accessed 2026-08-21). **Primary.** Establishes the four sensors (optical PPG with clinically validated PR/PRV, ventral EDA, accelerometer, digital temperature), "optimized sampling rates" language, the 18-biomarker list, CSV raw download via Care Portal, cloud storage with historical timestamped retrieval, absence of real-time streaming, and the Care Portal study/site/participant management and live wear-time tracking features.
2. Empatica store, Academic & Basic Research plan. https://www.empatica.com/store/platform-professional/ (accessed 2026-08-21). **Primary.** Establishes the 3-year bundle at $1,749.60 (from $2,332.80), the 5-year bundle at $2,187 (from $2,916), extra charger $42.90, band loops $21.90, package contents, self-serve download, S3 data access keys, and the "over 11 digital biomarkers" figure.
3. Empatica Support, Understanding your Empatica Health Monitoring Platform Plan. https://support.empatica.com/hc/en-us/articles/17721117772317-Understanding-your-Empatica-Health-Monitoring-Platform-Plan (accessed 2026-08-21). Establishes the Care app (Enterprise) vs Care Lab app (Academic & Basic Research) split and the standard-vs-complete biomarker suite distinction.
4. Empatica, "The Empatica Health Monitoring Platform receives FDA clearance." https://www.empatica.com/blog/the-empatica-health-monitoring-platform-receives-fda-clearance (accessed 2026-08-21). Establishes the November 2022 clearance covering EDA, SpO2, skin temperature, and movement-during-sleep digital biomarkers.
5. Empatica, "Empatica Receives New FDA Clearance for Cardiac Digital Biomarkers." https://www.empatica.com/blog/empatica-receives-new-fda-clearance-for-cardiac-digital-biomarkers/ ; PR Newswire, https://www.prnewswire.com/news-releases/empaticas-platform-receives-new-fda-clearance-for-cardiac-digital-biomarkers-301975974.html (accessed 2026-08-21).
6. Empatica Care. https://www.empatica.com/care/ (accessed 2026-08-21). Source of the "over 100 research-grade biomarkers" figure, conflicts with (1) and (2).
8. Empatica, Health Monitoring Platform for Research Studies (current URL). https://www.empatica.com/platform/research-studies/ (accessed 2026-10-09). **Primary.** Supersedes the count in (1): no number stated, a 17-row digital-biomarker table split by EmbracePlus and EmbraceMini, EmbraceMini specification, sensor modes, Academic bundle prices unchanged from (2), 1 study, 1 site and 1,000 participants per Academic account, no SDK for academic research.
9. Empatica store, Academic plan, re-read. https://www.empatica.com/store/platform-professional/ (accessed 2026-10-09). **Primary.** "A selection of digital biomarkers" with the same table; the "over 11" figure in (2) no longer appears.
10. Empatica homepage and clinical-trials page. https://www.empatica.com/ , https://www.empatica.com/platform/clinical-trials/ (accessed 2026-10-09). **Primary, vendor marketing.** "300+ digital measures", six with direct FDA clearance, the rest described as research-grade. Replaces the "over 100" figure attributed to (6), which the Care page no longer shows.
7. Wikipedia, Empatica. https://en.wikipedia.org/wiki/Empatica (accessed 2026-08-21). Background on the E4 lineage and seizure-detection origins; **secondary, low weight**.
11. Empatica store, Academic & Basic Research plan, re-read. https://www.empatica.com/store/platform-professional/ (accessed 2026-10-10). **Primary.** EmbracePlus and EmbraceMini device, subscription and bundle prices; "Access to all EmbracePlus and EmbraceMini sensor raw data".
12. Empatica, Apply for an Academic Discount. https://lp.empatica.com/academic-discount-professional-plan (accessed 2026-10-10). **Primary.** Eligibility and institutional-email application.
13. Empatica, llms.txt. https://www.empatica.com/llms.txt (accessed 2026-10-10). "5-year Platform Subscription: $1,749.60" (subscription only).
14. Empatica, "Empatica Actigraphy" blog post. https://empatica.com/blog/empatica-actigraphy-the-new-standard-to-measure-sleep-and-physical-activity (accessed 2026-10-10). **Primary, vendor.** Actigraphy Pro 64 Hz, Actigraphy Optimized 32 Hz and 14 days battery; Enterprise note.
15. Empatica, Health Monitoring Platform for Research Studies, re-read. https://www.empatica.com/platform/research-studies/ (accessed 2026-10-10). **Primary.** Five sensor modes, gyroscope in selected modes, 100 Hz Gyroscope 100 mode, no real-time streaming, no SDK for academic research.
16. Empatica legal page. https://www.empatica.com/legal/ (accessed 2026-10-10). **Primary, vendor.** ISO/IEC 27001:2022, ISO 13485:2016, MDSAP, CE, Data Processing Agreement.
17. Empatica participant privacy policy. https://www.empatica.com/privacy-participant/ (accessed 2026-10-10). **Primary.** HIPAA-compliant US-Virginia hosting; service period plus 10 years retention.
18. openFDA 510(k) records for Empatica. https://api.fda.gov/device/510k.json?search=applicant:empatica (accessed 2026-10-10), with indications for use read in https://www.accessdata.fda.gov/cdrh_docs/pdf22/K221282.pdf , https://www.accessdata.fda.gov/cdrh_docs/pdf24/K242737.pdf , https://www.accessdata.fda.gov/cdrh_docs/pdf26/K260374.pdf , https://www.accessdata.fda.gov/cdrh_docs/pdf25/K252981.pdf and https://www.accessdata.fda.gov/cdrh_docs/pdf25/K250515.pdf . **Primary.**
19. Samsung Health Sensor SDK, data specifications. https://developer.samsung.com/health/sensor/guide/data-specifications.html (accessed 2026-10-10). **Primary.** `EDA_CONTINUOUS`, raw, 1 Hz, Galaxy Watch8 and later.
