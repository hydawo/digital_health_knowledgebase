# Module 3 citation-graph screening, batch A, 14 papers, 2026-10-31

Screened against `_screening-and-profile-rules.md` Part A, the Module 3 section of CLAUDE.md and the README scope rules. Candidates came from the 2026-10 citation-graph pass (`_citation-graph-scan-2026-10.md`). All 14 arrived tagged as m-Path citers. Full text was read for every paper. Europe PMC full-text XML was used where a PMCID existed. PMC13395528 returned HTTP 500 from Europe PMC and was fetched as XML through NCBI E-utilities. Paper 1 came from the Research Square PDF. Paper 7 came from the accepted manuscript in the KU Leuven Lirias repository. Paper 8 came from the Umeå DiVA repository copy of the published PDF. No bot check was met. No PDF was stored in the repo.

The cohort-overlap check grepped `profiles/*.md`, `literature-index.json` and `_scan-queue.md` for each DOI, first author and cohort keyword. Two overlaps were found. Paper 14 is the Leuven NSSI cohort already profiled. Paper 5 shares its Leipzig cohort with a profile written today by a parallel batch.

The citation was right about the instrument for 13 of 14. Paper 6 cites m-Path but deployed its own Concerto-based web app.

| # | Paper | Verdict | Reason code | Device/platform actually deployed |
|---|---|---|---|---|
| 1 | Muller 2026, Research Square | INCLUDE | (deployment; funnel, compliance, technical barriers, safety load) | m-Path, BYOD |
| 2 | Böge 2025, Internet Interventions | BORDERLINE-include | (deployment; funnel, retention with reasons, completion vs benchmarks) | m-Path |
| 3 | O'Driscoll 2025, JMIR Ment Health | INCLUDE | (deployment; CONSORT funnel, withdrawal reasons, EMA and EMI engagement) | m-Path, BYOD |
| 4 | Elmer 2025, JMIR Ment Health | INCLUDE | (deployment; funnel with reasons, compliance, device loss) | m-Path, BYOD |
| 5 | Kaufmann 2025, Front Psychiatry | INCLUDE | (deployment; non-participation and dropout reasons, early reporting) | app built on m-Path, BYOD |
| 6 | Harrison 2023, JMIR | REJECT | architecture (instrument not profiled: EMCAT on Concerto) | EMCAT progressive web app built on Concerto (Cambridge Psychometrics Centre) |
| 7 | Dejonckheere 2024, Comput Human Behav | INCLUDE | (deployment experiment; exclusions, compliance, incentive effect) | m-Path, BYOD |
| 8 | Ekelund 2025, Int J Sport Exerc Psychol | BORDERLINE-reject | no-cohort | m-Path premium, BYOD |
| 9 | O'Driscoll 2024, JMIR Form Res | BORDERLINE-include | (deployment; retention, compliance, low-compliance exclusions) | m-Path plus Qualtrics, BYOD |
| 10 | Oba 2025 (SCED), JMIR Form Res | BORDERLINE-reject | no-cohort | m-Path on a provisioned phone, plus an unnamed activity tracker |
| 11 | Wong 2025, JMIR Form Res | REJECT | architecture | m-Path (prototype co-design only) |
| 12 | Oba 2025 (RCT), JMIR Form Res | INCLUDE | (deployment; funnel, zero dropout, EMA compliance, Fitbit wear, skin rash) | Fitbit Sense or Sense 2 plus m-Path, both provisioned |
| 13 | Weseman 2026, J Affect Disord | INCLUDE | (deployment; contact funnel, compliance, latency) | m-Path, BYOD |
| 14 | Kiekens 2024, JAMA Netw Open | BORDERLINE-reject | duplicate-cohort | m-Path |

Rows follow batch-file order. Row n is batch index n-1.

---

## 1. Muller et al. 2026, Research Square (preprint)

- Source read: Research Square PDF, 8 pages of article text, CC BY 4.0. Not peer reviewed.
- First author: Caroline Muller (byline). Posted 2026-09-24. DOI 10.21203/rs.3.rs-10880727/v1. PMCID none.
- Deployed (Methods, Study Procedure): "The research assistant then administered a baseline survey and helped the participant install the EMA application m-path (21) on the participant's smartphone." Matches the citation.
- Verdict: INCLUDE. Feasibility is the primary aim. The paper reports an eligibility funnel with reasons, prompt-level compliance, named connectivity and charging barriers, and a full breakdown of 42 safety activations.
- Existing profile on this cohort: none.
- Profile written: `profiles/mpath-zambia-youth-post-suicide-attempt-ema.md`.

### Extraction

- Design: mixed-methods short-term longitudinal EMA feasibility study (Methods, Study Design).
- Funding/COI: Eckenstein Geigy Professorship (Swiss TPH), Flourishing Minds Fund, University of Basel tenure-track professorship. Funders paid personnel, fieldwork, travel and participant incentives. No competing interests.
- Population/setting: ages 17 to 25, treated for a suicide attempt in seven public hospitals in Lusaka, Zambia. Mean age 21.5. 14 female, 7 male. Mean PHQ-9 14.0. 76.2% PHQ-9 of 10 or more. Lifetime attempts 1 to 6 (Table 2).
- Funnel (Results, Recruitment and Enrollment): 28 fully eligible, 21 enrolled (75.0%). Non-enrolment 3 no smartphone, 2 declined, 1 phone could not support m-Path, 1 could not travel.
- Retention (Participant Retention): 20 of 21 (95.24%) answered at least one prompt.
- Duration: 14 days, starting one week after recruitment.
- Deployment model: BYOD. Mobile data support. 14 Kwacha (0.54 EUR) per answered prompt, paid as phone-data money.
- Schedule: 06:00 prompt, 10:00 reminder, open to 12:00. 16:00 prompt, 20:00 reminder, open to 23:00. About three minutes per survey. m-Path forced full completion.
- Compliance (Prompt Completion and Compliance): 308 of 560 (55%). Mean 14.4 prompts (SD 9.5, median 14, range 0 to 28). Mean 8.8 days with any prompt (SD 5, median 9, range 0 to 14).
- Technical failure modes: intermittent internet connectivity, phone charging, a participant using a sibling's phone. Two participants unhappy with prompt timing.
- Safety (Emergency Activation Protocol): 42 activations among 18 participants. 11 unanswered (26.2%, 7 participants). 8 false activations (19.0%). 14 referrals (33.3%, 9 participants). 9 brief counselling (21.4%, 8 participants).
- Authors' conclusions: feasible and acceptable. Barriers are modifiable. The safety protocol is resource-intensive. They recommend adaptive EMA (CAT-MH) and clearer momentary-framing instructions.
- Not reported: number screened before eligibility, recruitment dates, OS, phone models, per-day compliance trend.
- Inconsistencies: 560 scheduled prompts equals 20 x 28, not 21 x 28. The abstract says "evening" and Methods says "afternoon" for the 16:00 prompt.

---

## 2. Böge et al. 2025, Internet Interventions

- Source read: Europe PMC full-text XML (PMC11816215). XML only.
- First author: Kerem Böge (first `contrib-type="author"` record). Not checked against a PDF byline. Internet Interventions 2025;39:100804. DOI 10.1016/j.invent.2025.100804. PMCID PMC11816215. NCT06207526.
- Deployed (Methods, Intervention): "The present intervention was thematically adapted to the context of delusions and used the mPath app (KU Leuven)." Matches the citation.
- Verdict: BORDERLINE-include. N=10 analysed is small. Feasibility is the primary outcome, and it reports a screening funnel, three losses with reasons and EMA/EMI completion against preset benchmarks.
- Existing profile on this cohort: none.
- Profile written: `profiles/mpath-dice-delusions-blended-ema-pilot.md`.

### Extraction

- Design: single-arm open-label pilot. Traffic-light progression criteria.
- Funding/COI: Berlin University Alliance, DAAD. NT and KB write CBT-for-psychosis books. KB co-founded digital-psychosis start-ups. 50 EUR on completion.
- Population: SSD outpatients aged 18 to 65 with distressing delusions, Charité CBF Berlin. 80% male. 60% native German speakers. 70% highly educated.
- Funnel (Results, Sample characteristics): 38 screened, 13 included (34% uptake), 1 dropout before intervention (time), 1 after session two (symptom exacerbation, unrelated SAE), 1 withdrawn for smartphone literacy, 10 analysed. Retention 10 of 13 (77%).
- Protocol: 10-minute app training. 6 days x 10 surveys of 39 items. Then 5 coping reminders and an 8-item survey daily for 10 days after sessions two and three.
- Completion: EMA mean 59%. All 10 above the 33% floor. 10 of 10 used the app between sessions. EMI mean 72%.
- Session engagement 4.50 to 4.70 of 5. Protocol adherence 90% to 97% (Results), "over 85%" (Discussion).
- Technical failure modes: none reported. Participants named too much text, too many surveys, too much scrolling.
- Not reported: recruitment dates, BYOD vs provisioned, OS, completion distribution, reminder engagement figures.

---

## 3. O'Driscoll et al. 2025, JMIR Mental Health

- Source read: Europe PMC full-text XML (PMC12483342).
- First author: Ciarán O'Driscoll (first contributor in the author group). JMIR Ment Health 2025;12:e79296. DOI 10.2196/79296. PMCID PMC12483342.
- Deployed (Methods, Trial Design and EMA Protocol): "intervention delivery took place via the m-path app" and "All participants downloaded the m-path app." Matches the citation.
- Verdict: INCLUDE.
- Existing profile on this cohort: none. Same lead author and platform as paper 9, but a different sample.
- Profile written: `profiles/mpath-uk-mindfulness-mentalization-emi-pilot-rct.md`.

### Extraction

- Design: parallel-group pilot RCT, 1:1, automated EMI in both arms. Preregistered. Data and code on OSF.
- Funding/COI: funding not stated. None declared. Prize draw for all. £20 at 60% EMA (lowered from 80% before the trial).
- Population: UK adults, PHQ-9 above 9 or GAD-7 above 7, no therapy or medication. University online participant pool. Mean age 23.50 (range 18 to 61).
- Funnel (Results, Recruitment; Retention): 280 assessed, 99 eligible (35%), 84 randomised (30%), 5 of 42 and 4 of 42 disengaged, 75 completed (89.2%). Recruitment March to December 2024.
- Withdrawal reasons: technical difficulties 3, time 1, not given 3, one adverse reaction (body-image distress, mindfulness arm). Withdrawers younger by 3.78 years.
- Protocol: 4 fixed EMAs/day for 28 days, 2-hour window, 60-minute reminder. Email reminder when completion fell below 80%, at most weekly.
- Completion (Intervention Delivery and Adherence): mean 98.21 EMAs (SD 12.69), 87.69% (SD 11.33%), range 57% to 100%. EMI triggered 79.4% and 78.6%. EMI engagement 18.3% and 21.9%. Mean 15.60 EMI prompts completed (SD 22.74).
- Not reported: OS, share meeting the 80% adherence definition, details of the technical difficulties.

---

## 4. Elmer et al. 2025, JMIR Mental Health

- Source read: Europe PMC full-text XML (PMC12421209).
- First author: Timon Elmer (first `contrib-type="author"` record. The XML front matter also lists editors and reviewers, excluded). JMIR Ment Health 2025;12:e74103. DOI 10.2196/74103. PMCID PMC12421209.
- Deployed (Methods, Procedure): "installed the m-Path smartphone app for EMA surveys and JITAI delivery." Matches the citation.
- Verdict: INCLUDE.
- Existing profile on this cohort: none.
- Profile written: `profiles/mpath-depression-social-support-jitai-mrt.md`.

### Extraction

- Design: preregistered feasibility study with microrandomized trigger strategies.
- Funding/COI: SNSF PZ00P1_208742. None declared. CHF 160 to 250 scaled to completion. Participation-rate feedback on day 10.
- Population: Swiss adults seeking outpatient psychotherapy, BDI-II above 9. 22 women, 3 men. Mean age 35.12.
- Funnel (Results, Overview): 130 assessed, 36 eligible and scheduled, 1 no-show, 2 intake within 2 weeks, 1 suicidal thoughts, 2 night shifts, 3 dropouts (2 lost smartphones, 1 operation), 2 left by choice, 25 included.
- Protocol: 6 random EMAs/day 8 AM to 8 PM, evening survey, weekly survey, 21 days. JITAIs from day 4, capped at 2/day.
- Completion: 2689 EMA reports, mean 107.56 (SD 20.46) of 126. Compliance 85.37% (SD 16.24%). 20 of 25 at 70% or more. Careless 6 of 389 (1.5%). Weekly 75, all complete. Evening mean 9.28 (SD 4.98).
- JITAI: 377 triggered (221 fixed, 110 SPC, 46 support need). 76 suppressed by the cap (15 people, 55 days).
- Technical: functioning rated 6.36 of 7. Two lost phones.
- Not reported: OS, recruitment dates.

---

## 5. Kaufmann et al. 2025, Frontiers in Psychiatry

- Source read: Europe PMC full-text XML (PMC12241026).
- First author: Luisa Kaufmann. Front Psychiatry 2025;16:1470554. DOI 10.3389/fpsyt.2025.1470554. PMCID PMC12241026. DRKS00027536.
- Deployed (Methods, App-based support service): "Using an internet platform called m-Path developed by KU Leuven (Belgium) to conduct EMA and EMI using smartphones (32), the authors created an unguided support app." Matches the citation.
- Verdict: INCLUDE. Non-participation and dropout are the outcomes.
- Existing profile on this cohort: `profiles/mpath-psychiatric-outpatient-app-support.md` (Golsong 2024, the parent feasibility paper, written by a parallel batch today). Same 57 participants. INCLUDE kept because this paper adds operational content the parent does not carry as its outcome, namely the anonymous non-participation reasons (n=29), interview-based dropout reasons (n=17), self-deletion of data by 2 dropouts, and the early-reporting dropout signal. Completer counts differ (40 here by the weekly-use rule, 38 complete datasets in Golsong). Cross-linked.
- Profile written: `profiles/mpath-psychiatric-outpatient-nonparticipation-dropout.md`.

### Extraction

- Design: secondary analysis of a single-arm prospective feasibility study. Recruitment February 21 to March 14, 2022.
- Funding/COI: open-access fee support only. No commercial COI. No compensation described.
- Funnel: 88 approached in person, 31 declined (29 gave reasons), 57 consented (64.8%), 17 dropouts (29.8%), 40 completers (70.2%).
- Dropout definition: no app use for a full week, or self-reported withdrawal.
- Reasons tables (Tables 1 and 2) are transcribed in the profile.
- Completeness: 3 of 17 dropouts had no mood data (2 deleted their own data, 1 baseline only). 14 dropouts averaged 6.33 reporters/day, days 1 to 12. 38 of 40 completers had complete sets, averaging 34.08 reporters/day.
- Early signal: fewer mood reports in days 1 to 5 (U=48.00, p<.001, r=0.61) and days 1 to 7 (U=25.50, p<.001, r=0.67).
- Technical: 0 app problems at week-one call in either group. 1 non-participant installation error.
- Not reported: OS, completion percentages for EMA.

---

## 6. Harrison et al. 2023, Journal of Medical Internet Research

- Source read: Europe PMC full-text XML (PMC10540021).
- First author: Conrad Harrison. J Med Internet Res 2023;25:e47179. DOI 10.2196/47179. PMCID PMC10540021.
- Deployed (Methods): "The EMCAT progressive web app has been built using Concerto, an open-source CAT development platform maintained by the University of Cambridge Psychometrics Centre." m-Path appears only in the reference list. This differs from the citation tag.
- Verdict: REJECT, architecture. Instrument not profiled: EMCAT on Concerto. The paper introduces a platform and illustrates it with a 40-patient hand-surgery pilot (response rates by schedule, median 93% daily, 43% thrice daily).
- Expansion candidate: weak. Concerto is a computerized-adaptive-testing engine, not a phenotyping platform.

---

## 7. Dejonckheere et al. 2024, Computers in Human Behavior

- Source read: accepted author manuscript, KU Leuven Lirias (49 pages, "in press" cover). Version of record not read. No PMCID.
- First author: Egon Dejonckheere (byline). Comput Human Behav 2024;160:108360 (volume from Crossref). DOI 10.1016/j.chb.2024.108360.
- Deployed (Procedure): "participants downloaded our ESM app m-Path on their smartphone." Matches the citation.
- Verdict: INCLUDE. A real 10-day deployment with technical exclusions and compliance as the outcome. The cohort is the experiment, not an illustration.
- Existing profile on this cohort: none.
- Profile written: `profiles/mpath-gamified-esm-compliance-experiment.md`.

### Extraction

- Design: preregistered between-person experiment, 2:1 gamified vs control. July to October 2022.
- COI: ED, SV and MM co-founded m-Path. MP and GK are m-Path employees. Funding KU Leuven C14/19/054 and FWO fellowships.
- Funnel: 200 enrolled, 7 excluded (2 phone malfunction, 3 erroneous sampling schemes, 1 early termination, 1 unknown withdrawal), 193 analysed (128 gamified, 65 control).
- Payment: 1.5 course credits (n=108) or 15 EUR (n=85), not contingent on compliance.
- Protocol: 10 prompts/day, 9 AM to 7 PM, 10 days, 10-minute expiry.
- Compliance: 58.31% (SD 21.13%, range 1% to 96%). Modelled first vs last day 20% difference. Gamified vs control 1% difference. 45 gamified participants never used the store. Coin use effect p=.052 in outlier-free models.
- Reliability: gamified discrepancy 0.20 points larger. 0.72 for non-spenders, 0.51 control, 0.55 full spenders.
- Not reported: OS, recruitment channels in detail, cause of the sampling-scheme errors.

---

## 8. Ekelund et al. 2025, International Journal of Sport and Exercise Psychology

- Source read: published PDF via the Umeå DiVA repository (23 pages, CC BY-NC-ND, Taylor & Francis). No PMCID.
- First author: Rebecka Ekelund (byline). Published online 2025-09-30. DOI 10.1080/1612197X.2025.2563323.
- Deployed (Measures): "The premium version of the m-Path (Mestdagh et al., 2023) was used to digitally collect daily life momentary assessments." Matches the citation.
- Verdict: BORDERLINE-reject, no-cohort. This is a single-case design with three athletes (four recruited, one left treatment for scheduling). It does report 105 days at 6 prompts/day with per-person response rates of 48%, 73% and 77%, and phone calls at weeks 3 and 8 that coincided with compliance recovery. Those figures describe three individuals and cannot support a deployment-level claim.
- Existing profile on this cohort: none.

---

## 9. O'Driscoll et al. 2024, JMIR Formative Research

- Source read: Europe PMC full-text XML (PMC10993123).
- First author: Ciarán O'Driscoll. JMIR Form Res 2024;8:e49857. DOI 10.2196/49857. PMCID PMC10993123.
- Deployed (Methods, Study Design): "Questionnaires and strategy training were delivered via Qualtrics and EMA/EMI using the m-path platform [23]." Matches the citation.
- Verdict: BORDERLINE-include. The text reports retention (65 of 73) and EMA completion (mean 85 of 112, 76%), plus low-compliance exclusions. The screening-to-set-up funnel is only in Figure 2. The compliance figures do not fully reconcile.
- Existing profile on this cohort: none.
- Profile written: `profiles/mpath-goal-pursuit-emi-feasibility.md`.

### Extraction

- Design: three iterations, the third an uncontrolled pilot analysed as SCED.
- COI: none declared. Funding not stated. Prize draw plus £20 and a report at 70% EMA.
- Population: UK adults, nonclinical (PHQ-9 of 15 or below), Android or iOS phone, social media recruitment. Mostly female students.
- Pilot: 4 semi-random EMAs/day in a 12-hour window, 28 days. 7-day baseline, then triggered prompts.
- Completion: 112 sent. Mean 85 (SD 33), 76%. 10 (14%) excluded for low compliance. Abstract says compliance "high (n=63, 86%)". Mean 18 (SD 13) triggered prompts.
- Attrition before app set-up described as high, with no count in text.
- Not reported: recruitment dates, iteration 1 and 2 samples (Appendix 3, not retrieved), exclusion threshold, technical failures.

---

## 10. Oba et al. 2025 (single-case JITAI), JMIR Formative Research

- Source read: Europe PMC full-text XML (PMC12288703).
- First author: Takeyuki Oba. JMIR Form Res 2025;9:e69556. DOI 10.2196/69556. PMCID PMC12288703.
- Deployed (Methods): participants "received 3 signals each day at fixed times (11 AM, 4 PM, and 9 PM) on their smartphones with an EMA app, m-Path [27], being installed." Procedure says they "received study instructions and mobile devices (a smartphone and activity tracker)." The tracker brand is not named and its data are not used.
- Verdict: BORDERLINE-reject, no-cohort. AB single-case design with N=8. It reports no dropouts and per-phase compliance (75.6% baseline, 59.7% intervention, one participant at 3%), plus 7 of 8 rating cue timing inappropriate. The cohort is too small to stand as a deployment profile. Its compliance figures are worth a line in the sibling profile if wanted.
- Related: same AIST overarching project and ethics approval (ID 2022-1240) as paper 12.

---

## 11. Wong et al. 2025, JMIR Formative Research

- Source read: Europe PMC full-text XML (PMC12638038).
- First author: Stephanie Ming Yin Wong (first contributor in the author group). JMIR Form Res 2025;9:e77036. DOI 10.2196/77036. PMCID PMC12638038.
- Deployed: "We therefore developed the MHapp using m-Path (a spin-off from KU Leuven's Faculty of Psychology)." Matches the citation.
- Verdict: REJECT, architecture. App review plus co-design workshops with 8 peer supporters and 5 service users, and usability testing. No deployment cohort.
- Note: its review found m-Path to be the only no-code builder designed for mental health interventions, among 11 tools. That is a Module 2 m-Path profile fact, if wanted.

---

## 12. Oba et al. 2025 (physical-activity EMI RCT), JMIR Formative Research

- Source read: Europe PMC full-text XML (PMC12677381).
- First author: Takeyuki Oba. JMIR Form Res 2025;9:e79360. DOI 10.2196/79360. PMCID PMC12677381.
- Deployed (Methods, Interventions): "Each participant received a smartphone and a Fitbit device at the beginning of the study ... Each evening, the participants were asked to self-report their daily step count and motivation for PA on an EMA app (m-Path; KU-Leuven [34])." Fitbit Measures names "Sense or Sense 2." The citation tagged m-Path only. Fitbit was also deployed.
- Verdict: INCLUDE.
- Existing profile on this cohort: none.
- Profile written: `profiles/fitbit-mpath-japan-physical-activity-emi-pilot-rct.md`.

### Extraction

- Design: pilot RCT, 1:1 block randomisation, single-blind. November 2024 to March 2025.
- Funding/COI: JSPS KAKENHI 23H01051. None declared. JPY 15,000 to 20,000.
- Population: Tsukuba area adults aged 18 to 64, inactive, healthy, no medication. Mean age 45.40.
- Funnel: 232 assessed, 40 randomised, 40 analysed. Recruitment shared with a paired sibling trial.
- Deployment: provisioned phone and Fitbit Sense or Sense 2, 24-hour wear on the nondominant wrist. EMA at 8 AM, 12 PM, 5 PM plus an evening prompt.
- Compliance: 79.5% (SD 23.5%) daytime. 87.2% (SD 18.81%) evening. Valid HR 90.3% (SD 10) of duration.
- Adverse: 14 participants reported a light skin rash, likely from the Fitbit.
- Acceptability (EMI arm, n=20): timing appropriate 5 (25%). Willing to continue 11 (55%).
- Not reported: reasons for non-enrolment in text, any sync or device failure.

---

## 13. Weseman et al. 2026, Journal of Affective Disorders

- Source read: PMC author-manuscript XML (PMC13395528) via NCBI E-utilities. Europe PMC returned HTTP 500 on three attempts.
- First author: Weseman CE. J Affect Disord 2026;407:121783. DOI 10.1016/j.jad.2026.121783. PMCID PMC13395528.
- Deployed (EMA Protocol): "All participants downloaded the app m-Path (see m-path.io; Mestdagh et al., 2023) to receive the EMA surveys." Matches the citation.
- Verdict: INCLUDE.
- Existing profile on this cohort: none.
- Profile written: `profiles/mpath-aphasia-depressive-affect-ema.md`.

### Extraction

- Design: feasibility and psychometric study. November 2024 to May 2025. Northwestern IRB.
- Funding: NIDCD K23DC020757. COI statement not found in the manuscript text.
- Funnel: 70 contacted, 43 declined, 27 enrolled and completed.
- Protocol: 4 fixed surveys/day (9 AM, 1 PM, 5 PM, 9 PM), 14 days, 1-hour window, reminders at 30 and 50 minutes. Text, picture and audio per item. Care partners at training.
- Compliance: mean 50 of 56 (SD 5.20), 89.6%. Open 6 min 38 s. Complete 1 min 27 s. Not associated with severity, cognition or depression.
- Feedback: SUS 84.81 (SD 12.67). Four reported 9 PM timing problems.
- Not reported: reasons for declining, OS, technical failures.

---

## 14. Kiekens et al. 2024, JAMA Network Open

- Source read: Europe PMC full-text XML (PMC11581677).
- First author: Glenn Kiekens. JAMA Netw Open 2024;7(10):e2440510. DOI 10.1001/jamanetworkopen.2024.40510. PMCID PMC11581677.
- Deployed (Ecological Momentary Assessment): "Nonsuicidal self-injury cognitions and behavior were assessed during each EMA survey via the m-Path app." Matches the citation.
- Verdict: BORDERLINE-reject, duplicate-cohort. This is the same Flanders cohort as `profiles/mpath-nssi-ema-benefits-challenges.md` (Bonnier 2025). Both report 132 enrolled, 8 losses, 124 completing, ages 15 to 39, 28 days at 6 prompts a day, June 2021 to August 2023. Bonnier already flags Kiekens 2024 as the same cohort.
- It adds four operational figures not in the Bonnier profile. Recommend folding them into that profile centrally rather than writing a second profile.
  - Daily engagement rate 95.50% (at least one survey on 26.74 of 28 days) among the 124 completers.
  - Median adherence 78.6% (IQR 59.5% to 88.7%). Mean 121 (SD 34.5) surveys per patient. 15,123 surveys in a 125-patient analytic cohort (1 completer below 25 surveys dropped, 2 dropouts above 25 added back).
  - Median completion time 86 seconds (IQR 61 to 127). 25 surveys submitted after 45 minutes excluded, leaving 15,098 valid.
  - The in-app self-injury event marker was "available for 91.2% of participants." The paper does not say why it was unavailable for the rest.
