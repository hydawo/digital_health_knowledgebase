# Spangenberg et al. 2026 — Reactivity and feasibility of 7-month post-discharge EMA of suicidality (MetricWire Catalyst), interview sample n=16

## Quick Facts

| Field | Details |
|---|---|
| Citation | Spangenberg L, Spahn C, Serebriakova J, Forkmann T, Glaesmer H. "Qualitative content analysis of reactivity effects and feasibility of ecological momentary assessments of suicide-related thoughts and behaviors in the long-term and in suicidal crises." *Frontiers in Psychiatry* 2026;17:1744947. DOI [10.3389/fpsyt.2026.1744947](https://doi.org/10.3389/fpsyt.2026.1744947). PMID 41868844 / PMC13003599. |
| Study design | Qualitative content analysis (inductive–deductive, consensual coding) of interviews with a **purposively selected subsample** of a preregistered long-term EMA cohort study, stratified by high vs. low compliance and by suicide-related thought/behaviour (STB) occurrence during the study. |
| Sample size (enrolled / analyzed) | **16 interviewed**, drawn from the parent EMA cohort (parent-cohort N not stated in this paper). Of the 16, **7 stopped responding during the second phase**. |
| Population | Adults **18–75**, German-speaking, recruited **as inpatients** in seven psychiatric clinics in **Leipzig and the Ruhr area around Essen, Germany**, following a suicide attempt or suicidal crisis, and followed after discharge. |
| Duration | **Two phases totalling ~7 months.** EMA 1: 21–24 days, starting 1–3 days before discharge, **4 semi-random prompts/day** (08:00–22:00, ≥120 min apart). EMA 2: **26 weeks**, prompts on **two random consecutive days per week**. Total **84–96 prompts in EMA 1** and **208 in EMA 2**. |
| Devices/platforms used | **[MetricWire](../../module-02-digital-phenotyping/profiles/metricwire.md)** — the **"Catalyst"** app, installed on participants' own smartphones at an in-hospital baseline. |
| Funding/COI | German Research Foundation (FO 784/8-1, SP 1556/5-1, GL 818/8-1); Open Access fund of Leipzig University. **No platform relationship stated.** |
| Last verified | 2026-09-01 |

## Summary

The **longest EMA protocol in this module** — roughly seven months, ~300 prompts — in one of the highest-risk populations research reaches: psychiatric inpatients discharged after a suicide attempt or crisis.

The compliance trajectory in the interview subsample is the number to carry: **63.3% in the 3-week post-discharge phase (SD 21.7, range 23–91) falling to 45.4% over the following 26 weeks (SD 28.5, range 0–87)**, with **7 of 16 ceasing to respond before the final days**. A range whose floor is 0% means at least one retained participant contributed nothing in phase 2.

Those figures are, in context, *good*. The authors cite prior post-discharge EMA studies reporting **21%**, **14–16%**, and **17.6%** compliance. A protocol that holds 45% over 26 weeks in this population is at the top of its literature — which tells you how low the ceiling is.

The qualitative findings are what makes it a Module 3 entry rather than a clinical one, and two of them are uncomfortable: **prompts occasionally intensified or triggered suicidal thoughts** (though **no evidence that EMA triggered suicidal *actions***), and **EMA's feasibility during an acute suicidal crisis was questioned by participants themselves** — reduced ability and willingness to respond exactly when the data matters most.

## Instrumentation and Deployment Model

**BYOD, enrolled in hospital.** The Catalyst app was installed on the participant's **own** smartphone during an in-person baseline assessment on the ward — a materially easier onboarding context than remote enrolment, and probably part of why compliance exceeds the comparison literature.

**Protocol mechanics that shape the compliance figures:**

- **Response window: 20 minutes**, with a **push reminder at 10 minutes** if the survey had not been opened. This is far shorter than the 1.5 h ([Kochhar et al.](avicenna-smoking-youth-ema-compliance.md)) or 2–3 h ([Kivelä et al.](avicenna-ema-suicidal-ideation-iatrogenic.md)) windows used elsewhere in this module, and mechanically depresses compliance while raising momentary validity.
- **29–31 Likert items plus 2 context items per survey**, presented in randomised order, with branching on the first suicidal-ideation item.
- **Participants signalled their own discharge date through the app**, which then triggered the start of EMA 1 — a neat participant-driven scheduling mechanism for a study whose window depends on an unpredictable clinical event.

**A safety feature worth copying:** the app carried **permanently accessible national and regional emergency numbers**.

**A data-cleaning rule that changes the compliance denominator:** responses submitted **<30 seconds** from start were coded careless and **set to missing, and excluded from the compliance rate**. One participant contributed 22 such responses in EMA 2. This is stricter than [Achterberg 2026](avicenna-adolescent-esm-school-phone-bans.md), who deliberately *retained* careless responses to avoid removing the most burdened participants — the two studies made opposite defensible choices, and their compliance figures are correspondingly non-comparable.

## Recruitment and Retention

Recruitment was in-person: research staff **attended routine meetings in seven clinics** to identify eligible inpatients, who were then approached individually. This is the highest-touch recruitment model in this module and stands in direct contrast to the online funnels of [Kivelä et al.](avicenna-ema-suicidal-ideation-iatrogenic.md) (39% of sign-ups started) and [Siebers et al.](metricwire-fraudulent-participation.md) (where virtual recruitment admitted fraud).

**The parent cohort's enrolment funnel, total N, and overall retention are not reported in this paper** — it is a qualitative sub-study. All retention and compliance figures below apply to the **16 purposively selected interviewees only**, who were deliberately sampled to span high and low compliance and are therefore *not* representative of the parent cohort in either direction.

## Data Completeness and Technical Issues

**Compliance in the interview sample** (completed assessments ÷ prompts, careless responses excluded):

| Phase | Duration | Prompts | Mean compliance | SD | Range |
|---|---|---|---|---|---|
| EMA 1 | 21–24 days, 4×/day | 84–96 | **63.3%** | 21.7 | 23–91% |
| EMA 2 | 26 weeks, 2 days/week | 208 | **45.4%** | 28.5 | **0–87%** |

**7 of 16 stopped participating during EMA 2**, submitting their last response before day 51 or 52 of that phase.

**Comparison figures the authors cite from the post-discharge EMA literature:** 21% and 14–16% over 3-week and 8-week windows; 17.6% in a 3–6-month outpatient study.

**The non-random-missingness problem, stated as the study's central methodological concern.** The authors set out the argument explicitly: participants at elevated STB risk are more likely to miss prompts and to drop out, so **missingness is confounded with the outcome being predicted**. They cite [Wang et al.](beiwe-inpatient-suicide-pilot.md) — profiled in this module — as evidence that missing responses are themselves predictors of suicide attempts.

Their own qualification is important and is the more careful position: non-response also arises from **losing or switching a phone, study fatigue, or starting a job where smartphones are not allowed** — so it "can indicate a suicidal crisis but might also reflect other disturbances," with correspondingly low predictive specificity. Their operational recommendation is to **reach out to participants** rather than treat non-response as a passive signal.

No app crashes, sync failures or platform faults are reported.

## Feasibility Findings

**Reactivity.** Some participants reported suicidal thoughts **occasionally intensifying or being triggered by survey prompts**. Crucially, **no evidence indicated that EMA triggered suicidal actions.** Read alongside [Kivelä et al.](avicenna-ema-suicidal-ideation-iatrogenic.md) — where no reactivity appeared in the EMA data but 18% reported ideation reactivity retrospectively — the two studies converge: **intensive suicidality monitoring produces subjective reactivity in a minority and no detectable behavioural harm.**

**Burden is not constant.** Burden **increased over time for some participants**, leading the authors to call for **personalised monitoring durations** rather than a fixed protocol length.

**The crisis paradox.** Participants questioned EMA's feasibility **during acute suicidal crises**, citing reduced ability and willingness to respond. This is the most consequential finding in the profile: a method designed to capture crises may systematically fail during them.

**Participant-requested features**, all currently implementable in modern EMA platforms:

- A **progress bar**.
- **Individual feedback on symptom trajectories** — specifically sleep, symptoms, and level of suicidal thoughts.
- **Extended or postponable response windows**, particularly once participants returned to work.
- **Daily (rather than twice-weekly) surveys in EMA 2** — counter-intuitively, more frequent prompting was requested as a *motivation* aid.
- **Adaptive sampling** matched to changing symptoms and life demands, which the authors note would improve compliance but complicates analysis and needs its own pilot work.

**Authors' overall conclusion:** long-term EMA monitoring after psychiatric discharge was perceived as **feasible and beneficial**.

## Relevance to Future Study Design

1. **A 7-month, ~300-prompt protocol in a post-discharge suicidal cohort is achievable at ~45% compliance** — and that is near the top of the published range. Power calculations should use 45%, not 80%.
2. **Response window length is a lever, and 20 minutes is at the aggressive end.** It buys momentary validity at a compliance cost this study cannot separate from population effects.
3. **The participants who matter most are the ones least able to respond.** Missingness is confounded with the outcome, but is not specific enough to use as a signal — reach out instead of inferring.
4. **Plan for burden to grow, and offer an exit that is not dropout.** Participants asked for personalised durations; a scheduled step-down is cheaper than losing them entirely.
5. **Ask participants what features they want and build the cheap ones.** A progress bar and symptom feedback were the top requests, are standard platform capabilities, and cost nothing to enable.
6. **Recruiting in person on the ward and installing on the participant's own phone appears to buy a large compliance advantage** over remote enrolment in this population — though this study cannot isolate that.
7. **Decide and document the careless-response rule.** Excluding <30 s responses (here) and retaining them (Achterberg) both defensible; the resulting compliance figures are not comparable.

## Evidence Confidence

**Verified** — the two-phase protocol structure and prompt counts, the 20-minute window and 10-minute reminder, the 29–31-item survey design, the <30 s careless-response exclusion rule, both phase-level compliance figures with SDs and ranges, the 7-of-16 phase-2 dropout, the emergency-numbers safety feature, the comparison compliance figures cited from the literature, and all qualitative themes. Read from the full text (Europe PMC PMC13003599), 2026-09-01.

**Unclear / not reported** — the parent cohort's total N, enrolment funnel, and overall compliance. **All figures in this profile describe 16 purposively selected interviewees, sampled to span high and low compliance.** They must not be quoted as cohort-level compliance for the parent study. Anyone needing that should retrieve the parent study's preregistration (cited as refs 40–41).

**Stated limitations:** selection bias in the interview sample, and no quantitative validation of the qualitative reactivity findings. The authors are explicit that generalisability is limited.

**Reported** — the reactivity findings are participant self-report gathered retrospectively in interview, not measured in the EMA series.

**COI:** none identified relating to MetricWire. The app is used as an instrument; the paper evaluates a method.

## Key Links

- Paper (OA, CC BY): https://doi.org/10.3389/fpsyt.2026.1744947
- Europe PMC: https://europepmc.org/article/PMC/PMC13003599
- Platform: https://metricwire.com/
- Parent-study preregistration: cited as refs 40–41 in the paper
- Local PDF: `../literature/2026-spangenberg-frontpsychiatry-ema-reactivity-feasibility-suicidal-crises.pdf`

## Related profiles

- Platform: [MetricWire](../../module-02-digital-phenotyping/profiles/metricwire.md)
- Convergent evidence on reactivity and safety: [`avicenna-ema-suicidal-ideation-iatrogenic.md`](avicenna-ema-suicidal-ideation-iatrogenic.md)
- Missingness as signal in a suicidal-ideation cohort (cited by these authors): [`beiwe-inpatient-suicide-pilot.md`](beiwe-inpatient-suicide-pilot.md)
- Opposite careless-response handling: [`avicenna-adolescent-esm-school-phone-bans.md`](avicenna-adolescent-esm-school-phone-bans.md)

## Sources

1. Spangenberg L, Spahn C, Serebriakova J, Forkmann T, Glaesmer H. *Front Psychiatry* 2026;17:1744947. DOI 10.3389/fpsyt.2026.1744947. Full text read from Europe PMC (PMC13003599), 2026-09-01. Establishes every figure in this profile.
