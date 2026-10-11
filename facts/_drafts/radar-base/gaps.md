# RADAR-base: gap hunt, 2026-10-10

Gap hunter pass for `facts/radar-base.yaml`. Every quote below returned "exact" from
`python3 tools/facts/quote_probe.py URL "quote"` on 2026-10-10. Accessed date is 2026-10-10 for all
entries. "KB" means the profile `module-02-digital-phenotyping/profiles/radar-base.md` (profile),
`module-02-digital-phenotyping/comparison-matrix.md` (matrix) and `facts/radar-base.yaml` (yaml, all
fields still `unresearched`, so the yaml lacks every finding below; only profile and matrix are
cited).

Contradictions and missing programs come first, then the rest by value.

---

## 1. Fitbit route is mid-migration to the Google Health API, and the push side is unreleased

- **Field:** deprecations (also export_routes)
- **Found:** RADAR-base's Fitbit integration depends on the legacy Fitbit Web API, which Google is
  decommissioning (the KB's own Fitbit profile gives a 30 October 2026 shutoff). RADAR-base opened a
  tracking issue on 2026-03-25 that reproduces Google's partner notice. Authorization support for the
  Google Health API was merged (RADAR-Rest-Source-Auth PR #332, merged; issue #331 closed), and
  RADAR-Schemas PR #424 "Migrate Fitbit Connector Schemas to GoogleHealth Push" merged. But the
  data-ingest piece, RADAR-PushEndpoint PR #92 "Add Google Health API push integration", is still
  open (last updated 2026-06-05), and the newest PushEndpoint release is v0.4.0 from 2025-06-19
  (GitHub API). Open follow-up issues #93, #94, #97, #98 cover webhook types, manual subscriptions,
  exercise TCX export and signature verification. As of 2026-10-10 no released RADAR-base component
  ingests Google Health API data, about three weeks before the legacy API shutoff.
- **URLs and quotes:**
  - https://github.com/RADAR-base/RADAR-PushEndpoint/issues/91 : "All integrations must be migrated by September 2026 when the legacy APIs will be decommissioned and data will stop syncing."
  - https://github.com/RADAR-base/RADAR-PushEndpoint/pull/92 : "Add Google Health API push integration"
  - https://github.com/RADAR-base/RADAR-PushEndpoint/releases : "v0.4.0" (latest release tag)
- **Date:** issue 2026-03-25; PR 2026-05-01, open; release 2025-06-19
- **Source type:** repository
- **KB has it:** no. Profile line 19 and matrix line 108 present Fitbit as a working REST integration
  with no migration risk; profile line 26 lists partners only.

## 2. Published Google User Data Privacy Policy: AI-training ban, London AWS residency, token deletion

- **Field:** ai_training_terms, data_residency, retention_terms (also raw_streams)
- **Found:** A RADAR-base "Google User Data Privacy Policy" page (modified 2026-06-30 per sitemap)
  governs Google Health API data. It bans training generalised AI/ML models, names AWS eu-west-2
  (London) or university infrastructure as storage, says disconnecting deletes Google tokens and
  identifiers, and lists the read-only scopes (steps, energy, exercise, HR, RHR, HRV, SpO2,
  respiratory rate, skin temperature, sleep stages, ECG waveforms, irregular-rhythm notifications,
  exercise GPS). Scope: it reads as covering the KCL-run deployment that holds the Google OAuth
  client, not every self-hosted instance (inference).
- **URL:** https://radar-base.org/google-privacy-policy/
- **Quotes:**
  - "No training of generalised AI/ML models."
  - "hosted either in AWS eu-west-2 (London) or university infrastructure, with access restricted to authorised study personnel"
  - "we then stop collection, revoke our access, and delete the associated Google tokens and identifiers"
  - "RADAR-base accesses the following from the Google Health API, read-only , on behalf of the study you enrolled in"
- **Date:** page modified 2026-06-30
- **Source type:** vendor_legal
- **KB has it:** no. No AI-training term anywhere; matrix line 147 gives residency only for The Hyve
  ("located at the choice of the client").

## 3. The Hyve states ISO 27001:2022 certification; KB says no ISO statement located

- **Field:** iso27001
- **Found:** The Hyve's homepage says "ISO27001 certified", and a 2023-12-05 article announces
  recertification to ISO 27001:2022, first certified 2017, with a scope covering hosting and support
  of open-source software. That scope plausibly covers RADAR-base as a Service, but the article does
  not name RADAR-base. No certificate or registry entry was found, so this is a self-claim (cap:
  Corroborated). A 2023 recertification on a three-year cycle would fall due around late 2026
  (inference). Caution: search results for "Hyve ISO 27001" return certificates for Hyve Ltd
  (hyve.com, a UK managed-hosting firm), a different company. Do not cite those.
- **URLs and quotes:**
  - https://www.thehyve.nl/ : "ISO27001 certified"
  - https://www.thehyve.nl/articles/the-hyve-iso-certified-2023 : "We're thrilled to announce our successful recertification for the ISO 27001:2022 standard!"
  - same page : "the development, hosting, and support of open-source software, consultancy, and biomedical informatics data analysis services"
- **Date:** article 2023-12-05; homepage current
- **Source type:** vendor_page
- **KB has it:** contradicts. Matrix line 147: "No HIPAA, SOC 2 or ISO statement located"; profile
  lines 104 and 132 say no ISO documentation was located.

## 4. aRMT privacy policy: 60-day deletion, Firebase analytics to developers, developers cannot delete project data

- **Field:** retention_terms (also gdpr_statement)
- **Found:** The Active app privacy policy (modified 2026-07-15) sets deletion "generally within 60
  days" including backups, sends Firebase Analytics, Crashlytics and log data to the developers
  (KCL and The Hyve), and states the developers cannot delete project data; deletion runs through the
  deployment owner. It also lists "Speech Audio" and "Digital Assays" as aRMT instruments.
- **URL:** https://radar-base.org/active-app-armt-privacy-policy/
- **Quotes:**
  - "RADAR-base projects will securely delete study data and remove it from system backups, generally within 60 days unless otherwise legally required to retain it"
  - "The app employs Google Firebase for app event data collection, messaging, remote configuration, and others."
  - "RADAR-base and the DEVELOPERS have no part, access to, or ability to act in this capacity or to delete PROJECT data."
- **Date:** modified 2026-07-15
- **Source type:** vendor_legal
- **KB has it:** no. Profile has no retention or deletion term; Firebase appears only as push
  messaging (profile line 99).

## 5. Phone audio is collected; KB marks audio Unclear

- **Field:** raw_streams
- **Found:** The Get Started page lists audio among pRMT passive streams. radar-commons-android has an
  openSMILE audio plugin (features only, not raw audio), a separate uncompressed audio-input plugin,
  and a camera-based PPG plugin, none of which the profile mentions.
- **URLs and quotes:**
  - https://radar-base.org/getting-started-with-radar-base/ : "Passive data collection (via the pRMT app) enables real-time monitoring of movement, location, audio, calls and texts, and app usage."
  - https://github.com/RADAR-base/radar-commons-android/tree/master/plugins/radar-android-audio : "It uses openSMILE to process audio from the phone's microphone, extracts features from it, and sends those features."
  - https://github.com/RADAR-base/radar-commons-android/tree/master/plugins/radar-android-ppg : "Plugin to measure PPG using the camera of a phone."
- **Date:** page modified 2025-11-18; plugins current on master
- **Source type:** vendor_page; repository
- **KB has it:** contradicts. Profile line 51: Audio / microphone row is all "Unclear". Camera PPG
  missing.

## 6. Wearable catalogue is wider than the KB says: Oura, Polar, and a new Dexcom CGM connector

- **Field:** raw_streams (also export_routes)
- **Found:** The Supported Devices page (updated 2026-06-08) lists Oura (REST connector), Apple Watch
  (aRMT HealthKit), Garmin and Fitbit (REST), Polar Vantage V3 and Polar H10 (pRMT, raw acceleration,
  PP/RR intervals, wrist ECG), Empatica E4 (pRMT), and IoT sensors. Faros, Biovotion and Pebble are
  marked deprecated. A 2026-10-05 post reports a Dexcom CGM connector built in a summer internship
  across RADAR-REST-Connector, Rest-Source-Auth, Schemas and Kubernetes. Note: the E4 is listed with no
  deprecation notice although the KB's Empatica profile treats it as a legacy device.
- **URLs and quotes:**
  - https://radar-base.org/docs/supported-devices/ : "RADAR-base Integration: via REST-API Connector RADAR-base Oura Schemas"
  - same page : "Polar Vantage V3 Wrist worn Raw acceleration Steps Heart rate (PPG) PP-interval in ms Wrist ECG"
  - same page : "Temperature RADAR-base Integration: via Passive App (pRMT) RADAR-base E4 Schemas"
  - same page : "Notice: Deprecated Device"
  - https://github.com/RADAR-base/RADAR-REST-Connector : "for specific Fitbit and Oura devices"
  - https://radar-base.org/2026/10/05/dexcom-integration-into-radar-base-internship/ : "This project integrates Dexcom continuous glucose monitoring (CGM) data into the RADAR-base ecosystem"
- **Date:** 2026-06-08 (devices page); 2026-10-05 (Dexcom post)
- **Source type:** vendor_docs; repository; vendor_page
- **KB has it:** no. Profile line 26 and matrix line 108 name Garmin, Huawei, Empatica and Fitbit
  only; no Oura, Polar or Dexcom.

## 7. Other connector changes: Garmin moved to OAuth 2.0; Huawei connector is work in progress; no Health Connect

- **Field:** deprecations (also raw_streams)
- **Found:** Garmin authorization moved from OAuth 1.0 to OAuth 2.0 (PR #317, merged 2026-03-25),
  and the PR notes push payload structure changes. A Huawei Health Kit connector is an open,
  work-in-progress PR (#204, updated 2026-09-30), so the KB's "Huawei partner" should not be read as a
  shipped integration. Android Health Connect reading is an open feature request (issue #488, opened
  2025-10-06), so the Android app has no Health Connect route.
- **URLs and quotes:**
  - https://github.com/RADAR-base/RADAR-Rest-Source-Auth/pull/317 : "This PR migrates Garmin authorization from OAuth 1.0 to OAuth 2.0."
  - https://github.com/RADAR-base/RADAR-REST-Connector/pull/204 : "Initial implementation of Huawei HealthKit"
  - https://github.com/RADAR-base/radar-commons-android/issues/488 : "Add Support for Reading Data from Google Health Connect"
- **Date:** 2026-03-25; 2026-07-14 (opened); 2025-10-06
- **Source type:** repository
- **KB has it:** no. Profile line 26 and matrix line 108 list Huawei as a partner without status.

## 8. Derived features: radarpipeline exists (KB says no feature catalogue verified)

- **Field:** derived_metrics
- **Found:** `RADAR-base/radarpipeline` is an Apache-2.0 Python feature-generation package on PyPI
  (last push 2026-01-13), presented at the 2023 symposium as a reusable feature catalogue. It is a
  companion tool, not built into the platform, much as Forest is for Beiwe.
- **URL:** https://github.com/RADAR-base/radarpipeline
- **Quote:** "An open-source python feature generation and visualization package use with RADAR project data."
- **Date:** repo last pushed 2026-01-13
- **Source type:** repository
- **KB has it:** contradicts in part. Profile line 67 says the feature-extraction catalogue was "not
  independently verified" and open question at profile line 155 is still open.

## 9. New participant self-enrolment portal and a next-generation app kit

- **Field:** app_availability (also hosting_options; participant onboarding has no schema field)
- **Found:** `radar-self-enrolment-ui` (Next.js, Ory Kratos/Hydra identity) lets participants find a
  study, consent, enrol and connect pRMT, aRMT and Apple Health remotely. `radar-base-app`
  (created 2025-11-26) is a new React Native app kit (`@radarbase/app-kit`) for configuration-driven
  study apps, which may become the successor to the Cordova/Ionic aRMT app (inference, not stated).
  An RFC process for substantial platform changes started in 2025-10.
- **URLs and quotes:**
  - https://github.com/RADAR-base/radar-self-enrolment-ui : "Complete tasks and connect devices (SEP, pRMT, aRMT, Apple Health)."
  - https://github.com/RADAR-base/radar-base-app : "A plugin-based React Native library of widgets, components, and services for building configuration-driven health research apps."
  - https://github.com/RADAR-base/rfcs : "This repository hosts the Request for Comments (RFC) process for proposing and collaborating on substantial changes to RADAR-base."
- **Date:** self-enrolment pushed 2026-09-22; app kit created 2025-11-26
- **Source type:** repository
- **KB has it:** no.

## 10. Export formats and support channels

- **Field:** export_routes
- **Found:** Raw data export in AVRO, JSON and CSV; a public Help Desk, Slack and Swagger API docs are
  listed on the community page. The Hyve also offers deployment, development and training "without
  vendor lock-in", separate from the hosted service.
- **URLs and quotes:**
  - https://radar-base.org/getting-started-with-radar-base/ : "exporting raw data for analysis in multiple formats, including AVRO, JSON, and CSV"
  - https://radar-base.org/community/ : "Reach out through our Help Desk for support and troubleshooting."
  - https://www.thehyve.nl/services/radar-base : "This enables the use of RADAR-base on a self-service basis, without vendor lock-in."
- **Date:** 2025-11-18 (radar-base.org pages); The Hyve page current
- **Source type:** vendor_page
- **KB has it:** no. Profile line 79 covers Kafka streaming only; no export formats or support channels.

## 11. RATE-AF trial cited in the UK 10 Year Health Plan

- **Field:** none directly (evidence of use; context for research_program)
- **Found:** RADAR-base says its RATE-AF wearables paper (Nature Medicine 2024) is cited in the UK
  Government's 10 Year Health Plan, with over 140 million data points collected.
- **URL:** https://radar-base.org/2026/05/12/%f0%9f%94%94spotlight-citation-in-the-nhs-10-year-plan/
- **Quote:** "with over 140 million data points collected and analysed"
- **Date:** 2026-05-12
- **Source type:** vendor_page
- **KB has it:** no. Profile line 116 lists disease areas without RATE-AF.

---

## Leads not confirmed (no exact quote; do not enter as facts)

- **Regulated / SaMD direction.** Search snippets for a KCL job, "Quality Management Lead" (job 154305,
  posted 2026-08-03, closed 2026-08-31), describe RADAR-base as expanding to support regulated
  clinical research and Software as a Medical Device, with a QMS aligned to ISO 13485 and ISO/IEC
  27001. The page now returns 404, and the Wayback Machine was rate-limited, so no quote was confirmed.
  Worth a re-check (fda_clearances, iso27001). Separately, BSI lists an ISO 13485 certificate
  (MD 818073) for KCL's Medical Engineering QMS, which does not name RADAR-base.
- **App Store seller "Onsentia Limited"** for RADAR Active RMT (KB profile line 10): no public
  information found on who this company is or how it relates to KCL or The Hyve.

## Searched, nothing found

- FDA 510(k)/De Novo, CE or UKCA marking for RADAR-base: none found (web search).
- SOC 2, HIPAA statement or BAA from RADAR-base, KCL or The Hyve: none found.
- NEN 7510 for The Hyve: none found.
- Price list or academic tier for RADAR-base as a Service: none (The Hyve pages re-read).
- Integrator coverage (Fitabase, Labfront, Terra, Thryve) of RADAR-base: none found; RADAR-base is a
  platform those integrators do not resell.
- RADAR-base news via general web search: nothing beyond radar-base.org's own sitemap posts.
- GSoC: the GSoC repo has a 2026 ideas page; no confirmation that RADAR-base was accepted for 2026.
- PubMed "RADAR-base" since 2025-06: three papers (ART-transition protocol, BMC Psychiatry 2025;
  ADHD digital markers, JMIR Form Res 2025; depression cognition, Neurosci Appl 2026); none adds
  access or terms information.
- iOS passive app: no new iOS pRMT repository; radar-sensorkit-cordova (SensorKit) last pushed
  2024-11-28.
