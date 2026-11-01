# Module 3 citation-graph screening, batch C, 11 papers, 2026-10-31

Screened against `_screening-and-profile-rules.md` Part A, CLAUDE.md "Module 3" and the README scope rules. Candidates came from the citation-graph pass in `_citation-graph-scan-2026-10.md`. Full text was read for 10 of 11 papers. Sources were the Europe PMC full-text XML (7 papers), the publisher PDF (Cureus, Exploration of Digital Health Technologies) and the medRxiv JATS XML (1 preprint). No PDF was stored in the repo. No email or personal identifier was sent to any service. Multimedia appendices and supplements were not retrieved for any paper.

Cohort-overlap check was by grep of `profiles/*.md`, `literature-index.json`, `_scan-queue.md` and `_screening-reports/*.md` for each DOI, first author, cohort name and IRB number. No existing Module 3 profile covers any cohort in this batch. Papers 1 and 7 below (Hackett 2024, Calvert 2025) are the same Temple University cohort and are written up as one profile.

No paper in this batch turned out to be a Beiwe deployment. The three papers the citation graph tagged as Beiwe used Feels.ai, a Hexoskin shirt with the Huixin EMAI app, and the ALLFTD Mobile App by Datacubed Health. The fourth Beiwe-tagged paper was unobtainable. So this batch adds nothing to Q106 or Q115.

| # | Paper | Verdict | Reason code | Device/platform actually deployed |
|---|---|---|---|---|
| 1 | Hackett 2024, JMIR Hum Factors | INCLUDE | (deployment; retention, GPS missingness by OS, troubleshooting log, battery) | mindLAMP, BYOD, self-hosted LAMP server |
| 2 | Chin Fatt 2026, Digital Health | REJECT | architecture | UTSW "mHealth" custom Xamarin app (not profiled) |
| 3 | Pyke 2026, J Child Adolesc Subst Use | UNOBTAINABLE | unobtainable | Not verified. Abstract names Fitbit plus a recovery app |
| 4 | Macrynikola 2025, JMIR Ment Health | INCLUDE | (deployment; recruitment funnel, retention, app adherence, access hurdles) | mindLAMP, BYOD, in a clinical service |
| 5 | Akpalu 2026, Cureus | REJECT | architecture | Feels.ai mood app (not profiled) |
| 6 | Dwyer 2024, JMIR Form Res | BORDERLINE-include | (deployment; unpaid remote attrition with reasons) | mindLAMP, BYOD, data collection only |
| 7 | Calvert 2025, Int Psychogeriatr | INCLUDE (merged into paper 1's profile) | (same cohort as 1; adds survey adherence and training time) | mindLAMP, BYOD |
| 8 | Green 2023, JMIR Form Res | REJECT | no-cohort | mindLAMP |
| 9 | Li 2024, Explor Digit Health Technol | BORDERLINE-reject | no-cohort | SMART, an iOS cognitive-training app "modified based on" LAMP |
| 10 | Zhao 2026, JMIR Form Res | REJECT | validation | Hexoskin smart shirt plus Huixin EMAI app (neither profiled) |
| 11 | Paolillo 2026, medRxiv | REJECT | validation | ALLFTD Mobile App by Datacubed Health (not profiled) |

---

## 1. Hackett et al. 2024, JMIR Human Factors

- Source read: Europe PMC full-text XML (PMC11624463), CC BY 4.0. XML only.
- First author: Katherine Hackett (Europe PMC author string and XML). Not checked against a PDF byline. Year 2024. *JMIR Human Factors* 2024;11:e59974. Published 2024-11-22. DOI 10.2196/59974. PMID 39576984. PMCID PMC11624463.
- Deployed (Methods, Privacy and Security Safeguards): "The LAMP platform was used for the collection of digital phenotyping (GPS) data via the mindLAMP smartphone app, which is available for free on the Apple App Store and Google Play Store." Backend: "Data collection and storage were supported by a self-deployed version of the open-source LAMP Platform." Matches the citation tag.
- Verdict: INCLUDE. Feasibility and acceptability are primary aim 1. The paper reports retention, a troubleshooting log with named causes, mean daily GPS missingness and its OS and race associations, and participant-reported battery and phone-use changes.
- Existing profile on this cohort: none.
- Profile written: `profiles/mindlamp-older-adults-gps-cognition-feasibility.md` (covers papers 1 and 7).

### Extraction

- Design: single-arm feasibility, acceptability and preliminary validity study (Abstract; Methods). Temple University IRB protocol 27013 (Ethical Considerations).
- Funding/COI: NIA F31AG069444, T32AG066598 (Hackett), R01AG062503, R21AG066771 (Giovannetti), R01MH116884 (Barnett) (Acknowledgments). "Conflicts of Interest: None declared."
- Compensation: US$50 paid upfront at session 1 (Study Timeline; Ethical Considerations).
- Population/setting: Philadelphia region, specialty dementia clinics and community. Aged 63 to 85. 31 healthy cognition, 5 MCI, 1 mild dementia (Abstract). Validation subset n=34, mean age 71.6 (SD 5.5), 68% female, 56% White, 35% Black, 76% iPhone (Participant Characteristics).
- Enrolled to analysed: 37 enrolled, 37 completed and in feasibility analysis. 34 in validity analysis after 3 were excluded for major health events (eye surgery; fall with loss of consciousness; fall with head trauma and COVID-19). Screening and refusal counts not reported.
- Duration: about 4 weeks between two visits. Participation April 2022 to January 2024 (Participant Characteristics). Recruitment began January 2022 (Recruitment). Monitoring was extended for unanticipated travel and travel days removed (Preliminary Processing).
- Deployment model: BYOD, iOS or Android, at least 1 year of prior smartphone use, home Wi-Fi required. In-person setup with study-generated 10-digit login. App deleted at session 2.
- Custom integration: self-hosted LAMP on a purchased 1-TB Temple cloud server, CouchDB storage, Temple IT monitoring and backup (Backend Technical Implementation). Custom cron job emailing the team when a participant had more than 3 days of missing sensor data.
- Sampling: GPS "at a maximum frequency of 1 Hz" (Digital Phenotyping). Features via the Barnett and Onnela R script with multiple imputation.
- Recruitment method: clinics, prior lab participants, community outreach events, educational talks.
- Retention: 100% (37/37) completed the 4-week period and session 2 "without requesting to withdraw" (Feasibility and Acceptability).
- Data completeness: mean 423 (SD 352) minutes of missing GPS per day, "approximately 29% of the day" (Preliminary Analyses). iPhone users had less missing GPS (r=-0.64, P<.0038). Black participants had more missing GPS than White (P=.003) and Asian (P=.02). Black participants were more often Android owners (chi-square 6.9, P=.03, N=33). iPhone ownership correlated with income (r=0.49).
- Technical failure modes: 6 troubleshooting incidents affecting 5 participants (14%). Causes were Android safe mode, location permission reset to "only while using app", outdated mindLAMP version, low-battery mode, and accidental app deletion. All resolved remotely by phone.
- Participant-reported: 92% (34/37) no new phone problems. 41% (15/37) charged more. 46% (17/37) reported major changes in phone use. 97% (36/37) no discomfort or paranoia. Consent quiz mean 97% (SD 5.7%).
- Authors' conclusions: mobility phenotypes "are feasibly captured from older adults' personal smartphones". Recommendations: test lower GPS sampling to reduce battery drain, consider portable batteries, revise consent materials with diverse co-design, keep automated missing-data checks.
- Not reported: screening or refusal counts; accelerometer or other-sensor completeness; number of cron alerts; server cost; per-OS missing minutes as raw numbers in the main text (Multimedia Appendix 2 not retrieved).

## 2. Chin Fatt et al. 2026, Digital Health

- Source read: Europe PMC full-text XML (PMC13247369), CC BY-NC 4.0.
- First author: Cherise R Chin Fatt. *Digital Health* 2026;12:20552076261458952. DOI 10.1177/20552076261458952. PMID 42272706. PMCID PMC13247369.
- Deployed (Methods): "We built the mHealth application using Xamarin, an open-source framework." The app was built at UT Southwestern for the T-RAD study. The citation graph tagged mindLAMP. mindLAMP does not appear in the full text.
- Verdict: REJECT, architecture. Instrument not profiled: UTSW "mHealth" custom Xamarin app. The paper is mainly a design and development description with one pilot (113 of 199 consenting, 110 iOS, 3 Android; "90% engagement" in the first three months among participants invited for prior high engagement). It is a weak Module 2 expansion candidate because it is a single-institution app still in pilot.
- Existing profile on this cohort: none.

## 3. Pyke et al. 2026, Journal of Child & Adolescent Substance Use

- Source attempted: not in Europe PMC or PMC (PMC ID converter "Identifier not found in PMC"). OpenAlex lists only the Taylor & Francis PDF. The T&F landing page and PDF URL both returned HTTP 403 with a Cloudflare "Just a moment" bot check. Not bypassed.
- First author per OpenAlex: Nicole M Pyke. 2026-09-01. DOI 10.1080/29973368.2026.2723021. PMCID none.
- Deployed: not verified. The abstract describes students using "Fitbit devices" and "a wearable recovery-focused health app". The citation graph tagged Beiwe. Fitbit is profiled in Module 1 (`fitbit-google.md`), so the paper could qualify if the full text supports it.
- Verdict: UNOBTAINABLE (bot check). Add to `shared/manual-sweep.md` for a by-hand fetch.

## 4. Macrynikola et al. 2025, JMIR Mental Health

- Source read: Europe PMC full-text XML (PMC11822323), CC BY 4.0.
- First author: Natalia Macrynikola (XML contrib list). Not checked against a PDF byline. *JMIR Mental Health* 2025;12:e65222. Published 2025-01-29. DOI 10.2196/65222. PMID 39879612. PMCID PMC11822323.
- Deployed (Methods, Intervention Procedures): treatment "involved weekly therapy sessions with a trained clinician, weekly check-ins with a digital navigator, and regular use of the mental health app mindLAMP." Sensors: "The sensors used in the Digital Clinic are accelerometer, ambient light, nearby devices (detected through proximity to Bluetooth), and screen state." Matches the tag.
- Verdict: INCLUDE. Recruitment funnel with denominators, retention against benchmarks, app adherence, questionnaire completion at three time points and named access hurdles.
- Existing profile on this cohort: none.
- Profile written: `profiles/mindlamp-digital-clinic-blended-care-open-trial.md`.

### Extraction

- Design: nonrandomized single-arm open trial, approved as quality improvement (BIDMC #2022D000016).
- Funding/COI: no funding statement found. Torous is editor-in-chief of *JMIR Mental Health* and recused himself. No compensation. Treatment free.
- Population/setting: PCP referrals at BIDMC and BID-Needham, Massachusetts. Completers mean age 41 (SD 14), 63.3% cisgender women, 70.2% White. English only.
- Funnel: 401 approached, 329 attended introductory meeting, 289 enrolled (72.1% of approached; 87.8% of attendees). 31 still in treatment excluded, leaving 258. 215 completed (83.3%).
- Duration: 8 weeks. Recruitment began August 2022. End of data collection not reported.
- Deployment model: BYOD, Android or Apple. OS split not reported.
- Support model: 16 non-clinician digital navigators, 10 hours of training each plus 2 supervised appointments. 10 clinicians, mostly trainees, about 8 hours of training.
- App adherence: 73.5% (158/215) used the app on at least half of their days (benchmark 70%).
- Questionnaires: 100% baseline, 83.3% (179/215) end of treatment, 39.1% (84/215) 3-month follow-up. 41.7% (68/163) among those with clinical baseline scores. For 36 missing end-of-treatment questionnaires, in-app PHQ-9 and GAD-7 within 10 days of the last session were used for 27.
- Hurdles (n=179): 72.1% none; 11.2% (20) difficulty using mindLAMP; 10.6% (19) no quiet place; 3.4% (6) unstable Wi-Fi; 2.2% (4) remembering home practice. Lessons Learned gives mindLAMP difficulty as 3.4% (6/179), conflicting with Results.
- Satisfaction: clinician 4.81, navigator 4.61, mindLAMP user experience 4.18 (5-point).
- Technical failure modes: none reported beyond the hurdle question.
- Authors' conclusions: "feasible, acceptable, and potentially efficacious"; proceed to RCT. Recommendations: paid or pre-scheduled 3-month follow-up, resolve privacy-for-sessions barriers at intake, partner with primary care.
- Not reported: passive sensor completeness; OS split; reasons for the 43 non-completers; data-collection end date.

## 5. Akpalu 2026, Cureus

- Source read: publisher PDF (Cureus, CC BY 4.0). The Cureus article page returned a Cloudflare bot check, but the direct PDF URL listed in OpenAlex returned the PDF without one.
- First author: Peter Akpalu (sole author, PDF byline). *Cureus* 2026, published 2026-09-30. DOI 10.7759/cureus.117257. PMCID not in PDF (not in Europe PMC).
- Deployed (Methods, About Feels.ai app): "Feels.ai is a mobile mood-tracking application designed for brief, low-burden emotional check-ins". The citation graph tagged Beiwe. Beiwe does not appear in the full text.
- Verdict: REJECT, architecture. Instrument not profiled: Feels.ai. Retrospective analysis of 61 voluntary app users with a classifier. The author declares ownership of Feels.ai and is its developer. Not a useful expansion candidate (single-developer consumer app with no research deployment base).

## 6. Dwyer et al. 2024, JMIR Formative Research

- Source read: Europe PMC full-text XML (PMC11615540), CC BY 4.0.
- First author: Bridget Dwyer. *JMIR Formative Research* 2024;8:e62725. Published 2024-11-19. DOI 10.2196/62725. PMID 39560976. PMCID PMC11615540.
- Deployed (Materials): "The first app that every participant used was mindLAMP ... In this study, mindLAMP served solely as a digital phenotyping data collection tool." Matches the tag.
- Verdict: BORDERLINE-include. The deployment content is attrition with reasons in an unpaid, fully remote mindLAMP protocol, including dropouts for "data quality reasons". It has no passive completeness or survey adherence figures, so it is thinner than the other includes.
- Existing profile on this cohort: none. Checked against `mindlamp-linc-passive-data-quality.md` (different cohort, 18 to 24 year olds, 2024 to 2025).
- Profile written: `profiles/mindlamp-unpaid-app-recommendation-engagement.md`.

### Extraction

- Design: two-arm pilot with random assignment after a 1-week observation phase. BIDMC IRB 2022P001143.
- Funding/COI: no funding statement found. "JT is the Editor-in-Chief for JMIR Mental Health." No compensation.
- Population: ResearchMatch, US adults, GAD-7 above 5. Remaining 47 mean age 43.0 (SD 16), 79% female, 89% White.
- Funnel: 82 enrolled. 22 left after meeting 1 (9 unknown, 6 lost interest, 3 time commitment, 3 data quality, 1 family emergency). 13 left after meeting 2 (2 data quality, 11 unknown). 47 remained. Abstract gives 17 (21%) and 18 (22%) by arm.
- Duration: 5 weeks. Calendar dates not reported.
- Deployment model: BYOD, Apple or Android. OS split not reported. Intervention app screen time collected by participant screenshot.
- Data completeness: not reported for any mindLAMP stream. "Data quality" not defined. Limitations adds that some who finished were also excluded for data quality.
- Authors' conclusions: recommendation "is feasible and may increase engagement"; attrition attributed to no compensation and remote format.
- Not reported: OS split; passive coverage; daily survey response rate; enrolment dates.

## 7. Calvert et al. 2025, International Psychogeriatrics

- Source read: Europe PMC full-text XML (PMC13142898), CC BY 4.0.
- First author: Elombe Calvert. *International Psychogeriatrics* 2026;38(2):100123 (issue March 2026; online 2025-09-08). DOI 10.1016/j.inpsyc.2025.100123. PMID 40925804. PMCID PMC13142898.
- Deployed: mindLAMP, same Temple cohort as paper 1. "This study represents a post-hoc analysis of data from a pilot project conducted at Temple University".
- Verdict: INCLUDE, merged into paper 1's profile rather than profiled separately. It is the same deployment, but it adds operational figures paper 1 lacks. These are nightly survey completion of 80% (SD 20%), training duration of 20.2 minutes (SD 6.5), and 1.0 mock-survey attempt (SD 0.2).
- Other figures: 27 iPhone, 10 Android (Table 1). Composite usability 19.4 (SD 4.5) of 25. No usability differences by phone type. Funding NIA. Authors declare no conflicts.
- Discrepancy with paper 1: cognitive classification is 30 healthy, 5 MCI, 1 "impaired, not MCI", 1 mild dementia, against paper 1's 31, 5, 1.

## 8. Green et al. 2023, JMIR Formative Research

- Source read: Europe PMC full-text XML (PMC10582803), CC BY 4.0.
- First author: James B Green. *JMIR Formative Research* 2023;7:e46491. DOI 10.2196/46491. PMID 37788066. PMCID PMC10582803.
- Deployed: "The mindLAMP app was the platform in which the DMHI was delivered in this protocol." Matches the tag.
- Verdict: REJECT, no-cohort. A quality improvement project with 5 patient dyads across two Boston coordinated-specialty-care clinics, of whom 3 completed follow-up. Adoption and penetration were 53% (9/17) across patients and clinicians. The cohort is too small to report deployment reality.

## 9. Li et al. 2024, Exploration of Digital Health Technologies

- Source read: publisher PDF (open access), 13 pages.
- First author: Huijun Li (PDF byline). *Explor Digit Health Technol* 2024;2:7-19. DOI 10.37349/edht.2024.00007. PMCID not in PDF.
- Deployed (Instruments): "Participants did cognitive training (memory and attention in particular) in an MHA called SMART, an app modified based on Learn, Assess, Manage, and Prevent (LAMP)." "Participants in this study used the IOS version." Recruited 2017 to 2019 in Shanghai and Suzhou.
- Verdict: BORDERLINE-reject, no-cohort. The instrument is a LAMP-derived cognitive-training app rather than mindLAMP as profiled, and the paper does not say whether it ran on LAMP infrastructure. Its deployment content is thin. 10 of 40 intervention participants were lost at 3 months with reasons, and 6 of 40 reported slow response or freezing while 4 said data could not be saved. There are no usage, adherence or completeness figures, and MARS ratings make up most of the results.

## 10. Zhao et al. 2026, JMIR Formative Research

- Source read: Europe PMC full-text XML (PMC13449976), CC BY 4.0.
- First author: Xinying Zhao. *JMIR Formative Research* 2026;10:e89485. DOI 10.2196/89485. PMID 42566247. PMCID PMC13449976.
- Deployed: "We conducted an intensive longitudinal study integrating smartphone-based EMA with continuous RIP using a Hexoskin smart shirt." "EMA was implemented using the Huixin EMAI platform (ZenSeven Technology Co, Ltd)". The citation graph tagged Beiwe. Beiwe does not appear in the full text.
- Verdict: REJECT, validation. Instrument not profiled: Hexoskin smart shirt (respiratory inductance plethysmography) and Huixin EMAI. The main aim is a sighing biomarker for anxiety. The secondary feasibility content (38 enrolled, 91.4% of targeted daytime wear) would be usable if Hexoskin were profiled. Hexoskin is a Module 1 expansion candidate.

## 11. Paolillo et al. 2026, medRxiv

- Source read: medRxiv JATS XML (full text), CC BY-NC-ND. Also deposited in PMC as PMC13622314 (OpenAlex), though the Europe PMC search by DOI did not return it.
- First author: Emily W Paolillo (medRxiv API author list). Posted 2026-09-21. DOI 10.64898/2026.09.18.26363439. Preprint, not peer reviewed.
- Deployed (Methods): "participants downloaded the ALLFTD Mobile App (available on both iOS and Android devices) onto their personal smartphones". Introduction: "This ALLFTD Mobile app, developed in collaboration with Datacubed Health". Passive streams were battery percentage and step count. The citation graph tagged Beiwe. Beiwe does not appear in the full text.
- Verdict: REJECT, validation. Instrument not profiled: ALLFTD Mobile App by Datacubed Health. The aims are reliability, validity and clinical utility of passive features in 567 adults across the FTLD spectrum. It does report deployment figures. Passive data were available for 98% of enrolled participants. All 10 participants with missing passive data used iOS (p=0.10). Android showed greater battery drain than iOS. Datacubed Health is a Module 2 expansion candidate because the platform underpins a large multisite consortium.

---

## Expansion candidates

- Datacubed Health (ALLFTD Mobile App). Module 2. Commercial smartphone assessment platform with passive battery and step data, deployed across the ALLFTD consortium (paper 11).
- Hexoskin smart shirt. Module 1. Research-grade respiratory and ECG garment (paper 10).
- Weak or not recommended: UTSW mHealth custom app (paper 2), Feels.ai (paper 5), SMART (paper 9, LAMP-derived).

## Bearing on open questions

- Q106 and Q115 (Beiwe heartbeat). No bearing. None of the four Beiwe-tagged papers deployed Beiwe, and one was unobtainable.
- OS-patterned missingness. Paper 1 adds a mindLAMP data point. iPhone users lost less GPS than Android users, and an apparent race difference in missingness tracked Android ownership. Paper 11 runs the other way for a different platform, with all 10 participants missing passive data on iOS.
