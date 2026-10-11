# Module 1, Working Inventory and Scope Decisions

This file is the Phase 1 output: the full inventory of candidate technologies, which were profiled in this research phase, which were deliberately deferred, and why. Per the operating rules, uncertain inclusion decisions are recorded rather than silently made.

**Status of this file:** written as the Phase 1 inventory on 2026-08-21 and **brought in line with the current profiles and the rebuilt `../comparison-matrix.md` on 2026-10-10** (Last verified: 2026-08-21; updated 2026-10-10). Several candidates first listed here as deferred have since been profiled or desk-checked; their rows now point to where that work lives. The entries still marked **Not researched** were identified during discovery but have not been researched, and nothing in those rows should be treated as verified. The historical scope reasoning below is kept as written.

---

## Profiled (14 profile files plus this inventory)

The rationale column says why each was included. It is not a ranking; Table 10 of `../comparison-matrix.md` holds the current differentiators and limitations, and where this table and a profile disagree, the profile wins.

| Ecosystem | Profile | Rationale for inclusion |
|---|---|---|
| Apple Watch / HealthKit / SensorKit | `apple-watch-healthkit.md` | Largest installed base; no vendor in the HealthKit data path; SensorKit research signals for approved studies; named in scope |
| Fitbit / Google | `fitbit-google.md` | Deepest validation literature and the *All of Us* dataset; named in scope; legacy API off 30 October 2026 and Google Health API not onboarding new projects (as of 2026-10-10) make it time-critical |
| Garmin | `garmin.md` | Weeks of battery, no subscription, Enhanced BBI; named in scope |
| Oura | `oura.md` | Highest four-stage kappa in Robbins 2024 (0.65, but Oura-funded) and best resting HR and HRV agreement in Dial 2025; independent PSG results are mixed and Oura was not in Schyvens 2025; named in scope |
| WHOOP | `whoop.md` | Best deep-sleep (N3) accuracy in Schyvens 2025 (69.63%), but fourth of six on overall kappa (0.37); named in scope |
| Samsung | `samsung.md` | Raw PPG, ECG, accelerometer, IBI and (Galaxy Watch8 and later) raw EDA from a mainstream watch via the Health Sensor SDK. One of several raw-signal routes in this module, not the only one (see Table 3 of the matrix); named in scope |
| Polar | `polar.md` | Free, source-available raw-signal SDK (Polar limited licence); field-standard H10; named in scope |
| Withings | `withings.md` | Cellular/phone-free collection (Ametris also offers a cellular hub); BP and body composition; named in scope |
| Empatica | `empatica.md` | Raw wrist EDA with an FDA-cleared EDA parameter; FDA-cleared platform. One of three raw EDA routes in this module, with Samsung Galaxy Watch8 and the Verily Study Watch (C); named in scope |
| Ametris (formerly ActiGraph) | `ametris-actigraph.md` | Reference standard for research accelerometry; named in scope |
| Axivity (AX3/AX6) + GENEActiv | `axivity-geneactiv.md` | Open research-grade accelerometry behind UK Biobank, Whitehall II, Fenland, Pelotas; added under the "not a closed list" clause |
| Movesense | `movesense.md` | Open sensor platform with custom firmware, single-lead ECG and a high-rate IMU; added under the "not a closed list" clause (formerly deferred, below) |
| Ultrahuman, Biostrap (now Sensor Bio), Verily Study Watch; RingConn, Circular and Amazfit / Zepp desk check | `emerging-platforms.md` | Close the discovery gap recorded in the first pass: a ring with a developer PPG stream, a research-repositioned raw-PPG platform, a research-only watch, and a data-access check of three further ring and watch vendors (formerly deferred, below) |
| Data intermediaries (cross-cutting) | `data-intermediaries.md` | Fitabase, Labfront, Fitrockr, unified APIs and open datasets, not device ecosystems, but they determine what a study can actually access |

---

## Deferred, research-grade accelerometry alternatives

Axivity and GENEActiv, the two most important alternatives, **were profiled** (`axivity-geneactiv.md`). The remaining candidates below were not (still true as of 2026-10-10).

| Candidate | Why it matters | Status |
|---|---|---|
| **movisens** (Move 4, EcgMove, EdaMove) | German research-instrument manufacturer combining accelerometry with ECG and EDA, plus a companion EMA platform (movisensXS). Potentially a direct Empatica alternative with an integrated survey layer. | **Not researched.** High priority, the EMA integration makes it distinctive. |
| **Fibion** | Thigh-worn accelerometry focused on sedentary behaviour. Note: Fibion's competitor-pricing articles were used as a (clearly labelled) secondary source in the Ametris profile, so the company is already in this knowledge base's source graph. | **Not researched.** |
| **Shimmer** (Shimmer3, Verisense) | Modular research sensor platform with configurable raw multimodal capture (ECG, EMG, GSR, IMU); Verisense targets clinical trials. | **Not researched.** |
| **PAMSys / activPAL** | activPAL is the accepted reference for **posture classification** (sitting/standing/stepping), which no other device here does well. | **Not researched.** Relevant for sedentary behaviour research specifically. |

---

## Deferred, other consumer and prosumer wearables

Rows updated 2026-10-10. The "Why it matters" text is the original 2026-08-21 discovery note.

| Candidate | Why it matters | Status |
|---|---|---|
| **Movesense** (Movesense Ltd; independent of Suunto since October 2021) | Open developer platform with programmable sensor modules, potentially a Polar-like raw-access story with more extensibility. | **Profiled:** `movesense.md`. |
| **Biostrap** | Positions explicitly toward research with raw PPG access claims. | **Profiled:** `emerging-platforms.md` (now Sensor Bio). Raw-data claims remain vendor statements (Corroborated at most). |
| **Ultrahuman Ring** | Oura competitor in the ring form factor with an API. | **Profiled:** `emerging-platforms.md` (UltraSignal and Partner API). |
| **RingConn, Circular, other smart rings** | Growing category; relevant to any ring-based design as Oura alternatives. | **Desk-checked 2026-10-09:** `emerging-platforms.md`. No research API found for RingConn or Circular. Samsung Galaxy Ring as a distinct research target is still not investigated in depth, but Samsung's docs confirm it has only a processed route through the phone-side Data SDK and no raw route (`../../facts/samsung.yaml`, 2026-10-11). |
| **Amazfit / Zepp Health** | Low-cost wearables with an open API; potentially relevant for large low-budget cohorts. | **Desk-checked 2026-10-09, partnerships re-checked 2026-10-10:** `emerging-platforms.md`. On-device Zepp OS sensor API only; no research cloud API found. |
| **Verily Study Watch** | Purpose-built research watch used in the Project Baseline studies. | **Profiled:** `emerging-platforms.md`. Enterprise only; current status still **Unclear** there. |
| **Muse** (InteraXon) | Consumer EEG headband; used in sleep and meditation research. Arguably a different modality rather than a wearable ecosystem competitor. | **Not researched.** Deferred as a distinct modality (see `emerging-platforms.md`, "Not investigated"). |
| **Dreem / Beacon Biosignals** | Wearable EEG for sleep, the only route to genuine consumer-deployable sleep staging by EEG rather than by inference. Highly relevant given how poorly every device in this module stages sleep. | **Not researched.** Deferred as a distinct modality. High priority for sleep research questions. |

---

## Profiled as a cross-cutting file, data intermediaries

A category that does not appear in the CLAUDE.md scope list but that materially changes the answer to "what can researchers actually access." **Profiled in `data-intermediaries.md`** rather than deferred, covering three sub-categories: research operations platforms (Fitabase, MyDataHelps), unified wearable APIs, and open datasets (All of Us Fitbit, UK Biobank accelerometry).

Vendors covered there, at varying (mostly Reported) confidence:

| Vendor | Note |
|---|---|
| **Terra API** | Described in secondary sources as a unified API across many wearable brands. |
| **Validic** | Published a Fitbit-to-Google-Health-API developer transition guide (used as a corroborating source in the Fitbit profile). Long-established in healthcare device connectivity. |
| **Thryve** | Published analysis of the Fitbit API deprecation (used as a corroborating source). |
| **Sahha** | Published analysis of the Fitbit API sunset (used as a corroborating source). |
| **Rook** | Named in discovery. |
| **Open Wearables** | Open-source unified wearable API; secondary sources indicate Oura and WHOOP integrations as of 2026, plus an MCP server for LLM access. |
| **Fitabase** | Already covered within the Fitbit and Garmin profiles; it is a research-specific instance of this category. |

**Remaining gap:** none of the unified-API vendors was researched to primary-documentation depth. They are characterised from vendor marketing and secondary sources and are marked Reported throughout.

---

## Explicitly out of scope for Module 1

| Category | Reason |
|---|---|
| Continuous glucose monitors (Dexcom, Abbott Libre) | Connected medical devices, belongs to a future module per CLAUDE.md's Future Modules list. Note that they are increasingly deployed *alongside* wearables in metabolic research, so a cross-reference will eventually be needed. |
| Blood pressure cuffs, spirometers, ECG patches as standalone products | Connected medical devices module. Partially touched where they are part of a wearable platform (Withings BPM, Ametris third-party sensor support). |
| Smartphone-based passive sensing | **This is Module 2.** Deliberately excluded here. |
| Implantables and prescription-only monitors | Out of scope. |
| Smart clothing / textile sensors | Not currently a significant research category; revisit if it matures. |

---

## Scope decisions made during this phase

1. **Apple, Samsung, and Polar were treated as ecosystems, not devices.** Each has multiple access surfaces with radically different capabilities (e.g. Apple's HealthKit vs SensorKit; Polar's BLE SDK vs AccessLink). Profiling only the headline consumer API would have been actively misleading.

2. **The Fitbit and Google Health API were profiled as one entity** rather than split. They are the same data, mid-migration; splitting them would have created two half-accurate profiles.

3. **ActiGraph was profiled under its current name, Ametris**, with the legacy name retained prominently in the filename, title, and headings, because essentially all existing literature and all researcher familiarity attaches to "ActiGraph."

4. **Middleware/aggregators were identified but not profiled**, on the grounds that Phase 1 scope was defined around device ecosystems. Flagged above as a recommended addition. *(Later reversed: they were profiled in `data-intermediaries.md`; see the section above.)*

5. **Axivity and GENEActiv were added to scope** despite not appearing in CLAUDE.md's starting list, under its explicit "starting point, not a closed list" clause. They underpin UK Biobank and comparable cohorts and set the openness and price benchmark for the whole module. **movisens, Shimmer, activPAL, and Fibion remain unprofiled**, the largest remaining device gap.

7. **Two files in this module (`axivity-geneactiv.md`, `data-intermediaries.md`) were produced during an interrupted segment of the research session.** Their central factual anchor (the UK Biobank AX3 configuration from Doherty et al. 2017) was independently re-verified against the primary source; the remainder was reviewed for internal consistency but not re-derived claim by claim. Flagged in `shared/research-log.md`.

6. **Validation evidence was scoped to decision-relevant findings**, per CLAUDE.md's instruction not to exhaustively review every validation paper. Two recent multi-device PSG comparisons and one major systematic review were used as the backbone, with the funding source noted where relevant.
