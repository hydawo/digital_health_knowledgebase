# MetricWire

## Quick Facts

| Field | Details |
|---|---|
| Organization | MetricWire Inc., Waterloo, Canada (founded 2013) |
| Category | Commercial EMA / passive-sensing platform for academic, clinical, and commercial research |
| Current status | Active |
| Platforms/devices | Participant app "Catalyst By MetricWire" on the App Store (v6.9.0, 2026-10-07) and Google Play (`com.metricwire.digitalhealth`, updated 2026-10-07); older "MetricWire" app listings last updated 2022 (iOS) and 2024 (Android); several study-branded apps under the same seller; web researcher dashboard. Checked 2026-10-10. |
| Open source | No |
| Hosting/deployment | Vendor SaaS only; data stored in the United States on Google Cloud Platform (vendor-stated). No self-hosting. |
| Pricing model | Commercial, custom quote; no public figures (`/pricing` returns 404). Demo by request ("Schedule Demo"); no trial is mentioned on the vendor site. An institution-level **Academic Site Licence** exists, described as "cost effective" but unpriced (Verified 2026-10-10) |
| Last verified | 2026-10-10 (vendor homepage, Site Licence and Data Privacy & Security Summary pages now fetch directly; /pricing returns 404) |

## Summary

- MetricWire is a Canadian commercial EMA-and-passive-sensing platform, in continuous operation since 2013, a longer commercial track record than most competitors profiled in this module. It supports electronic consent workflows, mobile diaries, passive sensor and geolocation capture, contextualized trigger-based survey deployment, and real-time monitoring/analytics dashboards, serving academic institutions, clinical research organizations, and commercial firms.

## Products / Platform Architecture

- **MetricWire app** (iOS/Android), participant-facing diary/survey and passive-sensing collection.
- **Researcher dashboard**, real-time monitoring and analytics.
- **Electronic consent module**, named as a distinct feature, useful for fully remote/decentralized study designs that need consent captured in-app rather than on paper.

## Sensors and Data Streams

- Every Module 2 profile uses the same table so platforms can be compared row by row. Rows are the passive streams named in `CLAUDE.md`. "Yes" and "No" are used only where a primary source says so; "Unclear" means nothing current was verified, and "No (OS)" means the operating system does not expose the stream to any third-party app. Confidence and sources are stated under the table. The convention is recorded in [`../../shared/profile-table-conventions.md`](../../shared/profile-table-conventions.md).

| Stream | Android | iOS | Raw or derived | Sampling configurable | Notes |
|---|---|---|---|---|---|
| GPS / location | Yes | Yes | Unclear | Unclear | Named on the vendor's materials. |
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
| Bluetooth | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Calls (metadata) | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| SMS (metadata) | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Keyboard | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Audio / microphone | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Notifications | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |
| Device information | Unclear | Unclear | Unclear | Unclear | Not verified against current documentation. |

**Verification.** Passive sensor and geolocation capture is named on the vendor's materials. Nothing beyond location was verified. Siebers 2025 (Module 3) used the platform's carrier-country metadata to detect fraud, which is device information of a kind, but it is not documented as a stream.

### Notes from earlier verification passes

- Passive sensor and geolocation capture is explicitly named on the vendor's own materials. The exact sensor catalog beyond location, and iOS-vs-Android parity, were **not independently verified against current developer documentation** this session, flagged as an open question.

## Derived Metrics / Analytics

- Not verified in any pass to date.

## Active Data Collection

- Mobile diaries and "contextualized trigger-based survey deployment", i.e., surveys fired based on sensor-detected context (e.g., location or time-based triggers) rather than only fixed schedules, are explicitly named vendor capabilities. This event/context-triggered EMA capability is a genuine differentiator worth confirming in more depth for any study design that needs it, since not every platform in this module documents trigger-based (as opposed to purely scheduled or random) survey delivery.

## Researcher and Study Management Features

- Real-time monitoring and analytics dashboards are named vendor features, implying live adherence/data-flow visibility for study staff. Specific participant-management, multi-site, and role-based-access capabilities were not independently verified this session.

## Data Access and Export

- The homepage says researchers can "customize your result set and exports" (read 2026-10-10). Export formats and API mechanics are not described on the public pages. Still open.

## APIs, SDKs, and Extensibility

- **Second-pass update (2026-08-24):** the MetricWire GitHub organization (https://github.com/MetricWire) contains exactly **one public repository**, a forked architecture-decision-record template with no product code, confirming no public SDK, client library, or open developer package is maintained by MetricWire itself. This **corroborates (does not merely leave open) the closed-source characterization**. However, two independent third-party clues point to an underlying private/partner API: (1) a MetricWire integration guide in the `m2c2-project/m2c2kit-integration-guides` GitHub repository describes URL-based identifier injection between MetricWire and the m2c2kit cognitive-assessment toolkit; (2) an unofficial Python client, `zeolite` (https://github.com/uwmadison-chm/zeolite, University of Wisconsin, Madison Center for Healthy Minds), exists specifically "for MetricWire's Catalyst system." **Upgraded Reported → Corroborated 2026-09-02:** peer-reviewed full text independently confirms the app name, Ball MI et al. 2025 (*Behavior Therapy*, [10.1016/j.beth.2025.05.007](https://doi.org/10.1016/j.beth.2025.05.007), PMC13289574) states that 10% of its participants "received EMA through the smartphone app **Catalyst by MetricWire**" (the other 90% used LifeData's RealLife Exp, the only published head-to-head deployment of the two platforms located so far; see [`lifedata.md`](lifedata.md)). The claim no longer rests on an unofficial third-party client alone. This confirms MetricWire's participant-facing app is called "Catalyst" and exposes some form of authenticated API that at least one outside research-computing group has reverse-engineered or been given credentialed access to. **No official, MetricWire-published API documentation was located**, the existence of a private/partner-only API is now Reported (upgraded from pure absence), but public documentation remains unconfirmed. Resolves unresolved-question #90 partially: an API of some form evidently exists, but it is not documented for general researcher self-service.

## Deployment and Infrastructure

- Vendor-hosted SaaS; no self-hosting option identified.

## Participant Experience

- Not verified in any pass to date.

### Background keepalive (added 2026-10-09)

- No server-triggered keepalive was found. MetricWire's help centre says force-quitting the app stops prompts until it is reopened. On iOS, the app schedules its next 64 local notifications at each refresh, and app versions 2.2.3 and 2.2.4 added a periodic background refresh. Participants can switch that refresh off in iOS settings.
- Researchers can spot force-quitting from repeated "app_launched" events in Participant Activity. No server-initiated wake or reopen push was described.
- Status: **Reported**, from search summaries of MetricWire's knowledge base, 2026-10-09. Source 8. The cited Atlassian page returned HTTP 404 on 2026-10-10, so the claim now rests on the search summary alone.

## Privacy, Security, and Compliance

- **Updated 2026-10-10 (direct fetch; the site no longer returns HTTP 403).** The vendor's "Data Privacy & Security Summary" (last reviewed 9/8/2025) states: "All data are stored in the United States using Google Cloud Platform", "All data are encrypted at rest using AES-256 and in-transit using at least TLS 1.2", production access needs multi-factor authentication, and "Metricwire is ISO 27001 certified and SOC II Type II compliant."
- The Academic Site Licence page states that MetricWire "is the only EMA platform that complies with FDA 21 CFR Part 11, HIPAA & GDPR". The "only" is a marketing claim and is contradicted in part by other vendors' statements in this module.
- **Confidence: Corroborated (vendor-stated), not independently confirmed.** No ISO certificate, certification body, SOC 2 report, auditor or BAA terms are published or linked. The 2026-08-24 note that compliance documentation was "not located" was a consequence of the 403 block, not of absence.

## Pricing

- **Academic Site Licence (Verified 2026-10-10, https://metricwire.com/site-licence/):** an institution-level licence "designed to provide researchers at leading institutions with technology solutions", offering self-serve administration of researcher permissions, dedicated engineering support, beta-program access, an academic advisory board and a dedicated account manager, at "cost effective" but unpublished prices ("a balance between impactful tools and feasible pricing"). No participant limits, data-access terms or approval process are stated, and the page carries a 2023 copyright, so confirm it is current.
- The homepage's calls to action are "Schedule Demo" and "Get Started", both leading to a contact form; no free trial is mentioned (2026-10-10). The 2026-08-24 "trial offered" note came from third-party directories only.
- Not public. **Second-pass update (2026-08-24, superseded on 2026-10-10 where noted above):** direct fetches of metricwire.com's homepage, `/pricing`, `/site-licence/`, and `/contact-us/` pages were all blocked with HTTP 403 (bot-protection), so the vendor's own pricing language could not be directly quoted this session either, a genuine attempt was made and remains blocked, not skipped. WebSearch confirms the same conclusion from a wider set of third-party directories (Capterra, SoftwareSuggest, TechnologyCounter, SoftwareWorld, Visualping) plus MetricWire's own `/contact-requested/` and `/contact-us/` page *titles* (visible in search indexing even though the page bodies could not be fetched): pricing is gated behind a sales-contact/demo-request flow, and a **"Site Licence"** page exists (https://metricwire.com/site-licence/) whose title strongly suggests an institutional/site-wide licensing tier, though its terms could not be read directly. Per CLAUDE.md's instruction, this remains recorded as **non-public pricing requiring vendor contact**, not estimated, Corroborated, not Verified, since no primary-source page body was successfully retrieved in either research pass.

## Research Evidence and Validation

- **Checked 2026-10-10:** PubMed `MetricWire[Title/Abstract]` returns three records (PMIDs 41364742, 34668869, 31511290), all studies or protocols that use the platform; none is a platform methods or validation paper. The Site Licence page calls MetricWire "the most published EMA platform", which refers to use and is not evidenced on the page.
- MetricWire has been used in published EMA research (e.g., referenced directly in a ResearchGate figure caption from a published EMA study using "MetricWire" as the data-collection platform). This session did not attempt a systematic count of peer-reviewed studies using MetricWire.

## Strengths

- Longest continuous commercial operating history among the purely commercial platforms profiled in this module (founded 2013).
- Context/trigger-based survey deployment (surveys fired by sensor-detected context, not just schedule) is an explicitly documented, distinctive EMA capability.
- Built-in electronic consent workflow, useful for decentralized/remote study designs.
- Real-time monitoring dashboard for adherence/data-flow visibility.

## Limitations

- **Closed-source, vendor-hosted only, now Verified via GitHub org inspection** (a single unrelated forked repo, no product code, no public SDK).
- Pricing is entirely non-public; requires vendor contact for any estimate, including the Academic Site Licence. (The 2026-08-24 HTTP 403 block has lifted; the pages were read on 2026-10-10 and still give no figures.)
- Compliance rests on vendor statements only: ISO 27001 and SOC 2 Type II (security summary) and 21 CFR Part 11, HIPAA and GDPR (Site Licence page), with no certificate, auditor or BAA terms published (Corroborated, 2026-10-10).
- An API of some form evidently exists (backend internally referred to as "Catalyst," per an unofficial third-party Python client) but is not publicly documented for general researcher self-service, narrower gap than "not independently confirmed" but still not resolved to Verified.
- Sensor catalog detail and iOS/Android parity were not independently verified against current documentation in either session.

## Best-Fit Use Cases

- EMA-centric studies needing context/trigger-based (not just scheduled) survey delivery.
- Decentralized studies needing an in-app electronic consent workflow.
- Teams wanting real-time adherence monitoring without building their own dashboard.

## Poor-Fit Use Cases

- Teams needing firm pricing before initiating vendor contact.
- Teams requiring self-hosting, source-code auditability, or a documented public API.
- Studies where an independently verifiable compliance certificate is a hard requirement before vendor contact (the vendor states ISO 27001, SOC 2 Type II, Part 11, HIPAA and GDPR, but publishes no certificate).

## Open Questions

- *(Directed to: MetricWire, via https://metricwire.com and its sales/contact channel. The site fetches directly again as of 2026-10-10.)*

- Current pricing structure (per-participant, per-study, subscription). Partly answered 2026-10-10: an Academic Site Licence exists for institutions, but its prices, limits and approval process are not published.
- Full current sensor/passive-data catalog and iOS-vs-Android parity.
- ~~HIPAA, GDPR/DPA, SOC 2, or 21 CFR Part 11 compliance documentation.~~ Partly answered 2026-10-10: the vendor states all of them (see Privacy, Security, and Compliance). Still open: certificates or audit reports, and BAA terms.
- Whether the "Catalyst" backend's API (evidenced only via an unofficial third-party client) is available to researchers through an official, documented channel, or only via ad hoc/partner arrangements.
- Data retention, export formats, and bulk-export mechanics.

## Key Links

- Official site: https://metricwire.com/ (direct fetch succeeded 2026-10-10)
- Site Licence page: https://metricwire.com/site-licence/ (read 2026-10-10)
- Data Privacy & Security Summary: https://metricwire.com/data-privacy-security-summary/
- Catalyst By MetricWire, App Store: https://apps.apple.com/us/app/catalyst-by-metricwire/id1585123028; Google Play: https://play.google.com/store/apps/details?id=com.metricwire.digitalhealth
- GitHub organization: https://github.com/MetricWire (direct fetch succeeded, second pass)
- Third-party profile (used for company facts this session): https://pitchbook.com/profiles/company/89864-11

## Sources

1. Search-summary characterization of MetricWire's own marketing materials, aggregated via WebSearch (accessed 2026-08-24, both sessions). **Corroborated, not Direct**, metricwire.com's homepage and pricing/contact pages returned HTTP 403 on direct fetch in both the first and second pass; the platform description (electronic consent, mobile diaries, passive sensor/geolocation capture, contextualized trigger-based surveys, real-time dashboards) comes from a search-engine summary of the vendor's own site content, so it should be treated as Corroborated rather than Verified.
2. MetricWire GitHub organization (**direct fetch, second pass**). https://github.com/MetricWire (accessed 2026-08-24). **Primary/Verified.** Confirms exactly one public repository (an unrelated forked ADR template), no public SDK/API client, corroborates closed-source characterization.
3. m2c2kit integration guide for MetricWire (search summary). https://github.com/m2c2-project/m2c2kit-integration-guides/blob/main/docs/metricwire.md (accessed 2026-08-24). URL-based identifier-injection integration pattern between MetricWire and the m2c2kit cognitive-assessment toolkit.
4. `zeolite`, unofficial Python client for MetricWire's "Catalyst" system, University of Wisconsin, Madison Center for Healthy Minds. https://github.com/uwmadison-chm/zeolite (accessed 2026-08-24, search summary). Evidence an internal/partner API ("Catalyst") exists even though no official public API documentation was located.
5. PitchBook, MetricWire company profile. https://pitchbook.com/profiles/company/89864-11 (accessed 2026-08-24, search summary). Founding year (2013), Waterloo, Canada headquarters.
6. Third-party software directories: Capterra, SoftwareWorld, SoftwareSuggest, TechnologyCounter, SourceForge, Visualping (accessed 2026-08-24, search summary, both sessions). Trial/demo-availability and contact-gated-pricing characterization; no specific pricing figures located in either session.
7. ResearchGate figure caption referencing MetricWire as the platform used in a published EMA study. https://www.researchgate.net/figure/Select-screenshots-from-the-EMA-study-smartphone-platform-MetricWire-EMA-ecological_fig2_354098947 (accessed 2026-08-24, search summary). Evidence of research use.
8. MetricWire knowledge base, "Missing Alerts Troubleshooting." https://metricwire.atlassian.net/wiki/spaces/mwknowledgebase/pages/6750210/Missing+Alerts+Troubleshooting (accessed 2026-10-09, search summary). Returned HTTP 404 on 2026-10-10; dead link.
9. MetricWire, "Data Privacy & Security Summary." https://metricwire.com/data-privacy-security-summary/ (last reviewed 9/8/2025; accessed 2026-10-10, direct fetch). **Primary, vendor-stated.** US storage on Google Cloud Platform, AES-256 at rest, TLS 1.2+ in transit, MFA, ISO 27001 and SOC II Type II statements; no certificate linked.
10. MetricWire, "Academic Site Licence." https://metricwire.com/site-licence/ (copyright 2023; accessed 2026-10-10, direct fetch). **Primary/Verified** for the programme's existence and terms; compliance and "most published" claims are vendor-stated.
11. MetricWire homepage. https://metricwire.com/ (accessed 2026-10-10, direct fetch). **Primary.** Schedule Demo / Get Started calls to action; no trial or pricing; "customize your result set and exports".
12. App Store and Google Play listings for "Catalyst By MetricWire" (`com.metricwire.digitalhealth`) and the older "MetricWire" app (`com.metricwire.android3`), direct fetch 2026-10-10. **Primary/Verified.**
13. PubMed search `MetricWire[Title/Abstract]` via E-utilities (accessed 2026-10-10). Three records: 41364742, 34668869, 31511290.
