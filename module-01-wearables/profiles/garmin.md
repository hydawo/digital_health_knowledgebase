# Garmin

## Quick Facts

| Field | Details |
|---|---|
| Organization | Garmin Ltd. |
| Category | Consumer/prosumer multisport and health wearable ecosystem with a business-oriented API programme |
| Current status | Active for existing API partners. **New Garmin Connect Developer Program access requests paused since spring 2026, queued requests also on hold, no reopening date** (Corroborated, 2026-10-10). Garmin Health research and Health SDK routes active (Corroborated) |
| Platforms/devices | Very wide range: Forerunner, Fenix, Venu, Vivosmart/Vivoactive, Instinct, Epix, Lily, Index scales, HRM chest straps; iOS and Android companion app (Garmin Connect) |
| Open source | No |
| Hosting/deployment | Vendor cloud (Garmin Connect), REST API with push or ping/pull delivery |
| Pricing model | Device purchase; **no subscription needed for core metrics** (optional Garmin Connect+ at US $6.99 a month or $69.99 a year since March 2025); API programme is free to join but business-use only, with license fees for some metrics (Garmin footnotes Enhanced Beat-To-Beat Interval: "Commercial use requires a license fee payment"). **New programme applications paused since spring 2026 (Corroborated)** |
| Last verified | 2026-10-11 (vendor fact record); earlier passes 2026-08-21 and 2026-10-10; Schyvens 2025 figures corrected from full text 2026-10-10 |

## Summary

- Garmin's distinguishing features for research are **battery life measured in weeks rather than days**, **no subscription paywall on core health metrics** (Garmin Connect+ is optional and is not needed for API or SDK data), and a genuine server-side API. The battery advantage is not a minor convenience: it substantially reduces the structured missingness that plagues Apple Watch studies and reduces participant burden in long deployments.

- The trade-off is commercial. The Garmin Connect Developer Program is explicitly **business-use only**, access is application-gated, and while Garmin states there are no licensing or maintenance fees for programme access, it also states that access to *some* metrics may require a license fee payment or a minimum device order quantity for commercial use. What that means concretely for an academic study is not published, which makes Garmin the platform where "you must contact the vendor" is most unavoidable.

- **Dated status as of 2026-10-10: new direct API access is closed.** Garmin's developer-programme overview page no longer offers a request link and reads "Stay tuned for more updates on the program" (read 2026-10-10). A Garmin reply forwarded on Garmin's own developer forum says "The application form for new API access requests is currently unavailable ... During this transition, new access requests are temporarily paused", with no reopening date, and Terra's blog (7 September 2026) reports the form was replaced by an "Under Construction" notice by spring 2026. The5krunner (14 September 2026) reports that requests already in the queue are also on hold, and that Garmin describes the reason as a redesign of the API programme. **Corroborated** (forum post quoting Garmin plus one secondary source; no formal Garmin announcement found). Garmin's FAQ still says it confirms applications "within two business days", which is stale while the pause lasts. Existing approved integrations are reported to keep working. A new study's practical routes are a research platform that already holds access (Labfront, Fitabase, Fitrockr; see `data-intermediaries.md`) or the Health SDK "Request Now" form, which is a separate enterprise channel.

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
| ECG | Venu 3 and some newer models, region-gated | Not documented as available via the Health API | Per reading | Garmin ECG App is FDA 510(k) K221774 (2023-01-12), Garmin's only 510(k) (Verified, openFDA, 2026-10-10). |
| Accelerometer | Yes | Not as raw data through the Health API (not listed among its metrics). Health SDK (Standard or Companion) lists "Accelerometer" for real-time streaming and logging; in-app via Connect IQ. | Garmin publishes no rate. SDK logging fixed at 25 Hz per two integrators (Corroborated). Connect IQ apps set the rate up to a device-reported maximum (Verified) | Health SDK is enterprise-partner only, licence fee or device MOQ for commercial use (Verified 2026-10-10). |
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

- Health API summary types include steps, heart rate, sleep, stress, calories, respiration, body composition (with a compatible Index scale), pulse ox, and **epoch summaries**, short fixed-window activity aggregations that are the closest thing Garmin offers to a granular activity time series. Garmin publishes no epoch length. Fitabase reports 15-minute epochs for steps, heart rate and intensity, with stress every 3 minutes (Reported, single integrator).

- Garmin's proprietary metrics (Body Battery, Training Readiness, Training Status, VO2max estimates, HRV Status, Sleep Score) are algorithmically derived and, like all vendor black-box metrics, are (a) not independently validated as a class and (b) subject to change by firmware update. Which of these are exposed through the API, and whether any require the license fee Garmin alludes to, is not established from public documentation.

## Active Data Collection

- None native. Garmin is a passive-sensing ecosystem; the Training API pushes workouts *to* the device rather than collecting participant-reported data.

## Researcher and Study Management Features

- **No first-party research console.** Garmin does not provide participant enrolment, adherence dashboards, or study management. Third-party research platforms fill this gap: **Fitabase** (Fitbit and Garmin, quote only), **Labfront** (published prices; Garmin SDK partnership) and **Fitrockr** (published prices); see `data-intermediaries.md`. Several clinical-trial vendors also integrate Garmin.

### Research program and academic data access (added 2026-10-10)

- **No Garmin academic programme or academic tier exists.** The Connect Developer Program is "only for business use" and the FAQ does not address universities. There is no separate research API, history depth or data resolution for academics.
- **Direct access is closed to new applicants** (see Summary; Corroborated). When open, the programme has no fee, but Garmin footnotes Enhanced Beat-To-Beat Interval with "Commercial use requires a license fee payment" and the FAQ says "Access to some metrics may require a license fee payment or minimum device order quantity for commercial use." Whether academic use counts as commercial is not stated (**Verified** that it is not published).
- **What a study gets through the Health API:** daily and epoch summaries, sleep, stress, pulse ox, respiration, Body Battery, blood pressure, Enhanced BBI, and second-level HR during activities, by push or ping/pull JSON. Rate limits and latency are not published (evaluation access is "throttled" and the agreement mentions request-volume limits, with no figures). Retention appears only in the agreement's EU transfer annex (see Privacy). Backfill tooling exists ("backfill user data", Garmin page); one integrator documents backfill as limited to **30 days before the user's consent date** and needing the `HISTORICAL_DATA_EXPORT` permission (Open Wearables docs, **Reported**).
- **Research grants are run by Garmin Health with Fitrockr.** Garmin's own release says Garmin Health launched the Asia 2026 grant on 2 February 2026 with Fitrockr (**Verified**, Garmin newsroom). It was open to postgraduates, PhD candidates and senior scholars in 11 Asian markets. It offered five vívoactive 5 units and closed on 31 March 2026. Fitrockr's grants page lists no current grant (**Verified**, fitrockr.com, 2026-10-10). Labfront runs its own grants programme (see `data-intermediaries.md`).
- **Enterprise research offering.** Garmin Health has sold research access since 2022 (launched as Garmin Health Research Solutions). Garmin describes high-resolution data by definable interval logging, independent data hosting and device control (**Verified**, Garmin newsroom). Pricing is not public.
- **Direct institutional deals.** Garmin is the exclusive smartwatch provider for King's College London's EMBRACE programme, with up to 40,000 adult participants (announced 17 September 2025). Garmin calls it its largest collaboration with a research institution to date (**Verified**, Garmin newsroom).
- **Eligibility.** An integrator reports that Connect Developer Program applicants must be a legal entity, universities included, and that personal applications are rejected (Open Wearables, **Reported**). Garmin's own pages say only "business use".
- **Practical route for an academic study today:** Labfront (Garmin SDK partnership, Enhanced or legacy BBI, published prices) or Fitabase (Garmin API route, Enhanced BBI during sleep, quote only), or Fitrockr.

## Data Access and Export

- **Health/Activity APIs**: OAuth-based user consent, then data syncs when the participant's device connects to Garmin Connect. Push or ping/pull delivery, JSON.
- **Backfill/historical data**: Garmin's model is oriented toward forward-looking subscription to a consented user's data. Garmin's Health API page lists "backfill user data" among its developer tools (Verified 2026-10-10) but gives no depth. A third-party integrator documents the depth as **30 days before the user's connection (consent) date**, one backfill request per user per timeframe, needing the `HISTORICAL_DATA_EXPORT` permission (Open Wearables, **Reported**, single secondary source). This matters a great deal for retrospective or run-in-period designs.
- **Participant self-export**: Garmin Connect allows users to export data and Garmin provides an account data export; also FIT files per activity, which are a rich per-activity binary format with high-resolution records.
- **FIT files** are worth noting: for activities, the FIT format contains second-level (or better) records and is openly documented by Garmin via the FIT SDK. This is a genuine high-resolution route that bypasses the summary-level API, but it is activity-scoped, not all-day.
- **Informal routes are unreliable.** The unofficial Garth library, which many tools use to pull Garmin Connect data without the developer programme, is deprecated after Garmin changed its auth flow (garth.readthedocs.io, read 2026-10-10).

## APIs, SDKs, and Extensibility

- REST + OAuth, push/ping-pull, JSON.
- Connect IQ SDK (on-device apps, Monkey C language).
- FIT SDK (open file format specification and parsing libraries).
- Health SDKs, Standard and Companion (real-time streaming and customizable logging), enterprise partners only. **Verified** 2026-10-10.
- **Approval, currently paused (Corroborated, 2026-10-10).** Garmin's FAQ still says it confirms application status "within two business days" and that integration takes one to four weeks, but new access requests have been "temporarily paused" since spring 2026 with no reopening date (Garmin replies quoted on two Garmin developer forum threads; Terra blog, 7 September 2026). Requests already in the queue are also on hold, and Garmin gives a programme redesign as the reason (the5krunner, 14 September 2026). Existing approved integrations are reported to keep working.
- **Deprecations.** No API shutdown or deprecation is announced. The redesign has no published date or details, so terms or APIs may change (**Unclear**, 2026-10-10). Health SDKs must be updated to receive new data types (Garmin Health SDK Q&A).

## Deployment and Infrastructure

- Vendor cloud. The research team needs an endpoint capable of receiving pushes (or a scheduled puller), plus storage. No self-hosting option.

## Participant Experience

- **iOS and Android** both supported.
- **Battery life is the standout**: many Garmin models run one to three weeks between charges, and some solar models longer. This materially improves 24h wear coverage and sleep-data completeness versus daily-charge devices, and reduces the number of participant reminders a study must send.
- Devices are physically larger and more "sport" styled than Oura/Fitbit, which can affect acceptability in some populations (and sleep comfort).
- Requires the Garmin Connect app installed and syncing.
- Wide price range means a study can match device tier to budget, though sensor availability varies across that range, a heterogeneous device fleet produces heterogeneous data.

## Privacy, Security, and Compliance

- **Two developer agreement versions are live** (both FRM-0952 Rev. B, read 2026-10-10). The Garmin International version is on developerportal.garmin.com (New York law, EU SCC annex). The Garmin China Shanghai RHQ version is at the www8.garmin.com en-US path (PRC law, PIPL annex). No source says which one binds a licensee outside China (**Unclear**). Ask Garmin.
- **GDPR roles and DPA.** The International agreement makes Garmin an independent controller, not the licensee's processor. It incorporates EU Standard Contractual Clauses module one (controller to controller), with Garmin Würzburg GmbH as exporter for EEA, UK and Swiss data. No processor DPA is published (**Corroborated**). The China version attaches a PIPL standard contract for data leaving the PRC instead.
- **Retention and deletion.** The International agreement's SCC annex says the licensee keeps personal data while the user keeps an account with it or until the user asks for deletion. The licensee must honour access, erasure and export requests (**Verified**). No general retention cap appears elsewhere.
- **HIPAA.** Garmin's Health SDK page says "The Standard SDK is HIPAA-compliant, allowing you to aggregate and archive the data in your own systems" (read 2026-10-10). This is Garmin's description of itself, **Corroborated** at most. No HIPAA statement covers Garmin Connect or the cloud APIs.
- **BAA.** Unclear as of 2026-10-10. Garmin publishes no BAA. Paubox says Garmin will sign one, but its supporting link points to the Health SDK page, which mentions no BAA.
- **SOC 2 and ISO 27001.** Not public (2026-10-10). No certificate or report was found on Garmin pages. Garmin's FY2025 10-K describes alignment with the NIST Cybersecurity Framework and names no certification.
- **Data residency.** Unclear. Read by hand on 2026-10-10, the Garmin Connect privacy policy says account data is stored in the US, UK and/or Australia, and in mainland China for Chinese mainland customers. The page is script-rendered, so this was not quote-checked. The Health API offers no selectable residency. The Standard SDK keeps data off Garmin servers.
- **AI and machine learning.** No ban on using Garmin data for AI. The API Brand Guidelines require Garmin attribution when Garmin device data feeds analytics, ML models or AI. The International agreement has no AI clause. The China version (clause 15.10) requires a conspicuous AI transparency statement in the licensee's privacy policy and explicit user consent before AI processing, and lets Garmin audit compliance (**Verified**).
- **Publication and attribution.** Both agreement versions (section 8.4) bar press releases or public statements about Garmin or the agreement's subject matter without Garmin's written approval. How this applies to academic publication is not stated. Only the China version (6.4(a)) exempts Health API data used solely for research, defense or remote patient monitoring from Garmin attribution rules.
- **Regulatory.** The Garmin ECG App holds FDA 510(k) K221774 (decision 2023-01-12, product code QDA, applicant Garmin International), the only 510(k) with Garmin as applicant (**Verified**, openFDA). Garmin says the ECG App is a Class IIa device under EU MDR (Garmin Deutschland release, January 2025, not checked against EUDAMED). The Index BPM clearance, K221486, names Ya Horng Electronic Co., Ltd. as applicant, not Garmin. Pulse Ox, HRV and sleep features are wellness features with no clearance.

## Pricing

- **Programme access:** Garmin states "there are no licensing or maintenance fees for access to the Garmin Connect Developer Program, but it is only for business use." The developer agreement (section 10.1, both versions) says no licence fees or other payments are due under it (**Verified**).
- **Future fees reserved:** the agreement lets Garmin charge for any API on 30 days' notice and charge for request volume above the Application Requirements limits (**Verified**).
- **Metric licensing:** Garmin states "access to some metrics may require a license fee payment or minimum device order quantity for commercial use." The only metric Garmin footnotes publicly is **Enhanced Beat-To-Beat Interval** ("Commercial use requires a license fee payment", Health API page, Verified 2026-10-10). The amount, and whether academic use counts as commercial, are not published.
- **Health SDKs:** evaluation is free. Commercial use needs a licence fee or a device minimum order quantity commitment. Neither amount is published, and the Garmin Health team designs terms per customer (**Verified**). Fitrockr describes the SDK licence cost as high (Reported).
- **Academic pricing:** not public (2026-10-10). No academic price or discount is published.
- **The $5,000 figure: unsupported.** Some third-party pages describe a one-time $5,000 administrative fee for production Health API access. No Garmin page carries it, and section 10.1 of the agreement and the FAQ contradict it. Its cited source (techdepot.blog) returned 403 on 2026-10-10, and aifitnessapi.com says only that some third-party reports mention a setup fee. Do not budget against it.
- **Devices (US suggested retail at launch):** vívosmart 5 $149.99 (2022); CIRQA Smart Band, screen-free, $199.99 (July 2026); Forerunner 70 $249.99, Forerunner 170 $299.99, Forerunner 170 Music $349.99 (May 2026) (**Verified**, Garmin newsroom). Current store prices were not checked.
- **No subscription** is required for core health metrics, a real cost advantage over WHOOP and Oura at cohort scale, and increasingly over Fitbit. Optional Garmin Connect+ (launched March 2025) costs US $6.99 a month or $69.99 a year after a 30-day trial. Garmin says all existing Garmin Connect features stay free (**Verified**). It is not needed for API or SDK data, but participants with and without it may see different in-app insights.

## Research Evidence and Validation

- **Heart rate:** the major systematic review of steps/EE/HR found Garmin among the more accurate brands for heart rate (alongside Apple), with all brands within roughly ±3% under controlled conditions.
- **Steps:** accurate in lab settings; degraded in free living, consistent with the rest of the category.
- **Energy expenditure:** unacceptable, as with every consumer brand (MAPE >30%).
- **Sleep staging:** weak. The independent 2025 Schyvens six-device validation gave Garmin Vivosmart 4 an overall Cohen's kappa of 0.21 ("fair") against PSG, the lowest of the six devices tested, with deep-sleep (N3) accuracy of 47.46% (also the lowest) and REM accuracy of 33.10% (corrected 2026-10-10 from a stale search-summary percentage; full text read, see `../validation-evidence.md` §1). Garmin sleep staging should not be used for stage-level endpoints.
- **Raw accelerometry:** Garmin devices have been included in mechanical shaker-table comparisons of raw accelerometry against ActiGraph, Apple Watch, and Fitbit, useful methodological literature for anyone attempting to treat consumer-device motion data as actigraphy.

## Strengths

- Exceptional battery life, the best data-completeness profile of any mainstream consumer wearable.
- No subscription needed for core metrics (Connect+ is optional).
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
- Compliance posture thin for regulated studies. No BAA, SOC 2 report or ISO 27001 certificate is public, and Garmin acts as an independent controller rather than a processor under the developer agreement.
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
- What, precisely, is the cost for an academic research team to obtain production Health API access? (The $5,000 administrative fee is unsupported as of 2026-10-10; the agreement says no fees are due.)
- **Which specific metrics require a license fee or minimum device order?** Partly answered 2026-10-10: Enhanced BBI is the only one footnoted publicly; amount and academic treatment unknown.
- Does Garmin grant developer programme access to universities and non-profit research groups, given the "business use only" framing? (One integrator reports universities qualify as legal entities; Reported, Open Wearables.)
- Does the Health API support historical backfill, and how far back? Partly answered: tooling exists; 30 days before consent per one integrator (Reported).
- What are the Health API rate limits and data latency?
- At what sampling rate does the Health SDK stream and log accelerometer, and on which devices? (Availability and licence model Verified 2026-10-10. Garmin publishes no rate; two integrators report fixed 25 Hz logging.)
- Is ECG data available via API on the models that support it?
- Is a BAA offered for the Standard SDK? Are data residency options available? (SOC 2 and ISO 27001 not public; GDPR roles and retention partly answered by the agreement, see Privacy.)
- Which developer agreement version (Garmin International or Garmin China Shanghai RHQ) binds a US or EU licensee?
- Does section 8.4 (no public statements without Garmin approval) apply to academic publications?

## Vendor Fact Record

<!-- facts:begin -->
<!-- facts:end -->

## Key Links

- Developer programme: https://developer.garmin.com/gc-developer-program/overview/
- Health API: https://developer.garmin.com/gc-developer-program/health-api/
- Programme FAQ: https://developer.garmin.com/gc-developer-program/program-faq/
- Developer Program Agreement, Garmin International version (PDF): https://developerportal.garmin.com/sites/default/files/Garmin%20Connect%20Developer%20Program%20Agreement.pdf
- Developer Program Agreement, Garmin China Shanghai RHQ version (PDF): https://www8.garmin.com/en-US/GARMINCONNECTDEVELOPERPROGRAMAGREEMENT/GARMINCONNECTDEVELOPERPROGRAMAGREEMENT_EN.pdf
- Health SDK: https://developer.garmin.com/health-sdk/overview/
- Garmin Health research: https://www.garmin.com/en-US/health/solutions/research-and-clinical-trials/
- Connect IQ developer site: https://developer.garmin.com/connect-iq/overview/
- FIT SDK: https://developer.garmin.com/fit/overview/
- Garmin Health (business): https://www.garmin.com/en-US/health/
- Developer support: connect-support@developer.garmin.com
- Fitabase (third-party Garmin research support): https://fitabase.com/

## Sources

1. Garmin Health API programme page. https://developer.garmin.com/gc-developer-program/health-api/ (accessed 2026-08-21). Establishes summary metrics, JSON output, ping/pull vs push, selective feed subscription, and that commercial use requires a license fee payment.
2. Garmin Connect Developer Program overview. https://developer.garmin.com/gc-developer-program/overview/ (accessed 2026-08-21). Establishes the five API products and their content.
3. Garmin Connect Developer Program FAQ. https://developer.garmin.com/gc-developer-program/program-faq/ (accessed 2026-08-21). Establishes "no licensing or maintenance fees … but it is only for business use", the metric-specific license/minimum-order caveat, two-business-day application confirmation, and one-to-four-week integration.
4. TechDepot developer access guide (secondary). https://techdepot.blog/garmin-api-access-guide (accessed 2026-08-21; returned 403 on 2026-10-10). Source of the reported $5,000 administrative fee and the Companion SDK accelerometer livestream claim. **Unsupported**; the fee is contradicted by source 17 and the FAQ.
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
17. Garmin Connect Developer Program Agreement, Garmin International version (FRM-0952 Rev. B). https://developerportal.garmin.com/sites/default/files/Garmin%20Connect%20Developer%20Program%20Agreement.pdf (accessed 2026-10-10). **Primary.** Section 10.1 no fees and fee reservations; 8.4 public statements; Garmin as independent controller; EU SCCs module one; retention period in the SCC annex; no AI clause.
18. Garmin Connect Developer Program Agreement, Garmin China Shanghai RHQ version. https://www8.garmin.com/en-US/GARMINCONNECTDEVELOPERPROGRAMAGREEMENT/GARMINCONNECTDEVELOPERPROGRAMAGREEMENT_EN.pdf (accessed 2026-10-10). **Primary.** Section 10.1 identical; 6.4(a) research exemption from attribution; 15.10 AI transparency and consent; PIPL annex.
19. Garmin Developer API Brand Guidelines. https://developer.garmin.com/downloads/brand/Garmin-Developer-API-Brand-Guidelines.pdf (accessed 2026-10-10). **Primary.** Attribution required when Garmin data feeds analytics, ML or AI.
20. Garmin newsroom, Garmin Health research solutions (2022). https://www.garmin.com/en-US/newsroom/?p=3942 (accessed 2026-10-10). **Primary.** High-resolution data by definable interval logging, independent hosting, device control.
21. Garmin newsroom, Garmin Health x Fitrockr Asia Research Grant 2026. https://www.garmin.com/en-PH/newsroom/press-release/news-2026-mar-fitrockr/ (accessed 2026-10-10). **Primary.** Launched by Garmin Health on 2 February 2026; eligibility; closing date 31 March 2026.
22. Garmin newsroom, King's College London EMBRACE (17 September 2025). https://www.garmin.com/en-US/newsroom/?p=5892 (accessed 2026-10-10). **Primary.** Up to 40,000 participants; Garmin's largest research-institution collaboration.
23. Garmin newsroom, Garmin Connect+ launch (March 2025). https://www.garmin.com/en-US/newsroom/?p=5556 (accessed 2026-10-10). **Primary.** $6.99/month or $69.99/year after a 30-day trial; existing features stay free.
24. FDA 510(k) K221774, Garmin ECG App. https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K221774 (read via https://api.fda.gov/device/510k.json?search=k_number:K221774, 2026-10-10). **Regulator.**
25. FDA 510(k) K221486, Index BPM. https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K221486 (read via openFDA, 2026-10-10). **Regulator.** Applicant Ya Horng Electronic Co., Ltd.
26. the5krunner, "Garmin developer API access paused", 14 September 2026. https://the5krunner.com/2026/09/14/garmin-developer-api-access-paused/ (accessed 2026-10-10). Secondary. Queued requests on hold; programme redesign.
27. Garmin developer forum, "Developer onboarding blocked". https://forums.garmin.com/developer/fit-sdk/f/discussion/435484/developer-onboarding-blocked/2054626 (accessed 2026-10-10). Forum post quoting a Garmin reply on the pause, with no timeline.
28. Garmin Health SDK Q&A. https://developer.garmin.com/health-sdk/questions-answers/ (accessed 2026-10-10). **Primary.** Evaluation free; licence fee or device MOQ; terms designed per customer; SDK updates needed for new data types.
29. Garmin newsroom device releases (accessed 2026-10-10). **Primary.** vívosmart 5: https://www.garmin.com/en-US/newsroom/press-release/featured/simple-and-streamlined-garmin-vivosmart-5-fitness-tracker-is-the-effortless-way-to-take-charge-of-your-everyday-health-wellness-and-activity/ ; CIRQA Smart Band: https://www.garmin.com/en-US/newsroom/press-release/wearables-health/meet-cirqa-smart-band-the-screen-free-health-and-fitness-tracker-from-garmin/ ; Forerunner 70 and 170: https://www.garmin.com/en-US/newsroom/press-release/sports-fitness/run-further-with-forerunner-70-and-forerunner-170-from-garmin/
30. Fitabase, Garmin datasets. https://fitabase.com/resources/knowledge-base/learn-about-garmin-data/garmin-datasets/ (accessed 2026-10-10). Secondary. 15-minute epochs; stress every 3 minutes.
31. Fitrockr, accelerometer and gyroscope; Avicenna forum, Garmin SDK. https://www.fitrockr.com/accelerometer-gyroscope/ ; https://forum.avicennaresearch.com/t/garmin-sdk/1261 (accessed 2026-10-10). Secondary. Fixed 25 Hz accelerometer logging.
32. Connect IQ Sensor API. https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor.html (accessed 2026-10-10). **Primary.** Device-reported maximum sample rate.
33. Open Wearables, Garmin API integration. https://openwearables.io/docs/providers/garmin-api-integration (accessed 2026-10-10). Secondary. Legal-entity applicants; backfill about the last month.
34. Fitrockr, how to obtain wearable data for research. https://www.fitrockr.com/help-center/how-to-obtain-wearable-data-for-research-or-healthcare/ (accessed 2026-10-10). Secondary. SDK licence cost described as high.
35. Paubox, "Is Garmin Connect HIPAA compliant". https://www.paubox.com/blog/is-garmin-connect-hipaa-compliant-2025-update (accessed 2026-10-10). Secondary. BAA claim with no traceable evidence.
36. Garmin FY2025 10-K cybersecurity section (tracker mirror). https://www.board-cybersecurity.com/annual-reports/tracker/20260218-garmin-cybersecurity-10k (accessed 2026-10-10). NIST CSF alignment; no certification named.
37. Garmin Connect privacy policy. https://www.garmin.com/en-US/privacy/connect/policy/ (read by hand 2026-10-10). Storage locations; script-rendered, not quote-checked.
38. Garth documentation. https://garth.readthedocs.io/en/latest/ (accessed 2026-10-10). Deprecated after Garmin's auth change.
