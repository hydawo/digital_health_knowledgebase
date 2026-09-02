# MetricWire

## Quick Facts

| Field | Details |
|---|---|
| Organization | MetricWire Inc., Waterloo, Canada (founded 2013) |
| Category | Commercial EMA / passive-sensing platform for academic, clinical, and commercial research |
| Current status | Active |
| Platforms/devices | iOS and Android apps; web researcher dashboard |
| Open source | No |
| Hosting/deployment | Vendor SaaS |
| Pricing model | Commercial, custom quote (**Corroborated across multiple third-party directories and a demo/contact-request flow on the vendor's own site**; no public rate figures found); a trial/demo is offered |
| Last verified | 2026-08-24 (second-pass re-verification attempted; primary site direct-fetch still blocked — see below) |

## Summary

MetricWire is a Canadian commercial EMA-and-passive-sensing platform, in continuous operation since 2013 — a longer commercial track record than most competitors profiled in this module. It supports electronic consent workflows, mobile diaries, passive sensor and geolocation capture, contextualized trigger-based survey deployment, and real-time monitoring/analytics dashboards, serving academic institutions, clinical research organizations, and commercial firms.

## Products / Platform Architecture

- **MetricWire app** (iOS/Android) — participant-facing diary/survey and passive-sensing collection.
- **Researcher dashboard** — real-time monitoring and analytics.
- **Electronic consent module** — named as a distinct feature, useful for fully remote/decentralized study designs that need consent captured in-app rather than on paper.

## Sensors and Data Streams

Passive sensor and geolocation capture is explicitly named on the vendor's own materials. The exact sensor catalog beyond location, and iOS-vs-Android parity, were **not independently verified against current developer documentation** this session — flagged as an open question.

## Active Data Collection

Mobile diaries and "contextualized trigger-based survey deployment" — i.e., surveys fired based on sensor-detected context (e.g., location or time-based triggers) rather than only fixed schedules — are explicitly named vendor capabilities. This event/context-triggered EMA capability is a genuine differentiator worth confirming in more depth for any study design that needs it, since not every platform in this module documents trigger-based (as opposed to purely scheduled or random) survey delivery.

## Researcher and Study Management Features

Real-time monitoring and analytics dashboards are named vendor features, implying live adherence/data-flow visibility for study staff. Specific participant-management, multi-site, and role-based-access capabilities were not independently verified this session.

## Data Access and Export

Not independently verified against current developer documentation this session — export formats and API access mechanics are an open question.

## APIs, SDKs, and Extensibility

**Second-pass update (2026-08-24):** the MetricWire GitHub organization (https://github.com/MetricWire) contains exactly **one public repository** — a forked architecture-decision-record template with no product code — confirming no public SDK, client library, or open developer package is maintained by MetricWire itself. This **corroborates (does not merely leave open) the closed-source characterization**. However, two independent third-party clues point to an underlying private/partner API: (1) a MetricWire integration guide in the `m2c2-project/m2c2kit-integration-guides` GitHub repository describes URL-based identifier injection between MetricWire and the m2c2kit cognitive-assessment toolkit; (2) an unofficial Python client, `zeolite` (https://github.com/uwmadison-chm/zeolite, University of Wisconsin–Madison Center for Healthy Minds), exists specifically "for MetricWire's Catalyst system." **Upgraded Reported → Corroborated 2026-09-02:** peer-reviewed full text independently confirms the app name — Ball MI et al. 2025 (*Behavior Therapy*, [10.1016/j.beth.2025.05.007](https://doi.org/10.1016/j.beth.2025.05.007), PMC13289574) states that 10% of its participants "received EMA through the smartphone app **Catalyst by MetricWire**" (the other 90% used LifeData's RealLife Exp — the only published head-to-head deployment of the two platforms located so far; see [`lifedata.md`](lifedata.md)). The claim no longer rests on an unofficial third-party client alone. This confirms MetricWire's participant-facing app is called "Catalyst" and exposes some form of authenticated API that at least one outside research-computing group has reverse-engineered or been given credentialed access to. **No official, MetricWire-published API documentation was located** — the existence of a private/partner-only API is now Reported (upgraded from pure absence), but public documentation remains unconfirmed. Resolves unresolved-question #90 partially: an API of some form evidently exists, but it is not documented for general researcher self-service.

## Deployment and Infrastructure

Vendor-hosted SaaS; no self-hosting option identified.

## Privacy, Security, and Compliance

Not independently verified against primary vendor documentation this session — flagged as an open question, particularly relevant given the platform's stated use by clinical research organizations, where compliance documentation (HIPAA, GDPR, 21 CFR Part 11) would typically be expected.

## Pricing

Not public. **Second-pass update (2026-08-24):** direct fetches of metricwire.com's homepage, `/pricing`, `/site-licence/`, and `/contact-us/` pages were all blocked with HTTP 403 (bot-protection), so the vendor's own pricing language could not be directly quoted this session either — a genuine attempt was made and remains blocked, not skipped. WebSearch confirms the same conclusion from a wider set of third-party directories (Capterra, SoftwareSuggest, TechnologyCounter, SoftwareWorld, Visualping) plus MetricWire's own `/contact-requested/` and `/contact-us/` page *titles* (visible in search indexing even though the page bodies could not be fetched): pricing is gated behind a sales-contact/demo-request flow, and a **"Site Licence"** page exists (https://metricwire.com/site-licence/) whose title strongly suggests an institutional/site-wide licensing tier, though its terms could not be read directly. Per CLAUDE.md's instruction, this remains recorded as **non-public pricing requiring vendor contact**, not estimated — Corroborated, not Verified, since no primary-source page body was successfully retrieved in either research pass.

## Research Evidence and Validation

MetricWire has been used in published EMA research (e.g., referenced directly in a ResearchGate figure caption from a published EMA study using "MetricWire" as the data-collection platform). This session did not attempt a systematic count of peer-reviewed studies using MetricWire.

## Strengths

- Longest continuous commercial operating history among the purely commercial platforms profiled in this module (founded 2013).
- Context/trigger-based survey deployment (surveys fired by sensor-detected context, not just schedule) is an explicitly documented, distinctive EMA capability.
- Built-in electronic consent workflow, useful for decentralized/remote study designs.
- Real-time monitoring dashboard for adherence/data-flow visibility.

## Limitations

- **Closed-source, vendor-hosted only — now Verified via GitHub org inspection** (a single unrelated forked repo, no product code, no public SDK).
- Pricing is entirely non-public; requires vendor contact for any estimate. Direct fetch of the vendor's own pricing/site-licence/contact pages was attempted in the second pass and blocked (HTTP 403) — this is a confirmed access barrier, not an unattempted gap.
- Compliance documentation (HIPAA/GDPR/Part 11) was not independently located in either session despite the platform's stated clinical-research-organization customer base — still the largest unresolved item for this platform.
- An API of some form evidently exists (backend internally referred to as "Catalyst," per an unofficial third-party Python client) but is not publicly documented for general researcher self-service — narrower gap than "not independently confirmed" but still not resolved to Verified.
- Sensor catalog detail and iOS/Android parity were not independently verified against current documentation in either session.

## Best-Fit Use Cases

- EMA-centric studies needing context/trigger-based (not just scheduled) survey delivery.
- Decentralized studies needing an in-app electronic consent workflow.
- Teams wanting real-time adherence monitoring without building their own dashboard.

## Poor-Fit Use Cases

- Teams needing firm pricing before initiating vendor contact.
- Teams requiring self-hosting, source-code auditability, or a documented public API.
- Studies where independently verified compliance documentation is a hard requirement before vendor contact.

## Open Questions

*(Directed to: MetricWire — via https://metricwire.com and its sales/contact channel; direct site fetch was blocked in this pass, so a human visiting the site directly, or vendor email, is the realistic next step rather than another automated fetch attempt)*

- Current pricing structure (per-participant, per-study, subscription) and whether academic pricing exists — including what the "Site Licence" page's terms actually are.
- Full current sensor/passive-data catalog and iOS-vs-Android parity.
- HIPAA, GDPR/DPA, SOC 2, or 21 CFR Part 11 compliance documentation.
- Whether the "Catalyst" backend's API (evidenced only via an unofficial third-party client) is available to researchers through an official, documented channel, or only via ad hoc/partner arrangements.
- Data retention, export formats, and bulk-export mechanics.

## Key Links

- Official site: https://metricwire.com/ (direct fetch blocked both sessions — HTTP 403 bot-protection; not independently verified content, URL inferred from company identity)
- Site Licence page: https://metricwire.com/site-licence/ (title only; fetch blocked)
- GitHub organization: https://github.com/MetricWire (direct fetch succeeded, second pass)
- Third-party profile (used for company facts this session): https://pitchbook.com/profiles/company/89864-11

## Sources

1. Search-summary characterization of MetricWire's own marketing materials, aggregated via WebSearch (accessed 2026-08-24, both sessions). **Corroborated, not Direct** — metricwire.com's homepage and pricing/contact pages returned HTTP 403 on direct fetch in both the first and second pass; the platform description (electronic consent, mobile diaries, passive sensor/geolocation capture, contextualized trigger-based surveys, real-time dashboards) comes from a search-engine summary of the vendor's own site content, so it should be treated as Corroborated rather than Verified.
2. MetricWire GitHub organization (**direct fetch, second pass**). https://github.com/MetricWire (accessed 2026-08-24). **Primary/Verified.** Confirms exactly one public repository (an unrelated forked ADR template), no public SDK/API client — corroborates closed-source characterization.
3. m2c2kit integration guide for MetricWire (search summary). https://github.com/m2c2-project/m2c2kit-integration-guides/blob/main/docs/metricwire.md (accessed 2026-08-24). URL-based identifier-injection integration pattern between MetricWire and the m2c2kit cognitive-assessment toolkit.
4. `zeolite` — unofficial Python client for MetricWire's "Catalyst" system, University of Wisconsin–Madison Center for Healthy Minds. https://github.com/uwmadison-chm/zeolite (accessed 2026-08-24, search summary). Evidence an internal/partner API ("Catalyst") exists even though no official public API documentation was located.
5. PitchBook — MetricWire company profile. https://pitchbook.com/profiles/company/89864-11 (accessed 2026-08-24, search summary). Founding year (2013), Waterloo, Canada headquarters.
6. Third-party software directories: Capterra, SoftwareWorld, SoftwareSuggest, TechnologyCounter, SourceForge, Visualping (accessed 2026-08-24, search summary, both sessions). Trial/demo-availability and contact-gated-pricing characterization; no specific pricing figures located in either session.
7. ResearchGate figure caption referencing MetricWire as the platform used in a published EMA study. https://www.researchgate.net/figure/Select-screenshots-from-the-EMA-study-smartphone-platform-MetricWire-EMA-ecological_fig2_354098947 (accessed 2026-08-24, search summary). Evidence of research use.
