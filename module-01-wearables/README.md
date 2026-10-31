# Module 1, Wearables

**Status:** initial research phase complete (2026-08-21); every device profile corrected and
re-verified against primary sources after the independent review of 2026-10-10 (commit c774edb);
comparison matrix, atlas and this README **rebuilt 2026-10-10 from the profiles**; matrix and README
cells for the eight batch-1 vendors corrected against the fact records in `../facts/` on 2026-10-11.
**Last verified:** 2026-10-11.
**Central question:** *What can researchers actually collect, access, export, and use from each
wearable ecosystem, under what conditions, and at what cost?*

---

## Contents

| File | Purpose |
|---|---|
| `comparison-matrix.md` | Thirteen cross-platform tables, rebuilt 2026-10-10 from the profiles: access model, sensors, **raw data availability**, API characteristics, study operations, participant burden, cost, compliance, evidence, differentiators and limitations, study-operations platforms, choosing by research question, and **research programs and academic access** (Table 13). Opens with a list of dated items |
| `wearable-data-atlas.html` | Published HTML view of Tables 1 to 12 of the matrix; resync whenever the matrix changes |
| `validation-evidence.md` | Full extraction from the primary validation literature: per-stage tables, ICCs, biases, conflicts of interest, and what the evidence base does not contain |
| `research-library-wearables.md` | ~90-paper sponsorship and COI bibliography (Tier A/B/C) for Oura, WHOOP and Apple Watch |
| `literature-library.md` | OA-status index and local PDF store for every individually named paper in `research-library-wearables.md`; 67 PDFs stored under `literature/<device-slug>/` as of 2026-10-10 |
| `sources.md` | Consolidated source register with type, retrieval method, date accessed, and what each source establishes |
| `profiles/` | One structured profile per ecosystem; **the source of truth for every summary file** |
| `../shared/terminology.md` | Definitions used consistently across profiles |
| `../shared/research-log.md` | Session log, decisions, and what could not be retrieved |
| `../shared/unresolved-questions.md` | Questions requiring direct vendor contact, with contacts |

### Profiles

**Consumer ecosystems**
- [`apple-watch-healthkit.md`](profiles/apple-watch-healthkit.md): Apple Watch, HealthKit, SensorKit (incl. PPG and ECG samples, iOS 17.4+), ResearchKit
- [`fitbit-google.md`](profiles/fitbit-google.md): Fitbit, Google Health API, Health Research Policy, Health Connect, Fitabase, *All of Us*
- [`garmin.md`](profiles/garmin.md): Health API, Health SDK (Standard and Companion), paused developer programme
- [`oura.md`](profiles/oura.md): Oura Ring Gen3, 4 and 5, API v2, API and MCP Agreement, Oura for Organizations research offering
- [`whoop.md`](profiles/whoop.md): WHOOP 4.0, 5.0 / MG, API v2, member tiers, API Terms of Use, WHOOP Unite
- [`samsung.md`](profiles/samsung.md): Galaxy Watch and Ring, Samsung Health Sensor SDK (formerly Privileged Health SDK), Research Stack
- [`polar.md`](profiles/polar.md): H10, Verity Sense, Polar 360, BLE SDK (source-available, Polar limited licence), AccessLink
- [`withings.md`](profiles/withings.md): ScanWatch line, API plans and Withings+, Advanced Research API, Health Solutions

**Open / programmable sensor platforms**
- [`polar.md`](profiles/polar.md): see above; H10 and Verity Sense are research instruments
- [`movesense.md`](profiles/movesense.md): Movesense MD / Flash / HR2, custom firmware, 512 Hz ECG, high-rate IMU (maximum a vendor conflict, 416 to 1666 Hz), Academic Program

**Research- and medical-grade**
- [`empatica.md`](profiles/empatica.md): EmbracePlus, EmbraceMini, Care Portal, academic plan
- [`ametris-actigraph.md`](profiles/ametris-actigraph.md): ActiGraph, now Ametris, now part of Signant Health; CentrePoint API
- [`axivity-geneactiv.md`](profiles/axivity-geneactiv.md): AX3/AX6, GENEActiv, open toolchain; Activinsights cloud option

**Emerging and specialist**
- [`emerging-platforms.md`](profiles/emerging-platforms.md): Ultrahuman UltraSignal and Partner API, Biostrap (now Sensor Bio), Verily Study Watch and the March 2026 Verily and Samsung collaboration, plus a data-access check of RingConn, Circular and Amazfit / Zepp

**Cross-cutting**
- [`data-intermediaries.md`](profiles/data-intermediaries.md): Labfront and Fitrockr (published pricing), Fitabase, unified APIs (Terra, Validic, Thryve, Rook, Sahha, Open Wearables), open datasets

Coverage: 12 device profiles (Apple, Fitbit/Google, Garmin, Oura, WHOOP, Samsung, Polar,
Withings, Movesense, Empatica, Ametris, and Axivity with GENEActiv in one file); short entries for
Ultrahuman, Biostrap/Sensor Bio and Verily, plus a data-access check of RingConn, Circular and
Amazfit / Zepp; and a cross-cutting file on intermediaries and open datasets.

---

## What changed on 2026-10-10

The independent review (`../shared/reviews/2026-10-10-independent-review.md`) found that the
comparison matrix had last been rebuilt on 2026-08-24, that only about half its sampled cells could
be confirmed, and that the atlas, this README and the explorer disagreed with the profiles. The
profiles were corrected first; the summaries were then rebuilt from them. The changes that matter
most for a study:

| Earlier summary said | Now |
|---|---|
| Fitbit legacy API "turns down in September 2026"; Google Health API open to new integrations | Legacy support ended 30 Sep 2026 and the API is **turned off 2 Nov 2026** (moved from 30 Oct on 23 Oct); Google was **not onboarding new Google Health API projects** on 2026-10-10 and is **apparently open again** by 2026-10-19 (Corroborated), with restricted-scope review |
| Garmin confirms applications within two business days | **New access requests paused since spring 2026** (Corroborated); Garmin's FAQ wording is stale |
| Empatica is the only raw EDA source | **Samsung Galaxy Watch8 and later expose raw EDA at 1 Hz** through the Health Sensor SDK; Verily also records EDA |
| Samsung raw PPG rate undocumented | PPG 25 Hz continuous and 100 Hz on demand; ECG 500 Hz; accelerometer 25 Hz |
| Apple: no raw PPG or accelerometer | SensorKit exposes PPG and ECG samples (iOS 17.4+) and accelerometer (iOS 14+) to Apple-approved studies; HealthKit still does not. Core Motion `CMSensorRecorder` gives 50 Hz accelerometer without an entitlement (12 h per call, 3-day retention) |
| WHOOP "MG ECG / BP claimed" | ECG feature FDA-cleared (K243236); Blood Pressure Insights not cleared (warning letter 2025, close-out 2026) |
| WHOOP terms bar permanent copies | They also bar AI/ML training, and new apps start at a 10-member Sandbox tier |
| Oura: no research console; rate limit 5,000 per 5 minutes | Oura for Organizations has a research offering; the 5,000 requests per 5 minutes figure is confirmed in the current docs (OpenAPI 1.41 FAQ); the API Agreement limits retention and bars AI training |
| Withings compliance Unclear; API reference behind login | Vendor states HIPAA and GDPR; ISO 27001:2022, ISO 27701 and HDS v2 certificates (AFNOR) were read; API reference is public; free plan needs **Withings+ from 12 Oct 2026** for new accounts |
| Labfront is the only research platform publishing prices | Fitrockr also publishes prices, and so do Terra and Thryve |
| Axivity accelerometer to 100 Hz; price by quote | AX3 12.5 to 3,200 Hz; AX3 from £139 and AX6 from £199, ex VAT, sold online |
| Movesense has no independent validation; price not public | Four small independent lab validations exist; MD €349 ex VAT; free sensors through an Academic Program |
| Enhanced BBI is nocturnal only | Garmin's 2023 note says it is measured during sleep, and the API route (Fitabase) captures it during sleep, but the Health SDK lists it for real-time streaming; Fitabase also has an SDK route via its Engage app, daytime coverage not stated |
| Dial 2025: WHOOP worst of five on resting HR and HRV | WHOOP was behind both Oura generations but ahead of the Polar watch (and Garmin on HRV) |

---

## The findings that should change how you plan a study

### 1. Sensor presence is nearly uninformative. Data access is what matters.

**Raw signal documented:** Polar (H10 ECG 130 Hz; Verity Sense PPG to 176 Hz at 22-bit; IMU to
416 Hz; free SDK under Polar's limited licence, no approval), Movesense (ECG to 512 Hz, IMU to at
least 416 Hz with vendor sources giving up to 1666 Hz, custom firmware),
Samsung (PPG green, IR and red, ECG 500 Hz, IBI, accelerometer 25 Hz, **EDA 1 Hz on Watch8**),
Axivity (accelerometry to 3,200 Hz), Ametris (accelerometry to 256 Hz; LEAP PPG under contract),
Withings (ScanWatch accelerometry and three-wavelength PPG at about 24.8 Hz, by contract),
Empatica (raw EDA, PPG and accelerometry; all rates published per sensor mode), Apple through
SensorKit (plus 50 Hz accelerometry through Core Motion, no entitlement needed),
Garmin through the enterprise Health SDK only. Ultrahuman (raw ring PPG, typically 50 Hz, own
Developer Mode recordings only, Verified), Sensor Bio V2 (raw PPG, IBI and accelerometer to 100 Hz,
vendor specification) and Verily (Corroborated; device program wound down in 2025) rest on vendor or
Corroborated statements.

**No raw signal through any documented route:** Fitbit/Google (except per-reading ECG voltage in
the Google Health API), **Oura**, **WHOOP**.

The highest documented raw rates come from open, modestly priced sensors (Axivity, Movesense,
Polar), not from the clinical-trial vendors; Samsung is the consumer exception. See
`comparison-matrix.md` Table 3.

### 2. Deep sleep and REM minutes are not measurable with consumer wearables.

Robbins 2024 ICCs for stage summaries: **deep sleep, Oura 0.32, Fitbit 0.36, Apple 0.13; REM, Oura
0.27, Fitbit 0.13, Apple 0.37.** All poor. Total sleep time and sleep efficiency (ICC 0.74 for Oura,
0.85 for Apple, 0.56 for Fitbit) are the defensible stage-derived endpoints. Every device in
Schyvens 2025 underestimated WASO by 12 to 48 minutes. Robbins was Oura-funded; independent PSG
results for Oura are mixed (Miller 2022, Lee 2023, Searles 2026). See `validation-evidence.md`.

### 3. Garmin is closed to new studies right now, and new Fitbit access is slow.

- **Fitbit / Google:** the legacy Fitbit Web API is turned off on **2 November 2026** (Google moved it from 30 October on 23 October). Google said on
  2026-10-10 it was **not onboarding new Google Health API projects**; by 2026-10-19 that notice was
  gone, with no announcement, so the API is **apparently open to new projects again** (Corroborated,
  2026-10-21). A new study can apparently open its own project, but every scope is Restricted, so
  approval needs Google's privacy and security review. Above 100 users it also needs verification and
  a CASA assessment ($500 to $4,500). Other routes are Fitabase (whether it can add new studies is
  not stated), on-device collection through Apple Health or Health Connect (Corroborated),
  participant self-export, or the *All of Us* dataset. Thryve and Validic need the study's own Google Cloud
  project, verified app and CASA; Terra says it manages the Google Health credentials, with its
  review and CASA status not stated.
- **Garmin:** new Connect Developer Program access requests have been **paused since spring 2026**
  (Corroborated), and queued requests are also on hold. Labfront, Fitabase and Fitrockr already hold
  access. Terra no longer does for new customers (customer's own Garmin credentials since
  mid-October 2026).

### 4. Vendor terms now constrain what a study can keep.

- **WHOOP** (terms effective 6 October 2026): no permanent copies of WHOOP data and no AI/ML training
  or testing on it, unless authorised by the WHOOP data owner or by applicable law; no third-party
  transfer; no research carve-out. New apps start at a 10-member Sandbox tier.
- **Oura** (API and MCP Agreement, effective 8 June 2026): keep API data only as long as strictly
  necessary, delete within 72 hours of a request or subscription cancellation, no AI/ML training and
  no evaluating or prompting AI models with API data outside the MCP Server. Participant consent does
  not lift these, and there is no research carve-out.
- **Withings:** from **12 October 2026**, participants with new Withings accounts need a paid
  Withings+ membership to share data with a free-plan app, including via Apple Health or Google
  Health.

Resolve these in writing with the vendor and institutional counsel before a protocol depends on them.
Polar's BLE SDK, Movesense, Axivity, Samsung's Sensor SDK and Apple's HealthKit have no vendor in
the data path and no such terms. Samsung's licence does let it collect information about the service
and its use.

### 5. Study operations is still the systematic gap, and some of it now has a price.

Apple, Fitbit/Google, Garmin and WHOOP provide no participant management. Apple's Study App
Template, free to approved Investigator Support Program applicants, is the nearest thing. WHOOP
reportedly sells research partners a paid web app for group downloads. Empatica (Care Portal),
Ametris (CentrePoint) and Samsung (Research Stack, status unclear, no code since October 2024) do
natively. Oura sells a research offering (Enterprise Platform, priced per Order). Published studies
since 2022 used a portal called "Oura Teams". **Labfront** (free 5-participant tier,
$500 or $1,250 a year, EMA at every tier) and **Fitrockr** (from €50 or €150 a month per device
licence, Reported; its help centre still says user-based) publish prices; Fitabase quotes per study. Table 13 of the matrix lists each vendor's
research programme, user caps, retention and AI-training terms, cost and status.

### 6. The cheapest good answers are still often not devices at all.

***All of Us*** holds Fitbit data from 59,000+ participants over 14 years, minute-level, 46% linked
to EHR and other data, with no exposure to the 2 November 2026 shutoff. **UK Biobank** holds raw
100 Hz wrist accelerometry from 100,000+ participants.

---

## What is actually gated

**Documentation is public for almost everything here.** Oura's, WHOOP's, Google's, Polar's,
Samsung's and Withings' API references were all read without an account (Withings' reference was
recorded as login-gated in August; it is public). Samsung's Sensor SDK is a public download;
partner approval is needed only to distribute an app.

**You can start today, without contacting the vendor, on:** Oura up to 10 users; WHOOP up to 10
members; Withings' free plan up to 10 users (Withings+ costs apply from 12 October 2026); Polar and
Movesense with no registration; Samsung in developer mode for testing; Labfront free for 5
participants; Empatica's academic plan by store purchase; Axivity by buying a device.

**You cannot start today on:** a new direct Garmin integration (applications paused). A new direct
Fitbit/Google project apparently can be started again (2026-10-21), but approval waits on Google's
restricted-scope review and, above 100 users, verification and CASA.

**What genuinely requires contact:** scale thresholds (Oura above 10 users, WHOOP tier upgrades,
Withings free plan above 10 users), and commercial terms nobody publishes: Garmin's Enhanced BBI and
SDK licences, Withings' research and paid plans, Fitabase's fees, Ametris's prices, Oura's research
offering, and BAA availability almost everywhere. See `../shared/unresolved-questions.md`.

---

## Known gaps

- **Current hardware is largely unvalidated:** Oura Ring 5, WHOOP 5.0/MG, Apple Series 12 and Fitbit
  Air postdate every PSG study here; no Oura versus WHOOP PSG comparison exists on current hardware.
- **Unpublished sampling rates:** Apple SensorKit PPG, Garmin Health SDK accelerometer (integrators
  report 25 Hz), Ultrahuman daily-metric series and non-PPG sensors (its raw PPG, typically 50 Hz, is
  published), Galaxy Watch streams through Verily Viewpoint, Zepp OS accelerometer modes, and RingConn's
  consumer schedule. Sensor Bio V2 and Verily Study Watch rates are now published.
- **Compliance rests on vendor statements:** only Empatica's ISO 27001 certificate (TÜV Rheinland
  01 153 2117571), Withings' AFNOR certificates and Ametris's ISO 27001:2022 certificate (Ignyte
  Assurance IA391-260410-001) were read, all as vendor-hosted PDFs; none for other vendors.
  Activinsights' only published ISO 27001 certificate expired on 31 October 2025. BAA availability is unpublished for most.
- **Live conflicts in the sources:** Ametris's ActiLife Data Vault allowance (4 GB in the manual,
  20 GB on the product page); Movesense's maximum IMU rate (416, 833 or 1666 Hz by source); Axivity
  AX3 and GENEActiv recording durations (each vendor's own documents disagree); the
  Withings+ US annual price ($99.50 or $99.95); Withings' inactive-account closure (3, 5 or 10 years);
  whether HealthKit's per-recording ECG voltage counts as raw (Apple's own pages disagree); Garmin's
  FAQ still quoting two-business-day approval while applications are paused; Sensor Bio's 100 Hz
  specification against a 15,000 samples per second press claim, and whether its raw export needs an
  enterprise-tier account; Circular's Ring 2 price ($349 or $299) and its blood pressure and glucose
  claims; the Verily Study Watch's status.
- **Not assessed:** movisens, Shimmer, activPAL, Fibion (research-grade alternatives); Galaxy Ring as
  a research target (Samsung's docs confirm only a processed route through the Data SDK, no raw
  route); EEG wearables; CGM.
- **Emerging entries** (Ultrahuman, Biostrap/Sensor Bio, Verily) rest partly on vendor statements, and
  the Verily Study Watch's status is a conflict (Reported): press reports Verily wound down its device
  program in August 2025, while Verily's trust page still lists Study Watch & Hub.

---

## Scope decisions

### Included beyond the starting list in `CLAUDE.md`

| Addition | Rationale |
|---|---|
| **Axivity AX3/AX6 and GENEActiv** | Underpin UK Biobank, Whitehall II, Fenland, Pelotas. Excluding them would misrepresent research-grade accelerometry as ActiGraph-only and would omit the open-hardware option |
| **Movesense** | A programmable research sensor with high ECG and IMU rates; missed in the first pass |
| **Fitabase, Labfront, Fitrockr and unified APIs** | Not wearables, but the layer through which most Fitbit and Garmin research runs. Currently the main route to new Garmin data, and one of two routes to new Fitbit data (the other is on-device via Apple Health or Health Connect) |
| **Open datasets (*All of Us*, UK Biobank)** | A legitimate and often better alternative to collecting new wearable data |
| **Health Connect** | The Android analogue to HealthKit; covered inside the Fitbit/Google profile |
| **Google Health API** | Not a separate ecosystem, but a discontinuity large enough to structure the Fitbit profile around |

### Deliberately deferred

| Excluded | Reason |
|---|---|
| **CGM (Dexcom, Abbott)** | A distinct device class with its own regulatory and access model. Belongs in a connected-medical-devices module |
| **EEG wearables (Muse, Dreem)** | Distinct modality; would need its own validation frame |
| **Smart clothing and patches (Hexoskin, VitalConnect, iRhythm)** | Distinct class, better suited to a remote patient monitoring module |
| **movisens, Shimmer, activPAL, Fibion** | Research-grade alternatives not yet profiled; see `profiles/_inventory-and-scope-decisions.md` |
| **Blood pressure and scale devices generally** | Covered only where they sit inside a profiled ecosystem (Withings, Garmin Index) |

RingConn, Circular and Amazfit / Zepp were checked for research data access on 2026-10-09 and
recorded in `profiles/emerging-platforms.md`; none publishes a self-serve research API. Circular
offers raw signal under research agreements and an API and SDK to selected business projects by
contact, and Zepp documents a legacy partner cloud API whose open status is unclear (corrected
2026-10-22 from the fact records).

### Inclusion judgements worth flagging

- **Polar** is listed in `CLAUDE.md` as a consumer wearable, but its research value is mostly in the
  sensor line (H10, Verity Sense), not the watches. The profile is weighted accordingly.
- **Withings** is arguably not a wearable company; the profile treats its non-wearable devices as
  first-class.
- **ActiGraph** is profiled under its current name, **Ametris**, with the rebrand and the Signant
  Health acquisition treated as decision-relevant facts.

---

## Confidence conventions used throughout

| Label | Meaning |
|---|---|
| **Verified** | Read directly from a current authoritative primary source |
| **Corroborated** | Multiple credible sources agree, but not confirmed in current primary documentation |
| **Reported** | Found in a credible source, not independently confirmed. Vendor marketing claims default here |
| **Unclear** | Evidence incomplete, conflicting, or absent. **Not an invitation to infer** |

Where two sources conflict, both are recorded and the conflict is named. The five contradictions
open in August (Apple ECG access, Withings accelerometer rate, Polar H10 accelerometry, Samsung's
minimum watch, Empatica's biomarker count) were resolved or reconciled on 2026-10-09. The Apple ECG
question reopened on 2026-10-11 as a narrower conflict over the word "raw". The conflicts still open
are listed under Known gaps.

---

## Recommended next research steps

1. **Ask Google when it will resume onboarding Google Health API projects**, and whether an approved
   Health Research Application is exempt from the CASA assessment or the 100-user cap.
2. **Ask Garmin when Connect Developer Program applications reopen** and whether academic use counts
   as "commercial use" for the Enhanced BBI licence fee.
3. **Pilot Labfront's free tier with a Garmin device** (5 participants) to see what Enhanced BBI looks like in
   practice (Tester accelerometry is 25 Hz only; higher rates need Advanced).
4. **Get the WHOOP and Oura retention and AI-training questions answered in writing** before any
   protocol depends on either.
5. **Ask Oura** what its research offering costs, what its "raw data" export contains, and what its
   Research Agreement says on retention and AI use (the Enterprise route already differs, since
   extracted data is not deleted on withdrawal).
6. **Ask Withings** whether a research partner on the free plan is exempt from the Withings+
   requirement.
7. **Ask Empatica** whether an Enterprise-only mode backs the "up to 28 days" battery claim, and for
   its DPA and BAA position.
8. **Request quotes** where pricing is unpublished: Fitabase, Ametris/Signant, the Withings Advanced
   Research API, Oura for research, Empatica Enterprise (100-device minimum).
9. **Profile movisens, Shimmer and activPAL**, the largest remaining device gap.
10. **Watch for validation of current hardware** (Oura Ring 5, WHOOP 5.0/MG, Fitbit Air).

Do not begin Module 2 as a consequence of this file.
