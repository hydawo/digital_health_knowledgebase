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
| Last verified | 2026-10-11 (vendor fact record) |

## Summary

- RADAR-base is an open-source remote-monitoring and digital-phenotyping platform built around a streaming (Apache Kafka-based, per its own published architecture papers) backend, designed for scale, extensibility, and multi-modal data, combining phone sensors, wearables, IoT devices, and third-party REST APIs (Garmin, Oura, and Fitbit until the legacy Fitbit Web API turns off on 2026-11-02, with a Google Health route partly released) in one pipeline. It has been used across large clinical cohorts spanning multiple sclerosis, depression, epilepsy, ADHD, Alzheimer's disease, autism, and lung disease research. It is jointly maintained by King's College London and The Hyve, and licensed Apache 2.0.

- Where Beiwe is a lab-scale platform with an optional managed service, RADAR-base presents itself as enterprise/consortium-scale infrastructure, it emerged from and has been used across large EU-funded multi-site clinical consortia (RADAR-CNS and successors), and its architecture reflects that: Kafka-based streaming, IoT gateway support (RADAR-IoT), and explicit support for both in-house institutional hosting and cloud deployment.

## Products / Platform Architecture

- **RADAR-base platform**, the overall open-source stack: mobile apps, backend streaming pipeline, management portal ("Management Portal"), and data pipeline for near-real-time processing and storage.
- **RADAR-IoT**, an open-source, interoperable IoT gateway framework extending the platform to non-phone/non-wearable sensor sources, per a dedicated published architecture paper.
- Wearable integrations on the Supported Devices page (Verified 2026-10-10) [18]:
  - Bluetooth through the Android pRMT app: Polar Vantage V3 and H10, Empatica E4. The E4 is listed with no deprecation notice although Empatica has retired it.
  - Cloud REST connectors: Fitbit (legacy route ends 2026-11-02, see below), Garmin, Oura (Oura includes vendor metrics such as the Readiness Score).
  - Apple Watch and other HealthKit data through the aRMT app's HealthKit plugin.
  - Deprecated: Faros, Biovotion, Pebble 2. Garmin authorization moved from OAuth 1.0 to OAuth 2.0, the default from RADAR-Rest-Source-Auth v4.4.15 (2026-05-07) [27].
  - Not shipped: a Huawei Health Kit connector (schemas released, connector PR #204 open); a Dexcom CGM connector from a 2026 internship, Reported in a radar-base.org post and absent from Supported Devices; Android Health Connect, an open feature request (issue #488, opened 2025-10-06) [31].
- Huawei and Garmin were also named as industry partners at the 2026 Symposium [3]. Partnership is not the same as a released integration.
- **Fitbit route (Verified 2026-10-31)** [19]. The Fitbit connector documented in the RADAR-REST-Connector README pulls from the legacy Fitbit Web API, which Google turns off on 2026-11-02 (moved from 2026-10-30). Google Health authorization (RADAR-Rest-Source-Auth v4.4.16, 2026-07-03) and schemas are released. RADAR-REST-Connector v0.7.6, released 2026-10-30, ships the Google Health converters as a separate google-health-library (ECG, HRV, sleep, exercise and other types). The push ingest, RADAR-PushEndpoint PR #92, was still open and unmerged on 2026-10-31 (last updated 2026-10-20, no new PushEndpoint release since v0.4.0), with eight follow-on Google Health PRs chained onto its branch, also open. The README does not yet document a Google Health route, so whether a released install ingests Google Health data end to end is Unclear.
  - Effect on studies, inferred from repository state. An install on the legacy Fitbit connector stops receiving new Fitbit data on 2026-11-02. Moving to Google Health needs the v0.7.6 converters plus an ingest route that is not yet released, so a team may need branch code or direct help from RADAR-base. Participants must re-authorise through Google. Data already collected is unaffected. The Google Health API was closed to new projects on 2026-10-10 but is apparently open again by 2026-10-19 (Corroborated 2026-10-21, `../../module-01-wearables/profiles/fitbit-google.md`), so a self-hosting team without its own Google Health project would need to open one and pass Google's restricted-scope review and, above 100 users, verification and CASA.

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
| Audio / microphone | Yes | Unclear | Derived. openSMILE audio features, not raw audio. | Unclear | Android via the `radar-android-audio` plugin; the Get Started page lists audio among pRMT streams [20]. Not checked on iOS. |
| Notifications | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Device information | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |

**Verification.** Android column Verified 2026-08-25 from radar-base.org's Phone Data Sensors page, re-read 2026-10-09 (page updated 2026-05-28; battery level is in its list). iOS column updated 2026-10-09 from the page's "Sensors per phone type" chart, which was read directly as an image. The chart was uploaded in September 2019. It marks acceleration, gyroscope, magnetic field, light, battery, regular location, Bluetooth scanning, timezone, time sync and weather as "foreground only" on iOS. Significant location changes and connection to known peripherals work in the background. Steps are read from HealthKit history in the foreground. App usage and call and SMS logs are not available, and data are sent "when activated only". **The chart conflicts with the iOS app's own repository.** `RADAR-base/radar-prmt-ios`, last committed 2021-01-19, describes the app as "work in progress" that "only records location data without sending it to a server". Rows where the chart describes foreground-only collection are therefore marked Conflicting documentation, not Yes. In current code the working iOS route is the active (aRMT, `RADAR-Questionnaire`) app's HealthKit task. It reads 17 HealthKit types (steps, flights climbed, walking and cycling distance, active and basal energy, heart rate, resting heart rate, SpO2, respiratory rate, sleep analysis, workouts, exercise time, blood glucose, blood pressure, weight) when the participant opens the task. A `radar-sensorkit-cordova` plugin for Apple SensorKit exists (last push 2024-11), but nothing found shows it in use. A new React Native app kit (`radar-base-app`) is under active development. Confidence: chart contents Verified; current iOS phone-sensor capability Unclear; HealthKit route Verified from code. Audio row added 2026-10-11 from the vendor fact record (Verified 2026-10-10): `radar-commons-android` has an openSMILE plugin that sends extracted features, and a separate plugin measures PPG with the phone camera [20].

### Notes from earlier verification passes

- **Updated 2026-08-25 (second pass, Verified via direct fetch of `radar-base.org/docs/4048-2/`, "Phone Data Sensors").** The Android passive-app (pRMT) sensor catalog is now itemized and confirmed: relative location (GPS/network, converted to relative coordinates for privacy), 3-axis acceleration (~200ms intervals), 3-axis gyration (rad/s), 3-axis magnetic field (200ms intervals), step count, ambient light (lux, on value change), Bluetooth device counts (hourly), OS-level activity-recognition events (walking, running, cycling, vehicle, etc.), OS-derived sleep events, phone lock/unlock/shutdown ("interaction state"), app foreground/background usage with category, call log (hashed numbers), SMS log (hashed numbers), contact-list count/changes (daily), battery level/charging state, local weather (temperature/pressure/humidity/precipitation, 3-hourly), and app/server connection-status monitoring, 17 documented streams in total. Wearable-sourced physiological signals arrive via separate device integrations (Empatica, Garmin, Fitbit, and others named as 2026 partners).

- **iOS/Android parity, resolved, not assumed (Corroborated).** The same documentation page states explicitly that "substantial differences" exist between the platforms' passive-app builds, and that iOS sensor availability is "more sparse... due to lack of background collection capabilities", the standard iOS background-execution constraint CLAUDE.md flags generically, now confirmed as RADAR-base's own documented position rather than an inferred general platform limitation. The page includes a comparison chart that this fetch could not fully extract; the itemized Android list above should not be assumed to transfer to iOS.

- Active: patient-reported outcome measures (PROMs) and other questionnaire-based active data collection, per the platform's own "About" description.

## Derived Metrics / Analytics

- **No built-in behavioural feature catalogue (Verified 2026-10-10)** [21]. The platform itself computes time-windowed aggregates plus data-quality and compliance monitors for live dashboards, held in a MongoDB hot store. Android passes through OS activity and sleep classifications.
- Behavioural feature extraction is a separate open-source Python package, `radarpipeline` ("feature generation and visualization"), a companion tool much as Forest is for Beiwe [21].
- Wearable vendor metrics (for example Oura's Readiness Score) arrive already computed through the REST connectors [18].
- Earlier passes quoted RADAR-base's description of "feature generation (such as behavioral, environmental, and physiological markers)" as platform scope. That work sits in `radarpipeline` and in per-study analysis, not in the platform.

## Active Data Collection

- PROM/questionnaire delivery is supported per the platform's own description; scheduling sophistication, branching logic, and EMA-specific features (event-triggered, randomized) were not independently verified this session.

## Researcher and Study Management Features

- **Verified 2026-08-25 (second pass, direct fetch of `github.com/RADAR-base`).** A dedicated `ManagementPortal` repository exists (Kotlin, actively updated, Apache-2.0), confirming the "Management Portal" is a real, currently maintained code artifact rather than only a description in marketing materials. The same organization also maintains `RADAR-Questionnaire` (a TypeScript active/questionnaire mobile app), `radar-prmt-android` (the native Android passive-sensing app), `RADAR-Schemas` (data schema catalog), and Kubernetes/Helm deployment tooling (`RADAR-Kubernetes`, `radar-helm-charts`), indicating a maintained, containerized-deployment-ready reference architecture. Specific participant-management, adherence-monitoring, and audit-logging feature depth within the Management Portal was not independently verified beyond confirming the repository's existence and active status.

## Data Access and Export

- Kafka-based streaming architecture is documented in RADAR-base's own peer-reviewed platform papers (e.g., the original RADAR-base description and RADAR-IoT). This supports near-real-time data flow by design, in contrast to platforms built around periodic batch sync. Self-hosting is explicit and emphasized, particularly for "in-hospital studies" needing enhanced privacy/data-residency control, a meaningfully different governance posture than a SaaS-only competitor. Cloud deployment is also supported for institutions that prefer it, including now via a confirmed managed-hosting route (see Pricing/Deployment below).
- **Export routes beyond Kafka streaming (Verified 2026-10-10)** [22]:
  - Raw data from cold storage as AVRO, JSON or CSV.
  - `radar-output-restructure` writes files by project, participant, topic and hour from S3, Azure Blob or local storage. HDFS support was dropped in version 2.0.0.
  - Aggregated data through the Swagger-documented REST API (RADAR-REST-API, reading MongoDB).
  - Live dashboards, manual file upload through the Upload Connector, and direct access to the deployment's own Kafka, object storage and databases.
- **History depth (Corroborated).** No platform limit, since data stays in the deployment the study owns. For REST wearables, staff set start and end dates per participant and can re-pull data between dates, subject to each vendor API's own history limits, which are not stated [28].
- **Rate limits are not public (2026-10-10).** Each deployment sets its own; none is documented for the REST API or gateway. Upstream vendor limits apply to the REST connectors, and the Fitbit connector polls each user every 150 s by default [19].

## APIs, SDKs, and Extensibility

- Apache 2.0 licence across the stack (per the project's own materials), meaning the full backend, mobile clients, and IoT gateway are open for institutional modification, comparable in openness to Beiwe, but architected for larger multi-site consortium deployments rather than single-lab studies.
- **Licence detail (Verified 2026-10-10).** Apache 2.0 on the backend, Management Portal, Android pRMT, aRMT and RADAR-Kubernetes. A few side repositories report no standard licence (m2c2kit, the OpenSmile Cordova plugin) [1].
- Developer access is open with no application: GitHub, a public wiki, Slack, Swagger API docs and a help desk. RADAR-Kubernetes states that community support is voluntary and given "as time permits" [23].

## Deployment and Infrastructure

- Self-hosted (institution-run infrastructure) or cloud-deployed, both explicitly supported, per the platform's own "About" page.
- **RADAR-Kubernetes sizing (Verified 2026-10-10)** [23]. Helm/helmfile install, on-premise or in any cloud. Minimum single node of 8 vCPU, 32 GB memory and 200 GB storage, or a 3-node cluster, plus a DNS and an SMTP server. The README calls it early-stage though used in a few production environments.
- RADAR-Docker is deprecated in favour of RADAR-Kubernetes (announced for end of 2021) [23].
- The Hyve can also host RADAR-base in a private cloud or on-premise, besides the public-cloud managed service [29].
- A participant self-enrolment portal (`radar-self-enrolment-ui`) and a React Native app kit (`radar-base-app`, created 2025-11-26) exist on GitHub. Neither is described as a released product.
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
- **Vendor fact record, 2026-10-10.** The points below supersede the "not independently verified" statement above where they overlap.
  - **ISO 27001 (Corroborated, self-claim).** The Hyve says it holds ISO 27001:2022 (recertified 2023, first certified 2017), scoped to development, hosting and support of open-source software, consultancy and biomedical data analysis. The scope does not name RADAR-base, and no certificate or registry entry was found. A three-year certificate from 2023 would be due for renewal around late 2026 (inference). Self-hosted deployments inherit no certification [25].
  - **HIPAA, BAA and SOC 2 not public (2026-10-10).** No mention on RADAR-base or The Hyve pages; the managed service is EU and GDPR oriented [15].
  - **GDPR and DPA (Corroborated).** Managed installs run in a GDPR-compliant public cloud at the client's chosen location. The Hyve draws up a Data Processing Agreement if it keeps managing the platform after the initial period or has access to sensitive data [15].
  - **Responsibility and deletion (Verified).** The active-app privacy policy puts all responsibility for data on the project and deployment owners. Data is kept for the study's duration. Deletion requests go from the project owner to the deployment owner, and study data is deleted, including from backups, generally within 60 days. The developers (KCL, The Hyve) cannot delete project data. The app sends Firebase analytics and crash data to the developers [26].
  - **Play data-safety declarations (Verified as declared).** The passive app's listing says data is not transferred over a secure connection and cannot be deleted. The active app's listing says data is encrypted in transit and cannot be deleted. The passive app's encryption declaration contradicts the platform docs (radar-commons sends data over HTTPS) and is most likely a wrong form entry, but it is what participants see. RADAR-Kubernetes uses TLS by default and has a `disable_tls` option, so encryption in transit depends on the deployment. "Cannot be deleted" fits the policy's model, where only the deployment owner deletes [16].
  - **Data residency.** Set by whoever hosts. The radar-base.org Google Health integration stores data in AWS eu-west-2 (London) or university infrastructure, and The Hyve's demo service keeps app data in the EU [24, 32].
  - **AI training.** Google Health API data collected through RADAR-base is not used to train generalised AI or ML models (Verified, scope Google Health integration; the policy appears to cover the KCL-run deployment, inference). No AI-training term is published for the platform generally or for The Hyve as host; The Hyve's demo-service policy says anonymised data may be kept indefinitely and identifiable contact data up to 10 years [24, 32].
  - **FDA.** No clearance. openFDA searches for RADAR-base, The Hyve, King's College and Onsentia returned no matches on 2026-10-10. RADAR-base is research software and claims no FDA status [30].

## Pricing

- Software is free and open source (Apache 2.0). No published licence fee was found.

- **Resolved 2026-08-25 (second pass, resolving unresolved-question #86, Verified via direct fetch of `thehyve.nl/services/radar-base-as-a-service`).** The Hyve, RADAR-base's co-maintainer, offers a named managed-hosting product, **"RADAR-base as a Service,"** distinct from self-hosting. Per the vendor's own service page: platform installation configured to the study's needs; hosting on a GDPR-compliant public cloud of the customer's choosing; support for "unlimited studies and participants" in the general offering description, though the same page separately caveats that the service is best suited to studies of **roughly 200 participants or fewer**, attributed to a single-server infrastructure model; end-user training for passive sensors, surveys, and wearable integrations (Fitbit/Garmin named); ongoing maintenance and technical support; and a stated 2 to 4 week setup timeline. **No pricing figures are published**, this remains a quote-based service, so RADAR-base does not yet match Beiwe's now-resolved rate transparency (see `profiles/beiwe.md`). This is RADAR-base's first confirmed managed-hosting alternative to self-hosting.
- **Re-read 2026-10-10 (Verified):** the page states that "The client organisation will always be the owner of the collected data"; a Data Processing Agreement is drawn up if The Hyve keeps managing the platform after the initial period or gets access to sensitive data; the platform runs on "a single computer based server in contrast to a cluster of computers", so throughput can limit concurrent senders; "Studies with a maximum of 200 participants are ideal for this setup", although the subscription "allows you to use it for any number of studies or participants"; and the service is "best suited for small-scale and short-term studies", with pilots recommended. Hosting is in "a GDPR compliant public cloud infrastructure located at the choice of the client". No price is given; contact via office@thehyve.nl or the inquiry form. Export procedures are not described.
- **Minimum commitment not public (2026-10-10).** The service page mentions a "subscription model" and an "initial service period" but gives no term or minimum. Self-hosting has no commitment. No academic discount or academic price list is published; The Hyve markets the same services to pharma, academia and CROs (Corroborated) [15, 29].
- The service page still advertises Fitbit training, although the legacy Fitbit route stops on 2026-11-02 (see Products / Platform Architecture) [19].
- **How larger deployments scale (Unclear):** the page does not say how the ~200-participant ceiling is raised. The documented open-source route for larger installs is RADAR-Kubernetes (pushed 2026-10-06), whose README says it is used "in few production environments" and is still in its early stages. That this is The Hyve's scale-up path is an inference, not stated.

## Research Evidence and Validation

- RADAR-base has a substantial published-use record across multiple disease areas, multiple sclerosis, depression, epilepsy, ADHD, Alzheimer's disease, autism, and lung disease, per its own publications page and independently indexed peer-reviewed platform-description papers (e.g., a 2024 JMIR Mental Health paper on RADAR-base for remote monitoring of mental and physical conditions). This is a broader clinical-domain published footprint than most other platforms profiled in this module, consistent with its EU consortium origin funding large multi-site cohort studies.

## Strengths

- Purpose-built for large-scale, multi-site, multi-modal (phone + wearable + IoT) data collection, with a streaming architecture designed for near-real-time throughput rather than batch sync.
- Broad, verifiable published-use record across multiple serious clinical domains.
- Apache 2.0, fully open source, with explicit self-hosting support aimed at institutions needing to keep data on their own infrastructure.
- Broad shipped wearable catalogue (Polar, Empatica E4, Garmin, Oura, HealthKit) and ongoing integration work (Huawei, Google Health, Dexcom in progress; Garmin moved to OAuth 2.0 in 2026). Garmin and Huawei were also named as industry partners at the 2026 Symposium [3, 18].
- Jointly maintained by an academic institution (KCL) and a dedicated open-source health-informatics company (The Hyve), which is a different (arguably more sustainable) maintenance model than a single academic lab.
- **New (second pass):** unlike the 2026-08-24 assessment, RADAR-base now has a confirmed managed-hosting route ("RADAR-base as a Service," via The Hyve) for teams without in-house DevOps capacity, plus a maintained, itemized Android passive-sensor catalog and a confirmed, actively-developed Management Portal repository.

## Limitations

- Kafka-based, self-hosted-by-default architecture implies a meaningfully higher DevOps/infrastructure floor than commercial no-code competitors, and likely higher than Beiwe's already-nontrivial AWS requirement, though this was not independently benchmarked head-to-head this session.
- **Updated 2026-08-25**: a managed-hosting option now exists (The Hyve's "RADAR-base as a Service"), but the vendor's own page caveats it to studies of roughly 200 participants or fewer (single-server infrastructure) and does not publish pricing, a real but different limitation than "no option exists at all."
- **Updated 2026-08-25**: iOS/Android sensor parity is now confirmed as *not* present, RADAR-base's own documentation states "substantial differences" exist and describes iOS sensor availability as "more sparse" due to background-execution constraints, consistent with the pattern already Verified for AWARE Framework in this module's earlier second pass. This should not be treated as a minor caveat.
- **Legacy Fitbit data stops on 2026-11-02.** The Google Health converters were released on 2026-10-30, but the push ingest was not, so a documented end-to-end Google Health route is still missing [19].
- No HIPAA or SOC 2 documentation was located (2026-10-10). The only ISO 27001 claim is The Hyve's own, for The Hyve B.V., with a scope that does not name RADAR-base (Corroborated) [25]. Compliance should not be inferred from EU/consortium origin. The managed-hosting page's own language commits only to "GDPR-compliant public cloud" hosting infrastructure, a hosting-environment claim, not a certification of RADAR-base's own compliance posture.

## Best-Fit Use Cases

- Large, multi-site, multi-country clinical cohort studies combining phone, wearable, and IoT data streams, especially where near-real-time data flow matters.
- Institutions with existing DevOps/data-engineering capacity that want full data custody via self-hosting.
- Studies already using or planning to use supported wearables (Garmin, Oura, Polar, HealthKit devices) alongside phone sensing. Fitbit only once a Google Health ingest release ships; Huawei only once its connector is released [18, 19].

## Poor-Fit Use Cases

- Small single-site pilots without dedicated infrastructure engineering support, the operational floor appears higher than several commercial or lighter-weight academic alternatives in this module.
- Teams wanting a fully managed SaaS experience for studies above roughly 200 participants: The Hyve's managed service exists but is pitched at small, short-term studies on a single server.
- Studies that need passive phone sensing on iOS: there is no maintained iOS passive app (radar-prmt-ios last committed 2021-01-19); iOS data come through HealthKit in the aRMT app.

## Open Questions

- *(Directed to: RADAR-base maintainers, King's College London / The Hyve, via https://radar-base.org)*

- ~~Is there a managed-hosting or paid-support offering comparable to Beiwe's Service Center?~~ **Resolved 2026-08-25**, yes, "RADAR-base as a Service" via The Hyve; pricing still not public.
- What does "RADAR-base as a Service" actually cost, and how does its ~200-participant single-server ceiling get raised for larger studies? (Re-checked 2026-10-10: still no price; RADAR-Kubernetes is the documented cluster route, but the page does not say The Hyve offers it.)
- ~~What is the exact current sensor/data-stream catalog, and how do iOS and Android differ?~~ **Largely resolved 2026-08-25** for Android (17-item itemized list) and qualitatively for the iOS gap ("substantial differences," iOS "more sparse"); the exact iOS-side itemized list (which of the 17 Android streams iOS lacks or restricts) is still not obtained. **Partly resolved 2026-10-09**: the 2019 per-stream chart is now in the stream table, but it conflicts with the dormant iOS pRMT repository, and current iOS passive collection appears to run through HealthKit in the aRMT app. Still open: which iOS app a new study would actually deploy for phone sensors. Re-checked 2026-10-10: radar-prmt-ios unchanged (last commit 2021-01-19, last push 2023-06-20, not archived) and still the only iOS pRMT repository in the organization.
- What compliance certifications (HIPAA, GDPR DPA beyond hosting-infrastructure GDPR-compliance framing, SOC 2, ISO 27001) does the maintained reference deployment or a typical institutional deployment carry? **Partly answered 2026-10-10.** The Hyve claims ISO 27001:2022 for The Hyve B.V.; whether its scope covers RADAR-base as a Service, and whether it was renewed after 2023, are still open. HIPAA and SOC 2 remain unpublished.
- Is the passive app's Play declaration that data is not transferred securely a form error? Only the developer (The Hyve) can answer.
- When will the Google Health push ingest (RADAR-PushEndpoint PR #92) ship and be documented? The converters shipped in REST-Connector v0.7.6 on 2026-10-30, three days before the Fitbit Web API turns off on 2026-11-02.
- What is the realistic infrastructure/DevOps staffing requirement to stand up and operate a **self-hosted** production instance (as distinct from the now-confirmed managed-hosting alternative)?
- ~~What built-in derived-feature/analytics catalog exists natively versus requiring custom per-study development?~~ **Resolved 2026-10-10**, no built-in behavioural catalogue; the platform computes aggregates and quality monitors, and feature generation is the separate `radarpipeline` package [21].

## Vendor Fact Record

<!-- facts:begin -->
*Generated from the fact record by `tools/facts/generate.py`. Edit the record, not this block.*

**Research access**

| Fact | Value |
|---|---|
| Formal research or academic program (name, what it offers) | No vendor research program as such; RADAR-base is open-source research software. The formal researcher offering is The Hyve's RADAR-base as a Service, an all-inclusive managed deployment (installation, cloud hosting, training, maintenance and support). The Hyve also sells deployment, integration and development services. [V, 2026-10-10] |
| Who can join the research program | No formal eligibility criteria. Anyone may self-host the open-source stack. The Hyve's service addresses pharma and academic researchers and CROs. [V, 2026-10-10] |
| How to apply, and any approval or review step | Self-hosting: no application, install from the public GitHub repositories. Managed service: inquiry to The Hyve, with set-up in 2 to 4 weeks; no review step is published. [V, 2026-10-10] |
| Whether the program is active, paused, renamed or closed | Active. The managed-service page is live, the 2026 symposium was held, and the GitHub organisation shows releases and pushes in October 2026 (RADAR-Schemas v0.9.2 on 2026-10-06). [V, 2026-10-10] |
| Whether the general developer or API program is open to new applicants | Open to all with no application. All components are on GitHub with a public wiki, Slack, Swagger API docs and a help desk. Community support is voluntary and best effort. [V, 2026-10-10] |
| Participant or user limits before approval or by tier | **RADAR-base as a Service (The Hyve):** No licence cap. RADAR-base as a Service allows any number of studies or participants but runs on a single server, and The Hyve says studies of at most 200 participants are ideal for it. Self-hosted capacity depends on the cluster. [V, 2026-10-10] |
| How academic access differs from commercial or consumer access | No published difference. The whole stack is Apache 2 for every user with no licence cost, and The Hyve markets the same services to pharma, academia and CROs. No separate academic terms or prices are published. [C, 2026-10-10] |

**Pricing**

| Fact | Value |
|---|---|
| Device or hardware list price | n/a |
| Consumer subscription or membership price | n/a |
| Research or academic pricing or discount | Not public [2026-10-31] |
| Fees for API, SDK, platform or data access | None for the software; all components are Apache 2 and free of licence cost. Costs are infrastructure and any paid services from The Hyve. [V, 2026-10-10] |
| Minimum order, term or commitment | **RADAR-base as a Service (The Hyve):** Not public [2026-10-31] |
| Whether pricing requires contacting sales | Yes for The Hyve's managed service and other services, which start with an inquiry; no prices are published. Self-hosting needs no quote. [C, 2026-10-10] |
| Price of managed hosting | Not public [2026-10-31] |

**Data access and terms**

| Fact | Value |
|---|---|
| Raw signals available to researchers, and by which route | Android passive app (pRMT): relative location (no absolute location reaches the server), accelerometer, gyroscope, magnetometer, steps, light, Bluetooth device counts, Android activity-recognition and sleep events, screen state, app usage, call and SMS metadata (hashed numbers), battery, weather; audio features via an openSMILE plugin, and a camera-PPG plugin. Bluetooth wearables via pRMT (Polar Vantage V3 and H10, Empatica E4); cloud wearables via REST connectors (Fitbit, Garmin, Oura); Apple Watch and other HealthKit data via the active app. iOS passive collection is sparser. No Android Health Connect route. [V, 2026-10-10] |
| Derived or processed metrics available to researchers | The platform computes time-windowed aggregates and data-quality and compliance monitors for live dashboards (MongoDB hot store), and Android passes through OS activity and sleep classifications. Behavioural feature extraction is a separate open-source Python package, radarpipeline. Wearable vendor metrics (for example Oura readiness) arrive through REST connectors. [V, 2026-10-10] |
| Documented sampling rates or temporal resolution | Android defaults: accelerometer, gyroscope and magnetometer about every 200 ms (about 5 Hz); Bluetooth device count hourly; contact list daily; weather every 3 hours; light and battery on change. Configurable per study. [V, 2026-10-10] |
| How far back data can be retrieved | No platform limit; phone data starts at enrolment and is kept in the deployment the study owns. For REST wearables staff set start and end dates per participant and can reset to re-pull data between dates, subject to each vendor API's own history limits, which are not stated. [C, 2026-10-10] |
| Export, API, SDK or file routes | Raw data exported from cold storage as AVRO, JSON or CSV; radar-output-restructure writes files by project, participant, topic and hour from S3, Azure Blob or local storage; aggregated data via the REST API (Swagger-documented); live dashboards; manual file upload via the Upload Connector; direct access to the deployment's own Kafka, object storage and databases. [V, 2026-10-10] |
| API rate limits | Not public [2026-10-31] |
| Terms on retaining, storing or deleting data | The deployment owner controls retention and deletion. The active-app policy says data is kept for the study's duration, deletion requests go from the project owner to the deployment owner, and study data is deleted including from backups generally within 60 days; the developers (KCL, The Hyve) cannot delete project data. Both Play listings declare that the developer gives no way to request deletion. The Hyve's demo service keeps identifiable contact data up to 10 years. [V, 2026-10-10] |
| Terms on using data to train AI or ML models | **Google Health API integration:** Google Health API data collected through RADAR-base is not used to train generalised AI or ML models. [V, 2026-10-10]<br>**Platform and The Hyve managed service:** Not public [2026-10-31] |
| Announced shutdowns, deprecations or migrations, with dates | **Fitbit route (legacy Fitbit Web API to Google Health API):** The released Fitbit connector (RADAR-REST-Connector) pulls from the legacy Fitbit Web API, which Google turns off on 2026-11-02. Migration to the Google Health API is under way: authorization is released (RADAR-Rest-Source-Auth v4.4.16, 2026-07-03), schemas are merged and released (RADAR-Schemas, push/googlehealth), and RADAR-REST-Connector v0.7.6 (released 2026-10-30) ships the Google Health converters as a separate google-health-library. The push ingest, RADAR-PushEndpoint PR #92 "Add Google Health API push integration", is still open and unmerged on 2026-10-31 (last updated 2026-10-20; newest release v0.4.0, 2025-06-19), with eight follow-on Google Health PRs stacked on its branch, all open, and the connector README still documents only the legacy Fitbit route. Whether a released install can ingest Google Health API data end to end is not documented. [V, 2026-10-31]<br>**Deployment and export:** RADAR-Docker deployment is deprecated in favour of RADAR-Kubernetes (announced for end of 2021). radar-output-restructure dropped HDFS from version 2.0.0. [V, 2026-10-10]<br>**Device integrations:** Faros, Biovotion and Pebble 2 integrations are marked deprecated. Garmin authorization moved from OAuth 1.0 to OAuth 2.0 (default from RADAR-Rest-Source-Auth v4.4.15, 2026-05-07). The iOS passive app repository has had no commit since 2021-01-19. [V, 2026-10-10] |
| Software licence of the platform's components | Apache 2.0 for the whole stack (backend, Management Portal, Android pRMT, aRMT, RADAR-Kubernetes). A few side repositories report no standard licence (m2c2kit, the OpenSmile Cordova plugin). [V, 2026-10-10] |
| Self-hosting and managed-hosting options | Self-host on-premise or in any cloud via RADAR-Kubernetes (Helm/helmfile; minimum single node 8 vCPU, 32 GB memory, 200 GB storage, or a 3-node cluster), with a DNS and SMTP server; the README calls it early-stage though used in production. Managed: The Hyve's RADAR-base as a Service, a dedicated per-organisation install on a public cloud of the client's choice; The Hyve also hosts in private cloud or on-premise. [V, 2026-10-10] |
| App store availability on iOS and Android | **pRMT (passive) Android:** RADAR passive RMT (publisher TheHyve) on Google Play, Android only. Its Play data-safety section, as declared by the developer, says data is not encrypted in transit and cannot be deleted. [V, 2026-10-10]<br>**pRMT (passive) iOS:** No passive app on the iOS App Store. The iOS pRMT repository is work in progress, records location only and sends nothing to a server; last commit 2021-01-19 (last push 2023-06-20). [V, 2026-10-10]<br>**aRMT (active) Android and iOS:** RADAR active RMT on Google Play (PhiDataLab) and on the iOS App Store (iPhone only, iOS 16.0 or later; seller Onsentia Limited). Its Play data-safety section declares data encrypted in transit. [V, 2026-10-10] |

**Compliance and regulatory**

| Fact | Value |
|---|---|
| Whether a HIPAA Business Associate Agreement is offered | Not public [2026-10-10] |
| Whether a data processing agreement is offered | **RADAR-base as a Service (The Hyve):** The Hyve draws up a Data Processing Agreement when it keeps managing a RADAR-base as a Service platform after the initial service period or has access to sensitive data. The client owns the data. [C, 2026-10-10] |
| Published HIPAA statement | Not public [2026-10-10] |
| Published GDPR statement | RADAR-base as a Service installs are hosted in a GDPR-compliant public cloud at the client's chosen location. The active-app policy places responsibility for data on the project and deployment owners, and says the app sends Firebase analytics and crash data to the developers. [C, 2026-10-10] |
| ISO/IEC 27001 status and evidence | **The Hyve B.V.:** The Hyve says it holds ISO 27001:2022 (recertified 2023, first certified 2017), scoped to development, hosting and support of open-source software, consultancy and biomedical data analysis. No certificate or registry entry found. [C, 2026-10-10] |
| SOC 2 status and evidence | Not public [2026-10-10] |
| FDA clearances, from the FDA database | Not public [2026-10-10] |
| Where data is stored, and residency options | Set by whoever hosts the deployment. RADAR-base as a Service runs in a public cloud location of the client's choice. The radar-base.org Google Health integration stores data in AWS eu-west-2 (London) or university infrastructure. The Hyve's demo service keeps app data in the EU. [V, 2026-10-10] |

<!-- facts:end -->

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
18. RADAR-base, "Supported Devices." https://radar-base.org/docs/supported-devices/ (accessed 2026-10-10, vendor fact record). **Primary/Verified.** Polar, Empatica E4, Fitbit, Garmin, Oura, HealthKit plugin; deprecated Faros, Biovotion, Pebble 2.
19. Fitbit route evidence (accessed 2026-10-10, re-checked 2026-10-30 and 2026-10-31, vendor fact record). REST-Connector v0.7.6 release notes https://github.com/RADAR-base/RADAR-REST-Connector/releases/tag/v0.7.6 ; **Primary/Verified.** RADAR-PushEndpoint issue #91 https://github.com/RADAR-base/RADAR-PushEndpoint/issues/91 and PR #92 https://github.com/RADAR-base/RADAR-PushEndpoint/pull/92 ; RADAR-PushEndpoint releases https://github.com/RADAR-base/RADAR-PushEndpoint/releases ; RADAR-Rest-Source-Auth releases https://github.com/RADAR-base/RADAR-Rest-Source-Auth/releases ; RADAR-REST-Connector README and releases https://github.com/RADAR-base/RADAR-REST-Connector ; Fitbit Web API turn-off notice https://dev.fitbit.com/build/reference/web-api/intraday/ and https://developers.google.com/health .
20. `radar-commons-android` audio and PPG plugins. https://github.com/RADAR-base/radar-commons-android/tree/master/plugins/radar-android-audio ; https://github.com/RADAR-base/radar-commons-android/tree/master/plugins/radar-android-ppg ; RADAR-base, "Getting Started." https://radar-base.org/getting-started-with-radar-base/ (accessed 2026-10-10). **Primary/Verified.**
21. `RADAR-base/radarpipeline` https://github.com/RADAR-base/radarpipeline and RADAR-base, "Concepts and Components." https://radar-base.org/docs/concepts-and-components-of-radar-base/ (accessed 2026-10-10). **Primary/Verified.** Aggregates and quality monitors in the platform; feature generation in a separate package.
22. Export routes. https://radar-base.org/getting-started-with-radar-base/ ; https://github.com/RADAR-base/radar-output-restructure ; https://radar-base.org/docs/concepts-and-components-of-radar-base/ (accessed 2026-10-10). **Primary/Verified.** AVRO, JSON, CSV export; restructure tool (no HDFS since 2.0.0); REST API.
23. `RADAR-base/RADAR-Kubernetes` README https://github.com/RADAR-base/RADAR-Kubernetes ; `RADAR-base/RADAR-Docker` README https://github.com/RADAR-base/RADAR-Docker ; RADAR-base Community page https://radar-base.org/community/ (accessed 2026-10-10). **Primary/Verified.** Sizing, early-stage status, voluntary support, RADAR-Docker deprecation, developer channels.
24. RADAR-base, "Google User Data Privacy Policy." https://radar-base.org/google-privacy-policy/ (accessed 2026-10-10). **Primary/Verified.** No AI/ML training on Google Health data; AWS eu-west-2 or university hosting.
25. The Hyve, "The Hyve ISO certified" (2023-12-05). https://www.thehyve.nl/articles/the-hyve-iso-certified-2023 ; homepage https://www.thehyve.nl/ (accessed 2026-10-10). **Self-claim, Corroborated.** ISO 27001:2022 for The Hyve B.V.
26. RADAR-base, "Active App (aRMT) Privacy Policy." https://radar-base.org/active-app-armt-privacy-policy/ (accessed 2026-10-10). **Primary/Verified.** Owner responsibility, retention for study duration, deletion within about 60 days via the deployment owner, Firebase.
27. `RADAR-base/RADAR-Rest-Source-Auth` PR #317. https://github.com/RADAR-base/RADAR-Rest-Source-Auth/pull/317 (accessed 2026-10-10). **Primary/Verified.** Garmin OAuth 1.0 to OAuth 2.0.
28. RADAR-base, "RADAR REST Source Auth." https://radar-base.org/docs/radar-rest-source-auth/ (accessed 2026-10-10). **Primary.** Per-participant start and end dates and re-pull for REST wearables.
29. The Hyve, "RADAR-base." https://www.thehyve.nl/services/radar-base (accessed 2026-10-10). **Primary/Verified.** Audience (pharma, academia, CROs), free of licence costs, private-cloud or on-premise hosting, development services.
30. openFDA 510(k), PMA and registration searches for RADAR-base, The Hyve, King's College and Onsentia, e.g. https://api.fda.gov/device/510k.json?search=device_name:"radar-base" (run 2026-10-10). **Regulator database.** No matches.
31. `RADAR-base/radar-commons-android` issue #488, "Add Support for Reading Data from Google Health Connect." https://github.com/RADAR-base/radar-commons-android/issues/488 (accessed 2026-10-10). **Primary.** Open feature request.
32. The Hyve, "RADAR-base demo privacy policy." https://www.thehyve.nl/radar-base-demo-privacy-policy (accessed 2026-10-10). **Primary/Verified.** EU data location; identifiable contact data up to 10 years; anonymised data may be kept indefinitely.
