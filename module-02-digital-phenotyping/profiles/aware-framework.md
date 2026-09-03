# AWARE Framework

## Quick Facts

| Field | Details |
|---|---|
| Organization | International academic collaboration (originated University of Oulu; contributors from University of Melbourne, Georgia Tech, CMU, and others) |
| Category | Open-source mobile context/sensing instrumentation framework |
| Current status | Active, GitHub commit activity as recently as July 2026 across multiple sensor-plugin repositories |
| Platforms/devices | Primarily Android; an iOS port exists with reportedly different/lesser feature coverage |
| Open source | Yes, **Apache-2.0** (confirmed directly on the `aware-client` and several plugin repositories; not every individual repo in the org was checked) |
| Hosting/deployment | Self-hosted client + backend; distributed via GitHub, not app stores. No managed/SaaS hosting offering found on the official site. |
| Pricing model | Free/open source; an Open Collective page exists for community funding |
| Last verified | 2026-08-24 (second-pass direct-source re-verification) |

## Summary

- AWARE is one of the longest-running open-source mobile sensing/instrumentation frameworks in this space, an "international collaboration effort" rather than a single lab's tool, with historical roots going back to early context-aware computing research (its origin paper, "AWARE: Mobile Context Instrumentation Framework," predates most other platforms in this module). It logs, shares, and reuses "mobile context", a broad framing that covers device/environmental sensors and usage signals. It is primarily an **Android** application; an iOS port exists but is explicitly described in AWARE's own materials as different in coverage, and AWARE is not distributed through app stores because its permission requirements (needed for research-grade sensing) exceed what current app-store developer policies allow for consumer apps.

## Products / Platform Architecture

- **AWARE Client**, the Android (primary) and iOS (port) data-collection app, distributed via GitHub rather than app stores.
- **AWARE plugins**, a modular plugin architecture; the search evidence shows active 2026 commit activity specifically on iOS sensor plugins, suggesting ongoing iOS-side investment even though Android remains primary.
- **AWARE Framework GitHub organization**, hosts the client and plugin repositories.
- An Open Collective page (https://opencollective.com/aware-framework) indicates a community/donation-based sustainability model rather than institutional grant funding alone.

## Sensors and Data Streams

- Every Module 2 profile uses the same table so platforms can be compared row by row. Rows are the passive streams named in `CLAUDE.md`. "Yes" and "No" are used only where a primary source says so; "Unclear" means nothing current was verified, and "No (OS)" means the operating system does not expose the stream to any third-party app. Confidence and sources are stated under the table. The convention is recorded in [`../../shared/profile-table-conventions.md`](../../shared/profile-table-conventions.md).

| Stream | Android | iOS | Raw or derived | Sampling configurable | Notes |
|---|---|---|---|---|---|
| GPS / location | Yes | No | Raw | Yes | The single most-used stream is Android only on the documented catalogue. |
| Accelerometer | Yes | Yes | Raw | Yes |  |
| Gyroscope | Yes | Yes | Raw | Yes |  |
| Magnetometer | Yes | Yes | Raw | Yes |  |
| Barometer | Yes | Yes | Raw | Yes |  |
| Ambient light | Yes | No | Raw | Yes |  |
| Proximity | Yes | No | Raw | Yes |  |
| Device motion / activity recognition | Yes | Yes | Raw. Gravity, linear accelerometer and rotation modules. | Yes | No OS activity labels in the catalogue. |
| Screen state | Yes | Yes | Event | Yes |  |
| App usage | Yes | No | Event. Applications and Installations modules. | Yes |  |
| Battery / charging | Yes | Yes | Event | Yes |  |
| Network / connectivity | Yes | Yes | Event | Yes |  |
| Wi-Fi | Yes | Yes | Scan | Yes |  |
| Bluetooth | Yes | Yes | Scan | Yes |  |
| Calls (metadata) | Yes | No (OS) | Metadata. Communication and Telephony modules. | Yes |  |
| SMS (metadata) | Yes | No (OS) | Metadata | Yes |  |
| Keyboard | Yes | No | Event | Yes |  |
| Audio / microphone | Unclear | Unclear | Unclear | Unclear | Not in the core catalogue fetched; plugins exist outside it. |
| Notifications | Unclear | No | Unclear | Unclear | Not listed as a core module. |
| Device information | Yes | Yes | Event. The Aware core module. | Yes |  |

**Verification.** Verified 2026-08-24 from awareframework.com/sensors, which lists about 33 modules with per-platform availability; roughly 14 are available on iOS. Sampling configurability is Reported from the framework's study-configuration model rather than checked per module. Modules outside this table (Processor, Screenshot, Screentext, Touch, Temperature, Timezone, Scheduler, Text-to-speech, MQTT, Google Fit) are Android only except Timezone and Rotation.

### Notes from earlier verification passes

- **Second-pass update (2026-08-24): direct-fetched from https://awareframework.com/sensors/, resolving unresolved-question #88.** AWARE's documented core sensor/plugin catalog and per-platform availability (**Verified**, read directly from the official sensors documentation page):

| Sensor | Android | iOS |
|---|---|---|
| Accelerometer | Yes | Yes |
| Applications | Yes | No |
| Aware (core) | Yes | Yes |
| Barometer | Yes | Yes |
| Battery | Yes | Yes |
| Bluetooth | Yes | Yes |
| Communication (calls/SMS metadata) | Yes | No |
| ESM/EMA | Yes | Yes |
| Gravity | Yes | Yes |
| Gyroscope | Yes | Yes |
| Installations | Yes | No |
| Light | Yes | No |
| Linear Accelerometer | Yes | Yes |
| Locations | Yes | No |
| Magnetometer | Yes | Yes |
| MQTT | Yes | No |
| Network | Yes | Yes |
| Keyboard | Yes | No |
| Processor | Yes | No |
| Proximity | Yes | No |
| Rotation | Yes | Yes |
| Scheduler | Yes | No |
| Screen | Yes | Yes |
| Screenshot | Yes | No |
| Screentext | Yes | No |
| Telephony | Yes | No |
| Touch | Yes | No |
| Temperature | Yes | No |
| Timezone | Yes | Yes |
| WiFi | Yes | Yes |
| Text-2-Speech | Yes | No |
| Google Fit | Yes | No |

- Of roughly 33 documented sensor/plugin modules, only about 14 are available on iOS, the large majority (including **Locations**, the single most commonly used passive-sensing stream in digital phenotyping) are **Android-only**. This is a materially larger and more consequential gap than the profile's earlier general "iOS differs" language conveyed: a study relying on GPS/location, app usage, call/SMS metadata, or keyboard-derived signals **cannot get that data from AWARE's iOS client at all**, not just a reduced version of it. Notably, **ESM/EMA is available on both platforms**, confirming AWARE does have a first-party survey module (resolves the "Active Data Collection" open question below in the affirmative).

## Derived Metrics / Analytics

- Not verified in any pass to date.

## Active Data Collection

- **Second-pass update (2026-08-24, Verified):** AWARE does include a first-party **ESM/EMA sensor module**, confirmed on both Android and iOS in the official sensor catalog (https://awareframework.com/sensors/). The exact scheduling/branching sophistication of this module relative to Beiwe's or mindLAMP's survey engines was not benchmarked this session, that finer-grained comparison remains open, but the existence of a native module (not a dependency on external tooling) is now Verified rather than open.

## Researcher and Study Management Features

- Not independently verified this session. AWARE's long academic history (multiple contributing universities) suggests a plugin/extension model for study-specific needs rather than a unified commercial dashboard, but this is inference from the project's structure, not a confirmed feature list.

## Data Access and Export

- Not independently verified this session.

## APIs, SDKs, and Extensibility

- The plugin architecture is AWARE's most distinctive and well-documented characteristic across its research history, it was explicitly designed for "logging, sharing and reusing mobile context," implying a first-class extension model for adding new sensors or behaviors. This is a genuine differentiator among the platforms in this module: AWARE's plugin ecosystem reflects contributions from many independent academic groups over a long period, rather than one lab's roadmap.

## Deployment and Infrastructure

- Self-hosted; distributed via GitHub rather than app stores specifically because AWARE's research-grade permission requirements exceed current app-store consumer-app policy limits. This is a meaningful operational fact: study teams must sideload the client (or use an enterprise/ad-hoc distribution mechanism) rather than direct participants to a public app-store listing, which adds onboarding friction relative to platforms that do maintain app-store listings.

- **Second-pass update (2026-08-24):** direct fetch of the official site confirms study configuration is handled through a dedicated **AWARE-Configurator** tool (https://awareframework.com/configurator/, also on GitHub as `AWARE-Configurator`, Apache-2.0, JavaScript). No managed/SaaS hosting offering was found anywhere on the official site, self-hosting the backend remains, as far as this session could confirm, the only deployment path. A companion analysis tool, **RAPIDS** (https://awareframework.com/rapids/), is referenced for post-collection data analysis, distinct from the collection pipeline itself.

## Participant Experience

- Not verified in any pass to date.

## Privacy, Security, and Compliance

- Not independently verified this session.

## Pricing

- Free and open source. An Open Collective community-funding page exists, suggesting the project relies at least partly on voluntary community/donation support for sustainability rather than a single well-funded institutional grant, worth noting as a maintenance-continuity consideration relative to platforms backed by a specific well-resourced lab or company.

## Research Evidence and Validation

- AWARE has a long academic pedigree and is referenced as a comparison baseline in numerous digital-phenotyping methods papers (e.g., named alongside Beiwe, Purple Robot, and RADAR-base in platform-comparison literature). This session did not attempt a systematic publication count for AWARE specifically.

## Strengths

- One of the most extensible, plugin-based architectures in this module, with a long multi-institution contribution history.
- Actively maintained in 2026 (verified commit activity, including on iOS sensor plugins specifically).
- Fully open source with no licence fee.
- Long-standing reference point in the digital-phenotyping methods literature, giving it broad academic familiarity.

## Limitations

- Primarily an Android framework; **now Verified (not just self-described) that the iOS port is missing roughly 19 of ~33 documented sensor modules**, including Locations, Applications, Communication (calls/SMS), Installations, Keyboard, Screenshot, Screentext, and Telephony, several of the most research-relevant passive streams are Android-only, not merely "reduced coverage" on iOS.
- Not distributed via app stores, adding participant-onboarding friction (sideloading or enterprise distribution required).
- Community/donation-based funding model (Open Collective) may imply less institutional continuity guarantee than a lab- or company-backed platform, this is a plausible risk factor, not a confirmed maintenance problem.
- Study-management/dashboard features (beyond the AWARE-Configurator study-config tool), data export mechanics, and compliance posture remain **not independently verified against current documentation** even after this second pass, the AWARE-Configurator repository and awareframework.com's Configurator/RAPIDS pages would be the next direct-fetch target for a third pass.

## Best-Fit Use Cases

- Studies needing a highly extensible, plugin-customizable Android-first passive-sensing framework, especially where the research team has engineering capacity to build or adapt plugins.
- Teams already familiar with AWARE from its extensive use in the methods literature as a reference/comparison platform.

## Poor-Fit Use Cases

- iOS-primary or iOS/Android-parity-critical study designs, **now Verified as poor-fit, not just plausible**: iOS cannot collect location, app usage, call/SMS metadata, keyboard, or several other Android-exclusive streams at all.
- Any study whose primary outcome measure is GPS/location and that needs iOS participants, location is Android-only.
- Teams wanting a polished, app-store-distributed participant experience without custom distribution workarounds.

## Open Questions

- *(Directed to: AWARE Framework maintainers, via https://github.com/awareframework or https://opencollective.com/aware-framework)*

- ~~What is the current, complete sensor/plugin catalog, and exactly how does iOS coverage differ from Android?~~ **Resolved 2026-08-24**, see the sensor table above (Verified, direct fetch).
- ~~Is there a first-party survey/EMA module, or does active data collection require external tooling?~~ **Resolved 2026-08-24**, yes, ESM/EMA is a native module on both platforms (Verified).
- What study-management/dashboard functionality exists for researchers beyond the AWARE-Configurator study-configuration tool, if any?
- What data export formats, retention behavior, and backend hosting requirements exist for a self-hosted deployment?
- What specific open-source licence governs each individual repository? (Apache-2.0 is confirmed on `aware-client` and several plugin repos, but not every one of the org's 97 repositories was checked.)
- What is the realistic sustainability/maintenance outlook given the Open Collective funding model?

## Key Links

- Official site: https://awareframework.com/
- Sensors documentation: https://awareframework.com/sensors/
- Plugins documentation: https://awareframework.com/plugins/
- Study Configurator: https://awareframework.com/configurator/
- RAPIDS (companion analysis tool): https://awareframework.com/rapids/
- GitHub organization: https://github.com/awareframework
- Open Collective (funding): https://opencollective.com/aware-framework

## Sources

1. AWARE Framework, official site. https://awareframework.com/ (accessed 2026-08-24). Platform framing, Android-primary/iOS-port distinction, app-store distribution constraint, international-collaboration origin, Configurator/RAPIDS tool references.
2. AWARE Framework, Sensors documentation (**direct fetch, second pass**). https://awareframework.com/sensors/ (accessed 2026-08-24). **Primary/Verified.** Complete per-sensor Android-vs-iOS availability table; resolves unresolved-question #88 and the Active Data Collection open question.
3. AWARE Framework GitHub organization. https://github.com/awareframework (accessed 2026-08-24, direct fetch second pass). Repository inventory (97 total repos), Apache-2.0 licence confirmed on `aware-client` and named plugin repos, commit activity as recently as Aug 2026.
4. AWARE Framework, Open Collective. https://opencollective.com/aware-framework (accessed 2026-08-24, search summary). Community-funding model.
5. Ferreira D. et al. "AWARE: Mobile Context Instrumentation Framework." Foundational project paper (ResearchGate listing). https://www.researchgate.net/publication/275349654_AWARE_Mobile_Context_Instrumentation_Framework (accessed 2026-08-24, search summary). Historical/architectural origin, used only to establish AWARE's long pedigree, not for current-state claims.
