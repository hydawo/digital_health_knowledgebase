# Oura

## Quick Facts

| Field | Details |
|---|---|
| Organization | Oura Health Oy (Ōura), Finland; the Oura API and MCP Agreement is signed with Ouraring, Inc., a Delaware corporation |
| Category | Consumer smart ring; sleep, recovery, and temperature focus |
| Current status | Active |
| Platforms/devices | Oura Ring (Gen3, Oura Ring 4, Oura Ring 5); iOS and Android app; **Oura Research** participant app for studies |
| Open source | No |
| Hosting/deployment | Vendor cloud (Oura Cloud), REST API v2 |
| Pricing model | Ring purchase + **mandatory membership subscription for API data access on Gen3 and later** |
| Last verified | 2026-10-11 (vendor fact record); earlier passes 2026-08-21 and 2026-10-10 |

## Summary

- Oura is the strongest consumer device for **sleep and nocturnal physiology**. Its form factor, a ring, puts the PPG sensor on the finger, where perfusion is better and motion artefact during sleep is lower than at the wrist, and it removes the screen-and-notifications distraction that makes wrist wearables uncomfortable to sleep in. In head-to-head PSG validation it led in Robbins 2024 (Oura-funded), but independent results are mixed (tied with WHOOP and behind Somfit on four-stage kappa in Miller 2022, behind three wrist devices in Lee 2023); see Research Evidence. Reworded 2026-10-10 to match that section.

- For research there are two decisive practical facts:

1. **The API is clean and comprehensive**, a well-structured REST v2 with roughly 19 documented data routes, OAuth 2.0, rate limits of 5,000 requests per 5 minutes applied per token and per application, webhooks, and date-ranged list endpoints. An app is limited to 10 users until Oura approves it.
2. **Data access is gated behind an active paid membership.** Oura's own support documentation states that Gen3-and-later users without an active Oura Membership cannot access their data through the Oura API, and neither can partner applications integrated with it. For a study, that means the subscription is not optional, it is a per-participant, per-month line item for the entire study duration, on top of the ring.

- That second fact is the single most important cost driver and is easy to miss when scoping a study.

- **Two further facts added 2026-10-10.** Oura sells a first-party research offering (Oura for Organizations, "Oura for research"), with dashboards, group export and a participant app, so the API is not the only route. This is not new: published studies from 2022 onward export data from an Oura researcher portal they call "Oura Teams" (Reported; see Researcher and Study Management Features). And the Oura API and MCP Agreement (effective 8 June 2026) limits how long API data may be kept and bars using it to train, evaluate or prompt AI models; see Data Access and Export.

## Products / Platform Architecture

- **Oura Ring**, titanium ring, worn on a finger (Oura recommends index finger; sizing kit required before ordering, which adds lead time to participant onboarding).
- **Oura app** (iOS/Android), sync and participant-facing insights.
- **Oura Cloud / API v2**, REST, OAuth 2.0.
- **Oura for Business / Oura for Organizations**, enterprise offering aimed at employers, healthcare, academic and clinical research, and military. Oura reports 200+ customers across those segments including US Air Force, US Navy, US Army, NASA, and universities. `ouraring.com/business` now redirects to `organizations.ouraring.com` (checked 2026-10-10).
- **Oura for research** (organizations.ouraring.com/solutions/researchers), the research offering within Oura for Organizations. Corrected 2026-10-10; the earlier text said what a research customer receives was not established. See Researcher and Study Management Features.
- **Oura Research app** (Oura Health Oy, App Store), a separate participant-facing app "For participants enrolled in research studies using the Oura Ring", which "collects data from your Oura Ring and shares it securely with your study's research team with your consent". Version history runs from 1.0 (22 April) to 1.0.11 (15 September); the listing shows no year. **Verified** that the app exists (2026-10-10).
  - Per Oura's privacy policy, the Research Sponsor is the controller of study data, Oura may act as its processor for hosting and administration, and the Sponsor selects participants. Studies can blind participants to their scores while the ring keeps collecting. **Verified** (privacy policy and consumer terms, 2026-10-10; sources 26, 27).

## Sensors and Data Streams

- Every Module 1 profile uses the same table so devices can be compared row by row. Rows are the sensors named in `CLAUDE.md`. "Present" is about the hardware; "Researcher access" is about what a study can actually obtain, which is the module's central question. "Unclear" means nothing current was verified. The convention is recorded in [`../../shared/profile-table-conventions.md`](../../shared/profile-table-conventions.md).

| Sensor | Present | Researcher access to underlying signal | Resolution or sampling | Notes |
|---|---|---|---|---|
| PPG | Yes, multi-wavelength (green, red, infrared on Gen 3 and later) | No raw PPG. Derived HR. | API docs: "Heart rate is provided at 5-minute increments"; each sample carries a `source` (awake, rest, sleep, workout, live, session); session HR comes from the Sessions endpoint | Re-verified 2026-10-10 (OpenAPI 1.41). The heart-rate route no longer carries a Gen 3 note; whether Ring 4 or 5 returns identical HR series is not stated (**Unclear**). |
| ECG | No | Not applicable | Not applicable |  |
| Accelerometer | Yes | No raw accelerometry. Derived activity, MET and steps only. | Derived |  |
| Gyroscope | Not documented as user-accessible | Not applicable | Not applicable |  |
| Magnetometer | No | Not applicable | Not applicable |  |
| Temperature | Yes, NTC skin temperature sensors | Derived nightly deviation from personal baseline, not a raw trace. | Nightly | The most distinctive research signal. |
| SpO2 | Gen 3 and later | Nightly average SpO2 and breathing regularity (`daily_spo2`: `spo2_percentage`, `breathing_disturbance_index`). | Nightly | The API's SpO2 route still says data are available only for users with a Gen 3 ring (OpenAPI 1.41, 2026-10-10). |
| GPS | No | Not applicable | Not applicable | No GPS, screen, altimeter or barometer, by design, for size and battery life. |
| Barometer / altimeter | No | Not applicable | Not applicable |  |
| EDA | No | Not applicable | Not applicable |  |
| Ambient light | No | Not applicable | Not applicable |  |
| Other | Unclear | Unclear | Unclear | Not verified against current documentation. |

**Verification.** As recorded in the Module 1 passes from Oura's documentation; the ring is a physiology device, not a mobility device.

### Notes from earlier verification passes

| Sensor | Present | Researcher access to underlying signal |
|---|---|---|
| PPG (multi-wavelength: green/red/IR on Gen3+) | Yes | **No raw PPG.** Derived HR at ~5-minute resolution while stationary, continuous during sleep. |
| Accelerometer | Yes | **No raw accelerometry.** Derived activity/MET/steps only. |
| Gyroscope | Not documented as user-accessible | n/a |
| Temperature (NTC skin temperature sensors) | Yes | Derived nightly temperature *deviation* from personal baseline, not absolute raw trace. This is Oura's most distinctive research signal. |
| SpO2 | Gen3+ | Nightly average SpO2 and breathing regularity. |
| GPS | **No** | n/a, the ring has no GPS, no altimeter, no barometer. |
| EDA | No | n/a |

- Note the deliberate design trade: the ring omits GPS, screen, and altimeter to achieve size and battery life. It is a physiology device, not a mobility device.

## Derived Metrics / Analytics

- Oura API v2 routes (19 documented, grouped):

- **Personal & configuration**, Personal Info (age, weight, height, biological sex, email); Ring Configuration (colour, design, firmware, hardware type, setup date); Ring Battery Level.

- **Daily summaries**, Daily Sleep (score + contributors: deep sleep, efficiency, latency, REM, restfulness, timing); Daily Activity (score, calories, MET minutes, steps, activity distribution); Daily Readiness (score + contributors: HRV balance, body temperature, sleep balance); Daily Resilience (sleep recovery, daytime recovery, stress indicators); Daily SpO2; Daily Stress (stress/recovery time with day summary).

- **Health metrics**, Heart Rate (timestamped BPM with source labelling); VO2 Max; Cardiovascular Age (vascular age, pulse wave velocity).

- **Sleep & sessions**, Sleep Periods (detailed stage data, deep/light/REM, with heart rate and HRV variation traces); Sleep Time (optimal bedtime recommendation, efficiency status); Sessions (guided breathing/meditation with biometrics); Rest Mode Period.

- **Activity & tags**, Workouts (activity type, calories, distance, intensity, timestamps); Enhanced Tags; Tags.

- **Re-checked 2026-10-10 against the OpenAPI spec (`openapi-1.41.json`, fetched directly from cloud.ouraring.com/v2/docs).** The user-collection routes are daily_activity, daily_cardiovascular_age, daily_readiness, daily_resilience, daily_sleep, daily_spo2, daily_stress, enhanced_tag, heartrate, personal_info, rest_mode_period, ring_battery_level, ring_configuration, session, sleep, sleep_time, tag, vO2_max and workout, plus webhook subscription routes and a sandbox copy of each data route. There is **no route for blood pressure, GLP-1, lab results or Health Radar**. The ring hardware enum includes `gen4` and `or5`. The only access gate the spec documents is an expired membership (HTTP 403, "the user's Oura subscription has expired"); no per-metric tier exists, since Oura sells one membership. **Verified.**

- **Resolution (OpenAPI 1.41, Verified 2026-10-10):** heart rate and HRV series at 5 minutes; 30-second sleep movement and 5-minute sleep phase classification; the sleep-period average HR is computed from 30-second samples and differs from the value shown in the app. Apple Health export carries heart rate at one-minute intervals (Oura Data Export article, source 33).
- **Enterprise Platform metrics:** the research page lists 50+ metrics, including blood pressure signals and nighttime breathing, which have no public API route. Which of them reach the platform export is not stated (**Corroborated**, vendor list; source 17).

- The **Sleep Periods** route is the research workhorse: it returns per-night stage hypnograms alongside within-night heart rate and HRV time series, which is unusually rich for a consumer API.

- Oura's HRV is RMSSD-based and measured continuously through the night, a substantively different (and for most research purposes better) quantity than Apple's opportunistic SDNN. Cross-platform HRV comparisons must account for this.

## Active Data Collection

- Minimal. Tags and Enhanced Tags let participants annotate timestamped events with free text/comments, which can serve as a lightweight event-marking mechanism (e.g. medication taken, symptom onset) but is not a survey/EMA system. No scheduled prompts, no branching logic.

## Researcher and Study Management Features

- ~~No first-party research console is documented in the public API.~~ **Corrected 2026-10-10: Oura has a research offering.** The "Oura for research" page under Oura for Organizations (organizations.ouraring.com/solutions/researchers) describes an "Oura Enterprise Platform" for researchers with:
  - curated, customisable dashboards with filtering, tagging and trends, and tracking of participant adoption, attrition and engagement;
  - "Manage groups and access levels" and "Download data by individual or group";
  - "Flexible data export of raw data to CSV or JSON file" and "Integrate data into existing systems with Oura API";
  - "Academic researchers can access premium metrics";
  - a choice of participant app "based on their study design" (the Oura Research app is listed separately on the App Store);
  - a claim that it "processes PHI in accordance with HIPAA" and complies with GDPR;
  - a "dedicated customer success team" for onboarding and data access.
  - Target segments named: academic researchers, life-science researchers, academic medical centres, government and non-profits, CROs and consumer-product researchers.
- **What is not published:** price, minimum order or term, eligibility criteria (the page lists target segments only), review criteria or timeline (contact form only), and what "raw data" means. Whether the export includes signal-level data (PPG, accelerometry) is **Unclear** as of 2026-10-10; Oura's security whitepaper says research partners "may receive data that has been processed to protect data subject privacy", and published "Oura Teams" exports describe one-minute MET data, not sensor signals (sources 24, 34 to 36). "Premium metrics" are not defined either.
- **How organizations buy:** purchases run on an Order under the Oura for Business Products and Services Agreement, which states fees and the Eligible Person count; a Research Sponsor may also sign a separate Research Agreement with Oura. Bulk orders start from a quote prepared by an Oura point of contact. The Enterprise Support Center calls the platform a licensed platform. **Verified** (business terms, partner support, 2026-10-10; sources 28, 30). **Verified** that the offering exists and what the page says (2026-10-10); its contents beyond the page are **Unclear**. All statements on the page are the vendor's own (**Corroborated** at most for any capability claim).
- **How it differs from the public API route:** the public API gives a self-built app per-user OAuth access to derived metrics, 10 users before approval, under the API Agreement's retention and AI-training limits. The research offering adds group management, dashboards, bulk export and support, at an unpublished price. The two routes do run on different terms. Oura's privacy policy says a participant withdrawing consent on the Enterprise Platform does not affect data the Data Recipient (for example a researcher) has already extracted, so the API Agreement's 72-hour deletion rule does not carry over; retention is then set by the Order, any Research Agreement and the study protocol. Oura also uses aggregated Enterprise Platform data for its own analytics and R&D. What a Research Agreement says about AI use or retention is not public. **Verified** (privacy policy, business terms, 2026-10-10; sources 26, 28).
- **"Oura Teams" (Reported).** Studies from 2022 to 2026 describe exporting CSV files, including one-minute MET data, from a researcher portal called "Oura Teams"; one paper also calls it "Oura on the Web" (Chinoy 2022, Haimovich 2026, a 2025 paper; sources 34 to 36). Oura's current pages do not use the name, and whether it is today's Enterprise Platform is not stated. teams.ouraring.com did not resolve on 2026-10-10. Ask Oura.

- In practice, academic Oura studies use one of three routes: (a) an Oura researcher portal ("Oura Teams" in the literature, or the Enterprise Platform), (b) a custom OAuth app pulling per-participant data, or (c) middleware. Provisioning is meaningfully harder than for wrist wearables because of **ring sizing**, each participant needs a sizing kit and a correct size before the actual device ships, adding weeks to onboarding and creating a real risk of mis-sized rings mid-study (finger size changes with temperature, hydration, pregnancy, and weight change).

## Data Access and Export

- **API v2**: OAuth 2.0 only. Oura's docs state that "personal access tokens were deprecated in December 2025 and are no longer available for use", for any integration, not only new ones. **Verified** (cloud.ouraring.com/v2/docs, OpenAPI 1.41, 2026-10-10).
- **User cap**: "API Applications are limited to **10** users before requiring approval from Oura. There is no limit once an application is approved." Approval is requested from the application's page once development is finished; criteria and turnaround are not published. **Verified** (2026-10-10).
- **Fees:** the docs say "the Oura API is free to use for both personal and commercial applications", but the API and MCP Agreement reserves the right to charge in future, with notice, including differentiated pricing for business users, and bars apps from charging users for API access. **Verified** (sources 15, 16, 2026-10-10).
- **Rate limits**: 5,000 requests per 5-minute period, per the FAQ in the current OpenAPI 1.41 document. The newer Rate Limits section of the same document names two layers, per access token and per application in aggregate across all its end-user tokens, without a number for each, so whether 5,000 is the per-token or per-application ceiling is not stated. A 429 response carries `Retry-After`, `X-RateLimit-Limit`, `X-RateLimit-Window`, `X-RateLimit-Reset` and `X-RateLimit-Tier` headers, which report the live ceiling. Higher limits are available on request (api-support@ouraring.com), and Oura may change limits without notice. **Verified** (2026-10-10). Corrected 2026-10-11; the earlier text said no number was published.
- **List endpoints** accept `start_date` / `end_date`; single documents fetchable by id. Oura advises making "a single request for historical data when a user first connects", then using webhooks. No lookback limit is documented (not public, checked 2026-10-10).
- **Oura API and MCP Agreement, effective 8 June 2026 (read 2026-10-10, Verified).** These terms govern any app, including a study's own, that uses the API:
  - **Retention:** User Data obtained through the Oura API "may not be stored or retained beyond the duration strictly necessary" (§3(m)), and "retaining or storing User Data or Oura Data beyond the periods specified in this Agreement" is a Prohibited Use (§4(a)(x)). Data obtained through the MCP Server may not be stored at all without separate written authorization, and aggregators may not store or cache any data (§3(m)). The developer docs FAQ, by contrast, recommends storing historical data in your own database. The record marks this a **conflict**: the Agreement is the contract and the FAQ is guidance. "Strictly necessary" is undefined, so whether a longitudinal research dataset qualifies is unclear; a study keeping a dataset should get written terms from Oura.
  - **Deletion:** users may opt out or delete at any time; on a deletion request "you shall delete all User Data relating to such User within seventy-two (72) hours", and User Data must also be deleted when the user cancels the app's subscription (§5(f)). On termination all User Data must be deleted, with written certification if Oura asks (§14). Storing location data is barred (§4(a)(xx)).
  - **AI and ML:** three clauses overlap. Training, fine-tuning or improving any AI model, or putting User Data into "any training dataset, evaluation dataset, or benchmark dataset", is a Prohibited Use unless Oura gives prior written consent (§4(a)(iii)). §4(d) bars using the Oura API to develop, train, fine-tune, evaluate, prompt or otherwise provide input to any AI model or platform, and permits use with large language models only through the Oura MCP Server; it has no consent route. A clause in capitals bars using User Data to train or improve "ANY AI MODEL OR OTHER ARTIFICIAL INTELLIGENCE OR MACHINE LEARNING SYSTEM", as a material breach, also with no consent route (§6(g)). "AI Model" is defined to include any machine learning model. Read together, training on API data is not obtainable under this Agreement alone, and §4(d) on its face reaches an LLM-assisted analysis of API data; whether a separate Research Agreement overrides these clauses is not public. Oura may audit for compliance.
  - **User consent does not help:** the Prohibited Uses apply "regardless of whether a User has purportedly consented" (§4(c)), so a study's own consent form cannot lift them.
  - **Benchmarking and reverse engineering:** use "for purposes of monitoring the availability, performance, or functionality of Oura's products ... including without limitation benchmarking" (§4(a)(ii)) and deriving Oura's "scoring methodologies, signal processing techniques ... or analytical models" (§4(a)(xi)) are Prohibited Uses unless Oura consents in writing. Read literally, this may reach device-validation studies that use API data; that reading is **Unclear** and needs Oura or counsel.
  - **Sharing:** disclosing User Data to any third party is a Prohibited Use except as the Agreement provides (§4(a)(vi)).
  - **Aggregators:** an aggregator must register separately for each end customer and get Oura's prior written approval for each one, and may not store or cache User Data (§3(e), §3(m)).
  - **No research carve-out** appears in the Agreement. For a study this means a permanent analysis dataset, data deposit, and any model training on Oura API data need Oura's written agreement (or, for the §4(d) and §6(g) bans, may not be obtainable at all under these terms).
  - **Parties:** the Agreement is with Ouraring, Inc. (Delaware), and each party is an independent controller of the personal data it discloses or receives. It supersedes the 2021 API Agreement. Oura may modify or discontinue any part of the API or MCP Server with or without notice.
- **Participant self-export**: all Oura users, including those without an active membership, can export all of their Oura data as CSV through the Membership Hub, which Oura describes as GDPR-compliant; preparation can take up to 10 days from the request (source 32). This is a useful fallback for participants whose membership lapses, and for studies that want a participant-mediated export path.
- **Other routes:** Apple Health and Health Connect sync (source 32); the Enterprise Platform (group download, CSV/JSON, API integration), and an "Enterprise API to send data to external systems" named on Oura's healthcare page, whose relation to the public API v2 is not stated (source 37); the Oura Research App for sponsor-run studies.
- **Oura on the Web discontinued 5 October 2026.** Data stay in the app and the Membership Hub export. The cloud.ouraring.com root now serves only an "Oura on the web" page (2026-10-10). **Verified** (support article, source 25).
- **Other deprecations:** API v1 removed 22 January 2024; the Tag route is deprecated in favour of Enhanced Tag (OpenAPI 1.41).
- **Membership gate**: Gen3 and later users without an active Oura Membership cannot access data through the API, and neither can partner apps for those users.
- **App version dependency**: users must have updated to a recent version of the Oura app for new data types to appear via API v2, meaning participant app-update behaviour can silently break a data stream.

## APIs, SDKs, and Extensibility

- REST v2, OAuth 2.0, JSON. Documentation at `cloud.ouraring.com/v2/docs` and `api.ouraring.com/v2/docs`. The pages are JavaScript-rendered, but the OpenAPI document is directly fetchable at `cloud.ouraring.com/v2/static/json/openapi-1.41.json` (checked 2026-10-10).
- Mature community client libraries exist in Python, Dart/Flutter, Deno/TypeScript, and others.
- No SDK for on-device code; the ring is not programmable.
- Webhooks: supported and recommended by Oura as "the preferred way to consume Oura data" (`/v2/webhook/subscription`, one subscription per event type and data type, notifications about 30 seconds after data sync from the mobile app, 10 retries on failed delivery). Sleep data reach the API only after the user opens the Oura app. **Verified** (OpenAPI 1.41, 2026-10-10).

## Deployment and Infrastructure

- Vendor cloud only. No self-hosting. Research team needs an OAuth app registration and its own storage.

## Participant Experience

- **Highest sleep-wear acceptability** of any device in this module. A ring is comfortable to sleep in, silent, screen-free, and socially unobtrusive.
- Battery roughly 4 to 7 days depending on generation and use; charging takes ~20 to 80 minutes on a small dock. Low burden, but the dock is a losable item in remote studies.
- **Sizing is the operational weak point.** Sizing kits, lead times, and finger-size drift over a long study are real sources of attrition and data loss.
- Not suitable for participants who cannot wear rings for occupational or safety reasons (healthcare workers with hand-hygiene protocols, machine operators, some athletes).
- Data syncs via the phone app; sync lapses cause gaps.
- iOS and Android.

## Privacy, Security, and Compliance

- Oura provides a GDPR-oriented user data download through the Membership Hub.
- **Security page and whitepaper (read 2026-10-10).** Oura's security page (ouraring.com/security; the same text was earlier read on ouraring.com/trust-center) says, under a SOC 2 heading, "Each year, independent auditors carefully review our security controls", and "We also meet HIPAA requirements where we handle protected health information for a healthcare partner"; it also lists Bluetooth encrypted with AES-128, TLS 1.2+ in transit, AES-256 at rest. The August 2026 security whitepaper says Oura undergoes an annual SOC 2 examination and maintains HITRUST certification; reports are not public and type I or II is not stated, and no HITRUST registry entry was found. The research page says the enterprise platform "processes PHI in accordance with HIPAA" and complies with GDPR. These are vendor statements: **Corroborated** (sources 19, 23, 24).
- **HIPAA status:** Oura says it is generally not a covered entity for its direct-to-consumer services (privacy policy).
- **BAA (Corroborated):** available to business customers and healthcare partners. The business terms bar uploading PHI unless the buyer has a BAA with Oura, the whitepaper describes an enclave for partners who sign one, and the privacy policy says Oura acts as a Business Associate in some instances. No BAA template is published, and whether one is offered for a research cohort on the Enterprise Platform needs confirmation. The public API has no BAA; each party is an independent controller (sources 16, 24, 26, 28).
- **GDPR and transfers (Corroborated):** Oura says it adheres to the EU and UK GDPR, with Oura Health Oy as controller for most processing, and it participates in the EU-US Data Privacy Framework (with UK and Swiss extensions); DPF participation is confirmed on the Commerce Department's registry (sources 24, 26, 40).
- **DPA:** none published (not public, 2026-10-10). For Research App studies Oura may be the sponsor's processor, which under GDPR needs a processing agreement, presumably within the Research Agreement.
- **Data residency (Corroborated):** member data may be processed on servers outside the user's country, with no consumer choice. For enterprise customers and partners, the whitepaper says deployment options "can support geo-specific residency and secure enclave deployment needs"; regions and cloud provider are not named (sources 24, 26).
- **Retention (consumer):** Oura keeps sleep, readiness and activity measurement data only while the account is active (privacy policy, Verified).
- **Oura's own AI use:** the privacy policy says Oura may use member personal data to build its own AI, ML and LLM features, and that it does not sell personal data to train third-party LLMs.
- **ISO 27001:** not mentioned on the security page or in the whitepaper, which cite SOC 2, HITRUST and the NIST Cybersecurity Framework; no certificate found (not public, 2026-10-10). The government page also claims design to NIST 800-171 and IL5 standards (vendor claim, unchecked).
- **FDA:** no Oura-held 510(k), De Novo or PMA (openFDA searches, 2026-10-10; **Verified** as not found). Oura Health Oy holds FDA establishment registration 3015599655 listing one device, "Fertile Window", product code LHD (fertility diagnostic, proceptive), class U, listed 2023-08-08, with no premarket number. Oura states the ring is not a medical device. Natural Cycles' clearances (from K202897) cover temperature input from the Oura ring; those clearances are Natural Cycles', not Oura's (sources 38, 39).
- Oura's enterprise/government customer list (US military branches, NASA) implies some security maturity, but **do not infer compliance from a customer list**, obtain it in writing.

## Pricing

- **Ring (US store, Verified 2026-10-10):** Oura Ring 5 from **$399** (Silver, Black), **$499** for Gold, Deep Rose, Stealth and Brushed Silver; introduced 28 May 2026 (launch press, source 21). Oura Ring 4 is still sold, from **$349** (Silver, Stealth), some finishes $399 to $499; Oura Ring 4 Ceramic **$399** (source 22). Corrected 2026-10-11; the earlier text had Ring 5 prices from press only.
- **Membership:** **$5.99/month or $69.99/year** for US members, before tax (EU €5.99/€69.99 after tax), one tier only; first month free for new members. *Status: **Verified*** against ouraring.com/membership, 2026-10-10.
- **Total cost of ownership is the key number for research.** For a 100-participant, 12-month study, membership alone is roughly $7,000 on top of ring hardware, and it is **mandatory**, because without it the API returns nothing for Gen3+ users. Compare this to Garmin, where core metrics carry no subscription at all.
- **Consumer membership** has no minimum term and can be cancelled at any time (Membership Hub).
- **Organizational and research pricing is not public** (checked 2026-10-10). No academic or research discount is published; the Enterprise Platform is a licensed platform whose fees, Eligible Person count and term are set in each Order, and bulk orders start from a quote prepared by an Oura point of contact. No minimum order or term is published (sources 28, 30). This is the highest-value question to put to Oura.
- **API fees:** none today, but the API and MCP Agreement reserves the right to start charging, including differentiated pricing for business users (source 16). The effective per-participant API cost is the membership.
- **Waived or donated memberships:** not published as a program. One precedent exists: a secondary source reports Oura contributed Gen3 rings and memberships to Tidepool's diabetes research dataset (announced November 2025; **Reported**, source 41), so in-kind support happens case by case.
- **Organization-paid memberships do not auto-renew.** The Oura for Organizations team contacts administrators at least 30 days before expiry, and members are asked for a personal payment method seven days before the membership ends. Plan study end dates and any extension around this (partner support, source 31).

## Research Evidence and Validation

- Full extraction in `../validation-evidence.md`.

### Robbins et al. 2024, *Sensors* 24(20):6532, Oura's strongest evidence, with a caveat

- N=35 healthy adults (ages 20 to 50), single night, concurrent PSG at Brigham and Women's Hospital, Oura Ring **Gen3** on the non-dominant index finger.

| Measure | Oura Gen3 | Apple Watch S8 | Fitbit Sense 2 |
|---|---|---|---|
| **Four-stage Cohen's kappa** | **0.65** | 0.60 | 0.55 |
| Sleep, wake kappa | 0.60 | 0.60 | 0.52 |
| Deep sleep sensitivity | **79.5%** | 50.5% | 61.7% |
| REM sensitivity | 76.0% | 82.6% | 67.3% |
| Light sleep sensitivity | 78.2% | 86.1% | 78.0% |
| TST bias | +9 min (ns) | | |
| SE / WASO vs PSG | **no significant difference** | WASO −10 min (p=0.02) | |
| Device failures | **0 / 35** | 6 / 35 | 2 / 35 |

- Oura was the only device of the three with **no data loss**, and the only one whose sleep efficiency and WASO did not differ significantly from PSG. Both are genuinely strong results.

> ### ⚠️ Declared interest
> **The study was funded by Oura Ring Inc. The lead author serves on Oura's Medical Advisory Board
> and receives consulting fees from Oura.** **Verified** from the paper's own disclosures.
>
> The protocol is sound and the paper is peer-reviewed, so this is **Corroborated with a declared
> interest**, not independent evidence. Never cite the κ=0.65 figure without this attached.

### The ICC problem, applies to Oura as much as anyone

- The same paper reports intraclass correlation coefficients, which are widely ignored in favour of the kappa headline:

| Measure | Oura ICC | Interpretation |
|---|---|---|
| Total Sleep Time | 0.74 | Good |
| Sleep Efficiency | 0.74 | Good |
| Light Sleep | 0.40 | Fair |
| **Deep Sleep** | **0.32** | **Poor** |
| **REM Sleep** | **0.27** | **Poor** |

- Even the best-performing consumer sleep tracker has *poor* between-person reliability for deep sleep and REM stage summaries. **A study using nightly deep-sleep or REM minutes from Oura as an outcome is substantially measuring device noise.** TST and SE are the defensible stage-derived endpoints.

### Other PSG studies that include Oura (added 2026-10-09)

- Found in a date-sorted PubMed and Europe PMC pass on 2026-10-09. None is Oura-funded, so they are a
- useful check on Robbins. **The ranking is not stable across studies:** Oura led in Robbins (Oura-funded)
- and on two-state sleep/wake kappa in Miller 2022 (0.51; Somfit 0.48, WHOOP 0.44), was effectively tied with WHOOP
- and behind Somfit (0.52) on four-stage kappa in Miller 2022, and trailed three wrist devices in Lee 2023.
- Corrected 2026-10-10 against the Miller PDF. Miller et al. also caution that their analyses were "comparisons of six
- independent devices to gold-standard PSG and ECG rather than a comparison between devices", and Oura's data were
- exported from the app at 5-minute precision while WHOOP's 30-second epochs were supplied by WHOOP staff.

| Study | Oura hardware | Other devices, same night | Oura four-stage κ | Comparison | Funding / COI | Confidence |
|---|---|---|---|---|---|---|
| Miller DJ, Sargent C, Roach GD 2022, *Sensors* 22(16):6317 | Gen2 | Apple Watch S6, Garmin FR245, Polar Vantage V, **WHOOP 3.0**, Somfit | 0.43 (two-state κ 0.51, best of six) | WHOOP 0.44, Somfit 0.52, Apple 0.20 | Australian Institute of Sport; authors' CQU lab receives WHOOP funding and equipment, and WHOOP staff supplied WHOOP's epoch data | **Verified** (full text read) |
| Grandner MA et al. 2023, *Sleep* 46(1):zsac152 | V2 | Happy Ring, **WHOOP 3.0**, Fitbit Charge 4, Actiwatch 2 | Not in main text (supplement) | Sleep/wake accuracy Oura 0.88 vs WHOOP 0.86; specificity 0.49 vs 0.54 | 5 of 7 authors affiliated with Happy Health, the competing ring's maker (PubMed affiliations); NIH grant R01 MD011600 listed | **Reported.** Corrected 2026-10-10: the full text was never read (PDF not obtained; PMC and OUP bot checks; not open access in Europe PMC) and the abstract reports Happy Ring figures only |
| Lee T et al. 2023, *JMIR mHealth uHealth* 11:e50983 | Ring 3 (Gen3) | Galaxy Watch 5, Pixel Watch, Fitbit Sense 2, Apple Watch 8, plus nearables | **0.35** (macro F1 0.52) | Galaxy Watch 5 0.42, Fitbit Sense 2 0.42, Pixel Watch 0.40, Apple Watch 8 0.30 | Most authors employed by and hold stock in Asleep, maker of a competing app (SleepRoutine) | **Verified** (tables read) |
| Searles ME et al. 2026, *SLEEP Advances* 7(1):zpag006 | Gen3 | Fitbit Sense 2, Withings Sleep Mat, SleepScore Max | Not reported as κ | In older adults (n=19) Oura underestimated TST by 75.5 min and overestimated deep sleep by 71.5 min | NIH NIA P30 AG073107; "Financial disclosure: None" | **Verified** (full text read) |

- Two of these four are authored by a competing device's maker (Happy Health, Asleep). That is a
- different kind of interest from Robbins' Oura funding, but it is still an interest. Lee 2023 also
- recorded a hospital/clinic sample with mean AHI 18, so it is not directly comparable to Robbins'
- screened-healthy sample.

### What is missing

- ~~Oura has never been tested against WHOOP under the same protocol.~~ **Corrected 2026-10-09:** two
- PSG studies did test both, on older hardware: Miller et al. 2022 (Oura Gen2 vs WHOOP 3.0, N=53,
- four-stage κ 0.43 vs 0.44, effectively tied, with the caveats above) and Grandner et al. 2023 (Oura V2 vs WHOOP 3.0, N=30 to
- 33; published online 29 June 2022, before Miller). Dial et al. 2025 compared Oura Gen3/Gen4 with WHOOP 4.0 for resting HR and HRV, not sleep
- stages. No study has compared Gen3 or later with WHOOP 4.0 or later against PSG. The bridged estimate
- in `../validation-evidence.md` §3b remains the only (indirect) evidence for current-generation hardware.
- The PSG-tested hardware is **Gen3 at newest**. Ring 4 has independent data only for nocturnal resting
- HR and HRV (Dial et al. 2025: Gen4 CCC 0.98 and 0.99, against Gen3 0.97 and 0.97, so no evidence of a
- difference). Ring 5 has none. Rechecked 2026-10-09 in PubMed (`oura` with Gen4/Ring 4/Ring 5 terms,
- 1 hit, Dial) and Europe PMC full text (14 hits, none a validation of Ring 4 or 5 beyond Dial).
- **Unclear** whether Ring 4/5 sleep staging differs from Gen3.
- **SpO2 and skin temperature have no independent validation against a reference instrument.**
- Rechecked 2026-10-09 and re-run 2026-10-10: PubMed `(oura[tiab] OR whoop[tiab]) AND (SpO2 OR "oxygen saturation" OR oximet* OR "blood oxygen")` returns
- 3 hits (a vascular-age paper, a ketogenic-diet trial and an unrelated 2004 emergency-medicine review matching "whoop"), none a validation; Europe PMC full-text searches pairing Oura with reference oximeters
- (Masimo, Nonin, arterial blood gas) and with temperature-reference terms found none. Oura's
- temperature literature is association and prediction work (TemPredict, cycle tracking), mostly
- Oura-affiliated, not sensor-accuracy work. **Still open.**
- Temperature-based illness-onset detection (UCSF/TemPredict and related COVID-era work) remains
- Oura's strongest non-sleep literature. **Reported**, not re-verified this session.
- Health Radar, Blood Pressure Signals, and GLP-1 insights have **no located independent validation.**
- Finger skin temperature is peripheral, not core; interpret accordingly.

## Strengths

- Among consumer rings, the most PSG sleep-staging studies located in this knowledge base (a count of what was found here, not a systematic census; reworded 2026-10-10), and by a clear margin the most comfortable device to actually sleep in, which means better nocturnal data completeness in practice, not just better algorithms. Its best PSG result is Oura-funded (Robbins 2024); independent PSG results are mixed (see Research Evidence, updated 2026-10-09).
- Continuous nocturnal RMSSD HRV and nightly temperature deviation, two research-grade-adjacent signals that most wrist competitors handle worse or not at all.
- Clean, well-documented REST API with rich per-night detail (stage hypnograms plus within-night HR/HRV traces).
- Webhook-first API design; Oura says correctly implemented webhook apps rarely hit rate limits (5,000 requests per 5 minutes, higher on request).
- iOS and Android.
- Participant self-export available even without membership, as a GDPR-backed fallback.
- Strong enterprise/government adoption suggests procurement paths exist for larger studies.

## Limitations

- **Mandatory paid membership for API access** on Gen3+, a recurring per-participant cost with no published academic waiver (one reported in-kind donation, Tidepool 2025).
- **No raw PPG, no raw accelerometry.** Everything is vendor-processed.
- **No GPS, altimeter, or barometer**, the ring cannot support mobility or location research at all.
- Ring sizing adds weeks to onboarding and creates mid-study fit failures.
- Not wearable by some occupational populations.
- Personal access tokens are gone (Verified 2026-10-10), which raises the engineering floor for small studies; an app is capped at 10 users until Oura approves it.
- Application-level aggregate rate limiting may constrain very large cohorts; the docs give 5,000 requests per 5 minutes without saying whether that is the per-token or per-application ceiling.
- **API Agreement (effective 8 June 2026):** no retention beyond what is strictly necessary, 72-hour deletion on request or subscription cancellation, no AI or ML training on API data, and no use of the API to evaluate or prompt AI models outside the MCP Server; participant consent does not lift these, and there is no research carve-out. Oura may also start charging for the API.
- Participant app-version dependence can silently break data types.
- Step counting is weaker than wrist devices.
- Compliance posture rests on vendor statements (HITRUST, annual SOC 2 examination, HIPAA for healthcare partners, BAA for business customers, geo-specific residency options for enterprise); no BAA template, DPA, ISO 27001 certificate or named hosting region is public.
- Vendor algorithm updates change metric definitions over time without researcher control, a known problem for Oura's readiness/score family specifically, which has been revised across generations.

## Best-Fit Use Cases

- Sleep research where staging quality and nocturnal wear compliance matter most (short of PSG).
- Circadian, menstrual cycle, ovulation, and fertility research using nightly temperature deviation.
- Illness-onset / infection-detection studies (temperature + HR + HRV + respiratory rate).
- Recovery, stress, and autonomic research needing continuous nocturnal RMSSD.
- Studies where an unobtrusive, screen-free device improves adherence or reduces reactivity (the device shows nothing on the wrist, so it is less likely to change behaviour).

## Poor-Fit Use Cases

- Any location, GPS, or mobility research.
- Step count or physical activity as a primary endpoint.
- Studies with no budget line for per-participant subscriptions.
- Raw signal research.
- Populations that cannot wear rings, or where finger size is unstable (pregnancy studies need particular care here).
- Rapid-deployment studies, sizing logistics prevent fast enrolment.

## Open Questions

- *(Directed to Oura: https://organizations.ouraring.com/solutions/researchers , api-support@ouraring.com.)*

- What does the Oura for Organizations research offering cost, who is eligible, and how does a team apply? Does it include waived or bulk memberships for study rings?
- What exactly is in its "raw data" export and its "premium metrics" for academics? Is any signal-level data (PPG, accelerometry) included?
- What does a Research Agreement say about retention and AI use? The Enterprise Platform route does not apply the API Agreement's 72-hour deletion to extracted data (privacy policy), but whether the Agreement's AI clauses (§4(d), §6(g)) have a research equivalent is not public.
- Is "Oura Teams", the researcher portal named in published studies, the current Enterprise Platform, and did the 5 October 2026 shutdown of Oura on the Web affect it?
- Is the 5,000 requests per 5 minutes limit per token or per application?
- What are the criteria and turnaround for approving an API app beyond 10 users?
- ~~Confirm the December 2025 Personal Access Token deprecation.~~ Resolved 2026-10-10: Oura's docs say PATs "are no longer available for use".
- Historical data depth retrievable via API for a newly authorised participant (no lookback limit documented, 2026-10-10).
- ~~Webhook availability.~~ Resolved 2026-10-10: webhooks are documented and recommended. Reliability in practice is untested.
- Is a BAA offered for a research cohort on the Enterprise Platform? Is there a DPA, and which hosting regions back the enterprise geo-specific residency option? ISO 27001 status. Note that the API Agreement is with Ouraring, Inc. (Delaware), not the Finnish Oura Health Oy, so EU headquarters alone says nothing about where data reside or which entity contracts. HITRUST, an annual SOC 2 examination, HIPAA for healthcare partners and BAAs for business customers are vendor-stated (security page and whitepaper, 2026-10-10).
- What happens to a participant's already-collected data if their membership lapses mid-study, is it retrievable later, or permanently inaccessible via API?
- ~~Current ring and membership pricing.~~ Resolved 2026-10-10: membership and Ring 4 and Ring 5 prices Verified on Oura's own pages.

## Vendor Fact Record

<!-- facts:begin -->
<!-- facts:end -->

## Key Links

- Official site: https://ouraring.com/
- Oura for Business / Organizations: https://organizations.ouraring.com/ (ouraring.com/business redirects here)
- Oura for research (researchers solution): https://organizations.ouraring.com/solutions/researchers
- Oura Research app (App Store): https://apps.apple.com/us/app/oura-research/id6748037636
- Oura API and MCP Agreement: https://cloud.ouraring.com/legal/api-agreement
- OpenAPI spec (v1.41): https://cloud.ouraring.com/v2/static/json/openapi-1.41.json
- Membership pricing: https://ouraring.com/membership
- Security page (formerly trust centre): https://ouraring.com/security
- Security whitepaper: https://ouraring.com/assets/documents/public-security-whitepaper.pdf
- Privacy policy: https://ouraring.com/privacy-policy
- Oura for Business terms: https://ouraring.com/business/terms-and-conditions
- Store (ring prices): https://ouraring.com/store
- API documentation (v2): https://cloud.ouraring.com/v2/docs and https://api.ouraring.com/v2/docs
- Developer portal: reached from Oura's partner support article https://partnersupport.ouraring.com/hc/en-us/articles/20949682312211-Using-the-Oura-API (the cloud.ouraring.com root now serves only an "Oura on the web" page, 2026-10-10; legacy app docs at https://cloud.ouraring.com/docs/)
- API error handling / rate limits: https://cloud.ouraring.com/docs/error-handling
- Oura support, The Oura API: https://support.ouraring.com/hc/en-us/articles/4415266939155-The-Oura-API
- Community Python client (useful endpoint reference): https://github.com/hedgertronic/oura-ring

## Sources

1. Oura Member Care, "The Oura API." https://support.ouraring.com/hc/en-us/articles/4415266939155-The-Oura-API (accessed 2026-08-21). **Primary.** Establishes the membership requirement for Gen3+ API access (for both users and partner apps), the Membership Hub GDPR download available to all users, and the app-version dependency for new data types.
2. Oura API v2 documentation. https://cloud.ouraring.com/v2/docs (accessed 2026-08-21, JavaScript-rendered, content not directly extractable in this session).
3. hedgertronic/oura-ring client README. https://github.com/hedgertronic/oura-ring (accessed 2026-08-21). Used as the endpoint inventory: 19 routes and their returned fields.
4. Oura API rate limiting and authentication (secondary, corroborated across sources): https://cloud.ouraring.com/docs/error-handling ; https://www.aifitnessapi.com/integrate/oura-api (accessed 2026-08-21). Original source of the 5,000 requests / 5 minutes figure, which Oura's own OpenAPI 1.41 FAQ also states (source 15, confirmed 2026-10-11); superseded by source 15.
5. Oura for Organizations. https://ouraring.com/business (accessed 2026-08-21). Establishes the enterprise segment and named customer categories.
6. Oura blog, 2024 validation study announcement. https://ouraring.com/blog/2024-sensors-oura-ring-validation-study/ (accessed 2026-08-21). Vendor framing of the *Sensors* study; note funding.
7. *Sensors* 2024;24(20):6532, "Accuracy of Three Commercial Wearable Devices for Sleep Tracking in Healthy Adults." https://www.mdpi.com/1424-8220/24/20/6532
8. Schyvens A.-M. et al. *SLEEP Advances* 2025;6(2):zpaf021. https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472, noted as **not** including Oura.
9. Oura membership pricing (secondary): https://www.bettervitals.com/learn/oura-ring-subscription-worth-it-2026 (accessed 2026-08-21). Superseded by source 18.
10. Miller DJ, Sargent C, Roach GD. "A Validation of Six Wearable Devices for Estimating Sleep, Heart Rate and Heart Rate Variability in Healthy Adults." *Sensors* 2022;22(16):6317. https://doi.org/10.3390/s22166317 (PMC9412437; accessed 2026-10-09). PDF: `../literature/whoop/2022-miller-sensors-six-wearables-sleep-hr-hrv-validation.pdf`.
11. Grandner MA, Bromberg Z, Hadley A, Morrell Z, Graf A, Hutchison S, Freckleton D. "Performance of a multisensor smart ring to evaluate sleep: in-lab and home-based evaluation of generalized and personalized algorithms." *Sleep* 2023;46(1):zsac152 (online 29 June 2022). https://doi.org/10.1093/sleep/zsac152 (PMC13396806; accessed 2026-10-09; PDF not obtained, PMC/OUP bot checks).
12. Lee T, Cho Y, Cha KS, et al. "Accuracy of 11 Wearable, Nearable, and Airable Consumer Sleep Trackers: Prospective Multicenter Validation Study." *JMIR mHealth uHealth* 2023;11:e50983. https://doi.org/10.2196/50983 (PMC10654909; accessed 2026-10-09; PDF not obtained, JMIR bot check).
13. Searles ME, Licata A, Cucinotta M, Kainec K, Spencer RMC. "Performance evaluation of consumer sleep-tracking wearables and nearables in healthy young and older adults." *SLEEP Advances* 2026;7(1):zpag006. https://doi.org/10.1093/sleepadvances/zpag006 (PMC12936866; accessed 2026-10-09; PDF not obtained, OUP bot check).
14. Dial MB et al. *Physiological Reports* 2025;13(16):e70527. https://doi.org/10.14814/phy2.70527, the only located independent data on Oura Gen4.
15. Oura API v2 OpenAPI specification, version 1.41. https://cloud.ouraring.com/v2/static/json/openapi-1.41.json (served by https://cloud.ouraring.com/v2/docs; accessed 2026-10-10). **Primary.** PAT retirement, 10-user cap before approval, free API, 5,000 requests per 5 minutes (FAQ) and two-layer rate limits (Rate Limits section), rate-limit headers, storage FAQ, Tag deprecation, sampling resolutions, webhooks (30 s after sync, 10 retries), 5-minute HR increments, Gen 3 note on SpO2, 403 on expired membership, route list, hardware enum (`gen4`, `or5`).
16. Oura API and MCP Agreement, effective 8 June 2026. https://cloud.ouraring.com/legal/api-agreement (accessed 2026-10-10). **Primary.** Retention, 72-hour deletion and deletion on subscription cancellation, AI and ML clauses §4(a)(iii), §4(c), §4(d) and §6(g), MCP Server as the only LLM route, reserved right to charge fees, benchmarking clause, aggregator approval, Ouraring, Inc. as counterparty, independent controllers, no research carve-out. The superseded 2021 version is at https://cloud.ouraring.com/legal/api-agreement/previous-terms/2021.
17. Oura for Organizations, "Oura for research". https://organizations.ouraring.com/solutions/researchers (accessed 2026-10-10). **Primary, vendor marketing.** Research dashboards, group download, raw-data CSV/JSON export, API integration, premium metrics for academics, HIPAA/GDPR statement, contact-only access.
18. Oura membership page. https://ouraring.com/membership (accessed 2026-10-10). **Primary.** $5.99/month or $69.99/year (US, before tax).
19. Oura trust centre. https://ouraring.com/trust-center (accessed 2026-10-10). **Primary, vendor statement.** HITRUST, annual independent audit under a SOC 2 heading, HIPAA for healthcare partners, encryption. The same text is on ouraring.com/security (source 23), which the vendor fact record cites.
20. Oura Research app, App Store listing (Oura Health Oy). https://apps.apple.com/us/app/oura-research/id6748037636 (accessed 2026-10-10). Participant app for research studies; version history 1.0 (22 April) to 1.0.11 (15 September).
21. Pulse 2.0, "Oura Reveals $399 Oura Ring 5 As The World's Smallest Smart Ring" (1 June 2026). https://pulse2.com/oura-reveals-399-oura-ring-5-as-the-worlds-smallest-smart-ring/ (accessed 2026-10-10). **Secondary/press.** Ring 5 $399 (Silver, Black) and $499 (premium finishes), introduced 28 May 2026.
22. Oura store. https://ouraring.com/store (accessed 2026-10-10). **Primary.** Ring 5 from $399, Ring 4 from $349, Ring 4 Ceramic $399 (US).
23. Oura security page. https://ouraring.com/security (accessed 2026-10-10). **Primary, vendor statement.** Annual independent audit, HIPAA for healthcare partners, encryption; no ISO 27001.
24. Oura public security whitepaper (August 2026). https://ouraring.com/assets/documents/public-security-whitepaper.pdf (accessed 2026-10-10). **Primary, vendor statement.** Annual SOC 2 examination and HITRUST certification, BAA enclave, GDPR adherence, geo-specific residency options, processed data for research partners.
25. Oura Member Care, membership article. https://support.ouraring.com/hc/en-us/articles/360025587353 (accessed 2026-10-10; last updated 6 October 2026). **Primary.** Membership prices (US and EU); Oura on the Web discontinued 5 October 2026.
26. Oura privacy policy. https://ouraring.com/privacy-policy (accessed 2026-10-10). **Primary.** Research App roles (sponsor controller, Oura processor), Enterprise Platform consent withdrawal and aggregated R&D use, consumer retention, Oura's own AI use, Business Associate role, not a covered entity for consumer services, Data Privacy Framework, servers outside the user's country.
27. Oura terms and conditions. https://ouraring.com/terms-and-conditions (accessed 2026-10-10). **Primary.** Research Sponsor selects study participants.
28. Oura for Business Products and Services Agreement. https://ouraring.com/business/terms-and-conditions (accessed 2026-10-10). **Primary.** Orders, fees and Eligible Person count; Research Agreement; BAA required before uploading PHI.
29. Oura partner support, "Using the Oura API". https://partnersupport.ouraring.com/hc/en-us/articles/20949682312211-Using-the-Oura-API (accessed 2026-10-10). **Primary.** Developer portal, membership gate for Gen3 users and partner apps, Gen2 unaffected.
30. Oura partner support, "Using the Bulk Order Portal". https://partnersupport.ouraring.com/hc/en-us/articles/45053628755347-Using-the-Bulk-Order-Portal (accessed 2026-10-10). **Primary.** Bulk orders start from a quote prepared by an Oura point of contact.
31. Oura partner support, "Managing Oura Membership for Organizations". https://partnersupport.ouraring.com/hc/en-us/articles/29588952984723-Managing-Oura-Membership-for-Organizations (accessed 2026-10-10). **Primary.** Organization memberships do not auto-renew; 30-day renewal contact.
32. Oura Member Care, Data Export. https://support.ouraring.com/hc/en-us/articles/360025441594 (accessed 2026-10-10). **Primary.** Membership Hub export (up to 10 days), Apple Health and Health Connect sync.
33. Oura Member Care, Data Export (Apple Health). https://support.ouraring.com/hc/en-us/articles/360025438734-Data-Export (accessed 2026-10-10). **Primary.** Heart rate exported to Apple Health in one-minute intervals.
34. Chinoy ED et al. *Nature and Science of Sleep* 2022 (PMC8957400). https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8957400/fullTextXML (accessed 2026-10-10). **Secondary.** Data exported from researcher portals set up by the device companies.
35. Haimovich et al. *JMIR Formative Research* 2026 (PMC13626187). https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13626187/fullTextXML (accessed 2026-10-10). **Secondary.** Data exported from the Oura Teams platform as CSV files.
36. 2025 study (PMC12440682). https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12440682/fullTextXML (accessed 2026-10-10). **Secondary.** Names "Oura Teams platform (Oura on the Web)".
37. Oura for Organizations, healthcare providers. https://organizations.ouraring.com/solutions/healthcare-providers (accessed 2026-10-10). **Primary, vendor marketing.** "Enterprise API" to send data to external systems.
38. openFDA device registration and listing, firm name Oura. https://api.fda.gov/device/registrationlisting.json?search=registration.owner_operator.firm_name:oura (accessed 2026-10-10). **Primary, regulator.** Registration 3015599655, Fertile Window, product code LHD.
39. FDA 510(k) and PMA database searches, applicant Oura. https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMN/pmn.cfm?start_search=1&Applicant=oura and https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMA/pma.cfm?start_search=1&applicant=oura (accessed 2026-10-10). **Primary, regulator.** No Oura-held clearance or approval.
40. Data Privacy Framework list. https://www.dataprivacyframework.gov/list (checked 2026-10-10). **Primary, regulator.** Oura's DPF participation.
41. FemTech Insider, "Tidepool and Oura collaborate to build diabetes research dataset". https://femtechinsider.com/tidepool-and-oura-collaborate-to-build-diabetes-research-dataset/ (accessed 2026-10-10). **Secondary/press.** Oura contributed Gen3 rings and memberships.
