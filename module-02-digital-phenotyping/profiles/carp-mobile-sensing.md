# CARP Mobile Sensing (Copenhagen Research Platform)

## Quick Facts

| Field | Details |
|---|---|
| Organization | Technical University of Denmark (DTU); Jakob E. Bardram's group |
| Category | Open-source cross-platform mobile sensing framework for digital phenotyping |
| Current status | Active — Flutter package (`carp_mobile_sensing`) actively distributed via pub.dev |
| Platforms/devices | Android and iOS (cross-platform via Flutter) |
| Open source | Yes — MIT licence |
| Hosting/deployment | Self-hosted / researcher-integrated (framework/library, not a turnkey SaaS) |
| Pricing model | Free/open source |
| Last verified | 2026-08-24 |

## Summary

CARP Mobile Sensing (CAMS) is the sensing component of the Copenhagen Research Platform (CARP), an open-source family of components from DTU for building mobile-health research apps. Unlike most platforms in this module, CAMS is explicitly a **cross-platform (Flutter-based) programming framework and runtime**, not primarily a hosted dashboard product — it is distributed as the `carp_mobile_sensing` Flutter package (available on pub.dev), meaning research teams build their own study app on top of it rather than configuring an existing app through a web portal. This is a materially different adoption model than Beiwe, RADAR-base, or the commercial platforms in this module, closer in spirit to a software library than a product.

**Added under CLAUDE.md's "starting point, not a closed list" clause** — CARP was not named in the module's initial scope list but is a genuinely active, distinctive, peer-reviewed open-source competitor and was included on that basis, mirroring how Module 1 added Axivity/GENEActiv beyond its own starting list.

## Products / Platform Architecture

- **CARP Core** — the underlying study-protocol and data-model framework.
- **CARP Mobile Sensing (CAMS)** — the Flutter-based sensing runtime, providing a "reactive and unified programming model" for collecting from on-board smartphone sensors and attached off-board wearables (the project's own materials name ECG-monitor wearable integration specifically).
- **`carp_mobile_sensing`** — the distributed Flutter package implementing CAMS, on pub.dev.
- Data-transformer support for converting collected data to standardized formats and applying privacy-preserving transformations is named as a first-class framework feature.

## Sensors and Data Streams

On-board smartphone sensors plus attached wearable devices (ECG monitors named specifically) are supported, per the project's own architecture paper and site. Because CAMS is Flutter-based and explicitly cross-platform, iOS/Android sensor parity is at least a stated design goal — but this session did not independently verify parity for every individual sensor stream, and CLAUDE.md's instruction not to assume iOS/Android parity still applies even to platforms designed cross-platform from the start, since underlying OS constraints (especially iOS background execution limits) apply regardless of the app framework used.

## Derived Metrics / Analytics

Data-transformer components support standardized-format conversion and privacy-preserving transformation as part of the core framework, per the project's own materials — implying at least some built-in processing capability beyond raw pass-through, though a Forest-comparable derived-metrics catalog was not identified.

## Researcher and Study Management Features

Not a dashboard product in the way most competitors in this module are — CAMS is a library/runtime that a development team integrates into their own study app. Any study-management UI would need to be built by the adopting team or come from a separate CARP component; this was not independently verified this session.

## Data Access and Export

Standardized data-format output and privacy-preserving transformation are named framework features; exact export mechanics were not independently verified this session.

## APIs, SDKs, and Extensibility

This is CAMS's core identity and its clearest differentiator in this module: it is, by design, a programming framework/SDK rather than a configured product. Full MIT-licence source access (copyright DTU) allows unrestricted institutional modification. Real-world use spans mental health, cardiovascular disease, and diabetes mHealth applications, per the project's own "About" materials — evidence that multiple distinct research apps have been built on top of CAMS rather than it being single-study tooling.

## Deployment and Infrastructure

Not a managed SaaS — a research team integrates the `carp_mobile_sensing` package into its own Flutter app and stands up whatever backend/storage infrastructure it needs. This requires genuine mobile-development capacity (Flutter/Dart), a different and arguably higher technical floor than configuring an existing dashboard-based platform, though lower than standing up a full backend like Beiwe's or RADAR-base's if the study doesn't need custom backend infrastructure.

## Privacy, Security, and Compliance

Privacy-preserving data transformation is named as a first-class framework capability (allowing e.g. on-device or pipeline-stage anonymization/aggregation before storage), which is architecturally notable — few other platforms in this module document this as a built-in framework feature rather than a per-study custom implementation. Formal compliance certifications (GDPR/HIPAA/etc.) were not independently verified this session; DTU's EU/Denmark base makes GDPR a highly likely design consideration but this is an inference, not a verified compliance claim.

## Pricing

Free and open source (MIT licence); the only cost is the adopting team's own development and infrastructure effort — no vendor licence fee of any kind, consistent with a library/framework distribution model.

## Research Evidence and Validation

CAMS is documented in a dedicated architecture paper ("The CARP Mobile Sensing Framework — A Cross-platform, Reactive, Programming Framework and Runtime Environment for Digital Phenotyping") and has been used to build multiple distinct mHealth research applications across mental health, cardiovascular disease, and diabetes domains, per the project's own materials. This session did not attempt a systematic count of downstream published studies using apps built on CAMS.

## Strengths

- Genuinely cross-platform (Flutter) by architectural design from the outset, rather than an Android-first codebase with a later iOS port (contrast with AWARE).
- MIT licence — one of the more permissive open-source licences among the platforms profiled in this module.
- Built-in privacy-preserving data-transformation support as a first-class framework feature, not a per-study bolt-on.
- Demonstrated reuse across multiple distinct disease-domain research apps, evidencing real framework maturity rather than single-study tooling.
- Named wearable (ECG monitor) integration support alongside on-board phone sensors.

## Limitations

- Not a turnkey product — adopting CAMS means building a custom Flutter app on top of it, requiring real mobile-development capacity that most other platforms in this module (which offer a pre-built app plus a configuration dashboard) do not require.
- No researcher-facing web dashboard/study-management product was identified — this appears to be entirely the adopting team's responsibility to build.
- Full sensor-parity, export-format, and compliance-certification detail were not independently verified this session.
- Smaller apparent ecosystem/community footprint than Beiwe, RADAR-base, or AWARE in general digital-phenotyping methods literature, though this was not systematically measured.

## Best-Fit Use Cases

- Research teams with in-house Flutter/mobile-development capacity that want a proven, MIT-licensed sensing engine to build a fully custom study app on top of, rather than working within another platform's dashboard constraints.
- Studies needing genuinely first-class cross-platform (iOS/Android) sensing architecture from a single codebase.
- Studies needing wearable (e.g., ECG) integration alongside phone sensing within a unified framework.

## Poor-Fit Use Cases

- Teams without mobile-development capacity who need a configure-don't-code study app.
- Studies needing an existing, ready-to-use researcher dashboard for participant/study management out of the box.
- Rapid-timeline pilots where standing up a custom app is not feasible before enrollment.

## Open Questions

*(Directed to: CARP / Jakob Bardram's group, DTU — via https://carp.dk/)*

- Does a companion researcher dashboard/study-management product exist, or is that entirely left to the adopting team?
- What is the full current wearable-integration catalog beyond ECG monitors?
- What GDPR/compliance documentation or guidance exists for CAMS-based deployments?
- What export formats and backend-storage patterns are typical/recommended for CAMS deployments?
- How many independent research groups outside DTU have built production studies on CAMS?

## Key Links

- Official site: https://carp.dk/
- CARP Mobile Sensing (CAMS): https://carp.dk/cams/
- CARP Core: https://carp.dk/core/
- GitHub organization: https://github.com/carp-dk
- Flutter package (pub.dev): https://pub.dev/packages/carp_mobile_sensing
- About: https://carp.cachet.dk/about/

## Sources

1. Copenhagen Research Platform — official site. https://carp.dk/ (accessed 2026-08-24, search summary). **Primary.** Platform family overview.
2. CARP Mobile Sensing (CAMS) page. https://carp.dk/cams/ (accessed 2026-08-24, search summary). **Primary.** Framework architecture, data-transformer/privacy-preserving-transformation features, ECG wearable integration.
3. About — CARP. https://carp.cachet.dk/about/ (accessed 2026-08-24, search summary). **Primary.** MIT licence, DTU copyright, real-world application domains (mental health, cardiovascular disease, diabetes).
4. `carp_mobile_sensing` Flutter package. https://pub.dev/packages/carp_mobile_sensing (accessed 2026-08-24, search summary). Confirms active distribution as a Flutter package.
5. Bardram J. et al. "The CARP Mobile Sensing Framework — A Cross-platform, Reactive, Programming Framework and Runtime Environment for Digital Phenotyping." arXiv. https://arxiv.org/pdf/2006.11904 (accessed 2026-08-24, search summary). Architecture paper.
