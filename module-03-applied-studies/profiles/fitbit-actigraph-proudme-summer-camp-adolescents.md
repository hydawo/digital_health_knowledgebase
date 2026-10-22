# Tan et al. 2026 - Fitbit Charge 6 and ActiGraph GT3X+ in the ProudMe summer obesity prevention pilot, adolescents 11 to 14, N=26

## Quick Facts

| Field | Details |
|---|---|
| Citation | Tan Q, Son P, Nie Y, Yang P, Staiano AE, Wang F, Shepherd DC, Queen K, Gordon S, Chen S. "Integrating technology-assisted behavioral management into a summer obesity prevention intervention program: a pilot controlled trial." *Frontiers in Physiology* 2026;17:1914161. DOI [10.3389/fphys.2026.1914161](https://doi.org/10.3389/fphys.2026.1914161). PMID 42819245 / PMC13623721. Published 2026-09-16. |
| Study design | Non-randomized pilot controlled trial, two parallel groups. Allocation followed availability for the in-person camp. Not prospectively registered. Usage of the three technology components is a stated aim. |
| Sample size (enrolled / analyzed) | 26 signed up and completed baseline (14 intervention, 12 control). One intervention participant withdrew after week 1. 25 completed post assessments. Fitbit data were usable for 10 of the 13 remaining intervention participants. |
| Population | Adolescents aged 11 to 14 living within 10 miles of the Louisiana State University campus, Baton Rouge, in neighbourhoods with moderate to high Area Deprivation Index rankings. 17 male, 9 female. 13 Black or African American, 9 Asian American, 3 White, 1 Hispanic. Five had obesity and four were overweight. |
| Duration | Eight weeks in summer 2025. A 10-day in-person camp over two weeks, then a six-week technology-supported extension at home. |
| Devices/platforms used | [Fitbit](../../module-01-wearables/profiles/fitbit-google.md) Charge 6, provided to intervention participants for the whole eight weeks. [ActiGraph](../../module-01-wearables/profiles/ametris-actigraph.md) GT3X+, hip-worn, during camp hours for the intervention group and at pre and post assessments for both groups. ProudMe Tech, a custom AI-assisted mobile app built by the LSU team. Participants used their own mobile devices for the app. No Module 2 platform. |
| Funding/COI | Louisiana Board of Regents Research Competitiveness Subprogram (LEQSF(2022-24)-RD-A-03), the LSU Foundation and Our Lady of the Lake Collaboration in Action Program 2024, and the Helen "Bessie" Silverberg Pliner Professorship. The authors declare no commercial or financial conflicts. Participant compensation is not reported. Camp included free lunch as an intervention component. |
| Last verified | 2026-10-22, against the publisher PDF |

## Summary

This pilot stacks three technologies onto a short summer camp for young adolescents from deprived neighbourhoods. The operational story is a two-phase one. Everything worked inside the supervised camp. Much less of it held up once the children went home.

The Fitbit stream is where that shows. Three of the 13 intervention participants who stayed in the study produced no usable Fitbit data at all. One lost the device. Two had sync failures that left nothing to export. Among the ten with data, recorded days ranged from 4 to 43, a mean of 19.6 (SD 14.2) over an eight-week intervention.

The app showed the same decline. Entries fell from 271 in week 1 and 247 in week 2 to a steadily lower count across the six home weeks. That happened despite parent reminders. The paper gives the total of 851 entries, but the weekly counts after week 2 appear only in a figure.

## Instrumentation and Deployment Model

Provisioned trackers, own phones. Intervention participants were given Fitbit Charge 6 devices for self-monitoring. Eligibility required access to a personal mobile device for at least 15 minutes a day, so the app ran on whatever device the family had. The paper does not say whether that device was a phone, a tablet or shared.

ActiGraph GT3X+ accelerometers had two roles. During camp, intervention participants wore them on the right waist from 8 AM to 1 PM on all ten camp days. At pre and post assessments both groups wore them, and a valid day needed at least 10 hours of wear. Epochs were 15 seconds, with Freedson cut-points.

ProudMe Tech was adapted from a web-based platform into a mobile app. It used a React.js front end, a Node.js/Express back end and MongoDB. Participants set SMART goals, logged physical activity, diet, screen time and sleep, and wrote reflections. Each entry triggered a GPT-4o response capped at 75 tokens at temperature 0.9. Every response passed through the OpenAI Moderation API before display. A post hoc review of all 851 generated messages found no unsafe responses.

The app was not connected to the Fitbit. App, Fitbit and accelerometer data were each downloaded to a local drive. The Fitbit export route is not described.

Parents received materials by email in weeks 1, 2, 4 and 6. From week 2 to week 8 families were encouraged to support app use three to five times a week and daily Fitbit wear. A trained camp counsellor helped campers with the app during camp sessions.

## Recruitment and Retention

Parents registered their children after parent-facing flyers and social media announcements. An online registration form served as screening. The number of families who registered but were not enrolled is not given in the text. The flow diagram (Figure 1) was not legible as text.

| Stage | n |
|---|---|
| Signed up and completed baseline | 26 |
| Intervention group | 14 |
| Control group | 12 |
| Intervention withdrawal after week 1 | 1 |
| Completed post assessment | 25 |
| Intervention participants with usable Fitbit data | 10 of 13 |
| Valid ActiGraph at pre (intervention / control) | 14 / 12 |
| Valid ActiGraph at post (intervention / control) | 13 / 10 |

The reason for the one withdrawal is not reported. The abstract describes the sample as 25 participants, while the methods and Table 2 count 26 at baseline.

## Data Completeness and Technical Issues

The Fitbit definition is loose by design. No minimum daily wear time was applied. A reported day was any exported day with non-zero recorded activity. Days with no recorded activity were treated as missing. Wear time itself was not measured.

| Fitbit measure (intervention, n=10 with records) | Value |
|---|---|
| Reported activity days, range | 4 to 43 |
| Reported activity days, total | 196 person-days |
| Reported activity days per participant | 19.6 (SD 14.2) |
| Fitbit-recorded activity | 30,079 min total; 153.5 min per reported day |
| Weekday versus weekend activity | 166.2 vs 135.6 min/day (p=.039) |

Technical failure modes named in the paper are one lost Fitbit and two "unsuccessful device synchronization" cases with no exportable activity data. The cause of the sync failures is not reported. The paper does not say whether the lost device was replaced.

The ActiGraph pre and post data lost two control participants at post. The reason is not given. Camp-hour ActiGraph data cover 13 intervention participants. The number of valid camp days per participant is not reported.

The authors caution that the weekday excess "might have reflected biased PA time toward the more compliant participants." With ten participants and recorded days ranging from 4 to 43, that is a real risk.

Not reported are Fitbit days split by camp and home phases, battery or charging problems, iOS versus Android, how or how often Fitbit data were exported, compensation, and reasons for app disengagement.

## Feasibility Findings

The authors conclude that the technology components "could be implemented within the structured summer camp setting, although sustained technology usage during the post-camp extension was limited." They describe app acceptability as modest. Total acceptability rose from 54.4% (SD 21.8) in week 1 to 58.3% (SD 20.3) in week 2.

They read the home-phase decline as evidence that general parent reminders and resources were not enough. Their recommendations are automated app reminders, missed-entry notifications, scheduled check-ins, parent-child goal review and coaching prompts. They also recommend moving from parental reminders to parental integration, such as shared goals and joint review of app progress. Finally, they suggest longer camp exposure or alternating in-person and remote weeks.

## Relevance to Future Study Design

Expect the supervised phase to flatter the device. Inside camp, the counsellor, the schedule and the peer group carried adherence. At home, Fitbit and app use fell off. The paper reports this for the app with weekly counts. For the Fitbit it reports only the overall spread.

Budget for total stream loss in a share of provisioned trackers. Here it was 3 of 13, through one loss and two sync failures. A protocol that checks for a first successful sync in the first days of home use would catch the sync cases early. This paper does not say whether any such check existed.

Set a wear-time rule before analysis. A non-zero-activity day definition makes Fitbit data look available without saying how long the device was worn. That makes the 196 person-days hard to compare with studies that use a 10-hour rule.

The eligibility rule of a personal device for 15 minutes a day did not exclude anyone as far as the paper reports. It leaves open whether the app ran on a phone the child carried. [Carlson 2026](garmin-low-income-physical-activity.md) defined smartphone access at household level in a low-income sample, which raises the same question.

## Evidence Confidence

Verified. The enrolment, withdrawal and assessment counts, the Fitbit and ActiGraph protocols, the Fitbit usable-record count and its three failure causes, every figure in the Fitbit table, the app entry counts for weeks 1 and 2 and in total, the acceptability scores, the app architecture, and the funding and conflict statements were read from the publisher PDF (CC BY) on 2026-10-22.

Reported. Weekly app entries after week 2 are described only as a steady decline in the text. Their values are in Figure 4, which was not read numerically.

Unclear. The withdrawal reason, the cause of the two sync failures, and the number of families screened are not stated in the text.

## Key Links

- Paper (OA, CC BY): https://doi.org/10.3389/fphys.2026.1914161
- Europe PMC: https://europepmc.org/article/PMC/PMC13623721
- Local PDF: `../literature/2026-tan-frontphysiol-proudme-summer-obesity-prevention-fitbit-actigraph.pdf`

## Related profiles

- Devices: [Fitbit](../../module-01-wearables/profiles/fitbit-google.md), [ActiGraph](../../module-01-wearables/profiles/ametris-actigraph.md)
- Low-income physical activity intervention with paid participants: [`garmin-low-income-physical-activity.md`](garmin-low-income-physical-activity.md)
- Another 2026 Fitbit pilot with GPT-4o feedback: [`fitbit-ai-sleep-feedback-adolescent-soccer.md`](fitbit-ai-sleep-feedback-adolescent-soccer.md)
- Adolescent deployments: [`beiwe-adolescent-feasibility.md`](beiwe-adolescent-feasibility.md), [`avicenna-adolescent-esm-school-phone-bans.md`](avicenna-adolescent-esm-school-phone-bans.md)
- Other ActiGraph deployments: [`actigraph-als-upper-limb-wear-time.md`](actigraph-als-upper-limb-wear-time.md), [`beiwe-actigraph-modus-als-progression.md`](beiwe-actigraph-modus-als-progression.md)

## Sources

1. Tan Q, Son P, Nie Y, Yang P, Staiano AE, Wang F, Shepherd DC, Queen K, Gordon S, Chen S. *Frontiers in Physiology* 2026;17:1914161. DOI 10.3389/fphys.2026.1914161. PMC13623721. Full text, Tables 1 to 4 and figure captions read from the publisher PDF, 2026-10-22. Establishes every figure in this profile.
