# Mayne et al. 2023 - AWARE GPS tracking with text-message EMA and Actiwatch in Philadelphia adolescents, N=25 over 7 days

## Quick Facts

| Field | Details |
|---|---|
| Citation | Mayne SL, DiFiore G, Hannan C, Nwokeji U, Tam V, Filograna C, Martin T, South E, Mitchell JA, Glanz K, Fiks AG. "Feasibility and acceptability of mobile methods to assess home and neighborhood environments related to adolescent sleep." *Sleep Health* 2023;9(3):331-338. DOI [10.1016/j.sleh.2023.01.014](https://doi.org/10.1016/j.sleh.2023.01.014). PMID 36781356 / PMC10293018 (author manuscript). |
| Study design | Single-arm pilot. Feasibility and acceptability of GPS tracking and EMA are the stated aims. Exploratory bivariate associations with sleep outcomes are secondary. |
| Sample size (enrolled / analyzed) | 25 adolescents enrolled and described. The screening and refusal funnel is not reported. Actigraphy available for 23 of 25. Morning EMA analysed for 108 nights from 24 teens. GPS exposure analysis used 135 days from 21 adolescents after accuracy and minimum-minutes filters. |
| Population | Adolescents aged 15 to 17 in Philadelphia, Pennsylvania, USA. Mean age 16.2, 56% male, 52% non-Hispanic white, 36% non-Hispanic Black. 68% had a parent with a bachelor's degree or higher. Enrolled November 2020 to July 2021, during the COVID-19 pandemic. |
| Duration | 7 days of continuous collection per participant, followed by an exit interview. |
| Devices/platforms used | [AWARE Framework](../../module-02-digital-phenotyping/profiles/aware-framework.md) app on participants' own smartphones for GPS only. EMA was delivered by text message with REDCap survey links, not through AWARE. Philips Actiwatch-2 (not profiled in Module 1) mailed to participants, plus a paper sleep diary. |
| Funding/COI | Leonard Davis Institute pilot grant, NHLBI K01HL155860 and internal Children's Hospital of Philadelphia funding. Competing interests "None". Compensation up to $90 for adolescents and $10 for parents. |
| Last verified | 2026-10-31 |

## Summary

This is a small, remote pilot that ran AWARE as a GPS logger on teenagers' own phones for one week. It sits in the module because the paper reports location completeness per participant-day and names the cause of the missing data.

Location capture was high. The study collected 202,763 GPS coordinates from 25 participants. Coordinates were available for a mean of 19.6 hours per participant-day (SD 8.2, median 24, range 0 to 24). Five participants (20%) had a coordinate for every possible minute of their week.

The missing GPS data had two named causes. Participants turned their phones off. Some Android phones also needed extra settings enabled manually to override limits on background collection.

Text-message EMA reached 78.6% overall completion. Completion was highest in the late afternoon (88.0%) and lowest in the morning (61.7%). The per-participant median was 86% (range 29 to 100%).

## Instrumentation and Deployment Model

Bring your own device. Eligibility required a smartphone with a text and data plan. Participants downloaded an AWARE app onto their own phones. It ran in the background and recorded latitude and longitude every 60 seconds, with speed, bearing, altitude and estimated accuracy. The paper does not say which AWARE client was used, whether iOS phones took part, or how many participants used each OS.

The whole study was remote because of COVID-19. Consent and assent went through REDCap and WebEx. The Actiwatch-2 and paper sleep diary arrived by mail.

EMA ran outside AWARE. Four surveys a day were sent at random times within fixed windows by text message with an embedded REDCap link. School-day windows were 6:00 to 8:00, 14:00 to 16:00, 17:00 to 19:00 and 20:00 to 22:00. Non-school-day windows started later. The morning window was adjusted to each participant's wake time and school start time.

For the exposure analysis, coordinates outside Philadelphia or with accuracy worse than 100 metres were dropped. Person-days with fewer than 360 minutes of accurate GPS were also dropped.

## Recruitment and Retention

Recruitment was mostly by email invitations from CHOP's Recruitment Enhancement Core to parents of 15 to 17 year olds with Philadelphia addresses who had received CHOP care. Flyers in CHOP primary care practices and on campus supplemented this. Parents completed an online screener. The number invited, screened and refused is not reported.

Retention through the 7 days is not reported as a separate figure. All 25 participants appear in the descriptive tables.

## Data Completeness and Technical Issues

GPS completeness per participant-day was a mean of 19.6 hours (SD 8.2). The range ran from 0 to 24 hours. The paper attributes missing GPS "primarily" to phones being turned off and to an Android issue "where additional settings needed to be manually enabled to override limits on data collection." It does not say how many phones were affected or whether the settings were fixed during collection.

Participants checked a map of one recent day's locations at the exit interview. Most said it matched their movements. One participant had inaccurate data "due to an unexplained technical issue."

The analytic GPS sample was 135 days from 21 adolescents after the accuracy and 360-minute filters. The paper does not report how many days or participants each filter removed.

Actigraphy was missing for 2 of 25 participants. One did not return the Actiwatch. One Actiwatch malfunctioned.

The main EMA barrier participants named was not being near their phone when the notification arrived. They asked for consistent pre-specified survey times and a longer morning window.

Battery drain, data upload volume, app crashes and server-side problems are not reported.

## Feasibility Findings

The authors conclude that smartphone GPS tracking and EMA were feasible and acceptable for assessing time-varying home and neighbourhood exposures in adolescents for up to one week.

Privacy concern was low. One participant (4%) agreed with "I was worried about my privacy due to the app tracking my location." 80% agreed or strongly agreed that EMA surveys were easy to answer. 84% disagreed that surveys interfered with daily activities.

The authors note that BYOD GPS avoids issuing a research device. They also list the costs. Apps must work across operating systems. Missing data comes from signal loss, phones being off and tall buildings. They recommend continuous data monitoring so staff can troubleshoot with participants.

## Relevance to Future Study Design

AWARE GPS on teenagers' own phones held a median of 24 hours a day for a week. The mean was nearly five hours lower, so a minority of participant-days carried most of the loss.

Plan for Android background limits at onboarding. The paper names manual settings changes as one of two main causes of missing location data. A setup checklist that enables those settings before day one is the obvious mitigation.

Morning EMA is the weak slot in school-age participants. A 61.7% morning completion against 88.0% in the late afternoon is a large gap for a one-week study.

The sample was relatively high in socioeconomic status. The authors say this may have understated problems with smartphone data and Wi-Fi access.

## Evidence Confidence

Verified. The GPS completeness figures, the two named causes of missing GPS, the EMA completion rates, the acceptability percentages, the Actiwatch losses, the compensation and the funding statement were all read from the Europe PMC/NCBI full text of the author manuscript (PMC10293018) on 2026-10-31.

Unclear. Which AWARE client ran, the iOS and Android split, and how many Android phones needed the settings change are not reported.

Not assessed here. The associations between neighbourhood exposures and sleep are exploratory, small-sample findings outside Module 3's scope.

## Key Links

- Paper: https://doi.org/10.1016/j.sleh.2023.01.014
- Europe PMC (author manuscript): https://europepmc.org/article/PMC/PMC10293018
- Local PDF: none held. Not stored by this screening pass.

## Related profiles

- Platform: [AWARE Framework](../../module-02-digital-phenotyping/profiles/aware-framework.md)
- Other AWARE deployments in young people: [`aware-light-smartsense-d-youth-depression.md`](aware-light-smartsense-d-youth-depression.md), [`aware-binge-drinking-jitai-sensor-loss.md`](aware-binge-drinking-jitai-sensor-loss.md)
- Passive location completeness in other cohorts: [`aware-msavorus-passive-completeness-companion.md`](aware-msavorus-passive-completeness-companion.md), [`mindlamp-older-adults-gps-cognition-feasibility.md`](mindlamp-older-adults-gps-cognition-feasibility.md)

## Sources

1. Mayne SL, DiFiore G, Hannan C, Nwokeji U, Tam V, Filograna C, Martin T, South E, Mitchell JA, Glanz K, Fiks AG. *Sleep Health* 2023;9(3):331-338. DOI 10.1016/j.sleh.2023.01.014. PMC10293018. Full text of the author manuscript read via NCBI efetch, 2026-10-31. Establishes every figure in this profile.
