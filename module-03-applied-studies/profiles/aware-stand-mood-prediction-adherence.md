# Balliu et al. 2024 — STAND: AWARE in a university depression treatment programme, N=437 enrolled / 183 modelled, up to 40 weeks

## Quick Facts

| Field | Details |
|---|---|
| Citation | Balliu B, Douglas C, Seok D, Shenhav L, Wu Y, Chatzopoulou D, Kaiser W, Chen V, Kim J, Deverasetty S, Arnaudova I, Gibbons R, Congdon E, Craske MG, Freimer N, Halperin E, Sankararaman S, Flint J. "Personalized mood prediction from patterns of behavior collected with smartphones." *npj Digital Medicine* 2024;7:49. DOI [10.1038/s41746-024-01035-6](https://doi.org/10.1038/s41746-024-01035-6). PMID 38418551 / PMC10902386. |
| Study design | Prediction/modelling study nested in the **STAND** treatment programme (UCLA Depression Grand Challenge). Two enrolment waves with different protocols and treatment durations. Includes a **dedicated adherence analysis** — a Results section with formal tests of adherence against wave, treatment arm, follow-up time, sex and age. |
| Sample size (enrolled / analyzed) | **437 installed AWARE and had ≥1 CAT-DI assessment → 238 with ≥5 assessments → 189 also with ≥60 days of sensor data → 183 also showing CAT-DI variation.** Wave 1 N=182; Wave 2 N=142 mild-moderate + 124 severe; 11 people participated in both waves. |
| Population | **UCLA students** aged ≥18 with internet access and English fluency, experiencing mild-to-severe depression or anxiety symptoms. **76.5% female, 26.5% White.** Routed by baseline CAT-DI severity: mild/moderate → online support ± peer coaching; severe → in-person clinician care. |
| Duration | Wave 1 up to **20 weeks** (Apr 2017 – Jun 2018); Wave 2 up to **40 weeks** (from academic year 2018, running three years, overlapping the Los Angeles Safer-At-Home order from March 2020). |
| Devices/platforms used | **[AWARE](../../module-02-digital-phenotyping/profiles/aware-framework.md)** only — BYOD smartphone, location / screen state / call and SMS logs. Mood measured by **CAT-DI** (Computerized Adaptive Testing Depression Inventory), delivered online, not through AWARE. No wearable. |
| Funding/COI | NSF #1829071; NIH R35GM125055; NSF III-1705121 and CAREER-1943497; NIH R01MH122569. **COI: "Dr. Gibbons is a founder of Adaptive Testing Technologies, who is the licensor of the CAT-DI."** The instrument-vendor relationship is on the *outcome measure*, not the sensing platform; no AWARE developer is an author. |
| Last verified | 2026-09-02 |

## Summary

Primarily a machine-learning paper — it exists to show that idiographic (per-person) models predict depression severity far better than nomothetic ones. It earns a Module 3 entry on the strength of a single section, **"Adherence to CAT-DI assessment protocol"**, which reports the module's largest natural experiment on **whether the surrounding care model determines retention**.

Participants were assigned to treatment arm by symptom severity, not by research design — but the two arms differed in exactly the variable this module cares about. The severe group received **regular in-person clinical sessions**; the mild-to-moderate group received **online support only**. The result:

> **Two-week attrition from the assessment protocol: 1.7% in the in-person clinical-care arm versus 33.5% (Wave 1) and 37.3% (Wave 2) in the online-support arm.**

**A roughly 20× difference in early attrition, with the sicker group retaining better.** The authors give the mechanism directly: clinical-care participants "had regular in-person treatment sessions during which they were instructed to complete any missing assessments."

This is the strongest evidence in the module for cross-cutting pattern 5 (*support intensity, not participant capability, drives the numbers*) and it simultaneously reproduces pattern 3 in an inverted form: **more severe illness predicted better, not worse, adherence** — because severity determined the care model.

Overall protocol adherence was nonetheless poor: **4,507 CAT-DI assessments delivered against 11,218 expected — 40.2%.**

The second contribution is a **structural, stream-specific OS asymmetry**: SMS-derived features could not be computed on iOS at all, so they exist for **only 15 of 183 participants (8.2%)**.

## Instrumentation and Deployment Model

**BYOD, and installation was compulsory.** All STAND participants were offered "behavioral health tracking through the AWARE framework and had to install the app in order to be included in the study." Eligible participants who **refused to install AWARE were excluded** — a rarely-stated recruitment gate that pre-selects on willingness to be sensed. The module has no comparable measurement of how many refused.

**Streams collected:** location (GPS), screen on/off, and counts of incoming and outgoing SMS and calls. Narrower than most AWARE deployments here — no accelerometer, Bluetooth, Wi-Fi, app-usage or notification streams.

**Feature engineering, and its operational assumptions:**

- Location clustered hierarchically (chosen over k-means and DBSCAN specifically for its "ability to deterministically assign clusters... independent of occasional data missingness"), 400 m maximum cluster radius, locations under 15 min/day discarded, and **positions linearly interpolated to every 3 minutes to paper over irregular GPS arrival**. That interpolation is a data-loss mitigation baked into the feature pipeline; anyone reusing these features is inheriting it.
- Sleep and circadian features derived **from phone-interaction logs, not from a wearable** — last night-time interaction as bedtime proxy, first morning interaction as waketime, longest phone-off period as sleep duration. Cheap, and entirely dependent on the participant's phone habits.
- 23 activity + 18 social-interaction + 13 sleep + 2 device-usage daily features, expanded to **1,325 features** by adding relative-change transforms.

**Two imputation passes, and their scale.** Daily feature values were imputed with AutoComplete and softImpute, **resulting in 29,254 days of logging events** across 183 individuals — against 3,005 actual CAT-DI mood assessments. The mood outcome was itself interpolated with cubic splines to produce daily targets. **The published prediction accuracies are computed on a heavily imputed and interpolated dataset**, which the authors are transparent about and handle carefully (splines fitted on training data only), but which any reader of the R² figures should hold in mind.

**No incentive is described.** Participation was embedded in an offered treatment programme.

## Recruitment and Retention

**The analytic funnel** (each step is an inclusion criterion, not attrition per se, but the effect on N is the same):

| Stage | n |
|---|---|
| Installed AWARE, ≥1 CAT-DI assessment | **437** |
| ≥5 CAT-DI assessments | 238 |
| **and** ≥60 days of sensor data in the overlapping period | 189 |
| **and** CAT-DI variation in the training set | **183** |

**58.1% of the enrolled cohort did not reach the analytic sample.** The single largest cut (437→238, 45.5%) is the ≥5-assessment requirement — i.e. it is an *adherence* filter, not a technical one. The 238→189 step (20.6%) is the **≥60 days of sensor data** requirement and is the closest thing this paper gives to a passive-completeness figure.

**Adherence to the assessment protocol:**

| Metric | Value |
|---|---|
| CAT-DI assessments provided / expected | **4,507 / 11,218 = 40.2%** |
| Two-week attrition — in-person clinical care | **1.7%** |
| Two-week attrition — online support, Wave 1 | **33.5%** |
| Two-week attrition — online support, Wave 2 | **37.3%** |
| Median assessments per analysed participant | 13 |
| Median follow-up per analysed participant | **171 days** |
| Median days between assessments | 10 (protocol: 7 or 14) |

Adherence varied significantly by wave (LRT P<2.2×10⁻¹⁶), treatment group (P<2.2×10⁻¹⁶) and follow-up time (P=1.29×10⁻⁶). After the first two weeks, attrition in the online-support arms was **linear** — no further cliff.

**Demographic predictors of adherence, and they do not replicate across waves:**

| Predictor | Finding |
|---|---|
| Male sex, online support, Wave 1 | **less** likely to complete all assessments (OR 0.86, P=2.9×10⁻⁴) |
| Male sex, online support, Wave 2 | **more** likely (OR 1.31, P=3.1×10⁻¹¹) |
| Male sex, clinical care | no association |
| Older age, online support, Wave 2 | **more** likely (OR 1.13, P<2.2×10⁻¹⁶) |
| Older age, Wave 1 or clinical care | no association |

**The sex effect reverses direction between two waves of the same study, at the same institution, on the same platform, both with p-values below 10⁻³.** This is the strongest available warning in the module against porting demographic adherence predictors between cohorts. Note also that "older" here spans a university student body, so the age effect covers a narrow range.

## Data Completeness and Technical Issues

**Definitions used:**

- *Adherence* — **CAT-DI assessments completed ÷ assessments expected by the protocol.** An active-stream definition, and the only adherence metric the paper reports.
- *Sensor-data sufficiency* — **≥60 days of sensor data** within the window covered by that participant's CAT-DI assessments. Used only as an inclusion filter; the underlying per-participant completeness distribution appears in a supplementary figure and is not stated numerically in the main text.
- Missing daily features were **imputed**, not excluded, under an explicit missing-at-random assumption.

**The OS asymmetry, and it is structural rather than behavioural:**

> "Due to OS restrictions, sensors needed to extract text message features are not available on iOS devices and were only computed for the **15 participants with Android devices**."

This is a **stream-specific, hard OS gate**: the SMS stream simply does not exist on iOS, so 168 of 183 participants (91.8%) contribute nothing to any SMS feature. It is a different phenomenon from the *yield* asymmetries reported by [McClaine 2024](aware-chemotherapy-engagement.md) (Android lower) and [Wu 2023](aware-alcohol-liver-disease-craving.md) (Android higher), and from the *survey-delivery* asymmetry [McInerney 2024](beiwe-type-2-diabetes-feasibility.md) found on Beiwe. It supports the module's current framing — **name the stream before stating an OS effect** — and adds a third category: streams that are OS-exclusive by platform policy, where the correct planning response is not mitigation but either accepting an 8% subsample or dropping the feature.

It also implies the cohort was **roughly 92% iOS**, which is unusually skewed and is not commented on in the paper.

**Missingness mechanism the authors name.** In defending the missing-at-random assumption they write that "the data is missing more often for participants that did not receive regular reminders" — i.e. **missingness tracks the support regime**, the same variable driving the attrition difference. That is a coherent account, but it means missingness is correlated with treatment arm and therefore with baseline severity.

**No app crashes, sync failures, battery-drain complaints or device-loss counts are reported.** No wearable was deployed, so no wear-time question arises.

## Feasibility Findings

The authors' framing is that the study "verified the feasibility of using passively collected digital behavioral phenotypes from smartphones to predict depressive symptoms weeks in advance". Their operational conclusions:

1. **Early attrition in online mental health studies is expected and large** — they call the two-week cliff "typical of online mental health studies" with a citation.
2. **The remedy they identify is contact:** participants in clinical care "were more adherent than those which received online support, despite endorsing more severe depressive symptoms. These participants had regular in-person treatment sessions during which they were instructed to complete any missing assessments **emphasizing the importance of using reminders or incentives for online mental health studies**."
3. **Prediction accuracy degraded past four weeks** (R² dropping below 70% after ~4 weeks ahead), and varied substantially across individuals. Individuals with more variable symptoms were harder to predict but benefited most from behavioural features.
4. They recommend **adding wearables** — devices "worn continuously" that "might measure behavior with less error" — as the next step, i.e. they regard smartphone-only sensing as the accuracy-limiting element.

## Relevance to Future Study Design

1. **The care model is the retention intervention.** 1.7% versus ~35% two-week attrition, in the same study, with the *sicker* arm retaining better. If a protocol already brings participants into a room periodically, use those contacts to reconcile missing assessments; if it does not, the module now has a price tag for that absence.
2. **A prediction paper's inclusion criteria are an attrition report in disguise.** 437 → 183 is a 58% loss, and the largest single cut is an adherence threshold. Read every ML paper's funnel this way before believing its cohort size.
3. **Do not port demographic adherence predictors between cohorts — not even between waves of your own study.** The sex effect here flips sign between Wave 1 and Wave 2 with p < 10⁻³ on both sides.
4. **Check which of your planned features are OS-exclusive before you design the analysis.** An SMS-based sociability feature on a predominantly-iOS cohort is an 8% subsample, not a feature.
5. **Compulsory app installation as an eligibility criterion pre-selects your cohort, and the size of that selection is almost never measured.** Record how many eligible people decline the sensing component.
6. **Interpolation and imputation choices are part of the deployment, not just the analysis.** 3-minute GPS interpolation and full daily-feature imputation are how this dataset absorbed its missingness; a study reusing the pipeline inherits both.

## Evidence Confidence

**Verified** — the 437/238/189/183 funnel; the 4,507-of-11,218 adherence figure; the 1.7% / 33.5% / 37.3% two-week attrition figures and their arm assignment; all LRT p-values and the sex/age odds ratios by wave and arm; the median 13 assessments, 171 follow-up days and 10-day inter-assessment gap; the 3,005 CAT-DI and 29,254 imputed feature-days; the 15-Android SMS restriction; the ≥60-day sensor inclusion rule; the compulsory-installation eligibility gate; and the CAT-DI COI. Read from the full text (Europe PMC PMC10902386), 2026-09-02.

**Reported** — the mechanism the authors give for the arm difference (in-session reconciliation of missed assessments). Plausible, stated by the authors, not experimentally isolated. Treatment arm is confounded with baseline severity by design, so this is not a randomised comparison of support intensity and should not be cited as one.

**Unclear** — per-participant passive data completeness (a supplementary figure only; no numeric statement in the main text); the number of otherwise-eligible participants who refused AWARE installation; the exact iOS/Android split of the full 437 (inferable only from the 15-of-183 SMS note); and how much of the reported prediction accuracy depends on the interpolation and imputation choices.

**Scope note.** This is a prediction/modelling paper and most of its content is out of Module 3's scope. It qualifies on the strength of its explicit adherence Results section, its published enrolment-to-analysis funnel, and the treatment-arm attrition contrast. **Cite it for the adherence findings; the ML results belong elsewhere.**

**Generalisability caution.** UCLA students, 76.5% female, 26.5% White, roughly 92% iOS, recruited into an offered treatment programme rather than a standalone research study — participants had a therapeutic reason to stay engaged that a pure observational cohort does not. Wave 2 overlaps the COVID-19 Safer-At-Home period; the authors found no significant COVID effect on CAT-DI variance but did not test it against adherence.

**COI:** author Robert Gibbons founds the company licensing the CAT-DI, the study's outcome instrument. No AWARE developer is an author and the paper makes no claims about the platform's merits.

## Key Links

- Paper (OA, CC BY): https://doi.org/10.1038/s41746-024-01035-6
- Europe PMC: https://europepmc.org/article/PMC/PMC10902386
- medRxiv preprint (same study): https://doi.org/10.1101/2022.10.12.22281007
- Local PDF: `../literature/2024-balliu-npjdigitalmedicine-personalized-mood-prediction-smartphones.pdf`

## Related profiles

- Platform: [AWARE](../../module-02-digital-phenotyping/profiles/aware-framework.md)
- Other AWARE deployments: [`aware-chemotherapy-engagement.md`](aware-chemotherapy-engagement.md), [`aware-momo-mood-mood-disorders.md`](aware-momo-mood-mood-disorders.md), [`aware-alcohol-liver-disease-craving.md`](aware-alcohol-liver-disease-craving.md)
- Stream-specific OS asymmetry: [`beiwe-type-2-diabetes-feasibility.md`](beiwe-type-2-diabetes-feasibility.md), [`carp-mpath-sense-performance-study.md`](carp-mpath-sense-performance-study.md)
- Support intensity as the dominant lever: [`mindlamp-linc-passive-data-quality.md`](mindlamp-linc-passive-data-quality.md), [`aware-momo-mood-mood-disorders.md`](aware-momo-mood-mood-disorders.md)
- Unpaid engagement in a care context: [`lamp-schizophrenia-cognition-unpaid.md`](lamp-schizophrenia-cognition-unpaid.md)
- Analytic-threshold-driven N: [`actigraph-als-upper-limb-wear-time.md`](actigraph-als-upper-limb-wear-time.md)

## Sources

1. Balliu B, Douglas C, Seok D, Shenhav L, Wu Y, Chatzopoulou D, Kaiser W, Chen V, Kim J, Deverasetty S, Arnaudova I, Gibbons R, Congdon E, Craske MG, Freimer N, Halperin E, Sankararaman S, Flint J. *npj Digit Med* 2024;7:49. DOI 10.1038/s41746-024-01035-6. Full text read from Europe PMC (PMC10902386), 2026-09-02. Byline verified against the publisher PDF. Establishes every figure in this profile.
