# RADAR-base

## Quick Facts

| Field | Details |
|---|---|
| Organization | King's College London and The Hyve (joint maintainers); originated in the IMI RADAR-CNS consortium |
| Category | Open-source, enterprise-grade remote monitoring / digital phenotyping platform |
| Current status | Active — 2026 RADAR-base Symposium held; industry partners (Garmin, Huawei, Empatica, PsychPlus, mySkin) actively integrating |
| Platforms/devices | Android and iOS apps ("RADAR-pRMT"/passive app), plus wearable and IoT device integrations |
| Open source | Yes — Apache 2.0 |
| Hosting/deployment | Self-hosted (institution-run, Kafka-based backend) or cloud-deployed |
| Pricing model | Free/open-source software; infrastructure and hosting/support costs are the researcher's own |
| Last verified | 2026-08-24 |

## Summary

RADAR-base is an open-source remote-monitoring and digital-phenotyping platform built around a streaming (Apache Kafka-based, per its own published architecture papers) backend, designed for scale, extensibility, and multi-modal data — combining phone sensors, wearables, IoT devices, and third-party REST APIs (e.g., Fitbit, Garmin) in one pipeline. It has been used across large clinical cohorts spanning multiple sclerosis, depression, epilepsy, ADHD, Alzheimer's disease, autism, and lung disease research. It is jointly maintained by King's College London and The Hyve, and licensed Apache 2.0.

Where Beiwe is a lab-scale platform with an optional managed service, RADAR-base presents itself as enterprise/consortium-scale infrastructure — it emerged from and has been used across large EU-funded multi-site clinical consortia (RADAR-CNS and successors), and its architecture reflects that: Kafka-based streaming, IoT gateway support (RADAR-IoT), and explicit support for both in-house institutional hosting and cloud deployment.

## Products / Platform Architecture

- **RADAR-base platform** — the overall open-source stack: mobile apps, backend streaming pipeline, management portal ("Management Portal"), and data pipeline for near-real-time processing and storage.
- **RADAR-IoT** — an open-source, interoperable IoT gateway framework extending the platform to non-phone/non-wearable sensor sources, per a dedicated published architecture paper.
- Wearable and third-party integrations named in vendor/partner materials include Garmin, Huawei, Empatica, and others as active industry partners (2026 Symposium).

## Sensors and Data Streams

Passive: accelerometer, GPS/location, audio (referenced in the platform's own description), plus wearable-sourced physiological signals via device integrations (e.g., Empatica, Garmin, Fitbit). Exact per-sensor sampling configurability, iOS-vs-Android parity, and background-collection constraints were **not independently verified against current developer documentation** this session — flagged as an open question, consistent with CLAUDE.md's explicit instruction not to assume iOS/Android parity.

Active: patient-reported outcome measures (PROMs) and other questionnaire-based active data collection, per the platform's own "About" description.

## Derived Metrics / Analytics

RADAR-base's own materials describe "feature generation (such as behavioral, environmental, and physiological markers)" as part of the platform's scope, but the specific built-in feature-extraction catalog (comparable to Beiwe's Forest) was **not independently verified** this session. Published clinical papers using RADAR-base (multiple sclerosis, depression, epilepsy, ADHD, Alzheimer's, autism, lung disease) indicate substantial downstream analytics work occurs on RADAR-base-collected data, but whether that analytics logic ships as part of the platform or is built per-study was not established.

## Active Data Collection

PROM/questionnaire delivery is supported per the platform's own description; scheduling sophistication, branching logic, and EMA-specific features (event-triggered, randomized) were not independently verified this session.

## Researcher/Admin Functionality

A "Management Portal" is referenced as part of the platform architecture in RADAR-base's own materials and prior peer-reviewed platform-description papers, implying study creation, participant management, and monitoring functionality — not independently re-verified against current documentation in this session.

## Data Architecture and Access

Kafka-based streaming architecture is documented in RADAR-base's own peer-reviewed platform papers (e.g., the original RADAR-base description and RADAR-IoT). This supports near-real-time data flow by design, in contrast to platforms built around periodic batch sync. Self-hosting is explicit and emphasized, particularly for "in-hospital studies" needing enhanced privacy/data-residency control — a meaningfully different governance posture than a SaaS-only competitor. Cloud deployment is also supported for institutions that prefer it.

## Extensibility and Technical Architecture

Apache 2.0 licence across the stack (per the project's own materials), meaning the full backend, mobile clients, and IoT gateway are open for institutional modification — comparable in openness to Beiwe, but architected for larger multi-site consortium deployments rather than single-lab studies.

## Deployment and Infrastructure

- Self-hosted (institution-run infrastructure) or cloud-deployed — both explicitly supported, per the platform's own "About" page.
- Kafka-based backend implies real operational/DevOps expertise is needed to run a production instance — likely a higher technical floor than Beiwe's already-nontrivial AWS/Django requirement, though this comparison was not independently benchmarked this session.
- Multi-site/multi-institution deployment is a design goal reflected in RADAR-base's consortium origins (RADAR-CNS, an EU IMI-funded multi-country, multi-disease programme).

## Privacy, Security, and Compliance

Self-hosting is positioned by the platform's own materials as advantageous for privacy control in "in-hospital" contexts, implying institutional data custody rather than a third-party cloud intermediary by default. Specific HIPAA, GDPR/DPA, SOC 2, or ISO certification documentation was **not independently verified** in this session; the platform's EU consortium origin (IMI, an EU/EFPIA public-private programme) suggests GDPR was a design consideration, but this is an inference, not a verified compliance claim, and should not be treated as one.

## Pricing

Software is free and open source (Apache 2.0). No published licence fee was found. As with any self-hosted, Kafka-based platform, the real cost is institutional infrastructure, DevOps/data-engineering staff time, and any paid support arrangement with maintainers (King's College London / The Hyve) — none of which is publicly priced. **Whether The Hyve or another entity offers a paid managed-hosting option comparable to Beiwe's Service Center was not established this session** — flagged as an open question.

## Research Evidence and Validation

RADAR-base has a substantial published-use record across multiple disease areas — multiple sclerosis, depression, epilepsy, ADHD, Alzheimer's disease, autism, and lung disease — per its own publications page and independently indexed peer-reviewed platform-description papers (e.g., a 2024 JMIR Mental Health paper on RADAR-base for remote monitoring of mental and physical conditions). This is a broader clinical-domain published footprint than most other platforms profiled in this module, consistent with its EU consortium origin funding large multi-site cohort studies.

## Strengths

- Purpose-built for large-scale, multi-site, multi-modal (phone + wearable + IoT) data collection, with a streaming architecture designed for near-real-time throughput rather than batch sync.
- Broad, verifiable published-use record across multiple serious clinical domains.
- Apache 2.0, fully open source, with explicit self-hosting support aimed at institutions needing to keep data on their own infrastructure.
- Active industry-partner ecosystem (Garmin, Huawei, Empatica, and others named at the 2026 Symposium) suggests ongoing wearable-integration investment.
- Jointly maintained by an academic institution (KCL) and a dedicated open-source health-informatics company (The Hyve), which is a different (arguably more sustainable) maintenance model than a single academic lab.

## Limitations

- Kafka-based, self-hosted-by-default architecture implies a meaningfully higher DevOps/infrastructure floor than commercial no-code competitors, and likely higher than Beiwe's already-nontrivial AWS requirement — though this was not independently benchmarked head-to-head this session.
- No managed-hosting-as-a-service option comparable to the Beiwe Service Center was identified — unverified as either present or absent.
- Sensor-level detail (exact passive streams, iOS/Android parity, sampling configurability) was not independently verified against current developer documentation this session — a real gap given how decisive iOS/Android asymmetry has proven in comparable platforms.
- Compliance documentation (HIPAA/GDPR/SOC2/ISO) was not located and should not be inferred from EU/consortium origin.

## Best-Fit Use Cases

- Large, multi-site, multi-country clinical cohort studies combining phone, wearable, and IoT data streams, especially where near-real-time data flow matters.
- Institutions with existing DevOps/data-engineering capacity that want full data custody via self-hosting.
- Studies already using or planning to use wearables from partner vendors (Garmin, Huawei, Empatica) alongside phone sensing.

## Poor-Fit Use Cases

- Small single-site pilots without dedicated infrastructure engineering support — the operational floor appears higher than several commercial or lighter-weight academic alternatives in this module.
- Teams wanting a fully managed, no-infrastructure-to-run SaaS experience out of the box (unless an unverified managed-hosting option exists — see Open Questions).

## Open Questions

*(Directed to: RADAR-base maintainers — King's College London / The Hyve — via https://radar-base.org)*

- Is there a managed-hosting or paid-support offering comparable to Beiwe's Service Center, and if so, what does it cost?
- What is the exact current sensor/data-stream catalog, and how do iOS and Android differ in what they can collect?
- What compliance certifications (HIPAA, GDPR DPA, SOC 2, ISO 27001) does the maintained reference deployment or a typical institutional deployment carry?
- What is the realistic infrastructure/DevOps staffing requirement to stand up and operate a production instance?
- What built-in derived-feature/analytics catalog exists natively versus requiring custom per-study development?

## Key Links

- Official site: https://radar-base.org/
- About: https://radar-base.org/about/
- Publications: https://radar-base.org/publications/
- 2026 Symposium announcement: https://radar-base.org/2026/05/28/%F0%9F%9A%80-radar-base-symposium-2026-innovation-impact-the-future-of-mobile-health/

## Sources

1. RADAR-base — "About." https://radar-base.org/about/ (accessed 2026-08-24). **Primary.** Platform purpose, architecture description, hosting models, data sources, KCL/The Hyve maintainership, Apache 2.0 licence.
2. RADAR-base — Publications. https://radar-base.org/publications/ (accessed 2026-08-24). **Primary (listing).** Published-use record across disease domains.
3. RADAR-base 2026 Symposium announcement. https://radar-base.org/2026/05/28/%F0%9F%9A%80-radar-base-symposium-2026-innovation-impact-the-future-of-mobile-health/ (accessed 2026-08-24). **Primary.** 2026 activity confirmation; named industry partners (Garmin, Huawei, Empatica, PsychPlus, mySkin).
4. "Digital Phenotyping of Mental and Physical Conditions: Remote Monitoring of Patients Through RADAR-Base Platform." *JMIR Mental Health* 2024. https://mental.jmir.org/2024/1/e51259 (accessed 2026-08-24, search summary). Peer-reviewed platform-use description across multiple clinical domains.
5. "RADAR-IoT: An Open-Source, Interoperable, and Extensible IoT Gateway Framework for Health Research." PubMed. https://pubmed.ncbi.nlm.nih.gov/39066012/ (accessed 2026-08-24, search summary). Establishes the IoT gateway extension and its open-source status.
