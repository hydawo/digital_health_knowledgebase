# Module 1 — Wearables

**Status:** initial research phase complete; **second deep-research pass completed 2026-08-21** (papers read in full, documentation gaps closed, several first-pass findings corrected).
**Last verified:** 2026-08-21.
**Central question:** *What can researchers actually collect, access, export, and use from each
wearable ecosystem, under what conditions, and at what cost?*

---

## Contents

| File | Purpose |
|---|---|
| `comparison-matrix.md` | Ten cross-platform tables — access model, sensors, **raw data availability**, API characteristics, study operations, participant burden, cost, compliance, evidence, differentiators |
| `validation-evidence.md` | **Full extraction from the primary validation literature**, read in full — per-stage tables, ICCs, biases, conflicts of interest, and what the evidence base does not contain |
| `sources.md` | Consolidated source register with type, retrieval method, date accessed, and what each source establishes |
| `profiles/` | One structured profile per ecosystem |
| `../shared/terminology.md` | Definitions used consistently across profiles |
| `../shared/research-log.md` | Session log, decisions, and what could not be retrieved |
| `../shared/unresolved-questions.md` | Questions requiring direct vendor contact, with contacts |

### Profiles

**Consumer ecosystems**
- [`apple-watch-healthkit.md`](profiles/apple-watch-healthkit.md) — Apple Watch, HealthKit, SensorKit, ResearchKit
- [`fitbit-google.md`](profiles/fitbit-google.md) — Fitbit, Google Health API, Health Connect, Fitabase, *All of Us*
- [`garmin.md`](profiles/garmin.md) — Health API, Health SDK (Standard and Companion)
- [`oura.md`](profiles/oura.md) — Oura Ring 4, API v2
- [`whoop.md`](profiles/whoop.md) — WHOOP 5.0 / MG, API v2, WHOOP Unite
- [`samsung.md`](profiles/samsung.md) — Galaxy Watch/Ring, Privileged Health SDK, Research Stack
- [`polar.md`](profiles/polar.md) — H10, Verity Sense, open BLE SDK, AccessLink
- [`withings.md`](profiles/withings.md) — ScanWatch line, Advanced Research API, Health Solutions

**Open / programmable sensor platforms**
- [`polar.md`](profiles/polar.md) — see above; H10 and Verity Sense are research instruments
- [`movesense.md`](profiles/movesense.md) — Movesense MD / Flash / HR2, custom firmware, 512 Hz ECG, 1.6 kHz IMU

**Research- and medical-grade**
- [`empatica.md`](profiles/empatica.md) — EmbracePlus, Care Portal
- [`ametris-actigraph.md`](profiles/ametris-actigraph.md) — ActiGraph → Ametris → Signant Health
- [`axivity-geneactiv.md`](profiles/axivity-geneactiv.md) — AX3/AX6, GENEActiv, open toolchain

**Emerging and specialist**
- [`emerging-platforms.md`](profiles/emerging-platforms.md) — Ultrahuman UltraSignal, Biostrap, Verily Study Watch (incl. the March 2026 Verily–Samsung collaboration)

**Cross-cutting**
- [`data-intermediaries.md`](profiles/data-intermediaries.md) — **Labfront** (published pricing), Fitabase, unified APIs (Terra, Validic, Thryve, Rook, Sahha, Open Wearables), open datasets

---

## What changed in the second pass

Four first-pass conclusions were wrong or materially incomplete. They are corrected in place, and
named here because a knowledge base that quietly fixes its own errors is not auditable.

| First pass said | Corrected |
|---|---|
| "WHOOP had the best independently measured deep-sleep sensitivity" — presented as a headline strength | WHOOP had the best deep-sleep **accuracy** (69.6%) but only the **fourth-best overall agreement (κ=0.37)** of six devices. Apple Watch led at κ=0.53. Quoting one without the other is misleading |
| Robbins 2024 flagged only as "vendor-promoted" | **The study was funded by Oura, and the lead author sits on Oura's Medical Advisory Board and takes consulting fees from Oura.** A declared conflict, not just promotion |
| Garmin BBI framed as SDK-only, requiring a custom app | **Enhanced BBI is available through the cloud Health API and through Fitabase/Labfront via ordinary Garmin Connect OAuth** — no custom app. But it is **nocturnal only** |
| Empatica, Polar sampling rates and several prices listed as "non-public" or "unclear" | **Empatica's academic pricing is published** ($1,749.60 / device / 3 yr). **Polar's exact per-stream rates are published** in the SDK repo. **Labfront publishes full pricing.** These were retrieval failures, not vendor secrecy |

Also added: **Movesense**, **Ultrahuman**, **Biostrap**, **Verily**, **Labfront** — five platforms
the first pass missed, three of which expose raw signal.

---

## The findings that should change how you plan a study

### 1. Sensor presence is nearly uninformative. Data access is everything — and more platforms give it than the first pass found.

**Raw signal available:** Polar (ECG 130 Hz, PPG 28–176 Hz at 22-bit, IMU to 416 Hz — **for ~$95,
open SDK, no approval**), Movesense (ECG to **512 Hz**, IMU to **1.6 kHz**, custom firmware),
Samsung (raw PPG incl. IR/Red, raw ECG, IBI, 25 Hz accel), Garmin (raw accel; BBI with per-beat
confidence), Withings (raw accel + 3-wavelength PPG, heavily conditioned), Empatica (**the only raw
EDA**), Ultrahuman (**the only ring with raw PPG**), Biostrap, Verily, Ametris, Axivity/GENEActiv.

**No raw signal at any price:** Apple (except discrete ECG voltage), Fitbit/Google, **Oura**,
**WHOOP**.

**The highest sampling rates in this module come from the cheapest, most open vendors.** Polar and
Movesense beat every major consumer platform *and* every clinical-trial vendor on raw specification.

### 2. Deep sleep and REM minutes are not measurable with consumer wearables. Full stop.

This is the finding most likely to be ignored, so it is stated bluntly. Robbins 2024 reports
intraclass correlation coefficients for stage summaries: **deep sleep — Oura 0.32, Fitbit 0.36,
Apple 0.13; REM — Oura 0.27, Fitbit 0.13, Apple 0.37.** All poor. Epoch-level kappa looks
respectable; between-person reliability of the numbers a study would actually analyse does not.

Total sleep time and sleep efficiency (ICC 0.74–0.85) are the defensible stage-derived endpoints.
Every device also underestimates WASO by 12–48 minutes, so fragmentation endpoints are systematically
flattered. See `validation-evidence.md`.

### 3. Fitbit's migration is now a compliance problem, not just an engineering one.

The legacy API turns down in September 2026; the consumer app already became **Google Health** on
19 May 2026. Beyond forced re-consent, three new gates emerged on close reading:

- **Unverified apps are capped at 100 users.**
- Verification requires a **third-party CASA security assessment: $500–$4,500, 2–6 weeks**, and
  **annually** if a third-party server is involved — which describes every research pipeline.
- In-app disclosure requirements apply.

And the intraday question resolved **leaning negative**: Heart Rate is documented as a *Sample* type
with **no stated sampling interval**, HRV/SpO2/RHR appear as **Daily Aggregates**, and there is no
Intraday endpoint family. Nobody should assume minute-level heart rate survives.

### 4. Study operations is the systematic gap — and there is now a priced answer for Garmin.

Apple, Fitbit/Google, Garmin, Oura and WHOOP provide **no** participant management, adherence
monitoring, or wear-time tracking. Only Empatica, Ametris and Samsung's Research Stack do natively.

**Labfront** changes the arithmetic for Garmin studies: free 5-participant tier,
**$500/yr for 20 participants**, **$1,250/yr** for all integrations and high-resolution sampling,
**EMA included at every tier**, and a Garmin partnership that raises sensor resolution beyond stock.
It is the only research platform in Module 1 that publishes prices. Fitabase remains the only option
for Fitbit, at quote-only pricing.

### 5. The cheapest good answers are still often not devices at all.

***All of Us*** holds Fitbit data from 59,000+ participants over 14 years, minute-level, 46% linked
to EHR and genomics — no procurement, no API, no exposure to the September 2026 turndown.
**UK Biobank** holds raw 100 Hz wrist accelerometry from 100,000+ participants.

### 6. WHOOP's contractual position remains the sharpest constraint in the module.

Its API terms bar building databases or permanent copies, bar third-party transfer even with
consent, and disclaim HIPAA. Read literally, incompatible with retaining an analysis dataset. There
is a written-agreement carve-out; obtain it before writing a protocol.

---

## What is actually gated — a correction of emphasis

The first pass implied more vendor gatekeeping than exists. To be precise:

**Documentation is public for almost everything here.** Oura's, WHOOP's, Fitbit/Google's, Polar's
and Samsung's references were all read directly, without an account. Only **Garmin** (portal login
for field schemas), **Withings** (Partner Hub) and **Samsung's Privileged SDK download** sit behind
a wall.

**You can start today, free, on most of them:** Oura up to 10 users; Google Health up to 100 users;
Polar and Movesense with no registration at all; WHOOP freely, subject to its terms; Labfront free
for 5 participants; Axivity by buying a device.

**What genuinely requires contact is (a) scale thresholds** — Oura above 10 users, Google Health
above 100 — **and (b) commercial terms nobody publishes**: Garmin's SDK licence, the Withings
research contract, Fitabase's fees, Ametris's price list, and BAA availability. Those block
*scaling* and *budgeting*, not *starting*. See `../shared/unresolved-questions.md`.

## Scope decisions

### Included beyond the starting list in `CLAUDE.md`

| Addition | Rationale |
|---|---|
| **Axivity AX3/AX6 and GENEActiv** | Underpin UK Biobank, Whitehall II, Fenland, Pelotas. Excluding them would misrepresent research-grade accelerometry as ActiGraph-only and would omit the only genuinely open-hardware option |
| **Fitabase and unified APIs** | Not wearables, but the layer through which most Fitbit/Garmin research actually runs. Omitting them would misdescribe practice |
| **Open datasets (*All of Us*, UK Biobank)** | A legitimate and often superior alternative to collecting new wearable data |
| **Health Connect** | The Android analogue to HealthKit; covered inside the Fitbit/Google profile |
| **Google Health API** | Not a separate ecosystem, but a discontinuity large enough to structure the Fitbit profile around |

### Deliberately deferred

| Excluded | Reason |
|---|---|
| **CGM (Dexcom, Abbott)** | A distinct device class with its own regulatory and access model. Belongs in a "connected medical devices" module |
| **EEG wearables (Muse, Dreem)** | Distinct modality; would need its own validation frame |
| **Smart clothing / patches (Hexoskin, VitalConnect, iRhythm)** | Distinct class, better suited to a remote patient monitoring module |
| ~~**Verily Study Watch, Biostrap, Ultrahuman**~~ | **Now covered** in `profiles/emerging-platforms.md` (second pass) |
| ~~**Movesense**~~ | **Now covered** with a full profile — it should have been in the first pass |
| **Amazfit/Zepp, RingConn, Circular** | Still not assessed. Recorded in `profiles/emerging-platforms.md` and `../shared/unresolved-questions.md` as a remaining discovery gap |
| **Blood pressure and scale devices generally** | Covered only where they sit inside a profiled ecosystem (Withings, Garmin Index) |

### Inclusion judgements worth flagging

- **Polar** is listed in `CLAUDE.md` as a consumer wearable, but its research value is almost
  entirely in the sensor line (H10, Verity Sense), not the watches. The profile is weighted
  accordingly.
- **Withings** is arguably not a wearable company at all; the profile says so and treats the
  non-wearable devices as first-class.
- **ActiGraph** is profiled under its current name **Ametris**, with the rebrand and the Signant
  Health acquisition treated as decision-relevant facts rather than trivia.

---

## Confidence conventions used throughout

| Label | Meaning |
|---|---|
| **Verified** | Read directly from a current authoritative primary source during this session |
| **Corroborated** | Multiple credible sources agree, but not confirmed in current primary documentation |
| **Reported** | Found in a credible source, not independently confirmed. Vendor marketing claims default here |
| **Unclear** | Evidence incomplete, conflicting, or absent. **Not an invitation to infer** |

Where two sources conflict, both are recorded and the conflict is named. Five live contradictions
are open in this module: Apple's ECG access, Withings' accelerometer sampling rate, Polar's H10
accelerometer streaming, Samsung's minimum supported watch generation, and Empatica's biomarker
count. See `../shared/unresolved-questions.md`.

---

## Recommended next research steps

Ordered by value per unit of effort. Steps 1–3 need no vendor contact at all.

1. **Empirically test Google Health API heart rate density.** Register a Google Cloud project (free,
   up to 100 users unverified), authorise one account, pull a day of Heart Rate samples, and count
   them. This single test resolves the highest-value open question in the module and requires
   nobody's permission.
2. **Pilot Labfront's free tier with a Garmin device** (5 participants, all settings enabled). This
   empirically answers what Enhanced BBI data actually looks like, what resolution is obtainable,
   and whether the platform suits the protocol — at zero cost.
3. **Test the Oura API path you already have** against the documented scope list, and specifically
   establish the **temporal resolution of the `heartrate` endpoint** and whether Ring 5's Health
   Radar outputs appear at all. Both are open questions answerable from an existing integration.
4. **Ask Oura what approval above 10 users involves.** In-product, via the applications portal. This
   is the only true blocker for an Oura study of realistic size.
5. **Ask Google whether an academic study qualifies for the "internal use within an organization"
   verification exception.** The difference is free registration versus a recurring $500–$4,500 CASA
   assessment.
6. **Get the WHOOP written-retention question answered** before any protocol depends on WHOOP.
7. **Request quotes** where pricing genuinely is unpublished: Fitabase, Ametris/Signant, the Withings
   Advanced Research API, Movesense volume, Empatica Enterprise. Empatica academic and Labfront no
   longer need a quote.
8. **Resolve the remaining contradictions**: build a test app to read `HKElectrocardiogramQuery`
   voltage samples; ask Withings which accelerometer rate is correct; ask Samsung whether Watch4 or
   Watch5 is the true Research Stack minimum; ask Empatica which biomarkers the academic plan
   actually includes (11+, 18, or 100+).
9. **Look for independent validation of Movesense** — the specifications are the best in the module
   and the evidence base appears empty, which is worth confirming rather than assuming.
10. **Close the last discovery gaps**: Amazfit/Zepp, RingConn, Activinsights' production status, and
    whether Schyvens' WHOOP 4.0 result transfers to the 5.0 hardware.

Do not begin Module 2 as a consequence of this file.
