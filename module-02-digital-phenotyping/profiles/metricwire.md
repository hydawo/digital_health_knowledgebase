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
| Pricing model | Commercial, custom quote; no public figures (`/pricing` returns 404). Demo by request ("Schedule Demo"); no trial is mentioned on the vendor site. An institution-level **Academic Site Licence** exists, described as "cost effective" but unpriced (Verified 2026-10-10). A third-party route also exists through Penn State's Survey Research Center, which sub-licenses an enterprise licence (Reported, 2026-10-11) |
| Last verified | 2026-10-11 (vendor fact record) |

## Summary

- MetricWire is a Canadian commercial EMA-and-passive-sensing platform, in continuous operation since 2013, a longer commercial track record than most competitors profiled in this module. It supports electronic consent workflows, mobile diaries, passive sensor and geolocation capture, contextualized trigger-based survey deployment, and real-time monitoring/analytics dashboards, serving academic institutions, clinical research organizations, and commercial firms.

## Products / Platform Architecture

- **Catalyst By MetricWire** (iOS 15.0 or later, v6.9.0 released 2026-10-07; Android `com.metricwire.digitalhealth`, updated 2026-10-07), the current participant-facing diary/survey and passive-sensing app. Free download; integrates Apple HealthKit on iOS and Health Connect on Android (Verified 2026-10-11) [12, 15].
- **Legacy "MetricWire" app** is still listed (iOS v4.9.9, last updated 2022-04-06; Android `com.metricwire.android3`, updated 2024-07-30) but is not maintained in step with Catalyst. New studies should not assume it; confirm with the vendor which app a study uses (Verified 2026-10-11) [12].
- **Study-branded apps.** MetricWire Inc. also publishes study-specific apps on the App Store (for example ARTEMIS, Rhythms In Daily Life, SOAR, MAP ARC, PLAD TRACE, TRACC MH, TREAT), which points to custom builds offered as a service. No vendor page describes white-label terms or price (Corroborated 2026-10-11) [12].
- **Researcher dashboard**, real-time monitoring and analytics.
- **Electronic consent module**, named as a distinct feature, useful for fully remote/decentralized study designs that need consent captured in-app rather than on paper.

## Sensors and Data Streams

- Every Module 2 profile uses the same table so platforms can be compared row by row. Rows are the passive streams named in `CLAUDE.md`. "Yes" and "No" are used only where a primary source says so; "Unclear" means nothing current was verified, and "No (OS)" means the operating system does not expose the stream to any third-party app. Confidence and sources are stated under the table. The convention is recorded in [`../../shared/profile-table-conventions.md`](../../shared/profile-table-conventions.md).

| Stream | Android | iOS | Raw or derived | Sampling configurable | Notes |
|---|---|---|---|---|---|
| GPS / location | Yes | Yes | Raw (latitude, longitude, altitude, speed) | Unclear | Fields named in the participant privacy policy [15]. API types `passivelocation`, plus `mobility`, `mobilityplaces`, `mobilitystops`, `mobilitymoves` (derivation undocumented) [14]. |
| Accelerometer | Unclear | Unclear | Unclear | Unclear | API types `accelerometer`, `linearacceleration`, `gravity` [14]. |
| Gyroscope | Unclear | Unclear | Unclear | Unclear | API type `gyroscope` [14]. |
| Magnetometer | Unclear | Unclear | Unclear | Unclear | API type `magnetometer` [14]. |
| Barometer | Unclear | Unclear | Unclear | Unclear | Not among the API's 31 phone stream types [14]. |
| Ambient light | Unclear | Unclear | Unclear | Unclear | API types `light` and `lightios`; an `ambient` type is also listed, meaning undocumented [14]. |
| Proximity | Unclear | Unclear | Unclear | Unclear | Not among the API's 31 phone stream types [14]. |
| Device motion / activity recognition | Unclear | Unclear | Unclear | Unclear | API types `activity`, `activitytypes`, `pedometer`, `steps` [14]. |
| Screen state | Unclear | Unclear | Unclear | Unclear | API type `screenevent` [14]. |
| App usage | Unclear | Unclear | Unclear | Unclear | API types `apps`, `appusage`, `appusageevents`, plus `usageeventsios`, `usageios` [14]. |
| Battery / charging | Unclear | Unclear | Unclear | Unclear | API type `battery` [14]. |
| Network / connectivity | Unclear | Unclear | Unclear | Unclear | Not among the API's 31 phone stream types [14]. |
| Wi-Fi | Unclear | Unclear | Unclear | Unclear | Not among the API's 31 phone stream types [14]. |
| Bluetooth | Unclear | Unclear | Unclear | Unclear | API type `bluetooth` [14]. |
| Calls (metadata) | Unclear | Unclear | Unclear | Unclear | API types `calls` and `callsios` [14]. |
| SMS (metadata) | Unclear | Unclear | Unclear | Unclear | API types `messages` and `messagesios` [14]. |
| Keyboard | Unclear | Unclear | Unclear | Unclear | Not among the API's 31 phone stream types [14]. |
| Audio / microphone | Unclear | Yes | Derived (sound level only, no audio recorded) | Unclear | API type `noise`. Catalyst's App Store notes say background ambient noise measurement records sound levels only [12, 14]. |
| Notifications | Unclear | Unclear | Unclear | Unclear | Not among the API's 31 phone stream types [14]. |
| Device information | Unclear | Unclear | Unclear | Unclear | API type `deviceinformation`, plus a per-participant device snapshot endpoint [14]. Siebers 2025 (Module 3) used carrier-country metadata to detect fraud. |

**Verification.** Checked 2026-10-11 against the MetricWire Consumer API spec on SwaggerHub (v3.0.0), the participant privacy policy and the Catalyst App Store listing. Corroborated. The API enumerates 31 stored phone stream types; it is a list of what can be exported, not a per-OS availability statement, so the Android and iOS columns stay "Unclear" except where another source names the platform. The separate `...ios` types suggest iOS streams are stored apart from Android ones. Whether exported sensor records are raw samples or summaries is not documented, and no phone sensor sampling rate is documented anywhere (not public, 2026-10-11). The sensor operations are named `...Enterprise`, so API access to sensor data may depend on licence tier [14].

### Wearable and health-platform data

- **Fitbit.** 19 API data types, including intraday heart rate, HRV, breathing rate and SpO2, plus ECG and temperature [14].
- **Polar.** Continuous heart rate, training heart rate, sleep and hypnogram, Nightly Recharge HRV and breathing rate [14].
- **Apple HealthKit.** Sleep, step count, exercise and distance, if enabled by the study team [12].
- **Android Health Connect.** Integrated under Google's Health Connect Limited Use policy [15].
- No back-fill limit for wearable history is documented; the API reports a "historical sync" with the oldest date retrieved (not public, 2026-10-11) [14].

### Notes from earlier verification passes

- Passive sensor and geolocation capture is explicitly named on the vendor's own materials. The exact sensor catalog beyond location, and iOS-vs-Android parity, were **not independently verified against current developer documentation** this session, flagged as an open question.

## Derived Metrics / Analytics

- Derived data come mainly from partner ecosystems. Fitbit activity, sleep, Active Zone Minutes, heart-rate zones and daily HRV; Polar daily activity, sleep and Nightly Recharge; HealthKit sleep, steps, exercise and distance [12, 14].
- The API also lists phone stream types named `mobility`, `mobilityplaces`, `mobilitystops`, `mobilitymoves` and `activitytypes`, but how they are derived is not documented [14].
- No documentation of platform-native feature extraction was found (Reported, 2026-10-11).

## Active Data Collection

- Mobile diaries and "contextualized trigger-based survey deployment", i.e., surveys fired based on sensor-detected context (e.g., location or time-based triggers) rather than only fixed schedules, are explicitly named vendor capabilities. This event/context-triggered EMA capability is a genuine differentiator worth confirming in more depth for any study design that needs it, since not every platform in this module documents trigger-based (as opposed to purely scheduled or random) survey delivery.

## Researcher and Study Management Features

- Real-time monitoring and analytics dashboards are named vendor features, implying live adherence/data-flow visibility for study staff. Specific participant-management, multi-site, and role-based-access capabilities were not independently verified this session.

## Data Access and Export

- The homepage says researchers can "customize your result set and exports" (read 2026-10-10). Portal export file formats are still not documented.
- **Two routes (Corroborated, 2026-10-11).** Configurable exports from the researcher web portal, and the MetricWire Consumer API (REST, JSON responses, OAuth2 client credentials, host `consumer-api.metricwire.com`) [11, 14]. See APIs, SDKs, and Extensibility.
- The API returns workspaces, studies, surveys, intakes, survey, diary and analysis submissions (with a PII option), media, participants, device snapshot and study activity, cognitive-task submissions, phone sensor data, and Fitbit and Polar data [14].
- Rate limits are not public. The spec documents no request limit or 429 behaviour; the only number is a default page size of 100,000 records for sensor queries (2026-10-11) [14].
- History depth is not public. Data stay on MetricWire servers until the research team deletes them; no wearable back-fill limit is documented (2026-10-11) [14, 15].

## APIs, SDKs, and Extensibility

- **Updated 2026-10-11 (vendor fact record). An official API spec is published.** MetricWire publishes the "MetricWire Consumer API" on SwaggerHub, versions 1.0.0 to 4.0.0, default 3.0.0 (last modified 2025-05-21), all marked non-private and downloadable without sign-in [14].
  - Authenticated customers exchange a client key and secret for a bearer token (OAuth2 client credentials) and receive JSON. Besides read endpoints, it can create, update and delete API triggers and digital interventions [14].
  - Version 4.0.0 (2025-05-13) drops eight operations present in 3.0.0, mostly bulk trigger creation, and adds none [14].
  - No SDK. `api.metricwire.com` returns an empty JSON object and is not the API host [14].
  - **Access tier is unclear.** There is no standalone developer programme or sign-up. Which licences include API credentials is not published, and the sensor and cognitive-task operation IDs end in "Enterprise", which suggests tier gating (Unclear, 2026-10-11) [14].
  - The UW-Madison `zeolite` client is built on this spec ("API documentation is available on Swaggerhub") and is not reverse-engineered; it states MetricWire does not endorse or maintain it [4].
  - The third-party m2c2kit integration guide for MetricWire was archived (read-only) on 2026-08-12 [3].
- **Second-pass update (2026-08-24, corrected 2026-10-11 where noted):** the MetricWire GitHub organization (https://github.com/MetricWire) contains exactly **one public repository**, a forked architecture-decision-record template with no product code, confirming no public SDK, client library, or open developer package is maintained by MetricWire itself. This **corroborates (does not merely leave open) the closed-source characterization**. However, two independent third-party clues point to an underlying private/partner API: (1) a MetricWire integration guide in the `m2c2-project/m2c2kit-integration-guides` GitHub repository describes URL-based identifier injection between MetricWire and the m2c2kit cognitive-assessment toolkit; (2) an unofficial Python client, `zeolite` (https://github.com/uwmadison-chm/zeolite, University of Wisconsin, Madison Center for Healthy Minds), exists specifically "for MetricWire's Catalyst system." **Upgraded Reported → Corroborated 2026-09-02:** peer-reviewed full text independently confirms the app name, Ball MI et al. 2025 (*Behavior Therapy*, [10.1016/j.beth.2025.05.007](https://doi.org/10.1016/j.beth.2025.05.007), PMC13289574) states that 10% of its participants "received EMA through the smartphone app **Catalyst by MetricWire**" (the other 90% used LifeData's RealLife Exp, the only published head-to-head deployment of the two platforms located so far; see [`lifedata.md`](lifedata.md)). The claim no longer rests on an unofficial third-party client alone. This confirms MetricWire's participant-facing app is called "Catalyst" and exposes an authenticated API. *(Corrected 2026-10-11: the earlier statements that no official API documentation existed and that zeolite reflected a reverse-engineered or partner-only API were wrong. The official spec is on SwaggerHub and zeolite links to it; see the bullet above.)*

## Deployment and Infrastructure

- Vendor-hosted SaaS; no self-hosting option identified. Hosted on Google Cloud Platform in the United States; no self-hosted or on-premises option is published (Corroborated 2026-10-11) [9].
- No separate hosting price is published; hosting is bundled in the vendor-run service (not public, 2026-10-11).

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
- **Added 2026-10-11 (vendor fact record).**
  - **HIPAA and Part 11.** The participant privacy policy says the software was built to comply with HIPAA and 21 CFR Part 11 in the US and GDPR in the EU, and that synced data go to HIPAA-compliant US servers. No independent evidence is published (Corroborated) [15].
  - **BAA.** Not public. No page says a Business Associate Agreement is offered (2026-10-11).
  - **DPA scope.** The policy says MetricWire enters into Data Protection Agreements with its own service providers. That covers sub-processors, not a DPA offered to customer research teams; no customer DPA is published (Unclear, 2026-10-11) [15].
  - **GDPR.** Prighter Group is named as EU and UK representative. The general privacy policy is written to Canada's PIPEDA. All data are stored in the US, and the transfer mechanism for EU studies is not described (Corroborated) [15, 17].
  - **FDA.** No 510(k), PMA or registration listing for MetricWire in openFDA (Verified 2026-10-11). The Part 11 claim concerns electronic records and signatures, not device clearance [21].
  - **Retention.** Data sync to US servers and are removed from the phone. At study end the research team deletes the data from MetricWire servers, and MetricWire says it keeps no further copies, except one archival copy where law requires. No fixed retention period is stated, and nothing says deletion is automatic (Verified 2026-10-11) [15].
  - **Play data-safety declaration.** The Google Play data-safety form for Catalyst lists app interactions under "Data shared" for app functionality, analytics, advertising or marketing, and personalization. This developer self-declaration sits oddly against the participant policy's "no commercial interest" wording and is worth raising with the vendor for IRB review [19].
  - **AI use of data.** Unclear. No MetricWire terms or policy mention AI or model training, and the participant policy limits data use to supporting the study. An implementation partner's case study (Onix, Reported at most) says a Gemini scheduling agent built for MetricWire on Vertex AI draws on participant data and survey responses. Whether that involves training on study data, and whose, is not stated (2026-10-11) [15, 20].

## Pricing

- **Academic Site Licence (Verified 2026-10-10, https://metricwire.com/site-licence/):** an institution-level licence "designed to provide researchers at leading institutions with technology solutions", offering self-serve administration of researcher permissions, dedicated engineering support, beta-program access, an academic advisory board and a dedicated account manager, at "cost effective" but unpublished prices ("a balance between impactful tools and feasible pricing"). No participant limits, data-access terms or approval process are stated, and the page carries a 2023 copyright, so confirm it is current.
  - Programme status is unclear (2026-10-11). The page is live with no closure notice, but the site's page sitemap gives its last modification as 2019-09-20, and no dated programme news was found [10, 22].
  - Application process is not public (2026-10-11). The page ends in a contact form, and the legacy app's Play listing says researcher portal access is requested by email to support@metricwire.com [10, 12].
- **Penn State Survey Research Center sub-licence (third party, Reported 2026-10-11).** Since March 2024 Penn State's SRC holds an enterprise-level MetricWire licence and offers access at "significantly reduced costs" to Penn State-affiliated investigators and external partners, either as an independent licence or as an SRC-run project with its programming and data management. Pilot data collection and student thesis or dissertation projects get access at no cost. No prices are published, and whether the no-cost tier is open to non-Penn State students is not stated. This is a university arrangement, not MetricWire pricing [18].
- **Terms.** The terms of use say fees paid are non-refundable, the terms are governed by Ontario law, and MetricWire reserves the right to discontinue the Services at any time. No minimum term, seat count or participant minimum is published (not public, 2026-10-11) [16].
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
- The Consumer API is documented on SwaggerHub (corrected 2026-10-11), but which licence tiers get API credentials is not published, and sensor and cognitive-task operations carry an "Enterprise" suffix [14].
- The API lists 31 phone stream types, but per-OS availability, raw-versus-summary format and sampling rates are not documented (2026-10-11) [14].
- Signs of churn with no announced deprecation (not public, 2026-10-11). The generic participant app looks superseded by Catalyst, the public Atlassian knowledge base returns 404, the third-party m2c2kit guide was archived 2026-08-12, and API 4.0.0 drops eight operations present in 3.0.0 [3, 8, 12, 14].
- Data residency is United States only, on Google Cloud Platform; no other region is offered (Verified 2026-10-11) [9, 15].

## Best-Fit Use Cases

- EMA-centric studies needing context/trigger-based (not just scheduled) survey delivery.
- Decentralized studies needing an in-app electronic consent workflow.
- Teams wanting real-time adherence monitoring without building their own dashboard.

## Poor-Fit Use Cases

- Teams needing firm pricing before initiating vendor contact.
- Teams requiring self-hosting, source-code auditability, or self-service API access without a licence negotiation (API credentials are tied to an undocumented licence tier).
- Studies that need data stored outside the United States.
- Studies where an independently verifiable compliance certificate is a hard requirement before vendor contact (the vendor states ISO 27001, SOC 2 Type II, Part 11, HIPAA and GDPR, but publishes no certificate).

## Open Questions

- *(Directed to: MetricWire, via https://metricwire.com and its sales/contact channel. The site fetches directly again as of 2026-10-10.)*

- Current pricing structure (per-participant, per-study, subscription). Partly answered 2026-10-10: an Academic Site Licence exists for institutions, but its prices, limits and approval process are not published.
- iOS-vs-Android parity for each stream, whether exported sensor records are raw samples or summaries, and sampling rates. Partly answered 2026-10-11: the API enumerates 31 stored phone stream types [14].
- ~~HIPAA, GDPR/DPA, SOC 2, or 21 CFR Part 11 compliance documentation.~~ Partly answered 2026-10-10: the vendor states all of them (see Privacy, Security, and Compliance). Still open: certificates or audit reports, and BAA terms.
- ~~Whether the "Catalyst" backend's API is available through an official, documented channel.~~ Answered 2026-10-11: the Consumer API is documented on SwaggerHub [14]. Still open: which licence tiers include API credentials, and whether a BAA or customer DPA is offered.
- ~~Data retention.~~ Answered 2026-10-11: the research team deletes data at study end; MetricWire keeps no copies beyond a possible legal archival copy [15]. API export mechanics are documented [14]. Still open: portal export file formats, rate limits and wearable back-fill depth.
- What the Google Play "Advertising or marketing" data-sharing declaration covers, and whether participant data are used to train or refine AI features [19, 20].

## Vendor Fact Record

<!-- facts:begin -->
*Generated from the fact record by `tools/facts/generate.py`. Edit the record, not this block.*

**Research access**

| Fact | Value |
|---|---|
| Formal research or academic program (name, what it offers) | Metricwire Academic Site Licence, an institution-level licence that adds beta programs, academic advisory boards, product updates, a dedicated account manager and dedicated engineering support for novel protocols. [V, 2026-10-11] |
| Who can join the research program | **MetricWire Academic Site Licence:** Aimed at researchers at institutions ("leading institutions"); no eligibility criteria are published. [R, 2026-10-11]<br>**Penn State SRC enterprise licence (third-party sub-licence):** Penn State-affiliated investigators and external partners can use the SRC's licence (independent licence or an SRC-run project); the no-cost tier is for pilot data and student thesis or dissertation projects. [R, 2026-10-11] |
| How to apply, and any approval or review step | Not public [2026-10-11] |
| Whether the program is active, paused, renamed or closed | Unclear |
| Whether the general developer or API program is open to new applicants | Unclear |
| Participant or user limits before approval or by tier | Not public [2026-10-11] |
| How academic access differs from commercial or consumer access | Academic institutions get a separate Academic Site Licence pitched on feasible pricing plus partnership services; commercial terms and the actual price difference are not published. [R, 2026-10-11] |

**Pricing**

| Fact | Value |
|---|---|
| Device or hardware list price | n/a |
| Consumer subscription or membership price | n/a |
| Research or academic pricing or discount | **MetricWire Academic Site Licence:** Offered as balancing tools and "feasible pricing", but no figures are published. [C, 2026-10-11]<br>**Penn State SRC enterprise licence (third-party sub-licence):** Since March 2024 Penn State's Survey Research Center holds an enterprise-level MetricWire licence and offers access at significantly reduced cost (independent licence, or projects run by the SRC with its programming and data management), and no-cost access for pilot data and student thesis or dissertation projects. No prices published. [R, 2026-10-11] |
| Fees for API, SDK, platform or data access | Not public [2026-10-11] |
| Minimum order, term or commitment | Not public [2026-10-11] |
| Whether pricing requires contacting sales | Yes in practice. No prices are posted, researcher portal access is requested by email, and the site licence and demo pages route to contact forms. [R, 2026-10-11] |
| Price of managed hosting | Not public [2026-10-11] |

**Data access and terms**

| Fact | Value |
|---|---|
| Raw signals available to researchers, and by which route | The Consumer API sensor endpoint lists 31 phone stream types: accelerometer, gyroscope, magnetometer, passive location, linear acceleration, pedometer, ambient, gravity, activity types, device information, activity, steps, noise, light, mobility, battery, Bluetooth, screen events, messages, calls, apps, app usage, app usage events, mobility places/stops/moves, and iOS-specific usage events, usage, calls, messages and light. Wearables: Fitbit (19 types including intraday heart rate, HRV, breathing rate, SpO2, plus ECG and temperature) and Polar (continuous heart rate, training heart rate, sleep and hypnogram, Nightly Recharge HRV and breathing rate). Apple HealthKit and Android Health Connect are also integrated. Routes: researcher portal and the Consumer API. [C, 2026-10-11] |
| Derived or processed metrics available to researchers | Derived data come mainly from partner ecosystems (Fitbit activity, sleep, Active Zone Minutes, heart-rate zones and daily HRV; Polar daily activity, sleep and Nightly Recharge; HealthKit sleep, steps, exercise, distance). The API also lists phone stream types named mobility, mobility places, stops and moves, and activity types, but their derivation is not documented. No platform-native feature-extraction documentation found. [R, 2026-10-11] |
| Documented sampling rates or temporal resolution | Not public [2026-10-11] |
| How far back data can be retrieved | Not public [2026-10-11] |
| Export, API, SDK or file routes | Two routes: configurable exports from the researcher web portal, and the MetricWire Consumer API (REST, JSON, OAuth2 client credentials, host consumer-api.metricwire.com). The API returns workspaces, studies, surveys, intakes, survey, diary and analysis submissions (with a PII option), media, participants, device snapshot and study activity, cognitive-task submissions, phone sensor data, Fitbit and Polar data, and can create, update and delete API triggers and digital interventions. No SDK. Portal export file formats are not documented. [C, 2026-10-11] |
| API rate limits | Not public [2026-10-11] |
| Terms on retaining, storing or deleting data | Data sync to US servers and are removed from the phone. When the study ends the research team deletes the data from MetricWire servers and MetricWire says it keeps no further copies, except that one archival copy may be kept where law requires. No fixed retention period is stated. [V, 2026-10-11] |
| Terms on using data to train AI or ML models | Unclear |
| Announced shutdowns, deprecations or migrations, with dates | Not public [2026-10-11] |
| Software licence of the platform's components | Proprietary. MetricWire owns the software; users get a personal, non-exclusive, revocable, non-transferable licence. No open-source components or product repositories published. [V, 2026-10-11] |
| Self-hosting and managed-hosting options | Vendor-hosted SaaS only, on Google Cloud Platform in the United States. No self-hosted or on-premises option is published. [C, 2026-10-11] |
| App store availability on iOS and Android | **Catalyst By MetricWire (current participant app):** iOS (requires iOS 15.0 or later; version 6.9.0 released 2026-10-07, regular releases through 2026) and Android (com.metricwire.digitalhealth, updated 2026-10-07). Free. Supports HealthKit on iOS and Health Connect on Android. [V, 2026-10-11]<br>**MetricWire (legacy generic participant app):** Still listed on iOS (version 4.9.9, requires iOS 12.0 or later, last updated 2022-04-06) and Android (com.metricwire.android3, updated 2024-07-30), but no longer maintained in step with Catalyst. [V, 2026-10-11]<br>**Study-branded (white-label) apps:** MetricWire Inc. also publishes study-branded apps, for example ARTEMIS, Rhythms In Daily Life, SOAR, MAP ARC, PLAD TRACE, TRACC MH and TREAT, which points to custom builds offered as a service. [C, 2026-10-11] |

**Compliance and regulatory**

| Fact | Value |
|---|---|
| Whether a HIPAA Business Associate Agreement is offered | Not public [2026-10-11] |
| Whether a data processing agreement is offered | Unclear |
| Published HIPAA statement | MetricWire says its software was built to comply with HIPAA and 21 CFR Part 11 (and GDPR), that synced data go to HIPAA-compliant US servers, and that it is "the only EMA platform" complying with Part 11, HIPAA and GDPR. No independent evidence published. [C, 2026-10-11] |
| Published GDPR statement | Claims GDPR compliance and names Prighter Group as its EU and UK representative. The general privacy policy is written to Canada's PIPEDA. [C, 2026-10-11] |
| ISO/IEC 27001 status and evidence | Claims ISO 27001 certification (security summary last reviewed 2025-09-08); no certificate, certification body, scope or date published. [C, 2026-10-11] |
| SOC 2 status and evidence | Claims SOC 2 Type II compliance; no report, auditor or period published. [C, 2026-10-11] |
| FDA clearances, from the FDA database | Not public [2026-10-11] |
| Where data is stored, and residency options | United States only, on Google Cloud Platform. No other region option is published. [V, 2026-10-11] |

<!-- facts:end -->

## Key Links

- Official site: https://metricwire.com/ (direct fetch succeeded 2026-10-10)
- Developer/API documentation: https://app.swaggerhub.com/apis-docs/MetricWire/ConsumerAPI/3.0.0
- Security/privacy: https://metricwire.com/participant-privacy-policy/; https://metricwire.com/privacy-policy/; https://metricwire.com/terms-of-use/
- Site Licence page: https://metricwire.com/site-licence/ (read 2026-10-10)
- Data Privacy & Security Summary: https://metricwire.com/data-privacy-security-summary/
- Catalyst By MetricWire, App Store: https://apps.apple.com/us/app/catalyst-by-metricwire/id1585123028; Google Play: https://play.google.com/store/apps/details?id=com.metricwire.digitalhealth
- GitHub organization: https://github.com/MetricWire (direct fetch succeeded, second pass)
- Third-party profile (used for company facts this session): https://pitchbook.com/profiles/company/89864-11

## Sources

1. Search-summary characterization of MetricWire's own marketing materials, aggregated via WebSearch (accessed 2026-08-24, both sessions). **Corroborated, not Direct**, metricwire.com's homepage and pricing/contact pages returned HTTP 403 on direct fetch in both the first and second pass; the platform description (electronic consent, mobile diaries, passive sensor/geolocation capture, contextualized trigger-based surveys, real-time dashboards) comes from a search-engine summary of the vendor's own site content, so it should be treated as Corroborated rather than Verified.
2. MetricWire GitHub organization (**direct fetch, second pass**). https://github.com/MetricWire (accessed 2026-08-24). **Primary/Verified.** Confirms exactly one public repository (an unrelated forked ADR template), no public SDK/API client, corroborates closed-source characterization.
3. m2c2kit integration guide for MetricWire (search summary). https://github.com/m2c2-project/m2c2kit-integration-guides/blob/main/docs/metricwire.md (accessed 2026-08-24). URL-based identifier-injection integration pattern between MetricWire and the m2c2kit cognitive-assessment toolkit. Repository archived (read-only) on 2026-08-12, checked 2026-10-11.
4. `zeolite`, unofficial Python client for MetricWire's "Catalyst" system, University of Wisconsin, Madison Center for Healthy Minds. https://github.com/uwmadison-chm/zeolite (accessed 2026-08-24, search summary; re-read 2026-10-11). Built on MetricWire's official SwaggerHub spec ("API documentation is available on Swaggerhub"); not endorsed or maintained by MetricWire.
5. PitchBook, MetricWire company profile. https://pitchbook.com/profiles/company/89864-11 (accessed 2026-08-24, search summary). Founding year (2013), Waterloo, Canada headquarters.
6. Third-party software directories: Capterra, SoftwareWorld, SoftwareSuggest, TechnologyCounter, SourceForge, Visualping (accessed 2026-08-24, search summary, both sessions). Trial/demo-availability and contact-gated-pricing characterization; no specific pricing figures located in either session.
7. ResearchGate figure caption referencing MetricWire as the platform used in a published EMA study. https://www.researchgate.net/figure/Select-screenshots-from-the-EMA-study-smartphone-platform-MetricWire-EMA-ecological_fig2_354098947 (accessed 2026-08-24, search summary). Evidence of research use.
8. MetricWire knowledge base, "Missing Alerts Troubleshooting." https://metricwire.atlassian.net/wiki/spaces/mwknowledgebase/pages/6750210/Missing+Alerts+Troubleshooting (accessed 2026-10-09, search summary). Returned HTTP 404 on 2026-10-10; dead link.
9. MetricWire, "Data Privacy & Security Summary." https://metricwire.com/data-privacy-security-summary/ (last reviewed 9/8/2025; accessed 2026-10-10, direct fetch). **Primary, vendor-stated.** US storage on Google Cloud Platform, AES-256 at rest, TLS 1.2+ in transit, MFA, ISO 27001 and SOC II Type II statements; no certificate linked.
10. MetricWire, "Academic Site Licence." https://metricwire.com/site-licence/ (copyright 2023; accessed 2026-10-10, direct fetch). **Primary/Verified** for the programme's existence and terms; compliance and "most published" claims are vendor-stated.
11. MetricWire homepage. https://metricwire.com/ (accessed 2026-10-10, direct fetch). **Primary.** Schedule Demo / Get Started calls to action; no trial or pricing; "customize your result set and exports".
12. App Store and Google Play listings for "Catalyst By MetricWire" (`com.metricwire.digitalhealth`) and the older "MetricWire" app (`com.metricwire.android3`), direct fetch 2026-10-10, re-checked 2026-10-11 (iTunes lookup for release dates and minimum iOS versions; App Store "More by MetricWire Inc." list for study-branded apps; Catalyst release notes on background noise measurement and HealthKit). **Primary/Verified.** https://apps.apple.com/us/app/catalyst-by-metricwire/id1585123028; https://apps.apple.com/us/app/metricwire/id1117108543; https://play.google.com/store/apps/details?id=com.metricwire.digitalhealth; https://play.google.com/store/apps/details?id=com.metricwire.android3
13. PubMed search `MetricWire[Title/Abstract]` via E-utilities (accessed 2026-10-10). Three records: 41364742, 34668869, 31511290.
14. MetricWire Consumer API specification, SwaggerHub. https://app.swaggerhub.com/apis-docs/MetricWire/ConsumerAPI/3.0.0 (registry: https://api.swaggerhub.com/apis/MetricWire/ConsumerAPI; accessed 2026-10-11). **Primary, vendor docs.** Versions 1.0.0 to 4.0.0, OAuth2 client credentials, JSON, host `consumer-api.metricwire.com`; enumerates phone sensor, Fitbit and Polar stream types; no rate limit or sampling rate documented.
15. MetricWire, Participant Privacy Policy. https://metricwire.com/participant-privacy-policy/ (accessed 2026-10-11). **Primary, vendor legal.** Location fields, Health Connect Limited Use, US HIPAA-compliant servers, retention and archival copy, HIPAA/Part 11/GDPR statement, Prighter Group, DPAs with service providers, "no commercial interest" wording.
16. MetricWire, Terms of Use. https://metricwire.com/terms-of-use/ (accessed 2026-10-11). **Primary, vendor legal.** Proprietary licence, fees "posted ... (if any)", non-refundable fees, Ontario law, right to discontinue the Services.
17. MetricWire, Privacy Policy. https://metricwire.com/privacy-policy/ (accessed 2026-10-11). **Primary, vendor legal.** Written to Canada's PIPEDA.
18. Penn State Survey Research Center, "Metricwire" (TRACE). https://survey.psu.edu/trace/metricwire, and Penn State News, "Survey Research Center adds Metricwire to TRACE portfolio" (2024-03-14). https://www.psu.edu/news/social-science-research-institute/story/survey-research-center-adds-metricwire-trace-portfolio (both accessed 2026-10-11). **Secondary, Reported.** Enterprise licence sub-licensed at reduced cost; no-cost tier for pilot and thesis work.
19. Google Play data-safety page, Catalyst By MetricWire. https://play.google.com/store/apps/datasafety?id=com.metricwire.digitalhealth&hl=en_US (accessed 2026-10-11). Developer self-declaration; app interactions listed under "Data shared".
20. Onix, "Metricwire launches AI-powered scheduling tool..." case study. https://www.onixnet.com/case-study/metricwire-launches-ai-powered-scheduling-tool-to-boost-survey-and-customer-support-efficiency/ (accessed 2026-10-11). **Secondary, Reported at most.** Gemini scheduling agent on Vertex AI using participant data and survey responses.
21. openFDA 510(k), PMA and registration-listing searches for MetricWire. https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm (accessed 2026-10-11). No matches.
22. MetricWire page sitemap. https://metricwire.com/page-sitemap.xml (accessed 2026-10-11). Site Licence page last modified 2019-09-20.
