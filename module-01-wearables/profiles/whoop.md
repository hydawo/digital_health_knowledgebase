# WHOOP

## Quick Facts

| Field | Details |
|---|---|
| Organization | WHOOP, Inc. (US) |
| Category | Subscription-first screenless wearable focused on strain, recovery, and sleep |
| Current status | Active |
| Platforms/devices | WHOOP band (4.0, WHOOP 5.0/MG generation); worn on wrist or via WHOOP Body apparel; iOS and Android |
| Open source | No |
| Hosting/deployment | Vendor cloud; REST API v2 |
| Pricing model | **Subscription-only**, the hardware is bundled into a recurring membership |
| Last verified | 2026-10-11 (vendor fact record); API terms, member tiers, scopes and FDA status re-verified 2026-10-10; first pass 2026-08-21 |

## Summary

- WHOOP is architecturally the most closed of the major consumer platforms. It is screenless (so it cannot display anything to a participant, which is either a reactivity advantage or a feedback limitation depending on the design), and its business model is a **subscription that includes the hardware**, you do not buy a WHOOP, you rent access to one.

- For research the defining characteristic is that the **API returns only WHOOP's proprietary aggregated scores and summaries. There is no raw heart rate time series and no inter-beat-interval data through the documented endpoints.** A recovery score, an RMSSD value for the night, a strain figure, a sleep stage summary, these are the unit of analysis. A researcher who wants the underlying physiology cannot get it through the API. In 2023 WHOOP supplied research partners on its WHOOP Unite route with raw CSV or Excel files ending in RR intervals; whether that route exists today is **Unclear** (vendor fact record, `raw_streams`, `program_status`; sources 24, 26).

- Against that, WHOOP had the best deep-sleep classification accuracy of six wrist devices in the strongest recent *independent* sleep-staging validation (Schyvens 2025), though it was fourth of six on overall agreement (κ 0.37); see Research Evidence. Corrected 2026-10-10 to match the table below.

## Products / Platform Architecture

- **WHOOP band**, screenless, worn continuously (24/7 is the intended use, including during sleep and exercise). Battery pack slides onto the band so the device can be charged **without removing it**, a genuinely distinctive feature that eliminates the charging gap that affects every other wrist wearable.
- **WHOOP app** (iOS/Android), the entire user interface.
- **WHOOP Developer Platform**, REST API v2, OAuth 2.0, webhooks.
- WHOOP has a clinical research function internally (it recruits for roles such as Lead Clinical Research Scientist) and has run partnerships with clinical institutions, but a published, self-serve research programme with defined terms is **not established**.
- **Research program and academic data access (checked 2026-10-10, vendor fact record 2026-10-11).**
  - **No named, self-serve research program.** WHOOP runs research through partnerships it approves. Its research page says it works with "academic and industry partners" and states no eligibility criteria, fees or data terms (read in a browser 2026-10-10); its CONTACT US button leads to a WHOOP "Research Request Intake" form. The privacy policy says WHOOP uses de-identified member data with research partners, and a 2026 Stanford paper in *npj Digital Medicine* analysed WHOOP-held member data available only "with permission of WHOOP, Inc." **Corroborated** (`research_program`; sources 18 to 21). Eligibility criteria are **Unclear** (`program_eligibility`).
  - **Application.** No published application or review process. Requests go through the intake form; a 2026 *Clinical and Translational Science* tutorial reports that WHOOP requires an institutional legal review, possibly tied to a minimum device order, before API access. The 2023 Unite FAQ pointed to healthcare@whoop.com. **Reported** (`program_application`; sources 18, 24, 27).
  - **Digital WHOOP Labs** is an in-app feature for members to join WHOOP's own studies, not a route for outside teams. Regional partnerships exist (a WHOOP and Mubadala Health Research Initiative with UAE institutions, May 2026). **Reported** (sources 22, 23).
  - **WHOOP Unite**, status **Unclear**. Unite was WHOOP's enterprise route and offered study-site support in 2022 to 2023; it was used in a research partnership with Ashley Addiction Treatment, announced November 2022, with the phone-free **WHOOP Gateway** Bluetooth hub (Business Wire, read via search results only). whoopunite.com now redirects to www.whoop.com (HTTP 301, 2026-10-10), Athletech News reported 22 Unite layoffs in January 2023, and no closure announcement was found. Treat the Unite raw-data route as unconfirmed and ask WHOOP through the intake form (`program_status`; sources 16, 25, 26).
  - **What an academic team actually gets through the API:** WHOOP's derived scores and summaries only (see Derived Metrics), for up to 10 members on the default Sandbox tier, more only through manually reviewed tier upgrades (see Data Access and Export). The API terms bar permanent copies of WHOOP data and any use of it to train or test machine-learning or AI models, unless authorised by the data owner or by law. No separate academic tier, raw-data route or research carve-out is documented. **Verified** (developer.whoop.com, 2026-10-10).
  - WHOOP also documents a server-to-server "Healthcare Partner Integration" API (service requests and lab requisitions). WHOOP says it is available only to WHOOP-approved healthcare partners and not to general developers; it covers lab requisition workflows, not member wearable data. **Verified** (`export_routes`, `developer_program_status`; source 33).

## Sensors and Data Streams

- Every Module 1 profile uses the same table so devices can be compared row by row. Rows are the sensors named in `CLAUDE.md`. "Present" is about the hardware; "Researcher access" is about what a study can actually obtain, which is the module's central question. "Unclear" means nothing current was verified. The convention is recorded in [`../../shared/profile-table-conventions.md`](../../shared/profile-table-conventions.md).

| Sensor | Present | Researcher access to underlying signal | Resolution or sampling | Notes |
|---|---|---|---|---|
| PPG | Yes, multi-wavelength | No raw PPG, no raw HR time series, no IBI or RR series via the API. Session and period aggregates only. Live HR can be broadcast over standard BLE. | Aggregates via API; HR sampled at 52 Hz on the device (2023 WHOOP FAQ, Reported) | Unite research files (2023) had 1-second rows ending in RR intervals; current availability Unclear (sources 24, 36). |
| ECG | WHOOP MG generation, reported | Not documented as available via the API | Unclear |  |
| Accelerometer | Yes | Not exposed. No raw accelerometry and no step time series in the documented API. One `step_count` total per cycle since 2026-09-23. | Not exposed; sampled at 52 Hz on the device (2023 WHOOP FAQ, Reported) | Step count added in the API changelog of 2026-09-23 (source 32). |
| Gyroscope | Unclear | Not exposed | Unclear |  |
| Magnetometer | Unclear | Not exposed | Unclear |  |
| Temperature | 4.0 and later | `skin_temp_celsius` within the recovery score object only | Per recovery period |  |
| SpO2 | 4.0 and later | `spo2_percentage` within the recovery score object only | Per recovery period |  |
| GPS | No | Not applicable | Not applicable | No onboard GPS. |
| Barometer / altimeter | Unclear | Unclear | Unclear |  |
| EDA | No | Not applicable | Not applicable |  |
| Ambient light | No | Not applicable | Not applicable |  |
| Other | Unclear | Unclear | Unclear | Not verified against current documentation. |

**Verification.** From WHOOP's developer API documentation as recorded in the Module 1 passes; see the notes below.

### Notes from earlier verification passes

| Sensor | Present | Researcher access to underlying signal |
|---|---|---|
| PPG (multi-wavelength) | Yes | **No raw PPG, no raw HR time series, no IBI/RR series via the API.** Only session/period aggregates. |
| Accelerometer | Yes | **Not exposed.** No raw accelerometry, no step time series in the documented API. |
| Skin temperature | Yes (4.0+) | Exposed only as `skin_temp_celsius` within the recovery score object. |
| SpO2 (pulse oximetry) | Yes (4.0+) | Exposed only as `spo2_percentage` within the recovery score object. |
| ECG | WHOOP MG generation (reported) | Not documented as available via the API. |
| GPS | **No** | n/a, no onboard GPS. |
| EDA | No | n/a |

## Derived Metrics / Analytics

- WHOOP API v2 endpoints and their returned score fields:

| Endpoint | Key returned fields |
|---|---|
| `GET /v2/cycle`, `GET /v2/cycle/{cycleId}` | id, user_id, timestamps, timezone_offset, score_state; score: `strain`, `kilojoule`, `average_heart_rate`, `max_heart_rate`; `step_count` (one total per cycle, null when no step data exists; added 2026-09-23, covered by `read:cycles`) |
| `GET /v2/recovery`, `GET /v2/cycle/{cycleId}/recovery` | cycle_id, sleep_id, user_id, timestamps, score_state; score: `recovery_score`, `resting_heart_rate`, `hrv_rmssd_milli`, `spo2_percentage`, `skin_temp_celsius` |
| `GET /v2/activity/sleep`, `GET /v2/activity/sleep/{sleepId}` | id, cycle_id, user_id, timestamps, nap flag, score_state; score: `stage_summary`, `sleep_needed` breakdown, `respiratory_rate`, `sleep_performance_percentage`, `sleep_consistency_percentage`, `sleep_efficiency_percentage` |
| `GET /v2/activity/workout`, `GET /v2/activity/workout/{workoutId}` | id, user_id, sport, timestamps, score_state; score: `strain`, `average_heart_rate`, `max_heart_rate`, `kilojoule`, `distance_meter`, altitude metrics, `zone_durations` |
| `GET /v2/user/measurement/body` | `height_meter`, `weight_kilogram`, `max_heart_rate` |
| `GET /v2/user/profile/basic` | user_id, email, first_name, last_name |

- OAuth scopes (six member-data scopes): `read:recovery`, `read:cycles`, `read:workout`, `read:sleep`, `read:profile`, `read:body_measurement`.

- Features sold in Peak and Life (Healthspan, Stress Monitor, ECG, Blood Pressure Insights) and the Journal have no API scope. The API returns one record per cycle, sleep, recovery or workout, with no intraday time series. **Verified** (`derived_metrics`, `sampling_rates`; sources 13, 36). WHOOP's 2023 research FAQ says sleep is staged in 30-second epochs on the device. **Reported** (source 24).

- Two things stand out. **`hrv_rmssd_milli` is a genuinely useful, well-defined field**, a nightly RMSSD in milliseconds, measured during slow-wave sleep, which is a more methodologically defensible HRV quantity than several competitors expose. And the **"cycle"** concept is WHOOP-specific: WHOOP organises the day around sleep-to-sleep physiological cycles rather than calendar days, which is arguably better aligned to circadian reality but requires care when merging with calendar-day data from other sources.

- `score_state` is important operationally, it signals whether a score is `SCORED`, `PENDING_SCORE`, or `UNSCORABLE`. Studies must handle unscorable periods explicitly rather than treating them as missing at random.

## Active Data Collection

- The WHOOP app includes a Journal feature where members log daily behaviours (alcohol, caffeine, sleep environment, etc.), which WHOOP correlates against recovery. **Journal data has no v2 API scope or endpoint**, so a study cannot pull it through the API, a notable loss, since it is the closest thing WHOOP has to structured self-report. WHOOP's June 2026 data-export article says the member CSV export includes "individual Journal entries", so each participant could export and forward their own. **Reported** (`export_routes`, member self-export; source 31, read from an Internet Archive capture of 2026-06-17).

- No survey/EMA scheduling, no branching logic, no notifications a researcher can control.

## Researcher and Study Management Features

- None documented in the public developer platform. No study console, no participant roster, no adherence dashboard, no bulk provisioning path. A study must build its own OAuth enrolment flow and monitor adherence by inspecting returned data.
- Outside the public platform, a 2026 tutorial reports that WHOOP provides a web application, for an additional fee, to view and download data for groups of individuals. WHOOP's 2023 Unite FAQ describes a blinded mode in which participants see only device metrics such as battery, and memberships that could be moved between participants. Current terms are not published. **Reported** (`export_routes`, research partnerships; sources 24, 27).

- **App approval is required** before an integration launches, WHOOP documents design guidelines and an app approval process. This is an additional gate and timeline item.
- **Member tiers (re-verified 2026-10-10).** "Every new app starts on the Sandbox tier, which allows up to 10 WHOOP members to connect." Tiers are Sandbox 10, Build 100, Growth 1,000, Scale 5,000 and Production unlimited. "Tiers are earned one at a time": an app can request only the next tier, and from Build onward "moving up requires at least 50% of your current tier's member limit to be connected" (so a Build app needs 50 connected members before it can request Growth). Requests "are reviewed manually", and requests without specific, detailed answers are rejected. **Verified** (developer.whoop.com/docs/developing/app-approval). For a study, this means a 300-person cohort cannot be authorised in one step: the app must pass Build (100) and reach 500 connected members on Growth before Scale is open, so tier requests have to be planned into the enrolment timeline.
- **Tier upgrade turnaround.** Developers on WHOOP's forum reported waits of two to more than three months for upgrades above Sandbox in June to August 2026; in one thread WHOOP staff escalated cases and some apps were then approved within days. These are user posts, not WHOOP policy. Build slack into the study timeline. **Reported** (`developer_program_status`; source 28).

## Data Access and Export

- **API v2**, OAuth 2.0, REST, JSON. Webhooks supported (v1 webhooks have been removed; v2 ids differ from v1 and a mapping lookup is documented).
- **Rate limits:** default **100 requests per minute and 10,000 requests per day per client**. Response headers carry `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`. WHOOP states it can increase limits on request with justification.
  - The daily cap is the binding constraint at scale: 10,000 requests/day across all users of the application. A 500-participant study pulling several endpoints daily with pagination will approach this. **Request a limit increase before enrolling, not after.**
- **Historical depth:** the collection endpoints document no lower bound on start time ("If not specified, the response will not filter cycles by a minimum time"), which implies but does not state that a newly authorised member's full history comes back. Collections page at up to 25 records per request. **Corroborated** (`history_depth`; source 13).
- **Participant self-export:** members can request a CSV for a chosen date range or their entire account history, delivered by emailed link, generation taking up to 24 hours. It holds daily scores, resting HR, HRV, respiratory rate, sleep architecture and Journal entries; MG members on Life get additional data. A member reports it holds per-stage totals, not intraday data. Each participant would have to run and forward their own export, so it is not a researcher-side bulk route. **Reported** (`export_routes`, `history_depth`; source 31, Internet Archive capture of 2026-06-17, live page 403 to scripts).
- **Research partnerships:** partners have received data outside the public API, as raw CSV or Excel files (2023 Unite FAQ, with API extraction "at an additional cost") and, per a 2026 tutorial, through a paid group-download web application. Current terms are not published. **Reported** (sources 24, 27).
- **Terms restrictions** (WHOOP API Terms of Use, effective 6 October 2026, read in full 2026-10-10, **Verified**):
  - The developer may not "build databases, or otherwise create permanent copies of WHOOP Data, or keep cached copies longer than permitted by the cache header" (§4.2).
  - The developer may not "Use any API or WHOOP Data to create, develop, test, train, fine-tune or improve any large language model or any other machine learning or artificial intelligence model, application, or system" (§4.2).
  - Both §4.2 bans open with "Unless expressly authorized by the WHOOP Data owner or by applicable law". The terms do not say whether the participant who connects their account counts as the "WHOOP Data owner", so whether participant consent lifts these bans is a legal question. **Unclear.**
  - The developer may not copy, sell, distribute or sublicense WHOOP Data to any third party (§4.2), and may not market, sell, license or lease API data to a third party "even if an End User consents to such use" (§3.1).
  - The developer may not use the APIs "to design, develop, augment, or support a medical device" (§3.1).
  - HIPAA (§1.8): "Unless otherwise agreed in writing by WHOOP", WHOOP makes no HIPAA representations, and a covered entity or business associate may not transmit Protected Health Information through the APIs without WHOOP's prior written consent.
  - WHOOP may limit "the number of API requests that Company may make, or the number of users Company may serve" (§1.5); use beyond those limits needs WHOOP's prior written consent and may carry additional terms or charges.
  - API access "is currently provided at no charge" (§1.12).
  - On termination the developer must delete any cached or stored content (§7).
  - Further prohibitions cover reverse-engineering WHOOP algorithms, processing export-controlled data, altering WHOOP terms, competing with WHOOP, and disparaging WHOOP.
  - Section numbers are counted from the order of clauses on the page, which does not print them.
  - **This matters directly for open science and for analysis.** Read literally, a study cannot keep a permanent analysis dataset of WHOOP data, cannot train a machine-learning model on it, and cannot deposit it or share it with collaborating institutions, unless the "data owner" or "applicable law" exception applies or WHOOP agrees in writing. No research carve-out exists. **Resolve this with WHOOP (apisupport@whoop.com is the contact the terms give for limit requests) and with institutional counsel before a study commits**, particularly for funders with open-data mandates.

## APIs, SDKs, and Extensibility

- REST v2 + OAuth 2.0 + webhooks. No device SDK; the band is not programmable.
- Live heart rate can be broadcast from the band over standard Bluetooth Low Energy to other devices (source 36).
- No raw-data route in the public API. The only documented raw route was the Unite research file delivery of 2023, whose current availability is **Unclear** (see Data Access and Export).

## Deployment and Infrastructure

- Vendor cloud only. No self-hosting, no on-premises option.

## Participant Experience

- **Best-in-class continuous wear.** Screenless, light, and, critically, chargeable *on the wrist* via a slide-on battery pack. Alone among wrist wearables, WHOOP has no structural charging gap, which is why its 24/7 data completeness can exceed Apple Watch and Fitbit in practice.
- Can be worn as a band or in WHOOP Body apparel (bicep sleeves, etc.), useful where wrist wear is impractical.
- Screenless means **no participant-facing feedback on the device**, this reduces reactivity (the participant is not glancing at step counts and changing behaviour), which is scientifically attractive for observational designs. It also means the device cannot be used as an intervention delivery mechanism.
- Battery life of 14+ days for WHOOP 5.0 and MG, per WHOOP's membership page (Internet Archive capture of 2026-10-02). **Reported** (source 29).
- Requires the app for any feedback and for syncing.
- iOS and Android.
- The subscription model means a participant who drops out or whose membership lapses takes the hardware access with them, device recovery and membership management are study logistics.

## Privacy, Security, and Compliance

- **HIPAA (re-verified 2026-10-10, vendor fact record 2026-10-11):** the API Terms say that "Unless otherwise agreed in writing by WHOOP", WHOOP makes no representation that the APIs meet HIPAA requirements, and bar use of the APIs to transmit PHI without WHOOP's prior written consent. No BAA is offered publicly. **Verified** (terms text, `baa`, `hipaa_statement`; source 5). The privacy policy says processing done on behalf of a covered entity follows that entity's Notice of Privacy Practices (source 20). WHOOP's 2023 Unite FAQ said WHOOP is not a HIPAA covered entity and that studies could be structured so that a BAA is unnecessary. **Reported** (source 24).
- **GDPR and DPA.** The privacy policy has a notice for European residents, names WHOOP, Inc. as controller, Whoop Limited (Dublin) as EU representative, and a UK representative. No customer DPA is published; the policy says WHOOP will sign Standard Contractual Clauses with customers on request. **Reported** (`gdpr_statement`, `dpa`; source 20, Internet Archive capture of 2026-08-06, policy dated August 3, 2026).
- **Data residency.** Personal data is processed in the United States; the 2023 FAQ says it is stored in AWS West. No residency options published. **Reported** (`data_residency`; sources 20, 24).
- **SOC 2 and ISO 27001.** The only SOC 2 claim found is in a 2022 WHOOP study-onboarding deck, which also claims Privacy Shield (invalid since 2020); no current report, trust page or attestation was found. No ISO 27001 claim was found and trust.whoop.com does not resolve (`soc2`, `iso27001`, both Reported; source 25). Ask WHOOP for a current SOC 2 report under NDA.
- **Deletion.** Members can request deletion through privacy.whoop.com, and WHOOP may keep de-identified or aggregated data. The API terms require a developer to delete stored content when the terms end (`retention_terms`; sources 5, 20).
- Given the restrictive data-transfer terms noted above, the compliance and data-governance conversation with WHOOP is a prerequisite, not a formality.
- **FDA status (re-verified 2026-10-10 in FDA databases):** see Research Evidence and Validation. The ECG feature is 510(k)-cleared; Blood Pressure Insights is not cleared.

## Pricing

- **Subscription includes hardware.** There is no separate device price; each membership includes the band (WHOOP 5.0 on One and Peak, WHOOP MG on Life). US prices on WHOOP's membership page: One $199/yr, Peak $239/yr, Life $359/yr, roughly $16.58 to $29.92 a month. **Verified** (read in a browser 2026-10-10; `subscription_price`, `device_price`; source 29). Canadian prices, from a capture of the same page on 2026-10-02: One CA$259/yr, Peak CA$349/yr, Life CA$529/yr.
- **Term.** The vendor page shows only per-year prices and states no membership term. A third party reports monthly billing only for existing members, still with a 12-month commitment. **Reported** (`minimum_commitment`; source 30).
- **This is the most expensive per-participant recurring cost in this module**, roughly 3 to 5× Oura's membership and far above Garmin's zero. For a 100-person 12-month study, WHOOP membership alone is on the order of $20,000, $36,000.
- **No published academic or research pricing** (`academic_pricing`, not public, 2026-10-10). WHOOP's bulk-buy page offers volume pricing to any buyer, up to 11% off Peak and 14% off Life and none on One (browser read, 2026-10-10; source 35). Research partnership fees are not published either; the 2023 Unite FAQ priced API extraction separately, a 2026 tutorial reports a paid group-download web application, and the same tutorial reports API access may be conditioned on a minimum device order. Expect a quote through the research intake form. **Reported** (`api_platform_fees`, `minimum_commitment`, `quote_required`; sources 18, 24, 27).
- No API fee: the API Terms state access "is currently provided at no charge", with prior notice promised if that changes. **Verified** (2026-10-10).

## Research Evidence and Validation

- **This section was materially wrong in the first draft of this knowledge base and has been corrected after reading Schyvens et al. 2025 in full.** See `../validation-evidence.md`.

- **Schyvens et al., *SLEEP Advances* 2025**, N=62, six devices vs PSG, independently funded (VLAIO), no author conflicts:

| Metric | Whoop 4.0 | Rank of 6 |
|---|---|---|
| **Cohen's kappa (overall agreement)** | **0.37, "fair"** | **4th of 6** |
| Sleep/wake sensitivity | 93.58% | 5th |
| Sleep/wake specificity | 40.13% | 4th |
| Wake accuracy | 40.13% | 4th |
| Light sleep accuracy | 61.99% | 4th |
| **Deep sleep accuracy** | **69.63%** | **1st** |
| REM accuracy | 61.99% | 3rd |
| TST bias | **+24.46 min (p=0.010)** | |
| SE bias | +4.10% (p=0.006) | |
| WASO bias | −19.15 min (p=0.007) | |
| SOL bias | **−10.95 min (p=0.006)** | |

- **The correct reading.** WHOOP had the best *deep-sleep classification accuracy* of the six devices tested, and the second-worst *overall* agreement, behind Apple Watch (κ=0.53) and both Fitbits (0.42, 0.41). Those two facts are compatible: a device that over-assigns deep sleep will catch most true deep epochs while misclassifying a great deal else. **Quoting WHOOP's 69.6% deep-sleep number without its κ=0.37 is misleading.**

- WHOOP also significantly overestimated total sleep time (+24 min), overestimated sleep efficiency, underestimated WASO by 19 minutes, and was one of only two devices with a significant sleep-onset latency bias.

- ~~No independent study has ever compared WHOOP and Oura under the same protocol.~~ **Corrected 2026-10-09.** Two PSG studies placed both under one protocol, on older hardware, and Dial et al. 2025 compared them for resting HR and HRV:

| Study | Hardware | Result | Funding / COI | Confidence |
|---|---|---|---|---|
| Miller DJ, Sargent C, Roach GD 2022, *Sensors* 22(16):6317, N=53, single night PSG + ECG | WHOOP 3.0 vs Oura Gen2 (plus Apple Watch S6, Garmin FR245, Polar Vantage V, Somfit) | Four-stage κ WHOOP 0.44 vs Oura 0.43 (tied); two-state κ 0.44 vs 0.51; WHOOP TST bias −12.2 min, Oura +1.5 min; WHOOP HR ICC 0.99, HRV ICC 0.99 vs ECG | Australian Institute of Sport funded it; the authors' CQU Sleep Lab "receives support for research (i.e., funding, equipment) from WHOOP Inc."; WHOOP staff, blinded to PSG, supplied WHOOP's sleep epochs and R-R intervals | **Verified** (full text read). Tier B for WHOOP |
| Grandner MA et al. 2023, *Sleep* 46(1):zsac152, in-lab PSG night (WHOOP n=33, Oura n=30) | WHOOP 3.0 vs Oura V2 (plus Happy Ring, Fitbit Charge 4, Actiwatch 2) | Sleep/wake accuracy WHOOP 0.86 vs Oura 0.88; specificity 0.54 vs 0.49 | 5 of 7 authors affiliated with Happy Health, the competing ring's maker (PubMed affiliations); NIH grant R01 MD011600 listed | **Reported.** Corrected 2026-10-10: the full text has never been read (PDF not obtained, PMC and OUP bot checks; not in Europe PMC's open-access set), and the abstract gives Happy Ring figures only, so the WHOOP and Oura figures cannot be checked against a source on record |
| Dial MB et al. 2025, *Physiol Rep* 13:e70527, 536 nights, Polar H10 reference | WHOOP 4.0 vs Oura Gen3/Gen4 | Resting HR and HRV: Oura ahead of WHOOP (see `../validation-evidence.md` §3a) | AFRL, no competing interests | **Verified** |

- Read together: on PSG four-stage staging the only direct comparison (Miller 2022) shows WHOOP 3.0 and Oura Gen2 tied (0.44 vs 0.43), which does not support the bridged estimate's "Oura meaningfully ahead" for that generation. It is not a clean head-to-head either: Oura led on two-state sleep/wake kappa (0.51 vs 0.44), WHOOP's 30-second epochs were supplied by WHOOP staff while Oura's were exported from the app at 5-minute precision, and the authors state the analyses "were comparisons of six independent devices to gold-standard PSG and ECG rather than a comparison between devices" (re-read in the stored PDF, 2026-10-10). No PSG study compares WHOOP 4.0 or later with Oura Gen3 or later; the bridged estimate in `../validation-evidence.md` §3b is still the only (indirect) evidence for current hardware.

- **No WHOOP 5.0/MG validation of any kind was located.** Searched 2026-10-09: PubMed `whoop[tiab] AND ("5.0" OR "WHOOP MG" OR "Whoop 5")` (3 hits, none a validation) and Europe PMC full text including preprints (`"WHOOP 5.0" OR "WHOOP MG"`, no validation study). Every located independent result is on WHOOP 2.0 to 4.0. Whether 5.0 performs differently is **Unclear**.

- The CQU author cluster's WHOOP ties are now documented paper by paper (rechecked 2026-10-09; Biosensors 2021 added 2026-10-10): Miller et al. 2021 (*Biosensors* 11(6):185) states that Dean Miller's CQUniversity position "is currently sponsored by WHOOP Inc", that this "was initiated after the data were collected", and that it "represents a potential conflict of interest" for Miller and for Roach, Sargent and Lastella; funding was ARC DP160104909 and the Australian Institute of Sport (Europe PMC full text of PMC8226553, **Verified**). Bellenger et al. 2022 (*Sensors* 22:6723, water polo HRV) was funded by the Australian Institute of Sport, and its COI statement discloses that the CQU Sleep Lab receives WHOOP funding and equipment, so it is **Tier B, Verified**. Miller et al. 2020 (*J Sports Sci*, PSG validation) lists the Australian Research Council (DP160104909) and the Australian Institute of Sport as funders in Crossref metadata, and its abstract says WHOOP scored the sleeps with its proprietary algorithm; its COI statement could not be read (publisher bot check). **Likely Tier B, COI Unclear.**

- **SpO2 and skin temperature:** no independent validation against a reference instrument located (PubMed and Europe PMC rechecked 2026-10-09). **Still open.**

- Further caveats: the Schyvens device was **WHOOP 4.0**, not the current 5.0/MG generation. WHOOP has an active internal research programme and publishes vendor-authored validation, which should be weighted as **Reported**.
- **Regulatory status, corrected 2026-10-10.** The earlier text said both MG features carry clearances "per WHOOP's claims"; that was wrong for blood pressure.
  - **ECG:** FDA 510(k) **K243236**, "WHOOP ECG (electrocardiogram) Feature (1.0)", decision 2025-04-04 (substantially equivalent), product code QDA. It is the only WHOOP 510(k) in openFDA. **Verified** (openFDA).
  - **Blood Pressure Insights (BPI): not cleared.** FDA Warning Letter CMS #709755 (14 July 2025) states WHOOP "is marketing Blood Pressure Insights ... in the United States without marketing clearance or approval" and that BPI falls outside the general-wellness policy. A close-out letter dated 17 June 2026 says that, after WHOOP's changes to BPI and its labelling, "FDA does not intend to enforce the device statutory and regulatory requirements for your BPI product as modified", and that the letter is specific to BPI as modified. So BPI is now marketed as a general-wellness feature under enforcement discretion, not as a cleared device. **Verified** (FDA letters, read 2026-10-10).
  - **Irregular Heart Rhythm Notifications (IHRN):** listed on the Life membership but not available in the US. A WHOOP staff account cited regulatory restrictions (May 2025), the membership page footnote says IHRN is not available in every region, and openFDA has no 510(k) for it. **Reported** (`fda_clearances`; sources 29, 34).

## Strengths

- **No charging gap**, the only wrist wearable here that can be charged while worn, giving the best structural 24/7 completeness.
- Best deep-sleep classification accuracy (69.6%) in the strongest recent comparison (Schyvens 2025), though fourth of six on overall four-stage agreement (κ 0.37); and tied with Oura on four-stage κ in the only head-to-head PSG study (Miller 2022, CQU lab with WHOOP support). Corrected 2026-10-09.
- Screenless design minimises measurement reactivity, genuinely useful for observational research.
- Well-defined nocturnal RMSSD field.
- Clean, small, easily consumed REST API with webhooks; simple to integrate.
- Alternative wear positions via WHOOP Body apparel.
- iOS and Android.

## Limitations

- **No raw data through the API.** No HR time series, no IBI/RR, no accelerometry, no PPG. The API exposes only WHOOP's own scores and summaries. This is the most restrictive public data model of any platform in this module. A Unite research raw-file route existed in 2023; its current status is **Unclear**.
- **Highest recurring per-participant cost** by a wide margin.
- **Restrictive API terms** (effective 6 October 2026): no permanent copies of WHOOP data, no ML or AI model training on it, no transfer to third parties, each unless authorised by the data owner or by law; no research carve-out. A potential conflict with open-data and data-sharing mandates and with any analysis that trains a model.
- **Member tiers cap a new app at 10 members** and require stepwise, manually reviewed upgrades (Build 100, Growth 1,000, Scale 5,000); developers reported waits of two to over three months in mid-2026 (Reported).
- Proprietary black-box composites (Strain, Recovery) with no published algorithms and no researcher control over version changes.
- No GPS, no step time series (only one `step_count` total per cycle, since 2026-09-23).
- Journal (self-report) data is not exportable through the API: the v2 OAuth scopes are exactly `read:body_measurement`, `read:cycles`, `read:profile`, `read:recovery`, `read:sleep` and `read:workout`, with no Journal scope or endpoint (**Verified**, developer.whoop.com/api, 2026-10-10). The member CSV export includes Journal entries, but only participant by participant (Reported).
- Default rate limits are low (10,000 requests/day per client) and require proactive negotiation at cohort scale.
- No study management tooling in the public platform (a paid group-download web application is reported for research partners); app approval adds a gate.
- Thinner academic literature than Fitbit.
- Compliance posture thinly documented: HIPAA explicitly disclaimed for the APIs, no public BAA or DPA, SOC 2 claimed only in a 2022 deck, no ISO 27001 claim found.

## Best-Fit Use Cases

- Studies where **continuous 24/7 wear and sleep-data completeness** are the binding constraint and the budget can absorb the subscription.
- Sleep timing/duration and sleep-continuity outcomes where the independent validation result is decisive.
- Observational designs where minimising participant reactivity to feedback is scientifically important.
- Recovery/autonomic research using nightly RMSSD, provided the vendor-derived nature of the value is acknowledged.
- Athletic, military, and occupational performance research, WHOOP's established user base.

## Poor-Fit Use Cases

- Any study needing raw or high-resolution physiological signals.
- Studies with open-data or data-deposition requirements, until the terms question is resolved.
- Studies that plan to train or validate a machine-learning model on WHOOP data, without WHOOP's written agreement.
- Large cohorts on a tight budget.
- Location, mobility, or intraday step endpoints (the API gives one step total per cycle).
- Studies needing participant-facing device feedback as part of an intervention.
- Studies requiring transparent, publishable metric definitions for primary endpoints.

## Open Questions

- *(Directed to WHOOP: developer support via https://developer.whoop.com/docs/developing/support/ , and WHOOP business/partnerships.)*

- **Do WHOOP's API Terms of Use permit depositing derived data in public research repositories or sharing it with collaborating institutions?** This is the single most important question for any funded academic study. As of the terms effective 6 October 2026, the default answer is no unless the data-owner or applicable-law exception applies (see Data Access and Export).
- What does the Research Request Intake route offer, to whom, and at what price? The research page names no eligibility criteria, fees or data terms (browser read, 2026-10-10). Is the Unite route, or its paid group-download web application, still available?
- Is any raw or higher-resolution data (HR time series, IBI) obtainable under a separate research agreement, outside the public API? WHOOP supplied raw files with RR intervals to Unite partners in 2023; nothing current says it still does.
- Is WHOOP Journal data available to a study by any route other than each participant's own CSV export?
- Does the API return a newly authorised member's full history? No lower bound on start time is documented, but full return is not stated.
- What rate-limit increases are realistically granted, and on what evidence?
- Is ECG data from the WHOOP MG generation available via API? (Re-checked 2026-10-10: the six v2 OAuth scopes have no ECG scope.)
- Does WHOOP treat the participant as the "WHOOP Data owner" who can authorise a permanent research copy under §4.2 of the API Terms? Will WHOOP agree in writing to research retention, data deposit or model training?
- Will WHOOP sign a BAA or DPA with a research customer, and can it supply a current SOC 2 report? Is any residency option offered outside the US?
- Independent validation of WHOOP HRV against ECG.
- Membership term length and renewal terms; the vendor page shows per-year prices only.

## Vendor Fact Record

<!-- facts:begin -->
*Generated from the fact record by `tools/facts/generate.py`. Edit the record, not this block.*

**Research access**

| Fact | Value |
|---|---|
| Formal research or academic program (name, what it offers) | No named, self-serve program for outside researchers. WHOOP runs research through partnerships it approves; it runs a research request intake form, says it uses de-identified member data with research partners, and academic papers have analysed WHOOP-held member data with WHOOP's permission. Digital WHOOP Labs is an in-app feature for members to join WHOOP's own studies. The WHOOP Unite enterprise route offered study-site support in 2022 to 2023 [C, 2026-10-10] |
| Who can join the research program | Unclear |
| How to apply, and any approval or review step | No published application or review process. Research requests go through WHOOP's Research Request Intake form; a 2026 tutorial reports WHOOP requires an institutional legal review, possibly tied to a minimum device order, before API access; the 2023 Unite FAQ pointed to healthcare@whoop.com [R, 2026-10-10] |
| Whether the program is active, paused, renamed or closed | Unclear |
| Whether the general developer or API program is open to new applicants | Open. Anyone with a WHOOP membership and device can create up to 5 apps in the Developer Dashboard; every new app starts on the Sandbox tier and higher tiers are requested and reviewed manually [V, 2026-10-10]<br>**Tier upgrade turnaround (developer forum reports):** Developers reported waits of two to more than three months for tier upgrades above the 10-member Sandbox in June to August 2026; in one thread WHOOP staff escalated and some apps were then approved within days [R, 2026-10-10] |
| Participant or user limits before approval or by tier | Member tiers per app: Sandbox 10, Build 100, Growth 1,000, Scale 5,000, Production unlimited. Tiers are earned one at a time with manual review, and from Build onward 50% of the current limit must be connected before requesting the next [V, 2026-10-10] |
| How academic access differs from commercial or consumer access | Not public [2026-10-10] |

**Pricing**

| Fact | Value |
|---|---|
| Device or hardware list price | No separate device price; each membership includes the hardware (WHOOP 5.0 on One and Peak, WHOOP MG on Life) [R, 2026-10-30] |
| Consumer subscription or membership price | US, vendor page: One $199/yr, Peak $239/yr, Life $359/yr. Canada, vendor page capture of 2026-10-02: One CA$259/yr, Peak CA$349/yr, Life CA$529/yr [V, 2026-10-10] |
| Research or academic pricing or discount | Not public [2026-10-10] |
| Fees for API, SDK, platform or data access | **Developer API:** No charge for the Developer Platform or API; WHOOP may start charging with prior notice. Each user needs a WHOOP membership [V, 2026-10-10]<br>**Research partnerships:** Research routes have carried extra fees. The 2023 Unite FAQ priced API extraction separately, and a 2026 tutorial reports a paid web application for viewing and downloading group data. Current fees are not published [R, 2026-10-10] |
| Minimum order, term or commitment | Consumer memberships are sold by the year; a third party reports monthly billing only for existing members, still with a 12-month commitment. A 2026 tutorial reports API access may be conditioned on a minimum device order. No research minimum is published [R, 2026-10-10] |
| Whether pricing requires contacting sales | **Developer API:** No; the API is free and self-serve [V, 2026-10-10]<br>**Research partnerships and Healthcare Partner API:** Yes in practice. No research or partner price is published; access is by WHOOP approval through the research intake form or partner agreement [R, 2026-10-10] |

**Data access and terms**

| Fact | Value |
|---|---|
| Raw signals available to researchers, and by which route | **Developer API:** None. The API returns scored summaries only; continuous heart rate is not available. The device can broadcast live heart rate over standard BLE [V, 2026-10-10]<br>**WHOOP Unite research (2023 FAQ; current availability unclear):** WHOOP supplied research partners with raw data files as CSV or Excel, each one-second row ending with RR intervals [R, 2026-10-10] |
| Derived or processed metrics available to researchers | Developer API v2. Cycle: day Strain, kilojoules, average and max HR, step count (since 2026-09-23). Recovery: score, resting HR, HRV (RMSSD), and SpO2 and skin temperature on 4.0 and later. Sleep: stage durations, performance, efficiency, consistency, respiratory rate, sleep need. Workout: Strain, HR, zones, distance. Body measurements and basic profile [V, 2026-10-10] |
| Documented sampling rates or temporal resolution | **Developer API:** One record per physiological cycle, sleep, recovery or workout; no intraday time series [V, 2026-10-10]<br>**Device sensors and WHOOP Unite research data (2022 to 2023 documents):** HR and accelerometer sampled at 52 Hz around the clock; sleep staged in 30-second epochs; Unite research data offered at 1-second and daily grains [R, 2026-10-10] |
| How far back data can be retrieved | The API's collection endpoints have no documented lower bound on start time, which implies but does not state that a member's full history is returned once they authorize. The member CSV export can cover the entire account history [C, 2026-10-10] |
| Export, API, SDK or file routes | **Developer API:** OAuth 2.0 REST API (v2) with webhooks; live heart rate over standard BLE; a separate server-to-server Partner API only for WHOOP-approved healthcare partners. No SDK [V, 2026-10-10]<br>**Member self-export (app):** Members can request a CSV of daily scores, resting HR, HRV, respiratory rate, sleep architecture and their Journal entries for a chosen date range, delivered by emailed link; MG members on Life get additional data. Per a member, the export holds per-stage totals, not intraday data [R, 2026-10-10]<br>**Research partnerships:** Research partners have received data outside the public API. The 2023 Unite FAQ describes raw CSV or Excel files, and a 2026 tutorial reports a paid web application for viewing and downloading group data. Current terms not published [R, 2026-10-10] |
| API rate limits | 100 requests per minute and 10,000 per day per client by default; increases on request [V, 2026-10-10] |
| Terms on retaining, storing or deleting data | API terms bar building databases or permanent copies of WHOOP Data, or caching beyond the cache header, unless authorized by the WHOOP Data owner or by law; stored content must be deleted when the terms end [V, 2026-10-10] |
| Terms on using data to train AI or ML models | Prohibited under the API terms; API data may not be used to create, train, test or improve any LLM or other ML or AI model, unless authorized by the WHOOP Data owner or by law [V, 2026-10-10] |
| Announced shutdowns, deprecations or migrations, with dates | v2 API launched 2025-07-01 and v1 is no longer supported; v1 webhooks no longer published (changelog 2025-11-01); v1 activity ids dropped after 2025-09-01, with a v1-to-v2 id mapping endpoint. No later deprecation in the changelog, whose newest entry is the 2026-09-23 step count [V, 2026-10-10] |

**Compliance and regulatory**

| Fact | Value |
|---|---|
| Whether a HIPAA Business Associate Agreement is offered | No BAA offered publicly. API terms bar transmitting PHI without WHOOP's prior written consent; WHOOP's 2023 research FAQ said studies could be structured so that a BAA is unnecessary [C, 2026-10-10] |
| Whether a data processing agreement is offered | No customer DPA published. The privacy policy says WHOOP will sign Standard Contractual Clauses with customers on request for EU to US transfers [R, 2026-10-10] |
| Published HIPAA statement | API terms say WHOOP makes no representation that the APIs meet HIPAA requirements unless agreed in writing. The privacy policy says processing done on behalf of a covered entity follows that entity's Notice of Privacy Practices [C, 2026-10-10] |
| Published GDPR statement | The privacy policy has a GDPR notice for European residents, names WHOOP, Inc. as controller, Whoop Limited (Dublin) as EU representative and a UK representative. A 2023 WHOOP FAQ called WHOOP GDPR compliant [R, 2026-10-10] |
| ISO/IEC 27001 status and evidence | Not public [2026-10-10] |
| SOC 2 status and evidence | The only claim found is a 2022 WHOOP study-onboarding deck listing SOC 2 among its compliance claims; no current report, trust page or attestation found [R, 2026-10-10] |
| FDA clearances, from the FDA database | One 510(k): K243236, WHOOP ECG (electrocardiogram) Feature (1.0), OTC ECG software, product code QDA, cleared 2025-04-04. Blood Pressure Insights is not cleared: FDA warning letter of 2025-07-14; the close-out letter of 2026-06-17 says FDA does not intend to enforce for BPI as modified [V, 2026-10-10]<br>**Irregular Heart Rhythm Notifications:** Listed on the Life membership but not available in the US; WHOOP staff cited regulatory restrictions (May 2025), and openFDA shows no 510(k) for it [R, 2026-10-30] |
| Where data is stored, and residency options | Personal data is processed in the United States; a 2023 WHOOP FAQ says it is stored in AWS West. No residency options published [R, 2026-10-10] |

<!-- facts:end -->

## Key Links

- Official site: https://www.whoop.com/
- Research page: https://www.whoop.com/us/en/research/
- Research Request Intake form: https://whoopinc.typeform.com/whoop-research
- Membership pricing: https://www.whoop.com/us/en/membership/
- Privacy policy: https://www.whoop.com/privacy/full-privacy-policy/
- Partner API overview: https://developer.whoop.com/docs/partner/overview
- API changelog: https://developer.whoop.com/docs/api-changelog
- Developer platform: https://developer.whoop.com/
- Developer introduction: https://developer.whoop.com/docs/introduction/
- API reference: https://developer.whoop.com/api/
- Rate limiting: https://developer.whoop.com/docs/developing/rate-limiting/
- Getting started: https://developer.whoop.com/docs/developing/getting-started/
- App approval: https://developer.whoop.com/docs/developing/app-approval/
- API Terms of Use: https://developer.whoop.com/api-terms-of-use/
- Support: https://developer.whoop.com/docs/developing/support/
- Consumer terms: https://www.whoop.com/termsofuse/

## Sources

1. WHOOP API documentation. https://developer.whoop.com/api/ (accessed 2026-08-21). **Primary.** Establishes the v2 endpoint inventory and every returned score field listed above, and that no raw HR or IBI endpoint is documented.
2. WHOOP Developer Platform introduction. https://developer.whoop.com/docs/introduction/ (accessed 2026-08-21). Establishes v2 status, v1 webhook removal, and the app-approval requirement.
3. WHOOP API rate limiting. https://developer.whoop.com/docs/developing/rate-limiting/ (accessed 2026-08-21). Establishes 100 req/min and 10,000 req/day per client, the rate-limit headers, and that increases are available on request.
4. WHOOP OAuth scopes (corroborated across developer documentation and integration guides). https://developer.whoop.com/docs/developing/getting-started/ ; https://openwearables.io/docs/providers/whoop-api-integration (accessed 2026-08-21).
5. WHOOP API Terms of Use. https://developer.whoop.com/api-terms-of-use/ (accessed 2026-08-21 via search index; **re-read in full 2026-10-10**, effective date 6 October 2026). **Primary.** Source of the permanent-copy and AI/ML bans and their data-owner exception (§4.2), the third-party and medical-device prohibitions (§3.1), the HIPAA clause (§1.8), the user-cap clause (§1.5), the no-charge clause and the termination deletion duty.
6. Schyvens A.-M. et al., "A performance validation of six commercial wrist-worn wearable sleep-tracking devices for sleep stage scoring compared to polysomnography." *SLEEP Advances* 2025;6(2):zpaf021. https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472, independent, n=62; WHOOP 4.0 best of six at ~69.6%.
7. WHOOP membership pricing (secondary, first pass): https://lifestack.ai/blog/how-much-is-whoop-membership ; https://www.droid-life.com/2026/04/22/is-a-fitbit-air-at-99-plus-a-monthly-subscription-appealing/ (accessed 2026-08-21). Superseded by source 29.
8. Miller DJ, Sargent C, Roach GD. "A Validation of Six Wearable Devices for Estimating Sleep, Heart Rate and Heart Rate Variability in Healthy Adults." *Sensors* 2022;22(16):6317. https://doi.org/10.3390/s22166317 (PMC9412437; accessed 2026-10-09). PDF: `../literature/whoop/2022-miller-sensors-six-wearables-sleep-hr-hrv-validation.pdf`.
9. Grandner MA et al. *Sleep* 2023;46(1):zsac152. https://doi.org/10.1093/sleep/zsac152 (PMC13396806; accessed 2026-10-09).
10. Bellenger CR, Miller D, Halson SL, Roach GD, Maclennan M, Sargent C. *Sensors* 2022;22(18):6723. https://doi.org/10.3390/s22186723 (funding and COI read from `../literature/whoop/2022-bellenger-sensors-hrv-variability-water-polo.pdf`, 2026-10-09).
11. Miller DJ, Lastella M, Scanlan AT, et al. *J Sports Sci* 2020;38(22):2631-2636. https://doi.org/10.1080/02640414.2020.1797448 (Crossref funder metadata, https://api.crossref.org/works/10.1080/02640414.2020.1797448, accessed 2026-10-09).
12. WHOOP for Developers, App Approval. https://developer.whoop.com/docs/developing/app-approval (accessed 2026-10-10). **Primary.** Sandbox, Build, Growth, Scale and Production member tiers, the 50% rule and manual review.
13. WHOOP for Developers, API reference. https://developer.whoop.com/api (accessed 2026-10-10). **Primary.** The six v2 OAuth scopes; no Journal or ECG scope.
14. FDA 510(k) K243236, WHOOP ECG (electrocardiogram) Feature (1.0). https://api.fda.gov/device/510k.json?search=k_number:K243236 ; https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K243236 (accessed 2026-10-10). **Primary.** Decision 2025-04-04, product code QDA; the only WHOOP record in openFDA (https://api.fda.gov/device/510k.json?search=applicant:whoop).
15. FDA Warning Letter, WHOOP, Inc., MARCS-CMS 709755, 14 July 2025. https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/warning-letters/whoop-inc-709755-07142025 ; close-out letter, 17 June 2026, https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/warning-letters/whoop-inc-709755-06172026 (both accessed 2026-10-10). **Primary.** BPI marketed without clearance; enforcement discretion for BPI as modified.
16. Business Wire, "WHOOP Unite and Ashley Addiction Treatment Partner to Break New Ground in Research and Patient Care", 10 November 2022. https://www.businesswire.com/news/home/20221110005420/en/ (seen via search results 2026-10-10, not opened). **Secondary/press.** WHOOP Unite and WHOOP Gateway in a research partnership.
17. Miller DJ, Roach GD, Lastella M, et al. *Biosensors* 2021;11(6):185. https://doi.org/10.3390/bios11060185 (funding and conflict-of-interest sections read in Europe PMC full text of PMC8226553, 2026-10-10).
18. WHOOP, Research Request Intake (Typeform). https://whoopinc.typeform.com/whoop-research (accessed 2026-10-10). **Primary.** Live form linked from the research page; form title only, questions not read, nothing submitted.
19. WHOOP, Research page. https://www.whoop.com/us/en/research/ (read in a browser 2026-10-10; HTTP 403 to scripts). **Primary.** Works with "academic and industry partners"; no eligibility criteria, fees or data terms.
20. WHOOP Privacy Policy, last updated August 3, 2026. https://www.whoop.com/privacy/full-privacy-policy/ (read from Internet Archive capture of 2026-08-06, https://web.archive.org/web/20260806173749/https://www.whoop.com/privacy/full-privacy-policy/ , accessed 2026-10-10). **Primary.** Research partners, GDPR notice and representatives, SCCs on request, US processing, covered-entity notice.
21. Stanford Wu Tsai Human Performance Alliance with WHOOP, *npj Digital Medicine* 2026. https://doi.org/10.1038/s41746-026-02799-9 (Europe PMC full text PMC13482339, accessed 2026-10-10). Data available only with WHOOP's permission.
22. WHOOP, Digital WHOOP Labs. https://www.whoop.com/us/en/digital-whoop-labs/ (Internet Archive capture of 2026-07-27, accessed 2026-10-10). **Primary.** In-app member research studies.
23. Mubadala, partnership press release, 2026-05-07. https://www.mubadala.com/en/news/mubadala-partners-with-whoop-to-strengthen-preventative-health-and-research-capabilities-in-the-uae (accessed 2026-10-10). **Secondary/press.**
24. WHOOP Unite Research FAQs, WHOOP-authored, file dated 2023-05, hosted by the University of Arizona sensor lab. https://www.sensorlab.arizona.edu/sites/default/files/2023-05/WHOOP%20Unite%20Research%20FAQs_0.pdf (accessed 2026-10-10). Raw CSV/Excel files with RR intervals, extra-cost API extraction, 52 Hz sampling, 30-second sleep epochs, BAA, GDPR, AWS West, healthcare@whoop.com. Dated; **Reported**.
25. WHOOP Unite Study Site Onboarding deck, WHOOP-authored, copyright 2022. https://sensorlab.arizona.edu/sites/default/files/2023-05/Study%20Site%20Onboarding.pdf (accessed 2026-10-10). 1-second and daily data grains; SOC 2 claim.
26. whoopunite.com, HTTP 301 to https://www.whoop.com/ (curl, 2026-10-10); Athletech News, Unite layoffs, 13 January 2023, https://athletechnews.com/whoop-b2b-solution-unite-layoffs/ (accessed 2026-10-10).
27. Tutorial on wearable API access, *Clinical and Translational Science* 2026. https://doi.org/10.1111/cts.70693 (Europe PMC full text PMC13438180, accessed 2026-10-10). Institutional legal review, possible minimum device order, paid group-data web application.
28. WHOOP developer forum threads on tier approval: https://www.community.whoop.com/t/no-response-on-api-app-approval-to-raise-the-10-user-limit/15246 ; https://www.community.whoop.com/t/production-api-access-submitted-jun-26-no-decision-after-60-days-playerslab-integration-already-built/15628 ; https://www.community.whoop.com/t/app-approval-to-raise-the-10-user-limit-3-submissions-since-april-still-no-response-today-ai/15779 (accessed 2026-10-10). User posts, June to August 2026.
29. WHOOP, Membership page. https://www.whoop.com/us/en/membership/ (US prices read in a browser 2026-10-10; Canadian prices, device inclusion, 14+ day battery and IHRN footnote from Internet Archive capture of 2026-10-02, https://web.archive.org/web/20261002041123/https://www.whoop.com/us/en/membership/). **Primary.**
30. trackervs, WHOOP pricing, updated May 13, 2026. https://trackervs.com/pricing/whoop-pricing/ (accessed 2026-10-10). **Secondary.** 12-month commitment for monthly billing.
31. WHOOP, "Access your WHOOP data with new integrations and data export options", June 15, 2026. https://www.whoop.com/us/en/thelocker/access-your-whoop-data-with-new-integrations-data-export-options/ (Internet Archive capture of 2026-06-17, accessed 2026-10-10). **Primary.** Member CSV export contents and history range; member forum report on granularity, https://www.community.whoop.com/t/please-open-up-access-to-my-data-through-any-channel/14709 .
32. WHOOP for Developers, API changelog. https://developer.whoop.com/docs/api-changelog (accessed 2026-10-10). **Primary.** `step_count` on cycles, 2026-09-23; v2 launch; v1 webhook removal.
33. WHOOP for Developers, Partner API overview. https://developer.whoop.com/docs/partner/overview (accessed 2026-10-10). **Primary.** Exclusive to WHOOP-approved healthcare partners.
34. WHOOP community, "Is IHRN available in the US?", WHOOP staff reply 2025-05-09. https://community.whoop.com/t/is-ihrn-available-in-the-us/477 (accessed 2026-10-10).
35. WHOOP, Bulk buy. https://www.whoop.com/us/en/bulk-buy/ (browser read 2026-10-10; HTTP 403 to scripts). Volume pricing for any buyer.
36. WHOOP for Developers, Support. https://developer.whoop.com/docs/developing/support (accessed 2026-10-10). **Primary.** No continuous HR via the API; BLE heart-rate broadcast; free API with membership requirement; about 4 KB per member-day.
