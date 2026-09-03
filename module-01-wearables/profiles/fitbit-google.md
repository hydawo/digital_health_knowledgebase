# Fitbit / Google (Fitbit Web API → Google Health API)

## Quick Facts

| Field | Details |
|---|---|
| Organization | Google LLC (Fitbit acquired by Google, completed January 2021) |
| Category | Consumer wearable ecosystem with the most established academic research footprint |
| Current status | Active, **mid-migration**. Legacy Fitbit Web API turns down **September 2026** (widely reported 30 Sept); consumer app became **Google Health** on 19 May 2026 |
| Platforms/devices | Fitbit trackers and smartwatches (Charge, Inspire, Luxe, Sense, Versa, **Air**), Google Pixel Watch; iOS and Android via the Google Health app |
| Open source | No |
| Hosting/deployment | Vendor cloud (Google/Fitbit); researchers pull via REST API or via a third-party research platform |
| Pricing model | Device purchase + optional Fitbit Premium subscription; API access is free but gated by approval for the streams researchers most want |
| Last verified | 2026-08-21 |

## Summary

- Fitbit has historically been the default consumer wearable for academic research, it is the most-studied brand in the validation literature, and a mature research-support ecosystem grew up around it (most notably Fitabase, which reports over 1,600 publications using its platform). Its structural advantage over Apple is that it exposes a genuine **server-to-server OAuth API**, so a research team can pull a whole cohort's data without shipping a mobile app.

- **That advantage is currently in the middle of a disruptive transition.** Google is deprecating the legacy Fitbit Web API in September 2026 and replacing it with the Google Health API, built on Google Cloud with Google OAuth 2.0. This is not a cosmetic rebrand: the authorisation system changes, the API surface is restructured, all scopes are classified as Restricted (requiring privacy and security review), and, critically for study operations, **OAuth tokens do not transfer, so every enrolled participant must re-consent**.

- Any study running past September 2026 that touches Fitbit data needs a migration plan *now*. As of this writing (2026-08-21) the turndown is roughly one month away.

### The 2026 migration, verified timeline and the new access gates

- *(This section added 2026-08-21 second pass, after reading Google's migration, verification, rate-limit, scope and data-type documentation directly.)*

### Timeline

| Item | Detail | Confidence |
|---|---|---|
| Google Health API available for new integrations | From **late May 2026** | **Corroborated** |
| **Fitbit consumer app rebranded to "Google Health"** | **19 May 2026**; rollout complete on Android and iOS by 26 May 2026 | **Corroborated** |
| Fitbit Premium → **Google Health Premium** | Same rebrand; adds a Gemini-powered Health Coach | **Corroborated** |
| Features removed in the rebrand | Badges, direct messaging, **Sleep Profile** | **Reported** |
| Side-by-side operation | May → **30 September 2026** | **Corroborated** |
| Legacy Fitbit Web API turndown | September 2026, widely reported as **30 September**. Google's own migration page states no date | **Corroborated**; exact date **Unclear** from primary source |
| Google Fit API sunset | End of 2026, history auto-migrated to Google Health | **Corroborated** |
| Token portability | **Access and refresh tokens cannot be transferred**; every user must re-authenticate | **Verified** |
| Backfill after re-consent | The API provides tools to backfill historical data once a user re-authenticates | **Verified** |

- Google's guidance is to use dismissible banners and repeated warnings, making re-consent mandatory only "coinciding with the official Fitbit Web API deprecation deadlines." Users who do not re-authenticate before the legacy endpoints close **experience data gaps**, though their data remains intact if they keep syncing through the Google Health app. **Verified.**

### Three new access gates that did not exist under the Fitbit API

- **1. Unverified apps are capped at 100 users.** Most Google Health API scopes are Restricted. An unverified app is limited to **100 users** and 250 QPS in total. **Verified** (developers.google.com/health/app-verification).

- **2. Verification is two-part, and the second part costs money.**
- *OAuth app verification*, Google Trust and Safety reviews identity, requested scopes, and
- justifications.
- *Security assessment (CASA)*, a **third-party** Cloud App Security Assessment. Google documents
- Tier 2 at **2 to 3 weeks**, Tier 3 at **4 to 6 weeks**, and fees of **$500, $4,500 USD** by complexity. **Verified.**

- Apps accessing restricted data *from or through a third-party server* must additionally undergo an **annual** security assessment by a Google-approved assessor. **Corroborated.** A research team pulling cohort data to an institutional server is precisely that pattern.

- **3. In-app disclosure.** Apps must prominently show, during normal use, how they access and use health data, not buried in a menu or an external document. **Verified.**

- Documented exceptions to restricted-scope verification are: personal use; development, testing and staging; service-owned data only; **internal use within an organization**; and domain-wide installation. **Whether an academic study qualifies as "internal use within an organization" is Unclear, and it is the single cheapest question to resolve**, it is the difference between a free registration and a recurring four-figure assessment.

### Rate limits, now published, and generous

| Scope | Limit |
|---|---|
| Per project, daily | **86.4M requests/day** (~1,000 QPS sustained) |
| Per project, per minute | **120,000 requests/minute** (~2,000 QPS burst) |
| Per user, per minute | **300 requests/minute** (5 QPS) |
| Unverified apps | 250 QPS total across at most 100 users |

- **Verified** (developers.google.com/health/rate-limits); increases requested via Google Cloud Console. Compare Fitbit's legacy **150 requests/hour/user**: once through verification, throughput ceases to be a constraint. **The cost has moved from rate limits to compliance.**

### The intraday question, partially resolved, leaning negative

- Google Health API record types are **Interval**, **Sample**, **Session**, and **Daily Aggregate**. Reading the data-type documentation directly:

- **Heart Rate is a *Sample* type**, instantaneous measurements, with **no documented sampling
- interval anywhere**. There is no `detail-level` parameter and no endpoint family named Intraday. **Verified.**
- HRV, SpO2, respiratory rate and resting heart rate appear chiefly as **Daily Aggregates**
- (`Daily Heart Rate Variability`, `Daily Oxygen Saturation`, `Daily Respiratory Rate`, `Daily Resting Heart Rate`). **Verified.** This resolves the gap flagged earlier in this profile: those streams do exist in the new API, but visibly as daily rollups.
- Seventeen OAuth scopes exist, with `.readonly` / `.writeonly` variants, all prefixed
- `https://www.googleapis.com/auth/googlehealth`. **Verified.**

- **Assessment: Unclear, leaning negative.** Absence of a documented interval is not proof that dense data is unavailable, Sample records could be returned densely, but the legacy API's explicit intraday contract, approval process and detail-level parameter have **no visible counterpart**. Until someone registers a project and empirically measures the density of returned Heart Rate samples, **no study should assume minute-level heart rate survives the migration.**

### The Fitbit Air, the open question from the first pass, answered

- Launched **7 May 2026**, shipping 26 May, at **$99.99 / £84.99**. **Corroborated** (multiple independent trade outlets; not read from Google's store page).

| Attribute | Detail |
|---|---|
| Form factor | **Screenless**, no display, no buttons; 12 g with band |
| Sensors | Optical HR; **red + infrared** for SpO2; **skin temperature**; **3-axis accelerometer**; **gyroscope**; vibration motor |
| Heart rate | **Readings saved at 2-second intervals** |
| Tracking | HR, sleep, SpO2, AFib; claimed 15% sleep accuracy improvement from new ML models |
| Battery | **Up to 7 days**; 5-minute charge = 1 day |
| App | Google Health, Android and iOS |

- **Why this matters beyond the price.** A screenless $99 device with a gyroscope, 7-day battery and 2-second HR storage is close to an ideal cheap observational instrument: no display means no feedback-driven behaviour change (the reactivity problem that afflicts smartwatch studies), and 7-day battery removes the sleep-versus-charging conflict. If the 2-second HR resolution reaches the API, the Air becomes the best cost-per-physiological-signal option in the consumer category. Whether it does is the intraday question above.

## Products / Platform Architecture

- **Devices:** Fitbit trackers and smartwatches, plus Google Pixel Watch. Google states that all Fitbit devices and Pixel watches, current and previous, collect data returned through the Google Health API.
- **Sync path:** device → phone app (Bluetooth) → Google/Fitbit cloud → API.
- **Reconciled Stream:** the Google Health API includes a reconciled stream that harmonises overlapping data from multiple sources so API output matches what the user sees in the app. This is helpful for consistency but means the API is returning a *processed, arbitrated* view rather than a per-source raw record, relevant if a study wants to know which device produced a value.

## Sensors and Data Streams

- Every Module 1 profile uses the same table so devices can be compared row by row. Rows are the sensors named in `CLAUDE.md`. "Present" is about the hardware; "Researcher access" is about what a study can actually obtain, which is the module's central question. "Unclear" means nothing current was verified. The convention is recorded in [`../../shared/profile-table-conventions.md`](../../shared/profile-table-conventions.md).

| Sensor | Present | Researcher access to underlying signal | Resolution or sampling | Notes |
|---|---|---|---|---|
| PPG | Yes | No raw PPG. Derived HR only. | Intraday HR down to 1 second nominal |  |
| ECG | Sense, Sense 2, Charge 5 and 6, region-gated | Reading-level results in the legacy Web API; Google Health API lists ECG as a Q2 2026 addition. No raw waveform documented. | Per reading |  |
| Accelerometer | Yes | No raw accelerometry via the API. Derived steps, activity and sleep only. | Derived | The single biggest gap against research-grade actigraphy. |
| Gyroscope | Unclear | Not exposed | Unclear |  |
| Magnetometer | Unclear | Not exposed | Unclear |  |
| Temperature | Supported models | Nightly skin temperature variation, not raw. | Nightly |  |
| SpO2 | Supported models | Daily and intraday SpO2. | Intraday |  |
| GPS | Built in on some models, connected GPS on others | Exercise GPS coordinates listed as a Q2 2026 Google Health API addition. | Exercise sessions |  |
| Barometer / altimeter | Some models | Floors climbed. | Derived |  |
| EDA | Sense and Sense 2 | EDA Scan sessions in the app; API exposure not established. Treat as unavailable until confirmed. | On demand and continuous EDA |  |
| Ambient light | Unclear | Unclear | Unclear |  |
| Other | Unclear | Unclear | Unclear | Not verified against current documentation. |

**Verification.** As recorded in the Module 1 passes; see the notes below for the original table wording and the migration timeline.

### Notes from earlier verification passes

| Sensor | Present | Researcher access to underlying signal |
|---|---|---|
| PPG | Yes | No raw PPG. Derived HR only (intraday down to 1-second nominal). |
| ECG | Sense/Sense 2, Charge 5/6 (region-gated) | ECG endpoint existed in the legacy Web API (reading-level results); Google Health API lists ECG as a Q2 2026 addition. Raw waveform access not documented as available. |
| Accelerometer | Yes | **No raw accelerometry via the API.** Only derived steps/activity/sleep. This is the single biggest gap versus research-grade actigraphy. |
| SpO2 | Yes on supported models | Daily and intraday SpO2. |
| Temperature | Yes on supported models | Nightly skin temperature variation, not raw. |
| GPS | Built-in on some models; connected GPS on others | Exercise GPS coordinates listed as a Q2 2026 Google Health API addition. |
| Altimeter | Yes on some models | Floors climbed. |
| EDA | Sense / Sense 2 (cEDA and on-demand EDA Scan) | EDA Scan sessions surfaced in the app; **API exposure of EDA is not established**, treat as unavailable until confirmed. |

## Derived Metrics / Analytics

- Legacy Fitbit Web API endpoint families (24 documented categories): Active Zone Minutes time series, Activity, Activity time series, Authorization, Blood Glucose, Body, Body time series, Breathing Rate, Cardio Fitness Score (VO2 Max), Devices, Electrocardiogram, Friends, Heart Rate time series, Heart Rate Variability, Intraday, Irregular Rhythm Notifications, Nutrition, Nutrition time series, Sleep, SpO2, Subscription, Temperature, User.

- Google Health API data types, per Google's own roadmap:
- **Available now:** steps, sleep, workouts, nutrition, hydration, vitals, women's health, calories/energy.
- **Q2 2026 additions:** 175+ activity types, goals, ECG, heart rate zones, blood glucose, respiratory rate, and GPS coordinates during exercise.
- **Q3 2026 additions:** blood pressure, basal metabolic rate, mindfulness, basal body temperature.

- REST resources exposed by the Google Health API v4: `projects.subscribers`, `projects.subscribers.subscriptions`, `users` (identity, profile, settings), `users.dataTypes.dataPoints` (query/create/update), `users.pairedDevices`. Service endpoint `https://health.googleapis.com`. Rollup values are documented for active energy, active minutes, active zone minutes, activity level, altitude, blood glucose, body fat, calories in heart rate zones, core body temperature, distance, floors, heart rate, hydration, nutrition, run VO2 max, sedentary periods, steps, swim lengths, time in heart rate zones, total calories, and weight, via `rollUp`/`dailyRollUp` over civil- and physical-time intervals.

- **Gap:** whether HRV, SpO2, and skin temperature, all present in the legacy API, are fully represented in the Google Health API today is **not established** by the sources consulted. They are not named in Google's "available now" list nor in the Q2/Q3 roadmap. For any study depending on those streams, this is a blocking question for Google before September 2026.

### Intraday data, the key research gate

- Intraday (within-day, high-resolution) data is what makes Fitbit usable for most research, and it is **not open by default**.

- Available intraday types: activity, breathing rate, heart rate, heart rate variability, SpO2, Active Zone Minutes.
- Granularity: heart rate at 1-second, 1-minute, 5-minute, or 15-minute detail levels; steps/activity at 1-minute or 15-minute. Fitbit notes the `1sec` detail level may not actually return 1-second sampling outside recorded exercise, because sampling density itself varies with context.
- Access: automatic only for a developer's *own* data under a "Personal" application type. For other users' data via "Client" or "Server" application types, access is **granted case by case** on request, with non-profit research and personal projects treated more favourably than commercial applications.

- Plan for a multi-week approval delay, and do not assume approval.

## Active Data Collection

- None native. Fitbit is a passive-sensing ecosystem; surveys/EMA must come from a separate instrument or a research platform layered on top.

## Researcher and Study Management Features

- Google/Fitbit provide **no first-party research console**, no cohort enrolment, adherence monitoring, or device management. In practice, academic Fitbit studies use a third-party research platform, most commonly **Fitabase**, which supplies:
- dashboards for data sync status, battery level, and connection state
- automated SMS notifications to participants about sync lapses and charging
- large-volume programmatic exports in JSON or CSV, avoiding per-participant manual retrieval
- a research-oriented API of its own

- Fitabase also supports Garmin, making it a plausible route to a two-device study. Its pricing is quote-based and not published.

## Data Access and Export

| Route | Mechanism | Notes |
|---|---|---|
| Google Health API | Google OAuth 2.0; REST; all scopes Restricted (privacy/security review) | The forward path. Register the project in Google Cloud Console. |
| Legacy Fitbit Web API | Fitbit OAuth 2.0; REST; webhook subscriptions | **Turning down September 2026.** Ran side by side with the new API from May to 30 September 2026 with no planned downtime. |
| Fitabase (or similar) | Vendor-mediated | Handles auth, retention, monitoring, and export; adds a data processor. |
| Participant self-export | Google Takeout / Fitbit account export | Viable for small N. |

- **Migration facts to design around:**
- OAuth tokens do not carry over. Silent migration is not possible; **every participant must re-authorise**. For a longitudinal study with a distributed or hard-to-reach cohort, this is an operational project, not a code change, and it will cost data completeness.
- Authorisation moves from Fitbit's system to Google OAuth 2.0, letting developers use standard Google auth libraries.
- Historical data already retrieved and stored (e.g. in Fitabase) is unaffected. Fitabase states it obtained early access, has been testing with Google, and expects minimal change to existing datasets, while flagging that participant reauthorisation may be required.

## APIs, SDKs, and Extensibility

- REST + OAuth 2.0; webhook/subscription support for change notification (legacy API had a Subscription endpoint; the new API exposes subscriber/subscription resources).
- **Health Connect** (Android) is the separate on-device aggregation layer that Fitbit data can flow into on Android phones; it is the successor to Google Fit's on-device role and is a distinct integration path from the Google Health API cloud path.
- Fitbit OS app/clockface development (Fitbit SDK) exists but does not provide raw sensor archives suitable for research.

## Deployment and Infrastructure

- Vendor cloud. Research team needs a Google Cloud project, an approved OAuth consent configuration, and somewhere to land the pulled data, or it outsources all of that to a research platform.

## Participant Experience

- Works with **both iOS and Android**, a decisive advantage over Apple Watch for representative sampling.
- Battery life is a genuine strength: several days to a week or more on trackers (Charge/Inspire class), versus about a day for Apple Watch. Longer battery means better 24h coverage and better sleep-data completeness.
- Low participant burden; devices are cheap enough to provision to participants rather than requiring BYOD.
- Requires the participant to keep the companion app installed and syncing; sync lapses are the dominant source of missing data, which is exactly why Fitabase's sync-monitoring exists.
- The re-consent event in September 2026 is an unavoidable participant-facing disruption.

## Privacy, Security, and Compliance

- All Google Health API scopes are **Restricted**, requiring a privacy and security review before access is approved.
- **A material constraint for clinical research:** Google's Health API developer terms prohibit using the service for any purpose involving Protected Health Information as defined by HIPAA *unless prior written consent is obtained from Google*. A study handling PHI cannot simply assume it may route that data through this API, this requires explicit resolution with Google.
- Developer terms also require storing data at the same level of granularity at which it is collected, and reserve Fitbit/Google's right to remove or block data determined to be inaccurate, misleading, or harmful.
- Google references a separate "Google Health API User Data and Health Research Policy" and a "Research Pledge"; the specific URL consulted returned 404 during this session and the contents are **not established here**. This should be read in full before any IRB submission.
- Data residency: not established for the Google Health API in the sources consulted.

## Pricing

- **API:** no fee documented for either the legacy or new API; the gate is approval, not payment.
- **Devices:** trackers are among the cheapest research-viable wearables, which is a large part of why they dominate the literature, provisioning a 200-person cohort is financially realistic.
- **Fitbit Premium:** reported at $99.99/year in 2026 (up from $79.99), roughly $9.99/month. *Reported*, from secondary sources, not verified against a Google/Fitbit pricing page. Premium is generally **not required** for research data access.
- **Fitabase:** quote-based, no published rates; the vendor states pricing is crafted per study.

## Research Evidence and Validation

- **Most-studied brand.** Fitbit dominates the validation literature; a major systematic review covering 158 publications across nine brands found Fitbit by far the most examined.
- **Steps:** accurate in laboratory settings; the review found Apple, Fitbit, and Garmin accurate roughly half the time overall, with free-living conditions substantially degrading performance.
- **Heart rate:** acceptable on average (all brands within ~±3% in controlled settings) but Fitbit specifically **tends to underestimate**, and performed less well than Apple Watch and Garmin in that review.
- **Energy expenditure:** unacceptable, no brand met accuracy thresholds, MAPE >30%.
- **Sleep staging:** the 2024 *Sensors* four-stage comparison put Fitbit Sense at 61.7 to 78.0% sensitivity and 72.8 to 73.2% precision, below Oura. The independent 2025 Schyvens six-device study was harsher still, reporting Fitbit Sense at ~48.3% and Fitbit Charge 5 at ~43.3% agreement, with most devices differing significantly from PSG on total sleep time, sleep efficiency, WASO, and light sleep.
- The practical read: Fitbit's *sleep/wake and duration* outputs are usable for behavioural research; its *stage-level* outputs are not a substitute for PSG.

## Strengths

- True server-side OAuth API, no need to build a mobile app.
- iOS **and** Android, enabling representative recruitment.
- Cheapest credible hardware at cohort scale; long battery life; low participant burden.
- Deepest validation literature of any consumer brand, which simplifies methods sections and reviewer defence.
- A mature research-support ecosystem (Fitabase) that solves adherence monitoring and bulk export, and also covers Garmin.
- Broad metric coverage including SpO2, HRV, breathing rate, temperature, VO2max, and ECG on some models.

## Limitations

- **The September 2026 turndown is an active, near-term risk** requiring re-consent from every participant. Longitudinal studies spanning the cutover will take a completeness hit.
- Feature parity of the new Google Health API is incomplete: HRV, SpO2, and skin temperature are not confirmed present, and ECG/GPS/respiratory rate were still roadmap items for 2026.
- Intraday access, the thing research actually needs, is gated case by case and can be refused.
- **No raw accelerometry.** Rules Fitbit out where raw actigraphy is the endpoint.
- HIPAA/PHI use requires Google's prior written consent, which is a real barrier for clinical studies.
- No first-party study management; a third-party platform is effectively mandatory at scale, adding cost and another data processor to the IRB.
- Heart rate underestimation bias; energy expenditure unusable; sleep staging weak.
- Algorithm changes are pushed by the vendor without researcher control, threatening longitudinal comparability across a study's duration.

## Best-Fit Use Cases

- Large, mixed-OS behavioural or physical-activity cohorts on a constrained device budget.
- Step count, activity, sleep timing/duration, and resting heart rate as outcomes or covariates.
- Intervention studies where the device doubles as a participant-facing feedback tool.
- Studies that want a turnkey adherence-monitoring workflow (via Fitabase) rather than building one.

## Poor-Fit Use Cases

- Studies requiring raw accelerometry or raw PPG.
- Clinical sleep architecture endpoints.
- Energy expenditure as a primary endpoint.
- Studies handling PHI without a prior written arrangement with Google.
- Studies that cannot tolerate a forced participant re-consent event in September 2026.
- Studies needing guaranteed metric stability across several years, vendor algorithm updates are outside the researcher's control.

## Open Questions

- Are HRV, SpO2, and skin temperature available in the Google Health API today, and at what granularity? (For: Google Health API developer support.)
- Is intraday access preserved under the new API, and does the case-by-case approval process carry over, including for already-approved legacy applications?
- What are the Google Health API's rate limits and historical-data/backfill limits?
- What exactly does the "Research Pledge" and the "User Data and Health Research Policy" require of academic studies? (Referenced by Google's terms; the page consulted 404'd.)
- Under what circumstances will Google grant the written consent needed for PHI use?
- Is EDA (Sense cEDA / EDA Scan) exposed through any API?
- Data residency options for non-US studies.
- Fitabase pricing at typical cohort sizes. (For: hello@fitabase.com.)

## Key Links

- Fitbit developer portal (legacy): https://dev.fitbit.com/build/reference/web-api/
- Fitbit intraday documentation: https://dev.fitbit.com/build/reference/web-api/intraday/
- Google Health API overview: https://developers.google.com/health/about
- Google Health API REST reference: https://developers.google.com/health/reference/rest
- Google Health API developer terms: https://developers.google.com/health/policies/health-api-developer-terms-and-conditions
- Health Connect (Android): https://developer.android.com/health-and-fitness/health-connect
- Fitabase: https://www.fitabase.com/
- Fitabase pricing (quote-based): https://www.fitabase.com/how-it-works/pricing/
- Fitabase research library: https://www.fitabase.com/research-library/
- Fitbit Web API Data Dictionary (PDF, v9, Aug 2024): https://assets.ctfassets.net/0ltkef2fmze1/45IN5bvBS827grKEsA8ZB0/648f3778acc936961f0572590c005ef0/Fitbit-Web-API-Data-Dictionary-Downloadable-Version-2.pdf

## Sources

1. Fitbit Web API reference. https://dev.fitbit.com/build/reference/web-api/ (accessed 2026-08-21). Establishes the 24 endpoint categories, the intraday definition, and the September 2026 deprecation notice.
2. Fitbit intraday documentation. https://dev.fitbit.com/build/reference/web-api/intraday/ (accessed 2026-08-21). Establishes intraday data types and the case-by-case approval process for third-party access.
3. Google, "About the Google Health API." https://developers.google.com/health/about (accessed 2026-08-21). Establishes the replacement relationship, data-type roadmap by quarter, device coverage, Google OAuth 2.0, Reconciled Stream, and Restricted scope classification.
4. Google Health API REST reference. https://developers.google.com/health/reference/rest (accessed 2026-08-21). Establishes v4 resources, service endpoint, and rollup data types.
5. Google Health API developer terms and conditions. https://developers.google.com/health/policies/health-api-developer-terms-and-conditions (accessed 2026-08-21). Establishes the PHI prohibition absent prior written consent, and the granularity-preservation requirement.
6. Fitabase, "How We're Preparing for Google's New API." https://www.fitabase.com/blog/post/google-health-api-announcement/ (accessed 2026-08-21). Establishes vendor-side migration posture and the reauthorisation caveat.
7. Fitabase, homepage and research library. https://fitabase.com/ , https://www.fitabase.com/research-library/ (accessed 2026-08-21). Establishes Fitbit+Garmin support, monitoring/export features, and the ~1,610-publication figure.
8. Fitabase pricing page. https://www.fitabase.com/how-it-works/pricing/ (accessed 2026-08-21). Establishes that pricing is quote-based.
9. Fuller D. et al. *JMIR mHealth uHealth* 2020;8(9):e18694. https://mhealth.jmir.org/2020/9/e18694/
10. *Sensors* 2024;24(20):6532 (Oura-funded four-stage validation). https://www.mdpi.com/1424-8220/24/20/6532
11. Schyvens A.-M. et al. *SLEEP Advances* 2025;6(2):zpaf021. https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472
12. Migration commentary (secondary, corroborating the side-by-side window and re-consent requirement): Sahha, https://sahha.ai/blog/fitbit-api-sunset-migration/ ; Validic, https://help.validic.com/space/VCS/5513478151/ ; Thryve, https://www.thryve.health/blog/fitbit-api-deprecation (accessed 2026-08-21).
13. Fitbit Premium pricing (secondary, unverified against vendor page): https://trackervs.com/pricing/fitbit-premium-cost/ (accessed 2026-08-21).
