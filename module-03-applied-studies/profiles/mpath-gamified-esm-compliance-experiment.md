# Dejonckheere et al. 2024 - Gamified in-app rewards versus standard m-Path ESM, Belgian adults, N=193 over 10 days

## Quick Facts

| Field | Details |
|---|---|
| Citation | Dejonckheere E, Verdonck S, Andries J, Röhrig N, Piot M, Kilani G, Mestdagh M. "Real-time incentivizing survey completion with game-based rewards in experience sampling research may increase data quantity, but reduces data quality." *Computers in Human Behavior* 2024;160:108360. DOI [10.1016/j.chb.2024.108360](https://doi.org/10.1016/j.chb.2024.108360). No PMCID. Preregistered on AsPredicted (#101798). |
| Study design | Preregistered between-person experiment. Random 2:1 allocation to a gamified or standard ESM protocol. Outcomes were compliance, response latency, completion time and response reliability. |
| Sample size (enrolled / analyzed) | 200 enrolled. 193 analysed (128 gamified, 65 control). |
| Population | Dutch-speaking adults in Belgium. 81.3% female. Mean age 22.67. 108 students paid in course credit and 85 community volunteers paid 15 EUR. |
| Duration | 10 days. Data collected July to October 2022. |
| Devices/platforms used | [m-Path](../../module-02-digital-phenotyping/profiles/m-path.md) on the participant's own smartphone. The gamified arm used an in-app coin store built with m-Path's own building blocks. Active only. |
| Funding/COI | KU Leuven Research Fund C14/19/054. Two authors hold FWO fellowships. Three authors (Dejonckheere, Verdonck, Mestdagh) co-founded m-Path, the commercial software used. Two more (Piot, Kilani) are m-Path employees. |
| Last verified | 2026-10-31 |

## Summary

This is an experiment run by the platform's developers on their own platform. It tests whether instant in-app rewards raise ESM compliance.

Compliance was low for a ten-a-day protocol. The whole-sample mean was 58.31% (SD 21.13%, range 1% to 96%). The authors attribute this to low pay, pay that did not depend on compliance, and no compliance cut-off.

Being in the gamified arm did not raise compliance on average. The modelled difference was 1% in likelihood to respond. Forty-five gamified participants never used the coin store. Participants who spent more coins did respond more often, but that effect lost significance in outlier-free models (p=.052).

Gamification made responses slightly less reliable. The gamified arm's test-retest discrepancy on a repeated item was 0.20 rating points larger than the control arm's. Gamified participants who spent none of their coins averaged 0.72. The model estimated 0.51 for controls and 0.55 for gamified participants who spent all their coins.

## Instrumentation and Deployment Model

BYOD. Participants met staff online in small groups by video call, downloaded m-Path, consented electronically and completed baseline questionnaires. The study's purpose was described in general terms to avoid demand effects.

Ten notifications a day came semi-randomly between 9 AM and 7 PM for 10 days, 100 in total. The mean gap between notifications was 60 minutes (SD 25). A survey expired if not opened within 10 minutes. Each survey had 12 emotion items, seven life-domain items and one repeated emotion item for reliability.

The gamified arm earned 10 coins per completed survey plus a streak bonus of 2 coins per consecutive completion. Coins bought fun facts or personal graphs.

The surveys and coin store are published in the public m-Path library for replication. OS breakdown is not reported.

## Recruitment and Retention

| Stage | n |
|---|---|
| Enrolled | 200 |
| Excluded, phone malfunction | 2 |
| Excluded, erroneous sampling schemes | 3 |
| Excluded, early termination | 1 |
| Excluded, data withdrawal for unknown reasons | 1 |
| Analysed | 193 |

Recruitment method beyond the student and community pools is not reported. Pay did not depend on compliance. The authors call it low relative to comparable KU Leuven ESM studies.

## Data Completeness and Technical Issues

| Measure | Value |
|---|---|
| Compliance, whole sample, mean (SD) | 58.31% (21.13%) |
| Range | 1% to 96% |
| First day versus last day, modelled | 20% lower likelihood to respond |
| 9 AM versus 7 PM, modelled | 3% difference, not significant |
| Gamified versus control, modelled | 1% difference |
| Gamified participants who never used the store | 45 of 128 |
| Survey opening, all coins spent versus none, modelled | 23 seconds faster |
| Male versus female, modelled | 14% lower likelihood to respond |

Five of seven exclusions were technical. Two were phone malfunctions. Three were erroneous sampling schemes. The paper does not say whether the sampling-scheme errors were on the researcher or platform side.

The authors note that non-contingent pay led some participants to answer only a single assessment.

## Feasibility Findings

The authors conclude that instant gamification raises data quantity only for participants motivated to use it. It also lowers data quality. They recommend that reward schemes target both response quantity and response quality.

They make the gamification building blocks openly available in m-Path.

## Relevance to Future Study Design

Ten prompts a day with a 10-minute expiry, non-contingent pay and no cut-off gave 58% mean compliance over 10 days in a young sample. Treat that as a floor for this design rather than a typical rate.

Do not expect an in-app reward store to fix compliance by itself. A third of the gamified arm never opened it.

Add a repeated item if a reward scheme is used. That was how this study detected the drop in reliability.

## Evidence Confidence

Reported. All figures were read from the accepted author manuscript (KU Leuven Lirias repository, 49 pages, marked "in press") on 2026-10-31. The publisher's version of record was not read. Volume 160 comes from Crossref metadata.

Conflict note. The study was designed and run by m-Path's founders and staff on their own product. The headline result is unflattering to the gamification feature they built.

## Key Links

- Paper: https://doi.org/10.1016/j.chb.2024.108360
- Accepted manuscript: https://lirias.kuleuven.be/handle/20.500.12942/745047
- Preprint: https://doi.org/10.31234/osf.io/49h65
- Data and code: https://osf.io/ctznf/
- Local PDF: none held

## Related profiles

- Platform: [m-Path](../../module-02-digital-phenotyping/profiles/m-path.md)
- Incentive design and compliance: [`mpath-student-esm-incentive-type-rct.md`](mpath-student-esm-incentive-type-rct.md), [`beiwe-spinal-cord-injury-incentives.md`](beiwe-spinal-cord-injury-incentives.md), [`mpath-nssi-ema-benefits-challenges.md`](mpath-nssi-ema-benefits-challenges.md)
- Same developer group: [`carp-mpath-sense-performance-study.md`](carp-mpath-sense-performance-study.md), [`mpath-dementia-esm-feasibility.md`](mpath-dementia-esm-feasibility.md)

## Sources

1. Dejonckheere E, Verdonck S, Andries J, Röhrig N, Piot M, Kilani G, Mestdagh M. *Computers in Human Behavior* 2024;160:108360. DOI 10.1016/j.chb.2024.108360. Accepted manuscript read from KU Leuven Lirias, 2026-10-31. Establishes every figure in this profile.
