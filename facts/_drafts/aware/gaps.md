# Gap hunt: aware (AWARE Framework)

Run 2026-10-11. Compared against `module-02-digital-phenotyping/profiles/aware-framework.md` (profile),
`module-02-digital-phenotyping/comparison-matrix.md` (matrix) and `facts/aware.yaml` (every field
still `unresearched`, so every finding below is "no" against the yaml). Every quote was checked with
`tools/facts/quote_probe.py` and returned `exact` on 2026-10-11. GitHub repository and issue metadata
(dates, licences, merge state) came from the GitHub API on the same day; no issue was opened or
commented on.

## A. Contradictions and missing programs

### 1. A paid AWARE study hosting service exists, run at the University of Melbourne
- **Field:** hosting_options, hosting_price, quote_required
- **Found:** the Support page offers to set up and host a study on an AWARE hosting service at the University of Melbourne. Contact is Dr Simon D'Alfonso. No price is published.
- **URL:** https://awareframework.com/support/
- **Quote:** "we can set it up and host it for you on our AWARE hosting service based at the University of Melbourne"
- **Date:** page created 2025-01-13, modified 2025-09-29 (WordPress API); accessed 2026-10-11
- **Source type:** vendor_page
- **KB:** **contradicts.** Profile line 12 ("no managed/SaaS hosting found"), line 127 ("self-hosting the backend remains ... the only deployment path"), line 146 ("no hosted service ... exists (none found 2026-10-10)"); matrix line 72 ("**None found**"), line 86 ("AWARE has none"), line 133 (pricing: "Own infrastructure"). This makes AWARE a fifth public-source platform with a hosted route, which changes the matrix's "four public-source platforms" sentence (line 84).

### 2. A paid support service exists
- **Field:** api_platform_fees, quote_required, academic_vs_commercial
- **Found:** paid, dedicated support for study setup or fixes, with payments funding development. Contact D'Alfonso; no price published.
- **URL:** https://awareframework.com/support/
- **Quote:** "we offer a paid service option, with all payment going back into further development of AWARE"
- **Date:** modified 2025-09-29; accessed 2026-10-11
- **Source type:** vendor_page
- **KB:** **contradicts.** Profile line 146 ("no hosted service, academic program or paid tier exists"); matrix line 133 ("None", "Not applicable").

### 3. The platform is now managed by a University of Melbourne team, not an open collaboration led from Oulu
- **Field:** program_status (organization context; no dedicated schema field)
- **Found:** the Team page names a current team in Melbourne's School of Computing and Information Systems: D'Alfonso, Kostakos, four PhD candidates, a postdoc and two software engineers. The Background Primer says Denzil Ferreira created AWARE in his PhD, co-supervised by Kostakos and Anind K. Dey (the Carnegie Mellon link). The aware-client README routes contributions to D'Alfonso or Kostakos.
- **URL:** https://awareframework.com/team/ ; https://awareframework.com/background-primer/ ; https://github.com/awareframework/aware-client
- **Quote:** "The AWARE platform is currently managed by a team within the University of Melbourne’s School of Computing and Information Systems" (team); "co-supervised by Prof. Vassilis Kostakos and Prof. Anind K. Dey" (primer)
- **Date:** team modified 2025-01-14; primer modified 2025-11-06; accessed 2026-10-11
- **Source type:** vendor_page, repository
- **KB:** **contradicts (framing).** Profile line 7 and matrix line 31 describe an "International academic collaboration (originated University of Oulu)" with Melbourne only as one contributor. Ownership and the support contact are not stated anywhere in the profile.

### 4. Open Collective is negligible as a funding source
- **Field:** program_status (sustainability); api_platform_fees
- **Found:** AWARE joined the Open Source Collective (fiscal host) on 2025-10-07. The collective shows one $20 contribution (2025-11-19), $16.82 total raised and an estimated annual budget of $20. The actual sustainability routes are the paid hosting and support (findings 1 and 2) and the Melbourne team.
- **URL:** https://opencollective.com/aware-framework ; https://awareframework.com/aware-joins-the-open-source-collective/
- **Quote:** "Total raised $16.82 USD" ; "Estimated annual budget $20.00 USD" ; "We develop the AWARE smartphone sensing platform and related tools"
- **Date:** joined 2025-10-07 (post date); balance as of 2026-10-11
- **Source type:** secondary (Open Collective), vendor_page
- **KB:** **contradicts (framing).** Profile line 25 says Open Collective "indicates a community/donation-based sustainability model"; lines 146 and 163 build a risk assessment on it. The donation channel is real but nearly empty; the profile misses the paid services and the institutional team.

### 5. iOS client V3 (released 2026-06-28) collects HealthKit, Apple Watch, AirPods motion, OS activity labels, keyboard, ambient noise, notifications, photos and music
- **Field:** raw_streams, derived_metrics, app_availability
- **Found:** the App Store description of AWARE Client V3 lists HealthKit records, Apple Watch collection, AirPods head motion, Core Motion activity recognition, a keyboard sensor through a bundled custom keyboard (Full Access required, metadata-only by default), ambient noise (dB plus sound labels), push notifications, photos metadata, music, iBeacon, Shortcuts and OpenWeather. Enrolment is by QR code. Version history: 1.3 ambient noise (Jun 30), 1.4 HealthKit (Jul 1), 1.5 Apple Watch (Jul 2), 1.6 keyboard (Jul 4).
- **URL:** https://apps.apple.com/us/app/aware-client-v3/id6781949744
- **Quote:** "selected Apple Health records such as heart rate, sleep, activity, workouts, ECG, activity summaries, and audiograms" ; "walking, running, cycling, driving, or stationary" ; "supported Apple Watch sensor collection when paired with the iOS app" ; "Keyboard data collection requires enabling the bundled custom keyboard and Full Access in iOS Settings" ; "The default keyboard storage mode stores only metadata and masks the key and text fields" ; "Added Ambient Noise collection for decibel values and optional environmental sound labels" ; "Scan the QR code provided by your study administrator"
- **Date:** releaseDate 2026-06-28, v1.7.0 2026-07-23 (iTunes lookup API); accessed 2026-10-11
- **Source type:** app_store
- **KB:** **contradicts.** Profile line 40 ("No OS activity labels"), line 49 (Keyboard iOS "No"), line 50 (Audio "Unclear" on iOS), line 51 (Notifications iOS "No"), line 117 (wearables: Fitbit and Apple Watch only, no HealthKit or AirPods), line 161 and matrix line 50 (keyboard listed as Android only). Caveats for the judge: the iOS keyboard only sees typing done on AWARE's own keyboard, and the notification module records the app's own pushes (see finding 6), so these are not equivalent to the Android streams. The KB records V3's version number but not its sensor set.

### 6. A June 2026 wave of new Swift iOS sensor repositories backs the V3 feature set
- **Field:** raw_streams, licence
- **Found:** about 40 `com.awareframework.ios.sensor.*` repositories, many created 2026-06-11 and pushed 2026-07-07: keyboard, notification, airpods, uwb, photos, ambientnoise, applogger, shortcuts, music, healthkit, applewatch and others. The notification module records notifications received while the app is in the foreground (not other apps' notifications). The keyboard module reads only a custom keyboard extension.
- **URL:** https://github.com/awareframework/com.awareframework.ios.sensor.keyboard ; https://github.com/awareframework/com.awareframework.ios.sensor.notification ; https://github.com/awareframework/com.awareframework.ios.sensor.ambientnoise ; https://github.com/awareframework/com.awareframework.ios.sensor.airpods ; https://github.com/awareframework/com.awareframework.ios.sensor.photos
- **Quote:** "This sensor module captures keystroke events from a custom iOS keyboard extension and persists them to a local SQLite database" ; "It records notifications received while the app is in the foreground" ; "This sensor module captures ambient sound levels (decibels) and classifies audio using Apple's SoundAnalysis framework" ; "This sensor module collects motion data from AirPods Pro and AirPods Max" ; "This sensor module monitors the photo library using the Photos framework and detects newly added photos or videos in real time"
- **Date:** created 2026-06-11, pushed 2026-07-07 (GitHub API)
- **Source type:** repository
- **KB:** **no.** Profile line 23 mentions "2026 commit activity specifically on iOS sensor plugins" but not which streams. Profile sources point at tetujin/AWAREFramework-iOS (last push 2026-02-17), which these newer awareframework-org packages appear to supersede for V3.

### 7. A GDPR statement and a privacy policy exist (dated 2019) and describe usage telemetry
- **Field:** gdpr_statement, retention_terms, hipaa_statement
- **Found:** the privacy policy (last modified 24 January 2019) has a GDPR section: random 128-bit ID reset per study, no personal identifiers collected by design, local-first storage, encryption and obfuscation "by default", participant withdrawal and deletion from phone and server. It also says the client pings AWARE every 15 minutes (device ID, timestamp, OS, package, version) to size the free dashboard. No HIPAA statement. The policy still describes the retired free dashboard (finding 9) and Play Store packages that no longer exist, so it is stale.
- **URL:** https://awareframework.com/privacy/
- **Quote:** "Last modified 24.January 2019" ; "AWARE offers data encryption and obfuscation by default" ; "a user can withdraw and remove the collected data from the server and the mobile phone at any time, directly from his phone" ; "the client lets us know every 15 minutes that your device exists and is still using AWARE"
- **Date:** policy dated 2019-01-24; accessed 2026-10-11
- **Source type:** vendor_legal
- **KB:** **contradicts.** Matrix line 157 has "Not established" and "Not located"; profile line 142 says "Not independently verified". Self-claim cap applies (Corroborated at most). Whether the current Android client still sends the 15-minute ping is unverified.

### 8. AWARE-Light became the main AWARE in January 2025; the original is archived as "AWARE Legacy"
- **Field:** deprecations, app_availability
- **Found:** the formerly separate AWARE-Light is now the main Android AWARE; the original client is archived as AWARE Legacy (last APK 4.0.836 from denzilferreira/aware-client). Downloads still label the APKs AWARE-Light. The citation page now gives van Berkel et al. 2022, *Personal and Ubiquitous Computing*, as the AWARE-Light reference.
- **URL:** https://awareframework.com/changes-to-the-aware-ecosystem/ ; https://awareframework.com/background-primer/ ; https://awareframework.com/downloads/ ; https://awareframework.com/science/
- **Quote:** "The version of AWARE formerly known as AWARE-Light has now become the main version of AWARE, whilst the archived original AWARE is now known as AWARE Legacy" ; "AWARE Legacy, which is the last phase of the original AWARE prior to it being archived" ; "the current AWARE line descends from AWARE-Light"
- **Date:** post 2025-01-13 (modified 2025-03-17)
- **Source type:** vendor_page
- **KB:** **no** in Module 2. Profile line 9 notes denzilferreira/aware-client is archived but does not explain that the live Android client is the former AWARE-Light. Module 3 uses "AWARE-Light" as if it were a separate platform (e.g. `module-03-applied-studies/feasibility-matrix.md` line 103), which a reader can't reconcile with Module 2.

### 9. The original free hosted dashboard (api.awareframework.com) is gone; AWARE Micro replaces it and is incompatible
- **Field:** deprecations, hosting_options
- **Found:** the aware-micro-server README says it is the new AWARE server and does not work with the old dashboard at api.awareframework.com. The 2015 tutorial "Run a study with AWARE" still tells researchers to log in to that dashboard. api.awareframework.com did not respond to a HEAD request on 2026-10-11 (a timeout, not a confirmed shutdown).
- **URL:** https://github.com/awareframework/aware-micro-server ; https://awareframework.com/run-a-study-with-aware/
- **Quote:** "This is not compatible with the old dashboard located at api.awareframework.com" ; "You will need to first authenticate on AWARE's dashboard here: https://api.awareframework.com"
- **Date:** aware-micro-server pushed 2025-11-27; tutorial modified 2025-02-06
- **Source type:** repository, vendor_page
- **KB:** **no.** The profile never mentions a dashboard history or the stale tutorial. Matrix line 179 ("no researcher dashboard confirmed") is consistent, but the reason is missing.

## B. Missing detail on deployment, data and access

### 10. AWARE Micro: the current backend (Java/Vert.x, MySQL, Docker)
- **Field:** hosting_options, export_routes
- **Found:** a JVM server (OpenJDK 11, Vert.x 4.3.3) writing to MySQL, with optional LetsEncrypt TLS and a Docker recipe for AWS, GCP or Azure. Config is edited in `aware-config.json`, and clients pick up changes within 15 minutes. The Downloads page says the iOS client needs this server. Apache-2.0.
- **URL:** https://github.com/awareframework/aware-micro-server
- **Quote:** "It is compatible with the existing AWARE clients" ; "The clients will retrieve the new configuration after 15 minutes"
- **Date:** pushed 2025-11-27
- **Source type:** repository
- **KB:** **no.** The profile says only "self-hosted backend" (lines 12, 125) and asks what the backend requirements are (line 184).

### 11. Android studies write directly to the researcher's MySQL, with no intermediate service; the hosted configurator takes root DB credentials
- **Field:** data_residency, export_routes, hosting_options
- **Found:** the "Use AWARE" page says Android phones upload directly to the study's MySQL 5.x server, reachable from the internet. A study is defined on the hosted configurator (configurator.awareframework.com, plus a beta instance), which needs the database's ROOT credentials to initialise it and says it does not keep them. The configuration JSON is shared with participants by a link (Dropbox, Google Drive). Participants can view sensors, opt out, force upload and disable sensors if allowed. The page also says AWARE "runs on Android devices only", which is stale given the iOS client.
- **URL:** https://awareframework.com/use-aware/ ; https://awareframework.com/configurator/
- **Quote:** "those devices directly upload data to your MySQL server, without any intermediate servers or cloud services" ; "You will need a MySQL server (version 5.x) that is accessible over the Internet" ; "Enter the ROOT username and password" ; "The root credentials are not permanently stored by the page" ; "head to the configurator at https://configurator.awareframework.com" ; "Participants can only do a small number of things with the AWARE client"
- **Date:** use-aware modified 2025-08-04; configurator modified 2025-04-01
- **Source type:** vendor_docs
- **KB:** **no.** Profile line 113 ("Data Access and Export: Not independently verified") and open question line 184. Residency is entirely the researcher's choice, apart from the hosted option in finding 1. The configurator handling root credentials is a security consideration the KB doesn't record. Unclear: whether the INSERT-only DB credentials sit in the shared config file. A public config posted in GitHub issue #56 carries `database_password` and `database_username` fields, so it looks likely, but this is not confirmed from docs.

### 12. Known unresolved data-duplication defect
- **Field:** raw_streams, export_routes
- **Found:** the maintainers say records can appear more than once (same timestamp and device ID) and tell researchers to deduplicate. The Downloads page repeats the advice.
- **URL:** https://awareframework.com/notes-advice/
- **Quote:** "An unresolved issue with AWARE concerns duplication of data records"
- **Date:** 2025-06-11
- **Source type:** vendor_docs
- **KB:** **no.**

### 13. Android special sensors need Accessibility, including Notifications and Keyboard
- **Field:** raw_streams
- **Found:** the aware-client README says Accessibility must be on for Applications, Touch, Notifications, Keyboard, crash logs and screen reader (screentext). On Android 13+ that needs "Allow restricted settings" for a sideloaded app. This settles the Android Notifications row.
- **URL:** https://github.com/awareframework/aware-client
- **Quote:** "Accessibility needs to be turned on for AWARE for special sensors to work: Applications, Touch, Notifications, Keyboard, Crash logs, Screen reader"
- **Date:** repo pushed 2026-08-07
- **Source type:** repository
- **KB:** **contradicts (Unclear filled).** Profile line 51 marks Notifications Android "Unclear". Participant-burden sections (line 131) don't cover the Accessibility step.

### 14. Screenshot and keyboard-content capture on Android
- **Field:** raw_streams
- **Found:** the Android Screenshot sensor captures full screen images, with per-app include or exclude lists in the configurator. The Android Keyboard sensor logs keystrokes on any keyboard. Issue #31 "Sensitive information handling" (passwords, usernames) has been open since 2024-02-28.
- **URL:** https://awareframework.com/screenshot-sensor/ ; https://awareframework.com/keyboard/ ; https://github.com/awareframework/aware-client/issues/31
- **Quote:** "This sensor records screenshots that include all visual elements displayed on the screen at the moment of capture" ; "This sensor records the users' keystrokes regardless of which keyboard is used" ; "Need to detect and anonymize sensitive information, e.g., passwords, username"
- **Date:** sensor pages modified 2025-09-29 and 2025-02-06; issue opened 2024-02-28, still open 2026-10-11
- **Source type:** vendor_docs, repository
- **KB:** **no** (the profile lists Screenshot and Keyboard as Android modules, line 87/81, but nothing on what they capture or the open sensitive-data issue).

### 15. Google Fit plugin is not in the standard build, and the Google Fit APIs are deprecated in 2026
- **Field:** deprecations, raw_streams
- **Found:** AWARE's Google Fit support has to be built per study on request. Google says the Fit APIs are deprecated in 2026, with no new sign-ups since 2024-05-01.
- **URL:** https://awareframework.com/google-fit/ ; https://developers.google.com/fit
- **Quote:** "This functionality is presently not part of the standard AWARE build, so contact us if you are interested in using it" ; "The Google Fit APIs, including the Google Fit REST API, will be deprecated in 2026"
- **Date:** AWARE page 2025-01-14; Google page accessed 2026-10-11
- **Source type:** vendor_docs, secondary (third-party platform docs)
- **KB:** **no.** The profile catalogue lists Google Fit as an Android module (line 95) with no caveat.

### 16. Android distribution: Play Protect warning, stable vs beta, version pinning
- **Field:** app_availability
- **Found:** since May 2025 some Android installs trigger an "unsafe app blocked" Play Protect warning, which participants have to click past. Stable is 4.2.1 (GitHub release 2025-05-26) and beta 4.7.x (4.7.3.beta released 2026-08-07, with PR #66 for 4.8.1.beta open). The maintainers advise keeping participants on one version because newer ones may not match the study config.
- **URL:** https://awareframework.com/unsafe-app-blocked/ ; https://awareframework.com/downloads/
- **Quote:** "some Android participants might now get the following message when installing AWARE" ; "newer versions might not be compatible with your study configuration file"
- **Date:** warning post 2025-05-26; downloads modified 2026-08-17
- **Source type:** vendor_page
- **KB:** **no.** Profile line 125 covers sideloading but not the Play Protect warning or versioning.

### 17. AWARE Narrator: an LLM-oriented narrative tool, with optional Google Maps geocoding
- **Field:** derived_metrics, ai_training_terms (related)
- **Found:** a Python tool that turns AWARE records into English sentences, with DBSCAN location clustering. It can optionally send coordinates to the Google Maps API for reverse geocoding. A paper is on arXiv (2411.04691, OzCHI 2024 late-breaking work). Apache-2.0, pushed 2026-07-21.
- **URL:** https://awareframework.com/aware-narrator/ ; https://github.com/awareframework/aware_narrator
- **Quote:** "The AWARE Narrator tool converts AWARE data records into English statements that describe the records" ; "It includes Google Maps API integration for reverse geocoding"
- **Date:** page modified 2025-12-12
- **Source type:** vendor_page, repository
- **KB:** **no.** Profile line 101 ("Derived Metrics: Not verified in any pass") and nothing on Narrator anywhere in the KB.

### 18. RAPIDS is AGPL-3.0 and maintained by the University of Pittsburgh (MoSHI)
- **Field:** derived_metrics, licence
- **Found:** carissalow/rapids is AGPL-3.0, not archived, last release v1.10.1 (2025-03-17), last push 2026-03-26. That's a copyleft licence, unlike AWARE's Apache-2.0.
- **URL:** https://github.com/carissalow/rapids
- **Quote:** "AGPL-3.0 license"
- **Date:** GitHub API, 2026-10-11
- **Source type:** repository
- **KB:** **no.** Profile line 127 names RAPIDS without licence, owner or status.

### 19. Licences are not uniform across the org
- **Field:** licence
- **Found:** of the org's 98 repos, GitHub reports many iOS sensor repos as NOASSERTION or no licence (e.g. keyboard, notification, airpods, bluetooth, network). The calendar sensor is MIT, and the core and accelerometer LICENSE files are Apache-2.0 text.
- **URL:** https://github.com/awareframework/com.awareframework.ios.sensor.calendar
- **Quote:** "MIT license"
- **Date:** GitHub API, 2026-10-11
- **Source type:** repository
- **KB:** **no** (partly anticipated). Profile line 11 and open question line 185 say not every repo was checked. Profile source 3 says "97 total repos"; the API now reports 98.

### 20. Academic partner with "unrestricted access": Orygen Digital
- **Field:** academic_vs_commercial, research_program
- **Found:** Orygen (Melbourne youth mental health) says its partnership with Melbourne's School of Computing and Information Systems gives it unrestricted access to AWARE. This is an informal partnership route, not a published program.
- **URL:** https://www.orygen.org.au/Research/Research-Areas/Orygen-Digital/Personal-sensing
- **Quote:** "the team at Orygen Digital has unrestricted access to an advanced personal sensing system called AWARE"
- **Date:** accessed 2026-10-11 (page undated)
- **Source type:** secondary
- **KB:** **no.**

### 21. Participant consent and settings-lock work is pending, not yet in main
- **Field:** program_status (maintenance); raw_streams
- **Found:** PR #64 (July 2026) adds a per-sensor runtime consent screen, locks participants out of settings unless the config allows it, and fixes sync race conditions. It was closed without merging, and the maintainers asked for it to be resubmitted through the beta branch. Issue #56 (2025-06-08), reporting that scheduled ESM questions never appear on the stable client, has had no reply.
- **URL:** https://github.com/awareframework/aware-client/pull/64 ; https://github.com/awareframework/aware-client/issues/56
- **Quote:** "New per-sensor runtime-permission consent screen shown after joining a study" ; "Nothing seems to work"
- **Date:** PR 2026-07-14; issue 2025-06-08
- **Source type:** repository
- **KB:** **no.** Reported confidence only; a single user report.

### 22. Support and training channels
- **Field:** program_application (how researchers get help)
- **Found:** a community Discord, a contact form (created 2025-10-13), and a UBISS 2025 summer-school workshop on AWARE at the University of Oulu (max 20 participants).
- **URL:** https://awareframework.com/support/ ; https://ubicomp.oulu.fi/ubiss2025/workshops-instructors
- **Quote:** "You can join the AWARE community on Discord"
- **Date:** support modified 2025-09-29; workshop 2025
- **Source type:** vendor_page, secondary
- **KB:** **no.**

### 23. App Store privacy label for V3
- **Field:** app_availability, gdpr_statement
- **Found:** the developer (Yuuki Nishiyama) declares Health and Fitness, Location, User Content (audio), Identifiers, Usage Data, Sensitive Info and Diagnostics as data linked to the user. Apple notes this is unverified. The description says data goes only to the study administrator's server.
- **URL:** https://apps.apple.com/us/app/aware-client-v3/id6781949744
- **Quote:** "Data is transmitted only to the server configured by your study administrator"
- **Date:** v1.7.0, 2026-07-23
- **Source type:** app_store
- **KB:** **no.**

## C. Searched, nothing found

- **FDA, CE or MDR status:** no clearance, warning letter or CE marking found. AWARE is research software, so not_applicable is likely for fda_clearances.
- **ISO 27001, SOC 2, BAA, DPA, HIPAA:** nothing on awareframework.com, the Support page or the privacy policy. Also nothing from partners (Orygen, CARP) or the Open Collective page. The paid hosting service's terms (DPA, BAA, residency) are unpublished, so a question for D'Alfonso.
- **Pricing for hosting or paid support:** not published; contact only.
- **Formal research, academic or grant program:** none beyond findings 1, 2 and 20. No application form or eligibility criteria.
- **Rate limits, history depth, AI-training terms:** nothing published. The architecture is direct-to-own-database, so API rate limits mostly don't apply. Narrator's optional Google Maps calls are the only third-party data flow found.
- **Job postings:** none found. The Team page lists two software engineers, with no dated postings.
- **Integrators (Fitabase, Labfront, Terra, Thryve):** no AWARE integration found. CARP's `carp_aware_package` is already in the KB.
- **aware-micro-server issues:** none open.
- **aware-light.org:** appears in search results as a Melbourne-maintained AWARE-Light site. The quote probe got no usable text, so it isn't used here.
- **rapids.science:** the docs site returned no usable text or a 404 for `/latest/`, so RAPIDS facts come from the repository only.
- **api.awareframework.com:** no response to a HEAD request on 2026-10-11. Recorded as observed, not as a confirmed shutdown.
