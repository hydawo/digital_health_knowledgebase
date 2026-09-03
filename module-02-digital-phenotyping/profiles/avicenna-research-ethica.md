# Avicenna Research (formerly Ethica / Ethica Data)

## Quick Facts

| Field | Details |
|---|---|
| Organization | Avicenna Research (rebrand of Ethica Data) |
| Category | Commercial mobile sensing, EMA, and clinical-trial data-capture platform |
| Current status | Active, under new name, the company rebranded from "Ethica Data" to "Avicenna Research" |
| Platforms/devices | iOS and Android apps; web researcher dashboard |
| Open source | No |
| Hosting/deployment | Vendor SaaS |
| Pricing model | Commercial; a free tier/trial is offered, full pricing not public |
| Last verified | 2026-08-25 (second pass) |

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

## APIs, SDKs, and Extensibility

- **Re-confirmed 2026-08-25 (second pass).** Direct fetch of both `avicennaresearch.com`'s homepage and `avicennaresearch.dev/features/data-access-and-analytics/` again found no mention of a developer/public API, this session's targeted search for Avicenna API documentation also returned nothing. The absence is now corroborated by two independent direct fetches plus a dedicated search rather than a single pass, strengthening (not just repeating) the "not confirmed" status, data access still appears to be dashboard/export-mediated (CSV, JSON, GEXF, KML) rather than API-mediated. White-label solutions remain named as a product offering, implying some degree of platform customization is available commercially.

## Deployment and Infrastructure

- **Re-confirmed 2026-08-25 (second pass, direct fetch of `avicennaresearch.com`).** Vendor-hosted SaaS; no self-hosting option identified on the homepage. Deployment model requires no researcher-side infrastructure, in contrast to Beiwe/RADAR-base/AWARE's self-hosting orientation, the tradeoff being reliance on the vendor's cloud rather than researcher-controlled infrastructure.

## Participant Experience

- Not verified in any pass to date.

## Privacy, Security, and Compliance

- **Materially upgraded 2026-08-25 (second pass, Verified via direct fetch of `avicennaresearch.com/legal/`).** This is now one of the better-documented compliance postures in this module:

- **ISO 27001:2022 certified infrastructure**, with the page stating "AES-256 encryption at rest." The certification is dated specifically: **certified November 2024 with zero nonconformities; a surveillance audit in November 2025, also zero nonconformities.**
- **HIPAA**: the legal page addresses the HIPAA Privacy Rule and Security Rule specifically in the context of minors' Protected Health Information, referencing required administrative, physical, and technical safeguards, and states Business Associate Agreements are required for covered transactions. This is HIPAA-*relevant* documented language, not a blanket "Avicenna is HIPAA compliant" certification claim, the distinction CLAUDE.md requires be preserved.
- **GDPR / UK GDPR / PIPEDA**: the page references "UK GDPR Article 8" (parental consent) and general EU GDPR compliance, plus PIPEDA (Canada) consent requirements for children under 13.
- **Data Processing Agreements**: described as addressing enhanced security requirements, audit rights, approved sub-processors, breach-notification procedures, and data return/deletion obligations.
- **What is still not confirmed**: no standalone, freestanding Security Policy or DPA *template* document was found linked from this page (the content is woven into Privacy Policy / Terms of Use rather than a dedicated trust-center page), and SOC 2 status specifically was not mentioned anywhere in this fetch. Treat the ISO 27001:2022 certification claim as **Verified** (specific, dated, audited), and the HIPAA/GDPR/PIPEDA language as **Corroborated** (specific and detailed, but self-reported by the vendor rather than independently audited in what this session could access).

- This resolves the bulk of unresolved-question #84 for Avicenna Research specifically, it is no longer accurate to say no Module 2 platform has documented compliance evidence; Avicenna Research now does.

## Pricing

- **Re-confirmed 2026-08-25 (second pass).** A dedicated search for current Avicenna Research pricing/security information did not surface a vendor pricing page, pricing remains non-public. Per third-party software-directory listings (Capterra, SoftwareAdvice), Avicenna/Ethica offers a free trial and has historically been described as offering "an absolutely free unlimited trial with all features available to test." **These are third-party directory characterizations, not the vendor's own pricing page, and should be treated as Reported rather than Verified.** Full commercial/enterprise pricing is not public and requires vendor contact.

## Research Evidence and Validation

- The platform has an academic research lineage as "Ethica/iEpi," described in its originating academic materials (University of Saskatchewan, cs.usask.ca) as an "industrial strength and flexible smartphone-based epidemiological sensing, crowdsourcing and Ecological Momentary Assessment system", indicating the platform predates its current commercial packaging and has an independent academic development history distinct from being purely a startup product. This session did not attempt a systematic count of peer-reviewed studies using Ethica/Avicenna.

## Strengths

- Broad, clinically-oriented active-assessment feature set (cognitive/behavioral tasks, TeleVisit, outcome assessment) beyond passive sensing alone, a different value proposition than academic open-source competitors.
- Specific, named export-format support (CSV, JSON, GEXF for network data, KML for location data) suggests real engineering investment in researcher-usable data delivery.
- Data made available to researchers within minutes of participant upload, per the vendor's own materials, a notably fast latency claim relative to platforms with less-documented sync behavior.
- Academic origin (Ethica/iEpi, University of Saskatchewan) gives the platform a longer track record than a purely commercial startup.
- White-label option suggests platform flexibility for institutions wanting a rebranded participant-facing app.
- **New (second pass, 2026-08-25):** the most specific, dated third-party-audited compliance posture of any platform in this module, ISO 27001:2022 certified (zero nonconformities, most recent surveillance audit November 2025), plus detailed HIPAA/GDPR/PIPEDA language addressing minors' data specifically.

## Limitations

- Commercial, closed-source, vendor-hosted only, no self-hosting or code-level customization path, unlike Beiwe/RADAR-base/AWARE/CARP.
- Full pricing is non-public; only a free-trial characterization from third-party directories was located, not verified against the vendor's own page (re-confirmed 2026-08-25, a dedicated pricing-page search still found nothing).
- No developer API was confirmed, which may limit programmatic integration relative to competitors with documented APIs (re-confirmed 2026-08-25 via two direct fetches plus a search).
- ~~Compliance documentation (HIPAA/GDPR/Part 11) was not independently verified this session~~, **materially resolved 2026-08-25**: Avicenna Research now has the most specific, dated third-party compliance evidence in this module (ISO 27001:2022, certified Nov 2024, zero-nonconformity surveillance audit Nov 2025), plus detailed HIPAA/UK-GDPR/PIPEDA language addressing minors' data specifically. 21 CFR Part 11 was still not mentioned anywhere fetched this session, and SOC 2 status remains unconfirmed, those two items are the genuine remaining gap, not the whole compliance picture.
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
- Is there a documented developer API distinct from the dashboard/export mechanism?, still unresolved after two direct fetches plus a search this pass.
- ~~What HIPAA, GDPR/DPA, SOC 2, or 21 CFR Part 11 compliance documentation exists?~~ **Largely resolved 2026-08-25**, see Privacy, Security, and Compliance above (ISO 27001:2022 Verified; HIPAA/GDPR/PIPEDA Corroborated). **SOC 2 status and 21 CFR Part 11 remain unconfirmed**, this is the narrower residual question.
- What is the exact current sensor/wearable integration catalog, and how does iOS coverage compare with Android?, not targeted this pass; still open.
- Under what circumstances is the "white-label" option available, and at what additional cost?, not targeted this pass; still open.

## Key Links

- Official site (current brand): https://avicennaresearch.com/
- Product/feature documentation: https://avicennaresearch.dev/
- Data Access & Analytics feature page: https://avicennaresearch.dev/features/data-access-and-analytics/
- App Store listing: https://apps.apple.com/us/app/ethica-avicenna/id1137173052
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
10. Avicenna Research, "Legal Documents." https://avicennaresearch.com/legal/ (accessed 2026-08-25, second pass). **Primary/Verified.** ISO 27001:2022 certification (certified Nov 2024, zero nonconformities; surveillance audit Nov 2025, zero nonconformities), AES-256 encryption at rest, HIPAA Privacy/Security Rule language for minors' PHI, UK GDPR Article 8, EU GDPR, PIPEDA, DPA scope description. Resolves the majority of unresolved-question #84 for this platform.
11. Avicenna Research, "Data Access & Analytics" (second-pass direct re-fetch). https://avicennaresearch.dev/features/data-access-and-analytics/ (accessed 2026-08-25). **Primary/Direct.** Re-confirms export formats (CSV, JSON, GEXF, KML); no developer API mentioned.
