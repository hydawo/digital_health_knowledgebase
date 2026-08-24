# Research Library — Oura, WHOOP, Apple Watch

A bibliography of peer-reviewed / published research involving Oura, WHOOP, and Apple Watch,
organized by **sponsorship status** rather than by topic. Companion to `validation-evidence.md`,
which does deep full-text extraction on the sleep-staging accuracy literature specifically. This
file is broader (any topic) but shallower per entry — authors, affiliations, funding/COI, key
finding, and a link.

**Last verified: 2026-08-24.** Supersedes the earlier two-device draft of this file.

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

**Kinnunen H, Altini M. 2021.** "The Promise of Sleep: A Multi-Sensor Approach for Accurate Sleep
Stage Detection Using the Oura Ring." *Sensors* 21(13):4302.
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
simultaneously vs. an ECG chest-strap reference; 13 adults (6 female), 536 nights. No industry/
vendor funding identified in secondary sources. **Corroborated, not Verified** — direct fetch of the
Wiley/PMC pages was blocked (403/CAPTCHA) in two separate passes; a follow-up with authenticated or
browser access is warranted before treating the "no vendor funding" finding as certain.
**Resting HR:** Oura Gen3 CCC=0.97 (MAPE 1.67±1.54%); Oura Gen4 CCC=0.98 (MAPE 1.94±2.51%); WHOOP
4.0 CCC=0.91 "moderate" (MAPE 3.00±2.15%); Polar CCC=0.86 "poor" (MAPE 2.71±2.75%).
**HRV:** Oura Gen4 highest, Oura Gen3 second; WHOOP moderate; Garmin and Polar poor agreement
(exact WHOOP/Garmin/Polar HRV CCC/MAPE not retrievable from search snippets — full-text read still
needed). https://physoc.onlinelibrary.wiley.com/doi/10.14814/phy2.70527 ·
PDF: https://physoc.onlinelibrary.wiley.com/doi/pdfdirect/10.14814/phy2.70527
**Action:** extract this in full into `validation-evidence.md`, which currently states no
Oura-vs-WHOOP head-to-head exists.

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

## Oura — systematic reviews (as discovery mechanism, and classified in their own right)

**Khan et al. 2025, *OTO Open*.** "The Oura Ring Versus Medical-Grade Sleep Studies: A Systematic
Review and Meta-Analysis." 6 studies, n=388 pooled, 2019–2024. **Unclear** — full text was blocked
(PMC CAPTCHA, Wiley 403) in two passes; authors, funding, and reference list not yet extracted.
Flagged for a follow-up pass with better access.

**Gong EJ, Bang CS, Lee JJ, Baik GH. 2025.** "Smart Ring in Clinical Medicine: A Systematic
Review." *Diagnostics* (MDPI) / JMIR preprint #83508. Hallym University College of Medicine, South
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
number, as it may be stale or page-specific). The blog page lists roughly 100 studies by year
(2016–2025) with no running total stated on that page itself.

**Composition, on a title-level skim (not individually tier-verified):** the large majority are
genuinely independent academic/clinical groups (Harvard/Brigham, UCSF/UCSD, NUS, Ohio State,
Vermont, assorted hospital and sports-science groups) using Oura as a data-collection instrument —
i.e. Tier C by authorship, even while Oura promotes the list. A smaller number are explicitly
Oura-authored/partnered. A meaningful subset trace back to the Oura-sponsored TemPredict
infrastructure (Tier B). **This corroborates that Oura's "170+/130+ studies" marketing claim is not
mostly Tier A/B** — but a non-trivial fraction is, and the list itself should not be read as neutral
without per-paper sorting.

## Oura — confirmed evidence gaps

- **No independent peer-reviewed SpO2 validation study found for Oura** — only Oura's own blog
  claims of accuracy improvement Gen3→Gen4.
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
"Inter- and Intrapersonal Associations Between Physiology and Mental Health." *JMIR* 27:e64955.
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

**"The menstrual cycle through the lens of a wearable device."** *npj Digital Medicine* 9:633
(2026), PMID 42185632. **Correction to the prior pass's assumption:** this paper's actual author
list could **not** be confirmed this pass (Nature login wall, PubMed cookie wall, EuropePMC nav-only
all blocked). One AI-generated secondary summary named "Alexander Gonzalez and Johanna J. O'Day,
Stanford Wu Tsai Human Performance Alliance" as lead authors — **this is unverified and should not
be trusted**; it doesn't match WHOOP's in-house authorship pattern on the sister paper above, so the
earlier assumption that this is Tier A is now **downgraded to Unclear** pending a direct read.
**Action: read the actual PDF before citing this paper's tier in any downstream content.**

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

**Bellenger CR, Miller DJ, Halson SL, Roach GD, Maclennan CE, Sargent C. 2022.** "Evaluating the
Typical Day-to-Day Variability of WHOOP-Derived Heart Rate Variability in Olympic Water Polo
Athletes." *Sensors* 22(18):6723. University of South Australia (ARENA), CQU Appleton Institute,
Australian Catholic University, Water Polo Australia. Same author cluster as the WHOOP-sponsored
Miller CQU position established above. **Corroborated, funding statement itself Unclear** —
flagged as likely Tier B given the overlapping author cluster, but the paper's own funding section
wasn't directly read. 11 elite male water polo players, 16 weeks pre-Tokyo Olympics, WHOOP 3.0.

**Miller DJ, Lastella M, Scanlan AT, Bellenger CR, Halson SL, Roach GD, Sargent C. 2020.** "A
validation study of the WHOOP strap against polysomnography to assess sleep." *Journal of Sports
Sciences* 38(22):2631–2636, PMID 32713257. All-CQU/Australian author list, no WHOOP employees
visible. **Unclear** — funding/COI text not retrievable (Tandfonline 403). Given the same author
cluster's demonstrated WHOOP-sponsorship pattern elsewhere, flag as likely Tier B pending direct
confirmation; do not assume independence.

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
64% four-stage agreement, κ=0.47. https://pmc.ncbi.nlm.nih.gov/articles/PMC8226553/

**Schyvens A, et al. 2025.** *SLEEP Advances* 6(2):zpaf021. Six devices incl. WHOOP 4.0 vs PSG.
**Funded by Flanders Innovation & Entrepreneurship (VLAIO); authors declare no conflicts.**
**Verified.** Full extraction in `validation-evidence.md` §1. WHOOP κ=0.37 ("fair"), 4th of 6.

**Dial MB, et al. 2025.** *Physiological Reports* 13:e70527. See Oura Tier C above — same paper,
includes WHOOP 4.0. WHOOP HR: CCC=0.91 "moderate" (MAPE 3.00±2.15%). WHOOP HRV: "moderate" accuracy,
behind both Oura generations (exact CCC/MAPE not yet extracted). **Corroborated, not Verified** —
funding not directly confirmed; flagged for full-text follow-up, same as the Oura entry.

**Lundstrom C, De Souza MJ, Koltun KJ, Strock N, Canil A, Williams N. 2024.** "Wearable technology
metrics are associated with energy deficiency and psychological stress in elite swimmers."
*International Journal of Sports Science & Coaching*. Penn State Kinesiology. Examined WHOOP
HRV/RHR/Strain/Recovery vs. lab RMR, T3 thyroid, RESTQ stress in Division 1 swimmers. **Notable
context, not necessarily disqualifying:** Penn State Athletics has an institutional WHOOP-Unite
equipment/software partnership (announced 2022) — separate from a research-funding relationship,
but worth flagging. **Unclear** — the paper's actual COI/funding section wasn't retrieved.

**Khodr R, Kamal L, Minerbi A, Gupta G. 2024.** "Accuracy, Utility and Applicability of the WHOOP
Wearable Monitoring Device in Health, Wellness and Performance — a systematic review." *medRxiv*
2024.01.04.24300784 (preprint; final publication status not confirmed). Univ. of Ottawa,
Institute for Pain Medicine (Rambam/Technion). No WHOOP-affiliated co-authors found.
**Corroborated, not Verified** — secondary sources report "no competing interests declared," but
the actual medRxiv disclosure text was blocked (403 on HTML and PDF). Worth a direct re-fetch: this
review's reference list is a good discovery mechanism for additional WHOOP papers.

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

## WHOOP — confirmed evidence gaps

- **No independent peer-reviewed SpO2 validation study found** — only WHOOP's own support-page
  description of sampling methodology (30-sec samples roughly every 20 min during sleep, with
  signal-quality gating).
- **No independent peer-reviewed skin/body-temperature validation study found** — same gap as SpO2.
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

**Mahalingaiah S, Fruh V, Rodriguez E, et al. 2022.** "Design and methods of the Apple Women's
Health Study: a digital longitudinal cohort study." *Am J Obstet Gynecol*. Harvard T.H. Chan School
of Public Health (lead) + NIEHS/NIH (Jukic). **Corroborated** — three-way named partnership (Apple +
Harvard Chan + NIEHS) per NIH's own press release; whether a named Apple employee appears as a paper
co-author specifically was **not confirmed** (PMC fetch blocked by a bot check).
https://pmc.ncbi.nlm.nih.gov/articles/PMC10518829/ ·
NIH release: https://www.nih.gov/news-events/news-releases/nih-partners-apple-harvard-university-womens-health-study

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

## Tier B — Apple-funded/affiliated but independent authors, or run via a named Apple-partner institution

**Apple Hearing Study** — University of Michigan partnership (with WHO). Collects headphone/
environmental sound exposure via iPhone + Apple Watch Noise app; examines cardiovascular/stress
links to long-term sound exposure. **Corroborated** (named partnership); individual peer-reviewed
outputs not identified this pass. https://sph.umich.edu/applehearingstudy

**2025 Apple Health Study** (holistic mental/physical health), led by Brigham and Women's Hospital,
launched via the Research app Feb 2025. **Corroborated** (secondary sources only); no individual
paper yet identified. https://www.apple.com/newsroom/2025/02/new-holistic-apple-health-study-launches-today-in-the-research-app/

## Tier C — Fully independent

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

**Doherty C, Lambe R, O'Grady B, Baldwin M. 2025.** "Investigating the accuracy of Apple Watch VO2
max measurements: A validation study." *PLOS ONE*. University College Dublin (Insight SFI Centre
for Data Analytics). **Funded by Science Foundation Ireland National Challenge Fund
(22/NCF/FD/10949); "funder had no role in study design"; no competing interests declared.**
**Verified.** Apple Watch underestimated VO2max by ~6 mL/kg/min vs. indirect calorimetry
(MAPE 13.31%), "not sufficiently accurate to inform clinical decision-making." n=28.
https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0323741

**Doherty C, et al. 2024.** "The Validity of Apple Watch Series 9 and Ultra 2 for Serial
Measurements of Heart Rate Variability and Resting Heart Rate." *Sensors* 24(19):6220. Same UCD/SFI
group and funder as above. **Verified**, no COI. n=39, 316 measurements vs. Polar H10/Kubios
reference; HRV underestimated by 8.31 ms (MAPE 28.88%, fails equivalence testing); RHR excellent
agreement (MAPE 5.91%). https://pmc.ncbi.nlm.nih.gov/articles/PMC11478500/

**Khushhal AA, Mohamed AA, Elsayed ME. 2025.** "Accuracy of Apple Watch to Measure Cardiovascular
Indices in Patients with Cardiac Diseases: Observational Study." *Global Heart*. Umm Al-Qura
University, Saudi Arabia. **Funded by Umm Al-Qura University grant 25UQU4280290GSSR01
(academic, not Apple); no competing interests declared.** **Verified.** n=260 cardiac patients (190
regular rhythm, 70 arrhythmia); HR excellent reliability at rest/exercise/recovery in both groups;
SpO2 excellent at rest, declining to "good" post-exercise in arrhythmia patients; no significant
skin-tone effect detected. https://globalheartjournal.com/articles/10.5334/gh.1456

**Wasserlauf J, et al.** "Accuracy of the Apple watch for detection of AF: A multicenter
experience." Northwestern / Boston University / Saint Luke's Cardiovascular Consultants. **Funded
by American Heart Association grant 18SFRN34250013; explicit statement "Apple was not involved in
any aspect of the study"; no disclosures.** **Verified.** n=30 known-AF patients, 6-month
monitoring; by-subject sensitivity 72%, specificity 100%, PPV 100%, NPV 90%; by-episode sensitivity
60%. https://pmc.ncbi.nlm.nih.gov/articles/PMC11694482/

**Littell L, Avari Silva JN, et al.** "Assessment of Apple Watch Series 6 pulse oximetry and
electrocardiograms in a pediatric population." St. Louis Children's Hospital / Washington University
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

## Apple Watch — systematic reviews / meta-analyses

**Shahid S, Iqbal M, Saeed H, et al. 2025.** "Diagnostic Accuracy of Apple Watch Electrocardiogram
for Atrial Fibrillation: A Systematic Review and Meta-Analysis." *JACC: Advances* 4(2):101538.
Multiple Pakistani medical colleges + Oklahoma Heart Hospital. **Unclear** — full text 403'd,
funding/COI not accessible this pass. Pooled sensitivity 94.8%, specificity 95%, AUC 0.96 vs.
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
Wearable Technology."** Nova Southeastern University, 2022, PMC8752409. 9 studies, n=1,581,
wrist wearables (Apple Watch, Samsung, KardiaBand) vs. conventional AF detection. **Unclear** —
funding/COI not confirmed this pass.

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
   independent peer-reviewed study was found for either metric on either device. Apple Watch has
   independent SpO2 validation (Littell et al., pediatric population) but it is thin outside that
   one study. This is a genuine, cross-vendor evidence gap worth flagging prominently.
6. **A genuine Oura-vs-WHOOP head-to-head now exists** (Dial et al. 2025) and should be fully
   extracted into `validation-evidence.md`, which currently states no such study exists. This is the
   single highest-value follow-up action from this research pass.

---

# Open items for a follow-up pass

1. **Read Dial et al. 2025 in full** (Oura Gen3/Gen4 vs WHOOP 4.0 vs ECG) and extract into
   `validation-evidence.md`. Highest priority — closes a previously-flagged gap.
2. **Verify the actual author list of the 2026 npj "menstrual cycle through the lens of a wearable
   device" paper** before citing its tier — the earlier assumption of Tier A is now downgraded to
   Unclear pending a direct read.
3. **Confirm funding for the Miller et al. 2020 J Sports Sciences WHOOP validation paper** and the
   Bellenger et al. 2022 water polo HRV paper — both likely Tier B given the CQU author cluster's
   established WHOOP-sponsorship pattern, but neither disclosure was directly read.
4. **Individually verify the ~6 reproductive-health/arrhythmia papers on Oura's own research list**
   flagged above (labor onset, pregnancy biometrics, LH-surge ultradian rhythms, AF-via-PPG) — a
   likely dense Tier A/B cluster that hasn't been author-checked one by one.
5. **Confirm which Oura page states "170+" vs "130+" studies** — may reflect a page-version or date
   discrepancy.
6. **Systematic reviews still needing direct funding/COI extraction**: Khan et al. 2025 (Oura, OTO
   Open), Shahid et al. 2025 (Apple Watch AF, JACC Advances), Choe & Kang 2025 (Apple Watch,
   Physiological Measurement), the Nova Southeastern AF wearables review, and the Khodr et al.
   WHOOP medRxiv preprint — all blocked by paywalls/CAPTCHAs this pass, all worth reading in full
   both for their own tier and as reference-list discovery mechanisms for papers not yet in this
   library.
7. **No SpO2 or temperature validation found for Oura or WHOOP** — confirm this is a true evidence
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
