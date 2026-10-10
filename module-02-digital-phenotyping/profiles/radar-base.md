# RADAR-base

## Quick Facts

| Field | Details |
|---|---|
| Organization | King's College London and The Hyve (joint maintainers); originated in the IMI RADAR-CNS consortium |
| Category | Open-source, enterprise-grade remote monitoring / digital phenotyping platform |
| Current status | Active; ManagementPortal pushed 2026-10-05, radar-prmt-android 2026-06-19, RADAR-Kubernetes 2026-10-06 (GitHub API, checked 2026-10-10); 2026 Symposium held. The iOS passive app (radar-prmt-ios) is dormant: last commit 2021-01-19 |
| Platforms/devices | Android passive app "RADAR passive RMT" on Google Play (`org.radarcns.detail`, offered by The Hyve, updated 2026-06-18). Active questionnaire app "RADAR active RMT" on Google Play (`org.phidatalab.radar_armt`, updated 2026-09-09) and the App Store ("RADAR Active RMT", seller Onsentia Limited, v3.3.18, 2026-08-24). No maintained iOS passive app: radar-prmt-ios is "work in progress" that records location only; iOS data come via the aRMT app's HealthKit task. Plus wearable and IoT integrations. Checked 2026-10-10 |
| Open source | Yes, Apache 2.0 |
| Hosting/deployment | Self-hosted (institution-run, Kafka-based backend; RADAR-Kubernetes for cluster installs) or cloud-deployed; managed hosting ("RADAR-base as a Service") from co-maintainer The Hyve, single-server, ideal for up to about 200 participants |
| Pricing model | Free/open-source software (Apache 2.0); self-hosting costs are the researcher's own; The Hyve's managed hosting is a subscription priced by quote only. No academic tier published (Verified 2026-10-10) |
| Last verified | 2026-10-10 (The Hyve service terms, app-store listings, repository activity) |

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
| GPS / location | Yes | Conflicting documentation | Derived. Relative coordinates for privacy. | Unclear | Android pRMT. 2019 iOS chart: significant location changes in background, regular location foreground only. The iOS pRMT repo says it records location but does not send it to a server. |
| Accelerometer | Yes | Conflicting documentation | Raw, about 200 ms intervals. | Unclear | 2019 iOS chart: foreground only. iOS pRMT repo is location-only and dormant. |
| Gyroscope | Yes | Conflicting documentation | Raw, rad/s. | Unclear | 2019 iOS chart: foreground only. |
| Magnetometer | Yes | Conflicting documentation | Raw, 200 ms intervals. | Unclear | 2019 iOS chart: foreground only. |
| Barometer | Unclear | Unclear | Unclear | Unclear | Not in the fetched list. |
| Ambient light | Yes | Conflicting documentation | Raw, lux on change. | Unclear | 2019 iOS chart: foreground only. |
| Proximity | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Device motion / activity recognition | Yes | Yes | Derived. Android: OS activity-recognition events, OS sleep events, step count. iOS: HealthKit steps, distance, flights, exercise time, workouts, sleep analysis. | Unclear | iOS data are read from HealthKit by the aRMT app's `healthkit` task when the participant opens it, not streamed in the background. No iOS activity-recognition events documented. |
| Screen state | Yes | Unclear | Event. Lock, unlock, shutdown. | Unclear |  |
| App usage | Yes | No | Event. Foreground and background with category. | Unclear | 2019 iOS chart: no. |
| Battery / charging | Yes | Conflicting documentation | Unclear | Unclear | Battery level is in the Android list on the Phone Data Sensors page. 2019 iOS chart: foreground only. |
| Network / connectivity | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Wi-Fi | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Bluetooth | Yes | Conflicting documentation | Derived. Device counts, hourly. | Unclear | 2019 iOS chart: scanning foreground only; connecting to known peripherals (wearables) yes. |
| Calls (metadata) | Yes | No (OS) | Metadata, hashed numbers. | Unclear | 2019 chart: Android "for self-published apps only", since Google Play restricts call-log access. |
| SMS (metadata) | Yes | No (OS) | Metadata | Unclear | Same Google Play restriction as calls. |
| Keyboard | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Audio / microphone | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Notifications | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Device information | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |

**Verification.** Android column Verified 2026-08-25 from radar-base.org's Phone Data Sensors page, re-read 2026-10-09 (page updated 2026-05-28; battery level is in its list). iOS column updated 2026-10-09 from the page's "Sensors per phone type" chart, which was read directly as an image. The chart was uploaded in September 2019. It marks acceleration, gyroscope, magnetic field, light, battery, regular location, Bluetooth scanning, timezone, time sync and weather as "foreground only" on iOS. Significant location changes and connection to known peripherals work in the background. Steps are read from HealthKit history in the foreground. App usage and call and SMS logs are not available, and data are sent "when activated only". **The chart conflicts with the iOS app's own repository.** `RADAR-base/radar-prmt-ios`, last committed 2021-01-19, describes the app as "work in progress" that "only records location data without sending it to a server". Rows where the chart describes foreground-only collection are therefore marked Conflicting documentation, not Yes. In current code the working iOS route is the active (aRMT, `RADAR-Questionnaire`) app's HealthKit task. It reads 17 HealthKit types (steps, flights climbed, walking and cycling distance, active and basal energy, heart rate, resting heart rate, SpO2, respiratory rate, sleep analysis, workouts, exercise time, blood glucose, blood pressure, weight) when the participant opens the task. A `radar-sensorkit-cordova` plugin for Apple SensorKit exists (last push 2024-11), but nothing found shows it in use. A new React Native app kit (`radar-base-app`) is under active development. Confidence: chart contents Verified; current iOS phone-sensor capability Unclear; HealthKit route Verified from code.

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

### Background keepalive (added 2026-10-09)

- No participant-facing, server-triggered keepalive like Beiwe's was found. The Android pRMT app runs as an Android foreground service (`startForeground` in `radar-commons-android`), the standard way to stay alive on Android.
- On the server side, `RADAR-Backend`'s `DisconnectMonitor` watches whether each source has stopped sending and **emails researchers** at configured addresses (example timeout 5 minutes). It does not notify the participant. Whether current Kubernetes deployments enable it by default was not checked.
- `RADAR-Appserver` schedules Firebase push notifications and data messages, but its documented use is questionnaire delivery and reminders for the aRMT app, not waking the passive app.
- Status: **Corroborated** from code and READMEs, 2026-10-09.

## Privacy, Security, and Compliance

- Self-hosting is positioned by the platform's own materials as advantageous for privacy control in "in-hospital" contexts, implying institutional data custody rather than a third-party cloud intermediary by default. Specific HIPAA, GDPR/DPA, SOC 2, or ISO certification documentation was **not independently verified** in this session; the platform's EU consortium origin (IMI, an EU/EFPIA public-private programme) suggests GDPR was a design consideration, but this is an inference, not a verified compliance claim, and should not be treated as one.

## Pricing

- Software is free and open source (Apache 2.0). No published licence fee was found.

- **Resolved 2026-08-25 (second pass, resolving unresolved-question #86, Verified via direct fetch of `thehyve.nl/services/radar-base-as-a-service`).** The Hyve, RADAR-base's co-maintainer, offers a named managed-hosting product, **"RADAR-base as a Service,"** distinct from self-hosting. Per the vendor's own service page: platform installation configured to the study's needs; hosting on a GDPR-compliant public cloud of the customer's choosing; support for "unlimited studies and participants" in the general offering description, though the same page separately caveats that the service is best suited to studies of **roughly 200 participants or fewer**, attributed to a single-server infrastructure model; end-user training for passive sensors, surveys, and wearable integrations (Fitbit/Garmin named); ongoing maintenance and technical support; and a stated 2 to 4 week setup timeline. **No pricing figures are published**, this remains a quote-based service, so RADAR-base does not yet match Beiwe's now-resolved rate transparency (see `profiles/beiwe.md`). This is RADAR-base's first confirmed managed-hosting alternative to self-hosting.
- **Re-read 2026-10-10 (Verified):** the page states that "The client organisation will always be the owner of the collected data"; a Data Processing Agreement is drawn up if The Hyve keeps managing the platform after the initial period or gets access to sensitive data; the platform runs on "a single computer based server in contrast to a cluster of computers", so throughput can limit concurrent senders; "Studies with a maximum of 200 participants are ideal for this setup", although the subscription "allows you to use it for any number of studies or participants"; and the service is "best suited for small-scale and short-term studies", with pilots recommended. Hosting is in "a GDPR compliant public cloud infrastructure located at the choice of the client". No price is given; contact via office@thehyve.nl or the inquiry form. Export procedures are not described.
- **How larger deployments scale (Unclear):** the page does not say how the ~200-participant ceiling is raised. The documented open-source route for larger installs is RADAR-Kubernetes (pushed 2026-10-06), whose README says it is used "in few production environments" and is still in its early stages. That this is The Hyve's scale-up path is an inference, not stated.

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
- Teams wanting a fully managed SaaS experience for studies above roughly 200 participants: The Hyve's managed service exists but is pitched at small, short-term studies on a single server.
- Studies that need passive phone sensing on iOS: there is no maintained iOS passive app (radar-prmt-ios last committed 2021-01-19); iOS data come through HealthKit in the aRMT app.

## Open Questions

- *(Directed to: RADAR-base maintainers, King's College London / The Hyve, via https://radar-base.org)*

- ~~Is there a managed-hosting or paid-support offering comparable to Beiwe's Service Center?~~ **Resolved 2026-08-25**, yes, "RADAR-base as a Service" via The Hyve; pricing still not public.
- What does "RADAR-base as a Service" actually cost, and how does its ~200-participant single-server ceiling get raised for larger studies? (Re-checked 2026-10-10: still no price; RADAR-Kubernetes is the documented cluster route, but the page does not say The Hyve offers it.)
- ~~What is the exact current sensor/data-stream catalog, and how do iOS and Android differ?~~ **Largely resolved 2026-08-25** for Android (17-item itemized list) and qualitatively for the iOS gap ("substantial differences," iOS "more sparse"); the exact iOS-side itemized list (which of the 17 Android streams iOS lacks or restricts) is still not obtained. **Partly resolved 2026-10-09**: the 2019 per-stream chart is now in the stream table, but it conflicts with the dormant iOS pRMT repository, and current iOS passive collection appears to run through HealthKit in the aRMT app. Still open: which iOS app a new study would actually deploy for phone sensors. Re-checked 2026-10-10: radar-prmt-ios unchanged (last commit 2021-01-19, last push 2023-06-20, not archived) and still the only iOS pRMT repository in the organization.
- What compliance certifications (HIPAA, GDPR DPA beyond hosting-infrastructure GDPR-compliance framing, SOC 2, ISO 27001) does the maintained reference deployment or a typical institutional deployment carry?
- What is the realistic infrastructure/DevOps staffing requirement to stand up and operate a **self-hosted** production instance (as distinct from the now-confirmed managed-hosting alternative)?
- What built-in derived-feature/analytics catalog exists natively versus requiring custom per-study development?

## Key Links

- Official site: https://radar-base.org/
- The Hyve, RADAR-base as a Service: https://www.thehyve.nl/services/radar-base-as-a-service
- RADAR passive RMT (Google Play): https://play.google.com/store/apps/details?id=org.radarcns.detail
- RADAR active RMT (Google Play): https://play.google.com/store/apps/details?id=org.phidatalab.radar_armt ; App Store: https://apps.apple.com/us/app/radar-active-rmt/id1483953055
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
10. RADAR-base, "Sensors per phone type" chart on the Phone Data Sensors page. https://radar-base.org/wp-content/uploads/2019/09/iOS_pRMT_App_Android_Sensor_Comparison.png (read 2026-10-09). **Primary/Direct.** Per-stream iOS vs Android availability as of 2019.
11. `RADAR-base/radar-prmt-ios` README and commits via the GitHub API. https://github.com/RADAR-base/radar-prmt-ios (accessed 2026-10-09). **Primary/Direct.** "Work in progress", location only, not sent to server; last commit 2021-01-19.
12. `RADAR-base/RADAR-Questionnaire` `package.json`, README and `src/app/shared/models/health.ts`. https://github.com/RADAR-base/RADAR-Questionnaire (accessed 2026-10-09). **Primary/Direct.** HealthKit task and supported types; Firebase messaging.
13. `RADAR-base/RADAR-Appserver` README and `RADAR-base/RADAR-Backend` README and `DisconnectMonitor.java`. https://github.com/RADAR-base/RADAR-Appserver ; https://github.com/RADAR-base/RADAR-Backend (accessed 2026-10-09). **Primary/Direct.** Push scheduling for questionnaires; researcher email on source disconnect.
14. RADAR-base GitHub repository listing, iOS-related repos (`radar-sensorkit-cordova`, `radar-base-app`) (accessed 2026-10-09). **Direct.**
15. The Hyve, "RADAR-base as a Service," re-read. https://www.thehyve.nl/services/radar-base-as-a-service (accessed 2026-10-10). **Primary/Verified.** Data ownership, DPA conditions, single-server model, ~200 participants ideal, small-scale and short-term fit, subscription, no price.
16. Google Play (`org.radarcns.detail`, `org.phidatalab.radar_armt`) and App Store (id 1483953055) listings, direct fetch 2026-10-10. **Primary/Verified.**
17. GitHub API for ManagementPortal, radar-prmt-android, radar-prmt-ios and RADAR-Kubernetes, plus the RADAR-Kubernetes README (accessed 2026-10-10). **Primary/Verified.**
