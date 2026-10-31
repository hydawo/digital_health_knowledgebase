# Avicenna Research (formerly Ethica / Ethica Data)

## Quick Facts

| Field | Details |
|---|---|
| Organization | Avicenna Research (rebrand of Ethica Data) |
| Category | Commercial mobile sensing, EMA, and clinical-trial data-capture platform |
| Current status | Active, under new name, the company rebranded from "Ethica Data" to "Avicenna Research" (Ethica name to be dropped by July 2024 [35]); weekly release notes continue (latest read 2026-10-06 [41]) |
| Platforms/devices | iOS app ("Avicenna Research", App Store, v1065 released 2026-10-07) and Android app (`com.ethica.logger`, Google Play, updated 2026-09-05); requires iOS 16.0+ or Android 10.0+ (Android minimum re-checked 2026-10-30) [39]; web researcher dashboard; a participant web app (surveys and cloud wearables, no phone sensors) [22]. Checked 2026-10-11. |
| Open source | No. Proprietary; the terms say all service software belongs to Avicenna Research or its software providers [17] |
| Hosting/deployment | Managed cloud service run by Avicenna by default. White-label option ranges from in-house data storage to a full on-premises installation of the closed-source services on the customer's infrastructure, and on-premise deployments are in use [28][29]. Data residency for the managed service is conflicting documentation (Canada versus UK/EEA statements, 2026-10-11; see Privacy). |
| Pricing model | Commercial licence, pricing not public. A free trial exists for testing only: trial data are wiped monthly and the study is deleted after one year, so real field research needs a paid licence (vendor FAQ, Verified 2026-10-10). No academic rate found. SMS notifications, if enabled, are billed at Twilio's cost plus 30% [32]. |
| Last verified | 2026-10-11 (vendor fact record) |

## Summary

- Avicenna Research is the current name of the platform long known in the digital-phenotyping and EMA literature as **Ethica** (also referenced historically as "Ethica/iEpi," reflecting an earlier academic lineage at the University of Saskatchewan). It is a commercial, no-code-for-researchers platform combining survey/EMA delivery, cognitive and behavioral tasks, sensor-based passive data collection, wearable integration, and a data-access/analytics dashboard, explicitly positioned toward clinical-trial and health-research use, not just academic mobile sensing. The company markets under both names in different contexts (the app store listing read "Avicenna (Ethica)" in 2026-08 and is now titled "Avicenna Research"), so researchers searching prior literature for "Ethica" should expect to land on Avicenna's current materials.

- **Naming note handled carefully per CLAUDE.md's instruction to record rather than silently resolve ambiguity:** Ethica Data and Avicenna Research are the same corporate entity under two names, not two competing platforms, confirmed by the shared app-store listing ("Avicenna (Ethica)"), Avicenna's own site being hosted at a URL referencing "Ethica Data" in its page title, and Crunchbase/CB Insights profiles cross-referencing both names to the same company.

## Products / Platform Architecture

- **Avicenna app** (iOS/Android, listed as "Avicenna (Ethica)" in 2026-08 and titled "Avicenna Research" by 2026-10-10), participant-facing data collection.
- **White-label study apps**, a working service. On 2026-10-11 the App Store listed 33 further iOS apps under Avicenna Research Inc. besides the main app (32 study-branded apps plus the Avicenna Keyboard app), 13 of them first released in 2026 [30].
- **Researcher dashboard**, study design, participant management, data access and analytics.
- Named feature areas per the vendor's own site: Outcome Assessment, TeleVisit, Cognitive and Behavioral Tasks, Sensor-based Data, Study Management, Data Access & Analytics, White-Label Solutions.

## Sensors and Data Streams

- Every Module 2 profile uses the same table so platforms can be compared row by row. Rows are the passive streams named in `CLAUDE.md`. "Yes" and "No" are used only where a primary source says so; "Unclear" means nothing current was verified, and "No (OS)" means the operating system does not expose the stream to any third-party app. Confidence and sources are stated under the table. The convention is recorded in [`../../shared/profile-table-conventions.md`](../../shared/profile-table-conventions.md).

| Stream | Android | iOS | Raw or derived | Sampling configurable | Notes |
|---|---|---|---|---|---|
| GPS / location | Yes | Yes | Raw (exportable as CSV, KML, GPX) | Yes, collection cycle 1 to 60 minutes | Each GPS cycle stays active 60 seconds and saves every reading [21][34]. |
| Accelerometer | Yes | Unclear | Raw | Yes, collection cycle 1 to 60 minutes; 60-second burst per cycle | On the Raw Data list [21][22]. |
| Gyroscope | Yes | Unclear | Raw | Yes, collection cycle | On the Raw Data list [21]. |
| Magnetometer | Yes | Unclear | Raw (magnetic field) | Yes, collection cycle | On the Raw Data list [21]. |
| Barometer | Yes | Unclear | Raw (pressure) | Yes, collection cycle | On the Raw Data list [21]. |
| Ambient light | Yes | Unclear | Raw | Yes, collection cycle | On the Raw Data list [21]. |
| Proximity | Yes | Unclear | Raw | Yes, collection cycle | On the Raw Data list [21]. |
| Device motion / activity recognition | Unclear | Unclear | Derived (step counts, activity information) | Unclear | Named on the Sensor Data page [43]; per-OS availability not stated. |
| Screen state | Yes | Unclear | Event | Unclear | On the Raw Data list [21]. |
| App usage | Yes | Yes | Raw on Android; hourly Screen Time usage summaries on iOS (added 2026-04) | Unclear | App Usage (Legacy) is closed to new studies [25][35]. |
| Battery / charging | Yes | Unclear | Raw | Unclear | On the Raw Data list [21]. |
| Network / connectivity | Unclear | Unclear | Unclear | Unclear | Not on the record's stream list. |
| Wi-Fi | Yes | Unclear | Raw | Unclear | On the Raw Data list [21]. |
| Bluetooth | Yes | Unclear | Raw, including beacons (beacon data also exportable as GEXF) | Unclear | Beaconing used in the SHED studies. Qian 2024 removed iPhone users because Bluetooth beaconing did not work reliably on iOS. |
| Calls (metadata) | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| SMS (metadata) | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Keyboard | Yes | Yes (separate app) | Raw | Unclear | On the Raw Data list [21]. On iOS a separate Avicenna Keyboard app collects keystroke data (App Store, released 2025-12-16) [30]. |
| Audio / microphone | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Notifications | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Device information | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |

**Verification.** Updated 2026-10-11 from the vendor fact record (raw_streams and sampling_rates, Verified). The stream list comes from the vendor's Raw Data reference [21], which also gives every data-source ID. The vendor says many sources are Android-only without saying which in the material read, so iOS reads "Unclear" except where an iOS route is documented. Phone sensors are polled once per collection cycle, every 5 minutes by default and configurable from 1 to 60 minutes; iOS honours the interval and Android may not [22]. The Bluetooth row's iOS finding comes from Qian et al. 2024, a Module 2 catalogue paper.

- **Wearables and other sources (record raw_streams, sampling_rates).** Garmin Health SDK raw watch data (25 Hz accelerometer, 32 Hz gyroscope, beat-to-beat intervals; heart rate or SpO2 configurable from every 1 second to once an hour) [26]. Apple SensorKit streams including ECG and PPG, motion downsampled to 32 Hz, on approved studies with a custom app [27]. Cloud data fetched daily from Fitbit (1-minute intraday activity), Garmin Health API (15-minute slices), Oura, WHOOP, Polar, HealthKit, Hexoskin and Mira [21][34]. The vendor's sensor page also lists web activity.

### Notes from earlier verification passes

- The vendor states integration with "a wide range of smartphone sensors and wearables that studies can use to objectively measure behavior or verify self-reports." Specific sensor list, sampling configurability, and iOS-vs-Android parity were **not independently verified against current developer documentation** this session, flagged as an open question, consistent with CLAUDE.md's instruction not to assume parity.

## Derived Metrics / Analytics

- **Updated 2026-10-11 (vendor fact record, derived_metrics, Verified).**
- Phone-derived step counts and other activity information [43].
- Vendor-computed wearable metrics pulled from cloud accounts (Garmin, Fitbit, Oura readiness and sleep, WHOOP recovery, Polar sleep) [21].
- GPS mobility features: **unclear whether still offered.** A vendor forum reference posted 2025-12-16 described a nightly batch (daily distance, radius of gyration, location entropy, time at home, daily location clusters), but that page has returned 404 since 2026-10-19 and is absent from forum search. Avicenna's security page says it "does not perform any processing on the data collected for a given study". Ask Avicenna [24].
- An Analysis page in the researcher dashboard for data quality, engagement and retention (added 2026-03) [24]. Kibana and Vega charts in the dashboard.
- The security post still says Avicenna "does not perform any processing on the data collected for a given study" [16], which the mobility-features reference contradicts.

## Active Data Collection

- Surveys/EMA, cognitive and behavioral tasks, and a "TeleVisit" feature (implying live video/remote-visit capability distinct from passive sensing) are named on the vendor's own feature page, a broader active-assessment feature set than most academic-open-source competitors in this module, oriented toward clinical-trial-style outcome assessment.

## Researcher and Study Management Features

- "Study Management" is an explicitly named product area. Specific capabilities (participant rostering, adherence monitoring, multi-site support, role-based access) were not independently verified against current documentation this session.

## Data Access and Export

- Per the vendor's own "Data Access & Analytics" page, study data are processed and made available "minutes after upload" from participants, accessible either by direct download or through analysis tools in the researcher dashboard. Supported export formats include **CSV and JSON**, plus format-specific outputs for particular data types, **GEXF for network graphs, KML for location data**, a level of export-format specificity not found on most competitors' public pages in this module. **Corroborated** from the vendor's own feature documentation, though this session did not independently test the export pipeline.
- The homepage once offered "Raw or processed sensor data", accessed "Via Avicenna Dashboard, or tools such as R or Jupyter" (read 2026-10-10). The site was redesigned by 2026-10-26 and that line is gone; the Sensor Data page now says collected data can be reviewed on the Researcher Dashboard, or queried and visualised through Avicenna's integrations [43] (re-read 2026-10-30).
- **Corrected 2026-10-11 (vendor fact record, export_routes, Verified).** A Data Export API exists. The 2026-10-10 line here said none did; that was wrong. See APIs, SDKs, and Extensibility.
- Export routes in the record. Researcher Dashboard export as a ZIP of CSV files (GPS also KML or GPX, Bluetooth beacons also GEXF), each export downloadable for 7 days [21]; in-dashboard Kibana querying and charts; the Data Export API [23]; direct database access on request [21], though an older forum answer says only for self-hosted deployments [36]. Participants can ask support for a machine-readable copy of their own data.
- Export limits: about 5 GB uncompressed per export and 100 stored exports per study [21]. No API request rate limit is published (not public, 2026-10-11).
- History: data is collected from study participation onward; Fitbit daily summaries dated before the study start are excluded [34]. No backfill of pre-enrolment history is documented for any source (Corroborated, inferred from the documentation). SensorKit data becomes exportable about 30 hours after collection [27].

## APIs, SDKs, and Extensibility

- **Re-confirmed 2026-08-25 (second pass).** Direct fetch of both `avicennaresearch.com`'s homepage and `avicennaresearch.dev/features/data-access-and-analytics/` again found no mention of a developer/public API, this session's targeted search for Avicenna API documentation also returned nothing. The absence is now corroborated by two independent direct fetches plus a dedicated search rather than a single pass, strengthening (not just repeating) the "not confirmed" status, data access still appears to be dashboard/export-mediated (CSV, JSON, GEXF, KML) rather than API-mediated. White-label solutions remain named as a product offering, implying some degree of platform customization is available commercially.
- **Updated 2026-10-10:** the vendor's public roadmap lists "Export Data with API" (forum topic 1406, created 2025-09-29) in the "To Do" category, to follow "OpenAPI Compatible APIs". This was read at the time as confirming no API existed; see the 2026-10-11 correction below.
- **Corrected 2026-10-11 (vendor fact record, developer_program_status and export_routes, Verified).** A Data Export API for sensor data is documented in a how-to article posted 2026-02-09 [23]. Researchers request an API key from support, tied to their researcher account. The flow is a POST to `/api/study/export/create/`, polling GET `/api/v1/filter/export/`, then download, with the header `Authorization: ApiKey USERNAME:API_KEY`. There is no full API reference and no self-serve developer program. The roadmap card predates the article and is still under To Do; it most likely covers a fuller, OpenAPI-style API, but the card does not say so.
- The open-source NiDB importer (commits to 2026-08-27) also posts a participation filter to `/api/v1/filter/export/` to export survey participation records [42]. The vendor does not document this use (inferred, not documented).
- Proprietary, closed source; the company GitHub organisation holds only an EMA software comparison list, no platform code [44].
- Deprecations and migrations (vendor fact record, Verified 2026-10-11) [35][34]
  - App IDs still carry "ethica" after the rebrand.
  - App Usage (Legacy) is closed to new studies.
  - Some GraphQL endpoints were replaced by REST (2023-10).
  - The WHOOP integration moved to WHOOP API v2 after v1 was deprecated (2025-11).
  - Fitbit participants must move to Google Accounts; legacy Fitbit accounts can no longer sync.

## Deployment and Infrastructure

- **Re-confirmed 2026-08-25 (second pass, direct fetch of `avicennaresearch.com`).** Vendor-hosted SaaS; no self-hosting option identified on the homepage. Deployment model requires no researcher-side infrastructure, in contrast to Beiwe/RADAR-base/AWARE's self-hosting orientation, the tradeoff being reliance on the vendor's cloud rather than researcher-controlled infrastructure.
- **Corrected 2026-10-11 (vendor fact record, hosting_options, Verified).** The default is the managed cloud service. The white-label option offers installation models "from in-house storage to a fully on-premises deployment"; in-house storage keeps the database on the customer's own infrastructure and is, per the vendor, the only arrangement that gives researchers direct database access [28] (wording re-read 2026-10-30). On-premise deployments are in use: a product card plans per-organisation login pages for on-premise subdomains, and a 2026-09-22 Garmin SDK post routes data to "an institution's own Avicenna infrastructure where applicable" [26][29]. This is vendor-installed closed-source software on customer infrastructure, not self-hosting from open source.
- Managed hosting is bundled into the study licence. On-premises and white-label prices are not published (not public, 2026-10-11) [28].

## Participant Experience

- The participant app is free on the App Store and Google Play and needs iOS 16.0+ or Android 10.0+ [39]. Participants using only the web app cannot contribute phone-sensor data [22].
- One field deployment shows the data-completeness risk. A 2025 JMIR mHealth study in rural South Africa used a customised Android app (Sesikhona), collected GPS every 30 minutes and got on average 95.3 of the expected 336 points (28.4%) per week, with frequent app terminations [31].
- Participants can delete all or part of their data at any time [17].

### Background keepalive (added 2026-10-09)

- No phone-app keepalive was found. Notification triggers cover participation events (invited, joined), activity-session events (released, completed, canceled, expired), appointments (scheduled, started, canceled), and a "Sensor Data Gap Detected" trigger that the server checks every 15 minutes (default threshold 1 hour, default minimum gap between notifications 4 hours), currently limited to the Garmin Health SDK Logged Wrist Status data source. Nothing fires when the phone app itself stops sending. **Verified 2026-10-10** from the Notifications reference (forum.avicennaresearch.com/t/notifications/1277, posted 2025-06-16), read directly.
- Researchers get monitoring instead. The Participation page shows an "In Operation" percentage (share of time the app was running and collecting sensor data) and a Last Recorded Data Time per participant. "Reload Devices" sends a message to participants' devices to pull new study settings. That is a configuration sync, not a keepalive, and the periodic sync otherwise "can take about 30 days".
- Status: **Corroborated** absence of a phone-app keepalive, from the Participation reference (dated 2025-06-16) and the Notifications reference, read 2026-10-09 and 2026-10-10. Sources 12 and 13.

## Privacy, Security, and Compliance

- **Corrected 2026-10-10.** The 2026-08-25 pass rated the ISO 27001 statement Verified and "independently audited". The evidence read is the vendor's own: the legal page says "ISO 27001:2022 certified infrastructure", "Certified November 2024 with zero nonconformities" and a November 2025 surveillance audit, and names no certification body or certificate number. The vendor's Security and Compliance forum post (updated 2025-11-08) says the certification was achieved "through UKAS" and links a UKAS CertCheck entry (https://certcheck.ukas.com/certified-entity/adc99141-1f0e-5832-951d-c9b4c1682be7), but that page sits behind a CAPTCHA and was not read. The claim is therefore **Corroborated (vendor-stated, with a registry link not read)**, not Verified. "Certified infrastructure" may also refer to the hosting provider rather than Avicenna's own management system.

- **ISO 27001:2022 certification stated by the vendor** (certified Nov 2024, surveillance audit Nov 2025, zero nonconformities, per its legal page), plus "AES-256 encryption at rest, TLS 1.2+ for data in transit, and full disk encryption". Avicenna is also on the UK ICO register of fee payers (ZC009135, registered 2025-10-07, expires 2027-10-06), which is a registration, not a certification. **Corroborated.**
- **Data residency: conflicting documentation (vendor fact record, data_residency, Unclear, 2026-10-11).** The security post says all data is on servers physically in Canada, with all staff in Canada [16], and the privacy policy says information may be stored on servers in Canada [17]. The privacy policy's children's-data section says UK/EEA data is processed and stored within the UK/EEA unless safeguards are in place, and the legal page claims an "infrastructure-agnostic approach" to residency [17]. The security post also lists AWS EC2 instances with no region [16]. A "Server Region" product card (created 2025-05-21) is filed under To Do but reads "Closed epic", which settles nothing [37]. On-premises installation is the documented route to local residency (see Deployment).
- **NHS DSPT.** Entry AVRESC001 shows a published 2025-26 self-assessment marked "Standards met" (25 November 2025) [33]. This is a self-assessment against NHS data-security standards, not an audit; the security post calls it a "certification", which overstates it. Neither the DSPT nor the ICO entry is evidence of ISO certification or of GDPR compliance.
- **HIPAA**: the legal page addresses the HIPAA Privacy Rule and Security Rule in the context of minors' Protected Health Information, and lists HIPAA Security Rule safeguards "where applicable". **Updated 2026-10-11 (vendor fact record, hipaa_statement, Corroborated):** the SensorKit approval guide also says Avicenna "maintains compliance with GDPR, PIPEDA, HIPAA, FDA 21 CFR Part 11, and ISO 27001" [27], a blanket self-described compliance claim. No independent HIPAA attestation was found.
- **BAA unclear (vendor fact record, baa, 2026-10-11).** The privacy policy says HIPAA requires Business Associate Agreements for covered transactions and offers "HIPAA compliance documentation (where applicable)" [17], but no page says Avicenna signs BAAs with US covered entities. Ask the vendor.
- **GDPR / UK GDPR / PIPEDA**: the page references "UK GDPR Article 8" (parental consent) and general EU GDPR compliance, plus PIPEDA (Canada) consent requirements for children under 13. The security post says Avicenna complies with GDPR as a data processor [16].
- **Data Processing Agreements**: described as addressing enhanced security requirements, audit rights, approved sub-processors, breach-notification procedures, and data return/deletion obligations. The security post says multiple European institutions have controller-processor agreements with Avicenna in place [16]. No DPA template is published (Corroborated, 2026-10-11).
- **Retention (vendor fact record, retention_terms, Verified).** After contract termination Avicenna keeps data for at least two years unless immediate deletion is requested, then deletes it unless law requires retention [17]. Trial study data is wiped monthly and the study deleted after a year [15]; export files are deleted after 7 days [21].
- **AI training terms not public (2026-10-11).** Neither the privacy policy nor the terms mention AI or machine-learning training. An experimental LLM survey chatbot is announced on the forum but not yet on the dashboard; its model provider and data flow are not stated.
- **No FDA record.** openFDA searches on 2026-10-11 returned no 510(k) or registration record for Avicenna Research or Ethica [38]. The platform makes no clearance claim; its Part 11 claim concerns electronic records, not clearance.
- **What is still not confirmed**: no standalone Security Policy or DPA template document was found linked from this page, and SOC 2 is not mentioned anywhere read (not public, 2026-10-11). 21 CFR Part 11 is not on the legal page or the security post, but the SensorKit approval guide claims it (corrected 2026-10-11). Treat the ISO 27001:2022 statement and the HIPAA/GDPR/PIPEDA/Part 11 language alike as **Corroborated** (specific and dated, but vendor-stated; no certificate read). "Through UKAS" names no certification body; UKAS accredits certification bodies and does not certify companies.

- This resolves the bulk of unresolved-question #84 for Avicenna Research at the vendor-statement level. MetricWire also publishes ISO 27001 and SOC 2 Type II statements (see its profile), equally without a certificate read, so Avicenna is not the only Module 2 platform with a stated certification.

## Pricing

- Pricing remains non-public: there is no pricing page (avicennaresearch.com/pricing returns 404, checked 2026-10-10). The vendor's own FAQ (forum.avicennaresearch.com/t/5, updated 2026-08-03) describes the trial: free of charge, full access to the default features, no participant limit, "intended only for test purposes", collected study data "wiped monthly", and the study deleted after one year. Field research with real participants needs the full licence; upgrade by emailing support@avicennaresearch.com with the study ID. **Verified 2026-10-10.** No academic or non-profit rate was found. The 2026-08-25 note relied on third-party directories (Capterra, SoftwareAdvice) describing an "unlimited" trial; the vendor's terms make clear it is a test environment, not a free tier.
- **Added 2026-10-11 (vendor fact record).**
- No separate academic or research programme exists. The platform itself is sold to researchers. Sign-up is self-serve (name, organisation, email, password; email verified before a study can be created) [40]. The privacy policy defines a Researcher as someone affiliated with an academic institution [17], while the homepage markets clinical as well as behavioral and real-world studies. Whether non-academic customers are excluded is not stated (Corroborated). No academic versus commercial terms or price difference is published.
- Licence fees and any overage fees are set in separate "Specific Conditions" referred to by the terms; for services billed per study, old pricing applies until the end of studies already defined [17]. No minimum term, study count or participant minimum is published (not public, 2026-10-11). No separate API fee is mentioned.
- SMS notifications are off by default and, if enabled through support, are billed at Twilio's per-message cost plus a 30% markup, including leased-number fees; in-app and email notifications carry no such charge [32].
- Studies using Apple SensorKit also need a per-study Apple entitlement, applied for by the institution, for which Avicenna builds a separate app [27].

## Research Evidence and Validation

- The platform has an academic research lineage as "Ethica/iEpi," described in its originating academic materials (University of Saskatchewan, cs.usask.ca) as an "industrial strength and flexible smartphone-based epidemiological sensing, crowdsourcing and Ecological Momentary Assessment system", indicating the platform predates its current commercial packaging and has an independent academic development history distinct from being purely a startup product. This session did not attempt a systematic count of peer-reviewed studies using Ethica/Avicenna.

## Strengths

- Broad, clinically-oriented active-assessment feature set (cognitive/behavioral tasks, TeleVisit, outcome assessment) beyond passive sensing alone, a different value proposition than academic open-source competitors.
- Specific, named export-format support (CSV, JSON, GEXF for network data, KML for location data) suggests real engineering investment in researcher-usable data delivery.
- Data made available to researchers within minutes of participant upload, per the vendor's own materials, a notably fast latency claim relative to platforms with less-documented sync behavior.
- Academic origin (Ethica/iEpi, University of Saskatchewan) gives the platform a longer track record than a purely commercial startup.
- White-label is a working service, not just a listed option: 33 further iOS apps under Avicenna Research Inc. on 2026-10-11 [30], with on-premises installation available on customer infrastructure [28].
- A documented sensor catalogue covering phone sensors, the Garmin Health SDK at 25 Hz and SensorKit [21][26][27].
- A specific, dated vendor compliance statement: ISO 27001:2022 certification stated (Nov 2024, surveillance audit Nov 2025, zero nonconformities), with a UKAS CertCheck link, plus detailed HIPAA/GDPR/PIPEDA language addressing minors' data. **Corroborated (vendor-stated)**; the certificate itself was not read (corrected 2026-10-10).

## Limitations

- Commercial and closed-source, with no self-hosting from source or code-level customization path, unlike Beiwe/RADAR-base/AWARE/CARP. On-premises installation exists only as a vendor-installed white-label deployment, priced by quote (corrected 2026-10-11) [28].
- Full pricing is non-public. The only free route is a test-only trial (data wiped monthly), so there is no free path for real field research (vendor FAQ, Verified 2026-10-10).
- The export API is thin. A Data Export API for sensor data is documented only at how-to level (2026-02-09), with the key issued by support and no full API reference or published rate limits [23]. A fuller API ("Export Data with API", forum topic 1406) is still on the "To Do" roadmap (corrected 2026-10-11; the 2026-10-10 line said no export API existed).
- ~~Compliance documentation (HIPAA/GDPR/Part 11) was not independently verified this session~~. Partly resolved 2026-08-25 and corrected 2026-10-10: the vendor states ISO 27001:2022 certification (Nov 2024, surveillance audit Nov 2025) and gives detailed HIPAA/UK-GDPR/PIPEDA language, all Corroborated (vendor-stated). SOC 2 is not mentioned anywhere read. 21 CFR Part 11 is claimed in the SensorKit approval guide, vendor-stated (corrected 2026-10-11) [27]. Whether Avicenna signs a BAA is unclear.
- Data residency for the managed service is conflicting documentation (Canada versus UK/EEA statements, 2026-10-11).
- The Ethica-to-Avicenna rebrand means older published literature citing "Ethica" may not obviously connect to the current company/product name for researchers doing their own literature search, worth flagging explicitly to anyone cross-referencing this profile against older papers.

## Best-Fit Use Cases

- Clinical-trial-style studies needing outcome assessment, cognitive/behavioral tasks, and passive sensing in one commercial, no-infrastructure-required platform.
- Teams wanting fast (minutes-scale) data availability after participant upload without building their own pipeline.
- Studies needing network-graph (GEXF) or location-specific (KML) export formats out of the box.

## Poor-Fit Use Cases

- Teams requiring self-hosting from source or source-code-level auditability, not offered. Full data custody is possible only through a vendor-installed on-premises deployment at an unpublished price (corrected 2026-10-11) [28].
- Teams needing a fully documented public API for real-time third-party integration. Only a how-to-level sensor-data export API exists, with the key issued by support (corrected 2026-10-11) [23].
- Budget-constrained academic pilots needing firm, public pricing before committing, pricing requires vendor contact.

## Open Questions

- *(Directed to: Avicenna Research, https://avicennaresearch.com/ , https://avicennaresearch.dev/)*

- What is current, non-trial pricing (per-participant, per-study, or subscription), and is academic/non-profit pricing available?, still unresolved after a second, dedicated search.
- ~~Is there a documented developer API distinct from the dashboard/export mechanism?~~ Answered 2026-10-10 as no, which was wrong. **Corrected 2026-10-11:** yes, a Data Export API for sensor data, documented at how-to level since 2026-02-09, key on request from support [23]. Still open: whether the undocumented participation-export use of `/api/v1/filter/export/` is supported for all licences.
- ~~What HIPAA, GDPR/DPA, SOC 2, or 21 CFR Part 11 compliance documentation exists?~~ **Largely resolved**, see Privacy, Security, and Compliance above (ISO 27001:2022, HIPAA/GDPR/PIPEDA and a Part 11 claim, all Corroborated as vendor statements, 2026-10-11). Still open: the certificate's scope, number and certification body (the UKAS CertCheck page needs a CAPTCHA), SOC 2, and whether Avicenna signs BAAs.
- Where is UK/EEA study data stored, and which AWS region do the EC2 instances use? Opened 2026-10-11 from the data-residency conflict.
- What is the exact current sensor/wearable integration catalog, and how does iOS coverage compare with Android? Partly answered 2026-10-11 from the Raw Data reference [21]; which sources are Android-only is still open.
- Under what circumstances is the "white-label" option available, and at what additional cost? Partly answered 2026-10-11: white-label is a working service with many live study apps and an on-premises option [28][30]; cost is still not published.

## Vendor Fact Record

<!-- facts:begin -->
*Generated from the fact record by `tools/facts/generate.py`. Edit the record, not this block.*

**Research access**

| Fact | Value |
|---|---|
| Formal research or academic program (name, what it offers) | No separate academic or research program; the platform itself is sold to researchers. Each study starts on a free Trial licence (full default features, no participant cap, for testing only) and must be upgraded to a paid full licence before field research with real participants. [V, 2026-10-11] |
| Who can join the research program | Open self sign-up for a researcher account (name, organization, email, password; email must be verified before a study can be created). The privacy policy defines a Researcher as someone affiliated with an academic institution, and the terms require account holders to be at least 18. Whether non-academic customers are excluded is not stated, and the homepage markets clinical as well as behavioral and real-world studies. [C, 2026-10-30] |
| How to apply, and any approval or review step | Self-serve sign-up creates Trial studies. Moving a study from Trial to Licensed is done by emailing support with the study ID; a demo can be booked. No review or approval criteria are published. Studies using Apple SensorKit also need a per-study Apple entitlement, applied for by the institution, for which Avicenna builds a separate app. [V, 2026-10-11] |
| Whether the program is active, paused, renamed or closed | Active. Self sign-up and the free Trial are open and weekly release notes continue (latest read 2026-10-06). Renamed from Ethica Data to Avicenna Research in 2023-2024; the Ethica name was to be dropped by July 2024. [V, 2026-10-24] |
| Whether the general developer or API program is open to new applicants | No public self-serve developer program. A Data Export API exists and is documented in a how-to article (posted 2026-02-09); researchers request an API key from support, tied to their researcher account. There is no full API reference. A Product Ideas card "Export Data with API" (2025-09-29), to follow "OpenAPI Compatible APIs", is still filed under To Do. [V, 2026-10-11] |
| Participant or user limits before approval or by tier | The free Trial licence has no participant-number limit, but trial data is wiped monthly and the study deleted after one year. No caps are published for licensed studies. [V, 2026-10-11] |
| How academic access differs from commercial or consumer access | Not public [2026-10-11] |

**Pricing**

| Fact | Value |
|---|---|
| Device or hardware list price | n/a |
| Consumer subscription or membership price | n/a |
| Research or academic pricing or discount | Not public [2026-10-11] |
| Fees for API, SDK, platform or data access | Licence fees are not published (Trial is free; the paid licence is arranged by email). The terms refer to fees and overage fees set in separate Specific Conditions. No separate API fee is mentioned. SMS notifications are off by default and, if enabled through support, are billed at Twilio's per-message cost plus a 30% markup, including leased-number fees; in-app and email notifications carry no such charge. [V, 2026-10-30] |
| Minimum order, term or commitment | Not public [2026-10-11] |
| Whether pricing requires contacting sales | Yes. No public price list (the /pricing page returns 404). A study is upgraded to a paid licence by emailing support with the study ID, or through a demo booking; the terms describe some services as billed per study. [V, 2026-10-30] |
| Price of managed hosting | Not public [2026-10-11] |

**Data access and terms**

| Fact | Value |
|---|---|
| Raw signals available to researchers, and by which route | Raw phone sensors through the Avicenna app (accelerometer, gyroscope, magnetic field, light, pressure, proximity, GPS, Wi-Fi, Bluetooth and beacons, battery, screen state, app usage, keyboard, web activity), with many sources Android-only; iOS app usage via hourly Screen Time summaries (added 2026-04). Garmin Health SDK raw watch data (25 Hz accelerometer, 32 Hz gyroscope, beat-to-beat intervals and more). Apple SensorKit streams including ECG and PPG, on approved studies with a custom app. Cloud data from Fitbit, Garmin Health API, Oura, WHOOP, Polar, HealthKit, Hexoskin and Mira. Exported via the dashboard, Kibana or the Data Export API. [V, 2026-10-30] |
| Derived or processed metrics available to researchers | Phone-derived step counts and other activity information; vendor-computed wearable metrics pulled from cloud accounts (Garmin, Fitbit, Oura readiness and sleep, WHOOP recovery, Polar sleep). An Analysis page for data quality, engagement and retention (added 2026-03). Kibana and Vega charts in the dashboard. Whether Avicenna still computes GPS mobility features is unclear (see note). [V, 2026-10-30] |
| Documented sampling rates or temporal resolution | Phone sensors are polled once per data-collection cycle, every 5 minutes by default, configurable from 1 to 60 minutes (iOS honours the interval, Android may not). Burst sources sample for a fixed window per cycle (accelerometer 60 seconds; GPS cycles stay active 60 seconds). Garmin Health SDK accelerometer 25 Hz, gyroscope 32 Hz, heart rate or SpO2 configurable from 1 second to 1 hour. SensorKit motion downsampled to 32 Hz. Cloud wearable data is fetched daily; Fitbit intraday activity is 1-minute, Garmin Health API 15-minute slices. [V, 2026-10-11] |
| How far back data can be retrieved | Data is collected from study participation onward; Fitbit daily summaries dated before the study start are excluded. No backfill of pre-enrolment history is documented for any source. SensorKit data becomes exportable about 30 hours after collection. [C, 2026-10-11] |
| Export, API, SDK or file routes | Researcher Dashboard export (ZIP of CSV; GPS also KML/GPX, Bluetooth Beacon also GEXF; the marketing page also names JSON), each file downloadable for 7 days. In-dashboard Kibana querying and charts. A Data Export API for sensor data: POST to /api/study/export/create/, poll GET /api/v1/filter/export/, header "Authorization: ApiKey USERNAME:API_KEY", key issued by support. Direct database access on request (an older forum answer says only for self-hosted deployments). Participants can ask support for a machine-readable copy of their own data. [V, 2026-10-11] |
| API rate limits | Not public [2026-10-11] |
| Terms on retaining, storing or deleting data | After contract termination Avicenna keeps data for at least two years unless immediate deletion is requested, then deletes it unless law requires retention. Trial-licence study data is wiped monthly and the study deleted after a year. Export files are deleted after 7 days. Participants can delete all or part of their data at any time. [V, 2026-10-30] |
| Terms on using data to train AI or ML models | Not public [2026-10-11] |
| Announced shutdowns, deprecations or migrations, with dates | Rebrand from Ethica Data to Avicenna Research, the Ethica name dropped by July 2024 (app IDs still carry "ethica"). App Usage (Legacy) closed to new studies. Some GraphQL endpoints replaced by REST (2023-10). WHOOP integration moved to WHOOP API v2 after v1 was deprecated (2025-11). Fitbit participants must move to Google Accounts; legacy Fitbit accounts can no longer sync. [V, 2026-10-11] |
| Software licence of the platform's components | Proprietary, closed source. The terms say all service software is the property of Avicenna Research or its software providers; the company GitHub organisation holds only an EMA software comparison list, no platform code. [V, 2026-10-30] |
| Self-hosting and managed-hosting options | Default: managed cloud service run by Avicenna. White-label option: rebranded apps, with installation ranging from in-house data storage (the database kept in the customer's own infrastructure, the only arrangement that gives researchers direct database access) to a full on-premises installation of the (closed-source) Avicenna services on the customer's infrastructure. On-premise deployments are in use: a product card plans per-organisation login pages for on-premise subdomains, and the 2026-09-22 Garmin SDK post routes data to "an institution's own Avicenna infrastructure where applicable". Terms and prices are not published. [V, 2026-10-30] |
| App store availability on iOS and Android | Participant app "Avicenna Research" is free on the iOS App Store (id1137173052, Avicenna Research Inc.) and Google Play (com.ethica.logger). Requires iOS 16.0+ or Android 10.0+ (raised from Android 9.0+ by 2026-10-26). A web app supports surveys and cloud wearables but no phone sensors. White-label study apps are a working service: on 2026-10-11 the App Store listed 33 further iOS apps under Avicenna Research Inc. (32 study-branded apps plus Avicenna Keyboard), and a 2025 JMIR mHealth paper used a customised Android app (Sesikhona). [V, 2026-10-30] |

**Compliance and regulatory**

| Fact | Value |
|---|---|
| Whether a HIPAA Business Associate Agreement is offered | Unclear |
| Whether a data processing agreement is offered | Yes. Avicenna acts as data processor and says multiple European institutions have controller-processor agreements with it; the privacy policy describes DPA contents (security, audit rights, sub-processors, breach notice, return or deletion). No DPA template is published. [C, 2026-10-30] |
| Published HIPAA statement | Self-described HIPAA compliance, with HIPAA Security Rule safeguards "where applicable". A forum guide also claims compliance with GDPR, PIPEDA, HIPAA, FDA 21 CFR Part 11 and ISO 27001. No independent HIPAA attestation found. [C, 2026-10-30] |
| Published GDPR statement | Says it complies with GDPR as a data processor. Two independent register entries exist, neither of which establishes GDPR compliance or ISO certification. UK ICO register of fee payers ZC009135 (registered 2025-10-07, expires 2027-10-06) shows only that Avicenna has registered and paid the UK data-protection fee. The NHS DSPT entry AVRESC001 shows a published 2025-26 self-assessment marked "Standards met" (25 November 2025), so it records a self-assessment against NHS data-security standards, not an audit. [C, 2026-10-11] |
| ISO/IEC 27001 status and evidence | Self-claimed ISO/IEC 27001:2022 certification "through UKAS", certified November 2024, with a November 2025 surveillance audit. No certificate, certificate number or certification body is published (UKAS accredits certification bodies; it does not certify companies). [C, 2026-10-30] |
| SOC 2 status and evidence | Not public [2026-10-11] |
| FDA clearances, from the FDA database | Not public [2026-10-11] |
| Where data is stored, and residency options | The security page says all data is on servers physically in Canada, with all staff in Canada, and the privacy policy says information may be stored on servers in Canada. The privacy policy's children's-data section says UK/EEA data is processed and stored within the UK/EEA unless safeguards are in place, and the same policy claims an "infrastructure-agnostic approach" to residency. The security page also lists AWS EC2 instances with no region. On-premises installation (see hosting_options) is the documented route to local residency. (conflict) [U, 2026-10-30] |

<!-- facts:end -->

## Key Links

- Official site (current brand): https://avicennaresearch.com/
- Product/feature documentation: https://avicennaresearch.dev/
- Data Access & Analytics feature page: https://avicennaresearch.dev/features/data-access-and-analytics/
- App Store listing: https://apps.apple.com/us/app/ethica-avicenna/id1137173052 (now titled "Avicenna Research", checked 2026-10-10)
- Trial terms FAQ: https://forum.avicennaresearch.com/t/5
- Security and compliance post: https://forum.avicennaresearch.com/t/security-and-compliance/1267
- Google Play listing: https://play.google.com/store/apps/details?id=com.ethica.logger
- Raw Data reference (stream list, export formats and limits): https://forum.avicennaresearch.com/t/raw-data/1241
- Data Export API guide: https://forum.avicennaresearch.com/t/how-to-export-study-data-using-the-api/1496
- White-label solutions: https://avicennaresearch.com/features/white-label-solutions
- Legal documents (index): https://avicennaresearch.com/legal
- Privacy policy: https://avicennaresearch.com/legal/privacy-policy/
- Terms of use: https://avicennaresearch.com/legal/terms-of-use/
- Release notes: https://forum.avicennaresearch.com/c/release-notes/6
- Contact: support@avicennaresearch.com

## Sources

1. Avicenna Research, official site. https://avicennaresearch.com/ (accessed 2026-08-24, search summary). **Primary.** Current company identity, rebrand from Ethica Data.
2. Avicenna Research (Ethica Data), product documentation site. https://avicennaresearch.dev/ (accessed 2026-08-24, search summary). **Primary.** Named feature areas (Outcome Assessment, TeleVisit, Cognitive and Behavioral Tasks, Sensor-based Data, Study Management, Data Access & Analytics, White-Label Solutions).
3. Avicenna Research, "Data Access & Analytics." https://avicennaresearch.dev/features/data-access-and-analytics/ (accessed 2026-08-24, search summary). **Primary.** Export formats (CSV, JSON, GEXF, KML), "minutes after upload" latency claim.
4. App Store listing, "Avicenna (Ethica)." https://apps.apple.com/us/app/ethica-avicenna/id1137173052 (accessed 2026-08-24). Confirms the Ethica/Avicenna naming continuity.
5. Google Play listing, "Avicenna Research." https://play.google.com/store/apps/details?id=com.ethica.logger (accessed 2026-08-24). Package name `com.ethica.logger` further corroborates continuity between Ethica and Avicenna.
6. Ethica/iEpi academic project page, University of Saskatchewan. https://www.cs.usask.ca/~osgood/iEpi/iEpi.html (accessed 2026-08-24, search summary). Academic origin as an epidemiological sensing/EMA system.
7. CB Insights, Avicenna Research company profile. https://www.cbinsights.com/company/ethica-data (accessed 2026-08-24, search summary). Corroborates the Ethica-to-Avicenna corporate continuity.
8. Third-party pricing/trial characterization: Capterra, SoftwareAdvice, SoftwareWorld listings (accessed 2026-08-24, search summary), **Reported**, not vendor-verified: free-trial characterization.
9. Avicenna Research, homepage (second-pass direct re-fetch). https://avicennaresearch.com/ (accessed 2026-08-25). **Primary/Direct.** Re-confirms no pricing, no developer API, no self-hosting mentioned; references security/compliance without naming frameworks on this specific page.
10. Avicenna Research, "Legal Documents." https://avicennaresearch.com/legal/ (accessed 2026-08-25, second pass). **Primary, vendor-stated** (relabelled from Verified on 2026-10-10: no certification body or certificate number on the page). ISO 27001:2022 certification (certified Nov 2024, zero nonconformities; surveillance audit Nov 2025, zero nonconformities), AES-256 encryption at rest, HIPAA Privacy/Security Rule language for minors' PHI, UK GDPR Article 8, EU GDPR, PIPEDA, DPA scope description. Resolves the majority of unresolved-question #84 for this platform.
11. Avicenna Research, "Data Access & Analytics" (second-pass direct re-fetch). https://avicennaresearch.dev/features/data-access-and-analytics/ (accessed 2026-08-25). **Primary/Direct.** Re-confirms export formats (CSV, JSON, GEXF, KML); no developer API mentioned.
12. Avicenna Research, "Participation" reference. https://forum.avicennaresearch.com/t/participation/1280 (redirected from learn.avicennaresearch.com; accessed 2026-10-09). **Primary/Direct.**
13. Avicenna Research, "Notifications" reference. https://learn.avicennaresearch.com/reference/study-setup-and-deployment/notifications (accessed 2026-10-09, search summary).
14. Avicenna Research, "Notifications" reference, direct read. https://forum.avicennaresearch.com/t/notifications/1277 (accessed 2026-10-10). **Primary/Verified.** Participation, Activity, Appointment and Sensor Data Gap Detected triggers; gap check every 15 minutes, limited to Garmin Health SDK wrist status.
15. Avicenna Research, "Frequently Asked Questions" (trial terms). https://forum.avicennaresearch.com/t/5 (post updated 2026-08-03; accessed 2026-10-10). **Primary/Verified.** Free test-only trial, monthly data wipe, deletion after one year, upgrade by email.
16. Avicenna Research, "Security and Compliance" forum post. https://forum.avicennaresearch.com/t/security-and-compliance/1267 (updated 2025-11-08; accessed 2026-10-10). **Primary, vendor-stated.** ISO 27001:2022 "through UKAS", GDPR processor status, Canadian data storage; links a UKAS CertCheck entry that could not be read (CAPTCHA). No SOC 2 or Part 11.
17. Avicenna Research, "Legal Documents" (re-read). https://avicennaresearch.com/legal/ (accessed 2026-10-10). **Primary, vendor-stated.** Same ISO wording as source 10; no certification body or certificate number; no SOC 2 or Part 11. Since the 2026-10 site redesign this URL is an index; the texts are at https://avicennaresearch.com/legal/privacy-policy/ (privacy policy, updated 2026-08-22) and https://avicennaresearch.com/legal/terms-of-use/ (terms, updated 2025-11-17), where every quote in the fact record was re-read on 2026-10-30.
18. Avicenna Research, product roadmap topic "Export Data with API". https://forum.avicennaresearch.com/t/1406 (created 2025-09-29; accessed 2026-10-10). **Primary/Verified.** Filed under "To Do".
19. App Store (iTunes lookup id 1137173052) and Google Play (`com.ethica.logger`) listings, direct fetch 2026-10-10. **Primary/Verified.** iOS v1065 released 2026-10-07; Android updated 2026-09-05.
20. UK ICO register of fee payers, entry ZC009135. https://ico.org.uk/ESDWebPages/Entry/ZC009135 (accessed 2026-10-10). **Primary.** Registration only.
21. Avicenna Research, "Raw Data" reference. https://forum.avicennaresearch.com/t/raw-data/1241 (accessed 2026-10-11, vendor fact record). **Primary/Verified.** Data-source list including SensorKit ECG and PPG and Oura, WHOOP and Polar metrics; ZIP of CSV, KML, GPX and GEXF exports; 7-day download window; export size limits; direct database access on request.
22. Avicenna Research, "Data Sources" reference. https://forum.avicennaresearch.com/t/data-sources/1266 (accessed 2026-10-11, vendor fact record). **Primary/Verified.** Collection cycle 5 minutes by default, 1 to 60 minutes custom; 60-second accelerometer burst; daily cloud fetch; web-app participants contribute no phone-sensor data.
23. Avicenna Research, "How to export study data using the API." https://forum.avicennaresearch.com/t/how-to-export-study-data-using-the-api/1496 (posted 2026-02-09; accessed 2026-10-11, vendor fact record). **Primary/Verified.** Data Export API for sensor data, key from support, create, status and download endpoints.
24. Avicenna Research, GPS mobility features reference https://forum.avicennaresearch.com/t/1460 (read 2026-10-11; 404 since 2026-10-19, so **Unclear**) and Analysis page announcement https://forum.avicennaresearch.com/t/1508 (accessed 2026-10-11, vendor fact record; **Primary/Verified**, Analysis page added 2026-03). See `facts/avicenna.yaml`, `derived_metrics` note.
25. Avicenna Research, iOS app usage announcement. https://forum.avicennaresearch.com/t/1512 (accessed 2026-10-11, vendor fact record). **Primary/Verified.** Hourly Screen Time usage summaries on iOS.
26. Avicenna Research, "Garmin Health SDK" reference https://forum.avicennaresearch.com/t/garmin-health-sdk/1261 and Garmin SDK post https://forum.avicennaresearch.com/t/1645 (2026-09-22) (accessed 2026-10-11, vendor fact record). **Primary/Verified.** 25 Hz accelerometer, 32 Hz gyroscope, heart rate or SpO2 sampling from 1 second to 1 hour; data routed to an institution's own Avicenna infrastructure where applicable.
27. Avicenna Research, "SensorKit" reference https://forum.avicennaresearch.com/t/sensorkit/1290 and "SensorKit approval" guide https://forum.avicennaresearch.com/t/sensorkit-approval/1563 (accessed 2026-10-11, vendor fact record). **Primary.** Per-study Apple entitlement, separate app, 32 Hz downsampling, about 30 hours to export; vendor-stated compliance with GDPR, PIPEDA, HIPAA, FDA 21 CFR Part 11 and ISO 27001.
28. Avicenna Research, "White-Label Solutions." https://avicennaresearch.com/features/white-label-solutions (accessed 2026-10-11, re-read 2026-10-30, vendor fact record). **Primary/Verified.** Installation models from in-house storage to a fully on-premises deployment; in-house storage is the only arrangement with direct database access for researchers; no price.
29. Avicenna Research, on-premise evidence. Comparison posts https://forum.avicennaresearch.com/t/1475 and https://forum.avicennaresearch.com/t/1225 ; product card https://forum.avicennaresearch.com/t/1009 (accessed 2026-10-11, vendor fact record). **Primary.** On-premise deployments offered and in use.
30. Apple App Store, developer page for Avicenna Research Inc. https://apps.apple.com/us/developer/avicenna-research-inc/id1137173051 and iTunes lookup for seller 1137173051 (accessed 2026-10-11, vendor fact record). **Primary/Verified.** 34 apps including the main app: 32 study-branded apps and Avicenna Keyboard (released 2025-12-16); 13 first released in 2026.
31. Sesikhona study, JMIR mHealth and uHealth 2025. https://doi.org/10.2196/67519 (full text via Europe PMC PMC12377519; accessed 2026-10-11, vendor fact record). **Peer-reviewed.** Customised Android app; 28.4% of expected weekly GPS points.
32. Avicenna Research, "How SMS notification costs are calculated." https://forum.avicennaresearch.com/t/how-sms-notification-costs-are-calculated/1540 (accessed 2026-10-11, vendor fact record). **Primary/Verified.** SMS off by default; Twilio cost plus 30% markup.
33. NHS Data Security and Protection Toolkit, organisation AVRESC001. https://www.dsptoolkit.nhs.uk/OrganisationSearch/AVRESC001 (accessed 2026-10-11, vendor fact record). **Primary (registry).** 2025-26 self-assessment, "Standards met".
34. Avicenna Research, wearable and location references. Fitbit https://forum.avicennaresearch.com/t/fitbit/1259 ; Garmin Health API https://forum.avicennaresearch.com/t/garmin-health-api/1260 ; Location https://forum.avicennaresearch.com/t/location/1255 (accessed 2026-10-11, vendor fact record). **Primary/Verified.** Fitbit 1-minute intraday data, pre-start summaries excluded, legacy Fitbit accounts no longer sync; Garmin 15-minute slices; 60-second GPS cycles.
35. Avicenna Research, rebrand and deprecation notices. "Our new brand and identity" https://forum.avicennaresearch.com/t/our-new-brand-and-identity/1120 ; "App Usage (Legacy)" https://forum.avicennaresearch.com/t/app-usage-legacy/1246 ; release notes 2023-10-16 https://forum.avicennaresearch.com/t/weekly-release-notes-2023-10-16/706 ; WHOOP v2 and ISO surveillance-audit release notes https://forum.avicennaresearch.com/t/1443 (accessed 2026-10-11, vendor fact record). **Primary/Verified.**
36. Avicenna Research, "Avicenna raw database software" forum answer. https://forum.avicennaresearch.com/t/avicenna-raw-database-software/800 (accessed 2026-10-11, vendor fact record). **Primary.** Direct database access only for self-hosted deployments (older answer).
37. Avicenna Research, "Server Region" product card. https://forum.avicennaresearch.com/t/1031 (created 2025-05-21; accessed 2026-10-11, vendor fact record). **Primary.** Under To Do, reads "Closed epic: OP-9223".
38. openFDA 510(k) and registration searches for "avicenna research" and "ethica". https://api.fda.gov/device/510k.json?search=applicant:%22avicenna+research%22 (and equivalents; run 2026-10-11, vendor fact record). **Primary (regulator).** No record.
39. Avicenna Research, "Participant app settings." https://forum.avicennaresearch.com/t/participant-app-settings/1278 (accessed 2026-10-11, re-read 2026-10-30, vendor fact record). **Primary/Verified.** iOS 16.0+ or Android 10.0+ (API level 29+); the page said Android 9.0+ on 2026-10-11.
40. Avicenna Research, "Step 1: Create a researcher account." https://forum.avicennaresearch.com/t/step-1-create-a-researcher-account/1160 (accessed 2026-10-11, vendor fact record). **Primary.** Self-serve sign-up and email verification.
41. Avicenna Research, weekly release notes 2026-10-06. https://forum.avicennaresearch.com/t/weekly-release-notes-2026-10-06/2188 (accessed 2026-10-11, vendor fact record). **Primary/Verified.** Platform active.
42. NiDB remote-import module. https://github.com/gbook/nidb/blob/master/src/nidb/moduleRemoteImport.cpp (accessed 2026-10-11, vendor fact record). **Third-party code.** Uses `/api/v1/filter/export/`, including an undocumented participation export.
43. Avicenna Research, "Sensor Data." https://avicennaresearch.com/features/sensor-data/ (re-read 2026-10-30, vendor fact record; the old /features/sensor-based-data URL redirects here). **Primary.** Motion data (acceleration, rotation, gravity), step counts and activity information, location, device context. The 2026-10-11 version said data could be accessed raw or processed in real time; the redesigned page does not.
44. Avicenna Research GitHub, `ema_software_map`. https://github.com/avicennaresearch/ema_software_map (accessed 2026-10-11, vendor fact record). **Primary.** The organisation's only content is an EMA software list; no platform code.
