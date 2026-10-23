# Module 5, Cardiac: Lane B seed (measurement science)

Prepared 2026-10-22. Lane B covers cardiac metric definitions (HRV, pulse rate variability, resting heart rate),
device-agnostic algorithms and open methods (PPG beat detection, signal quality, motion artifact handling, AF
detection, toolboxes), reviews and meta-analyses pooling many devices, and physiological limits (skin tone,
motion, perfusion, PPG versus ECG timing, cuffless BP calibration, false positive burden). Guidance, consensus
and evaluation frameworks are left to Lane A. 37 papers kept: 14 PDFs stored and verified, 10 open access but not
obtained this pass, 9 free to read but not stored for licence reasons, 4 paywalled.

## 1. Search log, 2026-10-22

Europe PMC REST (`/search`, `format=json`, `resultType=lite`, `sort=CITED desc`, page size 10 to 20), hit counts as returned:

| # | Query | Hits |
|---|---|---|
| E1 | `(TITLE:"atrial fibrillation") AND (TITLE:smartwatch* OR TITLE:wearable* OR TITLE:photoplethysmograph* OR TITLE:"smart watch*") AND (TITLE:"meta-analysis" OR TITLE:"systematic review") AND PUB_YEAR:[2015 TO 2026]` |  17 |
| E2 | `(TITLE:"heart rate variability") AND (TITLE:wearable* OR TITLE:"portable devices" OR TITLE:photoplethysmograph* OR TITLE:"pulse rate variability") AND (TITLE:"meta-analysis" OR TITLE:"systematic review" OR TITLE:review) AND PUB_YEAR:[2010 TO 2026]` |  13 |
| E3 | `(TITLE:"heart rate") AND (TITLE:wrist* OR TITLE:wearable* OR TITLE:photoplethysmograph*) AND (TITLE:"meta-analysis" OR TITLE:"systematic review") AND PUB_YEAR:[2010 TO 2026]` |  16 |
| E4 | `(TITLE:cuffless OR TITLE:"cuff-less" OR TITLE:"cuff-free") AND TITLE:"blood pressure" AND (TITLE:review OR TITLE:"meta-analysis" OR TITLE:benchmark OR TITLE:calibration) AND PUB_YEAR:[2010 TO 2026]` |  26 |
| E5 | `(TITLE:photoplethysmogra* OR TITLE:PPG) AND (TITLE:"beat detection" OR TITLE:"peak detection" OR TITLE:"detecting beats" OR TITLE:"signal quality" OR TITLE:"quality index") AND PUB_YEAR:[2010 TO 2026]` |  50 |
| E6 | `(TITLE:photoplethysmogra* OR TITLE:PPG) AND (TITLE:"motion artifact*" OR TITLE:"motion artefact*" OR TITLE:"physical exercise") AND TITLE:"heart rate" AND PUB_YEAR:[2010 TO 2026]` |  16 |
| E7 | `(TITLE:"ultra-short" OR TITLE:"ultra short") AND TITLE:"heart rate variability" AND PUB_YEAR:[2010 TO 2026]` |  71 |
| E8 | `(TITLE:"resting heart rate") AND (TITLE:wearable* OR TITLE:variability OR TITLE:intraindividual OR TITLE:definition) AND PUB_YEAR:[2010 TO 2026]` |  138 |
| E9 | `(TITLE:"skin tone" OR TITLE:"skin type" OR TITLE:"skin pigmentation" OR TITLE:"skin color" OR TITLE:"skin colour" OR TITLE:"inaccuracy") AND (TITLE:photoplethysmograph* OR TITLE:"optical heart rate" OR TITLE:"heart rate") AND PUB_YEAR:[2010 TO 2026]` |  16 |
| E10 | `(TITLE:"atrial fibrillation") AND (TITLE:"single lead" OR TITLE:"single-lead" OR TITLE:"short single lead") AND (TITLE:classification OR TITLE:detection OR TITLE:challenge OR TITLE:algorithm*) AND PUB_YEAR:[2015 TO 2026]` |  40 |
| E11 | `(TITLE:"atrial fibrillation") AND (TITLE:photoplethysmograph* OR TITLE:PPG) AND (TITLE:review OR TITLE:"deep learning" OR TITLE:algorithm*) AND PUB_YEAR:[2015 TO 2026]` |  25 |
| E12 | `(TITLE:"pulse transit time" OR TITLE:"pulse arrival time" OR TITLE:"pulse wave analysis") AND TITLE:"blood pressure" AND (TITLE:theory OR TITLE:review OR TITLE:surrogate OR TITLE:"pre-ejection") AND PUB_YEAR:[2010 TO 2026]` |  11 |
| E13 | `(TITLE:"heart rate variability" OR TITLE:"pulse rate variability") AND (TITLE:nocturnal OR TITLE:sleep OR TITLE:reproducibility OR TITLE:autonomic) AND (TITLE:photoplethysmograph* OR TITLE:"pulse rate" OR TITLE:reproducibility) AND PUB_YEAR:[2010 TO 2026]` |  42 |
| E14 | `(TITLE:NeuroKit2 OR TITLE:HeartPy OR TITLE:"open-source toolbox" OR (TITLE:toolbox AND TITLE:"heart rate variability") OR TITLE:pyPPG OR TITLE:"PhysioZoo")` |  82 |
| E15 | `(TITLE:"atrial fibrillation" OR TITLE:"irregular rhythm" OR TITLE:"abnormal pulse") AND (TITLE:"false positive*" OR TITLE:"diagnostic yield" OR TITLE:"overdiagnosis" OR TITLE:"positive predictive" OR TITLE:notification*) AND (TITLE:smartwatch* OR TITLE:wearable* OR TITLE:"Apple Watch" OR TITLE:consumer) AND PUB_YEAR:[2015 TO 2026]` |  5 |
| E16 | Known-item title lookups (Shaffer HRV norms, Natarajan 8 million, Charlton wearable PPG, wrist PPG review, Deep PPG, HRV in psychology), OR-joined | 7 |
| E17 | `(TITLE:photoplethysmograph*) AND (TITLE:review OR TITLE:tutorial) AND PUB_YEAR:[2017 TO 2026]` |  39 |
| E18 | `TITLE:"AF Classification from a Short Single Lead ECG Recording"` |  2 |

Follow-up checks:

- Europe PMC `resultType=core` lookup by `DOI:"..."` for all 45 shortlisted DOIs: titles, authors, year, PMID,
  PMCID, abstract and licence field.
- OpenAlex `/works/doi:...` for the same 45 DOIs (no mailto parameter): `open_access.oa_status` and
  `locations[].license`, used to decide which PDFs could be stored.
- Crossref `/works/{doi}` for HeartPy (10.1016/j.trf.2019.09.015) and a bibliographic query for the 2017
  PhysioNet/CinC Challenge paper (resolved DOI 10.22489/cinc.2017.065-469), since Europe PMC lacked full records.
- arxiv.org/abs/1409.5181 (one request) to read the licence on the TROIKA preprint: arXiv non-exclusive
  distribution licence, so not stored.
- Dedup against `_seed/known-dois.tsv` (483 rows) plus a title grep of Modules 1 to 4: one hit (Fuller 2020, below).
- PDF retrieval: publisher PDF links for CC-licensed items only. Frontiers, PLOS, Nature portfolio, IOP and IEEE
  served PDFs; MDPI and preprints.org returned "Access Denied", and Elsevier (Lancet, JACC), BMJ, OUP and
  europepmc.org returned a Cloudflare check, so those were not pursued. pmc.ncbi.nlm.nih.gov PDF links returned an
  HTML page, not a PDF. One CC BY-NC accepted copy came from the University of Birmingham repository (Gill 2022).
  The CinC 2017 proceedings PDF was fetched to check its footer, found to carry no CC licence, and deleted.
- Each stored PDF starts with `%PDF` and `pypdf` extracted the paper's own title and author text from page 1.

Shortlisted but not kept: Prasitlumkum 2021 (AF meta-analysis, superseded by C-B24), Georgiou 2018 (HRV review,
superseded by C-B22), Fuller 2020 (already in the KB), the HeartPy JORS software paper 10.5334/jors.241 (C-B16
kept instead), a wrist PPG signal quality evaluation (10.1088/1361-6579/ab225a, not screened in full), and a PTT calibration-model
review 10.1109/rbme.2021.3109643 (paywalled, covered by C-B33). Left to Lane A as guidance: the ESH working group
statement on cuffless BP devices (10.1097/hjh.0000000000003224) and the 2025 JAMA Cardiology narrative review on
cuffless BP accuracy and clinical use (10.1001/jamacardio.2025.0662).

## 2. Catalogue rows

| # | Title | Authors | Venue / Year | DOI / URL | OA status | PDF | What it establishes |
|---|---|---|---|---|---|---|---|
| C-B01 | An Overview of Heart Rate Variability Metrics and Norms | Shaffer F, Ginsberg JP | *Frontiers in Public Health* 2017 | [10.3389/fpubh.2017.00258](https://doi.org/10.3389/fpubh.2017.00258) | **Verified OA** | [2017-shaffer-frontpublichealth-overview-heart-rate-variability-metrics-norms.pdf](literature/2017-shaffer-frontpublichealth-overview-heart-rate-variability-metrics-norms.pdf) | Metrics. Review of the mechanisms behind 24 h, short-term (about 5 min) and ultra-short-term (under 5 min) HRV, with definitions of the common time-domain, frequency-domain and non-linear indices and published norms for them. A widely cited reference for what each HRV metric measures and the recording length it assumes. |
| C-B02 | Validity of (Ultra-)Short Recordings for Heart Rate Variability Measurements | Munoz ML, van Roon A, Riese H, Thio C, Oostenbroek E, Westrik I, de Geus EJ, Gansevoort R, et al | *PLoS ONE* 2015 | [10.1371/journal.pone.0138921](https://doi.org/10.1371/journal.pone.0138921) | **Verified OA** | [2015-munoz-plosone-validity-ultra-short-recordings-heart-rate-variability.pdf](literature/2015-munoz-plosone-validity-ultra-short-recordings-heart-rate-variability.pdf) | Metrics. In 3,387 adults, RMSSD and SDNN from 10 s, 30 s and 120 s ECG segments were compared with 240 to 300 s recordings. Agreement rose with length and was near perfect at 120 s; a single 10 s recording gave a valid RMSSD, and RMSSD outperformed SDNN at every length. |
| C-B03 | A Critical Review of Ultra-Short-Term Heart Rate Variability Norms Research | Shaffer F, Meehan ZM, Zerr CL | *Frontiers in Neuroscience* 2020 | [10.3389/fnins.2020.594880](https://doi.org/10.3389/fnins.2020.594880) | **Verified OA** | [2020-shaffer-frontneurosci-critical-review-ultra-short-term-hrv-norms.pdf](literature/2020-shaffer-frontneurosci-critical-review-ultra-short-term-hrv-norms.pdf) | Metrics. Critical review of 28 studies of ultra-short-term HRV (under 5 min). Most did not test criterion validity or relied on correlation and group differences, which do not control for bias; only three used an a priori limits-of-agreement criterion, which the authors argue should be the standard. |
| C-B04 | How accurate is pulse rate variability as an estimate of heart rate variability? A review on studies comparing photoplethysmographic technology with an electrocardiogram | Schäfer A, Vagedes J | *International Journal of Cardiology* 2013 | [10.1016/j.ijcard.2012.03.119](https://doi.org/10.1016/j.ijcard.2012.03.119) | **Paywalled** | none, not stored | Metrics. Review of studies comparing pulse rate variability (from PPG and other pulse waves) with ECG-derived HRV. PRV is a sufficient estimate at rest, though short-term variability tends to be overestimated, while physical activity and some mental stressors degrade agreement, often unacceptably. |
| C-B05 | Pulse rate variability in cardiovascular health: a review on its applications and relationship with heart rate variability | Mejía-Mejía E, May JM, Torres R, Kyriacou PA | *Physiological Measurement* 2020 | [10.1088/1361-6579/ab998c](https://doi.org/10.1088/1361-6579/ab998c) | **Free to read, not stored (licence)** | none, not stored | Metrics. Review of pulse rate variability applications and of studies comparing PRV with HRV. Concludes the relationship is not fully understood, that PRV is affected by physiological as well as technical factors, and that PRV must not be treated as a valid HRV surrogate in all scenarios. |
| C-B06 | Inter- and intraindividual variability in daily resting heart rate and its associations with age, sex, sleep, BMI, and time of year: Retrospective, longitudinal cohort study of 92,457 adults | Quer G, Gouda P, Galarnyk M, Topol EJ, Steinhubl SR | *PLoS ONE* 2020 | [10.1371/journal.pone.0227709](https://doi.org/10.1371/journal.pone.0227709) | **Verified OA** | [2020-quer-plosone-variability-daily-resting-heart-rate-92457-adults.pdf](literature/2020-quer-plosone-variability-daily-resting-heart-rate-92457-adults.pdf) | Metrics. Two years of wrist-tracker data from 92,457 US adults (about 33 million daily values) describing daily resting heart rate. Mean daily RHR was 65 bpm (range 40 to 109 between people), varied with age, sex, BMI, sleep duration and season, and was mostly stable within a person, which supports using an individual's own baseline. |
| C-B07 | Heart rate variability with photoplethysmography in 8 million individuals: a cross-sectional study | Natarajan A, Pantelopoulos A, Emir-Farinas H, Natarajan P | *The Lancet Digital Health* 2020 | [10.1016/s2589-7500(20)30246-6](https://doi.org/10.1016/s2589-7500(20)30246-6) | **OA but not obtained this pass** | none, not stored | Metrics. Cross-sectional analysis of interbeat intervals from 8,203,261 Fitbit users over one day, computing RMSSD, SDRR, HF and LF power on 5 min windows and Poincare measures on 60 min windows. Gives population benchmarks for wrist PPG HRV by age, sex and time of day; HRV metrics declined with age. |
| C-B08 | Reproducibility of Heart Rate Variability Is Parameter and Sleep Stage Dependent | Herzig D, Eser P, Omlin X, Riener R, Wilhelm M, Achermann P | *Frontiers in Physiology* 2017 | [10.3389/fphys.2017.01100](https://doi.org/10.3389/fphys.2017.01100) | **Verified OA** | [2017-herzig-frontphysiol-reproducibility-hrv-parameter-sleep-stage-dependent.pdf](literature/2017-herzig-frontphysiol-reproducibility-hrv-parameter-sleep-stage-dependent.pdf) | Metrics. Three nights of polysomnography in 15 healthy young men, with HRV computed on consecutive 5 min segments by sleep stage. Heart rate was reproducible in all stages and HF power was reproducible in slow wave sleep, while LF power and LF/HF were poorly reproducible in every stage, so nocturnal HRV reliability depends on parameter and stage. |
| C-B09 | Heart Rate Variability in Psychology: A Review of HRV Indices and an Analysis Tutorial | Pham T, Lau ZJ, Chen SHA, Makowski D | *Sensors* 2021 | [10.3390/s21123998](https://doi.org/10.3390/s21123998) | **OA but not obtained this pass** | none, not stored | Metrics. Review and tutorial covering the definitions of time-domain, frequency-domain and non-linear HRV indices and a step-by-step analysis pipeline from ECG, aimed at standardising how HRV is computed and reported in psychology research. |
| C-B10 | Detecting beats in the photoplethysmogram: benchmarking open-source algorithms | Charlton PH, Kotzen K, Mejía-Mejía E, Aston PJ, Budidha K, Mant J, Pettit C, Behar JA, et al | *Physiological Measurement* 2022 | [10.1088/1361-6579/ac826d](https://doi.org/10.1088/1361-6579/ac826d) | **Verified OA** | [2022-charlton-physiolmeas-detecting-beats-photoplethysmogram-benchmarking-open-source.pdf](literature/2022-charlton-physiolmeas-detecting-beats-photoplethysmogram-benchmarking-open-source.pdf) | Algorithms. Benchmarked 15 open-source PPG beat detectors against ECG beats on eight datasets. Eight scored F1 of 90% or more at rest, but performance fell during exercise (F1 55% to 91%), in neonates and in atrial fibrillation; MSPTD and qppg performed best, and the algorithms, data and framework are public. |
| C-B11 | Optimal Signal Quality Index for Photoplethysmogram Signals | Elgendi M | *Bioengineering* 2016 | [10.3390/bioengineering3040021](https://doi.org/10.3390/bioengineering3040021) | **OA but not obtained this pass** | none, not stored | Algorithms. Compared eight PPG signal quality indices (perfusion, kurtosis, skewness, relative power, non-stationarity, zero crossing, entropy, beat-detector matching) against expert labels on 106 recordings. Skewness best separated excellent, acceptable and unfit signals (F1 79% to 87%). |
| C-B12 | Signal-quality indices for the electrocardiogram and photoplethysmogram: derivation and applications to wireless monitoring | Orphanidou C, Bonnici T, Charlton P, Clifton D, Vallance D, Tarassenko L | *IEEE Journal of Biomedical and Health Informatics* 2015 | [10.1109/jbhi.2014.2338351](https://doi.org/10.1109/jbhi.2014.2338351) | **Free to read, not stored (licence)** | none, not stored | Algorithms. Signal quality indices for deciding whether a reliable heart rate can be obtained from wearable ECG and PPG, validated against manual labels (sensitivity and specificity 94% and 97% for ECG, 91% and 95% for PPG). Also shows the index can gate recording to save power with little loss of valid data. |
| C-B13 | TROIKA: a general framework for heart rate monitoring using wrist-type photoplethysmographic signals during intensive physical exercise | Zhang Z, Pi Z, Liu B | *IEEE Transactions on Biomedical Engineering* 2015 | [10.1109/tbme.2014.2359372](https://doi.org/10.1109/tbme.2014.2359372) | **Free to read, not stored (licence)** | none, not stored | Algorithms. TROIKA, a framework of signal decomposition, sparse spectrum reconstruction and spectral peak tracking for wrist PPG heart rate during intense exercise. On 12 subjects running up to 15 km/h the mean absolute error was 2.34 bpm; its dataset became a standard motion-artifact benchmark. arXiv copy is under the non-exclusive arXiv licence, so not stored. |
| C-B14 | Deep PPG: Large-Scale Heart Rate Estimation with Convolutional Neural Networks | Reiss A, Indlekofer I, Schmidt P, Van Laerhoven K | *Sensors* 2019 | [10.3390/s19143079](https://doi.org/10.3390/s19143079) | **OA but not obtained this pass** | none, not stored | Algorithms. Introduced PPG-DaLiA, a large public dataset of wrist PPG and acceleration during daily activities, and an end-to-end CNN on time-frequency spectra. Earlier methods were tuned to small datasets; the CNN cut mean absolute error by 31% on PPG-DaLiA and 21% on WESAD. |
| C-B15 | NeuroKit2: A Python toolbox for neurophysiological signal processing | Makowski D, Pham T, Lau ZJ, Brammer JC, Lespinasse F, Pham H, Schölzel C, Chen SHA | *Behavior Research Methods* 2021 | [10.3758/s13428-020-01516-y](https://doi.org/10.3758/s13428-020-01516-y) | **Free to read, not stored (licence)** | none, not stored | Algorithms. Methods paper for NeuroKit2, an open-source Python package with validated pipelines for ECG, PPG, EDA, EMG and respiration, including peak detection, rate extraction and HRV computation, built for transparent and reproducible physiological signal processing. |
| C-B16 | HeartPy: A novel heart rate algorithm for the analysis of noisy signals | van Gent P, Farah H, van Nes N, van Arem B | *Transportation Research Part F* 2019 | [10.1016/j.trf.2019.09.015](https://doi.org/10.1016/j.trf.2019.09.015) | **Free to read, not stored (licence)** | none, not stored | Algorithms. Methods paper for HeartPy, an open-source Python heart rate and HRV toolkit designed for noisy PPG from low-cost sensors. Abstract not indexed; summary from the title and Crossref metadata, full text not read this pass. |
| C-B17 | AF Classification from a Short Single Lead ECG Recording: the PhysioNet/Computing in Cardiology Challenge 2017 | Clifford GD, Liu C, Moody B, Lehman LH, Silva I, Li Q, Johnson AE, Mark RG | *Computing in Cardiology* 2017 | [10.22489/cinc.2017.065-469](https://doi.org/10.22489/cinc.2017.065-469) | **Free to read, not stored (licence)** | none, not stored | Algorithms. Describes the 2017 PhysioNet/CinC Challenge: over 8,500 short single-lead ECG recordings from a handheld device, labelled normal, AF, other rhythm or too noisy, with a hidden test set. The public dataset and scoring became the common benchmark for single-lead AF classifiers. Proceedings PDF carries no CC licence. |
| C-B18 | Multi-task deep learning for cardiac rhythm detection in wearable devices | Torres-Soto J, Ashley EA | *npj Digital Medicine* 2020 | [10.1038/s41746-020-00320-4](https://doi.org/10.1038/s41746-020-00320-4) | **Verified OA** | [2020-torressoto-npjdigitalmedicine-multi-task-deep-learning-cardiac-rhythm-wearables.pdf](literature/2020-torressoto-npjdigitalmedicine-multi-task-deep-learning-cardiac-rhythm-wearables.pdf) | Algorithms. DeepBeat, a multitask network that jointly scores PPG signal quality and detects AF, pretrained on about one million simulated signals and fine-tuned on over 500,000 labelled signals from three wrist devices. Multitask transfer learning raised F1 from 0.54 to 0.96, and a prospective ambulatory cohort gave sensitivity 0.98 and specificity 0.99. |
| C-B19 | Photoplethysmography based atrial fibrillation detection: a review | Pereira T, Tran N, Gadhoumi K, Pelter MM, Do DH, Lee RJ, Colorado R, Meisel K, et al | *npj Digital Medicine* 2020 | [10.1038/s41746-019-0207-9](https://doi.org/10.1038/s41746-019-0207-9) | **Verified OA** | [2020-pereira-npjdigitalmedicine-photoplethysmography-atrial-fibrillation-detection-review.pdf](literature/2020-pereira-npjdigitalmedicine-photoplethysmography-atrial-fibrillation-detection-review.pdf) | Algorithms. Review of AF detection from PPG covering signal processing, feature-based machine learning and deep learning approaches, with the limits and challenges that stand between these methods and clinical use. |
| C-B20 | Validity of Wrist-Worn photoplethysmography devices to measure heart rate: A systematic review and meta-analysis | Zhang Y, Weaver RG, Armstrong B, Burkart S, Zhang S, Beets MW | *Journal of Sports Sciences* 2020 | [10.1080/02640414.2020.1767348](https://doi.org/10.1080/02640414.2020.1767348) | **Paywalled** | none, not stored | Pooled accuracy. Meta-analysis of 44 studies (738 effect sizes, 15 brands) of wrist PPG heart rate against ECG or chest strap. Mean error was near zero at rest, in sleep and on the treadmill but larger in resistance training (-7.3 bpm) and cycling (-4.6 bpm), and grew by about 3 bpm per 10 bpm rise in heart rate during resistance training. |
| C-B21 | Smartphone Apps Using Photoplethysmography for Heart Rate Monitoring: Meta-Analysis | De Ridder B, Van Rompaey B, Kampen JK, Haine S, Dilles T | *JMIR Cardio* 2018 | [10.2196/cardio.8802](https://doi.org/10.2196/cardio.8802) | **OA but not obtained this pass** | none, not stored | Pooled accuracy. Meta-analysis of 14 studies of smartphone camera PPG apps against validated heart rate methods. Pooled mean difference was -0.32 bpm with correlations of 0.90 or more in adults, while results in children varied with measuring site and heart rate. |
| C-B22 | The Accuracy of Acquiring Heart Rate Variability from Portable Devices: A Systematic Review and Meta-Analysis | Dobbs WC, Fedewa MV, MacDonald HV, Holmes CJ, Cicone ZS, Plews DJ, Esco MR | *Sports Medicine* 2019 | [10.1007/s40279-019-01061-5](https://doi.org/10.1007/s40279-019-01061-5) | **Paywalled** | none, not stored | Pooled accuracy. Meta-analysis of 23 studies (301 effects) comparing HRV from portable devices with ECG. The difference was small but heterogeneous (ES 0.23); the HRV metric, body position and sex, not the device, moderated the error. |
| C-B23 | Smartphone detection of atrial fibrillation using photoplethysmography: a systematic review and meta-analysis | Gill S, Bunting KV, Sartini C, Cardoso VR, Ghoreishi N, Uh HW, Williams JA, Suzart-Woischnik K, et al | *Heart* 2022 | [10.1136/heartjnl-2021-320417](https://doi.org/10.1136/heartjnl-2021-320417) | **Verified OA** | [2022-gill-heart-smartphone-ppg-atrial-fibrillation-meta-analysis.pdf](literature/2022-gill-heart-smartphone-ppg-atrial-fibrillation-meta-analysis.pdf) | Pooled accuracy. Systematic review of smartphone camera PPG for AF against ECG (28 studies, 11,404 participants). Pooled sensitivity was 94% and specificity 97%, but the evidence came from small, biased, mostly secondary-care studies, so the authors call these figures unrealistically high. |
| C-B24 | Accuracy of Smartwatches in the Detection of Atrial Fibrillation: A Systematic Review and Diagnostic Meta-Analysis | Barrera N, Solorzano M, Jimenez Y, Kushnir Y, Gallegos-Koyner F, Dagostin de Carvalho G | *JACC: Advances* 2025 | [10.1016/j.jacadv.2025.102133](https://doi.org/10.1016/j.jacadv.2025.102133) | **OA but not obtained this pass** | none, not stored | Pooled accuracy. Diagnostic meta-analysis of 26 studies (17,349 patients) of smartwatch AF detection. Pooled sensitivity 95% and specificity 97% with very high heterogeneity (I2 95% and 99%); accuracy was similar for PPG-based and ECG-based detection. |
| C-B25 | Atrial fibrillation detection using single lead portable electrocardiographic monitoring: a systematic review and meta-analysis | Ramkumar S, Nerlekar N, D'Souza D, Pol DJ, Kalman JM, Marwick TH | *BMJ Open* 2018 | [10.1136/bmjopen-2018-024178](https://doi.org/10.1136/bmjopen-2018-024178) | **OA but not obtained this pass** | none, not stored | Pooled accuracy. Meta-analysis of AF detection rates with portable single-lead ECG (18 studies, 117,436 people) versus Holter monitoring (36 studies). Portable ECG detected AF in 1.7% of those screened, with significant heterogeneity, and was judged an efficient screening option. |
| C-B26 | Wearable cuffless blood pressure monitoring devices: a systematic review and meta-analysis | Islam SMS, Chow CK, Daryabeygikhotbehsara R, Subedi N, Rawstorn J, Tegegne T, Karmakar C, Siddiqui MU, et al | *European Heart Journal: Digital Health* 2022 | [10.1093/ehjdh/ztac021](https://doi.org/10.1093/ehjdh/ztac021) | **OA but not obtained this pass** | none, not stored | Pooled accuracy. Systematic review and meta-analysis of wearable cuffless BP devices validated up to December 2019. Pooled bias was small but highly heterogeneous, and differing standards and validation protocols prevented identifying the most accurate device or recommending clinical use. |
| C-B27 | Accuracy of Heart Rate Measurement with Wrist-Worn Wearable Devices in Various Skin Tones: a Systematic Review | Koerber D, Khan S, Shamsheri T, Kirubarajan A, Mehta S | *Journal of Racial and Ethnic Health Disparities* 2023 | [10.1007/s40615-022-01446-9](https://doi.org/10.1007/s40615-022-01446-9) | **Free to read, not stored (licence)** | none, not stored | Physiological limits. Systematic review of 10 studies (469 participants) that stratified wrist wearable heart rate or rhythm accuracy by skin tone. Four found lower accuracy in darker skin, four found no effect and two were mixed, so evidence is inconclusive and better-powered studies with objective skin tone measurement are needed. |
| C-B28 | Investigating sources of inaccuracy in wearable optical heart rate sensors | Bent B, Goldstein BA, Kibbe WA, Dunn JP | *npj Digital Medicine* 2020 | [10.1038/s41746-020-0226-6](https://doi.org/10.1038/s41746-020-0226-6) | **Verified OA** | [2020-bent-npjdigitalmedicine-sources-inaccuracy-wearable-optical-heart-rate.pdf](literature/2020-bent-npjdigitalmedicine-sources-inaccuracy-wearable-optical-heart-rate.pdf) | Physiological limits. Tested consumer and research wrist wearables across the full Fitzpatrick range, at rest and during activity, against ECG. Found no significant difference in accuracy by skin tone but significant differences between devices and activity types, with absolute error during activity about 30% higher than at rest. |
| C-B29 | Sources of Inaccuracy in Photoplethysmography for Continuous Cardiovascular Monitoring | Fine J, Branan KL, Rodriguez AJ, Boonya-Ananta T, Ajmal, Ramella-Roman JC, McShane MJ, Coté GL | *Biosensors* 2021 | [10.3390/bios11040126](https://doi.org/10.3390/bios11040126) | **OA but not obtained this pass** | none, not stored | Physiological limits. Review of PPG noise sources grouped as individual factors (skin tone, obesity, age, sex), physiology (respiration, venous pulsation, measurement site, temperature) and external factors (motion, ambient light, contact pressure), relevant to derived measures such as HRV and BP as well as heart rate. |
| C-B30 | Monte Carlo analysis of optical heart rate sensors in commercial wearables: the effect of skin tone and obesity on the photoplethysmography (PPG) signal | Ajmal, Boonya-Ananta T, Rodriguez AJ, Du Le VN, Ramella-Roman JC | *Biomedical Optics Express* 2021 | [10.1364/boe.439893](https://doi.org/10.1364/boe.439893) | **Free to read, not stored (licence)** | none, not stored | Physiological limits. Monte Carlo light-transport modelling of three commercial wrist PPG sensor geometries across Fitzpatrick types 1 to 6 and BMI 20 to 45. Higher BMI and darker skin reduced the PPG signal by up to 61% depending on device geometry. Journal is open access under the publisher's own agreement, not CC. |
| C-B31 | Heart Rate Variability (HRV) and Pulse Rate Variability (PRV) for the Assessment of Autonomic Responses | Mejía-Mejía E, Budidha K, Abay TY, May JM, Kyriacou PA | *Frontiers in Physiology* 2020 | [10.3389/fphys.2020.00779](https://doi.org/10.3389/fphys.2020.00779) | **Verified OA** | [2020-mejiamejia-frontphysiol-hrv-prv-assessment-autonomic-responses.pdf](literature/2020-mejiamejia-frontphysiol-hrv-prv-assessment-autonomic-responses.pdf) | Physiological limits. Whole-body cold exposure in 20 volunteers with PPG at the ear canal, earlobe, finger and toe alongside ECG. PRV indices changed more than HRV during cold exposure and differed from HRV by site, showing that peripheral vasoconstriction makes PRV diverge from HRV. |
| C-B32 | Wearable Photoplethysmography for Cardiovascular Monitoring | Charlton PH, Kyriaco PA, Mant J, Marozas V, Chowienczyk P, Alastruey J | *Proceedings of the IEEE* 2022 | [10.1109/jproc.2022.3149785](https://doi.org/10.1109/jproc.2022.3149785) | **Verified OA** | [2022-charlton-procieee-wearable-photoplethysmography-cardiovascular-monitoring.pdf](literature/2022-charlton-procieee-wearable-photoplethysmography-cardiovascular-monitoring.pdf) | Physiological limits. Survey of wearable PPG fundamentals: how the pulse wave is generated and shaped by the heart and vessels, signal processing, sources of error and the clinical applications in cardiovascular disease, with priorities for research. |
| C-B33 | Toward Ubiquitous Blood Pressure Monitoring via Pulse Transit Time: Theory and Practice | Mukkamala R, Hahn JO, Inan OT, Mestha LK, Kim CS, Töreyin H, Kyal S | *IEEE Transactions on Biomedical Engineering* 2015 | [10.1109/tbme.2015.2441951](https://doi.org/10.1109/tbme.2015.2441951) | **Free to read, not stored (licence)** | none, not stored | Physiological limits. Review of the theory linking pulse transit time to BP and the practical challenges: PTT must be calibrated per person, pulse arrival time includes the pre-ejection period, and vasomotor tone and smooth muscle changes affect PTT independently of BP. Free copy is a PMC author manuscript. |
| C-B34 | Pulse arrival time is not an adequate surrogate for pulse transit time as a marker of blood pressure | Zhang G, Gao M, Xu D, Olivier NB, Mukkamala R | *Journal of Applied Physiology* 2011 | [10.1152/japplphysiol.00980.2011](https://doi.org/10.1152/japplphysiol.00980.2011) | **Paywalled** | none, not stored | Physiological limits. Invasive aortic recordings in six dogs during large induced BP changes. BP tracking error with 1/PAT was about twice that with 1/PTT and failed FDA error limits, showing that pulse arrival time (which includes the pre-ejection period) is not an adequate surrogate for PTT. |
| C-B35 | Pulse arrival time as a surrogate of blood pressure | Finnegan E, Davidson S, Harford M, Jorge J, Watkinson P, Young D, Tarassenko L, Villarroel M | *Scientific Reports* 2021 | [10.1038/s41598-021-01358-4](https://doi.org/10.1038/s41598-021-01358-4) | **Verified OA** | [2021-finnegan-scientificreports-pulse-arrival-time-surrogate-blood-pressure.pdf](literature/2021-finnegan-scientificreports-pulse-arrival-time-surrogate-blood-pressure.pdf) | Physiological limits. In 30 volunteers given phenylephrine, the pre-ejection period rose by 5.5 ms on average while PTT changed by about 17 ms. Compares population and individually calibrated models for BP from PAT or PTT and quantifies the error PEP adds when ECG-to-PPG timing is used as PTT. |
| C-B36 | A benchmark for machine-learning based non-invasive blood pressure estimation using photoplethysmogram | González S, Hsieh WT, Chen TP | *Scientific Data* 2023 | [10.1038/s41597-023-02020-6](https://doi.org/10.1038/s41597-023-02020-6) | **Verified OA** | [2023-gonzalez-scientificdata-benchmark-ml-blood-pressure-estimation-ppg.pdf](literature/2023-gonzalez-scientificdata-benchmark-ml-blood-pressure-estimation-ppg.pdf) | Algorithms. Benchmark for machine-learning BP estimation from PPG alone on four open datasets with shared preprocessing and subject-wise validation, comparing 11 approaches. Shows that ignoring subject leakage across folds and the skewed BP distribution gives misleading, over-optimistic results, which bears on calibration-free claims. |
| C-B37 | Clinical evaluation and diagnostic yield following evaluation of abnormal pulse detected using Apple Watch | Wyatt KD, Poole LR, Mullan AF, Kopecky SL, Heaton HA | *Journal of the American Medical Informatics Association* 2020 | [10.1093/jamia/ocaa137](https://doi.org/10.1093/jamia/ocaa137) | **OA but not obtained this pass** | none, not stored | Physiological limits. Retrospective review of 264 patients evaluated at one health system after an abnormal pulse detected by Apple Watch. A clinically actionable cardiovascular diagnosis was made in 11.4% (15% of those with an explicit alert), with frequent ECGs, Holters and chest x-rays, illustrating the downstream burden of false positive notifications. |

## 3. Records

```json
[
 {
  "id": "C-B01",
  "doi": "10.3389/fpubh.2017.00258",
  "pmid": "29034226",
  "pmcid": "PMC5624990",
  "title": "An Overview of Heart Rate Variability Metrics and Norms",
  "year": 2017,
  "pdf": "module-05-measurement-science/cardiac/literature/2017-shaffer-frontpublichealth-overview-heart-rate-variability-metrics-norms.pdf",
  "pdf_status": "stored"
 },
 {
  "id": "C-B02",
  "doi": "10.1371/journal.pone.0138921",
  "pmid": "26414314",
  "pmcid": "PMC4586373",
  "title": "Validity of (Ultra-)Short Recordings for Heart Rate Variability Measurements",
  "year": 2015,
  "pdf": "module-05-measurement-science/cardiac/literature/2015-munoz-plosone-validity-ultra-short-recordings-heart-rate-variability.pdf",
  "pdf_status": "stored"
 },
 {
  "id": "C-B03",
  "doi": "10.3389/fnins.2020.594880",
  "pmid": "33328866",
  "pmcid": "PMC7710683",
  "title": "A Critical Review of Ultra-Short-Term Heart Rate Variability Norms Research",
  "year": 2020,
  "pdf": "module-05-measurement-science/cardiac/literature/2020-shaffer-frontneurosci-critical-review-ultra-short-term-hrv-norms.pdf",
  "pdf_status": "stored"
 },
 {
  "id": "C-B04",
  "doi": "10.1016/j.ijcard.2012.03.119",
  "pmid": "22809539",
  "pmcid": null,
  "title": "How accurate is pulse rate variability as an estimate of heart rate variability? A review on studies comparing photoplethysmographic technology with an electrocardiogram",
  "year": 2013,
  "pdf": null,
  "pdf_status": "paywalled"
 },
 {
  "id": "C-B05",
  "doi": "10.1088/1361-6579/ab998c",
  "pmid": "32498055",
  "pmcid": null,
  "title": "Pulse rate variability in cardiovascular health: a review on its applications and relationship with heart rate variability",
  "year": 2020,
  "pdf": null,
  "pdf_status": "free_not_redistributable"
 },
 {
  "id": "C-B06",
  "doi": "10.1371/journal.pone.0227709",
  "pmid": "32023264",
  "pmcid": "PMC7001906",
  "title": "Inter- and intraindividual variability in daily resting heart rate and its associations with age, sex, sleep, BMI, and time of year: Retrospective, longitudinal cohort study of 92,457 adults",
  "year": 2020,
  "pdf": "module-05-measurement-science/cardiac/literature/2020-quer-plosone-variability-daily-resting-heart-rate-92457-adults.pdf",
  "pdf_status": "stored"
 },
 {
  "id": "C-B07",
  "doi": "10.1016/s2589-7500(20)30246-6",
  "pmid": "33328029",
  "pmcid": null,
  "title": "Heart rate variability with photoplethysmography in 8 million individuals: a cross-sectional study",
  "year": 2020,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "C-B08",
  "doi": "10.3389/fphys.2017.01100",
  "pmid": "29367845",
  "pmcid": "PMC5767731",
  "title": "Reproducibility of Heart Rate Variability Is Parameter and Sleep Stage Dependent",
  "year": 2017,
  "pdf": "module-05-measurement-science/cardiac/literature/2017-herzig-frontphysiol-reproducibility-hrv-parameter-sleep-stage-dependent.pdf",
  "pdf_status": "stored"
 },
 {
  "id": "C-B09",
  "doi": "10.3390/s21123998",
  "pmid": "34207927",
  "pmcid": "PMC8230044",
  "title": "Heart Rate Variability in Psychology: A Review of HRV Indices and an Analysis Tutorial",
  "year": 2021,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "C-B10",
  "doi": "10.1088/1361-6579/ac826d",
  "pmid": "35853440",
  "pmcid": "PMC9393905",
  "title": "Detecting beats in the photoplethysmogram: benchmarking open-source algorithms",
  "year": 2022,
  "pdf": "module-05-measurement-science/cardiac/literature/2022-charlton-physiolmeas-detecting-beats-photoplethysmogram-benchmarking-open-source.pdf",
  "pdf_status": "stored"
 },
 {
  "id": "C-B11",
  "doi": "10.3390/bioengineering3040021",
  "pmid": "28952584",
  "pmcid": "PMC5597264",
  "title": "Optimal Signal Quality Index for Photoplethysmogram Signals",
  "year": 2016,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "C-B12",
  "doi": "10.1109/jbhi.2014.2338351",
  "pmid": "25069129",
  "pmcid": null,
  "title": "Signal-quality indices for the electrocardiogram and photoplethysmogram: derivation and applications to wireless monitoring",
  "year": 2015,
  "pdf": null,
  "pdf_status": "free_not_redistributable"
 },
 {
  "id": "C-B13",
  "doi": "10.1109/tbme.2014.2359372",
  "pmid": "25252274",
  "pmcid": null,
  "title": "TROIKA: a general framework for heart rate monitoring using wrist-type photoplethysmographic signals during intensive physical exercise",
  "year": 2015,
  "pdf": null,
  "pdf_status": "free_not_redistributable"
 },
 {
  "id": "C-B14",
  "doi": "10.3390/s19143079",
  "pmid": "31336894",
  "pmcid": "PMC6679242",
  "title": "Deep PPG: Large-Scale Heart Rate Estimation with Convolutional Neural Networks",
  "year": 2019,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "C-B15",
  "doi": "10.3758/s13428-020-01516-y",
  "pmid": "33528817",
  "pmcid": null,
  "title": "NeuroKit2: A Python toolbox for neurophysiological signal processing",
  "year": 2021,
  "pdf": null,
  "pdf_status": "free_not_redistributable"
 },
 {
  "id": "C-B16",
  "doi": "10.1016/j.trf.2019.09.015",
  "pmid": null,
  "pmcid": null,
  "title": "HeartPy: A novel heart rate algorithm for the analysis of noisy signals",
  "year": 2019,
  "pdf": null,
  "pdf_status": "free_not_redistributable"
 },
 {
  "id": "C-B17",
  "doi": "10.22489/cinc.2017.065-469",
  "pmid": "29862307",
  "pmcid": "PMC5978770",
  "title": "AF Classification from a Short Single Lead ECG Recording: the PhysioNet/Computing in Cardiology Challenge 2017",
  "year": 2017,
  "pdf": null,
  "pdf_status": "free_not_redistributable"
 },
 {
  "id": "C-B18",
  "doi": "10.1038/s41746-020-00320-4",
  "pmid": "32964139",
  "pmcid": "PMC7481177",
  "title": "Multi-task deep learning for cardiac rhythm detection in wearable devices",
  "year": 2020,
  "pdf": "module-05-measurement-science/cardiac/literature/2020-torressoto-npjdigitalmedicine-multi-task-deep-learning-cardiac-rhythm-wearables.pdf",
  "pdf_status": "stored"
 },
 {
  "id": "C-B19",
  "doi": "10.1038/s41746-019-0207-9",
  "pmid": "31934647",
  "pmcid": "PMC6954115",
  "title": "Photoplethysmography based atrial fibrillation detection: a review",
  "year": 2020,
  "pdf": "module-05-measurement-science/cardiac/literature/2020-pereira-npjdigitalmedicine-photoplethysmography-atrial-fibrillation-detection-review.pdf",
  "pdf_status": "stored"
 },
 {
  "id": "C-B20",
  "doi": "10.1080/02640414.2020.1767348",
  "pmid": "32552580",
  "pmcid": null,
  "title": "Validity of Wrist-Worn photoplethysmography devices to measure heart rate: A systematic review and meta-analysis",
  "year": 2020,
  "pdf": null,
  "pdf_status": "paywalled"
 },
 {
  "id": "C-B21",
  "doi": "10.2196/cardio.8802",
  "pmid": "31758768",
  "pmcid": "PMC6834218",
  "title": "Smartphone Apps Using Photoplethysmography for Heart Rate Monitoring: Meta-Analysis",
  "year": 2018,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "C-B22",
  "doi": "10.1007/s40279-019-01061-5",
  "pmid": "30706234",
  "pmcid": null,
  "title": "The Accuracy of Acquiring Heart Rate Variability from Portable Devices: A Systematic Review and Meta-Analysis",
  "year": 2019,
  "pdf": null,
  "pdf_status": "paywalled"
 },
 {
  "id": "C-B23",
  "doi": "10.1136/heartjnl-2021-320417",
  "pmid": "35277454",
  "pmcid": "PMC9554073",
  "title": "Smartphone detection of atrial fibrillation using photoplethysmography: a systematic review and meta-analysis",
  "year": 2022,
  "pdf": "module-05-measurement-science/cardiac/literature/2022-gill-heart-smartphone-ppg-atrial-fibrillation-meta-analysis.pdf",
  "pdf_status": "stored"
 },
 {
  "id": "C-B24",
  "doi": "10.1016/j.jacadv.2025.102133",
  "pmid": "41182224",
  "pmcid": "PMC12713314",
  "title": "Accuracy of Smartwatches in the Detection of Atrial Fibrillation: A Systematic Review and Diagnostic Meta-Analysis",
  "year": 2025,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "C-B25",
  "doi": "10.1136/bmjopen-2018-024178",
  "pmid": "30224404",
  "pmcid": "PMC6144487",
  "title": "Atrial fibrillation detection using single lead portable electrocardiographic monitoring: a systematic review and meta-analysis",
  "year": 2018,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "C-B26",
  "doi": "10.1093/ehjdh/ztac021",
  "pmid": "36713001",
  "pmcid": "PMC9708022",
  "title": "Wearable cuffless blood pressure monitoring devices: a systematic review and meta-analysis",
  "year": 2022,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "C-B27",
  "doi": "10.1007/s40615-022-01446-9",
  "pmid": "36376641",
  "pmcid": "PMC9662769",
  "title": "Accuracy of Heart Rate Measurement with Wrist-Worn Wearable Devices in Various Skin Tones: a Systematic Review",
  "year": 2023,
  "pdf": null,
  "pdf_status": "free_not_redistributable"
 },
 {
  "id": "C-B28",
  "doi": "10.1038/s41746-020-0226-6",
  "pmid": "32047863",
  "pmcid": "PMC7010823",
  "title": "Investigating sources of inaccuracy in wearable optical heart rate sensors",
  "year": 2020,
  "pdf": "module-05-measurement-science/cardiac/literature/2020-bent-npjdigitalmedicine-sources-inaccuracy-wearable-optical-heart-rate.pdf",
  "pdf_status": "stored"
 },
 {
  "id": "C-B29",
  "doi": "10.3390/bios11040126",
  "pmid": "33923469",
  "pmcid": "PMC8073123",
  "title": "Sources of Inaccuracy in Photoplethysmography for Continuous Cardiovascular Monitoring",
  "year": 2021,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "C-B30",
  "doi": "10.1364/boe.439893",
  "pmid": "35003845",
  "pmcid": "PMC8713672",
  "title": "Monte Carlo analysis of optical heart rate sensors in commercial wearables: the effect of skin tone and obesity on the photoplethysmography (PPG) signal",
  "year": 2021,
  "pdf": null,
  "pdf_status": "free_not_redistributable"
 },
 {
  "id": "C-B31",
  "doi": "10.3389/fphys.2020.00779",
  "pmid": "32792970",
  "pmcid": "PMC7390908",
  "title": "Heart Rate Variability (HRV) and Pulse Rate Variability (PRV) for the Assessment of Autonomic Responses",
  "year": 2020,
  "pdf": "module-05-measurement-science/cardiac/literature/2020-mejiamejia-frontphysiol-hrv-prv-assessment-autonomic-responses.pdf",
  "pdf_status": "stored"
 },
 {
  "id": "C-B32",
  "doi": "10.1109/jproc.2022.3149785",
  "pmid": "35356509",
  "pmcid": "PMC7612541",
  "title": "Wearable Photoplethysmography for Cardiovascular Monitoring",
  "year": 2022,
  "pdf": "module-05-measurement-science/cardiac/literature/2022-charlton-procieee-wearable-photoplethysmography-cardiovascular-monitoring.pdf",
  "pdf_status": "stored"
 },
 {
  "id": "C-B33",
  "doi": "10.1109/tbme.2015.2441951",
  "pmid": "26057530",
  "pmcid": "PMC4515215",
  "title": "Toward Ubiquitous Blood Pressure Monitoring via Pulse Transit Time: Theory and Practice",
  "year": 2015,
  "pdf": null,
  "pdf_status": "free_not_redistributable"
 },
 {
  "id": "C-B34",
  "doi": "10.1152/japplphysiol.00980.2011",
  "pmid": "21960657",
  "pmcid": null,
  "title": "Pulse arrival time is not an adequate surrogate for pulse transit time as a marker of blood pressure",
  "year": 2011,
  "pdf": null,
  "pdf_status": "paywalled"
 },
 {
  "id": "C-B35",
  "doi": "10.1038/s41598-021-01358-4",
  "pmid": "34815419",
  "pmcid": "PMC8611024",
  "title": "Pulse arrival time as a surrogate of blood pressure",
  "year": 2021,
  "pdf": "module-05-measurement-science/cardiac/literature/2021-finnegan-scientificreports-pulse-arrival-time-surrogate-blood-pressure.pdf",
  "pdf_status": "stored"
 },
 {
  "id": "C-B36",
  "doi": "10.1038/s41597-023-02020-6",
  "pmid": "36944668",
  "pmcid": "PMC10030661",
  "title": "A benchmark for machine-learning based non-invasive blood pressure estimation using photoplethysmogram",
  "year": 2023,
  "pdf": "module-05-measurement-science/cardiac/literature/2023-gonzalez-scientificdata-benchmark-ml-blood-pressure-estimation-ppg.pdf",
  "pdf_status": "stored"
 },
 {
  "id": "C-B37",
  "doi": "10.1093/jamia/ocaa137",
  "pmid": "32979046",
  "pmcid": "PMC7526465",
  "title": "Clinical evaluation and diagnostic yield following evaluation of abnormal pulse detected using Apple Watch",
  "year": 2020,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 }
]
```

## 4. Already in the KB, and needs hand download

### Already in the KB

- Fuller D et al 2020, *Reliability and Validity of Commercially Available Wearable Devices for Measuring Steps,
  Energy Expenditure, and Heart Rate: Systematic Review*, JMIR mHealth uHealth,
  [10.2196/18694](https://doi.org/10.2196/18694). Pooled heart rate accuracy across brands, Lane B in substance. Cited
  in `module-01-wearables/sources.md` (S-VAL-03) and `module-01-wearables/profiles/apple-watch-healthkit.md`; not in
  `known-dois.tsv`, found by title grep.

### Needs hand download

CC-licensed, but every automated route hit a bot check or returned HTML this pass.

- C-B07 Heart rate variability with photoplethysmography in 8 million individuals: a cross-sectional study (Lancet Digital Health, CC BY-NC-ND): https://doi.org/10.1016/s2589-7500(20)30246-6. Save as `2020-natarajan-lancetdigitalhealth-hrv-photoplethysmography-8-million-individuals.pdf`.
- C-B09 Heart Rate Variability in Psychology: A Review of HRV Indices and an Analysis Tutorial (MDPI, CC BY): https://doi.org/10.3390/s21123998, PMC8230044. Save as `2021-pham-sensors-hrv-psychology-review-indices-analysis-tutorial.pdf`.
- C-B11 Optimal Signal Quality Index for Photoplethysmogram Signals (MDPI, CC BY): https://doi.org/10.3390/bioengineering3040021, PMC5597264. Save as `2016-elgendi-bioengineering-optimal-signal-quality-index-photoplethysmogram.pdf`.
- C-B14 Deep PPG: Large-Scale Heart Rate Estimation with Convolutional Neural Networks (MDPI, CC BY): https://doi.org/10.3390/s19143079, PMC6679242. Save as `2019-reiss-sensors-deep-ppg-large-scale-heart-rate-estimation-cnn.pdf`.
- C-B21 Smartphone Apps Using Photoplethysmography for Heart Rate Monitoring: Meta-Analysis (JMIR, CC BY): https://doi.org/10.2196/cardio.8802, PMC6834218. Save as `2018-deridder-jmircardio-smartphone-apps-ppg-heart-rate-meta-analysis.pdf`.
- C-B24 Accuracy of Smartwatches in the Detection of Atrial Fibrillation: A Systematic Review and Diagnostic Meta-Analysis (JACC: Advances, CC BY): https://doi.org/10.1016/j.jacadv.2025.102133, PMC12713314. Save as `2025-barrera-jaccadv-smartwatches-atrial-fibrillation-diagnostic-meta-analysis.pdf`.
- C-B25 Atrial fibrillation detection using single lead portable electrocardiographic monitoring: a systematic review and meta-analysis (BMJ Open, CC BY-NC): https://doi.org/10.1136/bmjopen-2018-024178, PMC6144487. Save as `2018-ramkumar-bmjopen-af-detection-single-lead-portable-ecg-systematic-review.pdf`.
- C-B26 Wearable cuffless blood pressure monitoring devices: a systematic review and meta-analysis (OUP, CC BY-NC): https://doi.org/10.1093/ehjdh/ztac021, PMC9708022. Save as `2022-islam-ehjdigitalhealth-wearable-cuffless-blood-pressure-devices-meta-analysis.pdf`.
- C-B29 Sources of Inaccuracy in Photoplethysmography for Continuous Cardiovascular Monitoring (MDPI, CC BY): https://doi.org/10.3390/bios11040126, PMC8073123. Save as `2021-fine-biosensors-sources-inaccuracy-photoplethysmography-cardiovascular-monitoring.pdf`.
- C-B37 Clinical evaluation and diagnostic yield following evaluation of abnormal pulse detected using Apple Watch (OUP, CC BY-NC): https://doi.org/10.1093/jamia/ocaa137, PMC7526465. Save as `2020-wyatt-jamia-diagnostic-yield-abnormal-pulse-apple-watch.pdf`.

## 5. Gaps noticed

- No open, multi-device benchmark for nocturnal HRV or resting heart rate definitions turned up: vendors define
  "resting heart rate" and overnight HRV windows differently, and C-B06 and C-B07 each rest on one ecosystem.
  Worth a targeted search, or a Lane A standard if one exists.
- Cuffless BP evidence is thin on open methods: beyond C-B33 to C-B36 the literature is mostly single-device
  validations or guidance (Lane A). Skin tone and PPG has many small primary studies but only one systematic review
  (C-B27), and the false positive burden of AF notifications has one empirical paper (C-B37, a single-device clinic
  series, kept because nothing pooled exists).
