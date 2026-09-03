# Module 1, Working Inventory and Scope Decisions

This file is the Phase 1 output: the full inventory of candidate technologies, which were profiled in this research phase, which were deliberately deferred, and why. Per the operating rules, uncertain inclusion decisions are recorded rather than silently made.

**Status of this file:** the entries under "Deferred" were identified during discovery but **were not researched**. Nothing in those sections should be treated as verified. They exist so that a future session knows what is missing and does not have to rediscover it.

---

## Profiled in this phase (11 files, 12+ ecosystems)

| Ecosystem | Profile | Rationale for inclusion |
|---|---|---|
| Apple Watch / HealthKit / SensorKit | `apple-watch-healthkit.md` | Largest installed base; unique architecture; named in scope |
| Fitbit / Google | `fitbit-google.md` | Deepest research footprint; named in scope; API migration makes it time-critical |
| Garmin | `garmin.md` | Best battery life; no subscription; named in scope |
| Oura | `oura.md` | Best consumer sleep validation; named in scope |
| WHOOP | `whoop.md` | Best independent sleep-staging result; named in scope |
| Samsung | `samsung.md` | Only consumer vendor offering raw PPG/ECG/ACC; named in scope |
| Polar | `polar.md` | Free open-source raw-signal SDK; field-standard H10; named in scope |
| Withings | `withings.md` | Cellular/phone-free collection; BP and body composition; named in scope |
| Empatica | `empatica.md` | Only wrist EDA; FDA-cleared platform; named in scope |
| Ametris (formerly ActiGraph) | `ametris-actigraph.md` | Gold-standard research accelerometry; named in scope |
| Axivity (AX3/AX6) + GENEActiv | `axivity-geneactiv.md` | Open research-grade accelerometry behind UK Biobank, Whitehall II, Fenland, Pelotas; added under the "not a closed list" clause |
| Data intermediaries (cross-cutting) | `data-intermediaries.md` | Fitabase, unified APIs, and open datasets, not device ecosystems, but they determine what a study can actually access |

---

## Deferred, research-grade accelerometry alternatives

Axivity and GENEActiv, the two most important alternatives, **were profiled** (`axivity-geneactiv.md`). The remaining candidates below were not.

| Candidate | Why it matters | Status |
|---|---|---|
| **movisens** (Move 4, EcgMove, EdaMove) | German research-instrument manufacturer combining accelerometry with ECG and EDA, plus a companion EMA platform (movisensXS). Potentially a direct Empatica alternative with an integrated survey layer. | **Not researched.** High priority, the EMA integration makes it distinctive. |
| **Fibion** | Thigh-worn accelerometry focused on sedentary behaviour. Note: Fibion's competitor-pricing articles were used as a (clearly labelled) secondary source in the Ametris profile, so the company is already in this knowledge base's source graph. | **Not researched.** |
| **Shimmer** (Shimmer3, Verisense) | Modular research sensor platform with configurable raw multimodal capture (ECG, EMG, GSR, IMU); Verisense targets clinical trials. | **Not researched.** |
| **PAMSys / activPAL** | activPAL is the accepted reference for **posture classification** (sitting/standing/stepping), which no other device here does well. | **Not researched.** Relevant for sedentary behaviour research specifically. |

---

## Deferred, other consumer and prosumer wearables

| Candidate | Why it matters | Status |
|---|---|---|
| **Movesense** (Suunto) | Open developer platform with programmable sensor modules, potentially a Polar-like raw-access story with more extensibility. | **Not researched.** |
| **Biostrap** | Positions explicitly toward research with raw PPG access claims. | **Not researched.** Claims need verification. |
| **Ultrahuman Ring** | Oura competitor in the ring form factor with an API. | **Not researched.** |
| **RingConn, Circular, other smart rings** | Growing category; relevant to any ring-based design as Oura alternatives. | **Not researched.** |
| **Amazfit / Zepp Health** | Low-cost wearables with an open API; potentially relevant for large low-budget cohorts. | **Not researched.** |
| **Verily Study Watch** | Purpose-built research watch used in the Project Baseline studies. **Current availability and status are unknown** and should be verified before assuming it is procurable. | **Not researched.** Status verification needed. |
| **Muse** (InteraXon) | Consumer EEG headband; used in sleep and meditation research. Arguably a different modality rather than a wearable ecosystem competitor. | **Not researched.** Scope decision needed. |
| **Dreem / Beacon Biosignals** | Wearable EEG for sleep, the only route to genuine consumer-deployable sleep staging by EEG rather than by inference. Highly relevant given how poorly every device in this module stages sleep. | **Not researched.** High priority for sleep research questions. |

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

4. **Middleware/aggregators were identified but not profiled**, on the grounds that Phase 1 scope was defined around device ecosystems. Flagged above as a recommended addition.

5. **Axivity and GENEActiv were added to scope** despite not appearing in CLAUDE.md's starting list, under its explicit "starting point, not a closed list" clause. They underpin UK Biobank and comparable cohorts and set the openness and price benchmark for the whole module. **movisens, Shimmer, activPAL, and Fibion remain unprofiled**, the largest remaining device gap.

7. **Two files in this module (`axivity-geneactiv.md`, `data-intermediaries.md`) were produced during an interrupted segment of the research session.** Their central factual anchor (the UK Biobank AX3 configuration from Doherty et al. 2017) was independently re-verified against the primary source; the remainder was reviewed for internal consistency but not re-derived claim by claim. Flagged in `shared/research-log.md`.

6. **Validation evidence was scoped to decision-relevant findings**, per CLAUDE.md's instruction not to exhaustively review every validation paper. Two recent multi-device PSG comparisons and one major systematic review were used as the backbone, with the funding source noted where relevant.
