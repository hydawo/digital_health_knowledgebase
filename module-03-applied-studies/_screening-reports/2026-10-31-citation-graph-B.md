# Module 3 citation-graph screening, batch B, 10 papers, 2026-10-31

Screened against `_screening-and-profile-rules.md` Part A, CLAUDE.md "Module 3" and the README scope rules. Candidates came from the citation-graph pass in `_citation-graph-scan-2026-10.md`, where all ten were tagged RADAR-base. Full text was read for every paper. Sources were Europe PMC full-text XML where a PMCID existed, otherwise an open repository or preprint server. No PDF was stored in the repo. No identifier was sent to any lookup service. Two publisher routes hit bot checks (Springer link.springer.com for paper 9, the UZH ZORA repository for paper 5) and were not pursued. Open copies were found elsewhere for both. Cohort-overlap checks were done by grep of `profiles/*.md` for each DOI, first author, cohort name (RADAR-MDD, DMHS, RALD, ART, LEAP, AIMS-2-TRIALS) and the existing `radar-mdd-*.md` profiles.

| # | Paper | Verdict | Reason code | Device/platform actually deployed |
|---|---|---|---|---|
| 1 | Althobiani 2023, JMIR Form Res | INCLUDE | (deployment; retention, per-stream adherence, named technical failures) | RADAR-base active app + Garmin vivoactive 4 + NuvoAir spirometer + finger oximeter, provisioned |
| 2 | Denyer 2023, JMIR Form Res | REJECT | no-cohort | Fitbit Charge 3 + "Passive App" and "Active App" (platform not named in the paper) |
| 3 | Sun 2023, JMIR | BORDERLINE-reject | duplicate-cohort | RADAR-base + Fitbit Charge 2/3 (RADAR-MDD) |
| 4 | Cho 2024, JMIR Form Res | REJECT | no-cohort | Notion web page + KakaoTalk scheduled messages (instrument not profiled) |
| 5 | Eicher 2025, Sleep Medicine | REJECT | no-cohort | MHSL Sleepband v3 EEG headband (instrument not profiled); RADAR-base questionnaire app secondary |
| 6 | Douglas 2026, npj Digit Public Health | INCLUDE | (deployment; 12-month funnel, retention by subgroup, wear and survey adherence) | Apple Watch (provisioned) + participant iPhone + Apple Research app. Not RADAR-base. |
| 7 | Matcham 2022, J Affect Disord | BORDERLINE-include | (same cohort as RADAR-MDD profiles; adds new operational figures) | RADAR-base active app + Fitbit (RADAR-MDD) |
| 8 | White 2024, JMIR Mhealth Uhealth | INCLUDE | (deployment; RCT of engagement, technical exclusions, per-task completion) | RADAR-base Android app + Fitbit Charge |
| 9 | Haley 2025, J Technol Behav Sci | REJECT | no-cohort | None deployed in this study (interviews with RADAR-MDD alumni) |
| 10 | Yorke 2026, Research Square preprint | INCLUDE | (deployment; usable-data funnel, trait correlates of missingness, OS constraint) | RADAR-base pRMT (Android) and aRMT + Fitbit Inspire 2/3 |

Platform-tag accuracy for this batch. 6 of 10 actually deployed RADAR-base as the primary or co-primary instrument. Paper 5 used it only as a questionnaire app. Paper 2 does not name its platform. Paper 4 used none. Paper 6 used Apple's stack.

---

## 1. Althobiani et al. 2023, JMIR Formative Research

- Source read: Europe PMC full-text XML (PMC10709787), CC BY 4.0. XML only.
- First author: Malik A Althobiani (first author record in the XML; three editor records precede the author list). Not checked against a PDF byline. JMIR Form Res 2023;7:e51507. Epub 2023-11-24. DOI 10.2196/51507. PMID 37999935. PMCID PMC10709787 (from the XML).
- Deployed (Methods, Data Collection): "Third, data were collected from a number of devices: continuous passive monitoring using the Garmin vivoactive 4 and active monitoring outcomes using a daily finger pulse oximeter." And "Second, a multidimensional questionnaire and speech and vocalization sampling were administered using the RADAR-base active mobile phone app." Matches the tag. RADAR-base (Module 2) and Garmin (Module 1) are both profiled. NuvoAir spirometer is not profiled but is a secondary instrument.
- Verdict: INCLUDE. Feasibility is the primary aim. Reports a screening count, dropout with reasons for all five, data-based retention, per-stream adherence by burden tier, spirometry session counts and quality, and a named list of technical failure modes including Garmin background sync failures.
- Existing profile on this cohort: none.
- Profile written: `profiles/radar-base-garmin-respiratory-remote-monitoring.md`.

### Extraction

- Design: three-arm prospective observational cohort feasibility study (RALD). ISRCTN 16275601. HRA and HCRW ethics 21/WM/0087 (Methods, Ethics Approval).
- Funding/COI (Acknowledgments, Conflicts of Interest): NIHR Maudsley BRC (IS-BRC-1215-20018), HDR UK, IMI2 BigData@Heart (116074), NIHR UCLH BRC, UKRI London AI Centre, NIHR ARC South London, UCL IHI, King Abdul Aziz University via the Saudi Arabian Cultural Bureau. Wellcome (209553/Z/17/Z) funded JJ for unrelated research. No vendor funding or vendor author declared.
- Population/setting: Royal Free Hospital and University College Hospital, London. 20 COPD, 20 ILD, 20 post-COVID-19. Median age 64 (IQR given as 36-82 in text, 36-85 in Table 2). 25/60 (42%) women. 28/60 (47%) disability.
- Enrolled to analysed (Results, Patient Characteristics): 162 assessed, 60 recruited, 5 dropped out, 55 (92%) retained at 6 months. Survival analysis on 57: 31/57 (54%) full 180 days, 46/57 (81%) more than 150 days. The 57 denominator is not explained.
- Attrition reasons: 1 died in week 1, 1 felt unwell, 2 found the protocol too time-consuming, 1 privacy concerns.
- Duration: 180 days. Recruitment August 2021 to January 2022 (Methods) versus screening July 2021 to November 2022 (Results).
- Deployment model: provisioned kit (spirometer, Garmin, oximeter, "sometimes a smartphone"). Enrolment session, next-day call, first spirometry supervised by video. Daily data checks with reminder contact. Phone OS not reported.
- Retention device: "protocol holidays" offered to would-be dropouts. Median retention at 0.5 survival probability 179.9 days (no holiday) versus 165.1 (holiday). Number taking a holiday not reported.
- Completeness definitions (Methods, Analysis): questionnaire adherence as completed/expected. Garmin adherence over hourly windows, negative values as missing. Wear from heart rate presence.
- Wear (Results, Engagement): mean 18.66 h/day (SD 4.69), range of individual means 7.72 to 23.58. 123.91 h/week (SD 33.73). 463.82 h/month (SD 156.70). Expected maximum about 23 h because of charging.
- Garmin adherence: 70% to 90% for most data types (text summary of Figure 3). SpO2 lower from daytime motion artefact. ILD best, COVID lowest.
- Questionnaire adherence (Table 3, means): PHQ-8 84.7 COPD, 85.4 COVID, 92.3 ILD. Pulse oximetry entry 67.9, 64.1, 65.5. Audio tasks 64.8 to 81.2.
- Spirometry: 7200 requested, 4248 (59%) performed (Abstract). Weekly adherence ILD 94%, COPD 84%. 90.3% (3836/4248) acceptable ATS grade.
- Technical failure modes (Discussion, Missing Data, Technology, and Technical Issues; Table 4): recurrent Garmin background sync failures as the main cause of missing passive data; manual activation of continuous HR and SpO2 causing errors; app freezing, automatic log-out, test errors; phone-change compatibility; forgot to charge, lost charger, wrong plug type, deleted apps; skin irritation; watch lights disturbing sleep (38/57, 66%).
- Acceptability: 41/57 (72%) would wear day and night; 47/57 (82%) overnight; RADAR app efficient 42/57 (74%); would choose RADAR app 44/57 (77%); spirometry acceptable 36/40 (90%).
- Authors' conclusions: feasible and acceptable; passive collection outperformed active; recommend training, available technical support, flexible protocols, wireless oximeter.
- Not reported: compensation (though "not compensated" appears as a participant-given reason for missing data); phone OS; number given a study phone; number taking protocol holidays; exclusion reasons between 162 and 60; Figure 1 flowchart counts.

## 2. Denyer et al. 2023, JMIR Formative Research

- Source read: Europe PMC full-text XML (PMC10365629). XML only.
- First author: Hayley Denyer (XML). JMIR Form Res 2023;7:e44126. DOI 10.2196/44126. PMID 37389932. PMCID PMC10365629.
- Deployed (Methods): "The second session was administered once participants had received their wearable device (Fitbit Charge 3) and Android smartphone via post" and "The smartphone Passive App collected data on a range of measures, such as ambient noise, ambient light, phone use information". The paper never names RADAR-base. The "Passive App" and "Active App" naming matches RADAR-base but that is not stated. Fitbit is profiled.
- Verdict: REJECT, no-cohort. This is a qualitative interview study of 22 of the 40 ART pilot participants. It reports themes on charging, Fitbit sync and Passive App transfer problems, but no adherence, completeness or retention figures. The quantitative ART pilot paper, if published, would be the Module 3 candidate.
- Existing profile on this cohort: none.

## 3. Sun et al. 2023, Journal of Medical Internet Research

- Source read: Europe PMC full-text XML (PMC10463088). XML only.
- First author: Shaoxiong Sun (XML). J Med Internet Res 2023;25:e45233. DOI 10.2196/45233. PMID 37578823. PMCID PMC10463088.
- Deployed (Methods): "Wrist-worn devices, either Fitbit Charge 2 or Fitbit Charge 3, were given to participants" and "The data collection and management were handled by the open-source mHealth platform Remote Assessment of Disease and Relapse-base (RADAR-base)". Matches the tag.
- Verdict: BORDERLINE-reject, duplicate-cohort. It is a feature-extraction and statistics paper on 479 of the 623 RADAR-MDD participants (pre-COVID enrolment), already covered by `radar-mdd-recruitment-retention.md` and `radar-mdd-longterm-engagement.md`. Its only new operational content is median per-stream availability within 14-day PHQ-8 windows (GPS 13 of 14 days, IQR 1-14; Fitbit steps 14, IQR 0-14; phone interaction 13, IQR 0-14; Fitbit sleep 11, IQR 3-13) and the finding that at least 8 of 14 days are needed for an ICC of 0.9 on most features.
- Suggested central edit: one line in `radar-mdd-recruitment-retention.md` citing the 8-of-14-day reliability threshold and the per-stream window medians.

## 4. Cho et al. 2024, JMIR Formative Research

- Source read: Europe PMC full-text XML (PMC11544340). XML only.
- First author: Minji Cho (XML). JMIR Form Res 2024;8:e59623. DOI 10.2196/59623. PMID 39446465. PMCID PMC11544340.
- Deployed (Methods, proof-of-concept): "We chose the Notion website, as it can feature a planner-like layout" and "This functionality was achieved using the reserved message feature of KakaoTalk". No RADAR-base, no wearable, no passive sensing. The tag is wrong.
- Verdict: REJECT, no-cohort. Instrument not profiled: Notion and KakaoTalk used to simulate a design concept. A 2-week, n=16 simulation of an adolescent EMA system, with a formative n=34 paper-diary phase. Not a Module 1/2 expansion candidate, since neither tool is a research platform.

## 5. Eicher et al. 2025, Sleep Medicine

- Source read: bioRxiv preprint v1 JATS XML (10.1101/2025.03.21.644521, CC BY-NC-ND), via the bioRxiv API. The Sleep Medicine version of record (CC BY) was not read. The ZORA repository copy was behind a bot check and was not pursued. bioRxiv's HTML page returned a rate-limit block.
- First author: Corinne Eicher (bioRxiv metadata and CRediT statement). Sleep Med 2025;136:106830. DOI 10.1016/j.sleep.2025.106830. PMID 41033050. PMCID not in Europe PMC.
- Deployed (Methods): "During the intervention weeks, sleep was recorded using the MHSL-SB" and "participants completed the Karolinska Sleepiness Scale ... via a smartphone questionnaire application based on the RADAR-Base platform". The primary instrument is the MHSL Sleepband v3 frontal EEG headband with closed-loop auditory stimulation. RADAR-base only delivered the KSS and device checklists.
- Verdict: REJECT, no-cohort. Instrument not profiled: MHSL Sleepband v3 (ETH Zurich / Tosoo AG). N=5 healthy adults over 14 nights each. The deployment content concerns the headband (67 of 70 recordings available, 58 analysable after 3 parameter-setting losses, 4 sudden terminations and 2 with over 20% signal loss). No RADAR-base completeness figure is reported.
- Expansion candidate: MHSL Sleepband / Tosoo AG as a research EEG headband. Weak, given N=5. Relevant to open question 109 (Dreem EEG headband in RADAR-AD).
- COI: two authors are co-founder/shareholder and board president of Tosoo AG.

## 6. Douglas et al. 2026, npj Digital Public Health

- Source read: Europe PMC full-text XML (PMC13437235). XML only. Supplementary material not retrieved.
- First author: Christopher S Douglas (XML; first of seven equal contributors). npj Digit Public Health 2026;1:27. Published 2026-08-04. DOI 10.1038/s44482-026-00029-3. PMID 42558176. PMCID PMC13437235.
- Deployed (Methods): "we mailed all enrolled participants a study kit prior to their intake assessment, containing an Apple Watch, a participant instructions packet, and - for those without a compatible device - a loaner iPhone" and "enrollment in the Apple Research app, which managed the collection of sensor data, device data, and surveys". Apple Watch (`apple-watch-healthkit.md`) is profiled. The RADAR-base tag is wrong; RADAR-MDD appears only as a cited comparator.
- Verdict: INCLUDE. Reports a full screening-to-completion funnel, retention by age, ethnicity, education and severity, median time to dropout, milestone-linked dropout, completer adherence for PHQ-8, daily survey and watch wear, the wear definition, the monitoring and compensation model, and pilot funnels.
- Existing profile on this cohort: none. `aware-stand-mood-prediction-adherence.md` is a different UCLA cohort from the same group.
- Profile written: `profiles/apple-watch-dmhs-depression-anxiety-retention.md`.

### Extraction

- Design: prospective 12-month cohort, stratified recruitment. UCLA IRB #21-001558 (pilots #20-000995, #20-002337).
- Funding/COI: Apple Inc. and UCLA. NIH UL1TR001881 for REDCap. Four authors Apple employees with stock, one Apple intern.
- Funnel (Results): 17,150 screened (January 2022 to January 2023), 5,684 consented, 4,542 intake, 3,333 completed. 3 deletions, so 4,539 and 3,332. Retention 73.4%. 1,207 dropouts, median 241 days.
- Completion by subgroup (Table 1): age 65.3% / 75.6% / 83.6% / 90.2%; severity 79.9% healthy to 61.6% severe; PHQ-8 under 10 77.7% versus 10 or more 68.5%; White Hispanic 69.7%, Black 70.8%, Asian 75.6%, White non-Hispanic 75.8%. Sex not significant (p=0.479). Employment not significant (77.0% versus 80.7%).
- Dropout timing: rises near month 4 (first mandatory check-in, weeks 10 to 13, end of first compensation quarter), second check-in (weeks 46 to 49) and before exit.
- Adherence among completers: PHQ-8 90.5%; Daily Reflection 86.9% week 1 to 67.2% week 52; weekday 67.1% versus weekend 64.2%; watch wear 21.0 h (SD 2.2); 87.4% of weeks at target; 67.5% at target on 90% of weeks.
- Wear definition (Methods): hour compliant if StandHour field holds 0 or 1. Target 20 hours on at least 4 days a week.
- Deployment model: provisioned Apple Watch, own iPhone (70 loaners, about 2%), own data plan. Remote intake with iOS version check and Research app enrolment.
- Support model: automated daily compliance flags, staff outreach, in-app completion tracking, quarterly progress emails, 10-minute staff conversations at assessments.
- Compensation: tiered quarterly (Base, Silver, Gold), up to US$1,070 a year, watch kept on meeting a minimum threshold.
- Pilots: P1 1,744 screened, 184 enrolled, 164 first session, 159 final, 96% retention, 86% joint daily survey and wear compliance. P2 782 screened, 166 enrolled, 130 first, 121 final; two-watch rotation judged too complex.
- Technical failure modes: none itemised.
- Not reported: adherence among dropouts; reasons for dropout; device loss or failure; iOS-version effects; Supplementary Table 7 missing-data criteria (not retrieved).

## 7. Matcham et al. 2022, Journal of Affective Disorders

- Source read: author accepted manuscript PDF from figshare (article 24118110, CC BY). The ScienceDirect version of record was not read. A PsyArXiv preprint (osf.io/t2k5d) was downloaded but the accepted manuscript was used.
- First authors: Faith Matcham and Ewan Carr, joint (manuscript byline, asterisked). J Affect Disord 2022;310:106-115. DOI 10.1016/j.jad.2022.05.005. PMID 35525507. PMCID none in Europe PMC.
- Deployed (Methods, Usage): "engagement with the RADAR-base active remote measurement (aRMT) app ... was assessed based on the number of PHQ-8 questionnaires completed" and Fitbit wear "measured based on the availability of heart rate data for each 15-minute period of each day." Matches the tag.
- Verdict: BORDERLINE-include. Same RADAR-MDD cohort as `radar-mdd-recruitment-retention.md` and `radar-mdd-longterm-engagement.md`. It adds Fitbit wear and PHQ-8 completion at two fixed three-month windows, PSSUQ and TAM-FF usability scores, the finding that neither symptom severity nor usability predicts use to a practical degree, and a Google Analytics notification-count discrepancy. None of these is in the existing profiles. The case against is that it is a third profile on one cohort.
- Profile written: `profiles/radar-mdd-usability-predictors-engagement.md`.

### Extraction

- Analysed: 547 of 623 (87.8%) after excluding 7 (no clinical), 65 (no usability), 4 (no covariates). 535 at 12 months.
- Usage (Table 1): Fitbit wear median 0.90 (IQR 0.56-0.97) months 3-6, 0.74 (0.17-0.94) months 12-15. Zero PHQ-8 in window 86 (16%) and 100 (23%). Pooled zero wear 202/1082 (19%); zero PHQ-8 186/975 (19%).
- Usability: PSSUQ reversed 94 (75-106) and 93 (73-107). TAM-FF reversed 86 (71-101) and 87 (68-103).
- Effects (Table 3): TAM-FF ease of use +0.33 PHQ-8 and +0.02 wear per SD; GAD-7 -0.13 PHQ-8; WSAS -0.03 wear. Depression severity null.
- Compensation (Discussion): paid for enrolment, interviews and 3-monthly outcome data; not for app tasks or Fitbit wear.
- Technical: Google Analytics showed more questionnaires completed than notifications received; authors abandoned the analytics.
- Inconsistency: PHQ-8 count described as 0-9 in Methods, tabulated 0-6.
- Not reported in the accepted manuscript: funding and competing-interests sections. Industry ties (Lundbeck, Janssen) from affiliations only.

## 8. White et al. 2024, JMIR mHealth and uHealth

- Source read: Europe PMC full-text XML (PMC10837755), CC BY 4.0. XML only.
- First author: Katie M White (XML). JMIR Mhealth Uhealth 2024;12:e44214. Epub 2024-01-19. DOI 10.2196/44214. PMID 38241070. PMCID PMC10837755. The batch file gives the year as 2023.
- Deployed (Methods): "Both the control and intervention arms were delivered via the RADAR-base system using a smartphone app and a wearable Fitbit Charge (Fitbit Inc) device." Matches the tag.
- Verdict: INCLUDE. Engagement is the primary outcome of an RCT. Reports a recruitment funnel, follow-up, withdrawal with reason, itemised technical exclusions, per-task completion, wear days, notification analytics and complier figures.
- Existing profile on this cohort: none. Participants are former RADAR-MDD London participants, but this is a new 2021 deployment with its own protocol, so the duplicate-cohort rule does not apply. Overlap noted in the profile.
- Profile written: `profiles/radar-base-fitbit-mdd-inapp-engagement-rct.md`.

### Extraction

- Design: single-centre two-arm participant-blinded RCT. NCT04972474. KCL ethics RESCM-20/21-21083.
- Funding/COI: NIHR Maudsley BRC; RADAR-CNS IMI2 115902. MH leads RADAR-CNS (Janssen, UCB, MSD, Biogen, Lundbeck funding).
- Funnel: 347 contacted, 114 (32.9%) agreed, 100 (28.8%) enrolled, 1 withdrew (technical issues), 87 completed follow-up. Power target 132 not met.
- Technical exclusions: 2 could not use app or Fitbit after enrolment, 1 got no notifications, 4 could not sync Fitbit, 1 opted out of Fitbit. 97 any app data, 93 any Fitbit data.
- Completion: PHQ-8 median 9 of 12 (IQR 6-10), RSES 9 (6-10), speech 8 (6-9). Fitbit mean 74 of 84 days (SD 19.7). PHQ-8 control 69%, intervention 68%, P=.83. Combined adherence 32/48 (67%) versus 35/44 (80%), P=.98 as printed.
- Process (Table 6): notifications received mean 22.0 versus 22.6; opened 34.3% versus 39.9%. 29/48 viewed progress report; viewers 75.3% versus non-viewers 57.0% PHQ-8 completion.
- Inconsistency: text 35/58 versus Table 6 29/48 for repeat progress-report viewing.
- Not reported: compensation; Fitbit Charge model generation.

## 9. Haley et al. 2025, Journal of Technology in Behavioral Science

- Source read: published PDF from figshare (file 56068649, CC BY). Springer's own PDF link returned a bot challenge and was not pursued.
- First author: Fintan Haley (PDF byline). J Technol Behav Sci 2025. DOI 10.1007/s41347-025-00530-1. PMCID not in PDF.
- Deployed: none in this study. Methods: "The research was conducted through interviews with participants in the RADAR-MDD study". 15 RADAR-MDD alumni interviewed for about 30 minutes about hypothetical machine-learning early-warning systems. £30 voucher.
- Verdict: REJECT, no-cohort. Qualitative acceptability of a hypothetical system. No deployment metrics.

## 10. Yorke et al. 2026, Research Square preprint

- Source read: Research Square PDF v1 (CC BY 4.0). Not peer reviewed. Supplementary tables not retrieved.
- First author: Isabel Yorke (PDF byline). Posted 2026-04-19. DOI 10.21203/rs.3.rs-9381221/v1. No PMID or PMCID.
- Deployed (Methods, Overview): "The MMM involved participants wearing a Fitbit Inspire 2 or 3 wristband throughout the 28-day collection period" and "participants installed two data-collection smartphone apps supported by the RADAR-base platform". Matches the tag.
- Verdict: INCLUDE. Feasibility is the first aim. Reports enrolment and withdrawal, per-modality availability, usable-day totals, zero-usable-day counts with their wear profiles, trait correlates of availability, OS split and the iOS incompatibility of the passive app.
- Existing profile on this cohort: none (grep for LEAP, AIMS-2, autism).
- Profile written: `profiles/radar-base-fitbit-autism-sleep-feasibility.md`.

### Extraction

- Design: observational feasibility within the AIMS-2-TRIALS Mobile Measures Month.
- Funding/COI: IMI2 777394 (AIMS-2-TRIALS) with EFPIA, Autism Speaks, Autistica, SFARI; RADAR-base IMI2 115902; NIHR Maudsley BRC; Wellcome 308830/Z/23/Z and 316664/Z/24/Z. One author holds Google shares; two direct Onsentia Ltd; one also CogStack Ltd.
- Funnel: 34 autistic and 40 nonautistic enrolled; 1 nonautistic withdrew over pRMT app concerns; 73 analysed. Source pools: LEAP-3 UK sites 127 autistic and 51 nonautistic; KCL volunteers 26. Approach and refusal counts not in text.
- Availability (Table 1 medians): Fitbit wear 82.5% versus 78.9%; night wear 75.8% versus 77.9%; PSP days 75% versus 85.7%; sleep rating 92.9% versus 85.7%; pRMT 78.6% versus 85.7%; usable days 41.0% versus 71.4%. No group difference significant.
- Usable participant-days: 447/952 (47%) autistic, 645/1092 (59.1%) nonautistic. Zero usable days: 10 autistic (29.4%), 5 nonautistic (printed 12.5%).
- Correlates (Table 2): tactile sensitivity with PSP availability ρ=.44 (p=.03) and usable days ρ=.42 (p=.04), autistic only; age with ratings ρ=.27; IQ with PSP ρ=.31; SRS-2 with pRMT ρ=.31.
- OS: 91.2% / 87.2% Android. iOS incompatible with pRMT; 8 iOS users excluded from passive analyses.
- Wear algorithm: HR gaps over 120 s or rolling variance under 1 over 20 samples as non-wear; night 21:00-09:00.
- Not reported: compensation; sync or battery failures; approach and refusal counts.

---

## Expansion candidates and open-question notes

- MHSL Sleepband v3 (ETH Zurich, commercialised via Tosoo AG), research EEG headband with closed-loop auditory stimulation. Weak candidate. Belongs with open question 109 (Dreem headband).
- Open question 103 (RADAR-base iOS sensor list). Yorke 2026 states that in a 2022 to 2024 deployment "iOS devices were incompatible with the passive sensing platform," while iOS users could use the aRMT active app. Althobiani 2023 and White 2024 did not report OS or were Android-only by design.
- Garmin profile. Althobiani 2023 documents recurrent vivoactive 4 background sync failures and manual activation of continuous HR and SpO2 as the main sources of missing passive data in a 6-month clinical deployment.
- Fitbit profile. White 2024 lost 4 of 100 participants' Fitbit stream to phone-sync failure at setup.
- RADAR-MDD analytics. Matcham 2022 (JAD) reports Google Analytics notification counts lower than questionnaire completions, which led the team to drop analytics as an engagement measure.
