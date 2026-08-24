# Avicenna Research (formerly Ethica / Ethica Data)

## Quick Facts

| Field | Details |
|---|---|
| Organization | Avicenna Research (rebrand of Ethica Data) |
| Category | Commercial mobile sensing, EMA, and clinical-trial data-capture platform |
| Current status | Active, under new name — the company rebranded from "Ethica Data" to "Avicenna Research" |
| Platforms/devices | iOS and Android apps; web researcher dashboard |
| Open source | No |
| Hosting/deployment | Vendor SaaS |
| Pricing model | Commercial; a free tier/trial is offered, full pricing not public |
| Last verified | 2026-08-24 |

## Summary

Avicenna Research is the current name of the platform long known in the digital-phenotyping and EMA literature as **Ethica** (also referenced historically as "Ethica/iEpi," reflecting an earlier academic lineage at the University of Saskatchewan). It is a commercial, no-code-for-researchers platform combining survey/EMA delivery, cognitive and behavioral tasks, sensor-based passive data collection, wearable integration, and a data-access/analytics dashboard — explicitly positioned toward clinical-trial and health-research use, not just academic mobile sensing. The company markets under both names in different contexts (the app store listing reads "Avicenna (Ethica)"), so researchers searching prior literature for "Ethica" should expect to land on Avicenna's current materials.

**Naming note handled carefully per CLAUDE.md's instruction to record rather than silently resolve ambiguity:** Ethica Data and Avicenna Research are the same corporate entity under two names, not two competing platforms — confirmed by the shared app-store listing ("Avicenna (Ethica)"), Avicenna's own site being hosted at a URL referencing "Ethica Data" in its page title, and Crunchbase/CB Insights profiles cross-referencing both names to the same company.

## Products / Platform Architecture

- **Avicenna app** (iOS/Android, listed as "Avicenna (Ethica)") — participant-facing data collection.
- **Researcher dashboard** — study design, participant management, data access and analytics.
- Named feature areas per the vendor's own site: Outcome Assessment, TeleVisit, Cognitive and Behavioral Tasks, Sensor-based Data, Study Management, Data Access & Analytics, White-Label Solutions.

## Sensors and Data Streams

The vendor states integration with "a wide range of smartphone sensors and wearables that studies can use to objectively measure behavior or verify self-reports." Specific sensor list, sampling configurability, and iOS-vs-Android parity were **not independently verified against current developer documentation** this session — flagged as an open question, consistent with CLAUDE.md's instruction not to assume parity.

## Active Data Collection

Surveys/EMA, cognitive and behavioral tasks, and a "TeleVisit" feature (implying live video/remote-visit capability distinct from passive sensing) are named on the vendor's own feature page — a broader active-assessment feature set than most academic-open-source competitors in this module, oriented toward clinical-trial-style outcome assessment.

## Researcher and Study Management Features

"Study Management" is an explicitly named product area. Specific capabilities (participant rostering, adherence monitoring, multi-site support, role-based access) were not independently verified against current documentation this session.

## Data Access and Export

Per the vendor's own "Data Access & Analytics" page, study data are processed and made available "minutes after upload" from participants, accessible either by direct download or through analysis tools in the researcher dashboard. Supported export formats include **CSV and JSON**, plus format-specific outputs for particular data types — **GEXF for network graphs, KML for location data** — a level of export-format specificity not found on most competitors' public pages in this module. **Corroborated** from the vendor's own feature documentation, though this session did not independently test the export pipeline.

## APIs, SDKs, and Extensibility

A dedicated public API was **not confirmed** in this session — the vendor's documentation describes dashboard-based data access and standard export formats rather than a documented developer API. White-label solutions are named as a product offering, implying some degree of platform customization is available commercially.

## Deployment and Infrastructure

Vendor-hosted SaaS; no self-hosting option identified. Deployment model requires no researcher-side infrastructure, in contrast to Beiwe/RADAR-base/AWARE's self-hosting orientation — the tradeoff being reliance on the vendor's cloud rather than researcher-controlled infrastructure.

## Privacy, Security, and Compliance

Not independently verified against primary vendor documentation in this session. Given the platform's explicit clinical-trial positioning, HIPAA/GDPR/21 CFR Part 11-type compliance claims would be expected on a dedicated trust/security page — this session did not locate and read one directly, so no compliance claim should be assumed either way.

## Pricing

Per third-party software-directory listings (Capterra, SoftwareAdvice), Avicenna/Ethica offers a free trial and has historically been described as offering "an absolutely free unlimited trial with all features available to test." **These are third-party directory characterizations, not the vendor's own pricing page, and should be treated as Reported rather than Verified.** Full commercial/enterprise pricing is not public and requires vendor contact.

## Research Evidence and Validation

The platform has an academic research lineage as "Ethica/iEpi," described in its originating academic materials (University of Saskatchewan, cs.usask.ca) as an "industrial strength and flexible smartphone-based epidemiological sensing, crowdsourcing and Ecological Momentary Assessment system" — indicating the platform predates its current commercial packaging and has an independent academic development history distinct from being purely a startup product. This session did not attempt a systematic count of peer-reviewed studies using Ethica/Avicenna.

## Strengths

- Broad, clinically-oriented active-assessment feature set (cognitive/behavioral tasks, TeleVisit, outcome assessment) beyond passive sensing alone — a different value proposition than academic open-source competitors.
- Specific, named export-format support (CSV, JSON, GEXF for network data, KML for location data) suggests real engineering investment in researcher-usable data delivery.
- Data made available to researchers within minutes of participant upload, per the vendor's own materials — a notably fast latency claim relative to platforms with less-documented sync behavior.
- Academic origin (Ethica/iEpi, University of Saskatchewan) gives the platform a longer track record than a purely commercial startup.
- White-label option suggests platform flexibility for institutions wanting a rebranded participant-facing app.

## Limitations

- Commercial, closed-source, vendor-hosted only — no self-hosting or code-level customization path, unlike Beiwe/RADAR-base/AWARE/CARP.
- Full pricing is non-public; only a free-trial characterization from third-party directories was located, not verified against the vendor's own page.
- No developer API was confirmed, which may limit programmatic integration relative to competitors with documented APIs.
- Compliance documentation (HIPAA/GDPR/Part 11) was not independently verified this session despite the platform's clinical-trial positioning, which is exactly the context where such documentation matters most.
- The Ethica-to-Avicenna rebrand means older published literature citing "Ethica" may not obviously connect to the current company/product name for researchers doing their own literature search — worth flagging explicitly to anyone cross-referencing this profile against older papers.

## Best-Fit Use Cases

- Clinical-trial-style studies needing outcome assessment, cognitive/behavioral tasks, and passive sensing in one commercial, no-infrastructure-required platform.
- Teams wanting fast (minutes-scale) data availability after participant upload without building their own pipeline.
- Studies needing network-graph (GEXF) or location-specific (KML) export formats out of the box.

## Poor-Fit Use Cases

- Teams requiring self-hosting, full data custody, or source-code-level auditability — not offered.
- Teams needing a documented public API for real-time third-party integration — not confirmed to exist.
- Budget-constrained academic pilots needing firm, public pricing before committing — pricing requires vendor contact.

## Open Questions

*(Directed to: Avicenna Research — https://avicennaresearch.com/ , https://avicennaresearch.dev/)*

- What is current, non-trial pricing (per-participant, per-study, or subscription), and is academic/non-profit pricing available?
- Is there a documented developer API distinct from the dashboard/export mechanism?
- What HIPAA, GDPR/DPA, SOC 2, or 21 CFR Part 11 compliance documentation exists?
- What is the exact current sensor/wearable integration catalog, and how does iOS coverage compare with Android?
- Under what circumstances is the "white-label" option available, and at what additional cost?

## Key Links

- Official site (current brand): https://avicennaresearch.com/
- Product/feature documentation: https://avicennaresearch.dev/
- Data Access & Analytics feature page: https://avicennaresearch.dev/features/data-access-and-analytics/
- App Store listing: https://apps.apple.com/us/app/ethica-avicenna/id1137173052
- Google Play listing: https://play.google.com/store/apps/details?id=com.ethica.logger

## Sources

1. Avicenna Research — official site. https://avicennaresearch.com/ (accessed 2026-08-24, search summary). **Primary.** Current company identity, rebrand from Ethica Data.
2. Avicenna Research (Ethica Data) — product documentation site. https://avicennaresearch.dev/ (accessed 2026-08-24, search summary). **Primary.** Named feature areas (Outcome Assessment, TeleVisit, Cognitive and Behavioral Tasks, Sensor-based Data, Study Management, Data Access & Analytics, White-Label Solutions).
3. Avicenna Research — "Data Access & Analytics." https://avicennaresearch.dev/features/data-access-and-analytics/ (accessed 2026-08-24, search summary). **Primary.** Export formats (CSV, JSON, GEXF, KML), "minutes after upload" latency claim.
4. App Store listing — "Avicenna (Ethica)." https://apps.apple.com/us/app/ethica-avicenna/id1137173052 (accessed 2026-08-24). Confirms the Ethica/Avicenna naming continuity.
5. Google Play listing — "Avicenna Research." https://play.google.com/store/apps/details?id=com.ethica.logger (accessed 2026-08-24). Package name `com.ethica.logger` further corroborates continuity between Ethica and Avicenna.
6. Ethica/iEpi academic project page, University of Saskatchewan. https://www.cs.usask.ca/~osgood/iEpi/iEpi.html (accessed 2026-08-24, search summary). Academic origin as an epidemiological sensing/EMA system.
7. CB Insights — Avicenna Research company profile. https://www.cbinsights.com/company/ethica-data (accessed 2026-08-24, search summary). Corroborates the Ethica-to-Avicenna corporate continuity.
8. Third-party pricing/trial characterization: Capterra, SoftwareAdvice, SoftwareWorld listings (accessed 2026-08-24, search summary) — **Reported**, not vendor-verified: free-trial characterization.
