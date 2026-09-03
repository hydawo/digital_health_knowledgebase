# RADAR-base

## Quick Facts

| Field | Details |
|---|---|
| Organization | King's College London and The Hyve (joint maintainers); originated in the IMI RADAR-CNS consortium |
| Category | Open-source, enterprise-grade remote monitoring / digital phenotyping platform |
| Current status | Active, 2026 RADAR-base Symposium held; industry partners (Garmin, Huawei, Empatica, PsychPlus, mySkin) actively integrating |
| Platforms/devices | Android and iOS apps ("RADAR-pRMT"/passive app), plus wearable and IoT device integrations |
| Open source | Yes, Apache 2.0 |
| Hosting/deployment | Self-hosted (institution-run, Kafka-based backend) or cloud-deployed |
| Pricing model | Free/open-source software; infrastructure and hosting/support costs are the researcher's own |
| Last verified | 2026-08-25 (second pass) |

## Summary

- RADAR-base is an open-source remote-monitoring and digital-phenotyping platform built around a streaming (Apache Kafka-based, per its own published architecture papers) backend, designed for scale, extensibility, and multi-modal data, combining phone sensors, wearables, IoT devices, and third-party REST APIs (e.g., Fitbit, Garmin) in one pipeline. It has been used across large clinical cohorts spanning multiple sclerosis, depression, epilepsy, ADHD, Alzheimer's disease, autism, and lung disease research. It is jointly maintained by King's College London and The Hyve, and licensed Apache 2.0.

- Where Beiwe is a lab-scale platform with an optional managed service, RADAR-base presents itself as enterprise/consortium-scale infrastructure, it emerged from and has been used across large EU-funded multi-site clinical consortia (RADAR-CNS and successors), and its architecture reflects that: Kafka-based streaming, IoT gateway support (RADAR-IoT), and explicit support for both in-house institutional hosting and cloud deployment.

## Products / Platform Architecture

- **RADAR-base platform**, the overall open-source stack: mobile apps, backend streaming pipeline, management portal ("Management Portal"), and data pipeline for near-real-time processing and storage.
- **RADAR-IoT**, an open-source, interoperable IoT gateway framework extending the platform to non-phone/non-wearable sensor sources, per a dedicated published architecture paper.
- Wearable and third-party integrations named in vendor/partner materials include Garmin, Huawei, Empatica, and others as active industry partners (2026 Symposium).

## Sensors and Data Streams

- Every Module 2 profile uses the same table so platforms can be compared row by row. Rows are the passive streams named in `CLAUDE.md`. "Yes" and "No" are used only where a primary source says so; "Unclear" means nothing current was verified, and "No (OS)" means the operating system does not expose the stream to any third-party app. Confidence and sources are stated under the table. The convention is recorded in [`../../shared/profile-table-conventions.md`](../../shared/profile-table-conventions.md).

| Stream | Android | iOS | Raw or derived | Sampling configurable | Notes |
|---|---|---|---|---|---|
| GPS / location | Yes | Unclear | Derived. Relative coordinates for privacy. | Unclear | Documented on the Android passive app (pRMT). |
| Accelerometer | Yes | Unclear | Raw, about 200 ms intervals. | Unclear |  |
| Gyroscope | Yes | Unclear | Raw, rad/s. | Unclear |  |
| Magnetometer | Yes | Unclear | Raw, 200 ms intervals. | Unclear |  |
| Barometer | Unclear | Unclear | Unclear | Unclear | Not in the fetched list. |
| Ambient light | Yes | Unclear | Raw, lux on change. | Unclear |  |
| Proximity | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Device motion / activity recognition | Yes | Unclear | Derived. OS activity-recognition events, OS sleep events, step count. | Unclear |  |
| Screen state | Yes | Unclear | Event. Lock, unlock, shutdown. | Unclear |  |
| App usage | Yes | Unclear | Event. Foreground and background with category. | Unclear |  |
| Battery / charging | Unclear | Unclear | Unclear | Unclear | Not in the fetched list. |
| Network / connectivity | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Wi-Fi | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Bluetooth | Yes | Unclear | Derived. Device counts, hourly. | Unclear |  |
| Calls (metadata) | Yes | No (OS) | Metadata, hashed numbers. | Unclear |  |
| SMS (metadata) | Yes | No (OS) | Metadata | Unclear |  |
| Keyboard | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Audio / microphone | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Notifications | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Device information | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |

**Verification.** Android column Verified 2026-08-25 from radar-base.org's Phone Data Sensors page. The same page states that iOS availability is "more sparse" because of background-collection limits and carries a comparison chart the fetch could not extract, so the iOS column is Unclear throughout rather than inferred.

### Notes from earlier verification passes

- **Updated 2026-08-25 (second pass, Verified via direct fetch of `radar-base.org/docs/4048-2/`, "Phone Data Sensors").** The Android passive-app (pRMT) sensor catalog is now itemized and confirmed: relative location (GPS/network, converted to relative coordinates for privacy), 3-axis acceleration (~200ms intervals), 3-axis gyration (rad/s), 3-axis magnetic field (200ms intervals), step count, ambient light (lux, on value change), Bluetooth device counts (hourly), OS-level activity-recognition events (walking, running, cycling, vehicle, etc.), OS-derived sleep events, phone lock/unlock/shutdown ("interaction state"), app foreground/background usage with category, call log (hashed numbers), SMS log (hashed numbers), contact-list count/changes (daily), battery level/charging state, local weather (temperature/pressure/humidity/precipitation, 3-hourly), and app/server connection-status monitoring, 17 documented streams in total. Wearable-sourced physiological signals arrive via separate device integrations (Empatica, Garmin, Fitbit, and others named as 2026 partners).

- **iOS/Android parity, resolved, not assumed (Corroborated).** The same documentation page states explicitly that "substantial differences" exist between the platforms' passive-app builds, and that iOS sensor availability is "more sparse... due to lack of background collection capabilities", the standard iOS background-execution constraint CLAUDE.md flags generically, now confirmed as RADAR-base's own documented position rather than an inferred general platform limitation. The page includes a comparison chart that this fetch could not fully extract; the itemized Android list above should not be assumed to transfer to iOS.

- Active: patient-reported outcome measures (PROMs) and other questionnaire-based active data collection, per the platform's own "About" description.

## Derived Metrics / Analytics

- RADAR-base's own materials describe "feature generation (such as behavioral, environmental, and physiological markers)" as part of the platform's scope, but the specific built-in feature-extraction catalog (comparable to Beiwe's Forest) was **not independently verified** this session. Published clinical papers using RADAR-base (multiple sclerosis, depression, epilepsy, ADHD, Alzheimer's, autism, lung disease) indicate substantial downstream analytics work occurs on RADAR-base-collected data, but whether that analytics logic ships as part of the platform or is built per-study was not established.

## Active Data Collection

- PROM/questionnaire delivery is supported per the platform's own description; scheduling sophistication, branching logic, and EMA-specific features (event-triggered, randomized) were not independently verified this session.

## Researcher and Study Management Features

- **Verified 2026-08-25 (second pass, direct fetch of `github.com/RADAR-base`).** A dedicated `ManagementPortal` repository exists (Kotlin, actively updated, Apache-2.0), confirming the "Management Portal" is a real, currently maintained code artifact rather than only a description in marketing materials. The same organization also maintains `RADAR-Questionnaire` (a TypeScript active/questionnaire mobile app), `radar-prmt-android` (the native Android passive-sensing app), `RADAR-Schemas` (data schema catalog), and Kubernetes/Helm deployment tooling (`RADAR-Kubernetes`, `radar-helm-charts`), indicating a maintained, containerized-deployment-ready reference architecture. Specific participant-management, adherence-monitoring, and audit-logging feature depth within the Management Portal was not independently verified beyond confirming the repository's existence and active status.

## Data Access and Export

- Kafka-based streaming architecture is documented in RADAR-base's own peer-reviewed platform papers (e.g., the original RADAR-base description and RADAR-IoT). This supports near-real-time data flow by design, in contrast to platforms built around periodic batch sync. Self-hosting is explicit and emphasized, particularly for "in-hospital studies" needing enhanced privacy/data-residency control, a meaningfully different governance posture than a SaaS-only competitor. Cloud deployment is also supported for institutions that prefer it, including now via a confirmed managed-hosting route (see Pricing/Deployment below).

## APIs, SDKs, and Extensibility

- Apache 2.0 licence across the stack (per the project's own materials), meaning the full backend, mobile clients, and IoT gateway are open for institutional modification, comparable in openness to Beiwe, but architected for larger multi-site consortium deployments rather than single-lab studies.

## Deployment and Infrastructure

- Self-hosted (institution-run infrastructure) or cloud-deployed, both explicitly supported, per the platform's own "About" page.
- Kafka-based backend implies real operational/DevOps expertise is needed to run a production instance, likely a higher technical floor than Beiwe's already-nontrivial AWS/Django requirement, though this comparison was not independently benchmarked this session.
- Multi-site/multi-institution deployment is a design goal reflected in RADAR-base's consortium origins (RADAR-CNS, an EU IMI-funded multi-country, multi-disease programme).

## Participant Experience

- Not verified in any pass to date.

## Privacy, Security, and Compliance

- Self-hosting is positioned by the platform's own materials as advantageous for privacy control in "in-hospital" contexts, implying institutional data custody rather than a third-party cloud intermediary by default. Specific HIPAA, GDPR/DPA, SOC 2, or ISO certification documentation was **not independently verified** in this session; the platform's EU consortium origin (IMI, an EU/EFPIA public-private programme) suggests GDPR was a design consideration, but this is an inference, not a verified compliance claim, and should not be treated as one.

## Pricing

- Software is free and open source (Apache 2.0). No published licence fee was found.

- **Resolved 2026-08-25 (second pass, resolving unresolved-question #86, Verified via direct fetch of `thehyve.nl/services/radar-base-as-a-service`).** The Hyve, RADAR-base's co-maintainer, offers a named managed-hosting product, **"RADAR-base as a Service,"** distinct from self-hosting. Per the vendor's own service page: platform installation configured to the study's needs; hosting on a GDPR-compliant public cloud of the customer's choosing; support for "unlimited studies and participants" in the general offering description, though the same page separately caveats that the service is best suited to studies of **roughly 200 participants or fewer**, attributed to a single-server infrastructure model; end-user training for passive sensors, surveys, and wearable integrations (Fitbit/Garmin named); ongoing maintenance and technical support; and a stated 2 to 4 week setup timeline. **No pricing figures are published**, this remains a quote-based service, so RADAR-base does not yet match Beiwe's now-resolved rate transparency (see `profiles/beiwe.md`). This is RADAR-base's first confirmed managed-hosting alternative to self-hosting.

## Research Evidence and Validation

- RADAR-base has a substantial published-use record across multiple disease areas, multiple sclerosis, depression, epilepsy, ADHD, Alzheimer's disease, autism, and lung disease, per its own publications page and independently indexed peer-reviewed platform-description papers (e.g., a 2024 JMIR Mental Health paper on RADAR-base for remote monitoring of mental and physical conditions). This is a broader clinical-domain published footprint than most other platforms profiled in this module, consistent with its EU consortium origin funding large multi-site cohort studies.

## Strengths

- Purpose-built for large-scale, multi-site, multi-modal (phone + wearable + IoT) data collection, with a streaming architecture designed for near-real-time throughput rather than batch sync.
- Broad, verifiable published-use record across multiple serious clinical domains.
- Apache 2.0, fully open source, with explicit self-hosting support aimed at institutions needing to keep data on their own infrastructure.
- Active industry-partner ecosystem (Garmin, Huawei, Empatica, and others named at the 2026 Symposium) suggests ongoing wearable-integration investment.
- Jointly maintained by an academic institution (KCL) and a dedicated open-source health-informatics company (The Hyve), which is a different (arguably more sustainable) maintenance model than a single academic lab.
- **New (second pass):** unlike the 2026-08-24 assessment, RADAR-base now has a confirmed managed-hosting route ("RADAR-base as a Service," via The Hyve) for teams without in-house DevOps capacity, plus a maintained, itemized Android passive-sensor catalog and a confirmed, actively-developed Management Portal repository.

## Limitations

- Kafka-based, self-hosted-by-default architecture implies a meaningfully higher DevOps/infrastructure floor than commercial no-code competitors, and likely higher than Beiwe's already-nontrivial AWS requirement, though this was not independently benchmarked head-to-head this session.
- **Updated 2026-08-25**: a managed-hosting option now exists (The Hyve's "RADAR-base as a Service"), but the vendor's own page caveats it to studies of roughly 200 participants or fewer (single-server infrastructure) and does not publish pricing, a real but different limitation than "no option exists at all."
- **Updated 2026-08-25**: iOS/Android sensor parity is now confirmed as *not* present, RADAR-base's own documentation states "substantial differences" exist and describes iOS sensor availability as "more sparse" due to background-execution constraints, consistent with the pattern already Verified for AWARE Framework in this module's earlier second pass. This should not be treated as a minor caveat.
- Compliance documentation (HIPAA/SOC2/ISO) was not located and should not be inferred from EU/consortium origin. The managed-hosting page's own language commits only to "GDPR-compliant public cloud" hosting infrastructure, a hosting-environment claim, not a certification of RADAR-base's own compliance posture.

## Best-Fit Use Cases

- Large, multi-site, multi-country clinical cohort studies combining phone, wearable, and IoT data streams, especially where near-real-time data flow matters.
- Institutions with existing DevOps/data-engineering capacity that want full data custody via self-hosting.
- Studies already using or planning to use wearables from partner vendors (Garmin, Huawei, Empatica) alongside phone sensing.

## Poor-Fit Use Cases

- Small single-site pilots without dedicated infrastructure engineering support, the operational floor appears higher than several commercial or lighter-weight academic alternatives in this module.
- Teams wanting a fully managed, no-infrastructure-to-run SaaS experience out of the box (unless an unverified managed-hosting option exists, see Open Questions).

## Open Questions

- *(Directed to: RADAR-base maintainers, King's College London / The Hyve, via https://radar-base.org)*

- ~~Is there a managed-hosting or paid-support offering comparable to Beiwe's Service Center?~~ **Resolved 2026-08-25**, yes, "RADAR-base as a Service" via The Hyve; pricing still not public.
- What does "RADAR-base as a Service" actually cost, and how does its ~200-participant single-server ceiling get raised for larger studies (multi-server pricing/architecture)?
- ~~What is the exact current sensor/data-stream catalog, and how do iOS and Android differ?~~ **Largely resolved 2026-08-25** for Android (17-item itemized list) and qualitatively for the iOS gap ("substantial differences," iOS "more sparse"); the exact iOS-side itemized list (which of the 17 Android streams iOS lacks or restricts) is still not obtained.
- What compliance certifications (HIPAA, GDPR DPA beyond hosting-infrastructure GDPR-compliance framing, SOC 2, ISO 27001) does the maintained reference deployment or a typical institutional deployment carry?
- What is the realistic infrastructure/DevOps staffing requirement to stand up and operate a **self-hosted** production instance (as distinct from the now-confirmed managed-hosting alternative)?
- What built-in derived-feature/analytics catalog exists natively versus requiring custom per-study development?

## Key Links

- Official site: https://radar-base.org/
- About: https://radar-base.org/about/
- Publications: https://radar-base.org/publications/
- 2026 Symposium announcement: https://radar-base.org/2026/05/28/%F0%9F%9A%80-radar-base-symposium-2026-innovation-impact-the-future-of-mobile-health/

## Sources

1. RADAR-base, "About." https://radar-base.org/about/ (accessed 2026-08-24). **Primary.** Platform purpose, architecture description, hosting models, data sources, KCL/The Hyve maintainership, Apache 2.0 licence.
2. RADAR-base, Publications. https://radar-base.org/publications/ (accessed 2026-08-24). **Primary (listing).** Published-use record across disease domains.
3. RADAR-base 2026 Symposium announcement. https://radar-base.org/2026/05/28/%F0%9F%9A%80-radar-base-symposium-2026-innovation-impact-the-future-of-mobile-health/ (accessed 2026-08-24). **Primary.** 2026 activity confirmation; named industry partners (Garmin, Huawei, Empatica, PsychPlus, mySkin).
4. "Digital Phenotyping of Mental and Physical Conditions: Remote Monitoring of Patients Through RADAR-Base Platform." *JMIR Mental Health* 2024. https://mental.jmir.org/2024/1/e51259 (accessed 2026-08-24, search summary). Peer-reviewed platform-use description across multiple clinical domains.
5. "RADAR-IoT: An Open-Source, Interoperable, and Extensible IoT Gateway Framework for Health Research." PubMed. https://pubmed.ncbi.nlm.nih.gov/39066012/ (accessed 2026-08-24, search summary). Establishes the IoT gateway extension and its open-source status.
6. RADAR-base, "Phone Data Sensors." https://radar-base.org/docs/4048-2/ (accessed 2026-08-25, second pass). **Primary/Verified.** Itemized Android passive-sensor catalog (17 streams); explicit "substantial differences" and "more sparse" iOS-availability language.
7. RADAR-base, "Passive App (pRMT App)." https://radar-base.org/docs/prmt-app/ (accessed 2026-08-25, second pass, Direct fetch, limited detail retrieved). General passive-app description; did not itself yield iOS/Android platform-support detail (see source 6 instead).
8. `github.com/RADAR-base` organization page (second pass). https://github.com/RADAR-base (accessed 2026-08-25). **Primary/Verified.** Confirms `ManagementPortal`, `radar-prmt-android`, `RADAR-Questionnaire`, `RADAR-Schemas`, `RADAR-Kubernetes`, and `radar-helm-charts` repositories, all Apache-2.0, active through August 2026.
9. The Hyve, "RADAR-base as a Service." https://www.thehyve.nl/services/radar-base-as-a-service (accessed 2026-08-25, second pass). **Primary/Verified.** Confirms a named managed-hosting offering: GDPR-compliant cloud hosting, 2 to 4 week setup, ~200-participant single-server guidance, no published pricing. Resolves unresolved-question #86.
