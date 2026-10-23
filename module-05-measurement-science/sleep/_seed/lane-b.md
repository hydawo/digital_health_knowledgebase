# Module 5, Sleep: Lane B seed (measurement science)

Prepared 2026-10-22. Lane B covers sleep metric definitions, device-agnostic scoring and detection
algorithms, cross-device pooled accuracy, and the physiological limits of wrist sensing. Guidance,
consensus and evaluation frameworks are left to Lane A. 35 papers kept: 12 PDFs stored and
verified, 18 open access but not obtained this pass, 5 paywalled.

## 1. Search log, 2026-10-22

Europe PMC REST (`/search`, `format=json`, `sort=CITED desc`, page size 20 to 25), hit counts as returned:

| # | Query | Hits |
|---|---|---|
| E1 | `TITLE:"sleep regularity" AND (TITLE:metric* OR TITLE:index OR TITLE:measur*)` | 30 |
| E2 | `TITLE:"sleep regularity index"` | 22 |
| E3 | `(TITLE:"social jetlag" OR TITLE:"social jet lag") AND (TITLE:review OR TITLE:measur*)` | 17 |
| E4 | `(TITLE:actigraphy OR TITLE:accelerometer) AND TITLE:sleep AND (TITLE:algorithm* OR TITLE:"open source" OR TITLE:"machine learning") AND PUB_YEAR:[2010 TO 2026]` | 48 |
| E5 | `(TITLE:sleep AND (TITLE:wearable* OR TITLE:"consumer" OR TITLE:tracker*)) AND (TITLE:"meta-analysis" OR TITLE:"systematic review") AND PUB_YEAR:[2010 TO 2026]` | 22 |
| E6 | `(TITLE:actigraphy AND TITLE:polysomnograph*) AND (TITLE:"meta-analysis" OR TITLE:"systematic review")` | 1 |
| E7 | `(TITLE:"sleep stag*" OR TITLE:"sleep staging") AND (TITLE:photoplethysmograph* OR TITLE:PPG OR TITLE:"heart rate" OR TITLE:cardiac OR TITLE:cardiorespiratory) AND PUB_YEAR:[2015 TO 2026]` | 39 |
| E8 | `(TITLE:"van Hees" OR TITLE:GGIR OR ABSTRACT:"HDCZA" OR (TITLE:"sleep period" AND TITLE:accelerometer))` | 10 |
| E9 | `(TITLE:sleep AND (TITLE:"skin tone" OR TITLE:race OR TITLE:racial OR TITLE:"older adults" OR TITLE:insomnia) AND (TITLE:actigraph* OR TITLE:wearable* OR TITLE:tracker*) AND (TITLE:accuracy OR TITLE:validity OR TITLE:bias OR TITLE:agreement OR TITLE:polysomnograph*)) AND PUB_YEAR:[2010 TO 2026]` | 14 |
| E10 | `(TITLE:"non-wear" OR TITLE:nonwear) AND TITLE:sleep` | 4 |
| E11 | `(TITLE:"epoch-by-epoch" OR (TITLE:sleep AND TITLE:"Bland-Altman"))` | 6 |
| E12 | `(TITLE:"interdaily stability" OR TITLE:"rest-activity") AND (TITLE:nonparametric OR TITLE:"non-parametric" OR TITLE:fragmentation OR TITLE:package OR TITLE:metrics) AND PUB_YEAR:[2010 TO 2026]` | 25 |
| E13 | `(TITLE:"sleep-wake" OR TITLE:"sleep/wake") AND (TITLE:classification OR TITLE:benchmark) AND (TITLE:accelerometer OR TITLE:actigraphy OR TITLE:wrist) AND PUB_YEAR:[2015 TO 2026]` | 3 |
| E14 | `TITLE:"SleepPPG-Net"` | 1 |

Europe PMC `DOI:"..."` lookups (`resultType=core`) were then run for 63 known-candidate DOIs (standard
references and papers named in the brief) to confirm metadata and check them against
`known-dois.tsv`; 61 resolved, 2 were confirmed through Crossref instead (`10.1123/jmpb.2018-0063`,
`10.1145/3397325`).

OpenAlex `/works?search=` (from 2010, sorted by citations), used only as a cross-check because
relevance ranking was noisy: "sleep staging photoplethysmography wearable deep learning" 818; "sleep
regularity metrics comparison" 8,480; "consumer sleep tracker polysomnography meta-analysis" 1,530;
"actigraphy sleep wake algorithm open source" 3,006. OpenAlex DOI lookups were used to find
open-access locations for papers with no PMC copy.

Crossref `/works/<doi>`: 5 metadata checks (GGIR, Zhai 2020, Czeisler 2025, Plekhanova 2023, plus
GGIR again in the final metadata pass).

arXiv: `export.arxiv.org/robots.txt` disallows all paths, so the arXiv API was not queried. One PDF was
fetched from `arxiv.org/pdf/` (allowed by arxiv.org's robots.txt) after OpenAlex listed it as the
green copy of SleepPPG-Net.

PDF retrieval notes: the Europe PMC article render (`europepmc.org/articles/<PMCID>?pdf=render`) and
its backend returned a Cloudflare bot check for every PMCID this pass; NCBI PMC article pages are
disallowed by robots.txt. MDPI (access denied), PeerJ, BioMed Central/Springer, HAL, OUP, Wiley and
Human Kinetics also returned bot checks or errors. Nature, PLOS and arXiv served PDFs directly. Every
stored PDF starts with `%PDF` and `pypdf` extracted its own title words from the first two pages.

Screening: abstracts read for every kept paper. Excluded as out of lane: single-device validations
(Module 1), association studies that only use the SRI as an exposure (dementia, stroke, alcohol,
rugby), social jetlag outcome meta-analyses, EEG headband and apnea-detection reviews, and the AASM
actigraphy clinical guideline itself (`10.5664/jcsm.7230`, Lane A; its companion systematic review is
S-B27).

## 2. Catalogue rows

| # | Title | Authors | Venue / Year | DOI / URL | OA status | PDF | What it establishes |
|---|---|---|---|---|---|---|---|
| S-B01 | Irregular sleep/wake patterns are associated with poorer academic performance and delayed circadian and sleep/wake timing | Phillips AJK, Clerx WM, O'Brien CS, Sano A, Barger LK, Picard RW, Lockley SW, Klerman EB, et al | *Scientific reports* 2017 | [10.1038/s41598-017-03171-4](https://doi.org/10.1038/s41598-017-03171-4) | **Verified OA** | [2017-phillips-scientificreports-irregular-sleep-wake-patterns-academic-performance-circadian.pdf](literature/2017-phillips-scientificreports-irregular-sleep-wake-patterns-academic-performance-circadian.pdf) | Metrics. Introduced the Sleep Regularity Index (SRI), the probability of being in the same sleep or wake state at times 24 hours apart, in 61 students over 30 days. Irregular sleepers had a later melatonin onset and lower-amplitude light exposure, and SRI correlated with academic performance. |
| S-B02 | Measuring sleep regularity: theoretical properties and practical usage of existing metrics | Fischer D, Klerman EB, Phillips AJK | *Sleep* 2021 | [10.1093/sleep/zsab103](https://doi.org/10.1093/sleep/zsab103) | **OA but not obtained this pass** | none, not stored | Metrics. Simulation study comparing five regularity metrics (standard deviation, interdaily stability, social jet lag, composite phase deviation, SRI). They capture different timescales: StDev and IS need over a week of data for unbiased estimates, CPD and SRI need larger samples, and social jet lag captures only weekly change. |
| S-B03 | Validation of the Sleep Regularity Index in Older Adults and Associations with Cardiometabolic Risk | Lunsford-Avery JR, Engelhard MM, Navar AM, Kollins SH | *Scientific reports* 2018 | [10.1038/s41598-018-32402-5](https://doi.org/10.1038/s41598-018-32402-5) | **Verified OA** | [2018-lunsfordavery-scientificreports-validation-sleep-regularity-index-older-adults.pdf](literature/2018-lunsfordavery-scientificreports-validation-sleep-regularity-index-older-adults.pdf) | Metrics. External validation of the SRI from actigraphy in 1,978 older adults in MESA. Irregularity was independent of sleep duration and tracked later sleep timing, daytime sleep, lower light exposure and cardiometabolic risk. |
| S-B04 | Comparison of Sleep Regularity Index scores calculated by open-source packages and implications for outcomes research: rationale and design of the RIRI statement (Reporting Items for Regularity Indices) | Czeisler MÉ, Leota J, Le F, Campbell-Brown B, Rajaratnam SMW, Pase MP, Kramer DB | *Sleep* 2026 | [10.1093/sleep/zsaf299](https://doi.org/10.1093/sleep/zsaf299) | **Paywalled** | none, not stored | Metrics. In 73,794 accelerometer records, SRI scores from two open-source calculators (sleepreg and GGIR) differed markedly, and the choice of calculator alone changed associations with mortality, diabetes and atrial fibrillation. Proposes a 14-item reporting checklist for regularity indices (RIRI). |
| S-B05 | Social jetlag: misalignment of biological and social time | Wittmann M, Dinich J, Merrow M, Roenneberg T | *Chronobiology international* 2006 | [10.1080/07420520500545979](https://doi.org/10.1080/07420520500545979) | **Paywalled** | none, not stored | Metrics. Standard reference that defined social jetlag as the gap in mid-sleep timing between work days and free days, measured with the Munich ChronoType Questionnaire in 501 volunteers. Pre-2010 but still the source definition. |
| S-B06 | Chronotype and Social Jetlag: A (Self-) Critical Review | Roenneberg T, Pilz LK, Zerbini G, Winnebeck EC | *Biology* 2019 | [10.3390/biology8030054](https://doi.org/10.3390/biology8030054) | **OA but not obtained this pass** | none, not stored | Metrics. Review by the originators of the MCTQ that restates how chronotype (mid-sleep on free days, corrected for sleep debt) and social jetlag are defined and computed, and addresses common misuses of both. |
| S-B07 | A fresh look at the use of nonparametric analysis in actimetry | Gonçalves BS, Adamowicz T, Louzada FM, Moreno CR, Araujo JF | *Sleep medicine reviews* 2015 | [10.1016/j.smrv.2014.06.002](https://doi.org/10.1016/j.smrv.2014.06.002) | **Paywalled** | none, not stored | Metrics. Review of nonparametric rest-activity measures from actimetry (interdaily stability, intradaily variability, relative amplitude, M10 and L5) and what each says about circadian stability, fragmentation and amplitude, as distinct from sleep scoring. |
| S-B08 | Measures of fragmentation of rest activity patterns: mathematical properties and interpretability based on accelerometer real life data | Danilevicz IM, van Hees VT, van der Heide FCT, Jacob L, Landré B, Benadjaoud MA, Sabia S | *BMC medical research methodology* 2024 | [10.1186/s12874-024-02255-w](https://doi.org/10.1186/s12874-024-02255-w) | **OA but not obtained this pass** | none, not stored | Metrics. Gives mathematical proofs of the ranges of interdaily stability and intradaily variability, proposes estimators for transition probability and a new activity balance index, and reports their distributions and modest intercorrelation in 2,859 Whitehall II participants. |
| S-B09 | Automatic sleep/wake identification from wrist activity | Cole RJ, Kripke DF, Gruen W, Mullaney DJ, Gillin JC | *Sleep* 1992 | [10.1093/sleep/15.5.461](https://doi.org/10.1093/sleep/15.5.461) | **OA but not obtained this pass** | none, not stored | Algorithms. Standard reference for the Cole-Kripke algorithm: weighted moving sums of wrist activity counts scored sleep versus wake against PSG in 41 adults, agreeing about 88 percent of the time. |
| S-B10 | Activity-based sleep-wake identification: an empirical test of methodological issues | Sadeh A, Sharkey KM, Carskadon MA | *Sleep* 1994 | [10.1093/sleep/17.3.201](https://doi.org/10.1093/sleep/17.3.201) | **Paywalled** | none, not stored | Algorithms. Standard reference for the Sadeh algorithm, derived from PSG and wrist actigraphy in 20 adults and 16 adolescents. Epoch agreement was 91 to 93 percent, results were similar on either wrist, and agreement was consistently higher for sleep than for wake. |
| S-B11 | A Novel, Open Access Method to Assess Sleep Duration Using a Wrist-Worn Accelerometer | van Hees VT, Sabia S, Anderson KN, Denton SJ, Oliver J, Catt M, Abell JG, Kivimäki M, et al | *PloS one* 2015 | [10.1371/journal.pone.0142533](https://doi.org/10.1371/journal.pone.0142533) | **Verified OA** | [2015-vanhees-plosone-novel-open-access-method-sleep-duration-wrist.pdf](literature/2015-vanhees-plosone-novel-open-access-method-sleep-duration-wrist.pdf) | Algorithms. Origin of the van Hees sustained-inactivity method: sleep is detected as no change in arm angle above 5 degrees for 5 minutes or more inside a diary-defined window. Developed on 4,094 Whitehall II participants with raw wrist accelerometry. |
| S-B12 | Estimating sleep parameters using an accelerometer without sleep diary | van Hees VT, Sabia S, Jones SE, Wood AR, Anderson KN, Kivimäki M, Frayling TM, Pack AI, et al | *Scientific reports* 2018 | [10.1038/s41598-018-31266-z](https://doi.org/10.1038/s41598-018-31266-z) | **Verified OA** | [2018-vanhees-scientificreports-estimating-sleep-parameters-accelerometer-without-sleep-diary.pdf](literature/2018-vanhees-scientificreports-estimating-sleep-parameters-accelerometer-without-sleep-diary.pdf) | Algorithms. Origin of the HDCZA heuristic that detects the sleep period time window from the variance of the z-angle without a sleep diary. The window matched diaries within about 3 to 11 minutes and reached a C-statistic of 0.83 to 0.86 against PSG. |
| S-B13 | GGIR: A Research Community-Driven Open Source R Package for Generating Physical Activity and Sleep Outcomes From Multi-Day Raw Accelerometer Data | Migueles JH, Rowlands AV, Huber F, Sabia S, van Hees VT | *Journal for the Measurement of Physical Behaviour* 2019 | [10.1123/jmpb.2018-0063](https://doi.org/10.1123/jmpb.2018-0063) | **OA but not obtained this pass** | none, not stored | Algorithms. Reference paper for GGIR, the open-source R package that turns raw multi-day accelerometer data into physical activity and sleep outcomes. It describes the processing pipeline and the published methods each step is based on. |
| S-B14 | Validation of an automated sleep detection algorithm using data from multiple accelerometer brands | Plekhanova T, Rowlands AV, Davies MJ, Hall AP, Yates T, Edwardson CL | *Journal of sleep research* 2023 | [10.1111/jsr.13760](https://doi.org/10.1111/jsr.13760) | **OA but not obtained this pass** | none, not stored | Algorithms. The GGIR sleep algorithm applied to Axivity, GENEActiv and ActiGraph worn on both wrists in 30 adults against PSG. Sleep period, duration, onset and waking time fell within a 10 percent equivalence zone, but WASO and sleep efficiency agreed poorly. |
| S-B15 | Estimating sleep duration: performance of open-source processing of actigraphy compared to in-laboratory polysomnography in the community | Sansom K, Reynolds A, McVeigh J, Mazzotti DR, Dhaliwal SS, Maddison K, Walsh J, Singh B, et al | *Sleep advances* 2023 | [10.1093/sleepadvances/zpad028](https://doi.org/10.1093/sleepadvances/zpad028) | **OA but not obtained this pass** | none, not stored | Algorithms. In 835 middle-aged adults, GGIR processing of ActiGraph data, with or without a diary, overestimated PSG total sleep time by about 26 to 31 minutes, with poor agreement (ICC 0.27 to 0.44). Error grew with longer wake overnight, and the proprietary ActiLife algorithm overestimated more. |
| S-B16 | Benchmark on a large cohort for sleep-wake classification with machine learning techniques | Palotti J, Mall R, Aupetit M, Rueschman M, Singh M, Sathyanarayana A, Taheri S, Fernandez-Luque L | *NPJ digital medicine* 2019 | [10.1038/s41746-019-0126-9](https://doi.org/10.1038/s41746-019-0126-9) | **Verified OA** | [2019-palotti-npjdigitalmedicine-benchmark-large-cohort-sleep-wake-classification.pdf](literature/2019-palotti-npjdigitalmedicine-benchmark-large-cohort-sleep-wake-classification.pdf) | Algorithms. Builds a public benchmark of synchronised actigraphy and PSG from the MESA Sleep study and compares classic heuristic algorithms with machine learning models on it. Two classic algorithms beat the device's native scoring, and CNN and LSTM models scored highest. |
| S-B17 | Statistical machine learning of sleep and physical activity phenotypes from sensor data in 96,220 UK Biobank participants | Willetts M, Hollowell S, Aslett L, Holmes C, Doherty A | *Scientific reports* 2018 | [10.1038/s41598-018-26174-1](https://doi.org/10.1038/s41598-018-26174-1) | **Verified OA** | [2018-willetts-scientificreports-statistical-machine-learning-sleep-physical-activity-uk-biobank.pdf](literature/2018-willetts-scientificreports-statistical-machine-learning-sleep-physical-activity-uk-biobank.pdf) | Algorithms. Balanced random forests with hidden Markov smoothing classify sleep and activity modes from wrist accelerometry with 87 percent accuracy in free-living data from 132 adults, then applied to 96,220 UK Biobank participants. |
| S-B18 | Self-supervised learning of accelerometer data provides new insights for sleep and its association with mortality | Yuan H, Plekhanova T, Walmsley R, Reynolds AC, Maddison KJ, Bucan M, Gehrman P, Rowlands A, et al | *NPJ digital medicine* 2024 | [10.1038/s41746-024-01065-0](https://doi.org/10.1038/s41746-024-01065-0) | **Verified OA** | [2024-yuan-npjdigitalmedicine-self-supervised-learning-accelerometer-sleep-mortality.pdf](literature/2024-yuan-npjdigitalmedicine-self-supervised-learning-accelerometer-sleep-mortality.pdf) | Algorithms. A self-supervised deep network for sleep staging from wrist accelerometry, trained on 1,448 PSG nights. External validation showed fair to moderate agreement (total sleep bias 34.7 minutes, wide limits for REM and NREM), and the model was then applied in UK Biobank. |
| S-B19 | 40 years of actigraphy in sleep medicine and current state of the art algorithms | Patterson MR, Nunes AAS, Gerstel D, Pilkar R, Guthrie T, Neishabouri A, Guo CC | *NPJ digital medicine* 2023 | [10.1038/s41746-023-00802-1](https://doi.org/10.1038/s41746-023-00802-1) | **Verified OA** | [2023-patterson-npjdigitalmedicine-40-years-actigraphy-sleep-medicine-algorithms.pdf](literature/2023-patterson-npjdigitalmedicine-40-years-actigraphy-sleep-medicine-algorithms.pdf) | Algorithms. Independent head-to-head of 8 published sleep-wake algorithms on one PSG dataset. Simple regression and heuristic algorithms did slightly better than complex machine learning and deep learning models, which generalised poorly. |
| S-B20 | Ambulatory sleep scoring using accelerometers-distinguishing between nonwear and sleep/wake states | Barouni A, Ottenbacher J, Schneider J, Feige B, Riemann D, Herlan A, El Hardouz D, McLennan D | *PeerJ* 2020 | [10.7717/peerj.8284](https://doi.org/10.7717/peerj.8284) | **OA but not obtained this pass** | none, not stored | Algorithms. An algorithm that separates nonwear, sleep and wake in wrist and chest accelerometry, using the respiration signature in the acceleration spectrum to recognise worn but still periods. Median kappa about 0.83 in 98 participants against PSG and annotated nonwear. |
| S-B21 | Detecting Sleep and Nonwear in 24-h Wrist Accelerometer Data from the National Health and Nutrition Examination Survey | Thapa-Chhetry B, Arguello DJ, John D, Intille S | *Medicine and science in sports and exercise* 2022 | [10.1249/mss.0000000000002973](https://doi.org/10.1249/mss.0000000000002973) | **OA but not obtained this pass** | none, not stored | Algorithms. A machine learning algorithm that labels 24-hour wrist accelerometry as wake-wear, sleep-wear or nonwear, built for NHANES filtered data and extended to raw data. F1 scores were 0.84 to 0.97 on independent validation sets. |
| S-B22 | Sleep stage prediction with raw acceleration and photoplethysmography heart rate data derived from a consumer wearable device | Walch O, Huang Y, Forger D, Goldstein C | *Sleep* 2019 | [10.1093/sleep/zsz180](https://doi.org/10.1093/sleep/zsz180) | **OA but not obtained this pass** | none, not stored | Algorithms. Open, disclosed classifiers using raw acceleration, heart rate variability features and a circadian clock proxy from a consumer watch against PSG, with code and data released. Sleep-wake accuracy was 90 percent with 60 percent wake specificity, and wake/NREM/REM accuracy about 72 percent. |
| S-B23 | Deep learning for automated sleep staging using instantaneous heart rate | Sridhar N, Shoeb A, Stephens P, Kharbouch A, Shimol DB, Burkart J, Ghoreyshi A, Myers L | *NPJ digital medicine* 2020 | [10.1038/s41746-020-0291-x](https://doi.org/10.1038/s41746-020-0291-x) | **Verified OA** | [2020-sridhar-npjdigitalmedicine-deep-learning-sleep-staging-instantaneous-heart-rate.pdf](literature/2020-sridhar-npjdigitalmedicine-deep-learning-sleep-staging-instantaneous-heart-rate.pdf) | Physiological limits. A deep learning model scores four classes (wake, light, deep, REM) from instantaneous heart rate alone, trained on over 10,000 SHHS and MESA nights, reaching 0.77 accuracy and kappa 0.66. Shows how far cardiac rhythm alone can go in staging. |
| S-B24 | A deep transfer learning approach for wearable sleep stage classification with photoplethysmography | Radha M, Fonseca P, Moreau A, Ross M, Cerny A, Anderer P, Long X, Aarts RM | *NPJ digital medicine* 2021 | [10.1038/s41746-021-00510-8](https://doi.org/10.1038/s41746-021-00510-8) | **Verified OA** | [2021-radha-npjdigitalmedicine-deep-transfer-learning-wearable-sleep-stage-ppg.pdf](literature/2021-radha-npjdigitalmedicine-deep-transfer-learning-wearable-sleep-stage-ppg.pdf) | Physiological limits. Transfer learning from a large ECG sleep dataset to wrist PPG gave four-class staging with kappa 0.65 and 76 percent accuracy in 60 healthy adults. Shows that small PPG datasets limit model training and how ECG data can compensate. |
| S-B25 | SleepPPG-Net: A Deep Learning Algorithm for Robust Sleep Staging From Continuous Photoplethysmography | Kotzen K, Charlton PH, Salabi S, Amar L, Landesberg A, Behar JA | *IEEE journal of biomedical and health informatics* 2023 | [10.1109/jbhi.2022.3225363](https://doi.org/10.1109/jbhi.2022.3225363) | **Verified OA** | [2023-kotzen-ieeejbhi-sleepppg-net-deep-learning-sleep-staging-ppg.pdf](literature/2023-kotzen-ieeejbhi-sleepppg-net-deep-learning-sleep-staging-ppg.pdf) | Physiological limits. End-to-end deep learning for four-class staging from the raw PPG waveform, trained on 2,374 patients from two public databases, with median kappa 0.75 against 0.69 for the best feature-based approach. The PDF stored is the arXiv version. |
| S-B26 | Agreement between actigraphic and polysomnographic measures of sleep in adults with and without chronic conditions: A systematic review and meta-analysis | Conley S, Knies A, Batten J, Ash G, Miner B, Hwang Y, Jeon S, Redeker NS | *Sleep medicine reviews* 2019 | [10.1016/j.smrv.2019.05.001](https://doi.org/10.1016/j.smrv.2019.05.001) | **OA but not obtained this pass** | none, not stored | Pooled accuracy. Meta-analysis of 96 actigraphy versus PSG studies (4,134 participants). Actigraphy overestimated TST by about 22 minutes and sleep efficiency by about 5 percent in adults with chronic conditions, and these errors were consistently larger than in healthy adults. |
| S-B27 | Use of Actigraphy for the Evaluation of Sleep Disorders and Circadian Rhythm Sleep-Wake Disorders: An American Academy of Sleep Medicine Systematic Review, Meta-Analysis, and GRADE Assessment | Smith MT, McCrae CS, Cheung J, Martin JL, Harrod CG, Heald JL, Carden KA | *Journal of clinical sleep medicine* 2018 | [10.5664/jcsm.7228](https://doi.org/10.5664/jcsm.7228) | **OA but not obtained this pass** | none, not stored | Pooled accuracy. The systematic review and meta-analysis of 81 studies behind the AASM actigraphy guideline. Actigraphy gives objective sleep data that differ from sleep logs across insomnia, circadian, breathing and hypersomnolence disorders, but it is not reliable for periodic limb movements. |
| S-B28 | A systematic review of the accuracy of sleep wearable devices for estimating sleep onset | Scott H, Lack L, Lovato N | *Sleep medicine reviews* 2020 | [10.1016/j.smrv.2019.101227](https://doi.org/10.1016/j.smrv.2019.101227) | **Paywalled** | none, not stored | Pooled accuracy. Systematic review of 71 studies comparing wearable estimates of sleep onset latency against PSG. Actigraphy averages were often close to PSG but varied widely between individuals, and EEG-based devices were more accurate and less variable. |
| S-B29 | A Systematic Review of Sensing Technologies for Wearable Sleep Staging | Imtiaz SA | *Sensors* 2021 | [10.3390/s21051562](https://doi.org/10.3390/s21051562) | **OA but not obtained this pass** | none, not stored | Pooled accuracy. Systematic review of 90 papers covering 13 sensing modalities for wearable sleep staging. EEG is the only modality that identifies every stage, and PPG-based systems are easier to wear but cannot identify all stages. |
| S-B30 | Performance of consumer wrist-worn sleep tracking devices compared to polysomnography: a meta-analysis | Lee YJ, Lee JY, Cho JH, Kang YJ, Choi JH | *Journal of clinical sleep medicine* 2025 | [10.5664/jcsm.11460](https://doi.org/10.5664/jcsm.11460) | **OA but not obtained this pass** | none, not stored | Pooled accuracy. Meta-analysis of 24 studies (798 participants) of consumer wrist trackers across many brands against PSG. Pooled trackers underestimated TST by about 17 minutes and sleep efficiency by about 5 percent, and overestimated WASO by about 13 minutes. |
| S-B31 | Performance of seven consumer sleep-tracking devices compared with polysomnography | Chinoy ED, Cuellar JA, Huwa KE, Jameson JT, Watson CH, Bessman SC, Hirsch DA, Cooper AD, et al | *Sleep* 2021 | [10.1093/sleep/zsaa291](https://doi.org/10.1093/sleep/zsaa291) | **OA but not obtained this pass** | none, not stored | Pooled accuracy. Head-to-head of four wearable and three nearable consumer trackers plus actigraphy against PSG in 34 adults over three nights. Epoch sensitivity was at least 0.93 but specificity only 0.18 to 0.54, stage estimates were inconsistent, and performance dropped on disrupted nights. |
| S-B32 | Evaluating reliability in wearable devices for sleep staging | Birrer V, Elgendi M, Lambercy O, Menon C | *NPJ digital medicine* 2024 | [10.1038/s41746-024-01016-9](https://doi.org/10.1038/s41746-024-01016-9) | **Verified OA** | [2024-birrer-npjdigitalmedicine-evaluating-reliability-wearable-devices-sleep-staging.pdf](literature/2024-birrer-npjdigitalmedicine-evaluating-reliability-wearable-devices-sleep-staging.pdf) | Physiological limits. Scoping review of 35 studies and 62 wearable setups. Accelerometer-only devices work for sleep-wake but not multi-stage staging, while those adding PPG do better. Five recommendations for validation include equity in samples and consistent reporting. |
| S-B33 | Limiting racial disparities and bias for wearable devices in health science research | Colvonen PJ, DeYoung PN, Bosompra NA, Owens RL | *Sleep* 2020 | [10.1093/sleep/zsaa159](https://doi.org/10.1093/sleep/zsaa159) | **OA but not obtained this pass** | none, not stored | Physiological limits. Commentary on how wrist PPG and other wearable sensors may perform differently by skin tone, and how validation samples that underrepresent darker skin can carry this bias into health research. No abstract, and the full text was not read this pass. |
| S-B34 | Home is where sleep is: an ecological approach to test the validity of actigraphy for the assessment of insomnia | Sánchez-Ortuño MM, Edinger JD, Means MK, Almirall D | *Journal of clinical sleep medicine* 2010 | [10.5664/jcsm.27706](https://doi.org/10.5664/jcsm.27706) | **OA but not obtained this pass** | none, not stored | Physiological limits. Home actigraphy and PSG over three nights in 31 people with insomnia and 31 normal sleepers. Actigraphy consistently gave a shorter sleep onset latency than PSG, while WASO, TST and sleep efficiency did not differ. |
| S-B35 | Optimizing actigraphic estimates of polysomnographic sleep features in insomnia disorder | Te Lindert BHW, van der Meijden WP, Wassing R, Lakbila-Kamal O, Wei Y, Van Someren EJW, Ramautar JR | *Sleep* 2020 | [10.1093/sleep/zsaa090](https://doi.org/10.1093/sleep/zsaa090) | **OA but not obtained this pass** | none, not stored | Physiological limits. Actigraphy against PSG over 210 lab nights in insomnia disorder and matched controls, testing 150 algorithm parameter settings. Errors were larger in insomnia (TST error 29 versus 17 minutes), and one uncommon setting gave near-optimal estimates in both groups. |

## 3. Records

```json
[
 {
  "id": "S-B01",
  "doi": "10.1038/s41598-017-03171-4",
  "pmid": "28607474",
  "pmcid": "PMC5468315",
  "title": "Irregular sleep/wake patterns are associated with poorer academic performance and delayed circadian and sleep/wake timing",
  "year": 2017,
  "pdf": "literature/2017-phillips-scientificreports-irregular-sleep-wake-patterns-academic-performance-circadian.pdf",
  "pdf_status": "stored"
 },
 {
  "id": "S-B02",
  "doi": "10.1093/sleep/zsab103",
  "pmid": "33864369",
  "pmcid": "PMC8503839",
  "title": "Measuring sleep regularity: theoretical properties and practical usage of existing metrics",
  "year": 2021,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "S-B03",
  "doi": "10.1038/s41598-018-32402-5",
  "pmid": "30242174",
  "pmcid": "PMC6154967",
  "title": "Validation of the Sleep Regularity Index in Older Adults and Associations with Cardiometabolic Risk",
  "year": 2018,
  "pdf": "literature/2018-lunsfordavery-scientificreports-validation-sleep-regularity-index-older-adults.pdf",
  "pdf_status": "stored"
 },
 {
  "id": "S-B04",
  "doi": "10.1093/sleep/zsaf299",
  "pmid": "41001850",
  "pmcid": null,
  "title": "Comparison of Sleep Regularity Index scores calculated by open-source packages and implications for outcomes research: rationale and design of the RIRI statement (Reporting Items for Regularity Indices)",
  "year": 2026,
  "pdf": null,
  "pdf_status": "paywalled"
 },
 {
  "id": "S-B05",
  "doi": "10.1080/07420520500545979",
  "pmid": "16687322",
  "pmcid": null,
  "title": "Social jetlag: misalignment of biological and social time",
  "year": 2006,
  "pdf": null,
  "pdf_status": "paywalled"
 },
 {
  "id": "S-B06",
  "doi": "10.3390/biology8030054",
  "pmid": "31336976",
  "pmcid": "PMC6784249",
  "title": "Chronotype and Social Jetlag: A (Self-) Critical Review",
  "year": 2019,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "S-B07",
  "doi": "10.1016/j.smrv.2014.06.002",
  "pmid": "25065908",
  "pmcid": null,
  "title": "A fresh look at the use of nonparametric analysis in actimetry",
  "year": 2015,
  "pdf": null,
  "pdf_status": "paywalled"
 },
 {
  "id": "S-B08",
  "doi": "10.1186/s12874-024-02255-w",
  "pmid": "38849718",
  "pmcid": "PMC11157888",
  "title": "Measures of fragmentation of rest activity patterns: mathematical properties and interpretability based on accelerometer real life data",
  "year": 2024,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "S-B09",
  "doi": "10.1093/sleep/15.5.461",
  "pmid": "1455130",
  "pmcid": null,
  "title": "Automatic sleep/wake identification from wrist activity",
  "year": 1992,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "S-B10",
  "doi": "10.1093/sleep/17.3.201",
  "pmid": "7939118",
  "pmcid": null,
  "title": "Activity-based sleep-wake identification: an empirical test of methodological issues",
  "year": 1994,
  "pdf": null,
  "pdf_status": "paywalled"
 },
 {
  "id": "S-B11",
  "doi": "10.1371/journal.pone.0142533",
  "pmid": "26569414",
  "pmcid": "PMC4646630",
  "title": "A Novel, Open Access Method to Assess Sleep Duration Using a Wrist-Worn Accelerometer",
  "year": 2015,
  "pdf": "literature/2015-vanhees-plosone-novel-open-access-method-sleep-duration-wrist.pdf",
  "pdf_status": "stored"
 },
 {
  "id": "S-B12",
  "doi": "10.1038/s41598-018-31266-z",
  "pmid": "30154500",
  "pmcid": "PMC6113241",
  "title": "Estimating sleep parameters using an accelerometer without sleep diary",
  "year": 2018,
  "pdf": "literature/2018-vanhees-scientificreports-estimating-sleep-parameters-accelerometer-without-sleep-diary.pdf",
  "pdf_status": "stored"
 },
 {
  "id": "S-B13",
  "doi": "10.1123/jmpb.2018-0063",
  "pmid": null,
  "pmcid": null,
  "title": "GGIR: A Research Community-Driven Open Source R Package for Generating Physical Activity and Sleep Outcomes From Multi-Day Raw Accelerometer Data",
  "year": 2019,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "S-B14",
  "doi": "10.1111/jsr.13760",
  "pmid": "36317222",
  "pmcid": null,
  "title": "Validation of an automated sleep detection algorithm using data from multiple accelerometer brands",
  "year": 2023,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "S-B15",
  "doi": "10.1093/sleepadvances/zpad028",
  "pmid": "37485312",
  "pmcid": "PMC10362889",
  "title": "Estimating sleep duration: performance of open-source processing of actigraphy compared to in-laboratory polysomnography in the community",
  "year": 2023,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "S-B16",
  "doi": "10.1038/s41746-019-0126-9",
  "pmid": "31304396",
  "pmcid": "PMC6555808",
  "title": "Benchmark on a large cohort for sleep-wake classification with machine learning techniques",
  "year": 2019,
  "pdf": "literature/2019-palotti-npjdigitalmedicine-benchmark-large-cohort-sleep-wake-classification.pdf",
  "pdf_status": "stored"
 },
 {
  "id": "S-B17",
  "doi": "10.1038/s41598-018-26174-1",
  "pmid": "29784928",
  "pmcid": "PMC5962537",
  "title": "Statistical machine learning of sleep and physical activity phenotypes from sensor data in 96,220 UK Biobank participants",
  "year": 2018,
  "pdf": "literature/2018-willetts-scientificreports-statistical-machine-learning-sleep-physical-activity-uk-biobank.pdf",
  "pdf_status": "stored"
 },
 {
  "id": "S-B18",
  "doi": "10.1038/s41746-024-01065-0",
  "pmid": "38769347",
  "pmcid": "PMC11106264",
  "title": "Self-supervised learning of accelerometer data provides new insights for sleep and its association with mortality",
  "year": 2024,
  "pdf": "literature/2024-yuan-npjdigitalmedicine-self-supervised-learning-accelerometer-sleep-mortality.pdf",
  "pdf_status": "stored"
 },
 {
  "id": "S-B19",
  "doi": "10.1038/s41746-023-00802-1",
  "pmid": "36964203",
  "pmcid": "PMC10039037",
  "title": "40 years of actigraphy in sleep medicine and current state of the art algorithms",
  "year": 2023,
  "pdf": "literature/2023-patterson-npjdigitalmedicine-40-years-actigraphy-sleep-medicine-algorithms.pdf",
  "pdf_status": "stored"
 },
 {
  "id": "S-B20",
  "doi": "10.7717/peerj.8284",
  "pmid": "31915581",
  "pmcid": "PMC6942683",
  "title": "Ambulatory sleep scoring using accelerometers-distinguishing between nonwear and sleep/wake states",
  "year": 2020,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "S-B21",
  "doi": "10.1249/mss.0000000000002973",
  "pmid": "36007161",
  "pmcid": "PMC9615811",
  "title": "Detecting Sleep and Nonwear in 24-h Wrist Accelerometer Data from the National Health and Nutrition Examination Survey",
  "year": 2022,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "S-B22",
  "doi": "10.1093/sleep/zsz180",
  "pmid": "31579900",
  "pmcid": "PMC6930135",
  "title": "Sleep stage prediction with raw acceleration and photoplethysmography heart rate data derived from a consumer wearable device",
  "year": 2019,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "S-B23",
  "doi": "10.1038/s41746-020-0291-x",
  "pmid": "32885052",
  "pmcid": "PMC7441407",
  "title": "Deep learning for automated sleep staging using instantaneous heart rate",
  "year": 2020,
  "pdf": "literature/2020-sridhar-npjdigitalmedicine-deep-learning-sleep-staging-instantaneous-heart-rate.pdf",
  "pdf_status": "stored"
 },
 {
  "id": "S-B24",
  "doi": "10.1038/s41746-021-00510-8",
  "pmid": "34526643",
  "pmcid": "PMC8443610",
  "title": "A deep transfer learning approach for wearable sleep stage classification with photoplethysmography",
  "year": 2021,
  "pdf": "literature/2021-radha-npjdigitalmedicine-deep-transfer-learning-wearable-sleep-stage-ppg.pdf",
  "pdf_status": "stored"
 },
 {
  "id": "S-B25",
  "doi": "10.1109/jbhi.2022.3225363",
  "pmid": "36446010",
  "pmcid": null,
  "title": "SleepPPG-Net: A Deep Learning Algorithm for Robust Sleep Staging From Continuous Photoplethysmography",
  "year": 2023,
  "pdf": "literature/2023-kotzen-ieeejbhi-sleepppg-net-deep-learning-sleep-staging-ppg.pdf",
  "pdf_status": "stored"
 },
 {
  "id": "S-B26",
  "doi": "10.1016/j.smrv.2019.05.001",
  "pmid": "31154154",
  "pmcid": "PMC6594867",
  "title": "Agreement between actigraphic and polysomnographic measures of sleep in adults with and without chronic conditions: A systematic review and meta-analysis",
  "year": 2019,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "S-B27",
  "doi": "10.5664/jcsm.7228",
  "pmid": "29991438",
  "pmcid": "PMC6040804",
  "title": "Use of Actigraphy for the Evaluation of Sleep Disorders and Circadian Rhythm Sleep-Wake Disorders: An American Academy of Sleep Medicine Systematic Review, Meta-Analysis, and GRADE Assessment",
  "year": 2018,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "S-B28",
  "doi": "10.1016/j.smrv.2019.101227",
  "pmid": "31901524",
  "pmcid": null,
  "title": "A systematic review of the accuracy of sleep wearable devices for estimating sleep onset",
  "year": 2020,
  "pdf": null,
  "pdf_status": "paywalled"
 },
 {
  "id": "S-B29",
  "doi": "10.3390/s21051562",
  "pmid": "33668118",
  "pmcid": "PMC7956647",
  "title": "A Systematic Review of Sensing Technologies for Wearable Sleep Staging",
  "year": 2021,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "S-B30",
  "doi": "10.5664/jcsm.11460",
  "pmid": "39484805",
  "pmcid": "PMC11874098",
  "title": "Performance of consumer wrist-worn sleep tracking devices compared to polysomnography: a meta-analysis",
  "year": 2025,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "S-B31",
  "doi": "10.1093/sleep/zsaa291",
  "pmid": "33378539",
  "pmcid": "PMC8120339",
  "title": "Performance of seven consumer sleep-tracking devices compared with polysomnography",
  "year": 2021,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "S-B32",
  "doi": "10.1038/s41746-024-01016-9",
  "pmid": "38499793",
  "pmcid": "PMC10948771",
  "title": "Evaluating reliability in wearable devices for sleep staging",
  "year": 2024,
  "pdf": "literature/2024-birrer-npjdigitalmedicine-evaluating-reliability-wearable-devices-sleep-staging.pdf",
  "pdf_status": "stored"
 },
 {
  "id": "S-B33",
  "doi": "10.1093/sleep/zsaa159",
  "pmid": "32893865",
  "pmcid": "PMC8477341",
  "title": "Limiting racial disparities and bias for wearable devices in health science research",
  "year": 2020,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "S-B34",
  "doi": "10.5664/jcsm.27706",
  "pmid": "20191934",
  "pmcid": "PMC2823272",
  "title": "Home is where sleep is: an ecological approach to test the validity of actigraphy for the assessment of insomnia",
  "year": 2010,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "S-B35",
  "doi": "10.1093/sleep/zsaa090",
  "pmid": "32648912",
  "pmcid": null,
  "title": "Optimizing actigraphic estimates of polysomnographic sleep features in insomnia disorder",
  "year": 2020,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 }
]
```

## 4. Already in the KB, and needs hand download

### Already in the KB

- Rahimi-Eichi H et al 2021, *Open-source longitudinal sleep analysis from accelerometer data
  (DPSleep)*, JMIR mHealth uHealth, [10.2196/29849](https://doi.org/10.2196/29849). Open-source
  sleep algorithm, Lane B in substance. In `module-01-wearables/literature-library.md` (L080) and the
  Module 3 ledger.
- Schyvens AM et al 2025, *A performance validation of six commercial wrist-worn wearable devices for
  sleep stage scoring compared to polysomnography*, SLEEP Advances,
  [10.1093/sleepadvances/zpaf021](https://doi.org/10.1093/sleepadvances/zpaf021). Cross-device
  head-to-head, in `module-01-wearables/literature-library.md`.
- Chee MWL et al 2025, World Sleep Society recommendations,
  [10.1016/j.sleep.2025.106506](https://doi.org/10.1016/j.sleep.2025.106506). Skipped as instructed
  (already in the sleep catalogue, Lane A).

### Needs hand download

Free to read, but every automated route hit a bot check this pass.

- S-B02 Measuring sleep regularity: theoretical properties and practical usage of existing metrics (OUP hybrid OA, also PMC): https://doi.org/10.1093/sleep/zsab103, PMC8503839. Save as `2021-fischer-sleep-measuring-sleep-regularity-theoretical-properties-metrics.pdf`.
- S-B06 Chronotype and Social Jetlag: A (Self-) Critical Review (MDPI gold OA): https://doi.org/10.3390/biology8030054, PMC6784249. Save as `2019-roenneberg-biology-chronotype-social-jetlag-self-critical-review.pdf`.
- S-B08 Measures of fragmentation of rest activity patterns: mathematical properties and interpretability based on accelerometer real life data (BMC gold OA, also HAL): https://doi.org/10.1186/s12874-024-02255-w, PMC11157888. Save as `2024-danilevicz-bmcmedresmethodol-measures-fragmentation-rest-activity-patterns-mathematical.pdf`.
- S-B09 Automatic sleep/wake identification from wrist activity (free on OUP (bronze)): https://doi.org/10.1093/sleep/15.5.461. Save as `1992-cole-sleep-automatic-sleep-wake-identification-wrist-activity.pdf`.
- S-B13 GGIR: A Research Community-Driven Open Source R Package for Generating Physical Activity and Sleep Outcomes From Multi-Day Raw Accelerometer Data (Human Kinetics OA): https://doi.org/10.1123/jmpb.2018-0063. Save as `2019-migueles-jmeasphysbehav-ggir-research-community-driven-open-source-package.pdf`.
- S-B14 Validation of an automated sleep detection algorithm using data from multiple accelerometer brands (Wiley, CC BY): https://doi.org/10.1111/jsr.13760. Save as `2023-plekhanova-jsleepres-validation-automated-sleep-detection-multiple-accelerometer-brands.pdf`.
- S-B15 Estimating sleep duration: performance of open-source processing of actigraphy compared to in-laboratory polysomnography in the community (OUP gold OA, also PMC): https://doi.org/10.1093/sleepadvances/zpad028, PMC10362889. Save as `2023-sansom-sleepadvances-estimating-sleep-duration-open-source-processing-actigraphy.pdf`.
- S-B20 Ambulatory sleep scoring using accelerometers-distinguishing between nonwear and sleep/wake states (PeerJ gold OA, also PMC): https://doi.org/10.7717/peerj.8284, PMC6942683. Save as `2020-barouni-peerj-ambulatory-sleep-scoring-accelerometers-nonwear-sleep-wake.pdf`.
- S-B21 Detecting Sleep and Nonwear in 24-h Wrist Accelerometer Data from the National Health and Nutrition Examination Survey (PMC author manuscript): https://doi.org/10.1249/mss.0000000000002973, PMC9615811. Save as `2022-thapachhetry-medscisportsexerc-detecting-sleep-nonwear-24h-wrist-accelerometer-nhanes.pdf`.
- S-B22 Sleep stage prediction with raw acceleration and photoplethysmography heart rate data derived from a consumer wearable device (OUP OA, also PMC): https://doi.org/10.1093/sleep/zsz180, PMC6930135. Save as `2019-walch-sleep-sleep-stage-prediction-raw-acceleration-ppg-heart-rate.pdf`.
- S-B26 Agreement between actigraphic and polysomnographic measures of sleep in adults with and without chronic conditions: A systematic review and meta-analysis (PMC author manuscript): https://doi.org/10.1016/j.smrv.2019.05.001, PMC6594867. Save as `2019-conley-sleepmedrev-agreement-actigraphic-polysomnographic-measures-chronic-conditions.pdf`.
- S-B27 Use of Actigraphy for the Evaluation of Sleep Disorders and Circadian Rhythm Sleep-Wake Disorders: An American Academy of Sleep Medicine Systematic Review, Meta-Analysis, and GRADE Assessment (free in PMC): https://doi.org/10.5664/jcsm.7228, PMC6040804. Save as `2018-smith-jclinsleepmed-actigraphy-evaluation-sleep-disorders-systematic-review-meta-analysis.pdf`.
- S-B29 A Systematic Review of Sensing Technologies for Wearable Sleep Staging (MDPI gold OA, also PMC): https://doi.org/10.3390/s21051562, PMC7956647. Save as `2021-imtiaz-sensors-systematic-review-sensing-technologies-wearable-sleep-staging.pdf`.
- S-B30 Performance of consumer wrist-worn sleep tracking devices compared to polysomnography: a meta-analysis (free in PMC): https://doi.org/10.5664/jcsm.11460, PMC11874098. Save as `2025-lee-jclinsleepmed-performance-consumer-wrist-worn-sleep-trackers-meta-analysis.pdf`.
- S-B31 Performance of seven consumer sleep-tracking devices compared with polysomnography (OUP OA, also PMC): https://doi.org/10.1093/sleep/zsaa291, PMC8120339. Save as `2021-chinoy-sleep-performance-seven-consumer-sleep-tracking-devices-polysomnography.pdf`.
- S-B33 Limiting racial disparities and bias for wearable devices in health science research (PMC author manuscript): https://doi.org/10.1093/sleep/zsaa159, PMC8477341. Save as `2020-colvonen-sleep-limiting-racial-disparities-bias-wearable-devices.pdf`.
- S-B34 Home is where sleep is: an ecological approach to test the validity of actigraphy for the assessment of insomnia (free in PMC): https://doi.org/10.5664/jcsm.27706, PMC2823272. Save as `2010-sanchezortuno-jclinsleepmed-home-ecological-validity-actigraphy-insomnia.pdf`.
- S-B35 Optimizing actigraphic estimates of polysomnographic sleep features in insomnia disorder (free on OUP (bronze)): https://doi.org/10.1093/sleep/zsaa090. Save as `2020-telindert-sleep-optimizing-actigraphic-estimates-polysomnographic-insomnia-disorder.pdf`.

## 5. Gaps noticed

- Skin tone and sleep: no empirical cross-device study was found that tests sleep staging accuracy by
  skin pigmentation; S-B33 is a commentary. Older adults are covered only indirectly (S-B03, S-B26).
  A targeted search on Fitzpatrick type and PPG sleep staging would be worth a second pass.
- Epoch-by-epoch statistics: the main methods papers (Menghini 2021 framework, Haghayegh 2020
  Bland-Altman and ICC guide) read as guidance, so they were left to Lane A. Lane B has no paper
  dedicated to the statistics of EBE agreement itself, such as kappa versus prevalence-adjusted
  measures for imbalanced wake epochs.
- Phone-based sleep inference (screen-on and accelerometer sleep proxies) and naps or daytime sleep
  detection are not covered here and may need their own query.
