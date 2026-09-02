# Kochhar et al. 2025 — EMA protocol psychometrics and participant experience in smoking youth (Avicenna), N=84

## Quick Facts

| Field | Details |
|---|---|
| Citation | Kochhar S, Scholten H, Maciejewski DF, Pingel MA, Luijten M. "A mixed-methods investigation of an ecological momentary assessment protocol for cigarette-smoking youth: Psychometric properties and participant experiences." *Drug and Alcohol Dependence Reports* 2025;14:100314. DOI [10.1016/j.dadr.2024.100314](https://doi.org/10.1016/j.dadr.2024.100314). PMID 39867465 / PMC11759552. |
| Study design | Mixed-methods protocol-validation study, run as preparatory work for a mobile cessation intervention. Quantitative psychometrics (ICCs, convergent validity, test–retest reliability, multilevel internal consistency) plus coded qualitative responses about the EMA experience (inter-rater ICC = 0.95). |
| Sample size (enrolled / analyzed) | **84** (target 80, set by feasibility not power). Mean age **17.7 (SD 1.5)**; 58% female. |
| Population | Dutch youth aged **16–20** smoking cigarettes at least weekly and at least slightly motivated to quit. Convenience sampling via social-media advertising and educational institutions. Mean **54 cigarettes/week** (SD 41.70, range 3–200). |
| Duration | **7 days**, **5 EMA prompts/day** (max 35 per person), at random moments inside fixed 30-minute windows (09:00–09:30, 12:00–12:30, 15:00–15:30, 18:00–18:30, 21:00–21:30). |
| Devices/platforms used | **[Avicenna Research](../../module-02-digital-phenotyping/profiles/avicenna-research-ethica.md)** app on participants' own phones. |
| Funding/COI | Academic — Radboud University, Erasmus MC, Tilburg University; ethics via University of Twente. **No platform-developer relationship.** |
| Last verified | 2026-09-01 |

## Summary

A small, short, unglamorous study that earns its place for one reason: it is **the only entry in this module that asked participants directly what they disliked about the protocol, coded the answers, and reported the counts** — and the top complaints are about **platform mechanics**, not about content or about being monitored.

Compliance was **76.89% (SD 5.81)** — participants completed on average **27 of 35** EMAs. That is unremarkable. What is useful is the itemised feedback:

- **28.8% objected to the assessments expiring after 1.5 hours.**
- **27.5% found the number of questions too high** (the protocol had up to 11 items).
- **21.3% disliked answering the same questions every time.**
- Against which: **76.3% found all questions clear**, **72.5% found them easy to answer**, **46.3% said they gained insight into their own smoking or feelings**, and **15% believed they smoked less during the study**.

The expiry-window complaint is the transferable one. A 1.5-hour response window is a configurable platform setting, chosen by researchers, and here it was the single most-cited source of participant dissatisfaction.

## Instrumentation and Deployment Model

**Pure BYOD.** Eligible participants received a pre-EMA questionnaire (demographics, nicotine dependence, smoking urge, withdrawal) and instructions to download the **Avicenna** app.

**Prompt configuration.** Five prompts/day at a random moment within each fixed half-hour window. **Each survey was available for 1.5 hours from trigger, with a reminder 15 minutes before expiry.**

**Compliance-enhancing practices the authors used and name explicitly:**

- **Cumulative reimbursement tied to responses** — €0.50 per EMA plus €2.50 for the two questionnaires, up to **€20** or equivalent study credit.
- **Real-time monitoring of responses**, with the team contacting participants about the previous day's missed prompts.
- **A reminder 15 minutes before expiry.**
- **Framing the study around participants' own interest**: it was named "When do you smoke?" in Dutch and advertised as a chance to contribute to science. The authors report many participants cited scientific contribution as a motivator — echoing [Achterberg 2026](avicenna-adolescent-esm-school-phone-bans.md)'s finding in a Dutch adolescent sample.

## Recruitment and Retention

Recruitment was convenience-based (social media + educational institutions) with a feasibility-set target of 80. No enrolment funnel, screening-failure count, or withdrawal count is reported — a real gap, and the reason this profile carries no retention figure.

## Data Completeness and Technical Issues

**Compliance: 76.89% (SD 5.81), mean 27 of 35 EMAs, range 6–35.**

Note the range: at least one participant completed 6 of 35 (17%) while remaining in the analytic sample. As elsewhere in this module, the mean conceals a long tail.

**No demographic or behavioural predictor of compliance was found** — age, gender, weekly smoking and education level were all non-significant. This reproduces the null seen in [Dennard et al.](mpath-avatar2-esm-engagement.md) (no demographic or severity predictors of ESM completion) and, for symptom severity specifically, in [Kivelä et al.](avicenna-ema-suicidal-ideation-iatrogenic.md)

The paper reports **sample-level missingness per assessment moment and per study day** (its Figure 2) and states there was no effect of assessment time or day — unusual in this module, where morning prompts and later study days are the usual casualties. The very short 7-day window is the likely reason there is no decay to observe.

**No app crashes, sync failures or data-loss events are reported.** The protocol was active-only; no passive sensing was collected, so the whole class of background-collection failure modes documented elsewhere in this module does not apply.

## Feasibility Findings

**Quantitative:** all EMA items showed substantial within-person variance (multilevel ICCs), good convergent validity and good test–retest reliability. The authors' conclusion is that the protocol is psychometrically fit for use in a subsequent intervention trial.

**Participant experience, coded and counted:**

| Feedback | Share |
|---|---|
| Rated timing and frequency positively | M = 4.46 (SD 1.53) on 1–7 |
| Liked the number of questions (≤11 items) | 67.5% (54) |
| Satisfied with the timings | 53.8% (43) |
| **Disliked that assessments expired after 1.5 h** | **28.8%** |
| **Found the questions too many** | **27.5%** |
| **Disliked answering the same questions each time** | **21.3%** |
| Enjoyed monitoring their own behaviour | 20% (16) |
| Found all questions clear | 76.3% |
| Found questions easy to answer | 72.5% |
| Gained insight into own smoking/feelings | 46.3% (37) |
| Perceived no effect | 28.8% (23) |
| Thought they smoked *less* during the study | 15% (12) |
| Would change nothing about the study | 53.8% |

**Reactivity:** 15% believed they smoked less, but **the smoking data showed no change over the week** — the same objective/subjective divergence [Kivelä et al.](avicenna-ema-suicidal-ideation-iatrogenic.md) find for mood and ideation, here running in the benign direction.

Two items caused genuine comprehension problems and are worth flagging to anyone reusing them: **5 participants (6.3%) could not separate "restless" from "busy"**, and **5 (6.3%) found the smoking item's reference window ("last...") unclear**.

## Relevance to Future Study Design

1. **The response-expiry window is a design decision with a measurable acceptability cost.** 28.8% of participants disliked the 1.5-hour expiry — the most-cited complaint in the study. [Kivelä et al.](avicenna-ema-suicidal-ideation-iatrogenic.md) used 2–3 hours on the same platform and still attributed low morning compliance partly to the window. Longer windows trade momentary validity for compliance and satisfaction; the trade should be made deliberately.
2. **Pilot the items, not just the protocol.** Two of eleven items were misread by 6% of participants each. That is invisible in a compliance rate and fatal to a construct.
3. **Cumulative per-response payment plus a 15-minute pre-expiry reminder plus next-day follow-up on missed prompts** produced 77% over a week. The components are cheap and the authors name them as the mechanism.
4. **Framing recruitment around the participants' own curiosity works in this population** — reported independently by two Dutch adolescent studies in this module.
5. **Report the compliance range.** 6/35 sits inside a 77% mean.
6. **Report the recruitment funnel.** This study does not, which is the main thing preventing its numbers from being fully usable.

## Evidence Confidence

**Verified** — N=84, demographics, smoking volume, the 7-day/5-prompt/1.5-hour-window configuration, the €0.50/€2.50/€20 incentive structure, the 76.89% compliance figure with SD and range, the null demographic predictors, every coded participant-feedback percentage, and the two item-comprehension problems. Read from the full text (Europe PMC PMC11759552), 2026-09-01.

**Reported** — the authors' attribution of good compliance to their four compliance-enhancing practices. Named as consistent with prior reviews, not tested.

**Unclear** — the recruitment funnel and any withdrawals. Neither is reported, so "84" cannot be placed against a screened or approached denominator, and no retention rate can be derived.

**Stated limitations:** the sample size was set by feasibility and funding rather than by power; most EMA constructs were measured with single items; and the study was conducted entirely in Dutch in one country.

**Scope note.** This study sits close to Module 3's boundary: it is a **protocol-validation** paper, and its psychometric content (ICCs, convergent validity, test–retest reliability) is not Module 3 material. It is included because roughly half of it is a deployment-experience report with counted participant feedback on platform mechanics — content that exists in almost no other paper in this module.

**COI:** none identified. No author relationship to Avicenna Research is stated or apparent.

## Key Links

- Paper (OA, CC BY): https://doi.org/10.1016/j.dadr.2024.100314
- Europe PMC: https://europepmc.org/article/PMC/PMC11759552
- Platform: https://avicennaresearch.com/
- ESM Item Repository (source of several items): https://www.esmitemrepository.com/
- Local PDF: `../literature/2025-kochhar-dadr-ema-smoking-youth-psychometrics-experiences.pdf`

## Related profiles

- Platform: [Avicenna Research (Ethica)](../../module-02-digital-phenotyping/profiles/avicenna-research-ethica.md)
- Same platform, longer and heavier protocol, response-window discussion: [`avicenna-ema-suicidal-ideation-iatrogenic.md`](avicenna-ema-suicidal-ideation-iatrogenic.md)
- Dutch adolescent ESM, engagement design: [`avicenna-adolescent-esm-school-phone-bans.md`](avicenna-adolescent-esm-school-phone-bans.md)
- Null demographic predictors of completion: [`mpath-avatar2-esm-engagement.md`](mpath-avatar2-esm-engagement.md)

## Sources

1. Kochhar S, Scholten H, Maciejewski DF, Pingel MA, Luijten M. *Drug Alcohol Depend Rep* 2025;14:100314. DOI 10.1016/j.dadr.2024.100314. Full text read from Europe PMC (PMC11759552), 2026-09-01. Establishes every figure in this profile.
