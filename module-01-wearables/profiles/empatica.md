# Empatica

## Quick Facts

| Field | Details |
|---|---|
| Organization | Empatica Inc. (US/Italy) |
| Category | Research- and clinical-grade wearable with an FDA-cleared health monitoring platform |
| Current status | Active |
| Platforms/devices | **EmbracePlus** (current); **E4 wristband** (legacy predecessor, still widely cited in the literature) |
| Open source | No |
| Hosting/deployment | Empatica Cloud; Care Portal web console; AWS S3 data access keys |
| Pricing model | **Published, transparent bundle pricing for academic research** — unusual in this module |
| Last verified | 2026-08-21 |

## Summary

Empatica is the platform to reach for when the research question requires **raw physiological signal from a regulated, purpose-built device** rather than a consumer product with an API bolted on. Two things distinguish it:

1. **EDA (electrodermal activity).** Empatica is the only device in this module with a wrist-worn EDA sensor. For stress, arousal, emotion, seizure, and autonomic research, this is not a nice-to-have — it is the reason the device exists, and there is no substitute among Apple, Fitbit, Garmin, Oura, WHOOP, Samsung, Polar, or Withings.
2. **FDA clearance of the platform**, including cleared digital biomarkers. The Empatica Health Monitoring Platform received FDA clearance in November 2022 covering clinically validated digital biomarkers for electrodermal activity, SpO2, skin temperature, and movement during sleep, and a further clearance for cardiac digital biomarkers was announced subsequently. This is a materially different regulatory posture from every consumer platform here.

Empatica also publishes **actual prices for an academic research plan**, which — after working through Garmin's "contact us", Withings' "contracted partners only", Fitabase's "we'll craft a plan", and Ametris' silence — is a significant practical advantage for grant budgeting.

## Products / Platform Architecture

- **EmbracePlus** — wrist-worn multi-sensor device, the current product.
- **E4 wristband** — the legacy device. It appears in a very large volume of published EDA and stress research and remains the reference point in that literature. Studies replicating E4-based work should confirm signal comparability with EmbracePlus rather than assuming equivalence.
- **Empatica Cloud** — data storage and processing.
- **Care Portal** — web console for professionals to manage participants across sites and monitor digital biomarkers.
- **Care app** (Enterprise plan) / **Care Lab app** (Academic & Basic Research plan) — the participant/operator-facing applications; note the plan-tier split.
- **Empatica Health Monitoring Platform** — the FDA-cleared regulatory entity encompassing device + algorithms + platform.

## Sensors and Data Streams

| Sensor | Detail |
|---|---|
| **Advanced optical PPG** | Clinically validated pulse rate (PR) and pulse rate variability (PRV) |
| **Ventral EDA sensor** | Measures electrical conductance changes at the skin surface — the differentiating sensor |
| **Accelerometer** | Raw acceleration data |
| **Digital temperature sensor** | Peripheral skin temperature |

Empatica describes the device as using "optimized sampling rates" to balance data quality against battery efficiency. **Specific per-sensor sampling rates for EmbracePlus were not published on the pages retrieved** — a significant documentation gap given that sampling rate is the whole point of buying a research device. (For reference, the legacy E4 sampled EDA at 4 Hz, PPG/BVP at 64 Hz, ACC at 32 Hz, and temperature at 4 Hz; **do not assume EmbracePlus matches these.**) Obtain the EmbracePlus sampling specification in writing before designing a study.

## Derived Metrics / Analytics

Empatica supplies validated digital biomarkers computed on its platform. **The count is stated inconsistently across Empatica's own pages** — status: Unclear:
- The research-studies page lists **18 validated biomarkers**: sleep detection, pulse rate, pulse rate variability, respiratory rate, electrodermal activity (SCL), temperature, wearing detection, activity classification, steps, activity counts, actigraphy counts, MET, activity intensity, body position, and accelerometer magnitude standard deviation (among others).
- The store page for the Academic & Basic Research plan states **"over 11 digital biomarkers."**
- Another Empatica page refers to **"over 100 research-grade biomarkers."**

The most likely reconciliation is that the tiers differ — the Academic & Basic Research plan gives "a standard suite of raw data and digital biomarkers" while the Enterprise plan gives "the complete suite." **Confirm exactly which biomarkers the academic plan includes before purchase**, because the differentiator (EDA-derived measures) may or may not be fully in the standard tier.

Notable in that list for methodological reasons: **actigraphy counts** and **activity counts** are provided, meaning EmbracePlus output can be made comparable to the enormous ActiGraph-based physical activity literature — a genuinely useful bridge.

## Active Data Collection

Not a survey/EMA platform. Empatica is a sensing platform; self-report must come from elsewhere. The device's utility in seizure research does include participant/caregiver event marking, but a general EMA capability is not documented.

## Researcher and Study Management Features

The Care Portal provides a real study console — one of only two platforms in this module (with Ametris/CentrePoint) that does:

- Create **studies, sites, and unlimited participant credentials**.
- Manage **multiple sessions across participants from one device** — meaning a single device can be recycled across participants, which materially changes the cost model for sequential-cohort designs.
- **Live tracking of participant wearing time** to minimise data loss — active adherence monitoring, not post-hoc discovery.
- Onboard and offboard participants in a few clicks.
- Multi-site management.

## Data Access and Export

| Route | Detail |
|---|---|
| **Raw data download** | **CSV format**, via the Care Portal |
| **Programmatic access** | **Data access keys via Amazon S3** — bulk, scriptable retrieval |
| **Care Portal visualisation** | Biomarkers viewable in the console |
| **Cloud storage** | Data held in Empatica Cloud with historical, timestamped retrieval |
| **Real-time streaming** | **Not available.** Data is historical; live streaming is explicitly not offered. |

The absence of real-time streaming rules Empatica out for closed-loop or just-in-time adaptive intervention (JITAI) designs that need to act on physiology within minutes. For retrospective analysis it is irrelevant.

The S3 access-key route is a good design: it means bulk export is a first-class capability rather than a per-participant portal click, which is where many platforms fall down at scale.

## APIs, SDKs, and Extensibility

- S3-based bulk data access.
- Care Portal.
- A general-purpose REST API for study/participant management was **not established** from the pages retrieved.
- No device SDK; EmbracePlus is not user-programmable.
- The legacy E4 offered a real-time BLE streaming SDK; **EmbracePlus does not appear to**, which is a capability regression for lab-based real-time work and should be confirmed.

## Deployment and Infrastructure

Vendor cloud (Empatica Cloud, AWS-based). No self-hosting option. Research team needs only the ability to pull from S3 and store data.

## Participant Experience

- Wrist-worn. Purpose-built for continuous wear including sleep.
- **Battery life and charging cadence were not stated on the pages retrieved** — an important omission for protocol design. Obtain this figure. (An extra charger is sold separately at $42.90, which implies charging is frequent enough that spares matter.)
- Silicone band loops are a separate accessory at $21.90.
- The device is a medical/research device rather than a consumer product, so it offers little participant-facing engagement value — participants wear it because the study asks them to, not because they want to. Expect adherence to depend on study contact rather than device appeal.
- Multi-session device reuse supports staggered enrolment designs.

## Privacy, Security, and Compliance

- **FDA clearance** of the Empatica Health Monitoring Platform (initial clearance November 2022; additional clearance for cardiac digital biomarkers announced subsequently). This is the strongest regulatory position of any platform in this module.
- **The precise scope of each clearance — which biomarkers, for what intended use, in what population — was not verified in this session.** FDA clearance of a platform is not a blanket endorsement of every output. Obtain and read the actual 510(k) summaries before making any regulatory claim in a protocol or publication.
- HIPAA/BAA availability, SOC 2, ISO 13485/27001, GDPR DPA terms, and data residency were **not verified**. Given the clinical-trials positioning, these very likely exist — but confirm in writing.

## Pricing

**Corrected 2026-08-21: Empatica's academic pricing is public, contrary to the first pass.** Read
directly from the Empatica store's Academic & Basic Research plan page. **Verified.**

| Item | List | **Academic (25% off)** |
|---|---|---|
| EmbracePlus device (from) | **$1,166.40** | — |
| **3-year bundle** (device + charger + 3 yr Empatica Cloud & Care Portal + service and maintenance) | **$2,332.80** | **$1,749.60** |
| **5-year bundle** (as above, 5 yr data access) | **$2,916.00** | **$2,187.00** (25% off plus a further 10% on data access) |

Volume discounts apply automatically at **5+ devices**. Taxes and shipping additional.

The academic plan includes **"11+ digital biomarkers"** per the store page — note this conflicts
with the 18 named on the research-studies page and the "over 100" claimed in platform marketing.
Three different public figures. **Unclear** which biomarkers a purchaser actually receives; this is
now the most consequential remaining commercial question about Empatica, because it determines
whether the academic tier is sufficient for a given protocol.

**Enterprise plan** pricing remains quote-only. **Unclear.**

### What this means in practice

At **~$1,750 per device for three years including cloud and support**, an EmbracePlus is roughly
4× an Oura Ring 5 with membership (~$470/yr) and roughly 5× a Garmin Vivosmart. That is expensive
per unit — but the platform explicitly supports **running multiple participants sequentially on one
device**, so in a study with, say, 2-week wear periods, a single $1,750 device can serve dozens of
participants across three years. On a per-participant basis Empatica can be cheaper than a
consumer-device study, provided the design is sequential rather than concurrent.

For concurrent designs it is unambiguously the second-most expensive option here, after Ametris.

## Research Evidence and Validation

- Empatica describes its PR and PRV measurements as clinically validated and its digital biomarkers as validated; the FDA clearances lend these claims more weight than the marketing language of consumer vendors.
- The **E4 predecessor has a very large peer-reviewed footprint**, particularly in EDA/stress, affective computing, epilepsy/seizure detection, and autonomic research. Empatica's origins are in the seizure-detection domain (the Embrace line), which remains its deepest evidence base.
- **Empatica was not included in either the 2024 *Sensors* or 2025 Schyvens PSG sleep-staging comparisons.** Its sleep-detection validity relative to consumer devices is therefore not established by those benchmarks — though its FDA clearance covering "movement during sleep" biomarkers suggests a regulatory validation package exists.
- **EDA validation caveat that applies to the whole modality, not just Empatica:** wrist EDA is noisier and less well-standardised than palmar/finger EDA, is highly sensitive to motion artefact and ambient temperature, and produces substantial unusable data in free-living conditions. Studies should budget for aggressive artefact rejection and should not assume free-living wrist EDA behaves like laboratory EDA.

## Strengths

- **The only wrist EDA sensor in this module** — irreplaceable for stress, arousal, and seizure research.
- **FDA-cleared platform** with cleared digital biomarkers — a regulatory posture no consumer platform matches.
- **Raw data access as a standard, documented feature** (CSV + S3 keys), not a gated partnership.
- **Published academic pricing** — genuinely rare and enormously helpful for grant writing.
- Real study-management console with **live wear-time monitoring**.
- **Device reuse across participants** dramatically improves cost efficiency in staggered designs.
- Actigraphy counts provide a bridge to the established physical activity literature.
- Purpose-built for research; no consumer-product compromises.
- Deep evidence base in epilepsy, stress, and affective research via the E4 lineage.

## Limitations

- **No real-time streaming** — rules out JITAI and closed-loop designs.
- **Sampling rates not published** for EmbracePlus, which is a serious documentation gap for a research device.
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
- **Epilepsy and seizure detection/monitoring** — the platform's founding domain.
- Studies needing **raw multimodal physiological signal** (EDA + PPG + ACC + temperature) from a single validated device.
- **Regulated or clinical studies** where an FDA-cleared platform materially eases the regulatory pathway.
- **Staggered-enrolment designs** where devices rotate between participants — the cost model rewards this strongly.
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

*(Directed to Empatica: https://www.empatica.com/ , support at https://support.empatica.com/)*

- **What are the exact per-sensor sampling rates for EmbracePlus** (EDA, PPG/BVP, ACC, temperature)? Are they configurable?
- **Exactly which raw signals and which biomarkers are included in the Academic & Basic Research plan** versus Enterprise? Is EDA-derived biomarker output in the standard tier?
- Reconcile the "18 biomarkers" / "over 11 biomarkers" / "over 100 research-grade biomarkers" discrepancy.
- **What is EmbracePlus battery life, and what is the charging cadence?**
- Is there a real-time or near-real-time streaming option under any plan? Is the E4's BLE streaming SDK capability available in any form?
- Is there a REST API for study/participant management, or is the Care Portal the only interface?
- **Exact scope of each FDA clearance** — 510(k) numbers, cleared biomarkers, intended use, and cleared populations.
- HIPAA/BAA, SOC 2, ISO 13485/27001, GDPR DPA, data residency, and retention/deletion terms.
- Signal comparability between E4 and EmbracePlus for replication studies.
- Volume/multi-device pricing and whether device-only (no cloud) purchase is possible.
- Data retention after the 3- or 5-year access window expires — what happens to the data?

## Key Links

- Official site: https://www.empatica.com/
- Research studies platform: https://www.empatica.com/en-eu/platform/research-studies/
- Clinical trials platform: https://www.empatica.com/en-eu/platform/clinical-trials/
- Empatica Care: https://www.empatica.com/care/
- **Academic & Basic Research store/pricing:** https://www.empatica.com/store/platform-professional/
- Plan explanation: https://support.empatica.com/hc/en-us/articles/17721117772317-Understanding-your-Empatica-Health-Monitoring-Platform-Plan
- FDA clearance (platform): https://www.empatica.com/blog/the-empatica-health-monitoring-platform-receives-fda-clearance
- FDA clearance (cardiac digital biomarkers): https://www.empatica.com/blog/empatica-receives-new-fda-clearance-for-cardiac-digital-biomarkers/
- Support: https://support.empatica.com/

## Sources

1. Empatica — Health Monitoring Platform for Research Studies. https://www.empatica.com/en-eu/platform/research-studies/ (accessed 2026-08-21). **Primary.** Establishes the four sensors (optical PPG with clinically validated PR/PRV, ventral EDA, accelerometer, digital temperature), "optimized sampling rates" language, the 18-biomarker list, CSV raw download via Care Portal, cloud storage with historical timestamped retrieval, absence of real-time streaming, and the Care Portal study/site/participant management and live wear-time tracking features.
2. Empatica store — Academic & Basic Research plan. https://www.empatica.com/store/platform-professional/ (accessed 2026-08-21). **Primary.** Establishes the 3-year bundle at $1,749.60 (from $2,332.80), the 5-year bundle at $2,187 (from $2,916), extra charger $42.90, band loops $21.90, package contents, self-serve download, S3 data access keys, and the "over 11 digital biomarkers" figure.
3. Empatica Support — Understanding your Empatica Health Monitoring Platform Plan. https://support.empatica.com/hc/en-us/articles/17721117772317-Understanding-your-Empatica-Health-Monitoring-Platform-Plan (accessed 2026-08-21). Establishes the Care app (Enterprise) vs Care Lab app (Academic & Basic Research) split and the standard-vs-complete biomarker suite distinction.
4. Empatica — "The Empatica Health Monitoring Platform receives FDA clearance." https://www.empatica.com/blog/the-empatica-health-monitoring-platform-receives-fda-clearance (accessed 2026-08-21). Establishes the November 2022 clearance covering EDA, SpO2, skin temperature, and movement-during-sleep digital biomarkers.
5. Empatica — "Empatica Receives New FDA Clearance for Cardiac Digital Biomarkers." https://www.empatica.com/blog/empatica-receives-new-fda-clearance-for-cardiac-digital-biomarkers/ ; PR Newswire, https://www.prnewswire.com/news-releases/empaticas-platform-receives-new-fda-clearance-for-cardiac-digital-biomarkers-301975974.html (accessed 2026-08-21).
6. Empatica Care. https://www.empatica.com/care/ (accessed 2026-08-21). Source of the "over 100 research-grade biomarkers" figure — conflicts with (1) and (2).
7. Wikipedia — Empatica. https://en.wikipedia.org/wiki/Empatica (accessed 2026-08-21). Background on the E4 lineage and seizure-detection origins; **secondary, low weight**.
