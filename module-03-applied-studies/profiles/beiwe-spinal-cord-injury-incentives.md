# Mercier et al. 2020 — Beiwe after spinal cord injury: retention before vs. after a financial incentive was introduced, N=43

## Quick Facts

| Field | Details |
|---|---|
| Citation | Mercier HW, Hamner JW, Torous J, **Onnela JP**, Taylor JA. "Digital Phenotyping to Quantify Psychosocial Wellbeing Trajectories After Spinal Cord Injury." *American Journal of Physical Medicine & Rehabilitation* 2020;99(12):1138–1144. DOI [10.1097/PHM.0000000000001506](https://doi.org/10.1097/PHM.0000000000001506). PMC7680265 (NIHPA author manuscript). |
| Study design | Prospective methodological/feasibility study across two recruitment streams: (1) participants starting hybrid functional electrical stimulation row training (FESRT) at an outpatient exercise programme, and (2) newly-injured adults followed from inpatient-rehabilitation discharge into community reintegration (CRG). Weekly measurement, first 16 weeks analysed. |
| Sample size (enrolled / analyzed) | **105 approached → 43 enrolled → 24 not recorded as dropping out → 15 with "complete data"** (≥70% of surveys submitted). See Recruitment and Retention. |
| Population | Community-living adult wheelchair users with spinal cord injury. Mean age 40.0 (SD 16.4); 77% male; 77% White; median SCI duration 4.3 months (range 1.2 months – 43.7 years); injury levels C1–T12; 30% motor-complete tetraplegia. Exclusion: SCI due to suicide attempt. |
| Duration | 4 months per participant (16 weeks analysed), weekly measurement. Enrolment April 2017 – July 2019, across 27 months of an ongoing study. |
| Devices/platforms used | **[Beiwe](../../module-02-digital-phenotyping/profiles/beiwe.md)** only — participants' own smartphones (BYOD, Android or iOS). GPS + weekly survey battery. |
| Funding/COI | Craig H. Neilsen Foundation, Harvard Spaulding PM&R, NIDILRR (90SI5021), NIH Director's New Innovator Award (DP2MH103909). **Onnela (Beiwe's originator) and Torous are co-authors**; both declare an Otsuka-supported research grant unrelated to this study. Discussed under Evidence Confidence. |
| Last verified | 2026-09-01 |

## Summary

This is the only study identified so far in Module 3 that reports **retention before and after a
financial incentive was introduced into the same protocol** — and it is therefore the closest thing
the module has to an estimate of what money buys in a smartphone phenotyping deployment.

The study did not set out to test incentives. It began with no compensation, observed attrition it
considered unacceptable, and obtained IRB approval mid-study to pay **$30 per two-month block to
participants who completed at least 70% of surveys**. Retention rose from **50% to 78%**.

Two things make that number more useful than a headline comparison usually is, and one thing makes
it much weaker. More useful: the change was made inside one protocol, one site network, one
population, with the same app and the same survey battery, so most of the usual confounds between
"supported" and "unsupported" studies are held constant; and the authors report that the incentive
**did not change the sample's demographics**, so it is not obviously a recruitment-composition
effect. Much weaker: this is a **before/after comparison, not a randomised arm**. The pre-incentive
and post-incentive groups are separated in calendar time, so any co-occurring change in study
conduct, staffing, or population mix is confounded with the incentive, and the paper does not
publish the denominators for the two percentages (they appear only inside Figure 1, which is an
image in the author manuscript).

The study's second, subtler finding is arguably more transferable: **the incentive bought retention
but not engagement.** The authors state plainly that "the conditional remuneration did not
apparently incentivize survey response behaviors because percentage of complete surveys did not
increase." People stayed enrolled; they did not answer more.

## Instrumentation and Deployment Model

**BYOD, both operating systems.** Eligibility required demonstrating independent use of one's own
smartphone "using hands or adapted devices" — an accessibility screen, not a technology screen, and
notable given 30% of the cohort had motor-complete tetraplegia. Nine participants had high cervical
(C1–C4) injuries and all demonstrated independent smartphone use to study staff.

**Passive stream — GPS only, at an unusually sparse duty cycle:**

- **2-minute epochs spaced 18 minutes apart**, i.e. roughly 3 fixes per hour, and explicitly
  described as triggered "based on phone movement and usage."
- Fixes with accuracy worse than **20 m** were discarded before an accuracy-weighted 5-minute moving
  average.
- DBSCAN clustering separated visited locations from travel; a "location" required ≥4 points (≥20
  minutes) within 50 m. Home was assigned post hoc as the location with most time between midnight
  and 04:00 across the whole collection period; exercise and medical locations were identified via
  OpenStreetMap.
- Distance travelled was a rough estimate (sum of straight lines between locations) — the authors do
  not claim it as a true path length.

**Active stream — a weekly battery of 10–15 minutes**, delivered via a persistent notification and
answerable at any time during the week:

- PHQ-8, modified to reference the previous 7 days, plus an interference item.
- SCI-QOL Ability to Participate in Social Roles and Activities, and Satisfaction with SRA.
- A health-events checklist (hospitalisation, new infection, new musculoskeletal injury, new
  illness, mobility-equipment change or malfunction).
- Leisure Time Physical Activity Questionnaire for SCI, modified — frequency and intensity of ≥10
  minute bouts, excluding therapy and wheelchair propulsion for transport.

**Accessibility design worth copying:** "whenever possible, the number of required screen taps was
restricted to facilitate usability among those with limited hand function," and notifications were
spaced across the week rather than clustered. The study also placed a **"Call Crisis Clinician"
button on the app home screen**, with participants explicitly told at consent that responses were
not reviewed in real time — a safety-design pattern any study collecting PHQ-8 passively should
note.

**Engagement scaffolding beyond the incentive:** study staff **contacted participants after two
missing weeks** of survey or sensor data. That contact existed both before and after the incentive
change, so it is held constant across the 50%/78% comparison.

## Recruitment and Retention

**Enrolment funnel over 27 months at an outpatient exercise programme and an inpatient
rehabilitation discharge pathway:**

| Stage | N |
|---|---|
| Approached to determine eligibility | **105** |
| Enrolled | **43** (41%) |
| — from FESRT (exercise) stream | 19 |
| — from CRG (community reintegration) stream | 24 |

Stated reasons for not enrolling, in the authors' order of frequency: anticipating that **walking
would become their primary means of mobility before study end**; **no interest in research**; then
insufficient hand function, **concern for privacy**, and not owning a personal smartphone. The
walking-recovery reason is specific to this population and is a genuine eligibility trap for
rehabilitation studies that define their cohort by current mobility device.

**Attrition:**

| | N |
|---|---|
| Enrolled | 43 |
| Dropped out by 2 months | **14** |
| Dropped out between 2 and 4 months | **5** |
| Not recorded as dropping out | 24 |
| **Completed 4 months of data (≥70% of surveys)** | **15 (35% of enrolled)** |

Note the two definitions diverge sharply: 19/43 (44%) formally dropped out, but only **15/43 (35%)**
met the study's own "complete data" bar. The nine-participant gap is people who remained enrolled
while contributing too little to analyse — the same phenomenon
[Beukenhorst et al.](beiwe-als-adherence.md) documented in ALS, where eventual dropouts were
already near-silent while nominally enrolled.

**The incentive comparison — the reason this profile exists:**

> "Initially this study did not offer compensation to participants, however this was revised with
> IRB approval to promote study retention. After this revision, participants who completed at least
> 70% of surveys received a $30 check payment after each two-month period of enrollment."
>
> "After providing compensation, study retention increased from **50% to 78%**."

**What the incentive did and did not change:**

| Outcome | Before incentive | After incentive |
|---|---|---|
| Study retention | **50%** | **78%** |
| Percentage of surveys completed | — | **no increase** (authors' explicit statement) |
| Sample demographics | — | **similar** (authors' explicit statement) |
| Stated dropout reasons | time demands (6), medical complications (4), limited hand function (4), lost to follow-up despite multiple contacts (6) | one lost to follow-up; one withdrew wanting more privacy |

The qualitative shift in dropout reasons is as informative as the percentages. Pre-incentive, the
dominant reason was **time demands** and a large block of silent loss-to-follow-up. Post-incentive,
loss to follow-up essentially disappeared from the record. That is consistent with an incentive
working by making the ongoing relationship worth maintaining, rather than by making any given survey
easier.

**Who dropped out — the predictor profile, which is unusually informative here:**

| Characteristic | Dropped out | Completed | p |
|---|---|---|---|
| CRG (newly injured) vs FESRT (exercise) | 63% vs 21% | — | <0.05 |
| Age, years | 44.4 (17.1) | 36.5 (15.2) | 0.12 |
| Baseline ability to participate in SRA (T-score) | 39.9 (5.6) | 45.9 (7.4) | <0.05 |
| Baseline satisfaction with SRA (T-score) | 42.3 (4.7) | 48.5 (6.9) | 0.002 |
| Mild-intensity exercise sessions/wk | 2.6 (2.7) | 4.3 (2.3) | <0.05 |
| Moderate-intensity sessions/wk | 0.7 (1.3) | 3.2 (2.4) | <0.05 |
| High-intensity sessions/wk | 0.3 (0.8) | 1.9 (2.3) | <0.05 |
| Neurological level of injury | no difference | | |
| **Baseline depression severity** | **no difference** | | |

Two results here matter beyond SCI. First, **neurological level of injury did not predict
attrition** — the authors read this as evidence that "touchscreen interactions [are of] manageable
burden even among those with partial hand function," which is a meaningful accessibility finding for
a population often excluded from smartphone research on assumption. Second, **baseline depression
severity did not predict dropout**, joining the null results in
[Beukenhorst 2022](beiwe-als-adherence.md) and
[Matcham 2022](radar-mdd-recruitment-retention.md) — baseline clinical severity keeps failing to
predict attrition, while *social* and *behavioural* baseline variables (social participation,
exercise frequency) predict it strongly here.

## Data Completeness and Technical Issues

**Survey completion, by recruitment stream:**

| | Completed 4 months of data | Survey completion rate |
|---|---|---|
| FESRT (exercise programme) | 10/19 (**53%**) | **57%** |
| CRG (community reintegration) | 5/24 (**21%**) | **25%** |

**The stream effect is larger than the incentive effect.** A 2.5× difference in completion between
two arms of the same study, on the same platform, in the same disease. The authors attribute it to
the situation rather than the technology: newly-injured people leaving inpatient rehabilitation are
in "a dynamic period" with major life adjustment, less clinical and peer support, and (in this
cohort) more severe depression. The FESRT participants were already attending a structured
outpatient exercise programme — i.e. they had an existing, recurring, in-person touchpoint with the
research setting.

For study design, that is the more actionable finding: **an existing routine contact structure
appears to be worth more than a payment**, and the two are separable.

**Characteristics of participants with complete data** (≥70% surveys, n=15): longer SCI duration
(89.4 vs 7.1 months, p=0.005), greater ability and satisfaction with social participation, more
frequent physical activity at all intensities. In other words the analysable subsample is
systematically *further from injury, more socially engaged, and more active* than the enrolled
sample — a selection gradient that runs in the same direction as the dropout gradient and compounds
it.

**Technical issues the paper documents:** unreliable GPS fixes were discarded at a 20 m accuracy
threshold before any analysis (volume not reported); the authors note in limitations that
"imputation methods for within-individual GPS processing could decrease error variance due to
missing data," implying GPS missingness was material but they do not quantify it. **No
participant-level GPS completeness figure is published** — a real gap in an otherwise operationally
detailed paper.

**Sample-size planning, worth recording:** the study used the Onnela Lab's public
[digital phenotyping sample size calculator](https://onnela-lab.shinyapps.io/digital_phenotyping_sample_size_calculator/),
**assuming 50% missing data** and α=0.05. Forty individuals would give 99% power for a modest
correlation of depression with the seven other weekly measures; ten individuals would give 69%. They
enrolled 43 and analysed 15. That is a concrete instance of a planning assumption (50% missingness)
being roughly right at the *day* level and badly wrong at the *participant* level.

## Feasibility Findings

The authors' stated conclusion is deliberately hedged: digital phenotyping after SCI is "feasible
but not without attrition challenges," and "higher attrition among acute SCI suggests a need for
even less obtrusive smartphone platform."

Their own explicit recommendations:

1. **Consider passive-only monitoring for burdened populations.** "One of the most common reasons
   for drop out was time constraints and so monitoring psychosocial wellbeing via passive smartphone
   sensor data that does not require participant input may be warranted." (Read against
   [Beukenhorst 2022](beiwe-als-adherence.md)'s finding that passive-only smartphone collection is
   not architecturally possible pre-heartbeat — these two recommendations are in tension, and
   Beukenhorst's is the binding constraint.)
2. **Use branching logic** to select items based on current mood, reducing per-survey burden.
3. **Add speech-to-text survey response** to improve accessibility for limited hand function.
4. **Impute GPS within-individual** to reduce error variance from missingness.

They also record a null that matters for recruitment ethics: the IRB determined the $30 payment
"would not unduly influence participation," and the authors observed the incentive **did not alter
the demographic composition of the sample**.

## Relevance to Future Study Design

1. **This is the module's incentive number: retention 50% → 78% within one protocol.** Treat it as a
   *before/after* estimate, not a randomised effect. It is the best available evidence in this
   module, and it is weak evidence.
2. **Pay for retention, not for engagement.** The incentive kept people enrolled and did not raise
   survey completion at all. If the analytic requirement is dense per-person data rather than long
   follow-up, an incentive of this design will not deliver it.
3. **Structure the incentive around a threshold you can actually monitor.** This study paid $30 per
   two-month block conditional on ≥70% survey completion — cheap, auditable, and aligned with the
   analytic sample definition. Total exposure at N=43 over 4 months is trivially small relative to
   the retention gained.
4. **An existing routine contact point beats a payment.** 53% vs 21% completion between the exercise
   programme and the community-reintegration streams, same platform, same protocol. Recruit through
   a setting participants are already returning to, if you can.
5. **Life-transition periods are the hardest recruitment windows, not the most valuable ones.** The
   newly-injured cohort was the scientifically interesting group and the one that could not sustain
   participation. Budget separate N for each.
6. **Screen on social participation and activity, not on clinical severity.** Baseline social
   participation, satisfaction with participation, and exercise frequency all predicted attrition;
   injury level and depression severity did not.
7. **Motor impairment is not automatically a barrier to touchscreen research.** Independent
   smartphone use was demonstrable in participants with high cervical injuries, and attrition did
   not vary by neurological level. Screen for it; do not assume it.
8. **Distinguish "did not drop out" from "usable data" in the protocol, not after the fact.** 24/43
   remained but only 15/43 met the completeness bar. Publishing both is what makes this study
   useful; most studies publish only the flattering one.

## Evidence Confidence

**Verified** for enrolment (105 approached, 43 enrolled), the attrition counts (14 by 2 months, 5
between 2 and 4), the 15 participants with complete data, the FESRT/CRG completion split (53%/21%,
57%/25% surveys), the dropout predictor table, the GPS duty cycle and processing pipeline, and the
$30/70%/two-month incentive structure — all read directly from the full text.

**Reported, with a specific weakness, for the headline 50% → 78% retention figure.** The numbers are
stated in the abstract, the results, and the discussion of the published paper, so the *claim* is
firmly attributable. But: (a) it is a **before/after comparison within an ongoing study, not a
randomised arm**, so calendar-time confounding is unresolved and unresolvable from the published
material; (b) the **denominators are not in the text** — they appear only in Figure 1, a raster
image in the NIHPA manuscript that this pass could not read, so the precision of the two percentages
cannot be checked; (c) with 43 participants total, the two subgroups are small enough that a
handful of participants moves either figure by 5–10 points. Cite it as *"one before/after comparison
inside a single 43-participant study reported retention rising from 50% to 78% after a conditional
$30/2-month incentive was introduced"* — not as an effect estimate.

**Verified** for the accompanying null: the authors state directly that survey completion percentage
did not increase and that sample demographics were similar pre- and post-compensation.

**Unclear** for GPS data completeness. No participant-level or day-level GPS yield is published,
despite GPS being the paper's passive stream. Any claim about Beiwe's passive performance in this
population would be unsupported.

**Pre-heartbeat.** Data collection ran April 2017 – July 2019 (enrolment), well before Beiwe's
server-side heartbeat/keepalive push was globally enabled on 2024-05-29. Every completeness-related
observation here is a **pre-heartbeat lower bound**, not current platform performance. See
[`beiwe-als-adherence.md`](beiwe-als-adherence.md) for the mechanism and Tier 14 Q106 in
`../../shared/unresolved-questions.md`.

**COI, and what it could and could not distort.** **Onnela, Beiwe's originator, is a co-author**, as
is Torous, who leads a separate digital-psychiatry platform effort. The claims most exposed to that
COI would be comparative ones ("Beiwe performed better than X") — and the paper makes none. What it
reports instead is 44% attrition, a 35% analysable rate, an explicit statement that its own platform
was insufficiently unobtrusive for the acute-SCI group, and a recommendation for a "less obtrusive
smartphone platform." The incentive finding itself is a **study-conduct** result, not a platform
result: nothing about a $30 conditional payment is specific to Beiwe, and the same manipulation on
mindLAMP, RADAR-base, or a bespoke app would be expected to behave similarly. That is the strongest
argument for taking this particular number at face value despite the authorship.

**Generalisability.** N=43, single health-system network (Partners/Mass General Brigham), 77% male,
77% White, and an eligibility criterion requiring personal smartphone ownership and independent
operation. The authors themselves flag that they collected **no data at all** on the demographics or
socioeconomic status of the 62 people who were approached but not enrolled, and speculate — without
evidence — that "individuals from marginalized communities experience greater surveillance in public
situations and may be more likely to avoid a research study that collects GPS data." That is an
untested hypothesis worth carrying forward, not a finding.

## Key Links

- Paper (subscription; author manuscript free in PMC): https://doi.org/10.1097/PHM.0000000000001506
- Europe PMC record: https://europepmc.org/article/PMC/PMC7680265
- Onnela Lab digital phenotyping sample-size calculator (used by this study):
  https://onnela-lab.shinyapps.io/digital_phenotyping_sample_size_calculator/
- **Local PDF: none.** This is an NIHPA author manuscript outside the PMC open-access subset
  (`isOpenAccess: N`); Europe PMC's `?pdf=render` route returns HTTP 500 and PMC's own PDF endpoint
  is behind a proof-of-work bot challenge. **Full text was obtained instead via NCBI efetch XML**
  (`db=pmc&id=7680265&retmode=xml`), which carries the complete body and Table 1. Figure 1 (the
  participant-flow diagram holding the incentive-arm denominators) is a raster image and was not
  recoverable.

## Related profiles

- Platform: [Beiwe](../../module-02-digital-phenotyping/profiles/beiwe.md)
- **Direct counterpoint — an explicitly unpaid deployment**, where the clinical group out-engaged
  healthy controls: [`lamp-schizophrenia-cognition-unpaid.md`](lamp-schizophrenia-cognition-unpaid.md)
- Unpaid, unsupported Beiwe baseline in a progressive disease:
  [`beiwe-als-adherence.md`](beiwe-als-adherence.md)
- Uncompensated Beiwe at scale: [`beiwe-chronic-disease-substudy.md`](beiwe-chronic-disease-substudy.md)
- Paid, monitored, clinic-embedded Beiwe with a dismissal rule:
  [`beiwe-pain-clinic-operational-report.md`](beiwe-pain-clinic-operational-report.md)
- Heavily compensated wearable deployment (~USD 263/participant) for contrast:
  [`oura-university-freshmen-sleep.md`](oura-university-freshmen-sleep.md)
- Compensated, contact-supported platform contrast:
  [`radar-mdd-recruitment-retention.md`](radar-mdd-recruitment-retention.md)

## Sources

1. Mercier HW, Hamner JW, Torous J, Onnela JP, Taylor JA. *Am J Phys Med Rehabil*
   2020;99(12):1138–1144. DOI 10.1097/PHM.0000000000001506. Full text and Table 1 read from the
   NCBI efetch PMC XML render of PMC7680265, 2026-09-01. Establishes every figure in this profile
   except where noted as unrecoverable from Figure 1.
