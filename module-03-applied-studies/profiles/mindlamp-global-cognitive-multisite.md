# Castillo et al. 2025 — mindLAMP remote cognitive assessment across India and the US, N=56 over 30 days

## Quick Facts

| Field | Details |
|---|---|
| Citation | Castillo J, Cheong J, Choudhary S, Bondre A, Rozatkar AR, Mehta UM, Shrivastava R, Ahmad MA, Malviya A, Sen Y, Tugnawat D, Bhan A, Modak T, Das N, Nagendra S, Reddy PV, Chatterjee R, Lane E, Naslund JA, **Torous J**. "Mobile cognitive remote assessment of schizophrenia: a global multi-site pilot study." *Schizophrenia* 2025;11:144. DOI [10.1038/s41537-025-00660-8](https://doi.org/10.1038/s41537-025-00660-8). PMID 41309640 / PMC12660878. Published 2025-11-27. |
| Study design | **30-day multi-site observational pilot** comparing app-delivered cognitive assessments against the MATRICS Consensus Cognitive Battery, with exploratory EMA/sleep mediation analysis. Primary aims are psychometric (scoring metrics, criterion correlation, test–retest reliability); the operational content is secondary. |
| Sample size (enrolled / analyzed) | **62 enrolled and downloaded mindLAMP → 6 dropped out → 56 analysed (9.7% attrition).** By site: **Bangalore 21, Bhopal 23, Boston 12.** |
| Population | Adults ≥18 with schizophrenia or schizoaffective disorder, owning a smartphone able to run the app, speaking the local study language (English in Boston; English or Hindi in Bhopal and Bangalore). Excluded: uncontrolled mental illness, or speech/sight/hearing impairment affecting smartphone operation. Mean age 26.9 (SD 5.44, range 19–46); 31 male / 25 female; **45 of 56 Asian**. |
| Duration | 30 days per participant. Recruitment September 2024 – March 2025. |
| Devices/platforms used | **[mindLAMP](../../module-02-digital-phenotyping/profiles/mindlamp.md)**, BYOD. Ten in-app cognitive assessments; daily notifications at 18:00; 1–2 assessments or surveys assigned per day; GPS permissions enabled at intake for passive sensing; sleep inferred from **GPS + screen state**. REDCap for clinical instruments. |
| Funding/COI | Academic collaboration across **Beth Israel Deaconess Medical Center (Boston)**, **NIMHANS (Bangalore)**, **AIIMS Bhopal** and **Sangath**. **Competing interests: "the authors declare no competing interests"** — note that **John Torous is mindLAMP's principal academic developer and is senior author**, and the paper evaluates his platform's own assessment suite. IRB approval at each site. Participants "compensated at the beginning and the end of the study"; amounts not stated. |
| Last verified | 2026-09-02 |

## Summary

**Read this profile for its geography and its retention figure, not for its main results.** The
paper's primary contribution is psychometric — which of five speed–accuracy scoring metrics best
correlates app-based cognitive tasks with the MCCB — and that belongs to Module 2's literature
library rather than here. What Module 3 gains is the module's **second study with sites outside North
America and Western Europe**, and the only one running the *same* protocol concurrently in India and
the United States.

The operational headline: **62 enrolled, 6 dropped out, 9.7% attrition over 30 days in a
schizophrenia-spectrum cohort across three sites in two countries**, with **assessment completion
running roughly twice the protocol minimum** — participants were expected to complete each of the ten
assessments at least four times and completed the most-used task a mean of **8.8 times** (range 1–33).

The finding that most changes how the module should be read is a negative one about **cross-site
comparability**. The three sites' MCCB distributions differed significantly (Speed of Processing
F=6.591, p<0.01; Reasoning and Problem Solving F=9.481, p<0.01; Attention/Vigilance F=3.385, p<0.05;
Overall Composite F=4.978, p<0.05), with the two Indian sites resembling each other more than either
resembled Boston. Compounding this, **the Boston participants were asymptomatic** — every PANSS
subscale score was exactly 7 (the floor) with SD 0 — so **Boston was excluded from the PANSS totals
and from the primary analyses altogether**, which were run on the two Indian sites only.

A multi-site global pilot therefore ended up analysing a single country, because the sites recruited
clinically incomparable samples. **That is a study-operations finding, and a transferable one: "same
protocol, multiple countries" does not deliver a poolable cohort.**

## Instrumentation and Deployment Model

**BYOD mindLAMP**, set up with a research assistant at the intake visit, who also enabled **GPS
permissions** and — notably — **told participants in advance that they would be contacted for
troubleshooting if their data quality proved low.** Framing monitoring as an expected part of
participation, at onboarding, is the "Notify"/"Correct" contract from
[LINC](mindlamp-linc-passive-data-quality.md) stated to the participant up front. No troubleshooting
counts or data-quality figures are reported, so the effect cannot be assessed.

**Assessment schedule:** 1–2 cognitive assessments or surveys per day with a **single daily 18:00
notification**, over 30 days, such that each of the ten tasks should have been completed at least
four times.

**Cultural adaptation of the stimuli themselves, and this is the most reusable detail in the paper:**
the tasks are customisable without coding, and **the Emotion Recognition task used UPenn's ER-40
Color Emotional Stimuli in the US and the AIIMS Facial Toolbox for Emotion Recognition in India.**
mindLAMP is available in 8 languages including Hindi. Cross-cultural deployment required changing the
*content* of a task, not just its language — a distinction most multi-site protocols do not make.

**Inter-rater reliability was established across sites before the study**: research assistants at all
three sites rated five video-recorded clinical interviews, achieving ICC >0.75 for PANSS Total and
Positive and >0.4 for PANSS Negative. Reasonable practice for a multi-site study, and rare enough in
this module to note.

**Passive sensing was collected but barely used.** Sleep duration was inferred from a GPS +
screen-state algorithm and entered only an exploratory mediation analysis on the Indian sites. **No
passive data completeness, coverage or missingness figures appear anywhere in the paper** — a
striking omission given the same group's [LINC paper](mindlamp-linc-passive-data-quality.md) makes
exactly that measurement its subject.

## Recruitment and Retention

**62 enrolled and downloaded mindLAMP; 6 dropped out and were excluded from all analyses; 56
analysed.** No reasons for dropout are given. No pre-consent funnel (approached, screened, ineligible)
is reported for any site. Site allocation was by recruitment location, not randomised.

**9.7% attrition over 30 days in a schizophrenia-spectrum cohort** compares favourably with the
module's psychosis deployments — [Cohen 2023](mindlamp-relapse-3site.md) and
[Raugh 2021](dp-schizophrenia-tolerability.md) — though at a much shorter duration than either.

**One Boston participant did not complete the demographic survey.**

## Data Completeness and Technical Issues

**No data-quality metric is reported.** No coverage ratio, no missingness, no wear or app-uptime
figures, no technical failure modes, no troubleshooting counts — despite the intake script promising
troubleshooting contact for low data quality. This is the profile's principal limitation as a Module 3
entry.

What is reported is **assessment completion counts over 30 days**, against a protocol minimum of four
per task:

| Assessment | Mean completions | SD | Range |
|---|---|---|---|
| Cats and Dogs | 8.8 | 8.7 | 1–33 |
| Spatial Span | 8.7 | 8.0 | 1–31 |
| Balloon Risk | 7.4 | 7.9 | 1–31 |
| Symbol Digit Substitution | 7.0 | 7.8 | 1–31 |
| Spin the Wheel | 6.6 | 7.1 | 1–31 |
| Jewels A | 6.5 | 6.8 | 1–31 |
| Emotion Recognition | 6.4 | 6.4 | 1–31 |
| Jewels B | 5.5 | 6.2 | 1–31 |
| Maze | 4.1 | 3.1 | 1–13 |

Every mean exceeds the four-completion minimum, but **the standard deviations are as large as the
means and every range starts at 1** — so the cohort mean is carried by a minority of very high
completers, and some participants completed a task once in 30 days. **A mean completion count is a
poor engagement statistic and this table shows exactly why.** No participant-level engagement
distribution is provided.

**Task-order effects on reliability:** only **Balloon Risk (ICC 0.664), Jewels A (0.568) and Symbol
Digit Substitution (0.536)** reached moderate test–retest reliability; the remaining six did not. The
authors attribute this partly to environmental noise inherent to unsupervised remote administration —
"distractions and fatigue" — and to sensitivity to "mood, motivation, or even phone performance."
**Phone performance affecting a timed cognitive score is an operational hazard specific to BYOD
cognitive testing** and is not something a supervised battery has to contend with. For comparison the
authors cite a neuroUX study (393 adults, five completions over ten days) with ICCs of 0.438–0.912,
and Keefe's in-person MCCB composite ICC of 0.88.

## Feasibility Findings

The authors' feasibility claim is implicit rather than stated as an endpoint: a 30-day
remote cognitive-assessment protocol ran to completion across three sites in two countries in a
schizophrenia-spectrum population with ~10% attrition, and produced task-level scores correlating with
a gold-standard in-person battery on the Indian sites.

**Their own limitations are the operationally important part:** the total sample of 56 is small; each
remote assessment was completed roughly **once weekly**, which "may limit the reliability or validity"
of the results; **clinical symptomatology differed between sites**, which drove the decision to
analyse India only; the Boston site's **low symptom severity and lack of psychotic symptoms** is named
as a limitation in itself; and clinical diagnoses were taken from the recruiting service without
re-diagnosis.

## Relevance to Future Study Design

1. **Running the same protocol in multiple countries does not produce a poolable cohort.** Three
   sites, one protocol, established PANSS inter-rater reliability — and the sites still recruited
   clinically incomparable samples, forcing the primary analysis onto two of the three. **Plan for
   site heterogeneity as a primary analytic problem, not a sensitivity check**, and screen on symptom
   severity if between-site comparability matters.
2. **Cross-cultural deployment can require changing task content, not just language.** Swapping the
   emotion-recognition stimulus set between US and Indian norms is the concrete example. Ask, of any
   cognitive or affective task, whether its *stimuli* are culturally portable.
3. **Tell participants at onboarding that you will contact them about data quality.** Cheap, sets
   expectations, and matches the monitoring contract that
   [LINC](mindlamp-linc-passive-data-quality.md) formalises.
4. **Do not report engagement as a mean completion count.** Means of 4.1–8.8 with SDs of 3.1–8.7 and
   ranges starting at 1 describe a cohort in which some people did a task 33 times and others once.
   Report the distribution.
5. **Unsupervised remote cognitive testing loses reliability, and part of the loss is device
   performance.** Six of nine tasks failed to reach acceptable test–retest reliability. If a timed
   digital task is your endpoint, handset heterogeneity is a measurement-error source you must at
   minimum record.
6. **~10% attrition over 30 days is achievable in schizophrenia-spectrum cohorts across India and the
   US.** Useful as a planning anchor, but note the short duration.

## Evidence Confidence

**Verified** — the 62→56 enrolment and dropout counts; the per-site sample sizes; the demographic and
PANSS table including the Boston floor effect (all subscales exactly 7, SD 0) and its exclusion from
the totals; the ANOVA F statistics for cross-site MCCB differences; the assessment completion table
with means, SDs and ranges; all nine ICCs with confidence intervals; the schedule (1–2 assessments
per day, 18:00 notification, minimum four completions per task); the cultural stimulus substitution;
the PANSS inter-rater ICCs; the sleep-inference method; the intake troubleshooting statement. Read
from the full text and published PDF (PMC12660878), 2026-09-02.

**Not assessed here** — the paper's psychometric findings (Rate-Correct Score outperforming
alternative metrics; Jewels A and Symbol Digit Substitution correlating best with MCCB domains; the
sleep-mediation analysis). These are **validity results and belong to Module 2's literature library**,
not to this module, per `CLAUDE.md`'s scope rules.

**Thin as a Module 3 entry, and included on geography.** There is **no data-completeness, coverage,
missingness or technical-failure reporting of any kind**, no dropout reasons, and no pre-consent
funnel. Its operational content is limited to attrition, assessment counts and the site-heterogeneity
finding. It is profiled because the module has **almost no non-Western deployment evidence** and this
is the only entry running a single protocol concurrently in India and the US.

**COI.** The competing-interests statement declares none, but **John Torous is mindLAMP's principal
academic developer and the senior author**, and the paper evaluates his own platform's cognitive
assessment suite against a gold standard. Multiple co-authors are from his group. The finding most
exposed is the identification of Jewels A and Symbol Digit Substitution as the tasks meriting further
study; what tempers it is that **six of nine tasks are reported as failing test–retest reliability**,
which is not a flattering result for the suite.

**Small and homogeneous by site.** 12 participants in Boston, all asymptomatic; 45 of 56 participants
Asian; mean age 26.9. Whether these findings extend to older or more symptomatic cohorts is untested.

## Key Links

- Paper (OA, CC BY): https://doi.org/10.1038/s41537-025-00660-8
- Europe PMC: https://europepmc.org/article/PMC/PMC12660878
- mindLAMP docs: https://docs.lamp.digital/
- Local PDF: `../literature/2025-castillo-schizophrenia-mobile-cognitive-remote-assessment-multisite.pdf`

## Related profiles

- Platform: [mindLAMP](../../module-02-digital-phenotyping/profiles/mindlamp.md)
- Other mindLAMP/LAMP deployments: [`mindlamp-relapse-3site.md`](mindlamp-relapse-3site.md),
  [`lamp-schizophrenia-cognition-unpaid.md`](lamp-schizophrenia-cognition-unpaid.md),
  [`mindlamp-linc-passive-data-quality.md`](mindlamp-linc-passive-data-quality.md)
- Multi-site psychosis deployment including Indian sites: [`mindlamp-relapse-3site.md`](mindlamp-relapse-3site.md)
- Engagement in psychosis cohorts: [`dp-schizophrenia-tolerability.md`](dp-schizophrenia-tolerability.md),
  [`sleepsight-schizophrenia-rest-activity.md`](sleepsight-schizophrenia-rest-activity.md),
  [`connect-multi-wearable-psychosis.md`](connect-multi-wearable-psychosis.md)

## Sources

1. Castillo J, Cheong J, Choudhary S, et al. *Schizophrenia (Heidelb)* 2025;11:144.
   DOI 10.1038/s41537-025-00660-8. Full text and Tables 1–6 read from the published PDF and PMC XML
   (PMC12660878), 2026-09-02. Establishes every figure in this profile.
