# Garmin

## Quick Facts

| Field | Details |
|---|---|
| Organization | Garmin Ltd. |
| Category | Consumer/prosumer multisport and health wearable ecosystem with a business-oriented API programme |
| Current status | Active for existing API partners. **New Garmin Connect Developer Program access requests paused since spring 2026, no reopening date** (Corroborated, 2026-10-10) |
| Platforms/devices | Very wide range: Forerunner, Fenix, Venu, Vivosmart/Vivoactive, Instinct, Epix, Lily, Index scales, HRM chest straps; iOS and Android companion app (Garmin Connect) |
| Open source | No |
| Hosting/deployment | Vendor cloud (Garmin Connect), REST API with push or ping/pull delivery |
| Pricing model | Device purchase; **no consumer subscription for core metrics**; API programme is free to join but business-use only, with license fees for some metrics (Garmin footnotes Enhanced Beat-To-Beat Interval: "Commercial use requires a license fee payment"). **New programme applications paused since spring 2026 (Corroborated)** |
| Last verified | 2026-08-21; programme status, Health API metric list, Health SDK and research platforms re-verified 2026-10-10 |

## Summary

- Garmin's distinguishing features for research are **battery life measured in weeks rather than days**, **no consumer subscription paywall on core health metrics**, and a genuine server-side API. The battery advantage is not a minor convenience: it substantially reduces the structured missingness that plagues Apple Watch studies and reduces participant burden in long deployments.

- The trade-off is commercial. The Garmin Connect Developer Program is explicitly **business-use only**, access is application-gated, and while Garmin states there are no licensing or maintenance fees for programme access, it also states that access to *some* metrics may require a license fee payment or a minimum device order quantity for commercial use. What that means concretely for an academic study is not published, which makes Garmin the platform where "you must contact the vendor" is most unavoidable.

- **Dated status as of 2026-10-10: new direct API access is closed.** Garmin's developer-programme overview page no longer offers a request link and reads "Stay tuned for more updates on the program" (read 2026-10-10). A Garmin reply forwarded on Garmin's own developer forum says "The application form for new API access requests is currently unavailable ... During this transition, new access requests are temporarily paused", with no reopening date, and Terra's blog (7 September 2026) reports the form was replaced by an "Under Construction" notice by spring 2026. **Corroborated** (forum post quoting Garmin plus one secondary source; no formal Garmin announcement found). Garmin's FAQ still says it confirms applications "within two business days", which is stale while the pause lasts. Existing approved integrations are reported to keep working. A new study's practical routes are a research platform that already holds access (Labfront, Fitabase, Fitrockr; see `data-intermediaries.md`) or the Health SDK "Request Now" form, which is a separate enterprise channel.

## Products / Platform Architecture

- The Garmin Connect Developer Program is split into distinct APIs:

| API | Content |
|---|---|
| **Health API** | All-day health summary metrics. Metric families listed on Garmin's page (re-read 2026-10-10): steps, intensity minutes, sleep, calories, heart rate, stress, pulse ox, Body Battery, body composition, respiration, blood pressure and **Enhanced Beat-To-Beat Interval** (footnoted "Commercial use requires a license fee payment"), plus epoch summaries and "second-level HR during activities" |
| **Activity API** | Full activity/workout data for 30+ activity types |
| **Women's Health API** | Menstrual cycle tracking and pregnancy information |
| **Training API** | Push structured workouts and training plans *to* users' devices |
| **Courses API** | Push courses to compatible wearables and cycling computers |

- Separately, Garmin offers device-side and companion tooling:
- **Connect IQ SDK**, on-device apps, watch faces, data fields; can access device sensors including the accelerometer from within a running app.
- **Garmin Health SDKs (Standard and Companion, Android/iOS).** Garmin's Health SDK page (read 2026-10-10) says they are "Available to Garmin Health enterprise partners", with "Evaluation: Free; Commercial Use: License Fee or Minimum Device Order Quantity", requested through a "Request Now" form. Both list **Accelerometer** and **Enhanced Beat-To-Beat Intervals** under Real-Time Streaming Metrics and under Customizable Data Logging (where the device family supports it), plus "Accelerometer (Sums Of Axis Crossings)" for logging. The Companion SDK offers "live streams of heart rate, stress scores, accelerometer, and more" while the user keeps Garmin Connect; the Standard SDK keeps the data out of Garmin Connect entirely. Sampling rates are not published. **Verified** (Garmin page), replacing the earlier Reported status.

- Data flow for the Health API: device → Garmin Connect app → Garmin cloud → your endpoint. Garmin supports both **Ping/Pull** (Garmin notifies, you fetch) and **Push** (Garmin posts data to you) architectures, and lets you subscribe only to the metric feeds you need, which keeps ingest volume manageable. Output is JSON.

## Sensors and Data Streams

- Every Module 1 profile uses the same table so devices can be compared row by row. Rows are the sensors named in `CLAUDE.md`. "Present" is about the hardware; "Researcher access" is about what a study can actually obtain, which is the module's central question. "Unclear" means nothing current was verified. The convention is recorded in [`../../shared/profile-table-conventions.md`](../../shared/profile-table-conventions.md).

| Sensor | Present | Researcher access to underlying signal | Resolution or sampling | Notes |
|---|---|---|---|---|
| PPG | Yes, Elevate optical | Derived HR; no raw PPG documented | Derived |  |
| ECG | Venu 3 and some newer models, region-gated | Not documented as available via the Health API | Per reading |  |
| Accelerometer | Yes | Not as raw data through the Health API (not listed among its metrics). Health SDK (Standard or Companion) lists "Accelerometer" for real-time streaming and logging; in-app via Connect IQ. | Rate not published | Health SDK is enterprise-partner only, licence fee or device MOQ for commercial use (Verified 2026-10-10). |
| Gyroscope | Some models | Not via Health API | Unclear |  |
| Magnetometer | Unclear | Unclear | Unclear |  |
| Temperature | Limited, model-specific | Not established | Unclear |  |
| SpO2 | Many mid and high-end models | Pulse ox summaries via the Health API | Summaries |  |
| GPS | Most models, often multi-band | Activity and route data via the Activity API | Activity routes | Multi-band GNSS on higher-end models is a genuine differentiator for outdoor work. |
| Barometer / altimeter | Many models | Derived floors and elevation | Derived |  |
| EDA | No | Not applicable | Not applicable |  |
| Ambient light | Unclear | Unclear | Unclear |  |
| Other | Beat-to-beat intervals from the optical sensor | **Enhanced BBI** with a per-beat confidence value: listed on the Health API (fee for commercial use) and in the Health SDK. Fitabase's API route captures it **during sleep**; Labfront's SDK route accumulates it across the day | Per beat | Vendor help pages, Reported (Fitabase, Labfront, read 2026-10-10). |

**Verification.** As recorded in the Module 1 passes from Garmin's developer documentation; see the notes below.

### Notes from earlier verification passes

| Sensor | Present (model-dependent) | Researcher access |
|---|---|---|
| PPG (Elevate optical HR) | Yes | Derived HR; no raw PPG documented |
| Pulse Ox (SpO2) | Many mid/high-end models | Pulse ox summaries via Health API |
| ECG | Venu 3 and some newer models (region-gated) | Not documented as available via the Health API |
| Accelerometer | Yes | **Not as raw data through the Health API.** In-app access via Connect IQ; livestream reportedly via Companion SDK. See Open Questions. |
| Gyroscope | Some models | Not via Health API |
| Barometric altimeter | Many models | Derived floors/elevation |
| GPS/GNSS (often multi-band) | Most models | Activity/route data via Activity API |
| Temperature | Limited/model-specific | Not established |
| EDA | No | n/a |

- Garmin's GNSS quality is a genuine differentiator, multi-band GPS on higher-end models is better than most wrist wearables for outdoor location and distance work.

## Derived Metrics / Analytics

- Health API summary types include steps, heart rate, sleep, stress, calories, respiration, body composition (with a compatible Index scale), pulse ox, and **epoch summaries**, short fixed-window activity aggregations that are the closest thing Garmin offers to a granular activity time series.

- Garmin's proprietary metrics (Body Battery, Training Readiness, Training Status, VO2max estimates, HRV Status, Sleep Score) are algorithmically derived and, like all vendor black-box metrics, are (a) not independently validated as a class and (b) subject to change by firmware update. Which of these are exposed through the API, and whether any require the license fee Garmin alludes to, is not established from public documentation.

## Active Data Collection

- None native. Garmin is a passive-sensing ecosystem; the Training API pushes workouts *to* the device rather than collecting participant-reported data.

## Researcher and Study Management Features

- **No first-party research console.** Garmin does not provide participant enrolment, adherence dashboards, or study management. Third-party research platforms fill this gap: **Fitabase** (Fitbit and Garmin, quote only), **Labfront** (published prices; Garmin SDK partnership) and **Fitrockr** (published prices); see `data-intermediaries.md`. Several clinical-trial vendors also integrate Garmin.

### Research program and academic data access (added 2026-10-10)

- **No Garmin academic programme or academic tier exists.** The Connect Developer Program is "only for business use" and the FAQ does not address universities. There is no separate research API, history depth or data resolution for academics.
- **Direct access is closed to new applicants** (see Summary; Corroborated). When open, the programme has no fee, but Garmin footnotes Enhanced Beat-To-Beat Interval with "Commercial use requires a license fee payment" and the FAQ says "Access to some metrics may require a license fee payment or minimum device order quantity for commercial use." Whether academic use counts as commercial is not stated (**Verified** that it is not published).
- **What a study gets through the Health API:** daily and epoch summaries, sleep, stress, pulse ox, respiration, Body Battery, blood pressure, Enhanced BBI, and second-level HR during activities, by push or ping/pull JSON. Rate limits, latency and retention are not published. Backfill tooling exists ("backfill user data", Garmin page); one integrator documents backfill as limited to **30 days before the user's consent date** and needing the `HISTORICAL_DATA_EXPORT` permission (Open Wearables docs, **Reported**).
- **Research grants run through partners, not Garmin directly.** Fitrockr's grants page says "Fitrockr and Garmin support innovative research through grant programs"; the Garmin Health x Fitrockr Health Solutions Research Grant Asia 2026 offered five vívoactive 5 units and closed on 31 March 2026, and the page lists no current grant (**Verified**, fitrockr.com, 2026-10-10). Labfront runs its own grants programme (see `data-intermediaries.md`).
- **Practical route for an academic study today:** Labfront (Garmin SDK partnership, Enhanced or legacy BBI, published prices) or Fitabase (Garmin API route, Enhanced BBI during sleep, quote only), or Fitrockr.

## Data Access and Export

- **Health/Activity APIs**: OAuth-based user consent, then data syncs when the participant's device connects to Garmin Connect. Push or ping/pull delivery, JSON.
- **Backfill/historical data**: Garmin's model is oriented toward forward-looking subscription to a consented user's data. Garmin's Health API page lists "backfill user data" among its developer tools (Verified 2026-10-10) but gives no depth. A third-party integrator documents the depth as **30 days before the user's connection (consent) date**, one backfill request per user per timeframe, needing the `HISTORICAL_DATA_EXPORT` permission (Open Wearables, **Reported**, single secondary source). This matters a great deal for retrospective or run-in-period designs.
- **Participant self-export**: Garmin Connect allows users to export data and Garmin provides an account data export; also FIT files per activity, which are a rich per-activity binary format with high-resolution records.
- **FIT files** are worth noting: for activities, the FIT format contains second-level (or better) records and is openly documented by Garmin via the FIT SDK. This is a genuine high-resolution route that bypasses the summary-level API, but it is activity-scoped, not all-day.

## APIs, SDKs, and Extensibility

- REST + OAuth, push/ping-pull, JSON.
- Connect IQ SDK (on-device apps, Monkey C language).
- FIT SDK (open file format specification and parsing libraries).
- Health SDKs, Standard and Companion (real-time streaming and customizable logging), enterprise partners only. **Verified** 2026-10-10.
- **Approval, currently paused (Corroborated, 2026-10-10).** Garmin's FAQ still says it confirms application status "within two business days" and that integration takes one to four weeks, but new access requests have been "temporarily paused" since spring 2026 with no reopening date (Garmin reply quoted on Garmin's developer forum; Terra blog, 7 September 2026). Existing approved integrations are reported to keep working.

## Deployment and Infrastructure

- Vendor cloud. The research team needs an endpoint capable of receiving pushes (or a scheduled puller), plus storage. No self-hosting option.

## Participant Experience

- **iOS and Android** both supported.
- **Battery life is the standout**: many Garmin models run one to three weeks between charges, and some solar models longer. This materially improves 24h wear coverage and sleep-data completeness versus daily-charge devices, and reduces the number of participant reminders a study must send.
- Devices are physically larger and more "sport" styled than Oura/Fitbit, which can affect acceptability in some populations (and sleep comfort).
- Requires the Garmin Connect app installed and syncing.
- Wide price range means a study can match device tier to budget, though sensor availability varies across that range, a heterogeneous device fleet produces heterogeneous data.

## Privacy, Security, and Compliance

- Not established from the sources retrieved in this session. Garmin publishes a privacy policy and the Garmin Connect Developer Program Agreement (PDF, linked below), but specific research-relevant claims, HIPAA posture/BAA availability, SOC 2, GDPR data processing agreements, data residency, deletion guarantees, were **not verified**. Do not assume any of them. This is a vendor-contact item.
- One vendor statement exists: Garmin's Health SDK page says "The Standard SDK is HIPAA-compliant, allowing you to aggregate and archive the data in your own systems" (read 2026-10-10). This is Garmin's description of itself, **Corroborated** at most, and no BAA is mentioned on any public Garmin page found.

## Pricing

- **Programme access:** Garmin states "there are no licensing or maintenance fees for access to the Garmin Connect Developer Program, but it is only for business use."
- **Metric licensing:** Garmin states "access to some metrics may require a license fee payment or minimum device order quantity for commercial use." The only metric Garmin footnotes publicly is **Enhanced Beat-To-Beat Interval** ("Commercial use requires a license fee payment", Health API page, Verified 2026-10-10). The amount, and whether academic use counts as commercial, are not published.
- **The $5,000 figure:** multiple third-party sources describe a one-time $5,000 administrative fee for production-level Health API access. **Status: Reported, and specifically flagged as unconfirmed**, one of those same sources notes the terms are set privately with approved developers and are not listed on any Garmin page. Do not budget against this number without direct confirmation from Garmin.
- **Devices:** wide retail range from entry trackers to premium multisport watches.
- **No consumer subscription** is required for core health metrics, a real cost advantage over WHOOP and Oura at cohort scale, and increasingly over Fitbit.

## Research Evidence and Validation

- **Heart rate:** the major systematic review of steps/EE/HR found Garmin among the more accurate brands for heart rate (alongside Apple), with all brands within roughly ±3% under controlled conditions.
- **Steps:** accurate in lab settings; degraded in free living, consistent with the rest of the category.
- **Energy expenditure:** unacceptable, as with every consumer brand (MAPE >30%).
- **Sleep staging:** weak. The independent 2025 Schyvens six-device validation reported Garmin Vivosmart 4 at ~32.1% agreement for sleep-stage scoring against PSG, among the lowest of the six devices tested. Garmin sleep staging should not be used for stage-level endpoints.
- **Raw accelerometry:** Garmin devices have been included in mechanical shaker-table comparisons of raw accelerometry against ActiGraph, Apple Watch, and Fitbit, useful methodological literature for anyone attempting to treat consumer-device motion data as actigraphy.

## Strengths

- Exceptional battery life, the best data-completeness profile of any mainstream consumer wearable.
- No consumer subscription for core metrics.
- Server-side API with both push and ping/pull, and selective metric subscription.
- iOS and Android.
- Strong heart rate accuracy and excellent GNSS.
- FIT file format is openly documented and high-resolution for activities.
- On-device programmability via Connect IQ, unusual among consumer wearables and useful for custom study logic.
- Broad device range lets studies match hardware to budget and to participant population.

## Limitations

- **Business-use-only programme with opaque commercial terms**, the least transparent access path of the major consumer ecosystems, and a poor fit for a small academic grant that cannot absorb an unknown fee.
- **New programme applications paused since spring 2026** (Corroborated); a new study currently needs a partner platform.
- No raw accelerometry or raw PPG through the Health API.
- No first-party study management; a third-party platform is needed at scale.
- Sleep staging validity is poor.
- Proprietary metrics (Body Battery, Training Readiness) are black boxes subject to firmware-driven change.
- Compliance posture unverified, a blocker for regulated studies until confirmed.
- Sensor availability varies sharply across the product line.

## Best-Fit Use Cases

- Long-duration free-living studies where wear compliance and 24h coverage are the binding constraint.
- Physical activity, exercise, and outdoor/mobility research needing good GPS and HR.
- Studies where a per-participant subscription cost would be prohibitive.
- Athletic, military, occupational, and field-research populations where the device style and ruggedness fit.
- Teams that can write a Connect IQ app for bespoke on-device behaviour.

## Poor-Fit Use Cases

- Studies requiring raw accelerometry as an endpoint.
- Clinical sleep architecture endpoints.
- Small academic studies that cannot enter a commercial agreement or absorb undisclosed licensing costs.
- Regulated/PHI studies, until Garmin's compliance offering is confirmed in writing.
- Populations where a large sport watch is unacceptable.

## Open Questions

- *(All directed to Garmin: connect-support@developer.garmin.com, or the developer programme request form.)*

- When will Garmin reopen Connect Developer Program access requests, and will the updated programme admit universities?
- What, precisely, is the cost for an academic research team to obtain production Health API access? Is the widely repeated $5,000 administrative fee real and current?
- **Which specific metrics require a license fee or minimum device order?** Partly answered 2026-10-10: Enhanced BBI is the only one footnoted publicly; amount and academic treatment unknown.
- Does Garmin grant developer programme access to universities and non-profit research groups, given the "business use only" framing?
- Does the Health API support historical backfill, and how far back? Partly answered: tooling exists; 30 days before consent per one integrator (Reported).
- What are the Health API rate limits and data latency?
- At what sampling rate does the Health SDK stream and log accelerometer, and on which devices? (Availability and licence model Verified 2026-10-10; rates unpublished.)
- Is ECG data available via API on the models that support it?
- HIPAA posture (is a BAA available?), SOC 2, GDPR DPA, and data residency options.
- Data retention and participant deletion mechanics.

## Key Links

- Developer programme: https://developer.garmin.com/gc-developer-program/overview/
- Health API: https://developer.garmin.com/gc-developer-program/health-api/
- Programme FAQ: https://developer.garmin.com/gc-developer-program/program-faq/
- Developer Program Agreement (PDF): https://www8.garmin.com/en-US/GARMINCONNECTDEVELOPERPROGRAMAGREEMENT/GARMINCONNECTDEVELOPERPROGRAMAGREEMENT_EN.pdf
- Connect IQ developer site: https://developer.garmin.com/connect-iq/overview/
- FIT SDK: https://developer.garmin.com/fit/overview/
- Garmin Health (business): https://www.garmin.com/en-US/health/
- Developer support: connect-support@developer.garmin.com
- Fitabase (third-party Garmin research support): https://fitabase.com/

## Sources

1. Garmin Health API programme page. https://developer.garmin.com/gc-developer-program/health-api/ (accessed 2026-08-21). Establishes summary metrics, JSON output, ping/pull vs push, selective feed subscription, and that commercial use requires a license fee payment.
2. Garmin Connect Developer Program overview. https://developer.garmin.com/gc-developer-program/overview/ (accessed 2026-08-21). Establishes the five API products and their content.
3. Garmin Connect Developer Program FAQ. https://developer.garmin.com/gc-developer-program/program-faq/ (accessed 2026-08-21). Establishes "no licensing or maintenance fees … but it is only for business use", the metric-specific license/minimum-order caveat, two-business-day application confirmation, and one-to-four-week integration.
4. TechDepot developer access guide (secondary). https://techdepot.blog/garmin-api-access-guide (accessed 2026-08-21). Source of the reported $5,000 administrative fee and the Companion SDK accelerometer livestream claim. **Unconfirmed.**
5. AIFitnessAPI, Garmin API pricing (secondary). https://aifitnessapi.com/pricing/garmin-api-pricing (accessed 2026-08-21). Explicitly states Garmin's commercial terms are private and unpublished.
6. Fuller D. et al. *JMIR mHealth uHealth* 2020;8(9):e18694. https://mhealth.jmir.org/2020/9/e18694/
7. Schyvens A.-M. et al. *SLEEP Advances* 2025;6(2):zpaf021. https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472
8. "Comparison of raw accelerometry data from ActiGraph, Apple Watch, Garmin, and Fitbit using a mechanical shaker table." https://pmc.ncbi.nlm.nih.gov/articles/PMC10980217/ (preprint: https://www.medrxiv.org/content/10.1101/2023.05.25.23290556.full.pdf)
9. Fitabase (Garmin support). https://fitabase.com/ (accessed 2026-08-21).
10. Garmin Connect Developer Program overview, Health API page and Program FAQ. https://developer.garmin.com/gc-developer-program/overview/ ; https://developer.garmin.com/gc-developer-program/health-api/ ; https://developer.garmin.com/gc-developer-program/program-faq/ (re-read 2026-10-10). **Primary.** Overview: no request link, "Stay tuned for more updates on the program". Health API: metric list incl. Enhanced BBI with fee footnote, backfill tooling. FAQ: business use only, two-business-day wording.
11. Garmin Health SDK overview. https://developer.garmin.com/health-sdk/overview/ (accessed 2026-10-10). **Primary.** Enterprise partners only; evaluation free, commercial licence fee or device MOQ; accelerometer and Enhanced BBI streaming and logging; Standard SDK "HIPAA-compliant" vendor statement.
12. Garmin developer forum, "Cannot access Developer Program application form, Under Construction". https://forums.garmin.com/developer/connect-iq/f/discussion/434798/cannot-access-developer-program-application-form-under-construction/2027757 (accessed 2026-10-10). Forum post quoting a Garmin reply that new access requests are "temporarily paused".
13. Terra, "Garmin's Connect Developer Program is paused", 7 September 2026. https://tryterra.co/blog/garmin-connect-developer-program-pause (accessed 2026-10-10). Secondary.
14. Open Wearables, Historical Data Availability. https://openwearables.io/docs/providers/historical-data (accessed 2026-10-10). Secondary; Garmin backfill 30 days before consent.
15. Fitrockr Research Grants. https://www.fitrockr.com/research/research-grants/ (accessed 2026-10-10). Garmin Health x Fitrockr Research Grant Asia 2026, closed 31 March 2026.
16. Fitabase, Collecting Enhanced BBI using Garmin devices; Labfront, Understanding Enhanced BBI and Garmin overview. https://fitabase.com/resources/knowledge-base/learn-about-garmin-data/collecting-enhanced-beat-to-beat-interval-data-using-garmin-devices/ ; https://help.labfront.com/understanding-enhanced-bbi ; https://help.labfront.com/garmin-overview (accessed 2026-10-10). Vendor help pages: Fitabase's API route captures Enhanced BBI during sleep; Labfront's SDK partnership raises sensor resolution and offers legacy, enhanced or both.
