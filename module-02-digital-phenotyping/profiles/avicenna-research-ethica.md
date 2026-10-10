# Avicenna Research (formerly Ethica / Ethica Data)

## Quick Facts

| Field | Details |
|---|---|
| Organization | Avicenna Research (rebrand of Ethica Data) |
| Category | Commercial mobile sensing, EMA, and clinical-trial data-capture platform |
| Current status | Active, under new name, the company rebranded from "Ethica Data" to "Avicenna Research" |
| Platforms/devices | iOS app ("Avicenna Research", App Store, v1065 released 2026-10-07) and Android app (`com.ethica.logger`, Google Play, updated 2026-09-05); web researcher dashboard. Checked 2026-10-10. |
| Open source | No |
| Hosting/deployment | Vendor SaaS only; data stored on servers in Canada (vendor-stated). No self-hosting. |
| Pricing model | Commercial licence, pricing not public. A free trial exists for testing only: trial data are wiped monthly and the study is deleted after one year, so real field research needs a paid licence (vendor FAQ, Verified 2026-10-10). No academic rate found. |
| Last verified | 2026-10-10 (independent-review corrections: compliance tier, trial terms, notifications, export API roadmap, app-store listings) |

## Summary

- Avicenna Research is the current name of the platform long known in the digital-phenotyping and EMA literature as **Ethica** (also referenced historically as "Ethica/iEpi," reflecting an earlier academic lineage at the University of Saskatchewan). It is a commercial, no-code-for-researchers platform combining survey/EMA delivery, cognitive and behavioral tasks, sensor-based passive data collection, wearable integration, and a data-access/analytics dashboard, explicitly positioned toward clinical-trial and health-research use, not just academic mobile sensing. The company markets under both names in different contexts (the app store listing reads "Avicenna (Ethica)"), so researchers searching prior literature for "Ethica" should expect to land on Avicenna's current materials.

- **Naming note handled carefully per CLAUDE.md's instruction to record rather than silently resolve ambiguity:** Ethica Data and Avicenna Research are the same corporate entity under two names, not two competing platforms, confirmed by the shared app-store listing ("Avicenna (Ethica)"), Avicenna's own site being hosted at a URL referencing "Ethica Data" in its page title, and Crunchbase/CB Insights profiles cross-referencing both names to the same company.

## Products / Platform Architecture

- **Avicenna app** (iOS/Android, listed as "Avicenna (Ethica)"), participant-facing data collection.
- **Researcher dashboard**, study design, participant management, data access and analytics.
- Named feature areas per the vendor's own site: Outcome Assessment, TeleVisit, Cognitive and Behavioral Tasks, Sensor-based Data, Study Management, Data Access & Analytics, White-Label Solutions.

## Sensors and Data Streams

- Every Module 2 profile uses the same table so platforms can be compared row by row. Rows are the passive streams named in `CLAUDE.md`. "Yes" and "No" are used only where a primary source says so; "Unclear" means nothing current was verified, and "No (OS)" means the operating system does not expose the stream to any third-party app. Confidence and sources are stated under the table. The convention is recorded in [`../../shared/profile-table-conventions.md`](../../shared/profile-table-conventions.md).

| Stream | Android | iOS | Raw or derived | Sampling configurable | Notes |
|---|---|---|---|---|---|
| GPS / location | Yes | Yes | Unclear | Unclear | The vendor names location capture and wearable integration. |
| Accelerometer | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Gyroscope | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Magnetometer | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Barometer | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Ambient light | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Proximity | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Device motion / activity recognition | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Screen state | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| App usage | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Battery / charging | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Network / connectivity | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Wi-Fi | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Bluetooth | Yes | Unclear | Raw. Beaconing used in the SHED studies. | Unclear | Qian 2024 removed iPhone users because Bluetooth beaconing did not work reliably on iOS. |
| Calls (metadata) | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| SMS (metadata) | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Keyboard | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Audio / microphone | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Notifications | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Device information | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |

**Verification.** The vendor states integration with "a wide range of smartphone sensors and wearables." The specific catalogue, sampling configurability and per-platform parity were not verified against developer documentation. The Bluetooth row comes from Qian et al. 2024, a Module 2 catalogue paper.

### Notes from earlier verification passes

- The vendor states integration with "a wide range of smartphone sensors and wearables that studies can use to objectively measure behavior or verify self-reports." Specific sensor list, sampling configurability, and iOS-vs-Android parity were **not independently verified against current developer documentation** this session, flagged as an open question, consistent with CLAUDE.md's instruction not to assume parity.

## Derived Metrics / Analytics

- Not verified in any pass to date.

## Active Data Collection

- Surveys/EMA, cognitive and behavioral tasks, and a "TeleVisit" feature (implying live video/remote-visit capability distinct from passive sensing) are named on the vendor's own feature page, a broader active-assessment feature set than most academic-open-source competitors in this module, oriented toward clinical-trial-style outcome assessment.

## Researcher and Study Management Features

- "Study Management" is an explicitly named product area. Specific capabilities (participant rostering, adherence monitoring, multi-site support, role-based access) were not independently verified against current documentation this session.

## Data Access and Export

- Per the vendor's own "Data Access & Analytics" page, study data are processed and made available "minutes after upload" from participants, accessible either by direct download or through analysis tools in the researcher dashboard. Supported export formats include **CSV and JSON**, plus format-specific outputs for particular data types, **GEXF for network graphs, KML for location data**, a level of export-format specificity not found on most competitors' public pages in this module. **Corroborated** from the vendor's own feature documentation, though this session did not independently test the export pipeline.
- The homepage (re-read 2026-10-10) offers "Raw or processed sensor data", accessed "Via Avicenna Dashboard, or tools such as R or Jupyter". No export API exists yet (see APIs, SDKs, and Extensibility).

## APIs, SDKs, and Extensibility

- **Re-confirmed 2026-08-25 (second pass).** Direct fetch of both `avicennaresearch.com`'s homepage and `avicennaresearch.dev/features/data-access-and-analytics/` again found no mention of a developer/public API, this session's targeted search for Avicenna API documentation also returned nothing. The absence is now corroborated by two independent direct fetches plus a dedicated search rather than a single pass, strengthening (not just repeating) the "not confirmed" status, data access still appears to be dashboard/export-mediated (CSV, JSON, GEXF, KML) rather than API-mediated. White-label solutions remain named as a product offering, implying some degree of platform customization is available commercially.
- **Updated 2026-10-10:** the vendor's public roadmap confirms the absence. "Export Data with API" (forum topic 1406, created 2025-09-29) sits in the "To Do" category, to follow "OpenAPI Compatible APIs". **Verified** as a planned, not shipped, feature.

## Deployment and Infrastructure

- **Re-confirmed 2026-08-25 (second pass, direct fetch of `avicennaresearch.com`).** Vendor-hosted SaaS; no self-hosting option identified on the homepage. Deployment model requires no researcher-side infrastructure, in contrast to Beiwe/RADAR-base/AWARE's self-hosting orientation, the tradeoff being reliance on the vendor's cloud rather than researcher-controlled infrastructure.

## Participant Experience

- Not verified in any pass to date.

### Background keepalive (added 2026-10-09)

- No phone-app keepalive was found. Notification triggers cover participation events (invited, joined), activity-session events (released, completed, canceled, expired), appointments (scheduled, started, canceled), and a "Sensor Data Gap Detected" trigger that the server checks every 15 minutes (default threshold 1 hour, default minimum gap between notifications 4 hours), currently limited to the Garmin Health SDK Logged Wrist Status data source. Nothing fires when the phone app itself stops sending. **Verified 2026-10-10** from the Notifications reference (forum.avicennaresearch.com/t/notifications/1277, posted 2025-06-16), read directly.
- Researchers get monitoring instead. The Participation page shows an "In Operation" percentage (share of time the app was running and collecting sensor data) and a Last Recorded Data Time per participant. "Reload Devices" sends a message to participants' devices to pull new study settings. That is a configuration sync, not a keepalive, and the periodic sync otherwise "can take about 30 days".
- Status: **Corroborated** absence of a phone-app keepalive, from the Participation reference (dated 2025-06-16) and the Notifications reference, read 2026-10-09 and 2026-10-10. Sources 12 and 13.

## Privacy, Security, and Compliance

- **Corrected 2026-10-10.** The 2026-08-25 pass rated the ISO 27001 statement Verified and "independently audited". The evidence read is the vendor's own: the legal page says "ISO 27001:2022 certified infrastructure", "Certified November 2024 with zero nonconformities" and a November 2025 surveillance audit, and names no certification body or certificate number. The vendor's Security and Compliance forum post (updated 2025-11-08) says the certification was achieved "through UKAS" and links a UKAS CertCheck entry (https://certcheck.ukas.com/certified-entity/adc99141-1f0e-5832-951d-c9b4c1682be7), but that page sits behind a CAPTCHA and was not read. The claim is therefore **Corroborated (vendor-stated, with a registry link not read)**, not Verified. "Certified infrastructure" may also refer to the hosting provider rather than Avicenna's own management system.

- **ISO 27001:2022 certification stated by the vendor** (certified Nov 2024, surveillance audit Nov 2025, zero nonconformities, per its legal page), plus "AES-256 encryption at rest, TLS 1.2+ for data in transit, and full disk encryption". Data are stored on servers in Canada (security post) and the legal page says data are "processed and stored within the UK/EEA unless specific safeguards are in place" for those transfers; the two statements are recorded as found. Avicenna is also on the UK ICO register of fee payers (ZC009135, registered 2025-10-07), which is a registration, not a certification. **Corroborated.**
- **HIPAA**: the legal page addresses the HIPAA Privacy Rule and Security Rule specifically in the context of minors' Protected Health Information, referencing required administrative, physical, and technical safeguards, and states Business Associate Agreements are required for covered transactions. This is HIPAA-*relevant* documented language, not a blanket "Avicenna is HIPAA compliant" certification claim, the distinction CLAUDE.md requires be preserved.
- **GDPR / UK GDPR / PIPEDA**: the page references "UK GDPR Article 8" (parental consent) and general EU GDPR compliance, plus PIPEDA (Canada) consent requirements for children under 13.
- **Data Processing Agreements**: described as addressing enhanced security requirements, audit rights, approved sub-processors, breach-notification procedures, and data return/deletion obligations.
- **What is still not confirmed**: no standalone Security Policy or DPA template document was found linked from this page, and neither SOC 2 nor 21 CFR Part 11 is mentioned on the legal page or the security post (re-checked 2026-10-10). Treat the ISO 27001:2022 statement and the HIPAA/GDPR/PIPEDA language alike as **Corroborated** (specific and dated, but vendor-stated; no certificate read).

- This resolves the bulk of unresolved-question #84 for Avicenna Research at the vendor-statement level. MetricWire also publishes ISO 27001 and SOC 2 Type II statements (see its profile), equally without a certificate read, so Avicenna is not the only Module 2 platform with a stated certification.

## Pricing

- Pricing remains non-public: there is no pricing page (avicennaresearch.com/pricing returns 404, checked 2026-10-10). The vendor's own FAQ (forum.avicennaresearch.com/t/5, updated 2026-08-03) describes the trial: free of charge, full access to the default features, no participant limit, "intended only for test purposes", collected study data "wiped monthly", and the study deleted after one year. Field research with real participants needs the full licence; upgrade by emailing support@avicennaresearch.com with the study ID. **Verified 2026-10-10.** No academic or non-profit rate was found. The 2026-08-25 note relied on third-party directories (Capterra, SoftwareAdvice) describing an "unlimited" trial; the vendor's terms make clear it is a test environment, not a free tier.

## Research Evidence and Validation

- The platform has an academic research lineage as "Ethica/iEpi," described in its originating academic materials (University of Saskatchewan, cs.usask.ca) as an "industrial strength and flexible smartphone-based epidemiological sensing, crowdsourcing and Ecological Momentary Assessment system", indicating the platform predates its current commercial packaging and has an independent academic development history distinct from being purely a startup product. This session did not attempt a systematic count of peer-reviewed studies using Ethica/Avicenna.

## Strengths

- Broad, clinically-oriented active-assessment feature set (cognitive/behavioral tasks, TeleVisit, outcome assessment) beyond passive sensing alone, a different value proposition than academic open-source competitors.
- Specific, named export-format support (CSV, JSON, GEXF for network data, KML for location data) suggests real engineering investment in researcher-usable data delivery.
- Data made available to researchers within minutes of participant upload, per the vendor's own materials, a notably fast latency claim relative to platforms with less-documented sync behavior.
- Academic origin (Ethica/iEpi, University of Saskatchewan) gives the platform a longer track record than a purely commercial startup.
- White-label option suggests platform flexibility for institutions wanting a rebranded participant-facing app.
- A specific, dated vendor compliance statement: ISO 27001:2022 certification stated (Nov 2024, surveillance audit Nov 2025, zero nonconformities), with a UKAS CertCheck link, plus detailed HIPAA/GDPR/PIPEDA language addressing minors' data. **Corroborated (vendor-stated)**; the certificate itself was not read (corrected 2026-10-10).

## Limitations

- Commercial, closed-source, vendor-hosted only, no self-hosting or code-level customization path, unlike Beiwe/RADAR-base/AWARE/CARP.
- Full pricing is non-public. The only free route is a test-only trial (data wiped monthly), so there is no free path for real field research (vendor FAQ, Verified 2026-10-10).
- No researcher-facing export API exists yet. The vendor's own public roadmap lists "Export Data with API" (forum topic created 2025-09-29) under its "To Do" category, probably to follow "OpenAPI Compatible APIs" (Verified 2026-10-10, forum.avicennaresearch.com/t/1406). Data access is dashboard export or R/Jupyter tools for now.
- ~~Compliance documentation (HIPAA/GDPR/Part 11) was not independently verified this session~~. Partly resolved 2026-08-25 and corrected 2026-10-10: the vendor states ISO 27001:2022 certification (Nov 2024, surveillance audit Nov 2025) and gives detailed HIPAA/UK-GDPR/PIPEDA language, all Corroborated (vendor-stated). 21 CFR Part 11 and SOC 2 are not mentioned anywhere read.
- The Ethica-to-Avicenna rebrand means older published literature citing "Ethica" may not obviously connect to the current company/product name for researchers doing their own literature search, worth flagging explicitly to anyone cross-referencing this profile against older papers.

## Best-Fit Use Cases

- Clinical-trial-style studies needing outcome assessment, cognitive/behavioral tasks, and passive sensing in one commercial, no-infrastructure-required platform.
- Teams wanting fast (minutes-scale) data availability after participant upload without building their own pipeline.
- Studies needing network-graph (GEXF) or location-specific (KML) export formats out of the box.

## Poor-Fit Use Cases

- Teams requiring self-hosting, full data custody, or source-code-level auditability, not offered.
- Teams needing a documented public API for real-time third-party integration, not confirmed to exist.
- Budget-constrained academic pilots needing firm, public pricing before committing, pricing requires vendor contact.

## Open Questions

- *(Directed to: Avicenna Research, https://avicennaresearch.com/ , https://avicennaresearch.dev/)*

- What is current, non-trial pricing (per-participant, per-study, or subscription), and is academic/non-profit pricing available?, still unresolved after a second, dedicated search.
- ~~Is there a documented developer API distinct from the dashboard/export mechanism?~~ Answered 2026-10-10: no. An export API is on the vendor's "To Do" roadmap (forum topic 1406), not shipped.
- ~~What HIPAA, GDPR/DPA, SOC 2, or 21 CFR Part 11 compliance documentation exists?~~ **Largely resolved**, see Privacy, Security, and Compliance above (ISO 27001:2022 and HIPAA/GDPR/PIPEDA all Corroborated as vendor statements, 2026-10-10). Still open: the certificate's scope and number (the UKAS CertCheck page needs a CAPTCHA), SOC 2 and 21 CFR Part 11.
- What is the exact current sensor/wearable integration catalog, and how does iOS coverage compare with Android?, not targeted this pass; still open.
- Under what circumstances is the "white-label" option available, and at what additional cost?, not targeted this pass; still open.

## Key Links

- Official site (current brand): https://avicennaresearch.com/
- Product/feature documentation: https://avicennaresearch.dev/
- Data Access & Analytics feature page: https://avicennaresearch.dev/features/data-access-and-analytics/
- App Store listing: https://apps.apple.com/us/app/ethica-avicenna/id1137173052 (now titled "Avicenna Research", checked 2026-10-10)
- Trial terms FAQ: https://forum.avicennaresearch.com/t/5
- Security and compliance post: https://forum.avicennaresearch.com/t/security-and-compliance/1267
- Google Play listing: https://play.google.com/store/apps/details?id=com.ethica.logger

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
17. Avicenna Research, "Legal Documents" (re-read). https://avicennaresearch.com/legal/ (accessed 2026-10-10). **Primary, vendor-stated.** Same ISO wording as source 10; no certification body or certificate number; no SOC 2 or Part 11.
18. Avicenna Research, product roadmap topic "Export Data with API". https://forum.avicennaresearch.com/t/1406 (created 2025-09-29; accessed 2026-10-10). **Primary/Verified.** Filed under "To Do".
19. App Store (iTunes lookup id 1137173052) and Google Play (`com.ethica.logger`) listings, direct fetch 2026-10-10. **Primary/Verified.** iOS v1065 released 2026-10-07; Android updated 2026-09-05.
20. UK ICO register of fee payers, entry ZC009135. https://ico.org.uk/ESDWebPages/Entry/ZC009135 (accessed 2026-10-10). **Primary.** Registration only.
