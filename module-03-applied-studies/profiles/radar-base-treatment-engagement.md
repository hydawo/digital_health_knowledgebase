# de Angel et al. 2023 — RMT engagement during active psychological treatment for depression, N=66, 7 months

## Quick Facts

| Field | Details |
|---|---|
| Citation | de Angel V, Adeleye F, Zhang Y, Cummins N, Munir S, Lewis S, Laporta Puyal E, Matcham F, Sun S, Folarin AA, Ranjan Y, Conde P, Rashid Z, Dobson R, Hotopf M. "The Feasibility of Implementing Remote Measurement Technologies in Psychological Treatment for Depression: Mixed Methods Study on Engagement." *JMIR Mental Health* 2023;10:e42866. DOI [10.2196/42866](https://doi.org/10.2196/42866). PMC9906314. |
| Study design | **Mixed methods** longitudinal cohort — quantitative engagement analysis plus qualitative interviews to explain the differences. Distinguishes **attrition** (engagement with the study protocol) from **data availability** (engagement with the devices). |
| Sample size (enrolled / analyzed) | **66** people undergoing psychological therapy for depression. **Overall retention 60%.** |
| Population | Adults in NHS psychological therapy for depression (Lewisham Talking Therapies / South London and Maudsley), UK |
| Duration | **7 months** follow-up |
| Devices/platforms used | **[RADAR-base](../../module-02-digital-phenotyping/profiles/radar-base.md)** smartphone sensing + weekly questionnaires, speech and cognitive tasks; **[Fitbit](../../module-01-wearables/profiles/fitbit-google.md)** wearable |
| Funding/COI | KCL / NIHR Maudsley BRC. Shares authors and infrastructure with the RADAR-CNS programme. |
| Last verified | 2026-08-31 |

## Summary

The only study in this module that measures engagement **while participants are actively receiving
treatment**, and it produces the module's most counter-intuitive finding: **more treatment made
engagement worse, not better.**

**Higher-intensity treatment was associated with attrition (χ²₁=4.6; P=.03)**, as was **higher
baseline anxiety** (t=−2.80; P=.007), with longer treatments trending the same way (U=339.5; P=.05).
**Depression severity itself was not associated with attrition** (P=.86) — consistent with
[RADAR-MDD](radar-mdd-recruitment-retention.md) and [Beukenhorst](beiwe-als-adherence.md), and
another blow to the assumption that sicker participants disengage.

Its second contribution is showing that **two devices moved in opposite directions during
treatment**: participants in treatment **completed more active tasks but wore the Fitbit less** than
those still on the waiting list. The qualitative interviews explain both halves, and the Fitbit
explanation is uncomfortable and important — self-tracking without visible improvement produced
**guilt and internal pressure**, so people took the device off.

## Instrumentation and Deployment Model

RADAR-base collecting:

- **Active:** weekly questionnaires, plus **speech and cognitive tasks**.
- **Passive smartphone:** GPS/location, Bluetooth, accelerometry among others.
- **Passive wearable:** Fitbit.

**Comparison structure:** participants in treatment were compared against participants **in the same
study week who had not yet started treatment** (a waiting-list contrast), rather than against a
separate control group.

**Missing-data threshold used:** a minimum of **8 hours of passive data and at least one active task
completed**. The authors explicitly flag that there is **no standard threshold** for this and note
that Matcham et al. used a different one (a single data point per hour) — which is why cross-study
comparison of "data availability" figures is hazardous. This is one of the few papers in the module
to confront that directly.

## Recruitment and Retention

**Overall retention: 60% over 7 months.**

**Predictors of attrition:**

| Factor | Test | Association |
|---|---|---|
| **Higher-intensity treatment** | χ²₁=4.6 | **P=.03 — associated with attrition** |
| **Higher baseline anxiety** | t₅₆.₂₈=−2.80 | **P=.007 — associated with attrition** |
| Longer treatment | U=339.5 | P=.05 — trend toward significance |
| **Depression severity** | t₅₀.₄=−0.18 | **P=.86 — not associated** |

The anxiety-but-not-depression split is worth dwelling on: two closely correlated clinical
dimensions, only one of which predicts disengagement.

## Data Completeness and Technical Issues

**Data availability trajectories over 7 months — different streams, opposite shapes:**

| Stream | Start | End (7 months) |
|---|---|---|
| **Active** (questionnaires, speech, cognitive) | ~90% | **~30%** — highest initially, **steepest decline** |
| **Wearable (Fitbit)** | max ~80% | **~45%** |
| **Smartphone passive** | ~20–40% | **~20–40% — stable throughout** |

This is a genuinely different pattern from the other profiles here. Active data started highest and
fell hardest; **smartphone passive data started low and simply stayed low**; the wearable sat between
them. Compare [Huang et al.](beiwe-adolescent-feasibility.md), where passive Beiwe data held at ~94%
— the difference is platform and configuration, not participant type, and it is a caution against
treating "passive data is durable" as a universal law.

**Within passive smartphone data, missingness was ordered:** **GPS worst**, then **Bluetooth**, then
**accelerometry** best. That ordering — location worst, accelerometry best — matches
[Raugh et al.](dp-schizophrenia-tolerability.md) exactly, and the explanation there was
computational and radio demand. Two independent studies on different platforms produce the same
ranking.

**Within active data:** **speech and cognitive tasks had lower completion than clinical
questionnaires** — again matching RADAR-MDD's THINC-it finding.

**The treatment-group divergence:**

- Participants **in treatment** completed **more active tasks** than those on the waiting list.
- Participants **in treatment** provided **less Fitbit data** than those on the waiting list.

**Qualitative explanations (from the interviews):**

- *Why active tasks rose during treatment:* participants described a **cohesive experience** — active
  tasks "helped with homework, promoted working on their mental health, and sparked conversations
  with their therapist." The research task became part of the therapy.
- *Why Fitbit wear fell during treatment:* **"increased self-awareness that comes from tracking
  health with the Fitbit can be demotivating if there are no evident improvements in health outcomes
  such as sleep and physical activity,"** which "might increase the likelihood of participants
  removing the device to avoid feelings of guilt and internal pressure."

**Four qualitative themes** were developed. Among the reported subthemes: **a good relationship with
the study team improved the overall experience**; **knowing they were contributing to research was a
strong motivator**, but this was **dampened by tedious, repetitive study procedures**; technical
challenges (battery, measurement accuracy); and task complexity and enjoyability. The
**mental-health/engagement relationship was explicitly bidirectional** — when unwell, some
participants avoided the self-reflection the active tasks required.

## Feasibility Findings

The authors' conclusions, stated as implications rather than a verdict:

- **Different data streams show varied patterns of missing data despite coming from the same
  device** — so feature construction that combines sensors inherits the *worst* stream's
  availability.
- **Longer and more complex treatments, and clinical characteristics such as higher baseline anxiety,
  may reduce long-term RMT engagement.**
- **Different devices may show opposite patterns of missingness during treatment** — the finding with
  the least precedent elsewhere.
- Low data availability means **features derived from passive data may lack accuracy and could lead
  to false interpretations.**

They frame the consequences as bearing on "the scalability and uptake of RMTs in health care
settings, the generalizability and accuracy of the data collected, feature construction, and the
appropriateness of RMT use in the long term."

## Relevance to Future Study Design

1. **Do not assume clinical care improves research engagement.** Higher-intensity treatment predicted
   *attrition*. If recruiting through a treatment service, the most-treated patients are the likeliest
   to leave.
2. **Measure anxiety, not just depression, as an engagement covariate.** Depression severity was
   null; baseline anxiety was significant.
3. **Self-tracking can actively harm engagement when outcomes do not improve.** The guilt/pressure
   mechanism behind reduced Fitbit wear is a design risk for any study that shows participants their
   own health data, and it argues for careful framing of participant-facing feedback.
4. **Conversely, active tasks integrated with therapy get done.** Aligning research tasks with
   treatment homework raised completion — a cheap, transferable design move.
5. **Size the analysis off the least-available stream.** Multi-sensor features inherit the worst
   availability, and here GPS was worst.
6. **State your missing-data threshold explicitly.** The authors' 8-hours-passive-plus-one-active
   threshold differs from RADAR-MDD's one-point-per-hour, and availability figures are not comparable
   across differing definitions. This is a reporting standard the module needs.
7. **Reduce repetitive procedures.** "Contributing to research" was a strong motivator that tedium
   eroded.

## Evidence Confidence

**Verified** for the retention rate, the attrition-predictor statistics, the data-availability
trajectories and stream orderings, and the treatment-versus-waiting-list contrasts — primary
reported results read from the published PDF, with the qualitative themes drawn from the paper's own
reporting.

**Confounding — stated clearly by the authors and important.** This is a **longitudinal cohort, not
a randomised comparison**. Treatment and non-treatment groups "differed in more ways than only the
exposure to treatment": **delayed treatment start was related to treatment intensity, clinical risk,
health-centre catchment area, and symptom severity**. Despite adjustment, they acknowledge
**possible residual confounding**. The treatment-associated findings are therefore **Corroborated,
not causal** — do not read "treatment causes disengagement."

**A limitation the authors raise that applies across this whole module:** engagement is conventionally
operationalised as data availability, which **assumes missing data means deliberate disengagement**.
They point out it "can also be completely missing at random because of software errors," affecting
streams differently for technical reasons, and call for future work **mapping technical issues to
missing data**. Every availability figure in Module 3 carries this ambiguity, and this paper is the
one that names it.

**Small sample (N=66)** for the subgroup comparisons, particularly the treatment-versus-waiting-list
contrasts.

**Relationship to RADAR-MDD:** shares authors, infrastructure and institution with
[Matcham et al.](radar-mdd-recruitment-retention.md) and
[Zhang et al.](radar-mdd-longterm-engagement.md), but is a **separate cohort in a different clinical
context** (active psychological treatment rather than observational follow-up), so it is independent
evidence rather than a re-analysis.

## Key Links

- Paper (OA): https://doi.org/10.2196/42866 · https://mental.jmir.org/2023/1/e42866
- Europe PMC: https://europepmc.org/article/PMC/PMC9906314
- Local PDF: `../literature/2023-deangel-jmirmentalhealth-rmt-engagement-psychological-treatment.pdf`

## Related profiles

- Platform: [RADAR-base](../../module-02-digital-phenotyping/profiles/radar-base.md)
- Device: [Fitbit / Google](../../module-01-wearables/profiles/fitbit-google.md)
- Same platform family, observational cohorts:
  [`radar-mdd-recruitment-retention.md`](radar-mdd-recruitment-retention.md),
  [`radar-mdd-longterm-engagement.md`](radar-mdd-longterm-engagement.md)
- Same GPS-worst / accelerometry-best passive ordering:
  [`dp-schizophrenia-tolerability.md`](dp-schizophrenia-tolerability.md)

## Sources

1. de Angel V, et al. *JMIR Ment Health* 2023;10:e42866. DOI 10.2196/42866. Full text read from the
   published PDF (via Europe PMC, PMC9906314), 2026-08-31. Establishes every figure in this profile.
