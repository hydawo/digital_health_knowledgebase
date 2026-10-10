# Oura

## Quick Facts

| Field | Details |
|---|---|
| Organization | Oura Health Oy (Ōura), Finland |
| Category | Consumer smart ring; sleep, recovery, and temperature focus |
| Current status | Active |
| Platforms/devices | Oura Ring (Gen3, Oura Ring 4, Oura Ring 5); iOS and Android app; **Oura Research** participant app for studies |
| Open source | No |
| Hosting/deployment | Vendor cloud (Oura Cloud), REST API v2 |
| Pricing model | Ring purchase + **mandatory membership subscription for API data access on Gen3 and later** |
| Last verified | 2026-08-21; API, API Agreement, research offering, membership price and trust centre re-verified 2026-10-10 |

## Summary

- Oura is the strongest consumer device for **sleep and nocturnal physiology**. Its form factor, a ring, puts the PPG sensor on the finger, where perfusion is better and motion artefact during sleep is lower than at the wrist, and it removes the screen-and-notifications distraction that makes wrist wearables uncomfortable to sleep in. In head-to-head PSG validation it led in Robbins 2024 (Oura-funded), but independent results are mixed (tied with WHOOP and behind Somfit on four-stage kappa in Miller 2022, behind three wrist devices in Lee 2023); see Research Evidence. Reworded 2026-10-10 to match that section.

- For research there are two decisive practical facts:

1. **The API is clean and comprehensive**, a well-structured REST v2 with roughly 19 documented data routes, OAuth 2.0, two-layer rate limits (numbers no longer published), webhooks, and date-ranged list endpoints. An app is limited to 10 users until Oura approves it.
2. **Data access is gated behind an active paid membership.** Oura's own support documentation states that Gen3-and-later users without an active Oura Membership cannot access their data through the Oura API, and neither can partner applications integrated with it. For a study, that means the subscription is not optional, it is a per-participant, per-month line item for the entire study duration, on top of the ring.

- That second fact is the single most important cost driver and is easy to miss when scoping a study.

- **Two further facts added 2026-10-10.** Oura now sells a first-party research offering (Oura for Organizations, "Oura for research"), with dashboards, group export and a participant app, so the API is no longer the only route. And the Oura API and MCP Agreement (effective 8 June 2026) limits how long API data may be kept and bars using it to train AI models; see Data Access and Export.

## Products / Platform Architecture

- **Oura Ring**, titanium ring, worn on a finger (Oura recommends index finger; sizing kit required before ordering, which adds lead time to participant onboarding).
- **Oura app** (iOS/Android), sync and participant-facing insights.
- **Oura Cloud / API v2**, REST, OAuth 2.0.
- **Oura for Business / Oura for Organizations**, enterprise offering aimed at employers, healthcare, academic and clinical research, and military. Oura reports 200+ customers across those segments including US Air Force, US Navy, US Army, NASA, and universities. `ouraring.com/business` now redirects to `organizations.ouraring.com` (checked 2026-10-10).
- **Oura for research** (organizations.ouraring.com/solutions/researchers), the research offering within Oura for Organizations. Corrected 2026-10-10; the earlier text said what a research customer receives was not established. See Researcher and Study Management Features.
- **Oura Research app** (Oura Health Oy, App Store), a separate participant-facing app "For participants enrolled in research studies using the Oura Ring", which "collects data from your Oura Ring and shares it securely with your study's research team with your consent". Version history runs from 1.0 (22 April) to 1.0.11 (15 September); the listing shows no year. **Verified** that the app exists (2026-10-10).

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
- **What is not published:** price, contract and membership terms, eligibility, the application process (contact form only), and what "raw data" means. Nothing on the page says signal-level data (PPG, accelerometry) is included; given that the public API exposes only derived metrics, "raw" most likely means Oura's derived metrics in tabular form, but that is an inference. "Premium metrics" are not defined either. **Verified** that the offering exists and what the page says (2026-10-10); its contents beyond the page are **Unclear**. All statements on the page are the vendor's own (**Corroborated** at most for any capability claim).
- **How it differs from the public API route:** the public API gives a self-built app per-user OAuth access to derived metrics, 10 users before approval, under the API Agreement's retention and AI-training limits. The research offering adds group management, dashboards, bulk export and support, at an unpublished price. Whether the API Agreement's retention limits also bind research customers, or a separate research agreement replaces them, is not public.

- In practice, academic Oura studies typically either (a) enrol participants through a custom OAuth app and pull per-participant data, or (b) use middleware. Provisioning is meaningfully harder than for wrist wearables because of **ring sizing**, each participant needs a sizing kit and a correct size before the actual device ships, adding weeks to onboarding and creating a real risk of mis-sized rings mid-study (finger size changes with temperature, hydration, pregnancy, and weight change).

## Data Access and Export

- **API v2**: OAuth 2.0 only. Oura's docs state that "personal access tokens were deprecated in December 2025 and are no longer available for use", for any integration, not only new ones. **Verified** (cloud.ouraring.com/v2/docs, OpenAPI 1.41, 2026-10-10).
- **User cap**: "API Applications are limited to **10** users before requiring approval from Oura. There is no limit once an application is approved." The docs also say "the Oura API is free to use for both personal and commercial applications". The approval form, criteria, turnaround and any cost are not published. **Verified** (2026-10-10).
- **Rate limits**: enforced at two layers, per access token and per application in aggregate across all its end-user tokens. The current documentation (OpenAPI 1.41) **no longer publishes numeric limits**; a 429 response carries `Retry-After`, `X-RateLimit-Limit`, `X-RateLimit-Window`, `X-RateLimit-Reset` and `X-RateLimit-Tier` headers. Oura recommends webhooks, says most applications that implement them correctly do not hit limits, and asks teams expecting higher volume to contact api-support@ouraring.com. The earlier figure of 5,000 requests per 5 minutes came from a secondary source and is not in current Oura documentation. **Verified** (2026-10-10).
- **List endpoints** accept `start_date` / `end_date`; single documents fetchable by id. Oura advises making "a single request for historical data when a user first connects", then using webhooks. How far back that first request can reach is not stated. **Unclear.**
- **Oura API and MCP Agreement, effective 8 June 2026 (read 2026-10-10, Verified).** These terms govern any app, including a study's own, that uses the API:
  - **Retention:** User Data obtained through the Oura API "may not be stored or retained beyond the duration strictly necessary" (§3(m)), and "retaining or storing User Data or Oura Data beyond the periods specified in this Agreement" is a Prohibited Use (§4(a)(x)).
  - **Deletion:** users may opt out or delete at any time; on a deletion request "you shall delete all User Data relating to such User within seventy-two (72) hours" (§5(f)). On termination all User Data must be deleted, with written certification if Oura asks (§14).
  - **AI and ML:** training, fine-tuning or improving any AI model, or putting User Data into "any training dataset, evaluation dataset, or benchmark dataset", is a Prohibited Use unless Oura gives prior written consent (§4(a)(iii)). A separate clause in capitals bars using User Data to train or improve "ANY AI MODEL OR OTHER ARTIFICIAL INTELLIGENCE OR MACHINE LEARNING SYSTEM", with no consent exception (§6(g)).
  - **Benchmarking and reverse engineering:** use "for purposes of monitoring the availability, performance, or functionality of Oura's products ... including without limitation benchmarking" (§4(a)(ii)) and deriving Oura's "scoring methodologies, signal processing techniques ... or analytical models" (§4(a)(xi)) are Prohibited Uses unless Oura consents in writing. Read literally, this may reach device-validation studies that use API data; that reading is **Unclear** and needs Oura or counsel.
  - **Sharing:** disclosing User Data to any third party is a Prohibited Use except as the Agreement provides (§4(a)(vi)).
  - **Aggregators:** an aggregator must register separately for each end customer and get Oura's prior written approval for each one, and may not store or cache User Data (§3(e), §3(m)).
  - **No research carve-out** appears in the Agreement. For a study this means a permanent analysis dataset, data deposit, and any model training on Oura API data need Oura's written agreement (or, for the §6(g) training ban, may not be obtainable at all under these terms).
- **Participant self-export**: all Oura users, including those without an active membership, can download data files through the Membership Hub, which Oura describes as GDPR-compliant. This is a useful fallback for participants whose membership lapses, and for studies that want a participant-mediated export path.
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
- **Trust centre (read 2026-10-10).** Oura states: "Oura obtains a HITRUST certification"; under a SOC 2 heading, "Each year, independent auditors carefully review our security controls"; "We also meet HIPAA requirements where we handle protected health information for a healthcare partner"; Bluetooth encrypted with AES-128, TLS 1.2+ in transit, AES-256 at rest. The research page says the enterprise platform "processes PHI in accordance with HIPAA" and complies with GDPR. These are vendor statements with no certificate or report linked: **Corroborated** (vendor self-statement).
- **Not stated publicly:** BAA availability, ISO 27001, data residency and retention period. Ask Oura (its trust centre offers security documentation on request). Oura's enterprise/government customer list (US military branches, NASA) implies some security maturity, but **do not infer compliance from a customer list**, obtain it in writing.

## Pricing

- **Ring:** Oura Ring 5 from **$399** (Silver, Black) to **$499** (premium finishes), introduced 28 May 2026. *Status: Corroborated* (launch press; not found on an Oura page fetched 2026-10-10). Whether Ring 4 is still sold was not checked.
- **Membership:** **$5.99/month or $69.99/year** for US members, before tax (EU €5.99/€69.99 after tax), one tier only; first month free for new members. *Status: **Verified*** against ouraring.com/membership, 2026-10-10.
- **Total cost of ownership is the key number for research.** For a 100-participant, 12-month study, membership alone is roughly $7,000 on top of ring hardware, and it is **mandatory**, because without it the API returns nothing for Gen3+ users. Compare this to Garmin, where core metrics carry no subscription at all.
- Whether Oura for Organizations' research offering has academic pricing, bulk membership, or waived membership for study rings is **not established**: the research page lists no prices and offers only a contact form (checked 2026-10-10). This is the highest-value question to put to Oura.

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
- Webhook-first API design; Oura says correctly implemented webhook apps rarely hit rate limits (numeric limits are not published).
- iOS and Android.
- Participant self-export available even without membership, as a GDPR-backed fallback.
- Strong enterprise/government adoption suggests procurement paths exist for larger studies.

## Limitations

- **Mandatory paid membership for API access** on Gen3+, a recurring per-participant cost with no documented academic waiver.
- **No raw PPG, no raw accelerometry.** Everything is vendor-processed.
- **No GPS, altimeter, or barometer**, the ring cannot support mobility or location research at all.
- Ring sizing adds weeks to onboarding and creates mid-study fit failures.
- Not wearable by some occupational populations.
- Personal access tokens are gone (Verified 2026-10-10), which raises the engineering floor for small studies; an app is capped at 10 users until Oura approves it.
- Application-level aggregate rate limiting may constrain very large cohorts; the limits are not published.
- **API Agreement (effective 8 June 2026):** no retention beyond what is strictly necessary, 72-hour deletion on request, and no AI or ML training on API data; no research carve-out.
- Participant app-version dependence can silently break data types.
- Step counting is weaker than wrist devices.
- Compliance posture rests on vendor statements (HITRUST, annual SOC 2-style audit, HIPAA for healthcare partners); no BAA, ISO 27001 or residency statement is public.
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
- Do research customers sign a separate agreement that replaces the API Agreement's retention, deletion and AI-training limits?
- What are the criteria and turnaround for approving an API app beyond 10 users?
- ~~Confirm the December 2025 Personal Access Token deprecation.~~ Resolved 2026-10-10: Oura's docs say PATs "are no longer available for use".
- Historical data depth retrievable via API for a newly authorised participant.
- ~~Webhook availability.~~ Resolved 2026-10-10: webhooks are documented and recommended. Reliability in practice is untested.
- BAA, ISO 27001, GDPR DPA, and data residency (Oura is EU-headquartered, which may be advantageous for EU studies, but confirm where data actually resides). HITRUST, an annual SOC 2-style audit and HIPAA for healthcare partners are vendor-stated (trust centre, 2026-10-10).
- What happens to a participant's already-collected data if their membership lapses mid-study, is it retrievable later, or permanently inaccessible via API?
- ~~Current ring and membership pricing.~~ Membership Verified 2026-10-10 ($5.99/month, $69.99/year US); Ring 5 price Corroborated from launch press only.

## Key Links

- Official site: https://ouraring.com/
- Oura for Business / Organizations: https://organizations.ouraring.com/ (ouraring.com/business redirects here)
- Oura for research (researchers solution): https://organizations.ouraring.com/solutions/researchers
- Oura Research app (App Store): https://apps.apple.com/us/app/oura-research/id6748037636
- Oura API and MCP Agreement: https://cloud.ouraring.com/legal/api-agreement
- OpenAPI spec (v1.41): https://cloud.ouraring.com/v2/static/json/openapi-1.41.json
- Membership pricing: https://ouraring.com/membership
- Trust centre: https://ouraring.com/trust-center
- API documentation (v2): https://cloud.ouraring.com/v2/docs and https://api.ouraring.com/v2/docs
- Developer portal: https://cloud.ouraring.com/
- API error handling / rate limits: https://cloud.ouraring.com/docs/error-handling
- Oura support, The Oura API: https://support.ouraring.com/hc/en-us/articles/4415266939155-The-Oura-API
- Community Python client (useful endpoint reference): https://github.com/hedgertronic/oura-ring

## Sources

1. Oura Member Care, "The Oura API." https://support.ouraring.com/hc/en-us/articles/4415266939155-The-Oura-API (accessed 2026-08-21). **Primary.** Establishes the membership requirement for Gen3+ API access (for both users and partner apps), the Membership Hub GDPR download available to all users, and the app-version dependency for new data types.
2. Oura API v2 documentation. https://cloud.ouraring.com/v2/docs (accessed 2026-08-21, JavaScript-rendered, content not directly extractable in this session).
3. hedgertronic/oura-ring client README. https://github.com/hedgertronic/oura-ring (accessed 2026-08-21). Used as the endpoint inventory: 19 routes and their returned fields.
4. Oura API rate limiting and authentication (secondary, corroborated across sources): https://cloud.ouraring.com/docs/error-handling ; https://www.aifitnessapi.com/integrate/oura-api (accessed 2026-08-21). Source of the 5,000 requests / 5 minutes figure, which current Oura documentation (source 15) does not publish; **superseded 2026-10-10** for rate limits and PAT status.
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
15. Oura API v2 OpenAPI specification, version 1.41. https://cloud.ouraring.com/v2/static/json/openapi-1.41.json (served by https://cloud.ouraring.com/v2/docs; accessed 2026-10-10). **Primary.** PAT retirement, 10-user cap before approval, free API, two-layer rate limits without numbers, rate-limit headers, webhooks (30 s after sync, 10 retries), 5-minute HR increments, Gen 3 note on SpO2, 403 on expired membership, route list, hardware enum (`gen4`, `or5`).
16. Oura API and MCP Agreement, effective 8 June 2026. https://cloud.ouraring.com/legal/api-agreement (accessed 2026-10-10). **Primary.** Retention, 72-hour deletion, AI and ML training bans, benchmarking clause, aggregator approval, no research carve-out.
17. Oura for Organizations, "Oura for research". https://organizations.ouraring.com/solutions/researchers (accessed 2026-10-10). **Primary, vendor marketing.** Research dashboards, group download, raw-data CSV/JSON export, API integration, premium metrics for academics, HIPAA/GDPR statement, contact-only access.
18. Oura membership page. https://ouraring.com/membership (accessed 2026-10-10). **Primary.** $5.99/month or $69.99/year (US, before tax).
19. Oura trust centre. https://ouraring.com/trust-center (accessed 2026-10-10). **Primary, vendor statement.** HITRUST, annual independent audit under a SOC 2 heading, HIPAA for healthcare partners, encryption.
20. Oura Research app, App Store listing (Oura Health Oy). https://apps.apple.com/us/app/oura-research/id6748037636 (accessed 2026-10-10). Participant app for research studies; version history 1.0 (22 April) to 1.0.11 (15 September).
21. Pulse 2.0, "Oura Reveals $399 Oura Ring 5 As The World's Smallest Smart Ring" (1 June 2026). https://pulse2.com/oura-reveals-399-oura-ring-5-as-the-worlds-smallest-smart-ring/ (accessed 2026-10-10). **Secondary/press.** Ring 5 $399 (Silver, Black) and $499 (premium finishes), introduced 28 May 2026.
