# Research Library — Oura, WHOOP, Apple Watch

A bibliography of peer-reviewed / published research involving Oura, WHOOP, and Apple Watch,
organized by **sponsorship status** rather than by topic. Companion to `validation-evidence.md`,
which does deep full-text extraction on the sleep-staging accuracy literature specifically. This
file is broader (any topic) but shallower per entry — authors, affiliations, funding/COI, key
finding, and a link.

**Last verified: 2026-08-24.** Supersedes the earlier two-device draft of this file. Open-questions pass
2026-10-09: new PSG entries for Oura and WHOOP, CQU funding checks, Apple hypertension, SpO2/temperature
re-search; each change is dated in place. Bibliographic and confidence corrections from the 2026-10-10 independent review
are also dated in place.

**PDFs for every legitimately open-access paper individually cited in this bibliography are now
stored under `literature/<device-slug>/`.** See `literature-library.md` for the full index —
OA/paywall status per paper, PDF links, and the sponsorship-tier column preserved alongside it. A
handful of bibliographic corrections (author lists, venues, one paper's tier) surfaced while
obtaining those PDFs are noted there rather than edited into this file's prose.

## How entries are classified

| Tier | Definition |
|---|---|
| **A — Vendor-employee-authored** | An author holds a position at the vendor (Oura Health, WHOOP Inc, Apple Inc) at time of publication, or the study is a named vendor-sponsored flagship (e.g. Apple Heart Study) where the vendor is a data-holder/co-sponsor even if individual employee authorship isn't confirmed. |
| **B — Vendor-funded / vendor-affiliated, independent authors** | Authors are academic/independent researchers with no vendor employment, but the study was funded by a grant from the vendor, the authors/lab have a disclosed financial relationship with the vendor (consulting fees, advisory board, stock, a sponsored faculty/research position), or the underlying dataset was collected via vendor-sponsored infrastructure. |
| **C — Independent** | No vendor funding, no vendor employment, no disclosed financial COI with the vendor. |

**Confidence markers**, matching this knowledge base's evidence-confidence standard:
- **Verified** — the actual funding/COI disclosure text was read directly (by a prior pass in this
  conversation, or quoted directly in a secondary source).
- **Corroborated** — multiple secondary sources agree, or the tier is inferred from a clearly
  documented institutional relationship (e.g. a named vendor-university partnership), but the
  paper's own disclosure section was not read directly.
- **Unclear** — could not confirm from available sources. Never guessed.

Tier assignments below carry their confidence marker explicitly. Downstream content should not cite
a Tier B/C split more confidently than the marker warrants.

---

# OURA

## Tier A — Oura-employee-authored

**Altini M, Kinnunen H. 2021.** "The Promise of Sleep: A Multi-Sensor Approach for Accurate Sleep
Stage Detection Using the Oura Ring." *Sensors* 21(13):4302, DOI 10.3390/s21134302. Author order
corrected 2026-10-10 against Crossref (Altini first).
Both authors Oura Health staff (Altini also Vrije Universiteit Amsterdam). Oura's own sleep-staging
algorithm validation paper. **Verified.** https://www.mdpi.com/1424-8220/21/13/4302

**Willoughby AR, Alikhani I, Karsikas M, Chua XY, Chee MWL. 2023.** "Country differences in
nocturnal sleep variability: Observations from a large-scale, long-term sleep wearable study."
*Sleep Medicine* 110:155–165. ~50 million nights, ~220,000 Oura users, 35 countries. Mixed
NUS/Oura Health (Finland) author list. **Corroborated** (affiliation inferred from institutional
listing, not a directly-read COI statement).

**A cluster of large-scale "N million nights" Oura-population papers** (jet-lag / travel-related
sleep disruption, etc.), referenced on Oura's own research page, apparently from the same
Oura-Finland/NUS author group as the item above. **Tier A likely, individually Unclear** — not
separately author-verified.

**TemPredict-family papers** — see Tier B below; while the *underlying infrastructure* is
Oura-sponsored, individual papers vary in whether an Oura/TemPredict-affiliated author with a direct
financial interest (e.g. Benjamin Smarr, a co-inventor with a disclosed Oura financial interest) is
listed as a co-author. Treat each TemPredict-derived paper's precise tier (A vs. B) as needing an
individual author check; they are grouped under Tier B here as a conservative default since the
common thread is sponsorship of the *data infrastructure*, not universal Oura employment.

## Tier B — Oura-funded / Oura-affiliated, independent authors

**Robbins R, Weaver MD, Sullivan JP, et al. 2024.** "Accuracy of Three Commercial Wearable Devices
for Sleep Tracking in Healthy Adults." *Sensors* 24(20):6532. Brigham and Women's Hospital. N=35,
single-night PSG, Oura Gen3 vs Fitbit Sense 2 vs Apple Watch S8. **Funded by Oura Ring Inc.; lead
author (Robbins) sits on Oura's Medical Advisory Board and receives Oura consulting fees.**
**Verified.** Full extraction in `validation-evidence.md` §2. Oura scored best of the three
(κ=0.65 four-stage). https://pmc.ncbi.nlm.nih.gov/articles/PMC11511193/

**Liang T, Yilmaz G, Soon CS. 2024.** "Deriving Accurate Nocturnal Heart Rate, rMSSD and Frequency
HRV from the Oura Ring." *Sensors* 24(23):7475. NUS Centre for Sleep and Cognition. Not Oura
employees, but the Centre runs a standing **Oura–NUS Joint Lab** whose director's lab "receives
funding support from Oura Health for testing of Oura devices and co-development of new methods"
(Oura's own announcement). **Corroborated** (partnership confirmed from Oura's blog; the paper's own
COI text not directly read). https://www.mdpi.com/1424-8220/24/23/7475

**TemPredict Study 1 — Mason AE, Kasl P, Quer G, et al. 2022.** "Detection of COVID-19 using
multimodal data from a wearable device: results from the first TemPredict Study." *Scientific
Reports* 12:3463. **Funded by an Oura Health sponsored contract.** COI: Epel received loaned Oura
Ring hardware; co-authors Ashley Mason and Benjamin Smarr are co-inventors on wearable-illness
patents, and Smarr discloses Oura consulting income and a financial interest in Oura Ring Inc.
**Verified** (disclosure quoted directly by a secondary source). Algorithm flagged ~20% of
COVID-positive participants 2 days pre-symptom, 80% by symptom-day 3.

**TemPredict Study 2 —** "Metrics from Wearable Devices as Candidate Predictors of Antibody
Response Following Vaccination against COVID-19." *Vaccines* (MDPI) 2022. Built on the same
Oura-sponsored TemPredict infrastructure. **Corroborated.**

**Mason AE, Kasl P, Soltani S, et al. 2024** (author correction 2024). "Elevated body temperature
is associated with depressive symptoms: results from the TemPredict Study." *Scientific Reports*.
Draws on the Oura-sponsored TemPredict cohort/infrastructure; this specific analysis's stated
funding line is **US Army Medical Research and Development Command (USAMRDC) MIDRP/MOMRP and MTEC**
— i.e., a *different*, non-Oura funder for this particular paper, layered on top of Oura-sponsored
data collection. **Corroborated**, tiered B as a conservative default because of the shared
infrastructure and shared authors with direct Oura financial ties, even though the immediate grant
line is military.

**"Assessing Adherence to Multi-Modal Oura Ring Wearables From COVID-19 Detection Among Healthcare
Workers."** *Cureus* 2023. Likely TemPredict-adjacent/Oura-sponsored dataset. **Unclear** — not
independently verified this pass.

**A dense cluster of reproductive-health / pregnancy / arrhythmia papers on Oura's own research
list**, several apparently involving Marija/Benjamin Smarr or other TemPredict-adjacent authors:
"Predicting labor onset relative to estimated date of delivery," "Biometrics of complete human
pregnancy" (*npj Digital Medicine*, Aug 2024), "Feasibility of continuous distal body temperature
for passive, early pregnancy detection," "AF detection using Oura Ring with photoplethysmography"
(*Heart Rhythm*), "Ultradian Rhythms in HRV and Distal Body Temperature Anticipate the LH Surge"
(*Scientific Reports*, 2020). **Unclear / flagged, not individually tier-verified** — strong
candidates for Tier A or B given the author-overlap pattern, but each needs its own COI check before
being relied on.

**Added 2026-10-12.** Qin S, Jouvencel A, Soon CS, Shaif N, Ong JL, Chee MWL. 2026. "Comparison of
rest-activity rhythm metrics derived from Oura ring and actiwatch devices: A device validation and
analytical pipeline comparison study." *Sleep Health*, PMID 42855352. National University of
Singapore Centre for Sleep and Cognition. No `<CoiStatement>` element present in the PubMed record,
but the senior/corresponding author's affiliation is given directly in the record as "Oura-National
University of Singapore (NUS) Joint Lab, Oura Pte Ltd, Singapore" — the same standing Oura–NUS Joint
Lab already tiered B for Liang et al. 2024 above. **Tier B. Corroborated** (corrected 2026-10-24
from Verified: the affiliation is quoted from the PubMed record, but the paper's own conflict of
interest statement has not been read, because the full text is blocked to scripts. Three authors,
Soon, Ong and Chee, list "Oura Pte Ltd" in the affiliation, so Tier A cannot be excluded until the
statement is read). N=41
healthy adults, 14 days concurrent wear vs. Actiwatch (AW2); rest-activity rhythm metrics (IS, IV, RA,
L5/M10 timing) via nparACT, MotionWare, and a custom pipeline (ICC, Spearman's ρ, Bland-Altman).
https://pubmed.ncbi.nlm.nih.gov/42855352/

**Moved from Tier C 2026-10-24.** **Ong JL, Qin S, Martin TH, Chua XY, Soon CS, Yilmaz G, et al. 2026.** "24h movement behaviours in
university students compared to working age and older adults: wearable-based evidence and
cardiometabolic health implications." *BMC Medicine* 24(1):485. National University of Singapore,
Centre for Sleep and Cognition. **Senior author Michael W. L. Chee is a member of Oura's medical
advisory board; three co-authors are members of the Oura–NUS Joint Lab, though the paper states
this specific work "was conducted independently of the Joint Lab and was designed, funded, and
executed solely by NUS."** **Verified** (COI text read directly). 1,967 adults across three
Singaporean cohorts, 4 weeks of Oura recordings each: university students logged the most sedentary
time (633.9 min/day) and least activity (320.3 min/day) and sleep (431.8 min/day) of the three age
groups; reallocating 30 min/day from sedentary time to sleep or activity was associated with lower
BMI and body-roundness index. **Tier B. Verified** (the senior author's advisory board seat is an author tie under this file's Tier B definition, whatever the paper says about the Joint Lab). https://pmc.ncbi.nlm.nih.gov/articles/PMC13573439/

## Tier C — Fully independent

**Cao R, Azimi I, Sarhaddi F, Niela-Vilen H, Axelin A, Liljeberg P, Rahmani AM. 2022.** "Accuracy
Assessment of Oura Ring Nocturnal Heart Rate and Heart Rate Variability in Comparison With
Electrocardiography in Time and Frequency Domains." *JMIR* 24(1):e27487. UC Irvine / University of
Turku. **Funded by US NSF (WiFiUS grant CNS-1702950); no conflicts of interest declared.**
Acknowledges Oura Health for **data access only** (non-financial). **Verified.** Near-perfect RHR
(r²=0.996) and strong HRV (r²=0.980) agreement vs. ECG.
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8808342/

**Kristiansson E, Fridolfsson J, Arvidsson D, Holmång AB, Börjesson M, Andersson-Hall U. 2023.**
"Validation of Oura ring energy expenditure and steps in laboratory and free-living." *BMC Medical
Research Methodology* 23:50 (DOI 10.1186/s12874-023-01868-x; correction at s12874-023-02029-w).
University of Gothenburg / Sahlgrenska Academy. **Funding: Emil and Wera Cornell Foundation, Tore
Nilson Foundation, Erik & Lily Philipson Foundation, Swedish Heart-Lung Foundation, Swedish state
ALF grants (ALFGBG-965249, ALFGBG-720851). No Oura funding identified.** **Corroborated** (funding
list confirmed via secondary citation of the acknowledgments section; the exact "competing
interests" sentence itself wasn't directly read). Lab vs. indirect calorimetry r=0.93; free-living
vs. reference monitors r≥0.76.

**Dial MB, Hollander ME, Vatne EA, Emerson AM, Edwards NA, Hagen JA. 2025.** "Validation of
nocturnal resting heart rate and heart rate variability in consumer wearables." *Physiological
Reports* 13(16):e70527. Ohio State University Human Performance Collaborative / Air Force Research
Laboratory, Wright-Patterson AFB. **The closest thing to a genuine Oura-vs-WHOOP head-to-head in
the literature** — Garmin Fenix 6, Oura Gen3, Oura Gen4, Polar Grit X Pro, and WHOOP 4.0 all worn
simultaneously vs. an ECG chest-strap reference; 13 adults (7 male, 6 female), 536 nights.
**Verified — full text read directly (2026-08-25).** Funding: "financially supported by the Air
Force Research Laboratory (AFRL)." COI statement: "The authors declare that they have no competing
interests." No wearable-vendor funding of any kind.
**Resting HR:** Oura Gen3 CCC=0.97 (MAPE 1.67±1.54%); Oura Gen4 CCC=0.98 (MAPE 1.94±2.51%); WHOOP
4.0 CCC=0.91 "moderate" (MAPE 3.00±2.15%); Polar CCC=0.86 "poor" (MAPE 2.71±2.75%). Garmin Fenix 6
excluded from RHR only — its reported 30-min rolling window carries no timestamp, making
night-to-night alignment with the Polar H10 reference impossible.
**HRV (RMSSD):** Oura Gen4 CCC=0.99 (MAPE 5.96±5.12%); Oura Gen3 CCC=0.97 (MAPE 7.15±5.48%); WHOOP
4.0 CCC=0.94 (MAPE 8.17±10.49%); Garmin Fenix 6 CCC=0.87 (MAPE 10.52±8.63%); Polar Grit X Pro
CCC=0.82 (MAPE 16.32±24.39%). https://physoc.onlinelibrary.wiley.com/doi/10.14814/phy2.70527 ·
PDF: `literature/oura/2025-dial-physiologicalreports-nocturnal-rhr-hrv-validation.pdf`
Full extraction done in `validation-evidence.md` §3a (2026-08-25).

**Stone JD, Ulman HK, Tran K, et al. 2021.** "Assessing the Accuracy of Popular Commercial
Technologies That Measure Resting Heart Rate and Heart Rate Variability." *Frontiers in Sports and
Active Living*. Rockefeller Neuroscience Institute (West Virginia University), Boston University,
NFL Detroit Lions. **Unclear** — funding/COI not retrieved this pass; affiliations suggest
independent origin.

**Fudolig MI, Bloomfield LSP, et al. 2024 (LEMURS study).** "The Two Fundamental Shapes of Sleep
Heart Rate Dynamics and Their Connection to Mental Health in College Students." *Digital
Biomarkers* (Karger). University of Vermont computational social science group. ~600 students,
Oura Gen3, 25,000+ sleep periods. **Authors reported no biomedical financial conflicts; NSF support
indicated in secondary sources but exact grant number not directly read.** **Corroborated.**

**Moshe I, Terhorst Y, Opoku Asare K, et al. 2021.** "Predicting Symptoms of Depression and Anxiety
Using Smartphone and Wearable Data." *Frontiers in Psychiatry* 12:625247. Northwestern, Ulm, Oulu,
Helsinki. **Unclear** — funding/COI statement not directly read; no obvious Oura financial tie
found.

**Hirten RP, Danieletto M, Sanchez-Mayor M, et al. 2025.** "Physiological Data Collected From
Wearable Devices Identify and Predict Inflammatory Bowel Disease Flares." *Gastroenterology*.
Icahn School of Medicine at Mount Sinai. Mixed-device study (Apple Watch, Fitbit, **or** Oura Ring
— not Oura-specific). **Funded by NIDDK K23DK129835 (NIH); no Oura funding identified.**
**Corroborated.**

**Haimovich AD, Lacourciere A, Palihnich K, et al. 2026.** "Feasibility and Acceptability of Oura
Ring Sleep Monitoring in Older Adults Admitted From the Emergency Department: Prospective Cohort
Study." *JMIR Formative Research* 10:e92359. Beth Israel Deaconess Medical Center. **Oura Health
Ltd explicitly named in the COI statement as "not involved in study funding, design, data
collection, analysis, interpretation, manuscript preparation, or the decision to submit."**
**Verified** (the vendor relationship was directly addressed in the read disclosure text, not
merely absent — distinguished from the default no-mention case, which is marked Corroborated
elsewhere in this file). Pilot cohort of 15 ED-boarded older adults; 92.9% of completers wore the
ring ≥75% of the monitored period and 81.8% of exit-survey respondents found it not bothersome, but
median device-estimated sleep was only 4.3 h/24 h. https://pmc.ncbi.nlm.nih.gov/articles/PMC13626187/

**Azadifar S, Sameh A, Nauha L, Kärmeniemi M, Niemelä M, Farrahi V. 2026.** "Severity of depression
and anxiety symptoms is reflected in physiological and behavioral metrics collected from a
consumer-grade wearable ring." *BMC Medicine* 24(1):532. University of Oulu / TU Dortmund. **No
competing interests declared; COI statement does not mention Oura.** **Corroborated.** Northern
Finland Birth Cohort 1986 (n=1,290, two-week Oura wear); moderate-to-severe anxiety and
depression/anxiety symptom groups showed lower REM/deep sleep, higher nocturnal HR, lower RMSSD,
and lower daytime activity than symptom-free participants. https://pmc.ncbi.nlm.nih.gov/articles/PMC13625339/

**Choi A, Gonzalez-Robles C, Xu SS, Krueger MT, Chari A. 2026.** "Monitoring Real-World Function
With an Oura Ring Following Bilateral Subthalamic Nucleus Deep Brain Stimulation for Parkinson's
Disease." *Cureus* 18(8):e115385. University College London / National Hospital for Neurology and
Neurosurgery. **ICMJE disclosure: no financial support or financial relationships declared by any
author; does not mention Oura.** **Corroborated.** Single-patient case report (STN DBS for PD):
Oura "Sleep Score" rose from 45.0 to 53.5 and "Readiness Score" from 67.5 to 71.0 post-DBS, while
"Activity Score" and step count stayed flat despite motor improvement on the MDS-UPDRS Part III — a
dissociation between clinic-measured motor gains and free-living activity.
https://pmc.ncbi.nlm.nih.gov/articles/PMC13617320/

**Dine C, Rekkas Z, Frey BN, Krishnan S, Duarte D, Gomes FA, et al. 2026.** "Wearable-Based
Assessment for Relapse Prediction Following Repetitive Transcranial Magnetic Stimulation for
Depression: Protocol for a Feasibility Study (WARN-D Study)." *JMIR Research Protocols* 15:e89466.
McMaster University / St. Joseph's Healthcare Hamilton. **No author discloses an Oura relationship;
disclosed ties are to AbbVie, Lundbeck, Otsuka, Johnson & Johnson, Alcediag, Eisai, Idorsia, Jazz,
Paladin, ResMed, Eli Lilly — none Oura.** **Corroborated.** Study protocol only (funded Dec 2025,
not yet recruiting at submission): a 25-participant single-arm pilot will use an Oura Ring to test
feasibility (recruitment, adherence, retention, missing data, usability) of wearable monitoring
through rTMS treatment and 6-month follow-up for treatment-resistant depression. No results yet.
https://pmc.ncbi.nlm.nih.gov/articles/PMC13592458/

**Liao J, Chen R, Tian R, Qiu C, Chen W, Yang Z, Hao J, Ge Y, Lin Y, Dunn J, Bergin M, Gilliland FD,
Black M, Kalafut D, Wilson M, Zhang JJ, Chen Z. 2026.** "Wearable measured physiological stress and
activity patterns changes after 2025 Los Angeles wildfire among older adults: findings from a pilot
prospective cohort study." *Environmental Research, Health* (ERH). USC Keck School of Medicine /
Duke University / Cleveland Clinic. N=15 older adults (mean age 73.2), Oura Ring Gen 3 worn
continuously across baseline, the 2025 Eaton Fire, and post-fire periods. **No CoiStatement field
present in the PubMed record; no vendor funding or affiliation evident from the author list.**
**Corroborated** (absence of a disclosed conflict is suggestive, not proof, of independence).
41-minute increase in sedentary time observed during the fire period; six of fifteen participants
received evacuation alerts, associated with measurable changes in sleep heart rate, HRV, sleep
fragmentation, and breath rate. **Added 2026-10-09 from the 2026-09-01 automated scan (branch consolidation).**
https://pubmed.ncbi.nlm.nih.gov/42434202/

**Added 2026-10-09 (open-questions pass): four PSG studies that include Oura, none Oura-funded.**

**Miller DJ, Sargent C, Roach GD. 2022.** "A Validation of Six Wearable Devices for Estimating Sleep,
Heart Rate and Heart Rate Variability in Healthy Adults." *Sensors* 22(16):6317, PMID 36016077,
doi:10.3390/s22166317. CQUniversity. N=53, one lab night, Oura Ring Gen2 alongside WHOOP 3.0, Apple
Watch S6, Garmin FR245, Polar Vantage V and Somfit. Oura four-stage κ 0.43 (WHOOP 0.44), two-state κ
0.51 (best of six). Funded by the Australian Institute of Sport; the authors' lab receives WHOOP
funding and equipment. **Tier C for Oura (no Oura relationship), but run by a WHOOP-supported lab.
Verified** (full text read). Full table in `validation-evidence.md` §3c.
PDF: `literature/whoop/2022-miller-sensors-six-wearables-sleep-hr-hrv-validation.pdf`

**Grandner MA, Bromberg Z, Hadley A, Morrell Z, Graf A, Hutchison S, Freckleton D. 2023.**
"Performance of a multisensor smart ring to evaluate sleep: in-lab and home-based evaluation of
generalized and personalized algorithms." *Sleep* 46(1):zsac152, PMID 35767600. University of Arizona
and Happy Health, Inc. Oura V2 and WHOOP 3.0 as comparators to the Happy Ring against one PSG night:
sleep/wake accuracy Oura 0.88, WHOOP 0.86. "ZB, AH, ZM, AG, and DF are employees of Happy Health,
Inc."; Grandner reports Fitbit consulting among others. **Tier C for Oura, but authored by a competing
ring maker.** Tier: **Verified** (author affiliations in the PubMed record; NIH grant R01 MD011600
also listed). Device figures: **Reported**, corrected 2026-10-10 from "Verified (full text read via
PMC)": the PDF was never obtained (PMC/OUP bot checks), the full text is not open access in Europe PMC,
and the abstract gives Happy Ring figures only. Published online 29 June 2022.
https://pmc.ncbi.nlm.nih.gov/articles/PMC13396806/

**Lee T, Cho Y, Cha KS, et al. (incl. Kushida CA, Yoon IY, Kim JW). 2023.** "Accuracy of 11 Wearable,
Nearable, and Airable Consumer Sleep Trackers: Prospective Multicenter Validation Study." *JMIR mHealth
uHealth* 11:e50983, PMID 37917155. Asleep Co. with Seoul National University Bundang Hospital and
Stanford. N=75, Oura Ring 3 four-stage κ 0.35 (macro F1 0.52), below Galaxy Watch 5 (0.42), Fitbit
Sense 2 (0.42) and Pixel Watch (0.40), above Apple Watch 8 (0.30). COI: "Authors affiliated with Asleep
and CAK hold stocks or stock options in Asleep" (Asleep makes the SleepRoutine app, the best performer).
**Tier C for Oura, competitor-authored. Verified** (tables read via Europe PMC). PDF not obtained (JMIR
bot check). https://pmc.ncbi.nlm.nih.gov/articles/PMC10654909/

**Searles ME, Licata A, Cucinotta M, Kainec K, Spencer RMC. 2026.** "Performance evaluation of
consumer sleep-tracking wearables and nearables in healthy young and older adults." *SLEEP Advances*
7(1):zpag006, PMID 41768372. University of Massachusetts Amherst. Oura Gen3 (app 2.8.41), Fitbit Sense
2, Withings Sleep Mat, SleepScore Max vs PSG in 13 young and 19 older adults. In older adults Oura
underestimated TST by 75.5 min (p<0.0001) and overestimated deep sleep by 71.5 min. NIH NIA P30
AG073107; "Financial disclosure: None." Skin tone explicitly "not measured". **Tier C. Verified** (full
text read). PDF not obtained (OUP bot check). https://pmc.ncbi.nlm.nih.gov/articles/PMC12936866/

**Added 2026-10-12.** Li Y, Wang H, Chandrashekhar R, Major J, Chandna M, Bodison SC. 2026.
"Feasibility and Methodological Consideration of Using Wearable Devices to Examine the Relationship
Between Sleep and Balance: Case Report With 2 College Students." *JMIR Formative Research*,
PMID 42854191. University of Florida Department of Occupational Therapy. Case report (PubMed
PublicationType "Case Reports" + "Journal Article"), N=2, 4 months; Participant 1 wore an Apple Watch
Series 5 and an Oura ring, Participant 2 a Fitbit Charge 5 and an Oura ring (also cross-filed under
Apple Watch Tier C below; Fitbit is out of this file's three-device scope). CoiStatement: "Conflicts
of Interest: None declared." **Tier C. Corroborated** (no vendor named in the COI statement, which is
suggestive of independence, not proof). **Category: Use-case (feasibility-focused; genuinely
ambiguous against Validation, defaulted per this file's convention).** Primary outcome was feasibility
of continuous multi-device collection itself, not device accuracy: missing-data rates started as high
as 75.2% and fell to 14.1%/20.3% (wrist devices), 9.4%/25% (Oura rings), 0%/6.25% (sleep diaries)
after structured weekly check-ins were introduced. https://pubmed.ncbi.nlm.nih.gov/42854191/

## Oura — systematic reviews (as discovery mechanism, and classified in their own right)

**Khan et al. 2025, *OTO Open*.** "The Oura Ring Versus Medical-Grade Sleep Studies: A Systematic
Review and Meta-Analysis." 6 studies, n=388 pooled, 2019–2024. **Updated 2026-10-10:** the Europe
PMC full text (PMC12602993) states "Competing interests None" and "Funding source None". **Verified**,
no disclosed industry funding. Reference list not yet extracted.

**Gong EJ, Bang CS, Lee JJ, Baik GH. 2025.** "Smart Ring in Clinical Medicine: A Systematic
Review." *Biomimetics* (MDPI) — **corrected 2026-08-24; the source venue was previously misstated as
*Diagnostics*, confirmed via direct PDF read during the literature-library retrofit, same paper** —
/ JMIR preprint #83508. Hallym University College of Medicine, South
Korea. **Funded by the Bio & Medical Technology Development Program, National Research Foundation
of Korea (government grant RS-2023-00223501). No industry funding; authors declared none.**
**Verified** (fetched and read in full). 77 of 107 included studies (72%) involved Oura specifically
— confirms Oura dominates the smart-ring evidence base by volume. **65% of the 107 underlying
studies had moderate-to-high risk of bias** — an important caveat for the field generally, not
specific to any one tier. Pooled figures: HR r²=0.996, HRV r²=0.980, sleep detection sensitivity
93–96%, sleep-stage sensitivity 94.4–94.5% (but staging *accuracy* only ~53.18%); notable
clinical-prediction citations matching entries above: COVID-19 detection 2.75 days pre-symptom
(82% sensitivity — TemPredict), IBD flare prediction 7 weeks early (72% accuracy — Hirten et al.),
bipolar episode detection 3–7 days early (79% sensitivity).

## Oura's own self-published research list

Fetched directly: **ouraring.com/science-and-research** and **ouraring.com/blog/oura-in-research/**.
The science-and-research page currently states **"130+ peer-reviewed publications"** (not the
"170+" figure seen in earlier casual searches — worth re-checking which page or date carried that
number, as it may be stale or page-specific). **Rechecked 2026-10-09:** the live page says "130+
peer-reviewed publications" and "Powering research published in over 130 peer-reviewed publications".
Wayback snapshots show "over 130" from November 2025 through September 2026 and no count at all in the
July 2024, December 2024 and June 2025 snapshots. "170+" does not appear on this page in any snapshot
checked; its source remains unidentified. **Verified** (live page), **Corroborated** (history). The blog page lists roughly 100 studies by year
(2016–2025) with no running total stated on that page itself.

**Composition, on a title-level skim (not individually tier-verified):** the large majority are
genuinely independent academic/clinical groups (Harvard/Brigham, UCSF/UCSD, NUS, Ohio State,
Vermont, assorted hospital and sports-science groups) using Oura as a data-collection instrument —
i.e. Tier C by authorship, even while Oura promotes the list. A smaller number are explicitly
Oura-authored/partnered. A meaningful subset trace back to the Oura-sponsored TemPredict
infrastructure (Tier B). **This corroborates that Oura's "170+/130+ studies" marketing claim is not
mostly Tier A/B** — but a non-trivial fraction is, and the list itself should not be read as neutral
without per-paper sorting.

**Added 2026-10-26 (weekly scan).** Barnard J, Kelly M, Lastella M, Roberts S, Di Giovanni A, Guy J,
Condo D. 2026. "The Sleep and Diet of Elite Female Australian Rules Football Athletes Differ With
Age and Season Phase." *European Journal of Sport Science* 26(11):e70274, DOI 10.1002/ejsc.70274,
PMID 42904819. Deakin University / Central Queensland University (Australia). **"The authors declare
no conflicts of interest."** No Oura affiliation or funding named. **Tier C. Corroborated** (absence
of a disclosed conflict is suggestive, not proof, of independence). N=22 elite AFLW athletes, 10
nights (5 pre-season, 5 in-season); sleep measured via Oura ring alongside self-reported food
diaries; in-season protein and fat intake were lower than pre-season, sleep duration/timing did not
differ by season phase, and each additional year of age was associated with 8 min less sleep.
https://pmc.ncbi.nlm.nih.gov/articles/PMC13685518/

## Oura — confirmed evidence gaps

- **No independent peer-reviewed SpO2 validation study found for Oura** — only Oura's own blog
  claims of accuracy improvement Gen3→Gen4. **Rechecked 2026-10-09** via PubMed and Europe PMC full
  text (reference-oximeter terms): still none. Same for skin temperature against a reference
  thermometer. Search strings in `validation-evidence.md` §6c.
- **No independent validation of Ring 4 or Ring 5 sleep staging.** Gen4's only independent data is
  nocturnal resting HR/HRV (Dial et al. 2025, no difference from Gen3). Rechecked 2026-10-09.
- **Readiness/recovery score**: no independent validation found. The one external attempt located
  (a regression-based reverse-engineering of the score) explicitly notes the difficulty caused by
  the algorithm not being published — itself a notable finding, not just an absence of evidence.

---

# WHOOP

## Tier A — WHOOP-employee-authored

**Holmes KE, Kim J, Fielding F, Zeitzer JM, von Hippel W. 2026.** "Four core circadian behaviors
that improve cardiorespiratory fitness through consistent sleep." *Sleep* 49(2):zsaf318. Holmes,
Kim, Fielding: WHOOP Inc. Zeitzer: Stanford Psychiatry. von Hippel: Research with Impact (external).
N=38,838 WHOOP members, 31-day "Core Four Challenge." **Verified.**
https://academic.oup.com/sleep/article/49/2/zsaf318/8279894

**Presby D, Jasinski S, Capodilupo E, Holmes KE, von Hippel W, Grosicki GJ, Lee V. 2025.**
"Inter- and Intrapersonal Associations Between Physiology and Mental Health: A Longitudinal Study
Using Wearables and Mental Health Surveys." *Journal of Medical Internet Research* 27:e64955, DOI
10.2196/64955. Title and DOI completed 2026-10-10 against Crossref.
Capodilupo, Holmes: WHOOP Inc. N=181,574 WHOOP members. **Verified.**
https://www.jmir.org/2025/1/e64955

**Jasinski S, Presby D, Grosicki GJ, Capodilupo E, Lee V. 2024.** "A Novel method for quantifying
fluctuations in wearable derived daily cardiovascular parameters across the menstrual cycle."
*npj Digital Medicine* 7:373. **Verified — explicit COI text found:** "D.M.P., S.R.J., V.H.L., G.J.G
and E.R.C. are employed by the commercial company WHOOP Inc." Jasinski, Capodilupo, and Lee are
WHOOP Inc. Data Science & Research; Presby was Univ. of Lausanne/SIB at time of authorship (later
moved to WHOOP per the alcohol paper below); Grosicki: Georgia Southern. WHOOP has also filed a
related patent (US application 18/463,096, "Coaching based on reproductive phases") building on
this work — a notable commercial follow-on worth flagging. >11,000 members, 45,000 cycles.
https://www.nature.com/articles/s41746-024-01394-0

**Gonzalez A, O'Day JJ, Johnson SC, Kim J, Jasinski SR, Holmes KE, Delp SL, Hicks JL. 2026.** "The
menstrual cycle through the lens of a wearable device: insights into physiology, sleep, and cycle
variability." *npj Digital Medicine* 9:633 (DOI 10.1038/s41746-026-02799-9); bioRxiv preprint 2025,
10.1101/2025.09.11.675620. **Corrected 2026-08-24 (literature-library retrofit) — Verified via direct
PDF read:** a prior pass could not confirm authorship (Nature login wall, PubMed cookie wall,
EuropePMC nav-only all blocked) and explicitly flagged an AI-generated secondary summary naming
"Alexander Gonzalez and Johanna J. O'Day" as lead authors as **unverified and not to be trusted**,
downgrading the paper to Unclear. The open-access bioRxiv preprint (CC BY-NC-ND 4.0) has now been
read directly and **confirms that summary was correct**: Gonzalez and O'Day (Stanford Wu Tsai Human
Performance Alliance) are lead/corresponding authors, with Johnson (Stanford) plus Kim, Jasinski, and
Holmes (WHOOP Inc.) as co-authors. **Restored to Tier A** — mixed Stanford/WHOOP authorship with
substantive WHOOP co-authorship, not pure independent. PDF: `../literature/whoop/2026-gonzalez-oday-npjdigitalmedicine-menstrual-cycle-lens-wearable.pdf`.
**Final published version checked 2026-10-09:** *npj Digital Medicine* 9:633, published 2026-05-25,
PMID 42185632, PMC13482339 (Crossref and nature.com). Same eight authors as the preprint. Competing
interests: "Authors J.K., S.J., and K.H. hold shares in WHOOP, Inc. and were employees at the time of
data analysis and writing." Funding: Wu Tsai Human Performance Alliance at Stanford and the Joe and
Clara Tsai Foundation. Data held by WHOOP. **Tier A, Verified** against the published version.

**Grosicki GJ, Robinson A, Joyner M, Carter S, von Hippel W, Presby D, Fielding F, Bigalke J, Kim J,
Chapman C, Holmes KE. 2026.** "Real-world effects of alcohol on heart rate, sleep, and physical
activity by age and sex." *PLOS Digital Health*. 7 of 11 authors are WHOOP Inc. Department of
Performance Science/Research staff (Grosicki, von Hippel, Presby, Fielding, Kim, Chapman, Holmes);
independent co-authors from Indiana Univ., Mayo Clinic, Baylor. **Verified: "This work was supported
by WHOOP, Inc. through salary support provided to authors GJG, WvH, DMP, FF, JK, CC, and KEH."**
7 authors hold WHOOP stock options. ~21,000 members, 5M+ person-days.
https://journals.plos.org/digitalhealth/article?id=10.1371%2Fjournal.pdig.0001284

**Miller DJ, Capodilupo JV, Lastella M, Sargent C, Roach GD, Lee VH, Capodilupo ER. 2020.**
"Analyzing changes in respiratory rate to predict the risk of COVID-19 infection." *PLOS ONE*
15(12):e0243693. **Verified — explicit funding text:** "There was no specific funding provided for
this project. However, ERC, JVC and VHL are employees of Whoop Inc. In addition, Whoop Inc is
sponsoring the employment of DJM's position at CQUniversity." (John V. Capodilupo, Victoria H. Lee,
Emily R. Capodilupo: WHOOP Inc.; Dean J. Miller, Michele Lastella, Gregory D. Roach: CQU/Appleton
Institute — Miller's position itself WHOOP-sponsored.) 271 participants; algorithm flagged 20% of
COVID-positive individuals 2 days pre-symptom, 80% by symptom-day 3.
https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0243693

**"Alcohol Use Trajectories During the First 72 Weeks of WHOOP Wearable Platform Membership."**
JMIR mHealth Research Letter, 2026, PMC13119388. Author list not confirmed — PMC CAPTCHA blocked
direct verification. WHOOP's own press center attributes it to WHOOP research. ~30,000 members,
72-week longitudinal, 25.2% relative decline in drinking probability. **Corroborated, not
Verified** — recommend re-fetch via a different access route.

**"Travel, recovery and performance" narrative review.** *Sports Medicine* (2026), DOI
10.1007/s40279-026-02455-y. WHOOP's press release states it is "co-authored by WHOOP research
scientists alongside collaborators from UCSF, UCLA, Ontario Tech University, Monash University, and
Brigham and Women's Hospital." **Corroborated** (press-center claim), individual names not
independently verified — Springer login wall blocked direct access.

**"Tobacco Use and Behavior Change" study** referenced on WHOOP's press center (12,678 members,
72-week decline in tobacco use 55%→27%). **No peer-reviewed journal citation or DOI located** —
appears to be a WHOOP-internal blog/press release without a traceable publication. Flagged as
press-release-only; exclude from citation as a "published study" until a journal reference surfaces.

## Tier B — WHOOP-funded/affiliated, independent-author-led

**Berryhill S, Morton CJ, Dean A, et al. (senior investigator Parthasarathy S). 2020.** "Effect of
wearables on sleep in healthy individuals: a randomized crossover trial and validation study."
*Journal of Clinical Sleep Medicine* 16(5):775–783. University of Arizona Health Sciences Center for
Sleep and Circadian Sciences. **Funded by a grant to the University of Arizona from WHOOP Inc.;
authors reported no personal conflicts of interest.** **Verified.**
https://jcsm.aasm.org/doi/10.5664/jcsm.8356

**Bellenger CR, Miller D, Halson SL, Roach GD, Maclennan M, Sargent C. 2022.** (Author initials
corrected 2026-10-10 against Crossref: "Miller, Dean" and "Maclennan, Michael".) "Evaluating the
Typical Day-to-Day Variability of WHOOP-Derived Heart Rate Variability in Olympic Water Polo
Athletes." *Sensors* 22(18):6723. University of South Australia (ARENA), CQU Appleton Institute,
Australian Catholic University, Water Polo Australia. Same author cluster as the WHOOP-sponsored
Miller CQU position established above. ~~Corroborated, funding statement itself Unclear~~ **Tier B,
Verified 2026-10-09** from the stored PDF: "This study was supported by the Australian Institute of
Sport" (funding acquisition by the Water Polo Australia author), and COI: Roach, Sargent and Miller
"are members of a research group at Central Queensland University (i.e., The Sleep Lab @ Appleton
Institute...) that receives support for research (i.e., funding, equipment) from WHOOP Inc. However,
WHOOP was not involved in the design, conduct or reporting of this study." 11 elite male water polo
players, 16 weeks pre-Tokyo Olympics, WHOOP 3.0.

**Miller DJ, Lastella M, Scanlan AT, Bellenger CR, Halson SL, Roach GD, Sargent C. 2020.** "A
validation study of the WHOOP strap against polysomnography to assess sleep." *Journal of Sports
Sciences* 38(22):2631–2636, PMID 32713257. All-CQU/Australian author list, no WHOOP employees
visible. **Unclear** — funding/COI text not retrievable (Tandfonline 403). Given the same author
cluster's demonstrated WHOOP-sponsorship pattern elsewhere, flag as likely Tier B pending direct
confirmation; do not assume independence. **Rechecked 2026-10-09:** Tandfonline still blocks with a
bot check, and the CQU repository record (figshare 13411934) is metadata only. Crossref's
publisher-deposited funder metadata lists the Australian Research Council (DP160104909) and the
Australian Institute of Sport, no WHOOP. The abstract states that WHOOP "sleeps were scored by the
company based on proprietary algorithms". The COI statement is still unread. **Funding Corroborated
(non-WHOOP); COI Unclear; tier stays likely B.**

**Miller DJ, Sargent C, Roach GD. 2022.** "A Validation of Six Wearable Devices for Estimating Sleep,
Heart Rate and Heart Rate Variability in Healthy Adults." *Sensors* 22(16):6317, PMID 36016077. Added
2026-10-09. Funded by the Australian Institute of Sport; COI discloses that the authors' CQU Sleep Lab
receives WHOOP funding and equipment; WHOOP staff (blinded to PSG) supplied WHOOP sleep epochs and R-R
data. WHOOP 3.0 four-stage κ 0.44, tied with Oura Gen2 (0.43); HR and RMSSD ICC 0.99 against ECG.
**Tier B, Verified** (full text read). The first located PSG study to report four-stage agreement for
WHOOP and Oura in one protocol; Grandner et al. (*Sleep*, online 29 June 2022, before Miller's 22 August
2022) also included both but reported sleep/wake only. Corrected 2026-10-10. The authors caution that
the analyses compare each device with PSG "rather than a comparison between devices", and WHOOP's
epochs (30 s, supplied by WHOOP staff) and Oura's (5 min, from the app) were obtained differently.
Full table in `validation-evidence.md` §3c.

## Tier C — Fully independent

**Bellenger CR, Miller DJ, Halson SL, Roach GD, Sargent C. 2021 (correction 2022).** "Wrist-Based
Photoplethysmography Assessment of Heart Rate and Heart Rate Variability: Validation of WHOOP."
*Sensors* 21(10):3571. CQUniversity, **funded by the Australian Institute of Sport** (a national
sport-science body, not WHOOP). WHOOP 2.0 vs. ECG, 15 sessions, Oct–Dec 2018. **Verified.** Widely
cited by WHOOP as "99.7% HR / 99% HRV accuracy" — an accurate topline read of this paper, but the
device tested (WHOOP 2.0) is two hardware generations behind WHOOP 4.0/5.0.
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8160717/

**Miller DJ, et al. 2021.** "A Validation Study of a Commercial Wearable Device to Automatically
Detect and Estimate Sleep." *Biosensors* 11(6):185. CQUniversity / University of South Australia /
Australian Catholic University. Data collection independent of WHOOP; the paper discloses that
co-author Dean Miller's CQUniversity position **became WHOOP-sponsored after data collection
concluded** — a forward-looking COI, not a funding source for this specific study. **Verified.**
Re-read 2026-10-10 (Europe PMC full text): the statement says the sponsorship "represents a potential
conflict of interest for Dean Miller and for the co-authors who work in the same research group",
naming Roach, Sargent and Lastella; funding was ARC DP160104909 and the Australian Institute of Sport.
Placement in Tier C is a judgement call: by the standard applied to Bellenger 2022 (Tier B, lab
receives WHOOP support at publication) this paper is borderline Tier B.
64% four-stage agreement, κ=0.47. https://pmc.ncbi.nlm.nih.gov/articles/PMC8226553/

**Schyvens A, et al. 2025.** *SLEEP Advances* 6(2):zpaf021. Six devices incl. WHOOP 4.0 vs PSG.
**Funded by Flanders Innovation & Entrepreneurship (VLAIO); authors declare no conflicts.**
**Verified.** Full extraction in `validation-evidence.md` §1. WHOOP κ=0.37 ("fair"), 4th of 6.

**Dial MB, et al. 2025.** *Physiological Reports* 13:e70527. See Oura Tier C above — same paper,
includes WHOOP 4.0. **Verified — full text read directly (2026-08-25);** AFRL-funded, no vendor
funding, no competing interests declared. WHOOP HR: CCC=0.91 "moderate" (MAPE 3.00±2.15%). WHOOP
HRV: CCC=0.94 (MAPE 8.17±10.49%), behind both Oura generations, ahead of Garmin and Polar.

**Lundstrom EA, De Souza MJ, Koltun KJ, Strock NCA, Canil HN, Williams NI. 2024.** "Wearable technology
metrics are associated with energy deficiency and psychological stress in elite swimmers."
*International Journal of Sports Science & Coaching* 19(4):1578-1587 (online 2023), DOI
10.1177/17479541231206424. Author initials, volume and DOI corrected 2026-10-10 against Crossref. Penn State Kinesiology. Examined WHOOP
HRV/RHR/Strain/Recovery vs. lab RMR, T3 thyroid, RESTQ stress in Division 1 swimmers. **Notable
context, not necessarily disqualifying:** Penn State Athletics has an institutional WHOOP-Unite
equipment/software partnership (announced 2022) — separate from a research-funding relationship,
but worth flagging. **Unclear** — the paper's actual COI/funding section wasn't retrieved.

**Khodr R, Kamal L, Minerbi A, Gupta G. 2024.** "Accuracy, Utility and Applicability of the WHOOP
Wearable Monitoring Device in Health, Wellness and Performance — a systematic review." *medRxiv*
2024.01.04.24300784 (preprint; final publication status not confirmed). Univ. of Ottawa,
Institute for Pain Medicine (Rambam/Technion). No WHOOP-affiliated co-authors found.
**Corroborated, not Verified** — secondary sources report "no competing interests declared," but
the actual medRxiv disclosure text was blocked (403 on HTML and PDF).

**Obtained 2026-08-24** (literature-library retry) via Semantic Scholar's canonical medRxiv PDF URL,
which bypassed the earlier 403. The full text does not contain a visible, extractable competing-
interests/disclosure section, so this remains **Corroborated, not Verified** even with the PDF in
hand — the secondary-source COI claim still cannot be directly confirmed from the primary document
itself. See `../literature/whoop/2024-khodr-medrxiv-whoop-systematic-review.pdf`. This review's
reference list remains a good discovery mechanism for additional WHOOP papers.

**Grandner MA, et al. 2023.** *Sleep* 46(1):zsac152. Added 2026-10-09. Happy Ring development study
with WHOOP 3.0 and Oura V2 as comparators against PSG; WHOOP sleep/wake accuracy 0.86, specificity
0.54 (**Reported**; full text not read, corrected 2026-10-10). Five of seven authors affiliated with
Happy Health (PubMed). **Tier C for WHOOP, competitor-authored; tier Verified.** See Oura Tier C entry.

**Harms NR. 2018.** University of Nebraska-Lincoln dissertation (ProQuest/ERIC ED595664), "The
Impact of Whoop Technology on Sleep, Recovery, and Performance in NAIA Baseball Players." **Not
peer-reviewed** (thesis), 10 participants, no significant results. Low evidentiary weight — grey
literature, not a journal article; included here only for completeness.

## WHOOP — findings needing individual follow-up (surfaced, not yet verified)

- **Kimia Heydari, Elizabeth J. Enichen, Ben Li, Joseph C. Kvedar (all Harvard Medical School).**
  "A new metric to understand the association between heart rate variability and menstrual
  regularity." *npj Digital Medicine* 8:123 (2025), PMID 39994422. A short **commentary/perspective
  piece responding to the Jasinski et al. Tier-A cardiovascular-amplitude paper**, not primary data.
  No WHOOP employees as authors. **Tier C (independent commentary), Corroborated.**
- Støve & Hansen 2023 — WHOOP Band 3.0 vs. Apple Watch Series 6 HR accuracy during resistance
  exercise. Found only via secondary summary; source not directly fetched. Affiliations/funding
  unknown.
- A possible additional 2025 five-device nocturnal RHR/HRV study incl. WHOOP 4.0 vs ECG, distinct
  from Dial et al. — surfaced only in an AI-search summary. **Possible duplicate of Dial et al.;
  needs disambiguation before treating as a separate source.**
- "Readiness, recovery, and strain: an evaluation of composite health scores in consumer
  wearables." De Gruyter, DOI 10.1515/teb-2025-0001. Surfaced but not fetched — potentially a
  useful independent review of WHOOP's Recovery-score methodology.
- A living systematic review on wearable HRV across the menstrual cycle (Springer, DOI
  10.1007/s40279-025-02388-y) repeatedly surfaced in search and likely includes WHOOP data — not
  yet fetched for authorship/tier.

**Added 2026-10-26 (weekly scan).** Paterson KGP, Griest TD, Angeles E, Fenner SP, Eberhardt HK,
McKay CR, Helms KLW, Calderon A, Vukovich MD, Ormsbee MJ. 2026. "Pre-sleep milk-derived proteins do
not impair sleep or recovery in elite female athletes." *Journal of the International Society of
Sports Nutrition* 23(1), DOI 10.1080/15502783.2026.2746899, PMID 42897977. Florida State University
Institute of Sports Sciences & Medicine. **COI statement: "MJO serves as a non-paid member of the
International Protein Board."** Does not name WHOOP Inc. as funder/employer/consultant. **Tier C.
Corroborated** (absence of a disclosed WHOOP-specific conflict is suggestive, not proof, of
independence). Randomized, double-blinded, placebo-controlled crossover trial; 25 NCAA Division I
female athletes recruited, 21 analyzed; three consecutive nights each of casein, ALA, or
carbohydrate pre-sleep feeding vs. placebo. Objective sleep/recovery outcomes (TST, SOL, SE, RHR,
HRV) obtained from the **WHOOP 4.0 device**; no significant treatment effects were observed on any
outcome. https://pmc.ncbi.nlm.nih.gov/articles/PMC13686207/

## WHOOP — confirmed evidence gaps

- **No independent peer-reviewed SpO2 validation study found** — only WHOOP's own support-page
  description of sampling methodology (30-sec samples roughly every 20 min during sleep, with
  signal-quality gating).
- **No independent peer-reviewed skin/body-temperature validation study found** — same gap as SpO2.
  **Both rechecked 2026-10-09** (PubMed and Europe PMC full text, search strings in
  `validation-evidence.md` §6c): still none.
- **No WHOOP 5.0/MG validation of any kind found** (PubMed and Europe PMC including preprints,
  2026-10-09). Every independent result located is on WHOOP 2.0 to 4.0.
- **No WHOOP-specific peer-reviewed military/tactical-athlete study found**, despite WHOOP's
  commercial military/first-responder marketing and conference presence (e.g. a NATO tactical-
  athlete conference). A genuine gap between WHOOP's marketing footprint and its published evidence.

---

# APPLE WATCH

## Tier A — Apple-employee-authored / Apple-sponsored flagship studies

**Perez MV, Mahaffey KW, Hedlin H, et al. (Apple Heart Study Investigators). 2019.** "Large-Scale
Assessment of a Smartwatch to Identify Atrial Fibrillation." *N Engl J Med* 381:1909–1917. Stanford
(Perez, Mahaffey, Turakhia — PIs) plus named Apple co-authors (Ferris T, Balasubramanian V, Rajmane
A, Cheung L, Hung G, Lee J, Nag D, Gummidipundi SE, Hills MT, Desai S, Desai M) alongside Stanford/
AHA statisticians. **Verified: "the study was sponsored by Apple."** Individual COI: Perez reports
grants/personal fees from Apple; Mahaffey reports grants from AHA, Apple, and multiple pharma/device
companies; Turakhia reports grants from Apple, AHA, FDA, and personal fees from device/pharma
companies. 419,297 participants; 0.52% received irregular-pulse notifications; of those, 34% had AF
on subsequent ECG patch; 84% concordance with AF. https://www.nejm.org/doi/full/10.1056/NEJMoa1901183
· protocol: https://pubmed.ncbi.nlm.nih.gov/30392584/ · ClinicalTrials.gov NCT03335800

**Confirmed genuinely paywalled 2026-08-24** (literature-library retry): checked directly against
NCBI's own OA web service (`oa.fcgi?id=PMC8112605`), which returned `idIsNotOpenAccess`. Earlier
HTTP 500/CAPTCHA symptoms on this PMC deposit were downstream of this underlying non-OA status, not
a retrieval-infrastructure bug — no PDF obtained, and none should be expected without institutional
NEJM access.

**Mahalingaiah S, Fruh V, Rodriguez E, et al. 2022.** "Design and methods of the Apple Women's
Health Study: a digital longitudinal cohort study." *Am J Obstet Gynecol*. Harvard T.H. Chan School
of Public Health (lead) + NIEHS/NIH (Jukic). **Corroborated** — three-way named partnership (Apple +
Harvard Chan + NIEHS) per NIH's own press release; whether a named Apple employee appears as a paper
co-author specifically was **not confirmed** (PMC fetch blocked by a bot check).
https://pmc.ncbi.nlm.nih.gov/articles/PMC10518829/ ·
NIH release: https://www.nih.gov/news-events/news-releases/nih-partners-apple-harvard-university-womens-health-study

**Obtained 2026-08-24** (literature-library retry): NCBI's OA web service confirmed a genuine CC
BY-NC-ND open-access record; the PDF URL itself sat behind a JS bot-detection interstitial that a
real browser session cleared, yielding the actual PDF. See
`../literature/apple-watch/2022-mahalingaiah-ajog-apple-womens-health-study-design.pdf`.

**Apple Heart and Movement Study** (with American Heart Association + Brigham and Women's
Hospital). Companion methods paper: "Understanding activity and physiology at scale: The Apple
Heart & Movement Study," *npj Digital Medicine* (2024). Enrollment began Nov 2019 targeting 500,000
participants; data collection closed end of Feb 2025; data access limited to Apple, Brigham and
Women's, AHA, and the Research Studies Support Center — consistent with Tier A (Apple as
co-sponsor/data-holder). https://www.nature.com/articles/s41746-024-01187-5 ·
https://appleheartandmovementstudy.bwh.harvard.edu/

**Apple's internal VO2max validation white paper.** "Using Apple Watch to Estimate Cardio Fitness
with VO2 max" (Apple, May 2021). 534 development + 221 validation participants (755 total);
reported accuracy ~1.2–1.4 mL/kg/min (~4%), ICC ~0.86–0.89. Self-published by Apple, not a
peer-reviewed journal article with individually named/verifiable authors — **Reported**, not
independently verified; the PDF was not machine-readable via fetch in this pass, so figures above
are drawn from secondary summaries, not the primary text directly.
https://www.apple.com/healthcare/docs/site/Using_Apple_Watch_to_Estimate_Cardio_Fitness_with_VO2_max.pdf

**Apple Inc. 2025.** "Hypertension Notification Feature on Apple Watch" (white paper, September 2025)
and FDA 510(k) summary K250507 (cleared 2025-09-11). Added 2026-10-09. Pivotal study: 2,229 enrolled,
1,863 analysed, 30 days against a home cuff; sensitivity 41.2% (95% CI 37.2 to 45.3), specificity
92.3% (90.6 to 93.7); Fitzpatrick I-IV vs V-VI subgroup reported. Not a peer-reviewed paper; no journal
publication of the pivotal study located in PubMed or Europe PMC as of 2026-10-09. **Tier A, Verified**
(both documents read). https://www.apple.com/health/pdf/Hypertension_Notifications_Validation_Paper_September_2025.pdf ·
https://www.accessdata.fda.gov/cdrh_docs/pdf25/K250507.pdf · PDF:
`literature/apple-watch/2025-apple-whitepaper-hypertension-notifications.pdf`

## Tier B — Apple-funded/affiliated but independent authors, or run via a named Apple-partner institution

**Cohen JB, Brady TM, Juraschek SP, Picone DS, Yang E, Schutte AE. 2026.** "Apple Watch for
Hypertension Screening." *Hypertension* 83(2):e26031, PMID 41564145. Added 2026-10-09. A critique of
the hypertension feature's validation (low sensitivity, predicate device was an ECG-based cardiomyopathy
notifier, no ISO/IEEE cuffless protocol). Classified Tier B by this file's rule only because two
authors disclose Apple stock (Juraschek <$10k, Yang >$10k); the paper is critical of Apple, another
example of cross-cutting finding 1. **Verified** (COI and text read via PMC12826266).

**Apple Hearing Study** — University of Michigan partnership (with WHO). Collects headphone/
environmental sound exposure via iPhone + Apple Watch Noise app; examines cardiovascular/stress
links to long-term sound exposure. **Corroborated** (named partnership); individual peer-reviewed
outputs not identified this pass. https://sph.umich.edu/applehearingstudy

**2025 Apple Health Study** (holistic mental/physical health), led by Brigham and Women's Hospital,
launched via the Research app Feb 2025. **Corroborated** (secondary sources only); no individual
paper yet identified. https://www.apple.com/newsroom/2025/02/new-holistic-apple-health-study-launches-today-in-the-research-app/

## Tier C — Fully independent

**Added 2026-10-09:** Walzel S, Mikus R, Rafl-Huttova V, Rozanek M, Bachman TE, Rafl J. 2023.
"Evaluation of Leading Smartwatches for the Detection of Hypoxemia: Comparison to Reference Oximeter."
*Sensors* 23(22):9164, PMID 38005550. Czech Technical University grants; no conflicts. Apple Watch 8,
Galaxy Watch 5 and Withings ScanWatch vs Masimo Radical-7 during induced hypoxemia (N=18); all met the
≤4% Arms limit, Apple Watch 8 lowest bias. **Verified** (funding/COI read in the PDF). PDF:
`literature/apple-watch/2023-walzel-sensors-smartwatches-hypoxemia-reference-oximeter.pdf`. Jiang Y et
al. 2026, *JMIR Form Res* 10:e85253, PMID 41894520 (Duke): Apple Watch Series 7 vs arterial blood gas
under controlled hypoxia, Arms 5.82% below 88% SaO2, overestimation; senior author consults for Samsung
and sits on a Google advisory board (competitors, not Apple). **Corroborated** (abstract). Cohen JB,
Addo DK, et al. 2026, *JAMA* 335(11):1001, PMID 41661624: population model of the hypertension
notification feature in undiagnosed US adults; NIH/NHMRC funding, no Apple disclosures. **Corroborated**
(abstract and COI).

**Schyvens A, et al. 2025**, *SLEEP Advances* — already in this KB (Antwerp/VLAIO). Apple Watch
Series 8 had the best overall kappa (0.53) of six devices, but ~15/35 device failures (highest
data-loss rate in that study).

**Robbins R, et al. 2024**, *Sensors* — already in this KB (Brigham/Oura-funded). Note: this study
is Tier B **for Oura**, not for Apple — Apple had no funding role or COI identified regarding the
Apple Watch arm specifically; treat as arms-length for Apple's purposes even though the study
overall is Oura-sponsored. Apple Watch S8 had the best REM sensitivity (82.6%) of the three devices
but the worst deep-sleep bias (light +45 min, deep −43 min, both p<0.001).

**Jaworski D, Park EJ. 2023.** "Apple Watch Sleep and Physiological Tracking Compared to Clinically
Validated Actigraphy, Ballistocardiography and Polysomnography." IEEE EMBC. Simon Fraser University
/ WearTech Labs (Canada). **Unclear** — funding/COI not accessible (IEEE paywalled); affiliation
shows no Apple connection. Apple Watch deep-sleep detection ~62% accurate, frequently confused with
"core sleep." https://pubmed.ncbi.nlm.nih.gov/38083143/

**Lambe R, O'Grady B, Baldwin M, Doherty C. 2025.** "Investigating the accuracy of Apple Watch VO2
max measurements: A validation study." *PLOS ONE*. **Author order corrected 2026-08-24 — Lambe R is
first author, not Doherty C as previously listed; confirmed via direct PDF read during the
literature-library retrofit.** University College Dublin (Insight SFI Centre
for Data Analytics). **Funded by Science Foundation Ireland National Challenge Fund
(22/NCF/FD/10949); "funder had no role in study design"; no competing interests declared.**
**Verified.** Apple Watch underestimated VO2max by ~6 mL/kg/min vs. indirect calorimetry
(MAPE 13.31%), "not sufficiently accurate to inform clinical decision-making." n=28.
https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0323741

**O'Grady B, Lambe R, Baldwin M, Acheson T, Doherty C. 2024.** "The Validity of Apple Watch Series 9
and Ultra 2 for Serial Measurements of Heart Rate Variability and Resting Heart Rate." *Sensors*
24(19):6220. **Author order corrected 2026-08-24 — O'Grady B is first author, not Doherty C as
previously listed; confirmed via direct PDF read during the literature-library retrofit.** Same
UCD/SFI group and funder as above. **Verified**, no COI. n=39, 316 measurements vs. Polar H10/Kubios
reference; HRV underestimated by 8.31 ms (MAPE 28.88%, fails equivalence testing); RHR excellent
agreement (MAPE 5.91%). https://pmc.ncbi.nlm.nih.gov/articles/PMC11478500/

**Khushhal AA, Mohamed AA, Elsayed ME. 2025.** "Accuracy of Apple Watch to Measure Cardiovascular
Indices in Patients with Cardiac Diseases: Observational Study." *Global Heart*. Umm Al-Qura
University, Saudi Arabia. **Funded by Umm Al-Qura University grant 25UQU4280290GSSR01
(academic, not Apple); no competing interests declared.** **Verified.** n=260 cardiac patients (190
regular rhythm, 70 arrhythmia); HR excellent reliability at rest/exercise/recovery in both groups;
SpO2 excellent at rest, declining to "good" post-exercise in arrhythmia patients; no significant
skin-tone effect detected. https://globalheartjournal.com/articles/10.5334/gh.1456

**Wasserlauf J, Vogel K, Whisler C, Benjamin E, Helm R, Steinhaus DA, Yousuf O, Passman RS.** "Accuracy of the Apple watch for detection of AF: A multicenter
experience." *Journal of Cardiovascular Electrophysiology* — **venue added 2026-08-24; not previously
stated in this file, confirmed via direct PDF read during the literature-library retrofit.**
Northwestern / Boston University / Saint Luke's Cardiovascular Consultants. **Funded
by American Heart Association grant 18SFRN34250013; explicit statement "Apple was not involved in
any aspect of the study"; no disclosures.** **Verified.** n=30 known-AF patients, 6-month
monitoring; by-subject sensitivity 72%, specificity 100%, PPV 100%, NPV 90%; by-episode sensitivity
60%. https://pmc.ncbi.nlm.nih.gov/articles/PMC11694482/

**Littell L, Roelle L, Dalal A, Van Hare GF, Orr WB, Miller N, Avari Silva JN.** "Assessment of Apple Watch Series 6 pulse oximetry and
electrocardiograms in a pediatric population." *PLOS Digital Health* — **venue added 2026-08-24; not
previously stated in this file, confirmed via direct PDF read during the literature-library
retrofit.** St. Louis Children's Hospital / Washington University
School of Medicine. **"No specific funding for this work"; no competing interests.** **Verified.**
SpO2 mean diff 2.0±2.6% vs. hospital oximeters (r=0.76), 4 outlier readings >5% diff; ECG intervals
strong agreement (RR r=0.96, QT r=0.90); automated rhythm algorithm only 75% specificity in
pediatric patients — a flagged limitation for smaller/abnormal-ECG patients.
https://pmc.ncbi.nlm.nih.gov/articles/PMC9931318/

**Abou L, Fliflet A, Hawari L, Rice LA. 2022.** "Sensitivity of Apple Watch fall detection feature
among wheelchair users." *Assistive Technology* 34(5):619–625. University of Illinois
Urbana-Champaign, Kinesiology and Community Health. **Unclear** — funding/COI not confirmed this
pass, but academic affiliation with no indication of commercial funding. **Notable/surprising
finding:** only 14/300 fall trials detected — sensitivity 4.7%, false-negative rate 95.3% — starkly
worse than Apple's general-population marketing claims. Apple Watch Series 5, n=25 able-bodied
participants simulating wheelchair falls.
https://www.tandfonline.com/doi/full/10.1080/10400435.2021.1923087

**Brew B, Faux SG, Blanchard E.** "Effectiveness of a Smartwatch App in Detecting Induced Falls:
Observational Study." St Vincent's Hospital/UNSW (Brew, Faux) + My Medic Watch (Blanchard).
**Verified and flagged as a genuine conflict — just not an Apple one:** funded by **My Medic Watch**
(a commercial fall-detection company); Brew and Blanchard hold fall-detection patents with royalty
payments; Brew is a scientific advisor to, and Blanchard is director of, My Medic Watch. Tests
multiple smartwatches (not Apple-specific) alongside a company that itself sells competing
fall-detection software. Overall smartwatch-app sensitivity 77% (falls), 99% specificity; wrist-side
effect significant (92.5% vs. 76.3% sensitivity depending on wrist).
https://pmc.ncbi.nlm.nih.gov/articles/PMC8981002/

**Inocian EP, Junia AT, Ong Cordovez MG, et al. 2024.** "Accuracy of the Apple Watch in Detecting
Atrial Fibrillation Among Patients Undergoing 24-Hour Holter Monitoring: A Prospective, Pragmatic
Study." *Philippine Journal of Cardiology*. Perpetual Succour Hospital–Cebu Heart Institute,
Philippines. **No competing financial interests declared.** **Verified.** n=140; irregular-rhythm
notification sensitivity 21.4% / specificity 100%; ECG-app-based detection (1,295 ECGs) sensitivity
100% / specificity 99.1%. https://pjc.philheart.org/elib/journal/identifier/pjc.2024.0712.055060/pdf

**DEFINE AFib Study** (Piccini J, Lande J, Kanwar R, Johnson L, Passman R, et al.) — Apple Watch
irregular-rhythm notification vs. Medtronic Reveal LINQ implantable cardiac monitor. **Verified:
funded by Medtronic**, manufacturer of the comparator device — a real conflict, but pointed *away*
from Apple, not toward it. ICM detected substantially more AF episodes; 40% of AF episodes occurred
while the Apple Watch wasn't being worn; when worn, the irregular-rhythm notification caught only
26% of ICM-detected AF episodes. **This is a case where an industry-funded study is unfavorable to
the non-funding vendor (Apple)** — useful context against assuming all funding bias runs one
direction. https://academic.oup.com/eurheartj/article/45/Supplement_1/ehae666.3538/7839071

**Shcherbina A, Mattsson CM, Waggott D, et al. 2017.** "Accuracy in Wrist-Worn, Sensor-Based
Measurements of Heart Rate and Energy Expenditure in a Diverse Cohort." *J Pers Med* 7(2):3.
Stanford (Ashley lab, Bio-X); evaluated 7 devices including Apple Watch. Independent of any single
vendor. **Corroborated** (independent academic study; specific funding line not directly confirmed
this pass). 6/7 devices measured HR within 5%; energy expenditure inaccurate across all devices
(best off by 27%, worst by 93%). n=60. https://med.stanford.edu/news/all-news/2017/05/fitness-trackers-accurately-measure-heart-rate-but-not-calories-burned.html

**Stahl ST, Rodakowski J, Patira R, Smagula SF. 2026.** "Enhancing a Behavioral Intervention Using
Rest-Activity Rhythm Monitoring via a Consumer Wearable in Older Dementia Caregivers and People
With Dementia: Feasibility and Acceptability Study." *JMIR Formative Research* 10:e88773.
University of Pittsburgh. **Senior author Smagula is owner/CEO of Activity Rhythm Solutions, a
university-licensed start-up that built the myRhythmWatch system used in this study (grant
R41AG069596) — a direct commercial interest in the study instrument, not in Apple Watch itself.**
**Corroborated** (no Apple-specific financial relationship found; flagged because the
device-adjacent company COI is still relevant context). n=21 (15 caregivers, 6 people with
dementia): all 21 met the minimum valid-day threshold; caregivers averaged 35 valid RAR-monitoring
days with all 15 still using the app at week 6, versus 30 valid days and only 6/6 remaining active
users among people with dementia; caregivers showed medium-to-large pre/post improvements in
depression and insomnia scores. https://pmc.ncbi.nlm.nih.gov/articles/PMC13626640/

**Al-Falahi ZS, Schlegel TT, Lee V, Chow CK, Kozor R, Lindow T, et al. 2026.** "Study protocol for
The Heart Watch Study - Prognostic performance of smartwatch 12-lead ECG with advanced ECG analysis
in consumer self-screening for cardiovascular disease." *American Heart Journal* (in press), doi
10.1016/j.ahj.2026.107619. University of Sydney / Karolinska Institutet. **No CoiStatement present
in the indexed record.** **Unclear.** Study protocol only: a planned 30,000-participant
Australia-wide observational cohort will use an iPhone app plus Apple Watch to acquire a 12-lead
smartwatch ECG for advanced-ECG (A-ECG) machine-learning analysis, with the primary endpoint a
composite of all-cause mortality, cardiovascular hospitalization, and incident cardiovascular
disease via administrative-data linkage. No results yet. https://doi.org/10.1016/j.ahj.2026.107619

**Yusuf KO, Steinbrinker TA, Jörß K, Richter J, Hanß S, Zeppernik T, et al. 2026.** "A Multi-Site
Dashboard for Evaluating HiGHmed Cardiovascular Sensor Data from Apple Watch." *Studies in Health
Technology and Informatics* 340:66–76. University Medical Center Göttingen. **No CoiStatement
present in the indexed record.** **Unclear.** HiGHmed cardiology use-case sensor sub-study (12 of
93 enrolled participants shown): an R Shiny dashboard aggregating Apple Watch heart-rate/step data
with clinical records showed pre-hospitalization deterioration (falling KCCQ-12 scores, daily steps
dropping below 2,000) and a strong steps–heart-rate correlation (r≈0.8), alongside visible
sensor-data gaps and inconsistent manual-measurement adherence. https://doi.org/10.3233/SHTI260986

**Alshamrani M, Alhazmi S, Alafif T, Qadah TM, Aljabri M, Al-Eidarous W, et al. 2026.**
"Machine Learning-Based Prediction Model of Pilgrims' Tiredness During Hajj Using Smartwatch
Physiological and Mobility Indicators." *Sensors* 26(17):5625. Umm Al-Qura University, Saudi
Arabia. **"The authors declare no conflicts of interest"; no Apple relationship.**
**Corroborated.** Hajj 1445 (June 2024) Apple Watch dataset, 120 records from 3 participants: best
record-level tiredness-classification accuracy 93.33% (Decision Tree, MVN-sampled synthetic
augmentation), but leave-one-participant-out accuracy fell to 68.65% (SD 19.72%) — a reminder that
in-sample accuracy on a 3-participant dataset overstates cross-participant generalization.
https://pmc.ncbi.nlm.nih.gov/articles/PMC13567947/

**Jansen CE, Jaspers Focks J, Manglani Rodriguez S, Pol L, Edgar R, van Royen N, et al. 2026.**
"Wearable saving lives: a case report." *Resuscitation Plus* 31:101447. Radboud University Medical
Center. **COI discloses unrelated grants/speaker fees (European Resuscitation Council, Dutch Heart
Foundation, Biotronik, Abbott, Medtronic, Philips, Bayer, ZonMw) and an editorial-board role at the
publishing journal; none naming Apple.** **Corroborated.** Single-patient case report: Apple Watch
fall-detection triggered automated alerts during an unwitnessed out-of-hospital cardiac arrest,
enabling bystander CPR ~6–7 min post-collapse and a favourable neurological outcome after VF
arrest, CABG, and ICD implantation. https://pmc.ncbi.nlm.nih.gov/articles/PMC13543876/

**Zou L, Zhang L. 2026.** "Prescribing green dose for college students' mental health: Identifying
thresholds for green space exposure duration, frequency, and cumulative dose via smartwatch."
*Environmental Research*. Shanghai Jiao Tong University School of Design. N=43 healthy students,
six-week wearable-based observational study using Apple Watch data. **Explicit COI statement read
directly: "The authors declare that they have no known competing financial interests or personal
relationships that could have appeared to influence the work reported in this paper." No Apple
mention.** **Corroborated**. Single-session green-space
exposure of ~17–35 min associated with sleep outcomes; ~3 sessions/week most associated with
daytime functioning; cumulative weekly exposure of ~70–120 min associated with emotional outcomes
and HRV amplitude differences. **Added 2026-10-09 from the 2026-09-01 automated scan (branch consolidation).**
https://pubmed.ncbi.nlm.nih.gov/42250841/

**Shroddha Aditi Das, Mukherjee I, Lambiase PD. 2026.** "Apple Watch Saves an Athlete: Unmasking
Early Detection of Arrhythmogenic Cardiomyopathy." *Cureus*. Barts Health NHS Trust / Barts and the
London School of Medicine and Dentistry / NIHR Barts BRC & UCLH/UCL BRC, London. Single-patient case
report (33-year-old athlete): recurrent palpitations initially documented by a consumer wearable
(named as Apple Watch in the title) prompted a diagnostic workup that revealed arrhythmogenic
cardiomyopathy. **ICMJE disclosure read directly: "no financial support was received from any
organization for the submitted work... no financial relationships... no other relationships or
activities that could appear to have influenced the submitted work." No Apple mention.**
**Corroborated** — Tier C. **Category note: this is a single-patient case report, not a
population-level outcome study, so its fit under "Use-case" is genuinely ambiguous; included here
rather than excluded, since it otherwise
clears the relevance bar (device named in title, peer-reviewed journal article, has an abstract, in
English).** **Added 2026-10-09 from the 2026-09-01 automated scan (branch consolidation).** https://pubmed.ncbi.nlm.nih.gov/42639363/

**Serttaş A, Bulat Demir S, Uyanik Uğur G, Altunkurt O. 2026.** "Bounded control in digital
health: Privacy discourse and algorithmic governance in Apple Health." *Digital Health*. Faculty of
Communication, İstanbul Aydın University. Qualitative study (critical discourse analysis of Apple's
official "Health App and Privacy" text, plus semi-structured interviews with n=18 Apple Watch/Apple
Health users) examining how user control over health data is constructed, communicated, and
experienced. **Explicit COI statement read directly: "The authors declared no potential conflicts
of interest with respect to the research, authorship, and/or publication of this article." No Apple
mention.** **Corroborated** — Tier C. **Category note: this is a media/communication-studies paper
(qualitative discourse and interview analysis of device users' privacy experience), not an
accuracy-validation or health-outcome study — a genuinely ambiguous fit for a category scheme
designed around those two kinds of literature. Flagged for reconsideration (e.g. a future "Policy/Ethics" category) in a later pass if more
papers of this type are found.** **Added 2026-10-09 from the 2026-09-01 automated scan (branch consolidation).**
https://pubmed.ncbi.nlm.nih.gov/42633020/

**Added 2026-10-12.** Li Y, Wang H, Chandrashekhar R, Major J, Chandna M, Bodison SC. 2026.
"Feasibility and Methodological Consideration of Using Wearable Devices to Examine the Relationship
Between Sleep and Balance: Case Report With 2 College Students." *JMIR Formative Research*,
PMID 42854191. University of Florida Department of Occupational Therapy. Case report, N=2, 4 months;
cross-filed from the Oura Tier C section above (Participant 1 wore an Apple Watch Series 5 and an
Oura ring; Participant 2 a Fitbit Charge 5 and an Oura ring). CoiStatement: "Conflicts of Interest:
None declared." **Tier C. Corroborated.** **Category: Use-case (feasibility-focused; genuinely
ambiguous, defaulted per this file's convention).** Missing-data rates for the wrist devices fell
from as high as 75.2% to 14.1%/20.3% after structured weekly check-ins were introduced.
https://pubmed.ncbi.nlm.nih.gov/42854191/

**Added 2026-10-12.** Hallihan H, Lee S, Adomah R, Miranda R, Rospenda K. 2026. "A Problem-Solving
Therapy With Apple Watch Support for College Students With Alcohol Use Disorder Symptoms: Pilot
Randomized Controlled Trial." *JMIR Formative Research*, PMID 42832266. Brown University / University
of Illinois Chicago / University of Wisconsin-Milwaukee. Pilot RCT testing feasibility and
acceptability of a behavioral intervention (problem-solving therapy + Apple Watch, "PST-APPLE") for
college students with alcohol use disorder symptoms; Apple Watch used as an adjunct to the
intervention, not evaluated for sensor accuracy. CoiStatement: "Conflicts of Interest: None declared."
**Tier C. Corroborated.** **Category: Use-case.** https://pubmed.ncbi.nlm.nih.gov/42832266/

**Added 2026-10-24 (manual add-paper).** Wyatt KD, Poole LR, Mullan AF, Kopecky SL, Heaton HA. 2020.
"Clinical evaluation and diagnostic yield following evaluation of abnormal pulse detected using Apple
Watch." *Journal of the American Medical Informatics Association* 27(9):1359-1363, PMID 32979046,
PMC7526465. Mayo Clinic. Retrospective review of 264 patients evaluated over 4 months after an
abnormal pulse detected with Apple Watch; a clinically actionable cardiovascular diagnosis was made in
30 (11.4%), including 6 of 41 with an explicit alert, after frequent ECGs, Holter monitoring and chest
x-rays. Funding: FDA grant U01FD005938 (Yale-Mayo CERSI) and NIH UL1TR002377. COI statement (full-text
XML): "The authors have no personal conflicts of interest to declare. All authors are employed by Mayo
Clinic. Mayo Clinic has a partnership with AliveCor, which sells a direct-to-consumer
electrocardiogram product." No Apple tie; the AliveCor partnership is with a competing product.
**Tier C. Verified.** **Category: Use-case (clinical yield of irregular-rhythm alerts; left out of
Module 5 Cardiac because it studies one device).** https://pubmed.ncbi.nlm.nih.gov/32979046/

## Apple Watch — systematic reviews / meta-analyses

**Hogue T, Khoury A, Njeim P, Aswad N, Youssef L, Birtulescu S, et al. 2026.** "Advancement in
wrist worn physical activity trackers: technological developments and measurement accuracy: a
systematic review." *Frontiers in Digital Health* 8:1820224. Research Institute of McGill
University Health Centre / Vanderbilt University Medical Center. **"Conducted in the absence of any
commercial or financial relationships"; no Oura/WHOOP/Apple-specific disclosure (reviews wrist-worn
trackers broadly, not an Apple-Watch-specific study).** **Corroborated.** PRISMA review of 47
studies (of 1,659 screened, PROSPERO CRD42024551740) spanning pre-2010 to current devices: names
Apple Watch (with Garmin vivosmart) among "modern devices" reaching >0.80 validity correlation for
heart rate during exercise, versus ≤0.50 for early (pre-2010) monitors; energy-expenditure error
remains 10–40% even in recent devices. https://pmc.ncbi.nlm.nih.gov/articles/PMC13542415/

**Shahid S, Iqbal M, Saeed H, et al. 2025.** "Diagnostic Accuracy of Apple Watch Electrocardiogram
for Atrial Fibrillation: A Systematic Review and Meta-Analysis." *JACC: Advances* 4(2):101538.
Multiple Pakistani medical colleges + Oklahoma Heart Hospital. **Updated 2026-10-10:** the Europe PMC
full text (PMC11780081) states "The authors have reported that they have no relationships relevant to
the contents of this paper to disclose." **Verified**, no disclosed industry funding. Pooled sensitivity 94.8%, specificity 95%, AUC 0.96 vs.
12-lead ECG. https://pmc.ncbi.nlm.nih.gov/articles/PMC11780081/

**Choe J-P, Kang M. 2025.** "Apple watch accuracy in monitoring health metrics: a systematic review
and meta-analysis." *Physiological Measurement*. University of Mississippi, Health and Sport
Analytics Lab. **Unclear** — funding not disclosed in accessible summaries. 56 studies pooled:
MAPE 4.43% (HR), 8.17% (steps), 27.96% (energy expenditure).

**"The accuracy of Apple Watch measurements: a living systematic review and meta-analysis."**
*npj Digital Medicine* (2025/2026), same UCD/SFI-funded group as Doherty et al. above (2 entries).
82 studies pooled, 430,052 participants, 14 health metrics. **Corroborated** (same lab/funder
identity as the group's other papers), but this specific paper's disclosure text was gated behind a
login wall and not directly read. https://www.nature.com/articles/s41746-025-02238-1

**"Accuracy of Detecting Atrial Fibrillation: A Systematic Review and Meta-Analysis of Wrist-Worn
Wearable Technology."** Belani S, Wahood W, Hardigan P, Placzek AN, Ely S. *Cureus*, issued 2021-12-12 (Crossref), e20362, DOI 10.7759/cureus.20362. Nova Southeastern University, PMC8752409. Year corrected 2026-10-10 from 2022. 9 studies, n=1,581,
wrist wearables (Apple Watch, Samsung, KardiaBand) vs. conventional AF detection. **Updated
2026-10-10:** the Europe PMC full text states "The authors have declared that no competing interests
exist"; no funding statement was found. **Verified** for the COI statement.

## Apple Watch — access limitations and gaps

Apple's own VO2max white paper's actual individual authorship could not be confirmed (Apple-internal
PDF, not machine-readable via fetch; relayed only via secondary sources). Apple's official
research/publications listing is not a single enumerable bibliography — the newsroom describes the
three landmark studies narratively rather than listing citations; a separate ML-publications index
(machinelearning.apple.com/research/?domain=Health) exists and was not explored this pass.

---

# Cross-cutting findings across all three devices

1. **Funder bias does not run in one predictable direction.** Robbins et al. 2024 was funded by
   Oura and still gave Apple Watch its best marks for REM sensitivity — a competitor doing well in
   an Oura-funded study. DEFINE AFib was funded by Medtronic and was unfavorable to Apple, the
   non-funding vendor being compared. My Medic Watch funded a fall-detection study that was
   Apple-neutral but had its own commercial conflict pointed at fall-detection patents generally,
   not at any smartwatch maker. **The lesson: check who funded the study and read the actual
   finding — don't assume the funder's product always wins.**
2. **Sponsored-infrastructure clusters are common and easy to miss if you only check individual
   author employment.** Oura's TemPredict program funds a family of downstream papers (COVID
   detection, vaccine antibody response, depression/temperature) that don't all list an Oura
   employee as co-author but share sponsorship of the underlying cohort. WHOOP's CQUniversity
   cluster (Miller, Bellenger, and colleagues) includes a WHOOP-sponsored faculty position that
   touches several papers beyond the one where it's explicitly disclosed. **A single paper's
   author-employment check is not sufficient — the surrounding research program matters.**
3. **All three vendors have at least one flagship study that is explicitly vendor-sponsored and
   widely treated as authoritative in public discourse** (Apple Heart Study/NEJM; Oura's Kinnunen &
   Altini sleep-staging paper; the WHOOP-funded University of Arizona JCSM study). None of these are
   disqualified by sponsorship — they are peer-reviewed and, in Apple's case, large and rigorously
   designed — but each should carry its funding disclosure whenever cited, which is not how they are
   typically presented in vendor marketing.
4. **Apple has, by a wide margin, the most independent (Tier C) accuracy-validation literature of
   the three vendors** — likely a function of Apple Watch's scale and longevity in the consumer
   market rather than any special openness on Apple's part. Oura's evidence base leans on one
   heavily-cited but vendor-funded flagship (Robbins 2024) plus a genuinely large independent tail.
   WHOOP has the thinnest independent accuracy literature of the three, and its two most-marketed
   "independent" figures (Berryhill 2020's JCSM validation, and even the AIS-funded Bellenger 2021
   study by extension of the same author cluster) turn out to have funding or personnel ties back to
   WHOOP once traced.
5. **SpO2 and skin/body-temperature validation are near-total gaps for Oura and WHOOP alike** — no
   independent peer-reviewed study was found for either metric on either device (confirmed by a
   PubMed and Europe PMC full-text re-search on 2026-10-09; no validation located, **Corroborated**,
   since absence across two databases cannot be Verified; reworded 2026-10-10). Apple Watch has
   independent SpO2 validation (Littell et al., pediatric population) but it is thin outside that
   one study. This is a genuine, cross-vendor evidence gap worth flagging prominently.
6. ~~A genuine Oura-vs-WHOOP head-to-head now exists (Dial et al. 2025) and should be fully
   extracted~~ — **done 2026-08-25.** Full text read directly, AFRL funding and no-COI confirmed,
   complete RHR and HRV tables (all five devices) now in `validation-evidence.md` §3a.

---

# Open items for a follow-up pass

1. ~~Read Dial et al. 2025 in full~~ — **done 2026-08-25.**
2. ~~Verify the actual author list of the 2026 npj "menstrual cycle through the lens of a wearable
   device" paper before citing its tier~~ **Done** (bioRxiv read 2026-08-24; published version 9:633
   confirmed 2026-10-09). Tier A, Verified.
3. **Partly done 2026-10-09:** Bellenger 2022 Verified Tier B; Miller 2020 funders Corroborated as
   ARC/AIS, COI still unread. Original item: **Confirm funding for the Miller et al. 2020 J Sports Sciences WHOOP validation paper** and the
   Bellenger et al. 2022 water polo HRV paper — both likely Tier B given the CQU author cluster's
   established WHOOP-sponsorship pattern, but neither disclosure was directly read.
4. **Individually verify the ~6 reproductive-health/arrhythmia papers on Oura's own research list**
   flagged above (labor onset, pregnancy biometrics, LH-surge ultradian rhythms, AF-via-PPG) — a
   likely dense Tier A/B cluster that hasn't been author-checked one by one.
5. ~~Confirm which Oura page states "170+" vs "130+" studies (may reflect a page-version or date
   discrepancy)~~ **Done 2026-10-09: the page says 130+; no 170+ found in any snapshot checked.**
6. **Systematic reviews still needing direct funding/COI extraction** (updated 2026-10-10: Khan, Shahid
   and the Nova Southeastern review are done, all with no disclosed industry ties; see their entries):
   Choe & Kang 2025 (Apple Watch, Physiological Measurement, closed access), and the Khodr et al.
   WHOOP medRxiv preprint (the stored PDF has no extractable disclosure section). Original list: Khan et al. 2025 (Oura, OTO
   Open), Shahid et al. 2025 (Apple Watch AF, JACC Advances), Choe & Kang 2025 (Apple Watch,
   Physiological Measurement), the Nova Southeastern AF wearables review, and the Khodr et al.
   WHOOP medRxiv preprint — all blocked by paywalls/CAPTCHAs this pass, all worth reading in full
   both for their own tier and as reference-list discovery mechanisms for papers not yet in this
   library.
7. ~~No SpO2 or temperature validation found for Oura or WHOOP~~ **Done 2026-10-09: confirmed as a
   true gap by PubMed and Europe PMC full-text searches.** Original item: confirm this is a true evidence
   gap rather than a search-access limitation, ideally by attempting direct database searches (e.g.
   PubMed advanced search) rather than general web search.
8. **Apple's own VO2max white paper** — attempt a direct, readable fetch of the PDF rather than
   relying on secondary summaries.
9. Log items 4, 5, 7 and the Dial et al. gap-closure into `shared/unresolved-questions.md` per this
   knowledge base's standing convention (done — see Tier 9 there as of this pass).

---

## Access limitations encountered this pass

WebFetch was blocked (403, CAPTCHA, or login redirect) on: Wiley Online Library (Physiological
Reports, OTO Open), PMC/pmc.ncbi.nlm.nih.gov (reCAPTCHA on several but not all pages), MDPI direct
article pages, Springer/BiomedCentral, Nature/npj (idp.nature.com login wall), Tandfonline, JACC,
IEEE Xplore, and ResearchGate. Findings sourced only through these blocked routes are marked
Corroborated or Unclear rather than Verified, per this file's confidence-marker convention. A
follow-up pass with authenticated or browser-based access (rather than the WebFetch tool alone)
would likely upgrade a meaningful number of entries above from Corroborated to Verified.
