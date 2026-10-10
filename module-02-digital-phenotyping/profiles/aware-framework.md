# AWARE Framework

## Quick Facts

| Field | Details |
|---|---|
| Organization | International academic collaboration (originated University of Oulu; contributors from University of Melbourne, Georgia Tech, CMU, and others) |
| Category | Open-source mobile context/sensing instrumentation framework |
| Current status | Active; awareframework/aware-client pushed 2026-08-07, tetujin/AWAREFramework-iOS pushed 2026-02-17, AWARE Client V3 on the App Store updated 2026-07-23 (checked 2026-10-10). The older denzilferreira/aware-client repository is archived |
| Platforms/devices | Primarily Android; an iOS port with lesser coverage (the website catalogue marks 19 of 33 modules as iOS-available). iOS clients "AWARE Client V3" (v1.7.0, 2026-07-23) and "AWARE Client V2" (v1.14.2, 2025-07-10) are on the App Store (seller Yuuki Nishiyama); the Android client is not on Google Play and is distributed from GitHub |
| Open source | Yes, **Apache-2.0** (Verified 2026-10-10 on awareframework/aware-client via the GitHub API and on tetujin/AWAREFramework-iOS from its LICENSE file; not every repo in the org was checked) |
| Hosting/deployment | Self-hosted backend only; no managed/SaaS hosting found. Android client from GitHub (not Google Play); iOS client on the App Store, needing a study server URL. |
| Pricing model | Free/open source; an Open Collective page exists for community funding |
| Last verified | 2026-10-10 (sensor catalogue recount, App Store listings, licences, repository activity) |

## Summary

- AWARE is one of the longest-running open-source mobile sensing/instrumentation frameworks in this space, an "international collaboration effort" rather than a single lab's tool, with historical roots going back to early context-aware computing research (its origin paper, "AWARE: Mobile Context Instrumentation Framework," predates most other platforms in this module). It logs, shares, and reuses "mobile context", a broad framing that covers device/environmental sensors and usage signals. It is primarily an **Android** application; an iOS port exists but is explicitly described in AWARE's own materials as different in coverage. The Android client is not on Google Play: the homepage says "You won't find AWARE on the Google Play Store" because its permissions exceed current developer guidelines, and hosts it on GitHub instead. The iOS client is on the App Store ("AWARE Client V3" and "AWARE Client V2", checked 2026-10-10).

## Products / Platform Architecture

- **AWARE Client**, the Android (primary) and iOS (port) data-collection app. Android is distributed via GitHub, not Google Play; iOS is on the App Store as AWARE Client V3 (and the older V2).
- **AWARE plugins**, a modular plugin architecture; the search evidence shows active 2026 commit activity specifically on iOS sensor plugins, suggesting ongoing iOS-side investment even though Android remains primary.
- **AWARE Framework GitHub organization**, hosts the client and plugin repositories.
- An Open Collective page (https://opencollective.com/aware-framework) indicates a community/donation-based sustainability model rather than institutional grant funding alone.

## Sensors and Data Streams

- Every Module 2 profile uses the same table so platforms can be compared row by row. Rows are the passive streams named in `CLAUDE.md`. "Yes" and "No" are used only where a primary source says so; "Unclear" means nothing current was verified, and "No (OS)" means the operating system does not expose the stream to any third-party app. Confidence and sources are stated under the table. The convention is recorded in [`../../shared/profile-table-conventions.md`](../../shared/profile-table-conventions.md).

| Stream | Android | iOS | Raw or derived | Sampling configurable | Notes |
|---|---|---|---|---|---|
| GPS / location | Yes | Yes | Raw | Yes | The iOS client has Location, FusedLocations and Visit modules and keeps itself alive through Always location. The website catalogue also marks Locations as iOS-available (re-read 2026-10-10). |
| Accelerometer | Yes | Yes | Raw | Yes |  |
| Gyroscope | Yes | Yes | Raw | Yes |  |
| Magnetometer | Yes | Yes | Raw | Yes |  |
| Barometer | Yes | Yes | Raw | Yes |  |
| Ambient light | Yes | No | Raw | Yes |  |
| Proximity | Yes | Yes | Raw | Yes | From the iOS repository (Proximity module); the website catalogue marks Proximity Android only, so this one conflict between catalogue and code stands. |
| Device motion / activity recognition | Yes | Yes | Raw. Gravity, linear accelerometer and rotation modules. | Yes | No OS activity labels in the catalogue. |
| Screen state | Yes | Yes | Event | Yes |  |
| App usage | Yes | No | Event. Applications and Installations modules. | Yes |  |
| Battery / charging | Yes | Yes | Event | Yes |  |
| Network / connectivity | Yes | Yes | Event | Yes |  |
| Wi-Fi | Yes | Yes | Scan | Yes |  |
| Bluetooth | Yes | Yes | Scan | Yes |  |
| Calls (metadata) | Yes | Partial | Metadata. Communication and Telephony modules on Android. | Yes | The iOS Calls module uses CXCallObserver, which reports call events only while the app runs, with no history and no numbers. The catalogue marks Communication iOS-available and Telephony Android only. |
| SMS (metadata) | Yes | No (OS) | Metadata | Yes |  |
| Keyboard | Yes | No | Event | Yes |  |
| Audio / microphone | Unclear | Unclear | Unclear | Unclear | Not in the core catalogue fetched; plugins exist outside it. |
| Notifications | Unclear | No | Unclear | Unclear | Not listed as a core module. |
| Device information | Yes | Yes | Event. The Aware core module. | Yes |  |

**Correction 2026-10-09 (Verified, conflict recorded).** The AWARE iOS repository (https://github.com/tetujin/AWAREFramework-iOS, last push 2026-02-17) lists Location, Proximity and Call among its default iOS sensors, and its source tree has `Location`, `FusedLocations`, `Visit`, `Proximity` and `Calls` modules; awareframework.com/locations/ also has an iOS section. The website's sensors catalogue agrees for Locations and Communication (both marked iOS) but marks Proximity and Telephony Android only. The repository is the primary source for what the iOS client does, so the stream table above follows it. Found while researching unresolved question 119. **Corrected 2026-10-10:** the 2026-08-24 reading of the catalogue as Location-Android-only was a misreading; both the live page and its 2026-08-12 Wayback snapshot mark Locations with Android and iOS icons.

**Verification.** Verified 2026-10-10 from awareframework.com/sensors (the page's platform icons parsed from its HTML), which lists 33 modules; 19 are marked available on iOS (Accelerometer, Aware, Barometer, Battery, Bluetooth, Communication, ESM/EMA, Gravity, Gyroscope, Linear Accelerometer, Locations, Magnetometer, Network, Processor, Rotation, Scheduler, Screen, Timezone, WiFi) and 14 are Android only (Applications, Installations, Light, MQTT, Keyboard, Proximity, Screenshot, Screentext, Telephony, Touch, Temperature, Text-2-Speech, Sensor, Google Fit). The 2026-08-24 reading had the counts reversed ("roughly 14 on iOS"). Sampling configurability is Reported from the framework's study-configuration model rather than checked per module. Of the modules outside this table, Processor, Scheduler and Timezone are iOS-available; Screenshot, Screentext, Touch, Temperature, Text-2-Speech, MQTT and Google Fit are Android only.

### Notes from earlier verification passes

- **Second-pass update (2026-08-24): direct-fetched from https://awareframework.com/sensors/, resolving unresolved-question #88.** AWARE's documented core sensor/plugin catalog and per-platform availability. **Corrected 2026-10-10:** the iOS column below was misread on 2026-08-24. The live catalogue (and its 2026-08-12 Wayback snapshot) marks Communication, Locations, Processor and Scheduler as iOS-available as well; the corrected values are shown, with the 2026-08-24 value in brackets where it differed. The catalogue also lists a "Sensor" module (Android only) not in this table.

| Sensor | Android | iOS |
|---|---|---|
| Accelerometer | Yes | Yes |
| Applications | Yes | No |
| Aware (core) | Yes | Yes |
| Barometer | Yes | Yes |
| Battery | Yes | Yes |
| Bluetooth | Yes | Yes |
| Communication (calls/SMS metadata) | Yes | Yes (was No) |
| ESM/EMA | Yes | Yes |
| Gravity | Yes | Yes |
| Gyroscope | Yes | Yes |
| Installations | Yes | No |
| Light | Yes | No |
| Linear Accelerometer | Yes | Yes |
| Locations | Yes | Yes (was No) |
| Magnetometer | Yes | Yes |
| MQTT | Yes | No |
| Network | Yes | Yes |
| Keyboard | Yes | No |
| Processor | Yes | Yes (was No) |
| Proximity | Yes | No |
| Rotation | Yes | Yes |
| Scheduler | Yes | Yes (was No) |
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

- **Superseded in part 2026-10-09:** Locations, Proximity and Calls do exist in the iOS client (see the correction above), so the website catalogue understates iOS. App usage, SMS, keyboard, light, screenshot and screentext remain Android only. Original 2026-08-24 text follows, kept for provenance but **wrong on the counts** (corrected 2026-10-10: 19 of 33 modules are iOS-available, and Locations is one of them). Of roughly 33 documented sensor/plugin modules, only about 14 are available on iOS, the large majority (including **Locations**, the single most commonly used passive-sensing stream in digital phenotyping) are **Android-only**. This is a materially larger and more consequential gap than the profile's earlier general "iOS differs" language conveyed: a study relying on GPS/location, app usage, call/SMS metadata, or keyboard-derived signals **cannot get that data from AWARE's iOS client at all**, not just a reduced version of it. Notably, **ESM/EMA is available on both platforms**, confirming AWARE does have a first-party survey module (resolves the "Active Data Collection" open question below in the affirmative).

## Derived Metrics / Analytics

- Not verified in any pass to date.

## Active Data Collection

- **Second-pass update (2026-08-24, Verified):** AWARE does include a first-party **ESM/EMA sensor module**, confirmed on both Android and iOS in the official sensor catalog (https://awareframework.com/sensors/). The exact scheduling/branching sophistication of this module relative to Beiwe's or mindLAMP's survey engines was not benchmarked this session, that finer-grained comparison remains open, but the existence of a native module (not a dependency on external tooling) is now Verified rather than open.

## Researcher and Study Management Features

- Not independently verified this session. AWARE's long academic history (multiple contributing universities) suggests a plugin/extension model for study-specific needs rather than a unified commercial dashboard, but this is inference from the project's structure, not a confirmed feature list.

## Data Access and Export

- Not independently verified this session.

## Wearable integration (added 2026-10-10)

- The iOS framework (tetujin/AWAREFramework-iOS) has a `Fitbit` sensor module in `AWAREFramework/Classes/Sensors`, and an AWARE watchOS framework (`com.awareframework.ios.sensor.applewatch`) for Apple Watch exists and is used by CARP's `carp_aware_package`. Android wearable plugin coverage was not itemized. **Verified** from the repository listing and the CARP README, 2026-10-10.

## APIs, SDKs, and Extensibility

- The plugin architecture is AWARE's most distinctive and well-documented characteristic across its research history, it was explicitly designed for "logging, sharing and reusing mobile context," implying a first-class extension model for adding new sensors or behaviors. This is a genuine differentiator among the platforms in this module: AWARE's plugin ecosystem reflects contributions from many independent academic groups over a long period, rather than one lab's roadmap.

## Deployment and Infrastructure

- Self-hosted backend. The **Android** client is distributed via GitHub rather than Google Play because AWARE's research-grade permission requirements exceed current Play developer policy (per the AWARE homepage), so Android participants must sideload it. The **iOS** client is on the App Store ("AWARE Client V3", v1.7.0, updated 2026-07-23; "AWARE Client V2", v1.14.2, 2025-07-10; seller Yuuki Nishiyama; Verified 2026-10-10 via the iTunes lookup API) and is pointed at the study's server. Corrected 2026-10-10: earlier text said AWARE was not on any app store.

- **Second-pass update (2026-08-24):** direct fetch of the official site confirms study configuration is handled through a dedicated **AWARE-Configurator** tool (https://awareframework.com/configurator/, also on GitHub as `AWARE-Configurator`, Apache-2.0, JavaScript). No managed/SaaS hosting offering was found anywhere on the official site, self-hosting the backend remains, as far as this session could confirm, the only deployment path. A companion analysis tool, **RAPIDS** (https://awareframework.com/rapids/), is referenced for post-collection data analysis, distinct from the collection pipeline itself.

## Participant Experience

- Not verified in any pass to date.

### Background keepalive (added 2026-10-09)

- **Yes on iOS, off by default.** AWARE-iOS supports "Continuous Silent Push Notification". A server sends silent pushes with no visible alert, which "monitor the status of running sensors" and ask the app to reopen. AWARE's tutorial says pushes generally arrive within 10 minutes.
- It is off by default: `status_push_notification` is false and the server address is blank. Studies using the App Store client must ask the AWARE developers for a server URL. Custom builds on AWARE-iOS host their own Node.js `aware-push` server, which relays commands through APNs.
- This is the closest match to Beiwe's mechanism in this module, though it uses silent rather than visible pushes. No Android equivalent was found; the Android client relies on its own service. Tutorial posted 2020-02-14, updated 2025-02-06.
- Status: **Verified** for iOS from AWARE's own page, 2026-10-09. Sources 6 and 7.

## Privacy, Security, and Compliance

- Not independently verified this session.

## Pricing

- Free and open source; no hosted service, academic program or paid tier exists (none found 2026-10-10). An Open Collective community-funding page exists, suggesting the project relies at least partly on voluntary community/donation support for sustainability rather than a single well-funded institutional grant, worth noting as a maintenance-continuity consideration relative to platforms backed by a specific well-resourced lab or company.

## Research Evidence and Validation

- AWARE has a long academic pedigree and is referenced as a comparison baseline in numerous digital-phenotyping methods papers (e.g., named alongside Beiwe, Purple Robot, and RADAR-base in platform-comparison literature). This session did not attempt a systematic publication count for AWARE specifically.

## Strengths

- One of the most extensible, plugin-based architectures in this module, with a long multi-institution contribution history.
- Actively maintained in 2026 (verified commit activity, including on iOS sensor plugins specifically).
- Fully open source with no licence fee.
- Long-standing reference point in the digital-phenotyping methods literature, giving it broad academic familiarity.

## Limitations

- Primarily an Android framework. The website catalogue marks 14 of 33 modules as Android only; the iOS repository also runs Proximity and Calls. App usage, SMS, keyboard, installations, screenshot and screentext remain Android only (corrected 2026-10-10).
- The Android client is not on Google Play, so Android participants must sideload it from GitHub; the iOS client is on the App Store (corrected 2026-10-10).
- Community/donation-based funding model (Open Collective) may imply less institutional continuity guarantee than a lab- or company-backed platform, this is a plausible risk factor, not a confirmed maintenance problem.
- Study-management/dashboard features (beyond the AWARE-Configurator study-config tool), data export mechanics, and compliance posture remain **not independently verified against current documentation** even after this second pass, the AWARE-Configurator repository and awareframework.com's Configurator/RAPIDS pages would be the next direct-fetch target for a third pass.

## Best-Fit Use Cases

- Studies needing a highly extensible, plugin-customizable Android-first passive-sensing framework, especially where the research team has engineering capacity to build or adapt plugins.
- Teams already familiar with AWARE from its extensive use in the methods literature as a reference/comparison platform.

## Poor-Fit Use Cases

- iOS-primary or iOS/Android-parity-critical study designs that need app usage, SMS metadata, keyboard or other Android-only streams. Location, proximity and call events are available on iOS (corrected 2026-10-09), though iOS call data has no history.
- ~~Any study whose primary outcome measure is GPS/location and that needs iOS participants.~~ Withdrawn 2026-10-09: the iOS client collects location.
- Android-heavy studies wanting a Play-Store-distributed participant experience without sideloading.

## Open Questions

- *(Directed to: AWARE Framework maintainers, via https://github.com/awareframework or https://opencollective.com/aware-framework)*

- ~~What is the current, complete sensor/plugin catalog, and exactly how does iOS coverage differ from Android?~~ **Resolved 2026-08-24**, see the sensor table above (Verified, direct fetch).
- ~~Is there a first-party survey/EMA module, or does active data collection require external tooling?~~ **Resolved 2026-08-24**, yes, ESM/EMA is a native module on both platforms (Verified).
- What study-management/dashboard functionality exists for researchers beyond the AWARE-Configurator study-configuration tool, if any?
- What data export formats, retention behavior, and backend hosting requirements exist for a self-hosted deployment?
- What specific open-source licence governs each individual repository? (Apache-2.0 is confirmed on `aware-client` and on AWAREFramework-iOS, 2026-10-10, but not every one of the org's repositories was checked.)
- What is the realistic sustainability/maintenance outlook given the Open Collective funding model?

## Key Links

- Official site: https://awareframework.com/
- AWARE Client V3 (App Store): https://apps.apple.com/us/app/aware-client-v3/id6781949744
- AWARE Client V2 (App Store): https://apps.apple.com/us/app/aware-client-v2/id1455986181
- iOS framework repository: https://github.com/tetujin/AWAREFramework-iOS
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
6. AWARE Framework, "Continuous Silent Push Notification (SPN) on AWARE iOS." https://www.awareframework.com/continuous-silent-push-notification-spn-on-aware-ios/ (accessed 2026-10-09). **Primary/Direct.**
7. `tetujin/aware-push`, Node.js APNs relay for AWARE-iOS. https://github.com/tetujin/aware-push (accessed 2026-10-09, search summary).
8. AWARE Framework, Sensors catalogue, re-read with the platform icons parsed from the page HTML. https://awareframework.com/sensors/ (accessed 2026-10-10); Wayback snapshot https://web.archive.org/web/20260812101026/https://awareframework.com/sensors/ cited by the 2026-10-10 independent review. **Primary/Verified.** 33 modules, 19 iOS-marked, 14 Android only.
9. iTunes lookup API, AWARE Client V3 (id 6781949744) and AWARE Client V2 (id 1455986181) (accessed 2026-10-10). **Primary/Verified.**
10. GitHub API: awareframework/aware-client (Apache-2.0, pushed 2026-08-07), tetujin/AWAREFramework-iOS (pushed 2026-02-17; LICENSE Apache 2.0; Sensors directory listing), denzilferreira/aware-client (archived) (accessed 2026-10-10). **Primary/Verified.**
11. AWARE Framework homepage, "How to get AWARE" (accessed 2026-10-10). **Primary.** Not on Google Play; Android client hosted on GitHub.
12. `carp-dk/carp.sensing-flutter` README (accessed 2026-10-10). **Primary.** `carp_aware_package` uses the AWARE watchOS framework for Apple Watch.
