# Unresolved Questions

Questions that could not be reliably answered from available sources. Each names the organization
that can answer it and an official contact route where one exists.

**Last updated: 2026-08-25** (Module 2 third-pass direct-source re-verification of Beiwe, RADAR-base,
Avicenna Research, m-Path, and CARP Mobile Sensing resolved or materially updated Tier 10 items #84,
#85, #86, #89, #90, #93, #94 and added Tier 13 — see #101–#105 below. Module 1 literature-library
retrofit added Tier 12 — see #97–#100; Module 2 literature-library retrofit added Tier 11; Module 2
second-pass direct-source re-verification (AWARE/mindLAMP/MetricWire) annotated four Tier 10 items —
see #87, #88, #91, #92; Module 2 initial research pass added Tier 10; Module 1 content in Tiers 1–9
below unchanged from 2026-08-21/24).

---

## What is actually gated, and what is not

**Corrected 2026-08-21 (second pass).** The first draft of this file overstated vendor gating. The
distinction matters, so it is stated explicitly here.

**API documentation is public for every platform in this module except three.** Oura's, WHOOP's,
Fitbit/Google's, Polar's and Samsung's reference documentation was read directly, without an
account, during this research. Only **Garmin** (developer portal login for field-level schemas),
**Withings** (Partner Hub login for the API reference) and **Samsung's Privileged SDK download**
(partner approval to obtain the SDK itself) sit behind a wall.

**You can start building on most of these today, for free, with no one's permission:**

| Platform | What you can do right now, unaided |
|---|---|
| **Oura** | Register an OAuth application and pull full API v2 data for **up to 10 users**. No approval, no fee. Personal access tokens were retired in Dec 2025, so it is OAuth rather than a token, but that is a code change, not a gate |
| **Polar** | Clone the BLE SDK from GitHub and stream raw ECG at 130 Hz. No registration of any kind |
| **WHOOP** | Register an app and pull v2 data. The constraint is contractual (terms on data retention), not technical |
| **Fitbit / Google Health** | Register a Google Cloud project and pull data for **up to 100 users** unverified |
| **Movesense** | Buy a developer kit; open APIs, no licence cost, custom firmware permitted |
| **Axivity / GENEActiv** | Buy a device and download files over USB. There is no vendor to ask |

**So what is the "contact the vendor" list actually for?** Two things, neither of which is access to
documentation:

1. **Scale thresholds.** Oura's own documentation says applications are limited to 10 users "before
   requiring approval from Oura. There is no limit once an application is approved." What is *not*
   documented anywhere public is what that approval involves — form, review time, criteria, cost,
   whether academic studies are treated differently. A pilot with 8 participants never encounters
   this. A study with 40 does.
2. **Commercial terms that are simply not published.** Garmin's SDK licence fee. The Withings
   Advanced Research API contract. Fitabase's fee structure. Ametris's price list. Whether any of
   them will sign a BAA. These are not hidden behind a login — they are not written down anywhere.

The practical implication is that **none of these questions block starting work**. They block
*scaling* work, and they block *budgeting* work. A team can prototype against Oura, Polar, WHOOP or
Google Health this week and only hit a wall at participant 11, or 101, or when procurement asks for
a quote.

---

## Tier 1 — Gating at scale. Resolve before enrolling beyond a pilot.

| # | Question | Who | Contact | When it bites |
|---|---|---|---|---|
| 1 | **Does the Google Health API return dense (minute-level or better) heart rate?** Heart Rate is documented as a *Sample* type with no stated interval; HRV/SpO2/RHR appear as Daily Aggregates. No intraday endpoint family exists | Empirically testable — **no vendor contact needed** | Register a Google Cloud project, pull a day of Heart Rate samples, count them | Before designing any Fitbit-based physiological study post-Sept 2026 |
| 2 | **Does an academic study qualify for the Google Health API's "internal use within an organization" verification exception?** | Google | Google Cloud Console OAuth consent configuration | At participant 101. Difference between free and a recurring **$500–$4,500** CASA assessment |
| 3 | **What is Oura's approval process, criteria and turnaround above 10 users?** | Oura | The "My Applications" portal at cloud.ouraring.com — the request is made in-product | At participant 11 |
| 4 | **Will WHOOP grant written permission to retain a permanent analysis dataset?** Their API terms bar building databases or permanent copies, with an "unless otherwise agreed in writing" carve-out | WHOOP | developer.whoop.com/docs/developing/support/ | Before writing a protocol — this one *is* genuinely blocking, because it is contractual rather than technical |
| 5 | **What does a Garmin Health SDK licence cost for an academic study, and is the device MOQ waivable?** Note this may be avoidable entirely: Enhanced BBI is available through the **Health API** and through **Fitabase** via ordinary Garmin Connect OAuth, with no custom app | Garmin | "Request Now" at developer.garmin.com/health-sdk/ · connect-support@developer.garmin.com | Only if you need real-time daytime streaming rather than nocturnal BBI |
| 6 | **Samsung Partner Program criteria and timeline for Privileged Health SDK access.** This is a real wall — the SDK cannot be downloaded without it | Samsung | Partner Program request via developer.samsung.com/health/privileged/ | Before any Samsung raw-signal work |

## Tier 2 — Pricing. Five of eleven ecosystems have entirely non-public pricing.

| # | Question | Who | Contact |
|---|---|---|---|
| 6 | ~~Empatica Academic & Basic Research plan cost~~ — **RESOLVED, pricing is public.** Device from **$1,166.40**; 3-year bundle **$2,332.80** list / **$1,749.60** academic (25% off); 5-year **$2,916** / **$2,187** academic. Volume discounts automatic at 5+ devices | Empatica | https://www.empatica.com/store/platform-professional/ |
| 7 | **Precisely which digital biomarkers are Enterprise-only?** Now three conflicting public figures: the store page says the academic plan includes "11+ digital biomarkers", the research-studies page names **18**, and platform marketing says "over 100 research-grade biomarkers" | Empatica | as above |
| 8 | Fitabase fee structure — per participant, per study, per month? Cost of the Aggregate Data API and SMS add-ons? Cost of Engage when it launches? **Note: Labfront publishes its pricing (free / $500 / $1,250 per year) and covers Garmin, so a price comparison is now possible from one side** | Fitabase | hello@fitabase.com · https://www.fitabase.com/how-it-works/pricing/ |
| 9 | Current Ametris price list for LEAP, CentrePoint Insight Watch, wGT3X-BT, ActiLife, and CentrePoint — and whether academic pricing exists | Ametris (Signant Health) | https://ametris.com/ |
| 10 | Withings Advanced Research API commercial terms and cost | Withings Health Solutions | https://www.withings.com/us/en/health-solutions/research-clinical-trials |
| 11 | Oura institutional/bulk pricing for rings and memberships | Oura | https://ouraring.com/business |
| 12 | WHOOP Unite pricing and what it provides a research organization | WHOOP | WHOOP Unite sales |
| 13 | Axivity AX3/AX6 and Activinsights GENEActiv current list and academic pricing | Axivity Ltd; Activinsights Ltd | https://axivity.com/ |
| 14 | Which Garmin Health API metrics "may require a license fee payment," and how much? | Garmin | connect-support@developer.garmin.com |

---

## Tier 3 — Compliance and governance. Do not infer any of these.

| # | Question | Who | Notes |
|---|---|---|---|
| 15 | Will Google execute a HIPAA BAA covering Google Health API data for research? | Google | Not stated publicly |
| 16 | Does Fitabase execute a BAA, or is its de-identification model designed specifically to stay outside PHI? | Fitabase | The distinction changes the institutional review path entirely |
| 17 | Will Garmin execute a BAA for the Standard Health SDK, given it is described as HIPAA-compliant? | Garmin | A compliance claim is not a BAA |
| 18 | Oura: HIPAA BAA availability, GDPR DPA, SOC 2 / ISO 27001 status, data residency options, retention policy | Oura | None established from public sources |
| 19 | WHOOP: does any arrangement provide a BAA, given the explicit API HIPAA disclaimer? | WHOOP | |
| 20 | Empatica: BAA, DPA, SOC 2 / ISO status, data residency | Empatica | Almost certainly exists given clinical-trial customers, but unverified |
| 21 | Ametris/Signant: BAA, DPA, SOC 2 / ISO, Part 11 / GxP posture — **and whether the Signant acquisition changes data processing terms** | Ametris / Signant Health | Contract review item |
| 22 | Withings: BAA, DPA, SOC 2 / ISO, data residency; which devices hold which specific regulatory clearances in which jurisdictions | Withings | |
| 23 | Samsung: DPA/BAA for the Health Data SDK path; governance model for self-deployed Research Stack backends | Samsung | |
| 24 | Polar: BAA/DPA for Flow and AccessLink (not needed for the BLE SDK path, which has no processor) | Polar | |
| 25 | **Exact FDA clearance scope for Empatica** — 510(k) numbers and indications for use, for the platform and for each cleared biomarker | Empatica | "FDA-cleared" without an indication statement is not actionable |
| 26 | Exact regulatory clearance scope for WHOOP MG's ECG and Blood Pressure Insights | WHOOP | |

---

## Tier 4 — Technical specifications not publicly documented

| # | Question | Who | Notes |
|---|---|---|---|
| 27 | **Complete Garmin Health API data-type list and per-type field schema.** The summaries reference page returned 404 | Garmin | Only `dailies`, `epochs`, `sleeps`, `activities`, `activityDetails`, `hrv` confirmed by name |
| 28 | Garmin Health API rate limits, data latency, retention, and backfill depth | Garmin | None published |
| 29 | Google Health API rate limits | Google | None published |
| 30 | Withings Public Health Data API rate limits, retention, backfill depth | Withings | Behind Partner Hub login |
| 31 | Polar per-device sampling rates (ECG Hz, ACC Hz, PPI resolution) and onboard memory capacity / maximum offline logging duration | Polar | In per-product SDK docs, not retrieved |
| 32 | Samsung raw PPG sampling rate and whether it is configurable; realistic battery life under continuous raw PPG + accelerometer streaming | Samsung | |
| 33 | Empatica configurable sampling-rate ranges per sensor and their battery-cost curves | Empatica | Configurability confirmed; range not |
| 34 | Ametris current-device configurable sampling rates and dynamic ranges | Ametris | |
| 35 | What the CentrePoint API exposes — raw data or derived outcomes only? Auth model? Limits? | Ametris | |
| 36 | Oura `heartrate` time-series temporal resolution, and whether it is available on Ring 4 (the scope note still says "Gen 3 users") | Oura | |
| 37 | Whether Oura Ring 4's newer metrics (cardiovascular age, resilience, VO2 max) are gated by membership tier at the API level | Oura | |
| 38 | Whether Fitbit Premium-gated derived metrics are available through the API | Google | |
| 39 | Whether WHOOP Journal (self-report) data is available via the API | WHOOP | No journal scope appears in the v2 scope list |
| 40 | Whether Empatica offers real-time or near-real-time access under any plan — and how this reconciles with its real-time seizure-alerting product | Empatica | Research platform documented as historical-only |
| 41 | Maximum recording duration for Axivity AX3/AX6 and GENEActiv at various sampling-rate and range configurations | Axivity; Activinsights | |

---

## Tier 5 — Live contradictions between sources. Recorded, not resolved.

| # | Contradiction | Sources | Resolution path |
|---|---|---|---|
| 42 | **Apple ECG:** `HKElectrocardiogram` + `HKElectrocardiogramQuery` expose individual voltage measurements, and third parties do read them — but the ResearchKit & CareKit FAQ states researchers cannot access raw ECG data through HealthKit | S-APL-03 vs S-APL-04, S-VAL-07 | Build a test app and read an ECG sample's voltage measurements. Likely reconciliation: discrete recordings are accessible, continuous ECG is not |
| 43 | **Withings accelerometer sampling rate:** the Advanced Research API page says 25 Hz default, up to 100 Hz; the Raw Data page says both sensors sample at ≈24.824 Hz | S-WTH-01 vs S-WTH-02 | Ask Withings directly; the "up to 100 Hz" claim may be a roadmap or contracted-tier capability |
| 44 | **Polar H10 accelerometer:** the SDK README device matrix does not mark ACC for H10, but Polar's research-tools page states the H10 provides "raw sample data, such as ECG and 3D acceleration" | S-POL-01 vs S-POL-02 | Read `documentation/products/PolarH10.md` in the SDK repository |
| 45 | **Samsung minimum watch generation:** Privileged Health SDK FAQ says Galaxy Watch4 and later; Research Stack material references Galaxy Watch5 and later as tested | S-SAM-01 vs S-SAM-04 | May simply be SDK-support vs Research-Stack-tested. Confirm with Samsung |
| 46 | **Empatica biomarker count:** the research-studies page names 18 validated biomarkers; other Empatica material says "over 100 research-grade biomarkers" | S-EMP-01 vs vendor platform copy | Likely 18 clinically validated versus 100+ computed. Confirm which are in the Academic plan (see #7) |

---

## Tier 6 — Discovery gaps. Not researched in this pass.

Recorded so that their absence is a known gap rather than an implicit judgement of unimportance.

| # | Technology | Question |
|---|---|---|
| 47 | ~~**Verily Study Watch**~~ | **RESOLVED — active, not discontinued; clinical-research-only, never sold to consumers; records ECG, HR, EDA and inertial motion with weeks of onboard raw storage; multiple FDA 510(k) clearances. See `emerging-platforms.md`** |
| 48 | ~~Biostrap~~ | **RESOLVED — raw/processed PPG, gyroscope and accelerometer via RPM dashboard; configurable sampling rates; integrated surveys; pivoted from consumer to medical. Pricing still non-public** |
| 49 | ~~Ultrahuman Ring Air~~ | **RESOLVED — UltraSignal exposes raw PPG, accelerometer and temperature; whitelist-only Partner API with loaner dev kits. The only ring with raw PPG. Sampling rates and pricing still unknown** |
| 50 | RingConn, Circular, and other smart rings | Whether any offers research data access |
| 51 | Amazfit / Zepp Health | Zepp OS SDK and data access for research; significant in non-US markets |
| 52 | ~~Movesense (Suunto)~~ | **RESOLVED — full profile written. ECG 125–512 Hz, 9-axis IMU 13 Hz–1.6 kHz, custom firmware at no licence cost, Class IIa MDR on the MD variant. New gap: no independent validation located** |
| 53 | Whoop 4.0 vs 5.0 | Whether the Schyvens 2025 result on the 4.0 transfers to 5.0 hardware |
| 54 | ~~"Fitbit Air"~~ | **RESOLVED — launched 7 May 2026 at $99.99. Screenless, 12 g; PPG, red/IR SpO2, skin temperature, 3-axis accelerometer, gyroscope; HR saved at 2-second intervals; 7-day battery. Open question: is the 2-second HR exposed via the API?** |
| 55 | Activinsights / GENEActiv | Is the GENEActiv line still in active production and supply? |
| 56 | Open Movement project | Current maintenance status of OmGui and the AX firmware |

---

## Tier 7 — Evidence retrieval outstanding

| # | Item | Why |
|---|---|---|
| 57 | ~~Read Robbins et al. 2024 in full~~ | **DONE — full extraction in `../module-01-wearables/validation-evidence.md`. Surfaced the Oura funding and advisory-board conflict, and the poor deep/REM ICCs** |
| 58 | ~~Read Schyvens et al. 2025 in full~~ | **DONE — full extraction. Corrected a material misreporting in the first pass and recovered the ScanWatch result (κ=0.22)** |
| 59 | Find or commission a study placing **Oura and WHOOP under the same PSG protocol** | No such comparison exists. Their respective "best device" claims rest on studies that excluded each other |
| 60 | Independent validation of Samsung's derived metrics (sleep, Antioxidant Index, Vascular Load) | Samsung is absent from the major multi-device comparisons |
| 61 | Independent validation of ventral-wrist EDA (Empatica) against palmar EDA | Wrist EDA has known anatomical limitations |
| 62 | Apple hypertension-notification validation study | Referenced in Apple's launch materials; the underlying publication was not located |


---

## Tier 8 — New questions raised by the second pass

| # | Question | Who / how | Why it matters |
|---|---|---|---|
| 63 | **Does the Google Health API return dense heart rate samples in practice?** Documentation says Sample type with no interval | **Empirically testable** — register a project, pull a day, count samples | Determines whether Fitbit remains viable for physiological research at all |
| 64 | Does an academic study qualify for Google's "internal use within an organization" verification exception? | Google Cloud Console | Free vs a recurring $500–$4,500 CASA assessment |
| 65 | Is the **Fitbit Air's 2-second heart rate** exposed through the Google Health API? | Same test as #63, with an Air | Would make a $99 screenless device the best cost-per-signal option in the module |
| 66 | **Is there any independent validation of Movesense** ECG or IMU against reference instruments? | Literature search | The best hardware specs in the module appear to have an empty evidence base |
| 67 | Ultrahuman raw PPG **sampling rate**, and UltraSignal pricing and scale limits | Ultrahuman | Determines whether the only raw-PPG ring is actually usable at study scale |
| 68 | Biostrap sampling rates and pricing | Biostrap | Same |
| 69 | Are **Oura Health Radar** outputs (Blood Pressure Signals, Nighttime Breathing), GLP-1 insights and lab integration exposed through API v2? | Testable against an existing Oura integration | New Ring 5 capabilities may be app-only |
| 70 | Is **Garmin Enhanced BBI** on the standard Connect Developer Program tier, or does "select partners" imply separate approval or fee? | Garmin, or testable via Labfront's free tier | Changes whether nocturnal HRV is cheap or negotiated |
| 71 | Does Whoop 5.0 perform differently from the 4.0 tested by Schyvens? | Literature / WHOOP | The tested hardware is a generation old |
| 72 | Do Oura Ring 4/5 perform differently from the Gen3 tested by Robbins? | Literature / Oura | Same, and Ring 5 claims skin-tone-specific improvements |
| 73 | **Does anyone's PSG validation record participant skin tone?** Neither study did | Literature | PPG accuracy across skin tones is a known physical concern and is currently unquantified in this evidence base |
| 74 | Labfront vs Fitabase for Garmin: does Labfront's SDK-derived "higher resolution" exceed what Fitabase's OAuth route obtains? | **Testable** — both offer Garmin BBI; Labfront has a free tier | Direct cost and capability comparison |
| 75 | Which Empatica biomarkers does the academic plan include — 11, 18, or 100+? | Empatica | Three conflicting public figures; determines academic-tier sufficiency |
| 76 | Movesense SDK/firmware **licence identity** ("no licence cost" is stated; the licence is not named) | Movesense | Matters for institutional legal review and derivative work |

---

## Tier 9 — Raised by the research-library sponsorship pass (2026-08-24)

| # | Question | Who / how | Why it matters |
|---|---|---|---|
| 77 | **Is there any independent (non-vendor-funded/authored) SpO2 validation study for Oura or WHOOP?** None found in a broad literature sweep for either device | Literature search (PubMed advanced search rather than general web search — access was blocked on several publisher sites in this pass) | SpO2 accuracy is a live regulatory and clinical-safety concern (skin-tone bias); this is a near-total evidence gap for both devices |
| 78 | **Is there any independent skin/body-temperature validation study for Oura or WHOOP?** Same gap as #77 | Same | Both devices market temperature-based features (illness detection, ovulation) built on unvalidated-by-third-parties sensing |
| 79 | **Who actually authored "The menstrual cycle through the lens of a wearable device," *npj Digital Medicine* 9:633 (2026)?** Could not get past Nature's login wall, PubMed's cookie wall, or EuropePMC's nav-only page | Direct read of the paper (institutional access or the published PDF) | Determines whether this is WHOOP-employee-authored (as its sister paper is) or independent — currently Unclear, not assumed |
| ~~80~~ | ~~What are WHOOP 4.0's exact HRV CCC/MAPE figures in Dial et al. 2025, and does that paper disclose any vendor funding?~~ **Resolved 2026-08-25.** Full text read directly from the local PDF. WHOOP HRV: CCC=0.94, MAPE=8.17±10.49%. Funding: AFRL only; "authors declare that they have no competing interests." Full RHR/HRV tables for all five devices now in `validation-evidence.md` §3a; tier upgraded to Verified in `research-library-wearables.md`. | — | — |
| 81 | Do the Miller et al. 2020 (*J Sports Sciences*, WHOOP validation) and Bellenger et al. 2022 (water polo HRV) papers disclose WHOOP funding? Both share an author cluster with a confirmed WHOOP-sponsored CQU position (Dean Miller) | Tandfonline / MDPI, direct read | If WHOOP-funded, these should move from the "independent" framing they're often cited with to Tier B |
| 82 | Does Oura's own research page currently say "170+" or "130+" peer-reviewed studies, and has that number changed over time? | ouraring.com/science-and-research, checked on different dates | A moving/inconsistent headline number is itself worth noting if confirmed |
| 83 | Full funding/COI text for five systematic reviews blocked by paywalls this pass: Khan et al. 2025 (Oura, *OTO Open*), Shahid et al. 2025 (Apple Watch AF, *JACC: Advances*), Choe & Kang 2025 (Apple Watch, *Physiological Measurement*), the Nova Southeastern AF-wearables review (PMC8752409), Khodr et al. (WHOOP, medRxiv preprint) | Direct read via institutional access | Each review's own reference list is a discovery mechanism for further papers not yet in `research-library-wearables.md`, and none of the five has been tier-classified with a Verified-level disclosure read |

---

## Tier 10 — Module 2 (Digital Phenotyping Platforms), initial research pass (2026-08-24)

This module received a single research session, with a higher proportion of search-summary (as
opposed to direct-fetch) retrieval than Module 1 — see `module-02-digital-phenotyping/sources.md`'s
retrieval-method notes. The items below are recorded per CLAUDE.md's instruction to name the specific
vendor/organization and, where one exists, an official contact route.

| # | Question | Who / how | Why it matters |
|---|---|---|---|
| ~~84~~ | ~~No platform in Module 2 has documented HIPAA, GDPR/DPA, SOC 2, or 21 CFR Part 11 compliance evidence...~~ **Materially outdated as of 2026-08-25.** This is no longer accurate as a blanket claim: **Avicenna Research** now has an independently audited, dated **ISO 27001:2022 certification** (Verified) plus detailed HIPAA/UK-GDPR/PIPEDA language for minors' data (Corroborated), and **m-Path** now has a vendor self-declared "compliant with GDPR and HIPAA" statement (Corroborated, not independently audited). **Still genuinely unresolved**: mindLAMP, MetricWire, RADAR-base (beyond its managed-hosting-cloud's GDPR-compliance framing), Beiwe (beyond a non-certification HIPAA-applicability acknowledgment), CARP Mobile Sensing, and AWARE Framework — none of these six have documented compliance certification evidence, and SOC 2 / 21 CFR Part 11 status remains unconfirmed for every platform in the module including Avicenna Research and m-Path. | Direct contact with each remaining organization; see each profile's Key Links | Still the single largest *residual* cross-platform gap for the six platforms without compliance evidence, though the module is no longer uniformly undocumented on this axis |
| ~~85~~ | ~~What are actual **Beiwe Service Center (BSC)** rate figures?~~ **Resolved 2026-08-25.** Direct fetch of the BSC's own overview page now returns actual rates: **$1,937/month fixed + $6/Active Participant Month variable**, with worked examples totaling $24,144–$27,564. See `module-02-digital-phenotyping/profiles/beiwe.md`. | — | — |
| ~~86~~ | ~~Does **RADAR-base** offer a managed-hosting or paid-support option comparable to the Beiwe Service Center?~~ **Resolved (existence) 2026-08-25.** Yes — The Hyve (RADAR-base's co-maintainer) offers **"RADAR-base as a Service"**: GDPR-compliant cloud hosting, 2–4 week setup, best suited to studies of ~200 participants or fewer (single-server). **Not resolved: pricing.** No rate figures are published; this remains a quote-based service. See `module-02-digital-phenotyping/profiles/radar-base.md`. | The Hyve — https://www.thehyve.nl/services/radar-base-as-a-service | What does RADAR-base as a Service actually cost, and how is the ~200-participant ceiling raised for larger studies? |
| 87 | ~~Which **mindLAMP** repositories are current/production, and what are the successors to the explicitly deprecated `LAMP-portal` and `LAMP-app` repositories?~~ | BIDMC Division of Digital Psychiatry — https://github.com/BIDMCDigitalPsychiatry | **RESOLVED 2026-08-24 (second pass, Verified via direct GitHub fetch).** `LAMP-portal` and `LAMP-app` were formally archived 2020-11-17 (read-only); successors are `LAMP-dashboard` and `LAMP-core-android`/`LAMP-core-ios` respectively. See `module-02-digital-phenotyping/profiles/mindlamp.md`. **Remaining open sub-item:** the specific open-source licence covering `LAMP-server`/`LAMP-dashboard`/`LAMP-core-android`/`LAMP-core-ios` themselves was not located (only `LAMP-js`/`LAMP-py` = BSD-3-Clause and `LAMP-toolkit` = MIT are confirmed) — still needs direct contact or an individual-repo licence-file check. |
| 88 | ~~What is **AWARE Framework**'s exact current sensor/plugin catalog, and precisely how does iOS coverage differ from Android?~~ | AWARE Framework maintainers — https://github.com/awareframework | **RESOLVED 2026-08-24 (second pass, Verified via direct fetch of https://awareframework.com/sensors/).** Full per-sensor Android/iOS table obtained: ~14 of ~33 documented modules are available on iOS; Locations, Applications, Communication, Installations, Keyboard, Screenshot, Screentext, and Telephony are Android-only. ESM/EMA is confirmed available on both platforms. See `module-02-digital-phenotyping/profiles/aware-framework.md`. |
| 89 | **Avicenna Research (Ethica)** and **MetricWire** current, non-trial pricing (per-participant, per-study, or subscription); whether academic/non-profit pricing exists for either | Avicenna Research — https://avicennaresearch.com/ ; MetricWire — https://metricwire.com/ | **Still unresolved for both, now after two dedicated attempts on Avicenna Research.** Second pass (2026-08-24) attempted direct fetch of metricwire.com's homepage, `/pricing`, `/site-licence/`, and `/contact-us/` — all four returned HTTP 403 (bot-protection), a confirmed access barrier rather than an unattempted gap. A "Site Licence" page exists at that URL but its terms could not be read. **Third pass (2026-08-25)** directly fetched Avicenna Research's homepage and a dedicated pricing/security search — no pricing page or dollar figures were found; pricing genuinely appears not to be published anywhere public, not merely hard to find. Both platforms' pricing remains entirely non-public; direct vendor contact is still the only path forward. |
| 90 | Does **Avicenna Research** or **MetricWire** publish a documented developer API distinct from their dashboard/export mechanisms? | Same contacts as #89 | **Partially resolved for MetricWire 2026-08-24 (second pass).** Direct fetch of https://github.com/MetricWire confirms no public SDK/API client is maintained by MetricWire itself (one unrelated forked repo only). However, an unofficial third-party Python client (`zeolite`, UW–Madison Center for Healthy Minds) targets a MetricWire backend internally called "Catalyst," and an m2c2kit integration guide describes URL-based identifier injection with MetricWire — so some form of API evidently exists but is not publicly documented for general researcher self-service. **Avicenna Research's API status: still unresolved after a third pass (2026-08-25).** Two direct fetches (homepage, data-access-and-analytics page) plus a dedicated search found no mention of a developer API anywhere — strengthens the "not confirmed" finding with repeated direct evidence, but does not positively confirm absence. |
| 91 | ~~Is **Koa Health**'s digital-phenotyping technology available to outside research teams as a deployable platform, or is it purely internal to Koa Health's own products/collaborations?~~ | Koa Health — https://www.koahealth.com/research | **Largely resolved 2026-08-24 (second pass, Corroborated via direct fetch of https://www.koahealth.com/research).** The page's own language frames digital phenotyping strictly as an internal method applied through academic partnerships (LSE, Universitat Pompeu Fabra); it contains no mention of a deployable platform, SDK, API, or self-service mechanism for outside teams. This corroborates the exclusion decision with primary-source absence rather than just inference. **Not fully closed:** ruling out an unlisted enterprise/partnership-only offering still requires direct vendor contact via Koa Health's consultation-booking flow, which this session did not initiate. |
| 92 | Is **Purple Robot** (Northwestern CBITS / Precision Health Informatics Data Lab) still actively maintained, and is it realistically deployable for a new study today? | Precision Health Informatics Data Lab — https://phidatalab.org | **Still unresolved; new negative signal found 2026-08-24 (second pass).** A deliberate re-fetch of the lab page, `/software/`, and the domain root all returned **HTTP 500 across the entire phidatalab.org domain** — not a 404 or access-denied, but a server error suggesting the site may currently be broken, migrating, or offline. This is mildly corroborating of reduced institutional maintenance but is inconclusive on its own (could be a transient outage). Still requires either a later fetch attempt or direct contact with the Precision Health Informatics Data Lab. |
| ~~93~~ | ~~What is **m-Path**'s pricing model, and what GDPR/compliance documentation exists...?~~ **Resolved 2026-08-25.** Pricing: fully public, itemized tier structure (Free/Essential/Standard/Comfort, €0–€5,338/year) plus separately priced add-ons (Sensing Lite €3,000, Sensing Full €10,000, API Access €5,000, Smartwatch Integration €3,000, and others) — direct fetch of `m-path.io/pricing/`. Compliance: m-Path's own homepage states "compliant with GDPR and HIPAA" (Corroborated — vendor-stated, not independently audited; contrast Avicenna Research's audited ISO 27001 certificate). See `module-02-digital-phenotyping/profiles/m-path.md`. | — | — |
| 94 | What is **CARP Mobile Sensing**'s realistic adoption track record outside DTU — how many independent research groups have built production studies on the `carp_mobile_sensing` Flutter package? | CARP / Jakob Bardram's group, DTU — https://carp.dk/ | **Partially updated 2026-08-25, not resolved.** A 2025 ACM UbiComp/ISWC demonstration paper on CAMS was found, showing continued academic engagement, but this session did not confirm the authors' institutional affiliations, so it does not establish external (non-DTU) adoption — only that the framework remains actively presented at a major venue five years after its original 2020 paper. Still requires direct contact or a systematic citation-tracing pass to answer the original question. |

---

## Tier 11 — Raised by the Module 2 literature-library retrofit (2026-08-24)

See `module-02-digital-phenotyping/literature-library.md` for the full academic-paper index this pass
built, including local PDF copies of every open-access paper found.

| # | Question | Who / how | Why it matters |
|---|---|---|---|
| 95 | **Does any peer-reviewed methods, validation, or deployment paper about the MetricWire platform itself exist anywhere?** A targeted literature search this pass found none — MetricWire appears in the literature only as a data-collection instrument named inside other researchers' studies, never as the subject of its own platform paper | MetricWire — https://metricwire.com/ (site itself is HTTP-403-blocked; try direct email/sales contact) | This is a genuine gap, not a search-access failure like MetricWire's site-blocking issue elsewhere in this file (#89/#90) — it may mean MetricWire has never published on its own architecture/validity, which is worth confirming directly with the vendor before relying on the platform for a study requiring documented methodological grounding |
| 96 | **Is there an author-accessible (non-paywalled) copy of the 2012 iEpi paper** (Hashemian et al., "iEpi: An End to End Solution for Collecting, Conditioning and Utilizing Epidemiologically Relevant Data," ACM MobileHealth '12, DOI 10.1145/2248341.2248345)? Only the ACM Digital Library paywalled version and an unverified academia.edu re-upload were located; the latter was not downloaded because its authenticity as an author-posted copy could not be confirmed | University of Saskatchewan (Osgood/Stanley labs) — https://www.cs.usask.ca/~osgood/ ; or Avicenna Research (commercial successor) — https://avicennaresearch.com/ | This is the historical origin paper for the Ethica/Avicenna Research platform; obtaining it would let `profiles/avicenna-research-ethica.md` cite the platform's own academic precursor directly rather than only via secondary description |

---

## Tier 12 — Raised by the Module 1 literature-library retrofit (2026-08-24)

See `module-01-wearables/literature-library.md` for the full index this pass built, including local
PDF copies of 43 of the 54 individually-named papers in `research-library-wearables.md`.

| # | Question | Who / how | Why it matters |
|---|---|---|---|
| ~~97~~ | ~~Should the WHOOP "menstrual cycle through the lens of a wearable device" paper's tier be formally corrected from "Unclear" back to "Tier A" in `research-library-wearables.md`?~~ **Resolved 2026-08-24.** Corrected directly in `research-library-wearables.md`'s WHOOP Tier A section — confirmed byline (Gonzalez, O'Day, Johnson, Kim, Jasinski, Holmes, Delp, Hicks) restored, tier corrected to A. | — | — |
| ~~98~~ | ~~Is there a working, non-bot-blocked route to three papers with confirmed or probable open-access status that automated fetch could not retrieve this pass?~~ **Resolved 2026-08-24, 2 of 3.** Khodr et al. (medRxiv) obtained via a Semantic Scholar–resolved canonical URL. Mahalingaiah et al. (AJOG) obtained via a browser session that cleared a JS bot-detection challenge, reusing the resulting cookie in a direct `curl` request. Perez et al. (NEJM Apple Heart Study) checked directly against NCBI's own OA web service (`oa.fcgi`), which returned `idIsNotOpenAccess` — this one is **genuinely paywalled**, not a retrieval-infrastructure failure as previously assumed; correctly remains unobtained. See `module-01-wearables/literature-library.md`'s "2026-08-24 retry" section for full detail. | — | — |
| 99 | **Is the Harms 2018 NAIA-baseball WHOOP dissertation (Univ. of Nebraska–Lincoln, ProQuest/ERIC ED595664) obtainable through any route?** A UNL DigitalCommons copy exists (`digitalcommons.unl.edu/cgi/viewcontent.cgi?article=1104&context=teachlearnstudent`) but returned HTTP 403 on direct fetch, and ERIC's own hosted PDF URL returned HTTP 404 | University of Nebraska–Lincoln DigitalCommons; ProQuest (with institutional access) | Low priority — the source file itself frames this as grey literature "included here only for completeness" — but a genuine, low-cost gap to close if institutional ProQuest access is available |
| ~~100~~ | ~~Should `research-library-wearables.md`'s prose be updated with the bibliographic corrections this pass surfaced from reading the actual PDFs?~~ **Resolved 2026-08-24.** All five corrections applied directly: Gong et al. venue (*Biomimetics*, not *Diagnostics*); Wasserlauf venue added (*J Cardiovascular Electrophysiology*); Littell venue added (*PLOS Digital Health*); both Doherty-lab papers' author order corrected (Lambe R first on the VO2max paper, O'Grady B first on the HRV/RHR paper — Doherty C was not first author on either). | — | — |

---

## Tier 13 — Raised by the Module 2 third pass: Beiwe, RADAR-base, Avicenna Research, m-Path, CARP (2026-08-25)

This pass brought the five platforms not covered by the 2026-08-24 second pass (Beiwe, RADAR-base,
Avicenna Research, m-Path, CARP Mobile Sensing) up to the same direct-source-fetch standard already
applied to AWARE/mindLAMP/MetricWire, per CLAUDE.md's Maintenance section. New questions the pass
could not close are recorded here rather than left implicit.

| # | Question | Who / how | Why it matters |
|---|---|---|---|
| 101 | Does the `data_access_api_reference` directory in **Beiwe**'s `beiwe-backend` repository document a public, researcher-self-service REST API, or an internal/administrative interface only? | Onnela Lab — https://github.com/onnela-lab/beiwe-backend (open the directory's contents directly) | Changes whether Beiwe should be described as API-mediated or export/database-mediated for data access — a real differentiator against competitors with documented APIs |
| 102 | What is the full per-metric catalog within **Forest**'s `jasmine` (mobility), `willow` (communication), and `sycamore` (survey) subpackages? | Onnela Lab — https://github.com/onnela-lab/forest, or Forest's dedicated documentation site | The GitHub README names the subpackages but not their individual output metrics; needed for anyone evaluating Forest against a specific research question |
| 103 | What is **RADAR-base**'s exact iOS-side sensor list (which of the 17 itemized Android streams iOS lacks, restricts, or samples differently)? | RADAR-base — https://radar-base.org/docs/4048-2/ (the page references a comparison chart this pass could not extract) | The Android list is now itemized and Verified; the iOS side is only qualitatively described ("more sparse") — an iOS-heavy study needs the itemized version |
| 104 | What does **The Hyve**'s "RADAR-base as a Service" managed-hosting offering actually cost, and how is its ~200-participant single-server ceiling raised for larger studies? | The Hyve — https://www.thehyve.nl/services/radar-base-as-a-service | The offering's existence is now confirmed; without pricing it cannot be compared against Beiwe's now-fully-priced BSC alternative |
| 105 | How feature-complete and documented is CARP's `carp-portal` repository relative to competitors' researcher dashboards (Beiwe's, Avicenna's)? Does it require separate deployment/hosting from the CAMS sensing app? | CARP / Jakob Bardram's group, DTU — https://github.com/carp-dk/carp-portal | The repository's existence changes CARP's "build everything yourself" characterization, but its maturity was not assessed this pass — treating it as equivalent to a mature commercial dashboard without checking would overstate CARP's out-of-the-box researcher tooling |

---
