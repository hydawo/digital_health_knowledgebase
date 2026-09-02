# Onnela tranche — build report

**Written 2026-09-01. This is a handoff file, not a module artifact.** It reports what was built from
[`_onnela-module3-candidates.md`](_onnela-module3-candidates.md), what was rejected and why, the
errors found in the staged candidate list, and an assessment of whether this tranche tilts Module 3's
evidence base toward Beiwe.

**Files created by this pass (nothing else was touched):**

- 9 new profiles in `profiles/` (listed below)
- this report

`README.md`, `feasibility-matrix.md`, `sources.md`, `_inventory-and-scope-decisions.md`,
`_recency-scan-2026-09.md`, `_onnela-module3-candidates.md`, all pre-existing profiles, and
everything in `module-01-wearables/`, `module-02-digital-phenotyping/` and `shared/` were **not
modified**. No PDFs were copied; where a full text already existed elsewhere in the repository the
profile links to that path. **No new PDFs were added** — see "Retrieval outcomes" below.

---

## What was built (9 profiles)

| # | Profile | Study | Technologies | N | Candidate rank |
|---|---|---|---|---|---|
| 1 | [`beiwe-spinal-cord-injury-incentives.md`](profiles/beiwe-spinal-cord-injury-incentives.md) | Mercier et al. 2020, SCI | Beiwe | 43 | #1 |
| 2 | [`beiwe-actigraph-modus-als-progression.md`](profiles/beiwe-actigraph-modus-als-progression.md) | Johnson et al. 2023, ALS | Beiwe + ActiGraph Insight Watch + Modus StepWatch 4 | 40 | #2 |
| 3 | [`beiwe-nurses-health-study-burst.md`](profiles/beiwe-nurses-health-study-burst.md) | Yi et al. 2025, NHSII | Beiwe | 181 | #3 |
| 4 | [`beiwe-pain-clinic-operational-report.md`](profiles/beiwe-pain-clinic-operational-report.md) | Fu et al. 2024, chronic pain | Beiwe | 77 | #4 |
| 5 | [`actigraph-als-upper-limb-wear-time.md`](profiles/actigraph-als-upper-limb-wear-time.md) | Straczkiewicz et al. 2024, ALS | ActiGraph GT3X+ (bilateral wrist) | 202 | #6 |
| 6 | [`beiwe-fitbit-gynecologic-cancer-hope.md`](profiles/beiwe-fitbit-gynecologic-cancer-hope.md) | Wright et al. 2018, HOPE | Beiwe + Fitbit Zip + Fitbit Charge 2 | 10 | #8 |
| 7 | [`oura-university-freshmen-sleep.md`](profiles/oura-university-freshmen-sleep.md) | Soon et al. 2025, NUS freshmen | Oura Ring 3 (+ Z4IP app) | 638 | #16 |
| 8 | [`lamp-schizophrenia-cognition-unpaid.md`](profiles/lamp-schizophrenia-cognition-unpaid.md) | Liu et al. 2019, schizophrenia | **LAMP app** (mindLAMP predecessor) | 35 | #19 |
| 9 | [`beiwe-spine-disease-mobility.md`](profiles/beiwe-spine-disease-mobility.md) | Cote et al. 2019, spine disease | Beiwe | 105 | #12 |

**Every figure in all nine profiles comes from full text.** Seven were read from open-access PDFs via
`pdftotext` (two required a second pass in reflow mode to recover sentences broken across
two-column page boundaries); two — Mercier and Cote — were read from NCBI efetch PMC XML.

### Why these nine, and why the ranking was revised

The three you flagged as gap-filling (#1 Mercier, #2 Johnson, #3 Yi) were built first and all three
delivered. Beyond those, selection prioritised **operational content confirmed by full text** and
**platform/device balance**, which moved three studies substantially against the abstract-derived
ranking:

- **#6 Straczkiewicz 2024 promoted to the top tier.** Its abstract gives no hint of what the full
  text contains: the wear-time-threshold sensitivity that changes the analytic sample from 202 to
  240 to 308 participants at 21 / 16 / 8 hours per day. This is, in my judgement, the single most
  decision-relevant operational finding in the whole tranche — a within-study, same-raw-data
  demonstration that "wear time" definitions determine analytic N by ±50%. It is also non-Beiwe.
- **#16 Soon 2025 promoted.** Ranked mid-table from its abstract, but it is the largest deployment
  built here (638 participants, 64,642 nights), it is non-Beiwe and non-US, and it reports a clean
  three-stream burden gradient (72.4% ring / 66.2% intermittent diary / 42.8% daily EMA) in one
  cohort. It also runs a compliance-stratified missingness sensitivity analysis, which almost no
  study in this module does.
- **#19 Liu 2019 promoted.** Thin on conventional operational metrics — no retention data at all —
  but it is the module's cleanest **deliberately** unpaid deployment, and its finding that the
  clinical group completed ~3× as many voluntary assessments as healthy controls is the direct
  counterpoint to Mercier's incentive result. It is also **not a Beiwe study** (see the device
  attribution corrections below).
- **#5 Straczkiewicz 2026** (short prescribed exercises, N=329) was deprioritised in favour of the
  2024 paper from the same author on the same cohort family, to avoid two near-adjacent ALS
  accelerometer profiles. It remains a strong candidate for the next pass.
- **#12 Cote 2019 retained but downgraded in expected value**, because the headline reason it was
  ranked #12 turned out to be a misreading (below). It still earns a profile for its 42%
  smartphone-ownership exclusion and its published per-day missing-GPS-minutes figure.

---

## The most decision-relevant finding from each profile

1. **Mercier 2020** — Retention rose **50% → 78%** when a conditional $30/two-month incentive was
   introduced mid-study, **while survey completion rate did not increase at all.** Incentives bought
   presence, not effort. Separately, and larger than the incentive effect: the exercise-programme
   recruitment stream completed 53% vs the community-reintegration stream's 21%, same platform, same
   protocol — **an existing routine contact point outperformed a payment.**
2. **Johnson 2023** — ActiGraph 158 vs Modus 136 median valid days, and 21 vs 12 valid hours per
   valid day, **in the same cohort — and the authors state these must not be compared**, because a
   valid hour meant "device worn per vendor algorithm" on one device and "≥1 step logged" on the
   other. A behavioural wear criterion systematically penalises the more impaired participant; a
   device-state criterion does not.
3. **Yi 2025** — **32 of 181 participants (17.7%) submitted zero EMA surveys**, in an 8-day burst
   inside a cohort with 30+ years of survey compliance. Compliance was flat at ~55% from day 2 with
   **no fatigue curve**; the loss was front-loaded into onboarding, and 19 participants completed
   the feedback survey while never completing the baseline, naming installation and registration
   failures as the cause.
4. **Fu 2024** — The headline **84% overall / 51% active / 78% passive** completion figures are
   computed **over completers only (38 of 77)**, on a "any data that day" criterion, in a cohort
   censored by a formal below-20%-completion dismissal rule. Also: **76% of loss was health or life
   events, only 15% app difficulty** — situational attrition dominates technological attrition 5:1.
5. **Straczkiewicz 2024** — **202 / 240 / 308** analysable participants at **21 / 16 / 8** hours of
   required daily wear, same raw data. Mean 282.8 collected days yielded **51.34 valid days (18.2%)**
   under the 21-hour rule. And the analytic sample was declining **~20% more slowly** than the source
   cohort (−0.570 vs −0.714 ALSFRS-RSE points/month) — **a wear-time criterion is a covert
   disease-severity filter.**
6. **Wright 2018** — The published "approach-to-consent rate was 100%" conceals that **treating
   oncologists removed 8 of 18 eligible patients (44%) before anyone was approached**, for "bad
   timing," "too distressed," and language. True yield 10/18 = 56%. Also: one participant of ten was
   unusable because her Android 4.3 (2012) device could not run Beiwe.
7. **Soon 2025** — In one cohort over 20 weeks, a graded burden ladder: **72.4% of person-nights
   (wearable) / 66.2% (intermittent diary) / 42.8% (daily EMA app)**. Continuous wear at a 20-hour
   threshold yielded 72.4%, against Straczkiewicz's intermittent wear at a 21-hour threshold yielding
   18.2% — **the wear protocol dominates the threshold**.
8. **Liu 2019** — Unpaid, over 12 weeks, with fully ignorable prompts: participants with
   schizophrenia completed a mean of **24 assessments vs healthy controls' 8** — roughly the protocol
   ceiling vs a third of it. **The healthy control arm was the adherence risk.**
9. **Cote 2019** — **42% of everyone approached (90 of 216) was excluded on the spot for not owning
   a smartphone**, and a further 19 of the remaining 126 (15%) were lost to a forgotten app-store
   password or an absent phone. **Only 2 of 126 (1.6%) declined over data security.** Daily survey
   response was 43.4% against a weekly rate of 73.2% — same cohort, same prompts.

---

## The Mercier incentive numbers: obtainable, and what they actually say

**Obtainable — yes, from NCBI efetch XML, and the full text confirms the abstract.** Verbatim:

> "Initially this study did not offer compensation to participants, however this was revised with
> IRB approval to promote study retention. After this revision, participants who completed at least
> 70% of surveys received a **$30 check payment after each two-month period of enrollment**. […]
> After providing compensation, **study retention increased from 50% to 78%**."

**What is genuinely established:**

- The incentive structure: **$30 per two-month enrolment block, conditional on ≥70% survey
  completion.** That is a threshold design, not a volume-scaled one.
- The retention change: **50% → 78%**, stated in the abstract, results and discussion.
- **Survey completion did not improve.** "The conditional remuneration did not apparently
  incentivize survey response behaviors because percentage of complete surveys did not increase."
- **Recruitment composition did not change.** "The financial incentive did not appear to alter
  recruitment appeal to eligible participants: the sample's demographic characteristics were similar
  pre and post compensation."
- The **qualitative** shift in dropout reasons is arguably the strongest part. Pre-incentive: time
  demands (cited 6×), medical complications (4×), limited hand function (4×), and **six participants
  lost to follow-up despite multiple contact attempts**. Post-incentive: **one** lost to follow-up
  and one withdrawal over privacy. Silent loss-to-follow-up essentially disappeared.

**Three material weaknesses, all recorded in the profile:**

1. **It is a before/after comparison within one ongoing study, not a randomised arm.** The two
   groups are separated in calendar time (enrolment ran April 2017 – July 2019), so any co-occurring
   change in staffing, procedure or population mix is confounded with the incentive.
2. **The denominators are not in the text.** They exist only inside Figure 1, a raster image in the
   NIHPA author manuscript, which could not be read (see retrieval outcomes). With 43 participants
   total, a handful of people moves either percentage by 5–10 points.
3. **A larger, cleaner effect sits alongside it in the same paper and is not the incentive.** The
   FESRT (outpatient exercise programme) stream completed 53% of the 4-month protocol against the
   community-reintegration stream's 21%, and 57% vs 25% of surveys. Recruitment setting produced a
   2.5× difference; the incentive produced a 1.56× one. Anyone reading Mercier for "what does money
   buy" should read the stream comparison first.

**Recommended citation form:** *"One before/after comparison inside a single 43-participant Beiwe
study reported retention rising from 50% to 78% after a conditional $30-per-two-months incentive was
introduced, with no accompanying increase in survey completion rate (Mercier et al. 2020)."* Not as
an effect estimate.

**Nothing about this finding is Beiwe-specific.** A conditional payment is a study-conduct
manipulation; the same design on any Module 2 platform would be expected to behave the same way.
That is the strongest reason to take the number seriously despite Onnela's co-authorship.

---

## Assessed and rejected

### Rejected on an explicit `CLAUDE.md` scope rule — full text read

**#26 Nock et al. 2026** (*J Psychopathol Clin Sci*, `10.1037/abn0001117`, PMC13308188) — N=619,
6 surveys/day for 3 months, 79,448 surveys. **The largest deployment in the tranche, and I read the
full text before rejecting it.** The platform is **LifeData**, not Beiwe and not any Module 1 or 2
technology:

> "Participants provided informed consent, completed a baseline survey, and installed an app on
> their smartphone (**LifeData**) that delivered brief self-report surveys."

`CLAUDE.md`'s Module 3 scope rule is explicit that feasibility studies for technologies not yet
profiled in Modules 1 or 2 are "flagged as a candidate for Module 1/2 expansion instead" and must
not be "silently absorbed into Module 3." So it is flagged rather than profiled — **but its
operational content is substantial and should not be lost**, so it is recorded here:

- 619 consented; **502 (81.1%) provided data in at least one survey** — i.e. **18.9% never
  contributed**, despite $10 for the baseline survey and **$1 per completed EMA survey**.
- "Rolling median and mean survey **initialization rates were <50%** over the three-month study
  period and **decreased over time**."
- Over the 84-day window, adults provided data on a mean of **43 days (SD 33.2)** and adolescents
  **40 days (SD 25.7)** — roughly half.
- **Survey metadata was used as predictors**: lag from prompt to survey start, start-to-submission
  time, survey completed but not submitted until the next prompt, days since last survey, and count
  of extreme (0/10) responses. This is the "missingness as signal" pattern already established in
  the module by Wang 2021 ([`beiwe-inpatient-suicide-pilot.md`](profiles/beiwe-inpatient-suicide-pilot.md)).
- The authors state directly: "there was a significant amount of missing data, **even in the context
  of our paying participants** for completing surveys."

**Recommendation: profile LifeData in Module 2** (commercial EMA platform, `lifedatacorp.com`), then
build this study as a Module 3 entry. It is the module's largest smartphone-survey deployment and
its per-survey micropayment model is not represented anywhere else. Until then, do not add it to
`feasibility-matrix.md`.

### Rejected for depth-over-coverage — not full-text read this pass

Per your instruction to build 8–10 rather than all 27, the following were **not** full-text read and
their candidate-file rankings stand as **Reported**. Reasons are given so the next pass does not
re-derive them:

| # | Study | Reason not built |
|---|---|---|
| 5 | Straczkiewicz 2026, short prescribed exercises, N=329 | Strong candidate. Deferred to avoid three adjacent ALS-accelerometer profiles in one pass. **Highest-priority remaining item.** |
| 7 | van den Berg 2022, daily SF-36 micro-surveys, N=95 | **No PDF and no PMCID**; no OA route. Its 76% full-SF-36-vs-micro-survey comparison is genuinely novel for survey-burden design and is referenced from the Fu profile. **Needs institutional access.** |
| 9 | Lee 2024, vaping app, N=306 | Custom platform, not obviously a Module 1/2 technology — likely the same scope problem as Nock. **Check the platform identity before building.** |
| 10 | Karas 2024, ALS passive smartphone, N=63 | Beiwe, same disease and lab as three profiles already built; marginal added operational content over Beukenhorst and Johnson. |
| 11 | Pellegrini 2022, transdiagnostic, N=45 | Beiwe; per-group yield is the only novel angle. Moderate value. |
| 13 | Panda 2020, JAMA Surgery, N=139 | **PDF unobtainable** (see retrieval outcomes). Would need efetch XML; worth doing next pass — a 139-participant surgical Beiwe cohort. |
| 14 | Panda 2022, Ann Surg, N=99 | No PMCID, no OA route. |
| 15 | Straczkiewicz 2022, digital pill + Beiwe, N=24 | **No PMCID, no OA route** — and it is the only ingestible-sensor multi-device study in the set, so this is a real loss. Its self-described "focus on data quality" framing suggests high operational content. **Worth an institutional-access request.** |
| 17 | Vidal Bustamante 2024, N=55 | Beiwe + actigraphy; cohort composition only. |
| 18 | Boaro 2021, spine surgery GPS, N=39 | Beiwe; overlaps heavily with Cote 2019, now profiled. |
| 20 | Staples 2017, schizophrenia, N=17 | Early Beiwe, very small; historical value only. |
| 21 | Torous 2015, Mindful Moods, N=13 | Pre-Beiwe custom app — **same scope problem as Nock** (technology not profiled in Module 1/2). Historical baseline only. |
| 22 | Beukenhorst 2021, ALS COVID, N=8 | N=8; the operational point (continuity through a disruption) is narrative. |
| 23 | Nawabi 2025, glioblastoma, N=15 | No PMCID, no OA route; pilot scale. |
| 24 | Duey 2023, speech recordings, N=60 | No PMCID, no OA route. **The only audio/speech collection study in the set** — a genuine gap if it stays unbuilt. |
| 25 | Chung 2026, SMI daily surveys, N=56 | No PMCID, no OA route; platform not identified in the abstract (likely the same scope check as Nock). |
| 27 | Mahalingaiah 2022, Apple Women's Health Study | Design-and-methods paper. Large and important, but it is a protocol/architecture description rather than a deployment report; sits close to the `CLAUDE.md` exclusion for methods papers. **Judgement call — flag for your decision.** |

**Six of the eighteen unbuilt candidates (#7, #14, #15, #23, #24, #25) have no open-access route at
all.** That is a structural gap in this tranche, and it concentrates in exactly the venues that
publish surgical and psychiatric deployments (*Annals of Surgery*, *Neurosurgery*, *Psychiatry
Research*, *Quality of Life Research*).

---

## Errors caught in the staged candidate list

Four, of which two are material.

### 1. Cote 2019 — "105 patients enrolled (55 analyzed)" is wrong (material)

The candidate file called this "the clearest attrition signal in the set." **There is no 105→55
attrition.** All 105 enrolled participants were analysed and appear in Table 1. **55 (52.4%) is the
number who underwent a surgical intervention during follow-up.** The abstract's phrasing — "105
patients were enrolled with a median follow-up time of 94.5 days; 55 patients underwent a surgical
intervention during follow up" — is easy to misread from an abstract alone, which is precisely the
failure mode the candidate file warned about by labelling its rankings **Reported**. Corrected in
[`beiwe-spine-disease-mobility.md`](profiles/beiwe-spine-disease-mobility.md), with the correction
called out in the profile body.

The real funnel in that paper is better than the imagined one anyway: 216 approached → 90 excluded
for not owning a smartphone → 105 enrolled.

### 2. Liu 2019 — device attribution: it is the LAMP app, not Beiwe (material)

The candidate file lists "#19 Liu et al., technologies deployed: Smartphone cognitive assessments +
sensors (steps, sleep) + self-report" — ambiguous, and the surrounding context implies Beiwe. The
full text names it: participants completed assessments "by installing and running **our group's LAMP
smartphone app**," with source at `github.com/BIDMCDigitalPsychiatry/LAMP-app`. This is Torous's
BIDMC Division of Digital Psychiatry lineage — the direct predecessor of
**[mindLAMP](../module-02-digital-phenotyping/profiles/mindlamp.md)**, a separately profiled Module 2
platform. Profiled accordingly, and it improves the tranche's platform balance rather than worsening
it.

### 3. Nock 2026 — platform is LifeData, unprofiled (material for scope, not bibliography)

Covered above. The candidate file did not name a platform; the full text does.

### 4. Johnson 2023 — internal inconsistency in the candidate file's own naming (minor)

The candidate list correctly heads entry #2 as "Johnson SA et al." but the "Judgment calls" section
at the bottom refers to the same paper as "**#2 (Karas/Berry, npj Digital Medicine 2023)**." The
correct byline is **Johnson SA and Karas M as co-first authors** ("These authors contributed
equally"), with Berry JD as last author. Not a substantive error, but it would propagate into
citations.

### Also corrected in passing

- **Wright 2018 (#8)** — the candidate file says "Beiwe (PROs) + wearable accelerometers." The
  wearables are specifically a **Fitbit Zip (waist) and a Fitbit Charge 2 (wrist)**, both managed
  through **Fitabase**. Fitbit is a profiled Module 1 device, so this study cross-links to
  [`fitbit-google.md`](../module-01-wearables/profiles/fitbit-google.md) — it is a genuine
  Module 1 × Module 2 multi-device deployment, not a generic-accelerometer study.
- **Yi 2025 published typos** (not the candidate file's error): Table 3's header states N=1,276
  where the text and every row total give **1,267** (=181×7); and GPS invalid days render as
  "142 (11,21)" for 11.21%. Neither affects a conclusion; both are noted in the profile so a future
  reader re-deriving the arithmetic does not think they have made a mistake.

### Two technologies surfaced that are not profiled in Module 1 or 2

Flagged, per the `CLAUDE.md` rule, rather than absorbed:

- **Modus Health StepWatch 4** (ankle-worn step monitor) — a primary instrument in Johnson 2023.
  **Module 1 expansion candidate.**
- **Z4IP** (NUS Centre for Sleep and Cognition EMA/time-use app) — the sole active-data instrument
  in Soon 2025. **Module 2 expansion candidate.**
- **LifeData** — the platform in Nock 2026. **Module 2 expansion candidate**, and the blocker on
  building the largest study in the tranche.

---

## Retrieval outcomes

**Mercier 2020 and Cote 2019: full text obtained, PDF not.** Both are NIHPA author manuscripts
outside the PMC open-access subset (Europe PMC `isOpenAccess: N`). Three routes were tried:

| Route | Result |
|---|---|
| Europe PMC `fullTextXML` | Empty (0 bytes) for both |
| Europe PMC `?pdf=render` | **HTTP 500** for both (the same failure the cataloguing pass hit) |
| PMC direct PDF endpoint | Returns an HTML **proof-of-work bot challenge**, not a PDF |
| **NCBI efetch `db=pmc&retmode=xml`** | **Worked for both** — complete body text and all tables |

The PMC PDF route is now gated behind a computational bot challenge. Solving it would be
circumventing bot detection, so it was not attempted. **efetch XML is the working route for
NIHPA/JAMA-family author manuscripts and should be the documented default** — it carried everything
in both papers except raster figures.

**One consequence worth recording:** Mercier's Figure 1 is the participant-flow diagram holding the
**denominators for the 50%/78% incentive comparison**. It is a raster image and could not be read
by any available route. Those denominators remain unrecovered. An institutional-access PDF would
resolve it, and it is worth doing — it is the difference between a citable effect estimate and a
citable observation.

**No new PDFs were added to `literature/`.** Seven of the nine profiled studies already had full
texts in the repository (five in `module-02-digital-phenotyping/literature/onnela-lab/`, two in
`module-01-wearables/literature/`); those are linked by path, not copied. The remaining two have no
obtainable PDF.

**Supplementary material not retrieved** (noted in the relevant profiles, and worth a follow-up
pass): Straczkiewicz 2024 Section 2.3 (the wear-threshold sensitivity detail behind the 202/240/308
result), Soon 2025 Supplementary Methods / Table S1 / Figure S1 (the additional wear filtering and
the compliance-stratified bias check), and Johnson 2023's supplementary tables.

---

## Does this tranche tilt the module toward Beiwe?

**Yes — and materially, though less than it would have if the ranking had been followed literally.**

### The arithmetic

Before this pass the Module 3 baseline held **Beiwe 5, RADAR-base 4, mindLAMP 1**, plus device-side
studies. After this pass:

| Platform | Baseline | This pass | Total |
|---|---|---|---|
| **Beiwe** | 5 | **+6** | **11** |
| RADAR-base | 4 | 0 | 4 |
| mindLAMP (incl. LAMP predecessor) | 1 | +1 | 2 |
| AWARE / Avicenna / MetricWire / m-Path / CARP | 0 | 0 | **0** |
| Device-only (no Module 2 platform) | 9 | +2 | 11 |

**Beiwe now appears in 11 of 28 Module 3 profiles (39%), against 4 for RADAR-base and 2 for the LAMP
family.** Nine of those eleven are Onnela-lab-authored. Within this pass specifically, six of nine
profiles involve Beiwe.

### Why the tilt is real and not merited by the evidence

The tranche is drawn from **one lab's publication list**. That is a sampling frame, not a quality
signal. Nothing in the full texts read this pass suggests Beiwe outperforms RADAR-base, mindLAMP or
any commercial platform on any operational dimension — and several findings cut the other way (the
17.7% zero-response rate in Yi 2025, the 51% active-data completion in Fu 2024, the participant
describing surveys that simply did not render, the Android 4.3 incompatibility in Wright 2018, the
OS update that broke the app mid-study in Yi 2025).

Three specific risks that a reader of the module could now fall into:

1. **Sample-size illusion.** Eleven Beiwe entries against four RADAR-base entries could be read as
   "Beiwe is the better-evidenced platform." It means Beiwe's originating lab publishes prolifically
   and the discovery method sampled that lab exhaustively. The `feasibility-matrix.md` and
   `README.md` should say so where the platform counts appear.
2. **Correlated-authorship illusion.** Nine of the eleven Beiwe entries share an author. Their
   methodological conventions, reporting habits, populations (heavily ALS and Boston-area clinical
   cohorts), and even their sampling configurations are correlated. **Eleven Beiwe studies are not
   eleven independent observations of Beiwe.**
3. **Vintage illusion.** Every Beiwe figure in this tranche is **pre-heartbeat** — the newest
   collection window closes in 2023, and Beiwe's server-side keepalive was globally enabled
   2024-05-29. So the module's Beiwe evidence base is simultaneously the largest and the most
   systematically dated. Every Beiwe profile built here carries an explicit pre-heartbeat
   lower-bound label.

### What I did to reduce it, within the brief

- **Built three non-Beiwe profiles** where the ranking would not have produced them (Straczkiewicz
  ActiGraph at #6, Soon Oura at #16, Liu LAMP at #19) — and two of the three now carry
  higher-value findings than several of the Beiwe entries.
- **Reclassified Liu 2019 out of the Beiwe column** on device attribution, which is a correction,
  not a balancing exercise, but it happens to help.
- **Excluded Nock 2026** on the scope rule despite it being the largest study available, rather than
  bending the rule.
- **Named the COI explicitly in every profile**, with a specific analysis of which claims it could
  and could not distort, and **stated in each one whether the finding is Beiwe-specific or general**
  to smartphone sensing. It is worth recording that in every case examined this pass, **the
  transferable findings were platform-general**: incentive structure, clinician gatekeeping,
  smartphone-ownership exclusion, onboarding failure, wear-time definitions, recruitment channel.
  None of the tranche's genuinely useful operational findings depend on Beiwe.

### Recommendation

`README.md`'s "What's missing" section already warns that building this tranche alone "would make
[the Beiwe tilt] worse rather than better." **It has.** Before the next Onnela-derived tranche is
built, the module needs the AWARE / Avicenna / MetricWire / m-Path / CARP pass that
`_inventory-and-scope-decisions.md` recommends — and, when `feasibility-matrix.md` is updated with
these nine rows, a standing note that the Beiwe row count reflects one lab's publication volume and
one discovery pass, not comparative evidence quality.
