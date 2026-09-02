# Bonnier et al. 2025 — Benefits and challenges of 28-day EMA in treatment-seeking self-injury patients (m-Path), N=124

## Quick Facts

| Field | Details |
|---|---|
| Citation | Bonnier RA, Beames JR, Claes L, Kirtley OJ, de Thurah L, Weermeijer JDM, Uyttebroek L, Luijsmans M, **Myin-Germeys I**, Kiekens G. "Clinical benefits and challenges of ecological momentary assessment in individuals who self-injure and seek mental health treatment." *International Journal of Clinical and Health Psychology* 2025;25(3):100618. DOI [10.1016/j.ijchp.2025.100618](https://doi.org/10.1016/j.ijchp.2025.100618). PMID 41050767 / PMC12492036. |
| Study design | Prospective cohort with a post-protocol feedback survey; correlational and within-person (same- and next-assessment) analyses of discomfort, beep disturbance, compliance and self-insight. |
| Sample size (enrolled / analyzed) | **132 enrolled and completed baseline → 1 withdrew after baseline → 7 did not complete the EMA protocol → 124 completed → 98 (79.03%) completed the feedback survey**, forming the analytic sample for the experience measures. |
| Population | Adolescents and adults (**16–39**) with **past-month non-suicidal self-injury (NSSI) urges and/or behaviours**, receiving **inpatient or outpatient mental health treatment in Flanders, Belgium**. Recruited by referral from **21 mental health services** (9 inpatient, 8 outpatient, 4 hybrid). |
| Duration | **28 days**, **6 assessments/day**. |
| Devices/platforms used | **[m-Path](../../module-02-digital-phenotyping/profiles/m-path.md)** app (cited to Mestdagh et al. 2023), on participants' own phones. |
| Funding/COI | Academic — KU Leuven; ethics via UZ/KU Leuven. **Inez Myin-Germeys (KU Leuven), whose group is closely associated with the m-Path ecosystem, is a co-author**; no explicit developer-authorship disclosure appears in the extracted text. |
| Last verified | 2026-09-01 |

## Summary

The most complete accounting in this module of **what a month of intensive self-monitoring does to the people doing it** — measured, quantified, and reported in both directions.

Compliance was **74.87% (SD 18.78)** over 28 days at six prompts/day, declining linearly. That is a solid, unsurprising number. The value is everything around it:

- **78.57% reported at least one benefit.** Specifically **64.58% reported increased NSSI-specific self-insight** and **41.67% improved self-efficacy to resist NSSI** — against much lower rates for the *general* versions of the same constructs (32.65% and 9.28%). **The benefit is domain-specific: EMA taught people about the thing it asked about, not about themselves in general.**
- **7.29% experienced EMA in treatment as tiring, stressful, at times overwhelming, and not enjoyable.**
- And the mechanism linking the two: **higher emotional discomfort correlated with lower compliance (r = −0.29, P=.004), higher beep disturbance (r = .37, P<.001), and lower general self-insight (r = −0.28, P=.006)**. Within-person, **when participants felt more overwhelmed than usual, they reported higher beep disturbance in the same and the next assessment.**

That last result is the one a study designer should act on. **Distress and prompt-burden co-move within a person, at the timescale of a single prompt.** The participants who are hardest to reach are hardest to reach precisely when they are struggling — the same phenomenon [Spangenberg et al.](metricwire-post-discharge-ema-reactivity.md) surface qualitatively as the "crisis paradox", here demonstrated quantitatively.

## Instrumentation and Deployment Model

**BYOD**, with recruitment mediated entirely through clinical services rather than direct-to-participant advertising: eligible patients were informed by mental health professionals and through **informational sessions held at the services**. This referral model spanned a diverse service mix — 11 services primarily addressing emotion dysregulation and mood conditions, 5 targeting the adolescent-to-emerging-adulthood transition, 3 specialising in eating disorders, and 2 private practices.

**Protocol:** 28 days, six daily assessments of emotions, cognitions and behaviours including self-injury.

**Two design features worth carrying:**

- **A feedback report was produced for the participant *and their treating clinician***, summarising patterns in emotions, cognitions and harmful behaviours. This is one of only two studies in this module (with [Kivelä et al.](avicenna-ema-suicidal-ideation-iatrogenic.md)) where participants got their own data back — and the only one where the clinician did too. It positions EMA as a clinical adjunct rather than pure measurement, and correspondingly complicates the interpretation of any self-reported benefit.
- **Compliance-contingent financial compensation ranging from €20 to €100** — a five-fold spread tied to response rate, the steepest compliance-linked incentive gradient in this module.

**Minors were included** (16+), with additional parental/caregiver consent under 18.

## Recruitment and Retention

| Stage | n |
|---|---|
| Enrolled and completed baseline | 132 |
| Withdrew after baseline | 1 |
| Did not complete the 28-day EMA protocol | 7 |
| **Completed the EMA protocol** | **124 (93.9%)** |
| Completed the post-protocol feedback survey | **98 (79.03% of 124)** |

**93.9% protocol completion over 28 days at 6 prompts/day, in a self-injuring clinical population, is at the top of this module's range.** The compliance-contingent incentive and clinician-mediated recruitment are the obvious candidate explanations; neither is isolated.

Note the second attrition step: **26 of 124 completers (21%) did not fill in the feedback survey.** Every experience statistic below is computed on the 98 who did — plausibly the more engaged and less burdened, which biases the benefit/harm ratio favourably.

## Data Completeness and Technical Issues

**Average EMA compliance: 74.87% (SD 18.78), decreasing linearly across the 28 days** — the same monotone decay [Clark et al.](metricwire-sgm-youth-ema-feasibility.md) quantify at −4.35 points/week over an identical 28-day window.

**Correlates of the experience of EMA** (in the 98 who completed the feedback survey):

| Association | r | P |
|---|---|---|
| Emotional discomfort ↔ compliance | **−0.29** | .004 |
| Emotional discomfort ↔ beep disturbance | **+0.37** | <.001 |
| Emotional discomfort ↔ general self-insight | **−0.28** | .006 |

**Within-person, prompt-level:** feeling more overwhelmed by emotions than usual predicted **higher beep disturbance in the same assessment and the next one.**

No app crashes, technical failures or platform faults are reported. Unlike [Niemeijer et al.](carp-mpath-sense-performance-study.md), this deployment was **active-only** — no mobile sensing — so the OS background-execution failure modes that dominate m-Path Sense's performance profile do not arise.

## Feasibility Findings

**Benefits reported after the 28 days:**

| Reported benefit | Share |
|---|---|
| At least one benefit | **78.57%** |
| Increased **NSSI-specific** self-insight | **64.58%** |
| Improved self-efficacy **to resist NSSI** | **41.67%** |
| Increased **general** self-insight | 32.65% |
| Increased **general** self-efficacy | 9.28% |

**Harms / burden:** **7.29%** experienced EMA in treatment as tiring, stressful, at times overwhelming, and not enjoyable.

**Authors' conclusion:** although EMA in treatment may evoke emotional discomfort, it may help promote **NSSI-specific self-insight and self-efficacy outside the therapy room**.

This is the third m-Path/Avicenna study in this module to report participant-perceived self-insight as a benefit ([Dennard et al.](mpath-avatar2-esm-engagement.md), [Kochhar et al.](avicenna-smoking-youth-ema-compliance.md)), and the first to quantify the general/specific split.

## Relevance to Future Study Design

1. **Prompt burden and distress co-vary within the person, prompt to prompt.** Any protocol whose scientific target is distress is systematically under-sampling its target at its peaks. This argues for adaptive sampling, a shorter survey during high-distress states, or explicit modelling of non-random missingness — not for more prompts.
2. **Expect the benefit to be domain-specific.** Asking about NSSI produced NSSI insight (64.58%) far more than general insight (32.65%). Do not promise participants generalised self-understanding.
3. **A compliance-contingent €20–€100 gradient coincided with 93.9% protocol completion and 74.87% compliance** in a demanding clinical cohort. This is the module's clearest example of a steep incentive gradient alongside high retention — but it is confounded with clinician-mediated recruitment and with participants receiving a feedback report, so it does not isolate the incentive's effect.
4. **Returning data to the participant *and their clinician* changes what EMA is.** It plausibly drives the self-insight findings and turns the study into a partial intervention. Say so in the protocol.
5. **Report the feedback-survey response rate.** 79.03% here — meaning a fifth of completers' experiences are unmeasured, and probably the less positive fifth.
6. **~7% will find intensive EMA genuinely aversive.** That is a small, real, quantified number to put in an ethics application, alongside [Kivelä et al.](avicenna-ema-suicidal-ideation-iatrogenic.md)'s 22% reporting retrospective mood worsening — the two are not measuring the same thing and the gap between them is itself informative.

## Evidence Confidence

**Verified** — the full cohort flow (132/1/7/124/98), the 28-day 6×/day protocol, compliance of 74.87% (SD 18.78) and its linear decline, every benefit and harm percentage, all three correlations with their P values, the within-person overwhelm→beep-disturbance finding, the €20–€100 compliance-contingent compensation, the 21-service referral recruitment structure, and the participant-and-clinician feedback report. Read from the full text (Europe PMC PMC12492036), 2026-09-01.

**Reported** — the causal framing that EMA "may help promote" self-insight and self-efficacy. These are post-hoc self-reports with no control condition and no pre-post measure of the constructs; the authors' hedging is appropriate and should be preserved.

**Unclear** — how much of the reported benefit is attributable to the feedback report rather than to the EMA itself, since both were delivered; and the experiences of the 26 completers who did not fill in the feedback survey.

**Selection caution:** the analytic sample for all experience measures is the 98 who completed the feedback survey, not the 124 who completed the protocol. Benefit rates are therefore upper bounds.

**Related cohort:** the paper points to Kiekens et al. (2024) for diagnostic characteristics of the same cohort — treat any figures from that paper as describing this deployment, not a separate one.

**COI:** Inez Myin-Germeys (KU Leuven) is a co-author. KU Leuven is m-Path's home institution, and the paper cites the m-Path platform paper (Mestdagh et al. 2023) as its instrument reference. **No competing-interests statement addressing this appears in the extracted text.** The paper does not evaluate m-Path as a product and its burden findings run against a promotional reading, but the institutional proximity should be noted.

## Key Links

- Paper (OA, CC BY): https://doi.org/10.1016/j.ijchp.2025.100618
- Europe PMC: https://europepmc.org/article/PMC/PMC12492036
- Platform: https://m-path.io/
- Local PDF: `../literature/2025-bonnier-ijchp-ema-self-injury-benefits-challenges.pdf`

## Related profiles

- Platform: [m-Path](../../module-02-digital-phenotyping/profiles/m-path.md)
- Same platform, opposite completion picture and a platform-definition artefact: [`mpath-avatar2-esm-engagement.md`](mpath-avatar2-esm-engagement.md)
- The sensing extension of the same platform: [`carp-mpath-sense-performance-study.md`](carp-mpath-sense-performance-study.md)
- The "crisis paradox" qualitatively: [`metricwire-post-discharge-ema-reactivity.md`](metricwire-post-discharge-ema-reactivity.md)
- Iatrogenic-effect rates for comparison: [`avicenna-ema-suicidal-ideation-iatrogenic.md`](avicenna-ema-suicidal-ideation-iatrogenic.md)
- Linear compliance decay over an identical 28-day window: [`metricwire-sgm-youth-ema-feasibility.md`](metricwire-sgm-youth-ema-feasibility.md)

## Sources

1. Bonnier RA, et al. *Int J Clin Health Psychol* 2025;25(3):100618. DOI 10.1016/j.ijchp.2025.100618. Full text read from Europe PMC (PMC12492036), 2026-09-01. Establishes every figure in this profile.
2. Kiekens G, et al. 2024 — cited by the authors for diagnostic characteristics of the same cohort. Not retrieved this pass; **Reported**.
