# Unresolved Questions

Questions that could not be reliably answered from available sources. Each names the organization
that can answer it and an official contact route where one exists.

**Last updated: 2026-08-21** (Module 1 second deep-research pass; several items resolved and struck through).

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
| 80 | **What are WHOOP 4.0's exact HRV CCC/MAPE figures in Dial et al. 2025** (*Physiological Reports* 13:e70527), and does that paper disclose any vendor funding? | Direct read of the paper — Wiley/PMC blocked WebFetch with 403/CAPTCHA in two separate passes | This is the only found Oura-vs-WHOOP head-to-head study; `validation-evidence.md` currently states no such study exists and needs correcting once the full text is read |
| 81 | Do the Miller et al. 2020 (*J Sports Sciences*, WHOOP validation) and Bellenger et al. 2022 (water polo HRV) papers disclose WHOOP funding? Both share an author cluster with a confirmed WHOOP-sponsored CQU position (Dean Miller) | Tandfonline / MDPI, direct read | If WHOOP-funded, these should move from the "independent" framing they're often cited with to Tier B |
| 82 | Does Oura's own research page currently say "170+" or "130+" peer-reviewed studies, and has that number changed over time? | ouraring.com/science-and-research, checked on different dates | A moving/inconsistent headline number is itself worth noting if confirmed |
| 83 | Full funding/COI text for five systematic reviews blocked by paywalls this pass: Khan et al. 2025 (Oura, *OTO Open*), Shahid et al. 2025 (Apple Watch AF, *JACC: Advances*), Choe & Kang 2025 (Apple Watch, *Physiological Measurement*), the Nova Southeastern AF-wearables review (PMC8752409), Khodr et al. (WHOOP, medRxiv preprint) | Direct read via institutional access | Each review's own reference list is a discovery mechanism for further papers not yet in `research-library-wearables.md`, and none of the five has been tier-classified with a Verified-level disclosure read |
