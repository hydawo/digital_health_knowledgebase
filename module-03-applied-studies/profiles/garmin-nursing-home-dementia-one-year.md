# Boyle et al. 2026 - Garmin smartwatch over one year in nursing home residents with dementia, DIPH.DEM, N=11

## Quick Facts

| Field | Details |
|---|---|
| Citation | Boyle LD, Patrascu M, Husebo BS, Haugarvoll K, Steihaug OM, Marty B. "A One-Year Study Using Digital Biomarkers From Sensing Technologies to Assess Changes in Physical Activity Levels and Sleep Quality in Nursing Home Residents With Dementia: Observational Study." *JMIR Nursing* 2026;9:e95194. DOI [10.2196/95194](https://doi.org/10.2196/95194). PMID 42684378 / PMC13524361. Published 2026-08-28. |
| Study design | Observational pilot, three repeated 7-day measurement windows. Part of DIPH.DEM, the pilot for the larger 5-D study. The paper calls itself an extension of an earlier baseline-only paper on the same cohort. |
| Sample size (enrolled / analyzed) | 11 recruited. 2 died during data collection. 9 in the final analysis. |
| Population | Residents aged 65 or over on two dementia wards of one Norwegian nursing home (Bergen region). Age 77 to 93 (mean 84.0, SD 6.1). 8 female, 3 male. Mean Clinical Dementia Rating 2.2. In residence a mean 17.6 months. |
| Duration | Seven days of continuous wear at baseline, 6 months and 1 year. Data collected February 2024 to May 2025. |
| Devices/platforms used | [Garmin](../../module-01-wearables/profiles/garmin.md) Vivoactive 5 (firmware 11.14) at baseline and 6 months. Garmin Venu 3 (firmware 12.11) at 1 year. Raw accelerometry at 25 Hz retrieved through a hub run by Fitrockr, a Berlin data broker. A contactless radar sleep sensor (Vital Things Somnofy, version 0.7) ran alongside. Somnofy is not profiled in Module 1 and is not covered here. No phenotyping platform. |
| Funding/COI | Western Norway Regional Health Authority (Helse Vest RHF, F-12829-D10484). Conflicts of interest "None declared." Participant compensation is not reported. The staff support model is not reported. |
| Last verified | 2026-10-22 |

## Summary

A consumer wrist wearable was deployed in nursing home residents with moderate dementia across a full year. The watch was worn continuously, including during sleep and bathing, for a week at each of three timepoints.

Adherence held. Wear time was 96% at baseline, 88% at 6 months and 94% at 1 year. The authors report no adverse events. The losses they name are mundane. The watch came off for charging for 1 to 2 hours on day 4. Participants also took it off themselves for periods of 2 hours or less.

Attrition was death, not dropout. Two of 11 residents died during the year.

The data held up less well than the wear did. Wrist ENMO separated residents from each other at any one timepoint (ICC 0.58 to 0.79). It was not stable within a person across the year (ICC 0.00 to 0.02). The authors conclude wrist accelerometry suits single-timepoint assessment better than longitudinal tracking in this group.

## Instrumentation and Deployment Model

Provisioning is implied rather than described. The paper does not say who fitted, charged or collected the watches. Data were synced, paired and retrieved through a hub via Fitrockr. The paper does not mention participant Garmin Connect accounts or phones. Only raw accelerometer data were analysed, although both models carry heart rate sensors.

The team changed hardware mid-study. The Vivoactive 5 was replaced by the Venu 3 at the 1-year timepoint "for improved battery capacity and data storage capabilities." The paper does not say what battery or storage problem prompted the change. It does not compare the two models' outputs. The 1-year values therefore come from a different device and firmware than the first two timepoints.

Wrist placement was a deliberate trade-off. The authors chose the wrist to minimise obtrusiveness for frail residents. They note that hip or low-back placement gives more accurate activity data in older adults.

The first and last partial days of each window were dropped. That left 5 full days and 6 nights of acceleration data per participant per timepoint.

## Recruitment and Retention

Recruitment came from two dementia wards in one nursing home. Residents had to have lived there more than 6 weeks. They also needed documented moderate-to-severe cognitive impairment or dementia, confirmed by record or a CDR of 1 or more. Delirium at baseline and a life expectancy under six weeks excluded them.

Residents with capacity consented directly. For the rest, a legal guardian consented, usually a family member. The number screened, the number eligible and the number of guardians who declined are not reported.

| Stage | n |
|---|---|
| Recruited | 11 |
| Died during data collection | 2 |
| Final analysis | 9 |

No withdrawals for burden or device intolerance are reported.

## Data Completeness and Technical Issues

Adherence was defined as total wear time on the Garmin after the first and last days were removed.

| Timepoint | Wear-time adherence |
|---|---|
| Baseline | 96% |
| 6 months | 88% |
| 1 year | 94% |

After partial days were removed, 135 acquisition periods of acceleration data were available. For sleep, 189 acquisition periods covering 219 nights were analysed, but those came from the radar sensor.

The paper names two causes of missing watch data. One was charging, for 1 to 2 hours on day 4. The other was periodic removal by participants, for periods of 2 hours or less.

No sync failures, data-broker problems, device losses or skin reactions are reported. How often staff checked the watches is not reported. Per-participant missingness is not reported.

The abstract describes "adherence and acceptability" as 88% to 96%. Those are the wear-time figures. No separate acceptability measure is described in the Methods.

## Feasibility Findings

The authors conclude that adherence and acceptability stayed high across the year with no adverse events. They say the chosen devices and their level of unobtrusiveness "were a good match for the cohort."

They also conclude that wrist ENMO was not reliable as a longitudinal measure. They suggest single-timepoint use, or added sensors and other body positions, for long-term monitoring. They name a trade-off between unobtrusiveness and data quality when choosing sensors for vulnerable groups.

## Relevance to Future Study Design

A consumer Garmin watch can be kept on residents with moderate dementia for a week at a time, three times over a year, at 88% to 96% wear. That is the clearest number here. The sample is nine people in one home.

Plan the charging gap. A one-week window on a Vivoactive 5 needed a 1 to 2 hour charge on day 4. The team then switched models for battery and storage reasons. Check that the chosen watch can hold raw 25 Hz accelerometry for the full window.

Do not change device models between timepoints unless the analysis can absorb it. Here the 1-year data came from different hardware and firmware.

High wear did not buy a stable longitudinal signal. A study that needs within-person change in activity over months should not assume wrist accelerometry will deliver it in this population.

Expect deaths, not dropouts, to drive attrition in a year-long nursing home study.

## Evidence Confidence

Verified. The enrolment and death counts, the three wear-time adherence figures and their definition, the named causes of missing data, the device models and firmware, the model switch and its stated reason, the Fitrockr retrieval route, the ICC ranges, and the funding and conflict statements were read from the publisher PDF (PMC13524361, CC BY 4.0) and the Europe PMC JATS full text on 2026-10-22.

Unclear. The acceptability claim has no instrument behind it in the Methods. Treat it as the authors' reading of the wear figures and the absence of adverse events.

The feasibility claims rest on 9 to 11 residents in one home.

## Key Links

- Paper (OA, CC BY 4.0): https://doi.org/10.2196/95194
- Europe PMC: https://europepmc.org/article/PMC/PMC13524361
- Baseline paper on the same cohort (not read for this profile): Boyle LD et al. *Sensors* 2025;25(21):6635. DOI 10.3390/s25216635. PMC12610480.
- Cross-sectional paper on the same cohort (not read for this profile): Boyle LD et al. *Front Aging* 2026;7:1768935. DOI 10.3389/fragi.2026.1768935. PMC12975902.
- Local PDF: `../literature/2026-boyle-jmirnursing-garmin-somnofy-nursing-home-dementia-one-year.pdf`

## Related profiles

- Device: [Garmin](../../module-01-wearables/profiles/garmin.md)
- Other Garmin deployment: [`garmin-low-income-physical-activity.md`](garmin-low-income-physical-activity.md)
- Dementia and older-adult deployments: [`mpath-dementia-esm-feasibility.md`](mpath-dementia-esm-feasibility.md), [`radar-ad-feasibility-usability.md`](radar-ad-feasibility-usability.md), [`sensorkit-techsans-older-adults.md`](sensorkit-techsans-older-adults.md)
- Wrist device with a mid-study configuration change: [`geneactiv-beiwe-college-year-deep-phenotyping.md`](geneactiv-beiwe-college-year-deep-phenotyping.md)

## Sources

1. Boyle LD, Patrascu M, Husebo BS, Haugarvoll K, Steihaug OM, Marty B. *JMIR Nursing* 2026;9:e95194. DOI 10.2196/95194. Publisher PDF and Europe PMC JATS full text (PMC13524361) read 2026-10-22. Establishes every figure in this profile.
