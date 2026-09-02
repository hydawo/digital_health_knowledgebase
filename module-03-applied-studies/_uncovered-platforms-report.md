# Module 3 — Closing the platform-coverage gap: AWARE, Avicenna, MetricWire, m-Path, CARP

**Session:** 2026-09-01. **Scope:** the five Module 2 platforms that had **no** Module 3 entry, named as a sampling bias in [`README.md`](README.md) and [`_inventory-and-scope-decisions.md`](_inventory-and-scope-decisions.md).

**Outcome: 12 new study profiles across all five platforms, and 12 open-access PDFs.** No platform came back genuinely empty.

This file is a discovery-and-decisions record, not a findings summary. Findings live in the profiles.

---

## 1. Headline correction to `_recency-scan-2026-09.md`

That scan reported **"0 usable" AWARE candidates** and **"0" CARP candidates**, with the caveat that a non-Europe-PMC search had not been attempted. Both nulls turn out to be artefacts of the search, not of the literature — but for opposite reasons, and only one is a search failure.

| Platform | Recency scan verdict | This pass | Why the earlier pass missed it |
|---|---|---|---|
| **AWARE** | 0 usable (single hit a false positive on the ordinary word "aware") | **Many.** 3 profiled; ≥4 more qualifying candidates identified | The scan queried the bare token `aware`, whose false-positive rate is near-total. Querying **`"AWARE framework"`, `"AWARE app"` and `"AWARE-Light"`** returns 202 / 50 / 24 hits respectively, with a high true-positive rate. **This was a query-design failure, and the corrected result should be treated as overturning the scan's conclusion about AWARE's current research activity.** |
| **CARP** | 0 | **1 profiled; the null is close to real** | Not a query failure. CAMS is a *framework* embedded in other people's apps, so deployments are published under the app's name (m-Path Sense, DiaFocus, mCardia, Wrist Angel), never CARP's. Europe PMC full-text search for `"CARP Mobile Sensing"` returns **4 records total**, and OpenAlex returns **27**, of which almost all are architecture, tooling, dataset or protocol papers. |

**The correction to make in `_recency-scan-2026-09.md`'s per-platform table is AWARE's row.** CARP's row is directionally right; the reason given ("consistent with Module 2's own status notes... evidence about the platforms' current research activity") is wrong for CARP too — the framework is active, its deployments are just invisible to name-based search.

Also note the recency scan's cut-off (2024-06-01) excluded qualifying work: three of the twelve profiles here are from 2023–early 2024.

---

## 2. What was profiled

All 12 are open access; all 12 PDFs are in [`literature/`](literature/); every number in every profile was read from full text (Europe PMC `fullTextXML`), not from an abstract. First authors were verified against the article XML, not search metadata.

### AWARE — 3 profiles

| Profile | Study | N / duration | Most decision-relevant finding |
|---|---|---|---|
| [`aware-chemotherapy-engagement.md`](profiles/aware-chemotherapy-engagement.md) | McClaine 2024, *JMIR Cancer* | 162 / 90 days | Three streams measured side by side (surveys **61%**, AWARE **73%**, Fitbit **70%**), and **non-White participants had OR 0.49 for surveys and OR 0.35 for wearable data** — while **older age predicted *better* wearable engagement**. |
| [`aware-light-smartsense-d-youth-depression.md`](profiles/aware-light-smartsense-d-youth-depression.md) | Camargo 2025, *Digital Health* | 48→40 / 8 weeks | **29% of consented participants could not run AWARE-Light on their own Android handset** and needed loan phones; **7 of 8 non-completers withdrew because of app technical issues.** Per-stream completeness ranged from **38.4% (communication) to 79% (location)** inside one app. |
| [`aware-msavorus-loneliness-multidevice.md`](profiles/aware-msavorus-loneliness-multidevice.md) | Nguyen 2025, *JMIR Form Res* | 37→29 / 22 weeks | EMA adherence reported **by phase** — 79% → 75% → 69% overall — with the range widening to 14–139 of 140 during the intervention phase. Module 3's first Oura and first Samsung deployment. |

### Avicenna Research (Ethica) — 3 profiles

| Profile | Study | N / duration | Most decision-relevant finding |
|---|---|---|---|
| [`avicenna-ema-suicidal-ideation-iatrogenic.md`](profiles/avicenna-ema-suicidal-ideation-iatrogenic.md) | Kivelä 2024, *Assessment* | 82 / 21 days | **Two defensible acceptability rates for the same study, 59 points apart: 39% and 98%.** Plus: no reactivity in the EMA data, but **22% retrospectively reported mood worsening and 18% ideation reactivity**, predictable from BPD traits, PTSD and symptom severity. |
| [`avicenna-adolescent-esm-school-phone-bans.md`](profiles/avicenna-adolescent-esm-school-phone-bans.md) | Achterberg 2026, *J Res Adolesc* | 195 / 17 days | **78% compliance under a national school smartphone ban** (88% reported school restrictions) — bought by redesigning the window around 11 school + 6 weekend days and a four-part engagement stack. Weekday compliance **exceeded** weekend. |
| [`avicenna-smoking-youth-ema-compliance.md`](profiles/avicenna-smoking-youth-ema-compliance.md) | Kochhar 2025, *Drug Alcohol Depend Rep* | 84 / 7 days | The only study here that **coded and counted participant complaints**: the top one is **the 1.5-hour survey expiry window (28.8%)** — a researcher-set platform parameter, not a content or privacy objection. |

### MetricWire — 3 profiles

| Profile | Study | N / duration | Most decision-relevant finding |
|---|---|---|---|
| [`metricwire-fraudulent-participation.md`](profiles/metricwire-fraudulent-participation.md) | Siebers 2025, *JMIR* | 10 enrolled fraudulently + 37 blocked | **MetricWire's carrier-country field identified 10 fraudulent participants** (VPN in UTC+1, all Nigerian carriers) in a $480-compensation virtual HIV trial. A manual checklist then blocked 37 over 12 months with zero further enrolments. **No other profile in this module addresses fabricated data at all.** |
| [`metricwire-post-discharge-ema-reactivity.md`](profiles/metricwire-post-discharge-ema-reactivity.md) | Spangenberg 2026, *Front Psychiatry* | interview n=16 / ~7 months | The module's **longest protocol** (~300 prompts over 7 months, post-psychiatric-discharge). Compliance **63.3% → 45.4%**, which is at the *top* of a literature reporting 14–21%. Participants questioned EMA's feasibility **during acute crises** — the method fails when its target occurs. |
| [`metricwire-sgm-youth-ema-feasibility.md`](profiles/metricwire-sgm-youth-ema-feasibility.md) | Clark 2025, *PLOS ONE* | 50 / 28 days | **80.21% compliance in suicidal SGM youth** — the highest mental-health figure in this module — attributed to protocol **co-design with the population**, which set survey frequency around school phone policies and rerouted risk escalation away from police to local mobile crisis services. Compliance decayed **−4.35 points/week**. |

### m-Path — 2 profiles (plus the CARP entry below, which is also m-Path)

| Profile | Study | N / duration | Most decision-relevant finding |
|---|---|---|---|
| [`mpath-avatar2-esm-engagement.md`](profiles/mpath-avatar2-esm-engagement.md) | Dennard 2025, *JMIR Form Res* | 134 of 207 / 10×/day, 6 days | **Mean completion 39.1% — the module's lowest — because completion was defined as 100%-complete questionnaires, a definition forced by m-Path's partial-save export behaviour.** Also: **35.3% of trial participants declined the optional ESM component outright**, and no demographic or severity predictor of completion (F5,128=0.548, P=.74). |
| [`mpath-nssi-ema-benefits-challenges.md`](profiles/mpath-nssi-ema-benefits-challenges.md) | Bonnier 2025, *IJCHP* | 132→124 / 28 days | **Within-person, feeling more overwhelmed than usual predicted higher prompt burden in the same *and next* assessment** (and emotional discomfort correlated −0.29 with compliance) — the "crisis paradox" quantified. **78.57% reported a benefit; 7.29% found EMA aversive.** Benefit was domain-specific: 64.58% NSSI-specific self-insight vs 32.65% general. |

### CARP Mobile Sensing — 1 profile

| Profile | Study | N / duration | Most decision-relevant finding |
|---|---|---|---|
| [`carp-mpath-sense-performance-study.md`](profiles/carp-mpath-sense-performance-study.md) | Niemeijer 2023, *JMIR Form Res* | 104 (52 iOS / 52 Android) / 21 days | **Relative coverage rate ≈ 0.50 — half the specified measurements never arrived**, despite 69.51 GB of data. And **iOS gaps were ~6× longer than Android's** (median 47.36 vs 7.55 min; total gap time ~1.8 weeks vs ~5.5 days out of 21). Five named failure modes, including **11.5% of iOS users having the app's files deleted by the OS**. |

---

## 3. Nulls, near-nulls, and exactly what was searched

### CARP Mobile Sensing — a real scarcity, correctly diagnosed

Only **one** qualifying deployment study was found, and it is a study of CAMS embedded in someone else's app (m-Path Sense, KU Leuven — which does at least answer Module 2's open question about **adoption outside DTU** affirmatively).

**Searches run:**

| Source | Query | Result |
|---|---|---|
| Europe PMC full text | `"CARP Mobile Sensing" OR "CARP mobile sensing framework"` | **4 records total**: the m-Path Sense performance study (profiled); the *Sensors* 2022 software-architecture paper (architecture, out of scope); a *Frontiers in Sleep* 2025 **study protocol** with no results (out of scope by `CLAUDE.md`'s protocol rule); and a *Digital Health* 2024 episodic-future-thinking study whose full text mentions only CACHET as a funder, not CARP as an instrument. |
| Europe PMC full text | `"Copenhagen Research Platform"` | 4 records, overlapping the above plus one 2025 **protocol** (JMIR Res Protoc, ambulatory ECG digital biomarkers). |
| Europe PMC full text | `Bardram AND ("mobile sensing" OR "digital phenotyping" OR "carp")` | 33 records; the applied ones are Monsenso/RADMIS-lineage bipolar studies that do not name CARP as the instrument. |
| Europe PMC full text | `"CACHET" AND (smartphone OR sensing)` | 50 records, heavily contaminated by *Conus* gastropods and unrelated uses; the relevant ones are DiaFocus, an allergic-rhinitis air-quality study and the Neuropathy Tracker. |
| Europe PMC full text | `"CARP" AND ("digital phenotyping" OR "passive sensing" OR "Flutter")` | 65 records, dominated by cardiology (*carp*, CARP genes, "atrial flutter") — the ambiguity the recency scan flagged, confirmed. |
| arXiv API | `all:"CARP Mobile Sensing"` | **1 record** — the 2020 architecture preprint only. |
| OpenAlex | `search="CARP Mobile Sensing"` | **27 records.** Reviewed all 27. Composition: 2 versions of the architecture preprint, the 2025 UbiComp demonstration paper, `Sensors` 2022 architecture, m-Path platform paper, m-Path Sense (profiled), 2 Zenodo dataset records (UbiLife), Niimpy toolbox, mCardia, AwarNS, DiaFocus, and a scatter of unrelated middleware/LLM/scheduling papers. **No further study with a deployment cohort reporting recruitment, retention, adherence or completeness.** |
| Semantic Scholar API | attempted twice | **HTTP 429 (rate limited) both times; not usable this session.** |

**Verdict: the CARP null is structural, not a search artefact.** CAMS is distributed as a Flutter package and published about as software. Its deployments surface under application names. **Searching by platform name cannot find them** — this is a genuine limitation of the module's device/platform-side discovery method, and it will apply equally to any future framework-shaped (rather than product-shaped) platform.

**Two CARP leads deliberately *not* profiled, and why:**

1. **DiaFocus** — Lind N, Bækgaard P, **Bardram JE**, Cramer-Petersen C, Nørgaard K, Christensen MB. "Assessing the Clinical Feasibility of the DiaFocus System for Integrated Personalized Management of Type 2 Diabetes: 6-Month Pilot Cohort Study." *JMIR Diabetes* 2025;10:e63894 (PMC12377514). **This is a real 6-month feasibility deployment** (17 participants, median age 68, feasibility assessed via retention, app usage and the CACHET Unified Method for Assessment of Clinical Feasibility) with Bardram as an author. **But the full text never names CARP or CAMS**, and per the brief's instruction to verify platform usage from full text before profiling, it was not written up. The DiaFocus *system-design* paper (ACM TCH 2023) does appear in OpenAlex's CARP-citing set, which makes CARP usage **Corroborated but not Verified**. **Recommended next step: retrieve the DiaFocus design paper (ref 13 of the JMIR Diabetes article), confirm the CAMS dependency, and if confirmed, profile the 2025 pilot — it would be Module 3's first CARP-native clinical deployment and its first type-2-diabetes study.**
2. **Wrist Angel** (*JMIR Res Protoc* 2023) — a CARP-citing wearable-AI OCD study, currently protocol-only. Revisit when results publish.

### AWARE — the recency scan's null is wrong

Qualifying AWARE deployment studies exist in quantity. **Searches that worked:** `"AWARE framework" AND ("passive sensing" OR "mobile sensing" OR "digital phenotyping")` (44 hits), `"AWARE app" AND smartphone` (50), `"AWARE-Light"` (24). The bare token is unusable; the multi-word forms are clean enough to screen manually.

**Further qualifying AWARE candidates identified but not profiled this pass** (all verified to use AWARE from full text or abstract as noted):

- **PMC12174892** — *JMIR* 2025, "Longitudinal Digital Phenotyping of Multiple Sclerosis Severity Using Passively Sensed Behaviors and EMA." **AWARE + Fitbit confirmed from full text.** Strong candidate; MS is an unrepresented condition in this module.
- **PMC12741416** — *Data Brief* 2025, loneliness and well-being in Finnish immigrants: **AWARE + Oura Ring + Samsung Watch**, multimodal dataset. Would extend geography (Finland) and the Oura/Samsung coverage; a dataset paper, so operational content needs checking.
- **PMC12386097** — *Healthcare* 2025, digital phenotyping for early self-detection of psychological distress.
- **PMC12619020** — *JMIR Form Res* 2025, detecting perceived unfair treatment among US college students using mobile sensing.
- **PMC11888105** / **PMC11847758** — **sibling analyses of the SmartSense-D cohort already profiled.** Do not count as separate deployments (recorded in that profile).

### Avicenna, MetricWire, m-Path — no nulls

All three have substantial, current literature. The constraint was **selection**, not availability.

- **MetricWire**: 327 Europe PMC full-text hits. Overwhelmingly EMA studies in addiction, suicide and affect research; the platform is near-ubiquitous in US psychology EMA work. Selection favoured operational content over topic prestige.
- **Avicenna/Ethica**: verified via `"Ethica Data"` (66 hits) and `"Avicenna Research"` — note the latter returns **2,323 hits dominated by Iranian biomedical research institutes named after Avicenna**, exactly the ambiguity flagged in the recency scan. **`"Ethica Data"` and `"Ethicadata"` are the reliable queries**, since the company's rename means older and many current papers still cite the old name; several papers write it as "Ethica (a.k.a. Avicenna)".
- **m-Path**: the bare token `"m-Path"` returns 1,634 hits and is unusable (it matches hyphenation artefacts, `MPS3`, "path" compounds). **`"m-path.io"` (17), `"m-Path platform"` (11), `"m-Path app"` (48), `"the m-Path application"` (20) and `"m-Path Sense"` (5) are the reliable queries.**

**Notable candidates left on the table:**

- **PMC13152121** — *PLOS Glob Public Health* 2026, intensive longitudinal follow-up of cisgender and transgender women engaged in sex work, m-Path. Would address the module's **geography gap** if the setting is low- or middle-income; not verified this pass.
- **PMC12697974** — *PLOS Digit Health* 2025, the **HEALTH Platform** (Ethica-based), a smartphone-based system paper with a cohort.
- **PMC10863640** — *Clin Psychol Eur* 2023, the **WARN-D** study (Ethica) — a large early-warning-system-for-depression cohort.
- **PMC11923469** — *JMIR Form Res* 2025, feasibility of EMA after metabolic bariatric surgery (Ethica Data).
- **PMC12274019** — *JMIR Mhealth Uhealth* 2025, patterns of engagement with an mHealth component (MetricWire).

---

## 4. Cross-cutting observations this batch adds to the module

Recorded here rather than in `feasibility-matrix.md`, which is not this pass's to edit. Each is supported by profiles above.

1. **"Compliance" is now demonstrably a platform artefact as much as a participant one.** Three studies here report figures between 39.1% and 80.2% where the *definition* explains much of the spread: **100%-complete only** (Dennard, 39.1%), **fully-completed only, no partial saves** (Kivelä, 78%), **≥50% complete** (McClaine, 61%), and **careless <30s responses excluded** (Spangenberg) versus **careless responses deliberately retained** (Achterberg). Two of these definitional choices were **forced by platform behaviour**, not chosen on methodological grounds.
2. **Two studies in this batch contradict each other on OS-platform data yield.** McClaine found Android yield **lower** than iOS under AWARE (sampling-frequency differences); Niemeijer found iOS gaps **~6× longer** than Android's under CAMS. Both are Verified. **The module should stop treating OS asymmetry as having a known direction.**
3. **Morning prompts are the weakest slot, in three independent cohorts** — Achterberg (missed to sleep), Kivelä (chronotype plus a 3-hour window), Clark (the *only* survey type where adolescents differed from young adults). This is schedulable.
4. **Compliance decays at a measurable, similar rate across platforms and populations**: −4.35 points/week over 28 days (Clark, MetricWire), linear decline over 28 days (Bonnier, m-Path), 79%→75%→69% by phase over 22 weeks (Nguyen, AWARE), 63.3%→45.4% over 7 months (Spangenberg, MetricWire).
5. **Clinical severity again fails to predict attrition or compliance** — added here by Kivelä (BDI, BSSI, HADS-A, ISI all null), Dennard (PSYRATS null), Clark (attempt and NSSI history null), Kochhar (all demographics null) and McClaine (completers vs withdrawers differed only on insurance type). *Anxiety diagnosis* (Kivelä) and *student status* (Kivelä) did predict, as did *age group* (Clark) and *race* (McClaine).
6. **Intensive monitoring of suicidality is safe at the group level and uncomfortable for a minority**, now across three platforms: no detected reactivity but 18–22% retrospective self-report (Kivelä, Avicenna); reported thought intensification but **no behavioural harm** (Spangenberg, MetricWire); 7.29% finding it aversive (Bonnier, m-Path); **zero adverse events** (Camargo, AWARE-Light).
7. **Two new failure-mode classes enter the module**: **adversarial participation** (Siebers — fabricated enrolment in an incentivised virtual trial) and **institutional device restriction** (Achterberg — a national school phone ban as a design constraint).
8. **Handset-model compatibility is a distinct risk from OS compatibility.** "Android-only" was not a sufficient technical specification for AWARE-Light: 29% of consented participants still needed a different phone.

---

## 5. Technologies encountered that are not profiled in Modules 1 or 2

Flagged as **Module 1/2 expansion candidates**, per `CLAUDE.md`'s rule against silently absorbing unprofiled technologies:

| Technology | Where it appeared | What it is |
|---|---|---|
| **Realtime EXP by LifeData** | Ball et al. 2025, *Behavior Therapy* (see §6) | A commercial EMA platform. In that study **90% of participants used LifeData and only 10% MetricWire** — meaning LifeData is quantitatively the more consequential platform in at least one recent suicide-EMA study, and it is absent from Module 2. **Strongest expansion candidate from this pass.** |
| **MoSHI Surveys** | McClaine 2024 | In-house notification/survey app (University of Pittsburgh, Low lab), described as "free and commercially available". Not a general platform, but recurs in that group's work. |
| **RAPIDS** (Reproducible Analysis Pipeline for Data Streams) | McClaine 2024 | Open-source feature-extraction pipeline for phone and Fitbit data — functionally the analogue of **Forest** for Beiwe, and arguably belongs alongside it in Module 2's derived-features treatment. |
| **`mpathsenser`** | Niemeijer 2023 | R package extracting m-Path Sense raw data into SQLite. Same category as RAPIDS/Forest. |
| **mSavorUs** | Nguyen 2025 | Custom JITAI intervention app; not a research platform. |
| **DiaFocus, mCardia, Wrist Angel, AwarNS, Niimpy, CLAID** | OpenAlex CARP-citing set | The CARP-adjacent application and tooling ecosystem. Worth a short Module 2 note under the CARP profile as evidence of framework uptake, whether or not any is profiled separately. |
| **UNEEG subcutaneous EEG (ULT-EEG)** | *Frontiers in Sleep* 2025 CARP protocol | Ultra-long-term implanted EEG. Not a wearable in Module 1's sense, and the paper is a protocol — noted only so the encounter is on record. |

---

## 6. Bibliographic and attribution errors caught

| Item | Detail |
|---|---|
| **`_recency-scan-2026-09.md` — AWARE row** | States "**0 usable**... No qualifying AWARE deployment study since mid-2024 was found." **Incorrect.** The single-token query was the cause. At least seven qualifying AWARE studies exist, three profiled here. |
| **`_recency-scan-2026-09.md` — CARP row rationale** | The count (0) was right; the stated reason ("evidence about the platforms' current research activity") is wrong. CAMS is actively used; it is invisible to name-based search because it is a library. |
| **`_recency-scan-2026-09.md` — Ball et al. 2025 characterisation** | Listed as a MetricWire study ("MetricWire; mixed methods on engagement"). The full text shows **90% (n=90) of participants used *Realtime EXP by LifeData* and only 10% (n=10) MetricWire**, following a mid-study platform change. **Not a MetricWire study.** Not profiled here for that reason; it would be a reasonable LifeData entry if Module 2 adds LifeData. |
| **Achterberg 2026 authorship** | Europe PMC's `authorList` returns a single author; verified against the article XML that this is correct — **Michelle Achterberg is the sole author**, not a truncation. |
| **SmartSense-D sibling papers** | PMC11888105 and PMC11847758 report the same Melbourne AWARE-Light cohort (N≈40–41, same site, same platform) as PMC12034961. Recorded in the profile so they are not counted as three deployments. |
| **Bonnier 2025 cohort** | Points to Kiekens et al. 2024 for diagnostic characteristics of the *same* cohort. Recorded so that paper is not treated as a separate deployment. |
| **Spangenberg 2026 sample** | All compliance figures describe **16 purposively selected interviewees**, sampled to span high and low compliance — **not the parent cohort**, whose N is not reported in that paper. Flagged prominently in the profile; the figures must not be quoted as cohort-level compliance. |

---

## 7. Recommended next steps

1. **Correct the AWARE row (and the CARP rationale) in `_recency-scan-2026-09.md`**, and re-run any per-platform query in that scan that used a single ambiguous token. The reliable query forms for all five platforms are given in §3 above.
2. **Resolve the DiaFocus/CARP question** (§3) — it is the one realistic path to a second CARP profile and to a clinical, non-KU-Leuven CARP deployment.
3. **Add the five uncovered platforms to `feasibility-matrix.md`** using the 12 profiles here, and consider adding a column or footnote recording **the compliance definition each study used** — this pass makes it unavoidable that the matrix's numbers are not comparable without it.
4. **Assess LifeData for Module 2**, on the strength of Ball et al. 2025 and the correction in §6.
5. **Profile PMC12174892 (AWARE + Fitbit in multiple sclerosis)** — MS is unrepresented in this module, and the study is a confirmed AWARE deployment with a longitudinal design.
6. **Consider whether Module 3's discovery method needs a second axis.** Searching from the device/platform side, as `CLAUDE.md` prescribes, structurally cannot find framework-shaped platforms like CARP. A complementary **citation-graph pass** (works citing a platform's architecture paper, as run here via OpenAlex) found the CARP application ecosystem in one query where five full-text queries had failed.

---

## Method notes

- **Discovery:** Europe PMC REST (`/search`, full-text indexed, `sort=P_PDATE_D desc`), one to five query forms per platform; supplemented by arXiv and OpenAlex for CARP. Semantic Scholar was rate-limited (HTTP 429) and unusable.
- **Verification:** every candidate's platform usage was confirmed by grepping the **full text** for the platform name in an instrumentation context, and manually reading the surrounding sentence. Candidates matching only in a reference list, a funder acknowledgment, or the word "ethical"/"aware of" were discarded. This removed several apparent hits, including the *Digital Health* 2024 episodic-future-thinking paper (CACHET funder only) and every "Ethica" match that was really "ethical".
- **Extraction:** full-text XML via `https://www.ebi.ac.uk/europepmc/webservices/rest/<PMCID>/fullTextXML`, stripped to text with table cells preserved. No figure was taken from an abstract.
- **PDFs:** `https://europepmc.org/articles/<PMCID>?pdf=render` with a browser User-Agent; all 12 retrieved (123 KB – 2.0 MB), all CC BY except Camargo 2025 (CC BY-NC).
- **Naming:** `YYYY-firstauthor-venueslug-short-title.pdf`, first author verified from the article XML rather than search metadata.
