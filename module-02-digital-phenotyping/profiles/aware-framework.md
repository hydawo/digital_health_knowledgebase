# AWARE Framework

## Quick Facts

| Field | Details |
|---|---|
| Organization | Managed by a team in the University of Melbourne's School of Computing and Information Systems (Dr Simon D'Alfonso, Prof Vassilis Kostakos); created by Denzil Ferreira in his PhD [14]. Earlier profile text placed its origin at the University of Oulu, with contributors from other universities |
| Category | Open-source mobile context/sensing instrumentation framework |
| Current status | Active; Android stable 4.2.1 (2025-05-26) and beta 4.7.3 (GitHub release 2026-08-07), about 40 iOS sensor-module repositories pushed June and July 2026, AWARE Client V3 on the App Store updated 2026-07-23 (checked 2026-10-11) [10][22]. In January 2025 AWARE-Light became the main Android AWARE and the original client became AWARE Legacy (denzilferreira/aware-client, archived 2023-06-18) [15] |
| Platforms/devices | Primarily Android; an iOS port with lesser coverage (the website catalogue marks 19 of 33 modules as iOS-available). iOS clients "AWARE Client V3" (v1.7.0, 2026-07-23) and "AWARE Client V2" (v1.14.2, 2025-07-10) are on the App Store (seller Yuuki Nishiyama); the Android client is not on Google Play and is distributed from GitHub |
| Open source | Yes. **Apache-2.0** for the Android client, AWARE Micro server, configurator and AWAREFramework-iOS. The iOS V2 app repository has no LICENSE file but its README states Apache 2.0; many new iOS sensor-module repositories have no detected licence and one (calendar) is MIT; RAPIDS is AGPL-3.0. No public source repository for the V3 app was found (Verified 2026-10-11) [25] |
| Hosting/deployment | Self-hosted, or a paid hosting service run by the University of Melbourne team, arranged by contacting Dr Simon D'Alfonso [13]. Android uploads to a researcher-run MySQL 5.x server; iOS and AWARE Legacy upload to a self-run AWARE Micro server [17][21]. Android client from GitHub (not Google Play); iOS client on the App Store. |
| Pricing model | Software free (Apache 2.0, commercial and research use). Paid dedicated support and paid hosting exist, price not published, by contact (2026-10-11) [13]. Open Collective has raised USD 16.82 in total (checked 2026-10-11) [4] |
| Last verified | 2026-10-11 (vendor fact record); sensor catalogue recount 2026-10-10 |

## Summary

- AWARE is one of the longest-running open-source mobile sensing/instrumentation frameworks in this space, an "international collaboration effort" rather than a single lab's tool, with historical roots going back to early context-aware computing research (its origin paper, "AWARE: Mobile Context Instrumentation Framework," predates most other platforms in this module). It logs, shares, and reuses "mobile context", a broad framing that covers device/environmental sensors and usage signals. It is primarily an **Android** application; an iOS port exists but is explicitly described in AWARE's own materials as different in coverage. The Android client is not on Google Play: the homepage says "You won't find AWARE on the Google Play Store" because its permissions exceed current developer guidelines, and hosts it on GitHub instead. The iOS client is on the App Store ("AWARE Client V3" and "AWARE Client V2", checked 2026-10-10).
- The project is now run by a team at the University of Melbourne, which also sells dedicated study support and study hosting by contact, with no published price [13][14].

## Products / Platform Architecture

- **AWARE Client**, the Android (primary) and iOS (port) data-collection app. Android is distributed via GitHub, not Google Play; iOS is on the App Store as AWARE Client V3 (and the older V2).
- **AWARE plugins**, a modular plugin architecture; the search evidence shows active 2026 commit activity specifically on iOS sensor plugins, suggesting ongoing iOS-side investment even though Android remains primary.
- **AWARE Framework GitHub organization**, hosts the client and plugin repositories.
- An Open Collective page (https://opencollective.com/aware-framework) exists but has raised USD 16.82 in total (checked 2026-10-11) [4]. The project's revenue route is the University of Melbourne team's paid support and hosting service, with payment going back into AWARE's development [13].
- **AWARE Client V3 (iOS)**, released on the App Store 2026-06-28, built on new Swift sensor modules in the awareframework org. awareframework.com still links only V2 and has not announced V3 (checked 2026-10-11) [18][22].
- **AWARE Micro**, the server iOS and AWARE Legacy clients upload to; it is not compatible with the old dashboard at api.awareframework.com, which no longer resolves [21].

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
| Device motion / activity recognition | Yes | Yes | Raw. Gravity, linear accelerometer and rotation modules. iOS also Derived (activity labels). | Yes | The website catalogue lists no OS activity labels, but iOS V3 records activity recognition labels, significant motion and AirPods head motion, and V2 lists activity recognition [18]. |
| Screen state | Yes | Yes | Event | Yes |  |
| App usage | Yes | No | Event. Applications and Installations modules. | Yes |  |
| Battery / charging | Yes | Yes | Event | Yes |  |
| Network / connectivity | Yes | Yes | Event | Yes |  |
| Wi-Fi | Yes | Yes | Scan | Yes |  |
| Bluetooth | Yes | Yes | Scan | Yes |  |
| Calls (metadata) | Yes | Partial | Metadata. Communication and Telephony modules on Android. | Yes | The iOS Calls module uses CXCallObserver, which reports call events only while the app runs, with no history and no numbers. The catalogue marks Communication iOS-available and Telephony Android only. |
| SMS (metadata) | Yes | No (OS) | Metadata | Yes |  |
| Keyboard | Yes | Partial | Event | Yes | Android logs keystrokes on any keyboard and needs Accessibility access [24]. iOS V3 sees only typing on AWARE's own bundled keyboard, which needs Full Access; its default mode stores metadata only and masks key and text fields [18]. |
| Audio / microphone | Unclear | Yes | Derived. Decibel values and optional environmental sound labels on iOS. | Unclear | iOS V3 added ambient noise in a version update and V2 lists ambient noise features [18]. Not in the Android core catalogue; plugins exist outside it. |
| Notifications | Yes | Partial | Event | Unclear | Android has a Notifications sensor that needs Accessibility access [24]. The iOS V3 notification module records only the app's own pushes received in the foreground, not other apps' notifications [18]. |
| Device information | Yes | Yes | Event. The Aware core module. | Yes |  |

**Correction 2026-10-09 (Verified, conflict recorded).** The AWARE iOS repository (https://github.com/tetujin/AWAREFramework-iOS, last push 2026-02-17) lists Location, Proximity and Call among its default iOS sensors, and its source tree has `Location`, `FusedLocations`, `Visit`, `Proximity` and `Calls` modules; awareframework.com/locations/ also has an iOS section. The website's sensors catalogue agrees for Locations and Communication (both marked iOS) but marks Proximity and Telephony Android only. The repository is the primary source for what the iOS client does, so the stream table above follows it. Found while researching unresolved question 119. **Corrected 2026-10-10:** the 2026-08-24 reading of the catalogue as Location-Android-only was a misreading; both the live page and its 2026-08-12 Wayback snapshot mark Locations with Android and iOS icons.

**Verification.** Verified 2026-10-10 from awareframework.com/sensors (the page's platform icons parsed from its HTML), which lists 33 modules; 19 are marked available on iOS (Accelerometer, Aware, Barometer, Battery, Bluetooth, Communication, ESM/EMA, Gravity, Gyroscope, Linear Accelerometer, Locations, Magnetometer, Network, Processor, Rotation, Scheduler, Screen, Timezone, WiFi) and 14 are Android only (Applications, Installations, Light, MQTT, Keyboard, Proximity, Screenshot, Screentext, Telephony, Touch, Temperature, Text-2-Speech, Sensor, Google Fit). The 2026-08-24 reading had the counts reversed ("roughly 14 on iOS"). Sampling configurability is Reported from the framework's study-configuration model rather than checked per module. Of the modules outside this table, Processor, Scheduler and Timezone are iOS-available; Screenshot, Screentext, Touch, Temperature, Text-2-Speech, MQTT and Google Fit are Android only.

**Vendor fact record, 2026-10-11 (Verified).** The website catalogue describes the Android client and the V2-era iOS port. AWARE Client V3 (App Store, released 2026-06-28) adds HealthKit records (heart rate, sleep, activity, workouts, ECG, activity summaries, audiograms), Apple Watch sensors, AirPods head motion, activity labels, its own keyboard, music and photo metadata, iBeacon, Shortcuts triggers and ambient noise; the V3 store listing does not mention ESM/EMA [18]. Android sampling is set per sensor; the accelerometer takes a sampling delay in microseconds (200000 normal, 60000 UI, 20000 game, 0 fastest), hardware-dependent and non-deterministic, and GPS is checked every 180 seconds by default [30]. Per-sensor iOS rates were not itemized.

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

- The clients mostly store raw records. Some sensors add higher-level context, such as calling availability in Communication [28] and activity labels on iOS [18].
- Behavioural features come from **RAPIDS**, a separate pipeline maintained outside AWARE under AGPL-3.0 [19].
- **AWARE Narrator** turns records into English statements for LLM use and can optionally send coordinates to the Google Maps API for reverse geocoding [20].
- Verified 2026-10-11 (vendor fact record).

## Active Data Collection

- **Second-pass update (2026-08-24, Verified):** AWARE does include a first-party **ESM/EMA sensor module**, confirmed on both Android and iOS in the official sensor catalog (https://awareframework.com/sensors/). The exact scheduling/branching sophistication of this module relative to Beiwe's or mindLAMP's survey engines was not benchmarked this session, that finer-grained comparison remains open, but the existence of a native module (not a dependency on external tooling) is now Verified rather than open.
- **2026-10-11 (vendor fact record):** the AWARE Client V3 App Store listing does not mention ESM/EMA, so ESM on iOS is established for V2 and AWAREFramework-iOS only [18]. Issue 56 (2025-06-08, scheduled ESMs not appearing on the stable Android client) had no reply as of 2026-10-11 [31].

## Researcher and Study Management Features

- Not independently verified this session. AWARE's long academic history (multiple contributing universities) suggests a plugin/extension model for study-specific needs rather than a unified commercial dashboard, but this is inference from the project's structure, not a confirmed feature list.
- **2026-10-11 (vendor fact record):** a study is set up by building a JSON configuration in the public configurator (configurator.awareframework.com) and sending participants its link, or by QR code on iOS. Setting up a study in the configurator requires entering the database's root credentials, which the page says it does not store permanently [17]. The old free hosted dashboard is gone [21].

## Data Access and Export

- Android phones upload directly to the researcher's MySQL 5.x database at a configured offload frequency, with no intermediate service [17].
- iOS and AWARE Legacy clients upload to a self-run AWARE Micro server [21][22].
- Data not yet uploaded sits in a local SQLite database on the phone, which can be copied off and opened with an SQLite client [16].
- No vendor API and no vendor-held copy, so history depth is whatever the study keeps (Corroborated; inferred from the architecture).
- Records can be duplicated (same device_id and timestamp); deduplicate during cleaning [26].
- Verified 2026-10-11 (vendor fact record).

## Wearable integration (added 2026-10-10)

- The iOS framework (tetujin/AWAREFramework-iOS) has a `Fitbit` sensor module in `AWAREFramework/Classes/Sensors`, and an AWARE watchOS framework (`com.awareframework.ios.sensor.applewatch`) for Apple Watch exists and is used by CARP's `carp_aware_package`. Android wearable plugin coverage was not itemized. **Verified** from the repository listing and the CARP README, 2026-10-10.
- **2026-10-11 (vendor fact record):** both iOS apps read HealthKit. V2 reads heart rate, sleep and workouts, plus BLE heart rate and Fitbit via its web API; V3 reads heart rate, sleep, activity, workouts, ECG, activity summaries and audiograms, Apple Watch sensors, and AirPods head motion [18]. The Android Google Fit module is not in the standard build and must be requested, and the Google Fit APIs it depends on are being deprecated in 2026 [27].

## APIs, SDKs, and Extensibility

- The plugin architecture is AWARE's most distinctive and well-documented characteristic across its research history, it was explicitly designed for "logging, sharing and reusing mobile context," implying a first-class extension model for adding new sensors or behaviors. This is a genuine differentiator among the platforms in this module: AWARE's plugin ecosystem reflects contributions from many independent academic groups over a long period, rather than one lab's roadmap.

## Deployment and Infrastructure

- Self-hosted backend. The **Android** client is distributed via GitHub rather than Google Play because AWARE's research-grade permission requirements exceed current Play developer policy (per the AWARE homepage), so Android participants must sideload it. The **iOS** client is on the App Store ("AWARE Client V3", v1.7.0, updated 2026-07-23; "AWARE Client V2", v1.14.2, 2025-07-10; seller Yuuki Nishiyama; Verified 2026-10-10 via the iTunes lookup API) and is pointed at the study's server. Corrected 2026-10-10: earlier text said AWARE was not on any app store.
- **Corrected 2026-10-11 (vendor fact record):** self-hosting is not the only route. The University of Melbourne team will set up and host a study on its AWARE hosting service, by arrangement with Dr Simon D'Alfonso; price, terms and capacity are not published [13]. Self-hosted Android studies need a MySQL 5.x server reachable from the internet (own, AWS, Azure or Docker); iOS and AWARE Legacy need a self-run AWARE Micro server (JVM, Docker on AWS, GCP or Azure) [17][21].
- AWARE-Light became the main Android AWARE in January 2025; the original client is now AWARE Legacy [15]. The maintainers advise keeping all participants on one version, since newer versions may not be compatible with a study's configuration file [22].
- The Google Fit add-on depends on Google Fit APIs that Google is deprecating in 2026 [27].

- **Second-pass update (2026-08-24):** direct fetch of the official site confirms study configuration is handled through a dedicated **AWARE-Configurator** tool (https://awareframework.com/configurator/, also on GitHub as `AWARE-Configurator`, Apache-2.0, JavaScript). No managed/SaaS hosting offering was found anywhere on the official site, self-hosting the backend remains, as far as this session could confirm, the only deployment path. *(Superseded 2026-10-11: the Support page offers paid hosting at the University of Melbourne [13].)* A companion analysis tool, **RAPIDS** (https://awareframework.com/rapids/), is referenced for post-collection data analysis, distinct from the collection pipeline itself.

## Participant Experience

- Android participants sideload the APK. Since May 2025 some see a Play Protect "unsafe app blocked" warning when installing [23]. On Android 13 and later a sideloaded app needs "Allow restricted settings" before Accessibility can be enabled, and Accessibility is required for the Applications, Touch, Notifications and Keyboard sensors [24].
- iOS participants install AWARE Client V3 or V2 from the App Store (free) and enrol by QR code on V3 [18].
- Participants can withdraw from the app; the 2019 privacy policy says this removes their data from the server and phone, which was not confirmed for the current client (Corroborated) [16].
- Verified 2026-10-11 (vendor fact record) unless marked.

### Background keepalive (added 2026-10-09)

- **Yes on iOS, off by default.** AWARE-iOS supports "Continuous Silent Push Notification". A server sends silent pushes with no visible alert, which "monitor the status of running sensors" and ask the app to reopen. AWARE's tutorial says pushes generally arrive within 10 minutes.
- It is off by default: `status_push_notification` is false and the server address is blank. Studies using the App Store client must ask the AWARE developers for a server URL. Custom builds on AWARE-iOS host their own Node.js `aware-push` server, which relays commands through APNs.
- This is the closest match to Beiwe's mechanism in this module, though it uses silent rather than visible pushes. No Android equivalent was found; the Android client relies on its own service. Tutorial posted 2020-02-14, updated 2025-02-06.
- Status: **Verified** for iOS from AWARE's own page, 2026-10-09. Sources 6 and 7.

## Privacy, Security, and Compliance

- **Privacy policy.** A 2019 policy (last modified 24 January 2019) has a GDPR section. It says a random 128-bit ID is generated on install, no personal identifiers are collected by design, data stays on the phone by default, encryption and obfuscation are on by default, and participants can withdraw and delete their data [16]. Corroborated, as a self-claim describing a design, not a certification.
- **Partly stale.** The policy covers clients "offered by AWARE Framework in the Play Store", which no longer exist, and describes a free hosted dashboard that is gone. Its 15-minute usage ping goes to api.awareframework.com, which no longer resolves; in the current Android source the ping runs only when the aware_donate_usage setting is "true", and that preference is commented out of the settings screen. iOS behaviour was not checked [16].
- **Sensitive-content sensors (Android).** Keyboard logs keystrokes on any keyboard, Screenshot captures full-screen images and Screentext captures on-screen text. The Screentext page says some apps expose passwords to it when the participant turns on show-password, and issue 31 on detecting and anonymizing passwords and usernames has been open since 2024-02-28 [24][31]. Relevant for ethics review, and at odds with the "no personal identifiers" design claim.
- **Data residency.** Wherever the researcher puts the server; phones upload directly to it. The hosted service is at the University of Melbourne (Australia) [13][17]. AWARE Narrator can optionally send coordinates to Google Maps, the only third-party data flow found [20].
- **Not public (2026-10-11):** HIPAA statement (a site search for HIPAA returned no pages), BAA, DPA, SOC 2 and ISO 27001, including for the hosting service, and any AI-training terms. Self-hosted deployments sit with the researcher's institution.
- **FDA:** no 510(k) or PMA records for AWARE, AWARE-Light, the University of Melbourne or the University of Oulu (openFDA, 2026-10-11) [29]. AWARE makes no medical-device claim.

## Pricing

- Software free and open source under Apache 2.0, for commercial and research use alike; both iOS apps and the Android APKs are free [13][18].
- **Corrected 2026-10-11 (vendor fact record):** a paid service exists. The University of Melbourne team offers dedicated support for setting up a study or fixing an issue, and hosting on its AWARE hosting service, with all payment going back into AWARE's development. Contact Dr Simon D'Alfonso; no price, academic rate, minimum commitment or terms are published [13].
- No access program, eligibility rule or application step [13].
- Open Collective has raised USD 16.82 in total (checked 2026-10-11), so it is not a material funding source [4].

## Research Evidence and Validation

- AWARE has a long academic pedigree and is referenced as a comparison baseline in numerous digital-phenotyping methods papers (e.g., named alongside Beiwe, Purple Robot, and RADAR-base in platform-comparison literature). This session did not attempt a systematic publication count for AWARE specifically.

## Strengths

- One of the most extensible, plugin-based architectures in this module, with a long multi-institution contribution history.
- Actively maintained in 2026 (verified commit activity, including on iOS sensor plugins specifically).
- Fully open source with no licence fee.
- Long-standing reference point in the digital-phenotyping methods literature, giving it broad academic familiarity.

## Limitations

- Primarily an Android framework. The website catalogue marks 14 of 33 modules as Android only; the iOS repository also runs Proximity and Calls. App usage, SMS, installations, screenshot and screentext remain Android only (corrected 2026-10-10). iOS keyboard data covers only AWARE's own keyboard (V3, 2026-10-11) [18].
- The Android client is not on Google Play, so Android participants must sideload it from GitHub; the iOS client is on the App Store (corrected 2026-10-10). Some Android participants see a Play Protect warning on install (since May 2025) [23].
- Maintained by one university team, with Open Collective funding negligible (USD 16.82 raised) and a paid service as the revenue route; some maintenance signals are weak, such as issue 56 with no reply (2026-10-11) [4][13][31].
- The privacy policy dates from 2019 and is partly stale, and no HIPAA, BAA, DPA, SOC 2 or ISO 27001 material is published (2026-10-11) [16].
- Android Keyboard, Screenshot and Screentext sensors can capture sensitive content, including passwords in some apps; issue 31 has been open since 2024-02-28 [24][31].
- Duplicate records (same device_id and timestamp) need deduplication [26].
- Study-management features beyond the configurator remain **not independently verified**; the old hosted dashboard is gone [21].

## Best-Fit Use Cases

- Studies needing a highly extensible, plugin-customizable Android-first passive-sensing framework, especially where the research team has engineering capacity to build or adapt plugins.
- Teams already familiar with AWARE from its extensive use in the methods literature as a reference/comparison platform.

## Poor-Fit Use Cases

- iOS-primary or iOS/Android-parity-critical study designs that need app usage, SMS metadata, system-wide keyboard data or other Android-only streams. Location, proximity and call events are available on iOS (corrected 2026-10-09), though iOS call data has no history.
- ~~Any study whose primary outcome measure is GPS/location and that needs iOS participants.~~ Withdrawn 2026-10-09: the iOS client collects location.
- Android-heavy studies wanting a Play-Store-distributed participant experience without sideloading.

## Open Questions

- *(Directed to: AWARE Framework maintainers, via https://github.com/awareframework or https://opencollective.com/aware-framework)*

- ~~What is the current, complete sensor/plugin catalog, and exactly how does iOS coverage differ from Android?~~ **Resolved 2026-08-24**, see the sensor table above (Verified, direct fetch).
- ~~Is there a first-party survey/EMA module, or does active data collection require external tooling?~~ **Resolved 2026-08-24**, yes, ESM/EMA is a native module on both platforms (Verified).
- What study-management/dashboard functionality exists for researchers beyond the AWARE-Configurator study-configuration tool, if any?
- ~~What data export formats, retention behavior, and backend hosting requirements exist for a self-hosted deployment?~~ **Resolved 2026-10-11**, see Data Access and Export and Deployment (vendor fact record).
- ~~What specific open-source licence governs each individual repository?~~ **Resolved 2026-10-11**, see Quick Facts; licences are not uniform across the org [25].
- What is the realistic sustainability/maintenance outlook? Open Collective is negligible (USD 16.82); the paid support and hosting service is the revenue route [4][13].
- What are the price, terms, DPA, BAA and residency details of the University of Melbourne hosting service? *(Directed to Dr Simon D'Alfonso, via https://awareframework.com/support/)*
- Is AWARE Client V3 replacing V2 as the supported iOS client, and do the iOS clients still send any usage ping? (2026-10-11)

## Vendor Fact Record

<!-- facts:begin -->
*Generated from the fact record by `tools/facts/generate.py`. Edit the record, not this block.*

**Research access**

| Fact | Value |
|---|---|
| Formal research or academic program (name, what it offers) | No research access program. AWARE is open-source academic software that anyone can download and self-host. The only researcher offering is a paid service from the University of Melbourne team, covering dedicated study set-up or fixing support and hosting a study on their AWARE hosting service, arranged by contacting Dr Simon D'Alfonso. [V, 2026-10-11] |
| Who can join the research program | n/a |
| How to apply, and any approval or review step | n/a |
| Whether the program is active, paused, renamed or closed | n/a |
| Whether the general developer or API program is open to new applicants | Open source with no developer program or sign-up. Actively maintained by a team in the University of Melbourne's School of Computing and Information Systems (Dr Simon D'Alfonso, Prof Vassilis Kostakos); AWARE was created by Denzil Ferreira in his PhD, co-supervised by Kostakos and Anind K. Dey. Android stable is 4.2.1 and beta 4.7.3 (GitHub release 2026-08-07). The iOS apps are published under Yuuki Nishiyama's developer account. Contributions go to D'Alfonso or Kostakos; community support is on Discord. [V, 2026-10-11] |
| Participant or user limits before approval or by tier | Not public [2026-10-31] |
| How academic access differs from commercial or consumer access | No difference. The Apache 2.0 licence permits commercial and research use without restriction. [V, 2026-10-11] |

**Pricing**

| Fact | Value |
|---|---|
| Device or hardware list price | n/a |
| Consumer subscription or membership price | Free. Both iOS apps (AWARE Client V3 and V2) are free on the App Store, and the Android APKs are free downloads from GitHub and awareframework.com. [V, 2026-10-11] |
| Research or academic pricing or discount | Not public [2026-10-31] |
| Fees for API, SDK, platform or data access | None for the software. All core components are open source; there is no hosted API to pay for. Costs are the researcher's own server, or the unpriced paid support and hosting services. [V, 2026-10-11] |
| Minimum order, term or commitment | Not public [2026-10-31] |
| Whether pricing requires contacting sales | Yes for the paid services. Dedicated support and the University of Melbourne hosting service are arranged by contacting Dr Simon D'Alfonso; no price is listed. The software itself is free. [V, 2026-10-11] |
| Price of managed hosting | Not public [2026-10-31] |

**Data access and terms**

| Fact | Value |
|---|---|
| Raw signals available to researchers, and by which route | **Android (AWARE, formerly AWARE-Light):** Raw phone sensor and event streams written to the researcher's own database, including accelerometer, gyroscope, magnetometer, gravity, linear accelerometer, rotation, barometer, light, proximity, temperature, locations (GPS and network), battery, Bluetooth, WiFi, network, telephony, calls and messages, applications, installations, keyboard, touch, notifications, screen, screenshot, screentext and ESM/EMA answers. Applications, touch, notifications, keyboard and screentext need Android Accessibility access. Keyboard logs keystrokes on any keyboard, Screenshot captures full screen images, and Screentext captures on-screen text. [V, 2026-10-11]<br>**iOS, AWARE Client V3 (App Store, released 2026-06-28):** Motion (accelerometer, gyroscope, gravity, magnetometer, linear accelerometer, rotation, barometer, pedometer, activity recognition labels, significant motion, AirPods head motion), device and connectivity (battery, screen, device, processor, network, Bluetooth LE, timezone, app lifecycle), HealthKit records (heart rate, sleep, activity, workouts, ECG, activity summaries, audiograms), Apple Watch sensors, music and photo metadata, keyboard metadata from AWARE's own bundled keyboard, location, Wi-Fi, iBeacon, call events, OpenWeather, notifications and Shortcuts triggers. Ambient noise (decibels and sound labels) was added in a version update. Enrolment is by QR code. [V, 2026-10-11]<br>**iOS, AWARE Client V2 (App Store, version 1.14.2) and AWAREFramework-iOS:** Location, barometer, Wi-Fi and Bluetooth; accelerometer, gyroscope, gravity, linear accelerometer, magnetometer and activity recognition; ambient noise features; screen state and call events; network; timezone; OpenWeatherMap; BLE heart rate; HealthKit heart rate, sleep and workouts; calendar; Fitbit via web API; and ESM. Some sensors are extensions that need extra Info.plist permissions and App Store review. [V, 2026-10-11] |
| Derived or processed metrics available to researchers | The clients mostly store raw records; some sensors add higher-level context (for example call availability in Communication, OS activity labels on iOS). Behavioural features come from the separate RAPIDS pipeline (AGPL-3.0, maintained outside AWARE). The AWARE Narrator tool turns records into English statements for LLM use and can optionally send coordinates to the Google Maps API for reverse geocoding. [V, 2026-10-11] |
| Documented sampling rates or temporal resolution | **Android:** Configurable per sensor. The accelerometer is set as a sampling delay in microseconds (200000 normal, 60000 UI, 20000 game, 0 fastest) and is hardware-dependent and non-deterministic. GPS location is checked every 180 seconds by default. [V, 2026-10-11] |
| How far back data can be retrieved | No vendor-held copy or limit. Phones upload straight to the researcher's own server, so history is whatever the study keeps; data not yet uploaded sits in the phone's local database. [C, 2026-10-11] |
| Export, API, SDK or file routes | Android phones upload to the researcher's MySQL database at a configured offload frequency. iOS and AWARE Legacy upload to a self-run AWARE Micro server. Local data can also be copied off the phone and opened with an SQLite client. No vendor API. [V, 2026-10-11] |
| API rate limits | n/a |
| Terms on retaining, storing or deleting data | By default the client stores data only on the phone; in a study it is uploaded to the study server. Participants can withdraw and remove their data from the server and phone from the app. Retention on the server is otherwise the researcher's decision. [C, 2026-10-11] |
| Terms on using data to train AI or ML models | Not public [2026-10-31] |
| Announced shutdowns, deprecations or migrations, with dates | In January 2025 AWARE-Light became the main Android AWARE and the original client became AWARE Legacy (denzilferreira/aware-client, archived 2023-06-18). The old free hosted dashboard at api.awareframework.com is not compatible with AWARE Micro and the host no longer resolves. The Google Fit add-on depends on Google Fit APIs that Google is deprecating in 2026. [V, 2026-10-11] |
| Software licence of the platform's components | Apache License 2.0 for the Android client, AWARE Micro server, configurator and AWAREFramework-iOS. The iOS V2 app repository has no LICENSE file, though its README states Apache 2.0. Many new iOS sensor-module repositories have no detected licence, and one (calendar) is MIT. RAPIDS, the separate feature pipeline, is AGPL-3.0. [V, 2026-10-11] |
| Self-hosting and managed-hosting options | Self-hosted, or a paid managed option. Android needs a researcher-run MySQL 5.x server reachable from the internet (own, AWS, Azure or Docker). iOS and AWARE Legacy need a self-run AWARE Micro server (JVM, Docker on AWS, GCP or Azure). The University of Melbourne team will set up and host a study on its AWARE hosting service, by arrangement. [V, 2026-10-11] |
| App store availability on iOS and Android | **Android:** Not on Google Play. Distributed as APKs from the AWARE site and GitHub and sideloaded; stable 4.2.1, beta 4.7.3. Since May 2025 some participants see a Play Protect "unsafe app blocked" warning when installing. [V, 2026-10-11]<br>**iOS:** Two free App Store apps, both published by Yuuki Nishiyama. AWARE Client V3 is the current one (released 2026-06-28, version 1.7.0 on 2026-07-23, iOS 16.6 or later). AWARE Client V2 is still listed (version 1.14.2, 2025-07-10, iOS 12 or later) and is the one awareframework.com links to. [V, 2026-10-11] |

**Compliance and regulatory**

| Fact | Value |
|---|---|
| Whether a HIPAA Business Associate Agreement is offered | Not public [2026-10-11] |
| Whether a data processing agreement is offered | Not public [2026-10-11] |
| Published HIPAA statement | Not public [2026-10-11] |
| Published GDPR statement | The 2019 privacy policy has a GDPR section. It says a random 128-bit ID is generated on install, no personal identifiers are collected by design, data stays on the phone by default, encryption and obfuscation are on by default, and participants can withdraw and delete their data. [C, 2026-10-11] |
| ISO/IEC 27001 status and evidence | Not public [2026-10-11] |
| SOC 2 status and evidence | Not public [2026-10-11] |
| FDA clearances, from the FDA database | Not public [2026-10-11] |
| Where data is stored, and residency options | Wherever the researcher puts their own server. Android phones upload directly to the researcher's MySQL server with no intermediate service. The optional hosted service is based at the University of Melbourne (Australia). [V, 2026-10-11] |

<!-- facts:end -->

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
- Support, paid service and hosting: https://awareframework.com/support/
- Team: https://awareframework.com/team/
- Privacy policy: https://awareframework.com/privacy/
- Downloads: https://awareframework.com/downloads/
- AWARE Micro server: https://github.com/awareframework/aware-micro-server

## Sources

1. AWARE Framework, official site. https://awareframework.com/ (accessed 2026-08-24). Platform framing, Android-primary/iOS-port distinction, app-store distribution constraint, international-collaboration origin, Configurator/RAPIDS tool references.
2. AWARE Framework, Sensors documentation (**direct fetch, second pass**). https://awareframework.com/sensors/ (accessed 2026-08-24). **Primary/Verified.** Complete per-sensor Android-vs-iOS availability table; resolves unresolved-question #88 and the Active Data Collection open question.
3. AWARE Framework GitHub organization. https://github.com/awareframework (accessed 2026-08-24, direct fetch second pass). Repository inventory (97 total repos), Apache-2.0 licence confirmed on `aware-client` and named plugin repos, commit activity as recently as Aug 2026.
4. AWARE Framework, Open Collective. https://opencollective.com/aware-framework (accessed 2026-08-24, search summary; total raised USD 16.82 checked 2026-10-11). Community-funding model.
5. Ferreira D. et al. "AWARE: Mobile Context Instrumentation Framework." Foundational project paper (ResearchGate listing). https://www.researchgate.net/publication/275349654_AWARE_Mobile_Context_Instrumentation_Framework (accessed 2026-08-24, search summary). Historical/architectural origin, used only to establish AWARE's long pedigree, not for current-state claims.
6. AWARE Framework, "Continuous Silent Push Notification (SPN) on AWARE iOS." https://www.awareframework.com/continuous-silent-push-notification-spn-on-aware-ios/ (accessed 2026-10-09). **Primary/Direct.**
7. `tetujin/aware-push`, Node.js APNs relay for AWARE-iOS. https://github.com/tetujin/aware-push (accessed 2026-10-09, search summary).
8. AWARE Framework, Sensors catalogue, re-read with the platform icons parsed from the page HTML. https://awareframework.com/sensors/ (accessed 2026-10-10); Wayback snapshot https://web.archive.org/web/20260812101026/https://awareframework.com/sensors/ cited by the 2026-10-10 independent review. **Primary/Verified.** 33 modules, 19 iOS-marked, 14 Android only.
9. iTunes lookup API, AWARE Client V3 (id 6781949744) and AWARE Client V2 (id 1455986181) (accessed 2026-10-10). **Primary/Verified.**
10. GitHub API: awareframework/aware-client (Apache-2.0, pushed 2026-08-07), tetujin/AWAREFramework-iOS (pushed 2026-02-17; LICENSE Apache 2.0; Sensors directory listing), denzilferreira/aware-client (archived) (accessed 2026-10-10). **Primary/Verified.**
11. AWARE Framework homepage, "How to get AWARE" (accessed 2026-10-10). **Primary.** Not on Google Play; Android client hosted on GitHub.
12. `carp-dk/carp.sensing-flutter` README (accessed 2026-10-10). **Primary.** `carp_aware_package` uses the AWARE watchOS framework for Apple Watch.
13. AWARE Framework, Support. https://awareframework.com/support/ (accessed 2026-10-11). **Primary/Verified.** Paid dedicated support and University of Melbourne hosting service, by contact with Dr Simon D'Alfonso; Discord community.
14. AWARE Framework, Team. https://awareframework.com/team/ (accessed 2026-10-11). **Primary/Verified.** University of Melbourne management; Denzil Ferreira's PhD origin.
15. AWARE Framework, "Changes to the AWARE ecosystem" (2025-01-13). https://awareframework.com/changes-to-the-aware-ecosystem/ (accessed 2026-10-11). **Primary/Verified.** AWARE-Light renamed to AWARE; original now AWARE Legacy.
16. AWARE Framework, Privacy policy (last modified 24 January 2019). https://awareframework.com/privacy/ (accessed 2026-10-11). **Primary, Corroborated (partly stale).** GDPR section, local storage, withdrawal, usage ping; current Android source `aware-client` `Aware.java` checked for the ping setting.
17. AWARE Framework, Use AWARE. https://awareframework.com/use-aware/ (accessed 2026-10-11). **Primary/Verified.** MySQL 5.x requirement, direct upload, offload frequency, configurator.
18. App Store, AWARE Client V3. https://apps.apple.com/us/app/aware-client-v3/id6781949744 and AWARE Client V2. https://apps.apple.com/us/app/aware-client-v2/id1455986181 (accessed 2026-10-11); sensor repositories https://github.com/awareframework/com.awareframework.ios.sensor.keyboard and https://github.com/awareframework/com.awareframework.ios.sensor.notification. **Primary/Verified.** V3 and V2 streams, keyboard and notification scope.
19. AWARE Framework, RAPIDS. https://awareframework.com/rapids/ and https://github.com/carissalow/rapids (accessed 2026-10-11). **Primary/Verified.** Feature pipeline, AGPL-3.0.
20. AWARE Narrator. https://awareframework.com/aware-narrator/ and https://github.com/awareframework/aware_narrator (accessed 2026-10-11). **Primary/Verified.**
21. AWARE Micro server repository. https://github.com/awareframework/aware-micro-server (accessed 2026-10-11). **Primary/Verified.** Docker deployment, capacity, incompatibility with the old dashboard.
22. AWARE Framework, Downloads, and aware-client releases. https://awareframework.com/downloads/ and https://github.com/awareframework/aware-client/releases (accessed 2026-10-11). **Primary/Verified.** Stable 4.2.1, beta 4.7.3, AWARE Micro needed for iPhone, version-compatibility advice.
23. AWARE Framework, "Unsafe app blocked". https://awareframework.com/unsafe-app-blocked/ (accessed 2026-10-11). **Primary/Verified.** Play Protect warning.
24. AWARE Framework sensor pages: Keyboard https://awareframework.com/keyboard/, Screenshot https://awareframework.com/screenshot-sensor/, Screentext https://awareframework.com/screentext/; Accessibility requirement in the aware-client README https://github.com/awareframework/aware-client (accessed 2026-10-11). **Primary/Verified.**
25. GitHub licence detection across the awareframework org, including https://github.com/awareframework/aware-micro-server/blob/master/LICENSE, https://github.com/tetujin/aware-client-ios-v2 and https://github.com/awareframework/com.awareframework.ios.sensor.calendar (accessed 2026-10-11). **Primary/Verified.**
26. AWARE Framework, Notes and advice. https://awareframework.com/notes-advice/ (accessed 2026-10-11). **Primary/Verified.** Duplicate records.
27. Google, Google Fit APIs deprecation notice. https://developers.google.com/fit (accessed 2026-10-11). **Secondary for AWARE.**
28. AWARE Framework, Communication sensor. https://awareframework.com/communication/ (accessed 2026-10-11). **Primary/Verified.**
29. openFDA 510(k) and PMA searches for AWARE Framework, AWARE-Light, University of Melbourne and University of Oulu, e.g. https://api.fda.gov/device/510k.json?search=applicant:"University+of+Melbourne" (accessed 2026-10-11). No matches.
30. AWARE Framework, Accelerometer and Locations sensor pages. https://awareframework.com/accelerometer/ and https://awareframework.com/locations/ (accessed 2026-10-11). **Primary/Verified.** Sampling settings.
31. aware-client GitHub issues 31 (open since 2024-02-28) and 56 (2025-06-08). https://github.com/awareframework/aware-client/issues/31 and https://github.com/awareframework/aware-client/issues/56 (accessed 2026-10-11). **Primary.**
