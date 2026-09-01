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
| Last verified | 2026-08-25 (second pass) |

## Summary

CARP Mobile Sensing (CAMS) is the sensing component of the Copenhagen Research Platform (CARP), an open-source family of components from DTU for building mobile-health research apps. Unlike most platforms in this module, CAMS is explicitly a **cross-platform (Flutter-based) programming framework and runtime**, not primarily a hosted dashboard product — it is distributed as the `carp_mobile_sensing` Flutter package (available on pub.dev), meaning research teams build their own study app on top of it rather than configuring an existing app through a web portal. This is a materially different adoption model than Beiwe, RADAR-base, or the commercial platforms in this module, closer in spirit to a software library than a product.

**Added under CLAUDE.md's "starting point, not a closed list" clause** — CARP was not named in the module's initial scope list but is a genuinely active, distinctive, peer-reviewed open-source competitor and was included on that basis, mirroring how Module 1 added Axivity/GENEActiv beyond its own starting list.

## Products / Platform Architecture

- **CARP Core** — the underlying study-protocol and data-model framework.
- **CARP Mobile Sensing (CAMS)** — the Flutter-based sensing runtime, providing a "reactive and unified programming model" for collecting from on-board smartphone sensors and attached off-board wearables (the project's own materials name ECG-monitor wearable integration specifically).
- **`carp_mobile_sensing`** — the distributed Flutter package implementing CAMS, on pub.dev.
- Data-transformer support for converting collected data to standardized formats and applying privacy-preserving transformations is named as a first-class framework feature.

## Sensors and Data Streams

**Materially expanded 2026-08-25 (second pass, Verified via direct fetch of `carp.dk/cams/`).** The wearable-integration catalog is substantially broader than the first pass's generic "ECG monitor" reference. Confirmed named integrations:

- **On-board phone sensors** (via CAMS "sampling packages"): apps, connectivity, communication, location, activity, weather, audio, video, image, survey data.
- **Health-platform integration**: **Apple Health and Google Health Connect** are named directly as supported data sources — a HealthKit/Health Connect integration that was not previously documented in this profile and is a genuine differentiator (few other platforms in this module have confirmed HealthKit/Health Connect integration).
- **Named wearable devices**: Movisens (Move4, EcgMove4, EdaMove4), the eSense earplug, Polar (H10, Verity Sense), Movesense (MD, Active), and the Dexcom G7 continuous glucose monitor — a far more itemized and diverse list than "ECG monitor," spanning cardiac, EDA, activity, audio-wearable, and continuous-glucose sensing.

Because CAMS is Flutter-based and explicitly cross-platform, iOS/Android sensor parity is at least a stated design goal — but this session still did not independently verify parity for every individual sensor stream, and CLAUDE.md's instruction not to assume iOS/Android parity still applies even to platforms designed cross-platform from the start, since underlying OS constraints (especially iOS background execution limits) apply regardless of the app framework used.

## Derived Metrics / Analytics

Data-transformer components support standardized-format conversion and privacy-preserving transformation as part of the core framework, per the project's own materials — implying at least some built-in processing capability beyond raw pass-through, though a Forest-comparable derived-metrics catalog was not identified.

## Researcher and Study Management Features

**Updated 2026-08-25 (second pass, Verified via direct fetch of `github.com/carp-dk`) — this materially changes the prior "not a dashboard product" characterization.** The `carp-dk` GitHub organization (42 repositories total) includes several components beyond the CAMS sensing runtime itself:

- **`carp-portal`** — a JavaScript-based repository whose name and presence indicate a researcher-facing portal/dashboard component exists as part of the broader CARP platform family, distinct from the CAMS Flutter sensing package. Its feature completeness and documentation quality were not independently verified this session — its existence, not its depth, is the confirmed finding.
- **`carp-cli`** — a terminal client "with a native protocol editor," suggesting a command-line route to defining and managing study protocols without a GUI.
- **`carp-webservices-spring`** — a REST-based backend service (Kotlin/Spring Boot), implying a maintained server-side API layer exists for CARP deployments generally.
- **`carp.core-kotlin`** — described as an "infrastructure-agnostic framework for distributed data collection," i.e., the underlying study-protocol/data-model layer CAMS itself sits on top of.
- **`carp_study_app`** — a reference/example study app built on CAMS.

**Revised conclusion**: CARP is still fundamentally a framework/library-first ecosystem rather than a single polished turnkey product, and a research team should not assume `carp-portal` is a mature, feature-complete, documented dashboard equivalent to Beiwe's or Avicenna's — that was not established. But it is no longer accurate to say study-management tooling is "not offered" or "entirely the adopting team's responsibility to build" — CARP's own organization maintains portal, CLI, and backend-service components alongside the sensing library.

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

CAMS is documented in a dedicated architecture paper ("The CARP Mobile Sensing Framework — A Cross-platform, Reactive, Programming Framework and Runtime Environment for Digital Phenotyping") and has been used to build multiple distinct mHealth research applications across mental health, cardiovascular disease, and diabetes domains, per the project's own materials. **New 2026-08-25 (second pass, search-summary):** a follow-up demonstration paper, "The CARP Mobile Sensing Framework — Demonstration," was presented at the **2025 ACM International Joint Conference on Pervasive and Ubiquitous Computing (UbiComp/ISWC 2025)** — evidence of continued, current academic engagement with the framework at a major venue, five years after the original 2020 architecture paper. This session did not confirm the authors' institutional affiliation for the 2025 paper (i.e., whether it demonstrates DTU-external use or is authored by the same DTU group), so it should not yet be read as resolving the "adoption outside DTU" open question — it is evidence of currency, not external adoption. This session also did not attempt a systematic count of downstream published studies using apps built on CAMS.

## Strengths

- Genuinely cross-platform (Flutter) by architectural design from the outset, rather than an Android-first codebase with a later iOS port (contrast with AWARE).
- MIT licence — one of the more permissive open-source licences among the platforms profiled in this module. **Re-confirmed 2026-08-25** across multiple `carp-dk` repositories (`carp_study_app`, `carp.sensing-flutter`, `carp-webservices-spring`, `carp-cli`).
- Built-in privacy-preserving data-transformation support as a first-class framework feature, not a per-study bolt-on.
- Demonstrated reuse across multiple distinct disease-domain research apps, evidencing real framework maturity rather than single-study tooling; a 2025 ACM UbiComp demonstration paper indicates continued current engagement.
- **Materially expanded 2026-08-25**: named wearable integration now spans Movisens (ECG/EDA/activity), eSense, Polar, Movesense, and the Dexcom G7 CGM — not just "ECG monitor" — plus confirmed Apple Health and Google Health Connect integration, a genuine differentiator versus other platforms in this module.
- **New 2026-08-25**: a `carp-portal` repository exists, indicating a researcher-dashboard component is part of the broader CARP ecosystem, not solely the adopting team's responsibility (see Researcher and Study Management Features above for the appropriate caveats).

## Limitations

- Not a turnkey product — adopting CAMS's sensing engine still means building a custom Flutter app on top of it, requiring real mobile-development capacity that most other platforms in this module (which offer a pre-built app plus a configuration dashboard) do not require.
- ~~No researcher-facing web dashboard/study-management product was identified~~ — **revised 2026-08-25**: a `carp-portal` repository exists, but its feature completeness, documentation, and production-readiness were not independently verified this session — treat as "exists, depth unconfirmed" rather than "absent."
- Full sensor-parity (iOS vs. Android, stream-by-stream) and compliance-certification detail were not independently verified this session.
- Smaller apparent ecosystem/community footprint than Beiwe, RADAR-base, or AWARE in general digital-phenotyping methods literature — GitHub signals checked this session (84 stars / 31 forks on the core Flutter sensing repo) are modest relative to the module's larger academic platforms, though this was not systematically benchmarked star-for-star.

## Best-Fit Use Cases

- Research teams with in-house Flutter/mobile-development capacity that want a proven, MIT-licensed sensing engine to build a fully custom study app on top of, rather than working within another platform's dashboard constraints.
- Studies needing genuinely first-class cross-platform (iOS/Android) sensing architecture from a single codebase.
- Studies needing wearable (e.g., ECG) integration alongside phone sensing within a unified framework.

## Poor-Fit Use Cases

- Teams without mobile-development capacity who need a configure-don't-code study app.
- Studies needing an existing, ready-to-use, well-documented researcher dashboard for participant/study management out of the box — `carp-portal` exists (see above) but its maturity relative to Beiwe's or Avicenna's dashboards was not established this session, so this remains a caution rather than a confirmed absence.
- Rapid-timeline pilots where standing up a custom app is not feasible before enrollment.

## Open Questions

*(Directed to: CARP / Jakob Bardram's group, DTU — via https://carp.dk/)*

- ~~Does a companion researcher dashboard/study-management product exist?~~ **Resolved (existence) 2026-08-25** — `carp-portal` exists. **New sub-question**: how feature-complete and documented is `carp-portal` relative to competitors' dashboards (Beiwe's, Avicenna's)?
- ~~What is the full current wearable-integration catalog beyond ECG monitors?~~ **Resolved 2026-08-25** — see Sensors and Data Streams above (Movisens, eSense, Polar, Movesense, Dexcom G7, plus Apple Health/Google Health Connect).
- What GDPR/compliance documentation or guidance exists for CAMS-based deployments? — still unresolved; not targeted this pass beyond the CAMS feature page, which did not mention it.
- What export formats and backend-storage patterns are typical/recommended for CAMS deployments, and does `carp-webservices-spring` represent the standard/recommended backend, or one option among several?
- How many independent research groups outside DTU have built production studies on CAMS? Does the 2025 ACM UbiComp demonstration paper's author list include non-DTU institutions?

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
6. CARP Mobile Sensing (CAMS) feature page (second-pass direct fetch). https://carp.dk/cams/ (accessed 2026-08-25). **Primary/Verified.** Full named wearable-integration list (Movisens, eSense, Polar, Movesense, Dexcom G7) and confirmed Apple Health / Google Health Connect integration; no researcher dashboard mentioned on this specific page (see source 7 for the dashboard finding).
7. `carp-dk` GitHub organization (second-pass direct fetch). https://github.com/carp-dk (accessed 2026-08-25). **Primary/Verified.** Confirms `carp-portal`, `carp-cli`, `carp-webservices-spring`, `carp.core-kotlin`, and `carp_study_app` repositories; MIT licence re-confirmed across multiple repos; 42 total repositories in the organization.
8. "The CARP Mobile Sensing Framework — Demonstration." *Companion of the 2025 ACM International Joint Conference on Pervasive and Ubiquitous Computing (UbiComp/ISWC 2025)*. https://unpaywall.org/10.1145/3714394.3754442 (accessed 2026-08-25, search summary). Evidence of continued academic engagement with the framework in 2025; author affiliations not confirmed this session.
