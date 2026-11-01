# Yorke et al. 2026 - RADAR-base with Fitbit Inspire, 28-day remote sleep measurement in autistic and nonautistic young people, N=73 (preprint)

## Quick Facts

| Field | Details |
|---|---|
| Citation | Yorke I, Choudhury AR, Boatman C, Oakley B, Law ML, Holt R, Colomar Molla L, Forde NJ, Conde P, Sankesara H, Ranjan Y, Rashid Z, Telesia L, Loth E, Buitelaar J, Murphy D, Folarin A, Dobson R, Cummins N, Simonoff E. "Feasibility and exploration of remote multimodal sleep measurement in autistic and nonautistic smartphone users." *Research Square* preprint, posted 2026-04-19. DOI [10.21203/rs.3.rs-9381221/v1](https://doi.org/10.21203/rs.3.rs-9381221/v1). Not peer reviewed. No PMID or PMCID. |
| Study design | Observational feasibility study within the 28-day Mobile Measures Month (MMM) of the AIMS-2-TRIALS programme. Feasibility is the first of three aims. |
| Sample size (enrolled / analyzed) | 34 autistic and 40 nonautistic enrolled. 1 nonautistic withdrew over concerns about the passive app. 73 in the feasibility analysis. 10 autistic and 5 nonautistic contributed no analysable sleep days. |
| Population | Autistic and nonautistic participants aged 14 to 35 from the UK sites (KCL, Cambridge) of the LEAP-3 cohort, plus a nonautistic KCL volunteer sample. 76.5% of autistic and 38.5% of nonautistic participants male. Most in full-time work or education. |
| Duration | 28 days per participant. Recruitment March 2022 to November 2024. |
| Devices/platforms used | [Fitbit](../../module-01-wearables/profiles/fitbit-google.md) Inspire 2 (LEAP participants) or Inspire 3 (KCL volunteers), mailed out. [RADAR-base](../../module-02-digital-phenotyping/profiles/radar-base.md) passive app (pRMT, Android only) and active app (aRMT) for a daily sleep-quality slider on participants' own phones. |
| Funding/COI | IMI2 grant 777394 (AIMS-2-TRIALS) with EU Horizon 2020, EFPIA, Autism Speaks, Autistica and SFARI. RADAR-base funded by IMI2 grant 115902. NIHR Maudsley BRC and Wellcome. One author holds Google shares and notes Google acquired Fitbit. Two authors direct Onsentia Ltd, one also CogStack Ltd. Participant compensation is not reported. |
| Last verified | 2026-10-31 |

## Summary

This is the module's only autism deployment. It is included because the headline adherence figures and the usable-data figures diverge sharply, and the paper traces part of the gap to a measured participant trait.

Median adherence looked good in both groups. Fitbit wear was 82.5% of the time for autistic and 78.9% for nonautistic participants. Daily sleep ratings were available on 92.9% and 85.7% of days. Passive phone data were available on 78.6% and 85.7% of days. None of the group differences was significant.

Usable data were much lower. A usable day needed both a valid Fitbit primary sleep period and a sleep rating. 47% of possible autistic participant-days (447 of 952) were usable, against 59.1% (645 of 1092) for nonautistic participants. Ten autistic participants (29.4%) had no usable days at all.

Tactile sensitivity explains part of the loss. Among autistic participants, greater tactile sensitivity was associated with lower availability of a Fitbit sleep period (ρ = .44, p=.03, where higher scores mean lower sensitivity). It was also associated with fewer usable days overall (ρ = .42, p=.04).

## Instrumentation and Deployment Model

Hybrid. The Fitbit was mailed to each consenting participant. The phone was the participant's own. Setup ran over an enrolment video call with a researcher. The Fitbit models were chosen with autistic community representatives, partly for long battery life.

Eligibility originally required Android because the RADAR-base passive app only ran on Android. The rule was later relaxed to bring in more LEAP participants. iOS users took part in the Fitbit and active-app streams but contributed no passive phone data. 91.2% of autistic and 87.2% of nonautistic participants used Android. Eight iOS users were excluded from passive-data analyses.

The aRMT app prompted a sleep-quality rating on a 0 to 100 slider at 8:30am daily. The pRMT app supplied phone motion, app usage, screen state, light level and battery level. Battery records were the presence marker for whether the passive app was installed and running.

Fitbit wear was built from heart rate data. Gaps over 120 seconds and runs of near-constant heart rate (rolling variance under 1 over 20 samples) counted as non-wear. Night wear was 21:00 to 09:00.

## Recruitment and Retention

LEAP-3 brought 127 autistic and 51 nonautistic participants back to the UK sites. The KCL volunteer sample was 26. How many of these were approached for the MMM, and how many declined, is not reported in the text.

| Stage | Autistic | Nonautistic |
|---|---|---|
| Enrolled | 34 | 40 |
| Withdrew (concerns about the pRMT app) | 0 | 1 |
| In feasibility analysis | 34 | 39 |
| No usable sleep days | 10 (29.4%) | 5 (12.5% as printed) |

All ten autistic participants with no usable days showed night-time Fitbit wear under 25% and little or no sleep-period detection. Three also had low rating completion. Among the five nonautistic participants, four completed no sleep ratings and three had low night wear.

## Data Completeness and Technical Issues

| Metric, median (IQR) | Autistic | Nonautistic |
|---|---|---|
| Fitbit wear, % of time | 82.5 (52.6) | 78.9 (18.3) |
| Fitbit night wear, % | 75.8 (67.3) | 77.9 (15.0) |
| Days with a Fitbit primary sleep period, % | 75 (95.7) | 85.7 (28.6) |
| Days with a sleep rating, % | 92.9 (35.0) | 85.7 (48.2) |
| Days with passive phone data, % (Android only) | 78.6 (57.1) | 85.7 (35.7) |
| Usable days, % | 41.0 (92.1) | 71.4 (53.6) |

The wide IQRs in the autistic column are the finding. The medians are similar, but the autistic distribution has a long tail of participants with almost nothing.

Other correlates of availability were modest. Older age went with more sleep ratings (ρ = .27, p=.03). Higher IQ went with more Fitbit sleep periods (ρ = .31, p=.03). Higher self-rated autism characteristics went with more passive phone data (ρ = .31, p=.03). Sex was unrelated to any metric.

The only named technical constraint is the operating system. iOS devices were incompatible with the passive sensing app. No sync, battery or app-crash failures are reported. The participant who withdrew cited concerns about the passive app, without further detail.

## Feasibility Findings

The authors conclude that remote multimodal sleep measurement was generally feasible in both groups. They add that a notable minority, over a quarter of autistic participants, provided little or no usable sleep data.

They read the tactile-sensitivity result as sensory discomfort limiting night-time wear. They note sensory sensitivity is also linked to insomnia severity. People with the worst sleep may therefore be the most likely to drop out of wearable-based sleep studies.

They recommend evaluating contactless alternatives such as mattress-based or camera-based monitoring. They flag that the enrolment requirements (independent smartphone use, willingness to wear the Fitbit and share phone data) likely excluded lower-functioning and more sensory-sensitive autistic people.

## Relevance to Future Study Design

Report usable days, not only wear. Here median wear near 80% coexisted with 47% usable autistic participant-days.

Measure tactile sensitivity at baseline in any wearable sleep study with autistic participants. It predicted which participants would contribute nothing.

Budget for an Android-only passive stream if using RADAR-base's passive app as deployed in 2022 to 2024. About one in ten participants here had iPhones and lost that stream.

A 28-day protocol with a single daily slider kept sleep-rating completion near 90% in both groups. The rating was cheap. The wearable was the binding constraint.

## Evidence Confidence

Reported. This is an unrefereed preprint. All figures were read from the Research Square PDF (v1, CC BY 4.0) on 2026-10-31. The enrolment and withdrawal counts, Table 1 feasibility metrics, the usable-day totals, the zero-usable-day counts, the Table 2 correlations, the device and app details, the wear-time algorithm, the OS split and the funding and competing-interest declarations come from that text.

Unclear. The 12.5% figure for nonautistic participants with no usable days is printed against a denominator of 39, where 5 of 39 is 12.8%. Supplementary Tables S1 to S7 were not retrieved.

Not assessed here. Whether Fitbit sleep staging is valid in autistic sleepers is a Module 1 question. The authors did no reference-standard comparison.

## Key Links

- Preprint (OA, CC BY 4.0): https://doi.org/10.21203/rs.3.rs-9381221/v1
- Local PDF: none held

## Related profiles

- Platform: [RADAR-base](../../module-02-digital-phenotyping/profiles/radar-base.md)
- Device: [Fitbit / Google](../../module-01-wearables/profiles/fitbit-google.md)
- Other RADAR-base deployments: [`radar-mdd-recruitment-retention.md`](radar-mdd-recruitment-retention.md), [`radar-ad-feasibility-usability.md`](radar-ad-feasibility-usability.md), [`radar-base-garmin-respiratory-remote-monitoring.md`](radar-base-garmin-respiratory-remote-monitoring.md)
- Fitbit sleep in young people: [`fitbit-ai-sleep-feedback-adolescent-soccer.md`](fitbit-ai-sleep-feedback-adolescent-soccer.md)

## Sources

1. Yorke I, Choudhury AR, Boatman C, et al. *Research Square* preprint rs-9381221 v1, posted 2026-04-19. DOI 10.21203/rs.3.rs-9381221/v1. Full text, Tables 1 to 4 and figure captions read from the Research Square PDF, 2026-10-31. First author taken from the PDF byline. Establishes every figure in this profile.
