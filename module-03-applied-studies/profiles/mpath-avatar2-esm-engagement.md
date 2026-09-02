# Dennard et al. 2025 — ESM engagement inside the AVATAR2 psychosis trial (m-Path), N=134 of 207

## Quick Facts

| Field | Details |
|---|---|
| Citation | Dennard S, Garety P, Edwards C, Gumley A, Owrid O, Miller L, Allan S, Duerden A, Yanga F, Burns C, Fletcher H, Grant A. "Exploration of Factors That Affect Engagement With the Experience Sampling Method and Service Users' Experience of This Within the AVATAR2 Trial: Mixed Methods Study." *JMIR Formative Research* 2025;9:e78204. DOI [10.2196/78204](https://doi.org/10.2196/78204). PMID 41385734 / PMC12700335. |
| Study design | Mixed methods, nested in the **AVATAR2 multicentre UK RCT** (ISRCTN55682735). Quantitative: multiple regression of ESM completion on demographics and clinical severity. Qualitative: reflexive thematic analysis of purposively sampled interviews stratified by completion tercile plus an opt-out group. PPI consultants involved throughout. |
| Sample size (enrolled / analyzed) | **207 trial participants with baseline data → 134 (64.7%) consented to the optional ESM component → 17 interviewed.** |
| Population | UK adults in the AVATAR2 trial for **distressing auditory hallucinations**; diagnoses included schizophrenia (35.9%), bipolar affective disorder (2.4%) and severe depressive episode with psychotic symptoms (9.1%). |
| Duration | ESM: **10 prompts/day for 6 days**, administered at **three trial timepoints** (baseline before randomisation, and follow-ups). |
| Devices/platforms used | **[m-Path](../../module-02-digital-phenotyping/profiles/m-path.md)** smartphone app. Equipment, training and support were provided by the trial. |
| Funding/COI | UK public funding (NIHR-style disclaimer present). **No m-Path developer authorship.** |
| Last verified | 2026-09-01 |

## Summary

The lowest completion figure in this module — **mean ESM completion 39.1% (SD 28.5)** — and the profile exists largely to explain why that number is not comparable to anyone else's.

Two design decisions account for most of it. First, the protocol was **10 prompts per day**, roughly double the density of any other active-assessment study profiled here. Second, and decisively, **completion was defined as the percentage of questionnaires that were 100% complete** — because, as the authors state, saving incomplete questionnaires through the m-Path app "had implications for the reliability of the data export." A partially-answered questionnaire counted as zero.

Set against [McClaine et al.](aware-chemotherapy-engagement.md)'s ≥50%-complete definition (61%) or [Clark et al.](metricwire-sgm-youth-ema-feasibility.md)'s 80%, this is not evidence that psychosis populations engage worse. It is evidence that **a platform's partial-response handling propagates directly into the headline engagement statistic.**

The second finding is a strong null: **age, gender, ethnicity and clinical severity together did not predict ESM completion (F5,128 = 0.548, P=.74).** The authors read this as encouraging — "ESM can be engaging across a diverse user group."

The third is a recruitment fact easy to overlook: **35.3% of trial participants declined the optional ESM component outright.** In any study where phenotyping is an opt-in add-on, that self-selection precedes every engagement number.

## Instrumentation and Deployment Model

**Trial-supported BYOD.** Participants used the m-Path app with **equipment, training and support provided** by the trial team — an above-average support level, which makes the low completion figure more striking.

**Protocol:** 10 questionnaires/day for 6 days, at each of three trial timepoints. Items covered affect, voice-hearing experiences, social interactions and activity — ESM was a **secondary outcome measure** for AVATAR2, not the trial's primary instrument.

**The completion definition, in the authors' words:** "the percentage of questionnaires that were 100% complete, and this decision was made as saving incomplete questionnaires through the M-Path app had implications for the reliability of the data export." This is a platform-behaviour constraint driving a methodological choice driving a published statistic — exactly the chain this module exists to make visible. Compare [Kivelä et al.](avicenna-ema-suicidal-ideation-iatrogenic.md), where the Ethica/Avicenna app also did not save partial responses, with the same consequence.

## Recruitment and Retention

| Stage | n | % |
|---|---|---|
| AVATAR2 participants with baseline data | 207 | — |
| **Consented to the optional ESM component** | **134** | **64.7%** |
| Contacted for qualitative interview | 59 | — |
| Completed a qualitative interview | 17 | 28.8% of those contacted |

Interviewees were purposively sampled across **three completion terciles — low (≤18%), medium (19–54%), high (≥55%)** — plus a fourth **ESM opt-out** group. Sampling the people who refused the method is unusual and is the source of this paper's most useful qualitative material.

Note what the tercile boundaries imply: the "high" group starts at **55%** completion. In most other studies in this module, 55% would be the low tail.

## Data Completeness and Technical Issues

**Mean ESM completion: 39.1% (SD 28.5)** across the 134 consenting participants. Definition: **percentage of 100%-complete questionnaires.**

**Multiple regression of completion on age, gender, ethnicity and clinical severity (PSYRATS): F5,128 = 0.548, P = .74 — not significant.** No individual predictor reached significance.

**Barriers to completion identified qualitatively:**

- **Engaging in other routine tasks and activities.** Several participants deliberately completed prompts at a convenient time instead of on cue — better for them, worse for both completion and momentary validity. *"you can't do it as and when the notifications spring up because you have a life to live."*
- **Notifications not received or not heard**, often because phone sound was off. *"I didn't get the beeps."* The authors suggest high-completion participants may simply have been checking their phones more, or been more familiar with their own notification settings — i.e. **completion partly measures notification literacy, not motivation.**
- **Experiencing positive psychotic symptoms** at the time of a prompt.
- **Limited experience using technology.**
- **Prompt frequency and repetitiveness**, particularly over the assessment period. Several participants said the 6-day limit was what made it tolerable and that the same density **would not be sustainable long term** — a view held most strongly by *high*-completion participants.
- **Trial involvement itself** competing for attention.
- **Concerns about security and privacy**, which influenced the decision to opt out at all.

No app crashes or technical faults are reported beyond the partial-save limitation.

## Feasibility Findings

**Authors' conclusion:** ESM completion was not associated with demographic or clinical-severity factors, which suggests ESM can engage a diverse user group; but engagement can be improved with **increased support or training** for digital assessment, and with **clear information about how digital data are used and recorded** to address privacy concerns.

Reported benefits — ESM functioning as more than measurement: **increased knowledge and awareness of one's own mental health**, including the relationship between mood and voice-hearing and their triggers. The authors note this makes ESM potentially therapeutic as well as observational, and connect it to empowerment and help-seeking. The same benefit appears in [Bonnier et al.](mpath-nssi-ema-benefits-challenges.md) and [Kochhar et al.](avicenna-smoking-youth-ema-compliance.md) — three m-Path/Avicenna studies independently reporting self-insight as a participant-perceived benefit.

Participant suggestions: more support during ESM use (researcher-initiated contact is cited from prior work as raising completion), and reconsidering the number of daily questionnaires.

## Relevance to Future Study Design

1. **Check how the platform handles partial responses before you define completion.** m-Path's export reliability with partial saves forced an all-or-nothing definition here, roughly halving the reportable figure. This is the single most transferable lesson in the profile.
2. **10 prompts/day is at the top of the feasible range even for 6 days**, and participants who *achieved* high completion were the ones saying it could not be sustained longer.
3. **An opt-in phenotyping component inside a larger trial loses about a third of the cohort before it starts** (64.7% opted in here) — and those who opt out cite privacy. Budget the sample accordingly, and interview the refusers.
4. **Notification literacy is a modifiable determinant.** Checking notification settings during onboarding is nearly free and may explain part of the tercile spread.
5. **Demographics and symptom severity did not predict completion**, adding a fourth psychosis/high-risk cohort to this module's null on that question.
6. **Report ESM engagement stratified**, not just as a mean. The tercile structure (≤18% / 19–54% / ≥55%) is far more informative than "39.1%."

## Evidence Confidence

**Verified** — the 207/134/59/17 funnel and the 64.7% opt-in rate, the 10-prompts-per-day × 6-days × 3-timepoints protocol, the mean completion of 39.1% (SD 28.5) and its explicit definition, the regression result (F5,128 = 0.548, P=.74), the tercile boundaries, the diagnostic composition, and all qualitative themes and quotations. Read from the full text (Europe PMC PMC12700335), 2026-09-01.

**Reported** — the authors' interpretations of *why* completion varied (notification-checking behaviour, familiarity with settings). These are inferences from interview material, offered as such.

**Unclear** — whether the three ESM timepoints had differing completion rates, and whether completion decayed within the 6-day window; neither is reported. Also unclear: how many of the 73 who declined ESM cited privacy specifically, since only the interviewed opt-out participants are characterised.

**Selection caution:** the 17 interviewees were purposively rather than randomly sampled, and only 17 of 59 contacted agreed — qualitative themes should not be treated as prevalence estimates.

**COI:** none identified relating to m-Path. The paper evaluates a method inside a trial and reports a platform limitation (partial-save export reliability) against interest.

## Key Links

- Paper (OA, CC BY): https://doi.org/10.2196/78204
- Europe PMC: https://europepmc.org/article/PMC/PMC12700335
- AVATAR2 trial: ISRCTN55682735
- Platform: https://m-path.io/
- Local PDF: `../literature/2025-dennard-jmirformres-avatar2-esm-engagement.pdf`

## Related profiles

- Platform: [m-Path](../../module-02-digital-phenotyping/profiles/m-path.md)
- Same platform, clinical population, self-insight benefit: [`mpath-nssi-ema-benefits-challenges.md`](mpath-nssi-ema-benefits-challenges.md)
- Underlying sensing framework and its OS limits: [`carp-mpath-sense-performance-study.md`](carp-mpath-sense-performance-study.md)
- Same no-partial-save platform behaviour: [`avicenna-ema-suicidal-ideation-iatrogenic.md`](avicenna-ema-suicidal-ideation-iatrogenic.md)
- Contrasting lenient completion definition: [`aware-chemotherapy-engagement.md`](aware-chemotherapy-engagement.md)
- Other psychosis-population deployments: [`mindlamp-relapse-3site.md`](mindlamp-relapse-3site.md), [`dp-schizophrenia-tolerability.md`](dp-schizophrenia-tolerability.md), [`sleepsight-schizophrenia-rest-activity.md`](sleepsight-schizophrenia-rest-activity.md)

## Sources

1. Dennard S, et al. *JMIR Form Res* 2025;9:e78204. DOI 10.2196/78204. Full text read from Europe PMC (PMC12700335), 2026-09-01. Establishes every figure in this profile.
