# Module 3 citation-graph screening, batch D, 16 papers, 2026-10-31

Screened against `_screening-and-profile-rules.md` Part A, CLAUDE.md "Module 3" and README scope rules. Candidates came from the citation-graph pass in `_citation-graph-scan-2026-10.md`. Full text was sought through Europe PMC (search by DOI, then `fullTextXML`), NCBI efetch for PMC XML when Europe PMC returned a server error, then OpenAlex-listed repository and preprint copies. No personal identifier was sent to any service. No bot check was passed. No PDF was stored in the repository. Cohort-overlap check by grep of `profiles/*.md`, `literature-index.json` and `_scan-queue.md` for each DOI, first author and cohort name found no existing Module 3 profile for any included cohort. One rejected paper (Mahir 2025) shares the MoMo-Mood cohort with `aware-momo-mood-mood-disorders.md`.

| # | Paper | Verdict | Reason code | Device/platform actually deployed |
|---|---|---|---|---|
| 1 | Li 2022, JMIR Form Res | REJECT | no-cohort | Unnamed WASH study app (not profiled). AWARE is cited only for iOS limits |
| 2 | Zhang 2025, Proc ACM HCI | REJECT | unobtainable | Not determinable (ACM challenge page) |
| 3 | Chiou 2026, BMC Sports Sci Med Rehabil | REJECT | no-cohort | Polar H10 chest strap as an in-class intensity monitor at one site only |
| 4 | Mayne 2023, Sleep Health | INCLUDE | (deployment; GPS completeness per day with named causes, EMA completion) | AWARE app on own phones for GPS; EMA by REDCap text links; Actiwatch-2 |
| 5 | Mahir 2025, JMIR mHealth uHealth | REJECT | validation | AWARE screen events vs Actiwatch 2 vs Murata bed sensor vs EMA (MoMo-Mood) |
| 6 | Bardram 2023, ACM Trans Comput Healthc (DiaFocus) | REJECT | unobtainable | Not determinable from full text (all routes served challenge pages) |
| 7 | Howie 2024, J Surg Res | REJECT | unobtainable | Not determinable (repository and publisher served challenge pages) |
| 8 | Davis-Wilson 2025, JMIR Form Res | REJECT | validation | Garmin Fenix 6/6s via Health Companion SDK and the SIGMA+ Health app; Polar H10 reference in 5 |
| 9 | Jackson 2025, Int J Ment Health Nurs | REJECT | no-cohort | Polar H10 during a single VR session, 7 participants |
| 10 | Fifield 2026, Research Square | INCLUDE (preprint) | (deployment; completion by group, retention, missed-prompt reasons) | m-Path, own phones |
| 11 | Pihlajamäki 2026, Behav Res Methods | INCLUDE | (deployment; randomised incentive effect on compliance, zero attrition) | m-Path, own phones |
| 12 | Geeraerts 2026, Palliat Med | INCLUDE | (deployment; invite-to-enrol funnel, compliance, dropout reason) | m-Path on provisioned Motorola e20 Android phones |
| 13 | Stroian 2024, J Contextual Behav Sci | BORDERLINE-include | (deployment; install, activation, day-use and stage completion) | m-Path as intervention delivery platform, own phones |
| 14 | Verbeke 2024, Curr Dev Nutr | REJECT | no-cohort | Qualtrics email survey for the pilot; m-Path only in two 1-week UX rounds of 10 |
| 15 | Kaplan 2025, Behav Res Methods | REJECT | validation | Fabla voice-diary app (not profiled) vs Qualtrics text diary |
| 16 | Golsong 2024, JMIR Form Res | INCLUDE | (deployment; full funnel, dropout rule, per-questionnaire response counts) | App built on m-Path, own phones |

---

## 1. Li et al. 2022, JMIR Formative Research

- Source read: Europe PMC full-text XML (PMC9706389).
- First author: Sophia Xueying Li (first contributor record). Year 2022. JMIR Form Res 6(11):e40765. DOI 10.2196/40765. PMID 36374539. PMCID PMC9706389 (from the XML).
- Deployed (Methods, Data Collection): "Sensor-based data were collected actively and passively from participants through the study app." The app is never named. AWARE appears only as reference 38 (Nishiyama et al.), cited for iOS collection restrictions. The citation-graph attribution to AWARE is wrong.
- Verdict: REJECT, no-cohort. Instrument not profiled: unnamed WASH (Warfighter Analytics Using Smartphones for Health) study app. The deployment content itself is rich and would qualify if the platform were identified.
- Numbers that would matter if the app is identified: 17,556 enrolled, 6788 (38.66%) excluded as malicious actors, 10,768 analysed. Two recruitment phases (social media and news, March to July 2020; Prolific and MTurk, 2021). 84-day protocol. Android exposed 31 passive modalities and iOS 14. 18 of 31 Android streams and 12 of 14 iOS streams were shared by at least 50% of users. Phase 2 required accelerometer and gyroscope, yet 503 of 4089 (12.31%) did not share accelerometer and 856 of 4089 (20.89%) did not share gyroscope. Phase 1 median retention iOS 37 days vs Android 22 days. Phase 2 baseline-survey completers retained a median 59 days vs 19. Black participants shared passive streams less (OR 0.44 to 0.49). Payment weekly in phase 1, every 3 weeks in phase 2.
- Expansion candidate: low priority. Module 2 cannot profile an unnamed app. The WASH platform would need identifying first (the paper cites Bracken et al. 2022 for the malicious-actor work).
- Existing profile on this cohort: none.

## 2. Zhang, Trujillo and Poellabauer 2025, Proceedings of the ACM on Human-Computer Interaction

- Source read: none. OpenAlex and Semantic Scholar list only `dl.acm.org/doi/pdf/10.1145/3711043` as the OA copy, with no repository full text. ACM DL served a Cloudflare "Just a moment..." challenge page earlier in this programme. A further script request to ACM was refused by this session's safety classifier as bot-check circumvention, so it was not retried. arXiv returned no preprint by title or by author. The FIU discovery record found by web search has no file.
- Verdict: REJECT, unobtainable (bot check).
- Q118 status: unchanged. Whether the study deployed AWARE remains unverified. Needs a by-hand fetch in a browser or a copy from the authors (FIU). Add to `shared/manual-sweep.md`.

## 3. Chiou et al. 2026, BMC Sports Science, Medicine and Rehabilitation

- Source read: NCBI efetch PMC XML (PMC12917964). Europe PMC `fullTextXML` returned HTTP 500 and its PDF render served a challenge page.
- First author: Shin-Yi Chiou. Year 2026. BMC Sports Sci Med Rehabil 18:97. DOI 10.1186/s13102-025-01507-6. PMID 41593782. PMCID PMC12917964.
- Deployed (Methods): "A chest-worn heart rate monitor (Polar H10) was provided to participants at MoveWell from October 2024 to April 2025 (iteration 2 & 3) but was not expanded to the other site due to equipment availability." Data were viewed in the Polar Team app.
- Verdict: REJECT, no-cohort. A real but small exercise-programme cohort (10 participants). The device was an intensity-fidelity tool. Adherence is class attendance (MoveWell 82 ± 11% and 72 ± 22%, Greenbank 48 ± 20%), not device wear. No device completeness or failure content.
- Existing profile on this cohort: none.

## 4. Mayne et al. 2023, Sleep Health

- Source read: NCBI efetch PMC XML (PMC10293018, author manuscript). Europe PMC `fullTextXML` returned HTTP 500.
- First author: Stephanie L. Mayne. Year 2023. Sleep Health 9(3):331-338. DOI 10.1016/j.sleh.2023.01.014. PMID 36781356. PMCID PMC10293018.
- Deployed (Data Collection): "GPS tracking was conducted using an app from the AWARE Framework system, which participants downloaded onto their own smartphones." EMA was by "text messages with embedded REDCap survey links", not AWARE. Actiwatch-2 (Philips Respironics) on the non-dominant wrist. Matches the citation for AWARE.
- Verdict: INCLUDE. Feasibility is the stated aim. Per-participant-day GPS completeness with named causes of loss is the transferable content.
- Existing profile on this cohort: none.
- Profile written: `profiles/aware-adolescent-neighborhood-sleep-gps-ema.md`.

### Extraction

- Design: single-arm pilot, 7 days, remote (Participants and Methods B.1, B.2).
- Funding/COI: LDI pilot grant, NHLBI K01HL155860, CHOP Possibilities Project. Competing interests "None" (Acknowledgements).
- Compensation: adolescents up to $90, parents $10 (B.2).
- Population: 25 adolescents aged 15 to 17, Philadelphia, enrolled November 2020 to July 2021 (B.1). Mean age 16.2, 56% male, 52% non-Hispanic white, 36% non-Hispanic Black, 68% parent with bachelor's or higher, 24% household income under $50,000 (Results, Table 1).
- Recruitment: CHOP Recruitment Enhancement Core email invitations to parents, plus flyers (B.1). Numbers invited, screened, refused: not reported.
- Deployment model: BYOD AWARE app, background GPS every 60 seconds (B.2). OS split not reported. AWARE client not named.
- GPS completeness (C.1): 202,763 coordinates. Mean 19.6 hours per participant-day (SD 8.2, median 24, range 0 to 24). 5 of 25 (20%) had every minute.
- Failure modes (C.1): phones turned off; "an issue with Android phones where additional settings needed to be manually enabled to override limits on data collection"; one participant with inaccurate data "due to an unexplained technical issue".
- Analytic filters (B.4): drop points outside Philadelphia or accuracy over 100 m; drop person-days under 360 minutes. Result 135 days from 21 adolescents (Table 2). Losses per filter not reported.
- EMA (C.2): 78.6% overall. Late afternoon 88.0%, morning 61.7%. Median per participant 86% (range 29 to 100%). Main barrier not being near the phone.
- Actigraphy (Table 1 footnote): 23 of 25. One device not returned, one malfunctioned.
- Acceptability (C.3): 1 of 25 (4%) worried about location privacy. 80% found EMA easy. 84% said EMA did not interfere.
- Authors' conclusions: feasible and acceptable for up to one week. Recommend continuous monitoring to troubleshoot (Discussion).
- Not reported: screening funnel, OS split, AWARE client, number of Android phones affected, battery, data volume, retention as a separate figure.

## 5. Mahir et al. 2025, JMIR mHealth and uHealth

- Source read: Europe PMC full-text XML (PMC12741658).
- First author: Afrooz Mahir. Year 2025. JMIR Mhealth Uhealth 13:e82465. DOI 10.2196/82465. PMID 41380148. PMCID PMC12741658.
- Deployed (Data Collection): "smartphone and EMA data was gathered through the AWARE app". Actiwatch 2, Murata SCA11H bed sensor. The 2-week active phase of MoMo-Mood plus its pilot.
- Verdict: REJECT, validation. The paper is a cross-modality agreement study of sleep onset, offset and total sleep time. Its only deployment content is per-modality counts after cleaning.
- Existing profile on this cohort: `aware-momo-mood-mood-disorders.md` (same MoMo-Mood study). The new numbers below are small enough to add to that profile as a note if wanted.
- Numbers that could be added to the existing profile: 164 main-study participants plus a 37-person pilot. 13 of 164 (7.9%) submitted no passive data. After filtering, 102 actigraph users, 108 bed-sensor users and 148 smartphone users. The 2-week active phase length was set by Actiwatch battery life without recharging. Compensation was four movie tickets.

## 6. Bardram et al. 2023, ACM Transactions on Computing for Healthcare (DiaFocus)

- Source read: none. ACM DL PDF and full-HTML routes returned a challenge page and HTTP 403. OpenAlex lists green copies at DTU Orbit (`DiaFocus_ACM_HEALTH_2022_2_.pdf`) and the University of Copenhagen research portal (`DiaFocus_KU.pdf`). Both file URLs returned Cloudflare "Just a moment..." challenge pages to a plain request. Figshare item 28621112 holds metadata only, with no file. arXiv has no preprint.
- Verdict: REJECT, unobtainable (bot check on every route). Also not a strong Module 3 candidate on its abstract, since the 12-patient feasibility study sits inside a system-design paper.
- Q112 finding: no new evidence from this paper. The abstract says only that DiaFocus "is built using a generic data collection framework for mobile and wearable sensing". It does not name CARP. The full text was not read, so this pass cannot say whether the body names CARP or CAMS. The existing 2026-10-09 resolution, which rests on CARP's own DiaFocus pages, is untouched.
- Manual sweep: the DTU Orbit or KU copy can be opened by hand in a browser to check the framework sentence.
- Related lead: the 6-month DiaFocus clinical pilot (Lind et al. 2025, JMIR Diabetes 10:e63894, PMC12377514) is open access and is the better Module 3 candidate. It is already noted in `module-02-digital-phenotyping/sources.md` (S-CARP-13) and `_uncovered-platforms-report.md`, but has no Module 3 profile.

## 7. Howie et al. 2024, Journal of Surgical Research

- Source read: none. Not in PMC (PMID 39106733 only). The Edinburgh Research Explorer copy (`Feasibility_of_Wearable_Sensors_HOWIE_DOA02072024_VOR_CC-BY-NC-ND.pdf`) and the journal PDF both returned challenge pages.
- First author per Europe PMC metadata: Howie EE (byline not seen). J Surg Res 2024;302:222-231.
- Verdict: REJECT, unobtainable (bot check). The abstract describes four studies, 84 participants and five sensors. Which sensors were used, and whether any is Polar, cannot be checked without full text. Add to the manual sweep.

## 8. Davis-Wilson et al. 2025, JMIR Formative Research

- Source read: Europe PMC full-text XML (PMC11894354).
- First author: Hope Davis-Wilson. Year 2025 (issue year; the batch file says 2024). JMIR Form Res 9:e53645. DOI 10.2196/53645. PMID 39993288. PMCID PMC11894354.
- Deployed (Device Protocol): "Each participant was outfitted with a Garmin Fenix 6/6s smartwatch". IBI data came through Garmin's Health Companion SDK into the RTI SIGMA+ Health app on the participant's phone or a study-issued Samsung phone, then to AWS. "A subset of participants (n=5) wore a Polar H10 ECG heart rate monitor" as reference, read through the Elite HRV app. The citation-graph label of Polar is the reference device, not the instrument under study.
- Verdict: REJECT, validation. The paper is a semi-simulation of missing IBI data plus a Garmin vs Polar H10 agreement analysis.
- The one operational number: 31 recruited, and 15 excluded for an expected data fraction under 70%. Data collection May 2022 to June 2023, up to 180 days. Funding DARPA 140D63-19-C-0023. Paid $50 every 3 months.
- Module 1 note: confirms Garmin Health Companion SDK access to beat-level IBI for research, worth a line in `module-01-wearables/profiles/garmin.md` if not already there.
- Existing profile on this cohort: none.

## 9. Jackson et al. 2025, International Journal of Mental Health Nursing

- Source read: Europe PMC full-text XML (PMC11724164).
- First author: Jessica Eve Jackson. Int J Ment Health Nurs 2025;34(1):e13499. DOI 10.1111/inm.13499. PMID 39794919. PMCID PMC11724164.
- Deployed (Methods): "The Polar H10 Heart Rate Monitor was used to measure heart rate, which was self-assembled by the participants around their chest." Films shown on a Meta Quest 2.
- Verdict: REJECT, no-cohort. 13 expressed interest, 8 entered routine assessment, 7 viewed the films, in a single lab session. Gaze recording failed for one participant per scenario "due to technical error". No longitudinal deployment content.

## 10. Fifield et al. 2026, Research Square (preprint)

- Source read: Research Square preprint PDF v1 (CC BY 4.0), 31 pages. Text only. Figures 1, 2 and 4 and Additional file 1 were not read.
- First author: K Fifield (byline). Posted 2026-10-12. DOI 10.21203/rs.3.rs-10394948/v1. No PMID or PMCID. Not peer reviewed.
- Deployed (EMA protocol): "EMA questions were sent through the m-Path smartphone app (Mestdagh et al., 2023)." Matches the citation.
- Verdict: INCLUDE, labelled as a preprint.
- Existing profile on this cohort: none.
- Profile written: `profiles/mpath-tsc-young-adults-ema-feasibility.md`.

### Extraction

- Design: two-week intensive longitudinal mixed-methods study, CREMAS-reported (Methods, Design).
- Funding/COI: KCL psychology PhD studentship; KCL Public Engagement Small Grant for the advisory group; "No competing interests reported" (Funding statement; title page). Compensation not stated in the main text.
- Population: 18 young adults with TSC and 18 age- and sex-matched controls, aged 17 to 35 (Participants). Predicted IQ above 70 and own smartphone required (Limitations).
- Enrolled to analysed: 36 consented, 0 withdrew, 36 in completion analysis. One TSC participant did partial baseline (Participants).
- Protocol: 4 prompts a day, semi-random in 2-hour blocks, at least 1 hour apart, 14-hour maximum day. Reminder at 30 minutes, expiry at 60 minutes. Up to 29 items. 14 days. 56 prompts each, 2016 total (EMA protocol; Results).
- Completion: TSC 896/1008 (88.89%, range 60.71 to 100%). Non-TSC 906/1008 (89.88%, range 76.79 to 100%). Overall 1802/2016 (89.38%). W = 148.5, p = .679 (Results).
- Correlates in TSC: total current symptoms rho = -0.48, p = .043. Lifetime symptoms rho = -0.54, p = .019. No association with genotype, IQ, TSSS, demographics (Table 3).
- Missed-prompt reasons: sleeping first in both groups. Socialising second in TSC, studying in controls (Fig. 4 text).
- Careless responding: 5.1% of valid responses (6.1% TSC, 4.1% non-TSC).
- Usability: PSSUQ TSC median 1.37, non-TSC mean 1.38, U = 146.5, p = .496.
- Technical failures: none reported.
- Authors' conclusions and recommendations: feasible and acceptable; expand activity categories, reorder questions, add flexible response formats (Summary of Feasibility). Longer protocols, possibly randomised by prompt frequency (Limitations).
- Not reported in text: recruitment funnel counts, compensation, OS split, any technical issue.

## 11. Pihlajamäki et al. 2026, Behavior Research Methods

- Source read: PsyArXiv preprint v1 PDF from OSF (`osf.io/download/pc924_v1/`, 53 pages). The Springer PDF served a "Client Challenge" page and was not read. Not in PMC.
- First author: Milla Pihlajamäki (preprint byline). Published BRM 2026;58(11):300. DOI 10.3758/s13428-026-03164-0. PMID 42778816. PMCID not found.
- Deployed (Procedure): "We used REDCap to collect and manage all non-ESM data including the screening, baseline, and follow-up questionnaires and m-Path (Mestdagh et al., 2023) to collect and manage all ESM data." Matches the citation.
- Verdict: INCLUDE. The figures are from the preprint and the profile says so.
- Existing profile on this cohort: none.
- Profile written: `profiles/mpath-student-esm-incentive-type-rct.md`.

### Extraction

- Design: three-arm randomised experiment, 64 per arm, REDCap randomisation (Procedure; Experimental manipulation). Registration after data collection, deviations documented (Transparency and openness).
- Funding/COI: FWO G049023N, KU Leuven C1 C16/23/011. No conflicts declared (Statements). Ethics KU Leuven G-2023-7096.
- Compensation: fixed arms 80 euros (10 baseline, 63 ESM, 7 follow-up). Per-beep arm 0.5 euros per beep, up to 63 euros for ESM (Experimental manipulation).
- Population: students aged 18 to 30, Dutch and English proficiency, own smartphone, no previous ESM study (Sample). Fixed arm 81.25% female, feedback arm 84.38% female (Table 1; per-beep column not captured in text extraction).
- Enrolled to analysed: 192 recruited, no dropouts, 192 analysed. 190 in compliance models (Results, Sample characteristics; H1).
- Protocol: 9 beeps a day, 9:00 to 22:30, nine 75-minute windows each followed by 15 minutes without a beep. 24 to 28 items. Questionnaire available 15 minutes (Response latency definition). 14 days.
- Compliance: per-beep 90.81%, fixed 86.64%, feedback 86.53% (86.38% with the 2 excluded). Per-beep vs each other arm p<.001. Fixed vs feedback p=.809. No time interaction (H1). Table 1 SDs 9.31 (fixed) and 9.9 (feedback).
- Partial compliance: 163 responses (0.67%) from 79 participants (H1).
- Attention check failure at least once: 1.56% of participants (H2).
- Cost: per-beep arm paid about 57.21 euros on average for ESM, 5.79 euros less than fixed (Recommendations).
- Technical issues: "we were not aware of any technical problems during it" (Sample characteristics).
- Authors' recommendations: use payment per beep in motivated non-clinical student samples; feedback did not change behaviour; extend to clinical samples (Discussion; Limitations).
- Not reported in preprint: recruitment dates, screening counts, OS split.

## 12. Geeraerts et al. 2026, Palliative Medicine

- Source read: author manuscript PDF from the Ghent University repository (18 pages). Not in PMC. Published typeset version not read.
- First author: Joran Geeraerts (manuscript title page). Palliat Med 2026;40(4):535-545. DOI 10.1177/02692163261416264. PMID 41677574. PMCID not found.
- Deployed (Measures and procedures): "We provided participants with a Motorola e20 smartphone (Android operating system) for the study's duration, training in using the device to fill in the ESM-AC questionnaire in the m-Path application". Matches the citation.
- Verdict: INCLUDE.
- Existing profile on this cohort: none.
- Profile written: `profiles/mpath-advanced-cancer-esm-feasibility.md`.

### Extraction

- Design: 7-day observational ESM study with baseline and follow-up (Study design). Protocol published (ref 12). Ethics UZ Brussel BUN 1432023000043, Ghent ONZ-2023-0136.
- Funding/COI: FWO G0C8120N; FWO fellowship 12AEO24N. No conflicts. Compensation not reported.
- Population: stage III or IV lung or stage IV breast cancer, ECOG 2 or better, Dutch-speaking, at UZ Brussel and UZ Ghent, September 2023 to March 2024. Stratified by age and tumour site. Mean age 66.3 (range 35 to 83), 72.5% female (Table 1).
- Funnel: 79 invited, 40 consented (50.6%); most decliners cited no time or interest. 1 dropout after 2 days (stress from repetitive questions). 2 excluded for misinterpreting response scales (aged 81 and 82). 37 analysed (Results).
- Protocol: 10 auditory beeps a day, about 30 seconds, random within 10 blocks at least 30 minutes apart, personalised day window. 60 scheduled across 6 days (Measures). Response window not stated.
- Compliance: 1703 of 2400 scheduled (71%) (Feasibility). No participant characteristic, time or symptom variable predicted compliance.
- Inconsistency: the Discussion refers to "the 80% completion rate". Unreconciled with 71%.
- Latency 37 seconds (SD 66). Completion time 3.8 minutes (SD 1.9). Conscious misses on 17 days, mostly during activities.
- Support: researcher phone call after day 1; phone and email throughout.
- Acceptability: burden items 1.4 to 3.6, ease of use 4.3 to 6.6, clarity 6 to 6.9, reactivity 1.1 to 1.5 on 1 to 7 scales (Table 2).
- Technical failures: none reported.
- Authors' recommendations: pen-and-paper alternatives for inclusivity; longer, less intensive schedules may improve enrolment; training and check-up calls helped (Discussion).
- Not reported: response window, compensation, device return rate, any technical issue.

## 13. Stroian et al. 2024, Journal of Contextual Behavioral Science

- Source read: published PDF from the Bilkent University institutional repository (bitstream via `hdl.handle.net/11693/116823`). Not in PMC.
- First author: Paula I. Stroian (byline). J Contextual Behav Sci 2024;34:100839. DOI 10.1016/j.jcbs.2024.100839. No PMID or PMCID found. Available online 2024-09-06.
- Deployed (Procedure): "participants allocated to the nCompass group received detailed instructions for installing and using the m-path mobile application ... on which the intervention was delivered." Matches the citation.
- Verdict: BORDERLINE-include. m-Path is the delivery platform for an intervention, not a research data-collection instrument. It is kept because the paper reports install, activation, days of use and stage completion for the platform arm, which a team reusing m-Path for an intervention would need.
- Existing profile on this cohort: none.
- Profile written: `profiles/mpath-ncompass-depression-self-help-pilot-rct.md`.

### Extraction

- Design: two-arm pilot RCT, Qualtrics randomisation, preregistered on OSF (Method 2.1, 2.3; Ethics line).
- Funding/COI: no funding statement; no conflict of interest. Incentive a draw for one of five $20 vouchers on completing follow-up (2.3).
- Population: adults with BDI-II of 14 or more, Romanian Facebook groups, March to November 2023. nCompass mean age 27.06 (SD 7.13), 92.16% female (2.1; Table 1).
- Funnel (4.1): 102 randomised, 51 per arm. nCompass 48 installed (94.12%), 43 active (84.31%), 42 post-test (82.35%), 32 follow-up (printed 62.45%). Control 50 post-test (printed 94.33%), 40 follow-up (printed 75.47%). The printed control percentages and the nCompass follow-up percentage do not reconcile with n = 51.
- Engagement (4.1): of 48 installers, stage 1 41 (85.41%), stage 2 38 (79.16%), stage 3 35 (72.92%). Of 43 active, 40 (93.02%), 36 (83.72%), 32 (74.41%). Mean 10.34 of 15 days used. 68.15% of proposed activities self-reported done on active days.
- Technical support: users with difficulties contacted the team by email and were helped by email or phone. Number not reported.
- Authors' recommendations: more extensive incentives for adherence to study measures in fully online trials (Discussion).
- Not reported: OS split, notification delivery, missing evening ratings, technical failures, screening counts in text.

## 14. Verbeke and Matthys 2024, Current Developments in Nutrition

- Source read: Europe PMC full-text XML (PMC11585766).
- First author: Joke Verbeke. Curr Dev Nutr 2024;8(11):104479. DOI 10.1016/j.cdnut.2024.104479. PMID 39582947. PMCID PMC11585766.
- Deployed: the pilot ESDAM ran as "a Web-based questionnaire platform (Qualtrics) via email". m-Path ("mPath") was used only in Phase IV, two 1-week UX rounds of 10 participants each, three prompts a day.
- Verdict: REJECT, no-cohort. The m-Path part is two usability rounds with interview outcomes and no completion or completeness figures. The pilot is a Qualtrics convergent-validity study.

## 15. Kaplan et al. 2025, Behavior Research Methods

- Source read: Europe PMC full-text XML (PMC12343679).
- First author: Deanna M. Kaplan. Behav Res Methods 2025;57(9):257. DOI 10.3758/s13428-025-02777-1. PMID 40797121. PMCID PMC12343679.
- Deployed: "Fabla, a researcher-developed and university-hosted smartphone app" built in Flutter for iOS and Android on HIPAA-eligible AWS, maintained by Emory's AppHatchery, compared with a Qualtrics text diary. m-Path appears only in the Introduction as the one other EMA platform with audio responses.
- Verdict: REJECT, validation. Instrument not profiled: Fabla. A within-person comparison of voice and text diaries (87 participants, 1 week each, November 2023).
- Expansion candidate: Fabla for Module 2 (voice-first EMA, open to outside research teams per the paper). Low priority, since it is a single-institution tool with one validation study.

## 16. Golsong et al. 2024, JMIR Formative Research

- Source read: Europe PMC full-text XML (PMC11656116).
- First author: Konstanze Golsong. JMIR Form Res 2024;8:e60461. DOI 10.2196/60461. PMID 39630503. PMCID PMC11656116.
- Deployed (App Intervention): "It was built using the m-Path system, which was developed at Katholieke Universiteit Leuven, Belgium". Matches the citation.
- Verdict: INCLUDE.
- Existing profile on this cohort: none. A companion paper on dropout reasons (Kaufmann et al., ref 23) is announced.
- Profile written: `profiles/mpath-psychiatric-outpatient-app-support.md`.

### Extraction

- Design: prospective single-arm observational study, DRKS0027536, Leipzig ethics 558/21-ek (Study Design; Ethical Considerations).
- Funding/COI: no grant named; OA fund only. No conflicts. "No compensation was given for participation in the study."
- Population: psychiatric outpatients at University Hospital Leipzig, any diagnosis, February to March 2022. Mean age 37.21 (SD 13.55), 74% women (Sample Characteristics).
- Funnel (Participants and Recruitment): 88 introduced, 57 (65%) consented and started, 2 deleted data, 15 dropped out for 1 week or more of non-use, 2 missed the final questionnaire, 38 analysed. 31 decliners gave reasons on paper (deferred to ref 23).
- Dropout rule: no app use for a full week, or a request to stop. Completers 40/57 (70%), dropouts 17/57 (30%) (Definition of Completers).
- Deployment: BYOD, supervised installation after a therapy session, handout and manual, follow-up call at 1 week (Participants and Recruitment).
- EMA-like questionnaires: 3 a day, windows 6:00 to 11:59, 12:00 to 17:59, 18:00 to 23:59, maximum 28 each. Full cohort (n=55) means 15.15, 14.67, 14.00. Completers (n=38) means 20.26, 19.39, 20.08 (Tables 2 and 3). 49 of 55 and 37 of 38 answered all three types at least once.
- Module use: 44% of full cohort and 26% of completers never tried a module (Module Use).
- Activity button: completers mean 12 (SD 15.72, median 6); full cohort mean 10 (SD 13.82, median 4).
- Safety: PHQ-9 item 9 SOP triggered for 14/57 (25%) at baseline and 11/57 (19%) at post (Safety Procedures).
- Technical failures: none reported.
- Authors' recommendations: push reminders and personalisation to raise module use (Discussion).
- Not reported: OS split, reasons for dropout (deferred), any technical issue.

---

## Open-question findings

- Q112 (DiaFocus on CARP): this pass could not read the DiaFocus design paper. Every route to it served a challenge page or 403. The abstract says only "a generic data collection framework for mobile and wearable sensing". The 2026-10-09 resolution from CARP's own pages stands. A by-hand read of the DTU Orbit or KU repository copy would settle whether the paper body names CARP or CAMS.
- Q118 (AWARE ACM paper `10.1145/3711043`): still unobtainable. No author-hosted copy, repository copy or arXiv preprint exists. The platform remains unverified.

## Manual-sweep items

1. `10.1145/3711043`, ACM DL PDF, open in a browser and check the Methods for the sensing app (Q118).
2. `10.1145/3586579`, DTU Orbit `files/350251047/DiaFocus_ACM_HEALTH_2022_2_.pdf` or KU `files/405745478/DiaFocus_KU.pdf`, check for "CARP" or "CAMS" (Q112).
3. `10.1016/j.jss.2024.07.009`, Edinburgh Research Explorer `files/526009302/...VOR_CC-BY-NC-ND.pdf`, check which five sensors were used and whether any is profiled.
4. `10.3758/s13428-026-03164-0`, Springer published version, check the compliance figures match the preprint.

## Expansion candidates

- Fabla (Emory voice-diary app) for Module 2. Low priority.
- WASH study app (unnamed) for Module 2, only if the platform can be identified.
- Lind et al. 2025, JMIR Diabetes 10:e63894 (PMC12377514), the DiaFocus 6-month pilot, as a Module 3 candidate on CARP.
