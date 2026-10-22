# Kedoin et al. 2026 - Fitbit Inspire 3 with GPT-4o sleep feedback over LINE, high school female soccer team, pilot RCT, N=25

## Quick Facts

| Field | Details |
|---|---|
| Citation | Kedoin H, Itoh Y, Nirengi T, Sato Y, Sugisawa S, Nishio Y, Akitsu R. "Feasibility and Preliminary Effects of AI-Generated Personalized Sleep Feedback in High School Female Soccer Players: Pilot Randomized Controlled Trial." *JMIR Formative Research* 2026;10:e101615. DOI [10.2196/101615](https://doi.org/10.2196/101615). PMID 42821993 / PMC13673175. Published 2026-10-01. |
| Study design | Single-team pilot RCT, parallel groups, stratified 1:1 allocation. Technical and operational feasibility is a stated aim alongside preliminary efficacy. Registered retrospectively (UMIN000061189, 2026-04-07), about eight months after study procedures began. |
| Sample size (enrolled / analyzed) | 25 enrolled. 25 analyzed (12 intervention, 13 control). No withdrawals. |
| Population | Female soccer players from one high school team, Japan. Mean age 16.93 (SD 0.70). Mean playing experience 9.61 years (SD 2.14). The school is not named. |
| Duration | Ten weeks after a week-0 setup session. Briefing and setup 2025-08-18. Baseline observation weeks 1 to 4 from 2025-09-01. Randomization in week 5. Intervention weeks 6 to 9. Final assessment completed 2025-11-03. |
| Devices/platforms used | [Fitbit](../../module-01-wearables/profiles/fitbit-google.md) Inspire 3, study-provisioned and collected at week 10. Participants used their own smartphones for Fitbit sync and LINE. A custom Google Apps Script pipeline pulled sleep data from the Fitbit Web API, sent it to GPT-4o, and delivered messages through the LINE Messaging API. No Module 2 platform. |
| Funding/COI | 2025 Nippon Sport Science University Academic Research Grant. The authors built the intervention system themselves. They declare no commercial ownership, patents or licensing income. They declare no funding, equipment or technical support from Fitbit, Google, OpenAI or LY Corporation. Participants received monetary compensation. The amount is not reported. |
| Last verified | 2026-10-22, against the Europe PMC full-text XML (PMC13673175) |

## Summary

This is a small, tightly run deployment of a consumer tracker in minors. Its main operational interest is the automated pipeline between the tracker and the participant. The study wired the Fitbit Web API to a large language model and a messaging app, then ran it unattended for four weeks.

Retention was total. All 25 players finished, and questionnaire completion was 100% at both assessments. Every message the system sent was delivered.

The wear figure is the useful one. Median valid Fitbit nights were 26 (IQR 24 to 28) in the intervention group and 22 (IQR 15 to 26) in the control group. The intervention only produced a message on days with valid prior-night data. Missing a night therefore cost an intervention participant her morning feedback. The authors do not discuss this as a driver of the wear gap, and the design cannot separate it from chance in 25 people.

## Instrumentation and Deployment Model

Hybrid. The Fitbit Inspire 3 was handed out at a week-0 briefing attended by players, parents and coaching staff. Apps were configured and participants joined the study's LINE official account in the same session. Eligibility required a smartphone able to run LINE and sync Fitbit data. Players were told to wear the device on the non-dominant wrist during sleep. Daytime wear was not requested.

The custom integration is described in unusual detail.

- A user management sheet in Google Sheets held each participant's study ID, LINE user ID, nickname, group, Fitbit authentication details and data-sheet name.
- Google Apps Script called the Fitbit Web API sleep endpoint (`/1.2/user/-/sleep/date/{date}.json`) with OAuth 2.0 bearer tokens. Expired tokens were refreshed with the stored refresh token and the call was retried.
- Only records flagged `isMainSleep = true` were kept. Naps were therefore discarded.
- The script time zone was set to Japan Standard Time.
- For the intervention group, nickname and sleep metrics were sent to GPT-4o through the OpenAI Responses API. Names, school, LINE IDs and Fitbit credentials were not sent.
- Messages went out through the LINE Messaging API. Date and participant flags prevented duplicate delivery. API rate limits and server errors triggered retries with exponential backoff. An unextractable response was logged and no message was sent.

The system was tested with dummy data and test users before the trial. The prompt, model, delivery logic and API settings were frozen for the study period. Generated messages were not reviewed by researchers before delivery.

The control group received fixed, pre-reviewed general sleep messages at 8 AM daily. Those were also written with GPT-4o, before the trial started.

## Recruitment and Retention

Recruitment was the whole available team. The sample size was set by enrolling all eligible players available during the study period. The number of players approached is not reported in the text. No one was excluded after eligibility screening.

| Stage | n |
|---|---|
| Enrolled | 25 |
| Allocated to intervention | 12 |
| Allocated to control | 13 |
| Withdrew | 0 |
| Analyzed | 25 |

Assent came from the players. Written consent came from a parent or guardian for each player. Coaching staff received the same written and verbal explanation as parents.

## Data Completeness and Technical Issues

A valid wear night was a night on which the Fitbit recorded a main sleep episode with every sleep variable needed for analysis. No minimum number of valid nights was required per participant. Missing nights were not imputed. Each participant's sleep metrics are means over whatever valid nights she had.

| Measure | Intervention (n=12) | Control (n=13) |
|---|---|---|
| Valid Fitbit wear nights, median (IQR) | 26 (24 to 28) | 22 (15 to 26) |
| LINE delivery success, of messages sent | 100% | 100% |
| Questionnaire completion, baseline and post | 100% | 100% |

The paper does not state which weeks the wear-night counts cover or what the denominator is. The paragraph sits under the description of the intervention period. Without the window, the figures cannot be turned into a percentage.

Delivery success is measured against messages sent. An intervention participant with no valid prior-night data received no message that day, and that non-event was logged rather than counted as a failure. The number of such days per participant is not reported.

The paper reports "no major technical problems affecting intervention delivery or study continuation." It does not report how often tokens were refreshed, how often retries fired, or whether any sync gaps occurred. No adverse events and no privacy breaches were reported.

Not reported are battery or charging burden, device loss or damage, iOS versus Android breakdown, message opening or reading, acceptability, and perceived burden. The authors state that engagement and acceptability were not assessed at all.

## Feasibility Findings

The authors conclude that the multicomponent system "demonstrated technical and operational feasibility in this single-team setting." They base this on 100% delivery, 100% questionnaire completion, and the absence of major technical problems, adverse events and privacy breaches.

They limit the claim themselves. Feasibility here means technical and operational feasibility only. It does not establish acceptability or sustained use.

Their design recommendations are for the next trial. They call for prospective registration, a larger sample, longer follow-up and direct measurement of engagement and acceptability. In multi-team studies they recommend cluster randomization by team, because messages may have been shared between arms within one team.

## Relevance to Future Study Design

The pipeline is the transferable part. It shows a Fitbit Web API sleep pull with token refresh running daily for a month without reported failure. A team building automated feedback on Fitbit data can copy its failure handling, which covers token expiry, duplicate suppression, retries with backoff, and no message on missing data.

Making feedback conditional on valid data may raise wear. That is a hypothesis this paper raises but does not test. The intervention arm's median was four nights higher, and its IQR was much narrower.

A 100% delivery rate is not a measure of reach when nothing is sent on missing-data days. Report delivered messages against scheduled days as well as against sent messages.

The `isMainSleep` filter drops naps and split sleep. That matters less for high school students than for shift workers, but it shapes what "valid night" means.

Retention of 25 out of 25 came with a coach-attended in-person setup, parental consent, a single team and monetary compensation. Those conditions are not reported in enough detail to cost.

## Evidence Confidence

Verified. The enrolment, allocation and retention counts, the valid-night definition, the wear-night medians and IQRs, the delivery and questionnaire completion rates, the integration architecture, the funding and conflict statements, and the dates were all read from the Europe PMC full-text XML of the published article (CC BY 4.0) on 2026-10-22.

Unclear. The time window and denominator behind the valid-wear-night medians are not stated. The CONSORT diagram (Figure 4) was not legible in the XML text, so any screening count it holds was not read.

The first author was taken from the XML's author contributor records, not from a PDF byline. The XML lists a JMIR editor and reviewer before the authors, which is the known JMIR ordering hazard. Kedoin H is first among the records typed as authors.

## Key Links

- Paper (OA, CC BY 4.0): https://doi.org/10.2196/101615
- Europe PMC: https://europepmc.org/article/PMC/PMC13673175
- Trial registration: UMIN000061189
- Local PDF: none. Europe PMC's render returned HTML, PMC returned a bot check and JMIR's PDF endpoint refused automated retrieval. Full text was read from the Europe PMC XML.

## Related profiles

- Device: [Fitbit](../../module-01-wearables/profiles/fitbit-google.md)
- Other Fitbit deployments: [`fitbit-actigraph-proudme-summer-camp-adolescents.md`](fitbit-actigraph-proudme-summer-camp-adolescents.md), [`sleepsight-schizophrenia-rest-activity.md`](sleepsight-schizophrenia-rest-activity.md), [`beiwe-fitbit-gynecologic-cancer-hope.md`](beiwe-fitbit-gynecologic-cancer-hope.md)
- Adolescent deployments: [`beiwe-adolescent-feasibility.md`](beiwe-adolescent-feasibility.md), [`avicenna-adolescent-esm-school-phone-bans.md`](avicenna-adolescent-esm-school-phone-bans.md)
- Ring adherence in a nightly-wear protocol: [`oura-tempredict-healthcare-worker-adherence.md`](oura-tempredict-healthcare-worker-adherence.md)

## Sources

1. Kedoin H, Itoh Y, Nirengi T, Sato Y, Sugisawa S, Nishio Y, Akitsu R. *JMIR Formative Research* 2026;10:e101615. DOI 10.2196/101615. PMC13673175. Full text including Tables 1 to 3, figure captions, ethics, funding and conflict statements read from the Europe PMC full-text XML, 2026-10-22. Establishes every figure in this profile.
