# Module 2 — Working Inventory and Scope Decisions

This file is the Phase 1 output: the full inventory of candidate technologies, which were profiled in
this research phase, which were deliberately deferred, and why. Per the operating rules, uncertain
inclusion decisions are recorded rather than silently made — mirroring Module 1's
`profiles/_inventory-and-scope-decisions.md`.

---

## Profiled in this phase (8 platforms, 8 files)

| Platform | Profile | Rationale for inclusion |
|---|---|---|
| Beiwe | `profiles/beiwe.md` | Named in scope; the platform this module is explicitly anchored to |
| RADAR-base | `profiles/radar-base.md` | Named in scope; largest consortium-scale open-source competitor |
| mindLAMP | `profiles/mindlamp.md` | Named in scope; distinctive dual research/clinical orientation |
| AWARE Framework | `profiles/aware-framework.md` | Named in scope; longest-running, most plugin-extensible open-source option |
| Avicenna Research (formerly Ethica) | `profiles/avicenna-research-ethica.md` | Named in scope as "Ethica"; current name resolved and documented |
| MetricWire | `profiles/metricwire.md` | Named in scope; longest continuous commercial operating history in the module |
| m-Path | `profiles/m-path.md` | Discovered during Phase 1 broad search; added under the "starting point, not a closed list" clause for its distinctive EMA/EMI/JITAI sophistication and dedicated peer-reviewed methods paper |
| CARP Mobile Sensing (DTU) | `profiles/carp-mobile-sensing.md` | Discovered during Phase 1 broad search; added for the same reason — a genuinely distinct architecture (Flutter library, not a hosted product) that materially changes the comparison space |

## Deferred or partially covered — legacy and adjacent

Covered in `profiles/legacy-and-adjacent-platforms.md` rather than given full standalone profiles:

| Candidate | Why it matters | Status |
|---|---|---|
| **Purple Robot** | Historically named alongside Beiwe/AWARE/RADAR-base in the methods literature; most complete Android sensor coverage of any platform reviewed in a cited systematic review | **Not fully profiled.** Current maintenance status is Unclear (no recent activity signal found); Android-only regardless. Labeled clearly as legacy per CLAUDE.md's instruction rather than silently excluded. |
| **StudentLife** | Landmark 2013–14 Dartmouth study/app; the resulting dataset remains in active secondary use | **Not profiled as a platform** — it is a completed study and its app was tied to that study, not a reusable tool. Its dataset's continuing relevance is noted. |
| **Koa Health** | Active, well-published digital-phenotyping research program at a real commercial mental-health company | **Deferred, not profiled.** No evidence found this session of a publicly documented, externally-deployable "Koa Health platform" comparable to the other commercial entries — its technology appears to power its own products/collaborations rather than being offered as general-purpose research infrastructure. Needs direct vendor confirmation before either inclusion or firm exclusion. |
| **PhoneStudy** | Named as a discovery-search candidate in the task prompt | **Searched for, not found.** No distinct, independently notable platform by this name was located beyond generic academic use of the term. Recorded as "not found" per CLAUDE.md's instruction to record uncertain inclusion decisions rather than silently drop a named candidate. |

## Explicitly out of scope for Module 2

| Category | Reason |
|---|---|
| Consumer wearable ecosystems (Apple Watch, Oura, WHOOP, Fitbit, Garmin, Samsung, Polar, Withings, Empatica, ActiGraph/Ametris) | **This is Module 1.** Already profiled there. Samsung's Health Research Stack — the one Module 1 entry with digital-phenotyping-adjacent characteristics — is cross-referenced from `profiles/legacy-and-adjacent-platforms.md` rather than duplicated. |
| Consumer mental-health apps without a research/study-deployment layer (e.g., pure meditation or mood-tracking consumer apps) | Not a research platform in the sense this module covers — no study-management, no researcher data access. |
| EHR/FHIR interoperability platforms | Belongs to a future "health data interoperability" module per CLAUDE.md's Future Modules list, unless a specific digital-phenotyping platform's EHR/FHIR integration is a documented feature (none was established this session for any profiled platform). |
| General-purpose survey tools without passive sensing (e.g., generic REDCap-only deployments) | Out of scope — this module is specifically about platforms combining or centering passive smartphone sensing, not any tool that can deliver a questionnaire. |

## Scope decisions made during this phase

1. **Ethica and Avicenna Research were treated as one entity, not two**, based on convergent evidence
   (shared app-store listing "Avicenna (Ethica)," shared Android package name `com.ethica.logger`,
   and third-party directory cross-referencing). CLAUDE.md's instruction to record rather than
   silently resolve ambiguity is satisfied by stating this explicitly in the profile rather than
   simply picking one name.
2. **CARP Mobile Sensing was profiled despite being architecturally a library/framework rather than a
   hosted product**, because excluding it on that technicality would have hidden a real, distinct
   option from any team weighing "build our own app on a proven engine" against "configure an
   existing platform's dashboard" — a genuine decision axis CLAUDE.md's research questions call for
   ("SDK availability," "custom app builds," "backend extensibility").
3. **m-Path was included even though its core identity is EMA/EMI rather than passive sensing**,
   because it explicitly bundles a sensing module (m-Path sense) and because its JITAI support and
   dedicated methods paper made it a distinctive enough comparison point to omit only by narrowing
   the module's scope past what CLAUDE.md's own research-question list implies (it explicitly asks
   about EMA, JITAI-adjacent triggered assessment, and wearable-triggered assessment).
4. **Purple Robot and StudentLife were deliberately not given full profiles**, on the same principle
   Module 1 used for its "Deferred" candidates: better to name them, state why they weren't fully
   researched, and flag the specific unresolved status question (maintenance status for Purple
   Robot; dataset-vs-platform distinction for StudentLife) than to either silently omit them or
   promote thin research to a full profile's apparent authority.
5. **This module received a single research session**, not Module 1's two-pass depth. This is stated
   plainly in `README.md` and `comparison-matrix.md` rather than presented as equivalent-depth
   research — the "not independently verified this session" markers throughout every profile are the
   direct, honest consequence of that scoping decision, not evidence of platforms being less
   documented than Module 1's wearables.
6. **Compliance documentation (HIPAA/GDPR/SOC2) was not established for any platform**, including
   ones with explicit clinical positioning. Rather than mark this Unclear once and move on, it is
   called out at the module level (README, comparison matrix Table 7, and unresolved-questions.md)
   because it is the single highest-value gap for anyone actually planning a regulated study.
