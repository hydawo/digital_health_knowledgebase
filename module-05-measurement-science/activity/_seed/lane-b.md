# Module 5, Physical activity and fitness: Lane B seed (measurement science)

Prepared 2026-10-23. Lane B covers metric definitions and properties (counts versus raw acceleration metrics, intensity
cut-points and their placement and device dependence, intensity gradient and MX metrics, cadence thresholds, wear-time
and valid-day rules, MET definitions), device-agnostic algorithms and open methods (open counts, non-wear detection,
activity recognition datasets and models, open step counting, VO2max estimation), reviews and meta-analyses pooling
many devices, and physiological and signal limits (wrist versus hip, walking speed, older adults, resting-data
fitness estimates). Guidance, consensus and evaluation frameworks are left to Lane A. 36 papers kept: 11 PDFs stored
and verified, 16 open access but not obtained this pass, 6 free to read but not stored for licence reasons, 3 paywalled.

## 1. Search log, 2026-10-23

Europe PMC REST (`/search`, `format=json`, `resultType=lite`, `sort=CITED desc`, page size 10 to 20), hit counts as returned:

| # | Query | Hits |
|---|---|---|
| E1 | `(TITLE:"step count*" OR TITLE:steps) AND (TITLE:wearable* OR TITLE:"activity tracker*" OR TITLE:pedometer* OR TITLE:smartphone* OR TITLE:"consumer") AND (TITLE:"meta-analysis" OR TITLE:"systematic review") AND PUB_YEAR:[2010 TO 2026]` | 3 |
| E1b | `(ABSTRACT:"step count*" OR TITLE:steps OR TITLE:"step count*") AND (TITLE:wearable* OR TITLE:tracker* OR TITLE:pedometer* OR TITLE:"activity monitor*" OR TITLE:Fitbit) AND (TITLE:"meta-analysis" OR TITLE:"systematic review" OR TITLE:"review") AND (TITLE:validity OR TITLE:accuracy OR TITLE:validation) AND PUB_YEAR:[2010 TO 2026]` | 9 |
| E2 | `(TITLE:"energy expenditure") AND (TITLE:wearable* OR TITLE:"activity tracker*" OR TITLE:"activity monitor*" OR TITLE:consumer OR TITLE:smartwatch*) AND (TITLE:"meta-analysis" OR TITLE:"systematic review") AND PUB_YEAR:[2010 TO 2026]` | 3 |
| E2b | `(TITLE:"energy expenditure") AND (TITLE:"meta-analysis" OR TITLE:"systematic review") AND (TITLE:accelerometer* OR TITLE:monitor* OR TITLE:wearable* OR TITLE:device*) AND PUB_YEAR:[2010 TO 2026]` | 7 |
| E3 | `(TITLE:VO2max OR TITLE:"VO2 max" OR TITLE:"maximal oxygen uptake" OR TITLE:"cardiorespiratory fitness") AND (TITLE:wearable* OR TITLE:smartwatch* OR TITLE:"consumer") AND (TITLE:"meta-analysis" OR TITLE:"systematic review" OR TITLE:review) AND PUB_YEAR:[2010 TO 2026]` | 1 |
| E3b | `(TITLE:"oxygen" OR TITLE:VO2* OR TITLE:"cardiorespiratory fitness") AND (TITLE:wearable* OR TITLE:smartwatch* OR TITLE:"consumer" OR TITLE:"heart rate" OR TITLE:"free-living") AND (TITLE:estimat* OR TITLE:predict*) AND PUB_YEAR:[2010 TO 2026]` | 97 |
| E4 | `(TITLE:"raw acceleration" OR TITLE:"raw accelerometer" OR TITLE:ENMO OR TITLE:"mean amplitude deviation" OR TITLE:"monitor-independent" OR TITLE:"activity counts") AND PUB_YEAR:[2010 TO 2026]` | 71 |
| E5 | `(TITLE:"cut-point*" OR TITLE:"cut point*" OR TITLE:thresholds) AND (TITLE:accelerometer* OR TITLE:acceleration) AND (TITLE:comparab* OR TITLE:wrist OR TITLE:placement* OR TITLE:"intensity") AND PUB_YEAR:[2010 TO 2026]` | 11 |
| E6 | `(TITLE:"intensity gradient" OR TITLE:"MX metric*" OR TITLE:"beyond cut points" OR TITLE:"translational accelerometer metrics")` | 69 (mostly ecology off-topic) |
| E7 | `(TITLE:cadence) AND (TITLE:intensity OR TITLE:threshold* OR TITLE:"steps/min" OR TITLE:"how fast") AND PUB_YEAR:[2010 TO 2026]` | 59 |
| E8 | `(TITLE:"non-wear" OR TITLE:nonwear OR TITLE:"wear time") AND (TITLE:accelerometer* OR TITLE:algorithm*) AND PUB_YEAR:[2010 TO 2026]` | 54 |
| E9 | `(TITLE:"human activity recognition" OR TITLE:"activity classification" OR TITLE:"machine learning") AND (TITLE:wrist OR TITLE:accelerometer* OR TITLE:"free-living" OR TITLE:"in the wild") AND (TITLE:dataset OR TITLE:benchmark OR TITLE:"self-supervised" OR TITLE:"free-living" OR TITLE:"systematic review") AND PUB_YEAR:[2014 TO 2026]` | 29 |
| E10 | `(TITLE:"step count*" OR TITLE:"step-count*" OR TITLE:"step detection") AND (TITLE:"open-source" OR TITLE:algorithm* OR TITLE:"self-supervised") AND (TITLE:wrist* OR TITLE:accelerometer* OR TITLE:smartphone*) AND PUB_YEAR:[2014 TO 2026]` | 5 |
| E11 | `(TITLE:"step count*" OR TITLE:steps OR TITLE:pedometer* OR TITLE:"activity monitor*" OR TITLE:"activity tracker*") AND (TITLE:"walking speed" OR TITLE:"gait speed" OR TITLE:"slow walking" OR TITLE:"walking aid*" OR TITLE:rollator OR TITLE:"placement") AND PUB_YEAR:[2010 TO 2026]` | 38 |
| E12 | `(TITLE:"activity monitor*" OR TITLE:accelerometer* OR TITLE:wearable*) AND (TITLE:"chronic disease" OR TITLE:"older adults" OR TITLE:"clinical population*" OR TITLE:hospital*) AND (TITLE:"systematic review") AND (TITLE:validity OR TITLE:accuracy) AND PUB_YEAR:[2010 TO 2026]` | 2 |
| E13 | `(TITLE:wrist) AND (TITLE:hip OR TITLE:waist) AND (TITLE:accelerometer* OR TITLE:"step*") AND (TITLE:comparison OR TITLE:comparab* OR TITLE:"attachment site*") AND PUB_YEAR:[2010 TO 2026]` | 14 |
| E14 | `(TITLE:"sedentary") AND (TITLE:accelerometer* OR TITLE:thigh OR TITLE:posture OR TITLE:wrist) AND (TITLE:validity OR TITLE:validation OR TITLE:classification OR TITLE:thresholds OR TITLE:comparison) AND PUB_YEAR:[2010 TO 2026]` | 37 |
| E15 | `(TITLE:"energy expenditure") AND (TITLE:"heart rate") AND (TITLE:"individual calibration" OR TITLE:"branched" OR TITLE:"combined" OR TITLE:"accelerometry" OR TITLE:"flex") AND PUB_YEAR:[2010 TO 2026]` | 15 |
| E16 | `(TITLE:"metabolic equivalent" OR TITLE:MET OR TITLE:METs OR TITLE:"Compendium of Physical Activities") AND (TITLE:compendium OR TITLE:"resting metabolic rate" OR TITLE:"3.5") AND PUB_YEAR:[2010 TO 2026]` | 14 |
| E17 | `(TITLE:accelerometry OR TITLE:accelerometer*) AND (TITLE:"activity counts" OR TITLE:MIMS OR TITLE:ENMO) AND (TITLE:comparison OR TITLE:harmoniz* OR TITLE:mapping OR TITLE:NHANES) AND PUB_YEAR:[2015 TO 2026]` | 2 |
| E18 | `(TITLE:Fitbit OR TITLE:"activity tracker*" OR TITLE:"consumer-wearable*") AND (TITLE:"systematic review") AND PUB_YEAR:[2014 TO 2026]` | 18 |
| E19 | `(TITLE:"heart rate") AND (TITLE:"cardiorespiratory fitness" OR TITLE:VO2max OR TITLE:"aerobic fitness") AND (TITLE:"non-exercise" OR TITLE:"resting heart rate" OR TITLE:"free-living" OR TITLE:"population") AND PUB_YEAR:[2010 TO 2026]` | 10 |
| E20 | Known-item title lookups, one query each: van Hees ENMO 2013, Karas metric comparison, Migueles placement comparability, Bassett step counting review, Yuan self-supervised HAR, Syed non-wear, Spathis CRF prediction, Fokkema ten trackers, Van Remoortel chronic disease review, Germini wrist trackers review | 1 or 2 each |

Follow-up checks:

- Europe PMC `resultType=core` lookup by `DOI:"..."` for all 39 shortlisted DOIs: title, full author list, year, PMID,
  PMCID, abstract and licence field. Descriptions are written from these abstracts only.
- OpenAlex `/works/doi:...` for the same DOIs (no mailto parameter): `open_access.oa_status` and `locations[].license`,
  used to decide which PDFs could be stored.
- Dedup: every DOI checked against `_seed/known-dois.tsv`, and author and title strings grepped across the repo.
- PDFs fetched from publisher or repository URLs given by OpenAlex. Europe PMC article pages, JMIR (`/PDF` is
  disallowed in its robots.txt), Springer, BioMed Central, BMJ, ScienceDirect and PMC PDF links returned bot checks or
  HTML and were not pursued further. Each stored file starts with `%PDF`, `pypdf` extracts the paper's own title and
  authors, and the CC licence statement was confirmed in the text or by Europe PMC and OpenAlex.
- Dropped at shortlist: Fokkema 2017 (ten trackers by walking speed, single-study duplicate of P-B34's point), Tudor-Locke
  2019 CADENCE-Adults (thresholds summarised by P-B10), Feehan 2018 Fitbit review (single brand; Chevance 2022 already
  covers Fitbit in Module 1).

## 2. Catalogue rows

| # | Title | Authors | Venue / Year | DOI / URL | OA status | PDF | What it establishes |
|---|---|---|---|---|---|---|---|
| P-B01 | Separating movement and gravity components in an acceleration signal and implications for the assessment of human daily physical activity | van Hees VT, Gorzelniak L, Dean León EC, Eder M, Pias M, Taherian S, Ekelund U, Renström F, et al | *PLOS ONE* 2013 | [10.1371/journal.pone.0061691](https://doi.org/10.1371/journal.pone.0061691) | **Verified OA** | [2013-vanhees-plosone-separating-movement-gravity-acceleration-signal.pdf](literature/2013-vanhees-plosone-separating-movement-gravity-acceleration-signal.pdf) | Metrics. Introduces and compares raw-acceleration metrics, including ENMO and HFEN, against a robot arm reference and in human wrist and hip data with energy expenditure. No metric was best across all conditions, ENMO did better at low frequencies, and removing gravity raised the variance explained in daily activity energy expenditure from 26% to between 30% and 36%. |
| P-B02 | Age group comparability of raw accelerometer output from wrist- and hip-worn monitors | Hildebrand M, van Hees VT, Hansen BH, Ekelund U | *Medicine and Science in Sports and Exercise* 2014 | [10.1249/mss.0000000000000289](https://doi.org/10.1249/mss.0000000000000289) | **Free to read, not stored (licence)** | none, not stored | Metrics. Compared raw ENMO output from ActiGraph and GENEActiv on hip and wrist in children and adults against indirect calorimetry and derived wrist and hip intensity thresholds. Hip and wrist values differed significantly, and brands were comparable at the same site in adults but not in children. Free copy is an unlicensed repository version. |
| P-B03 | Intensity Thresholds on Raw Acceleration Data: Euclidean Norm Minus One (ENMO) and Mean Amplitude Deviation (MAD) Approaches | Bakrania K, Yates T, Rowlands AV, Esliger DW, Bunnewell S, Sanders J, Davies M, Khunti K, et al | *PLOS ONE* 2016 | [10.1371/journal.pone.0164045](https://doi.org/10.1371/journal.pone.0164045) | **Verified OA** | [2016-bakrania-plosone-intensity-thresholds-raw-acceleration-enmo-mad.pdf](literature/2016-bakrania-plosone-intensity-thresholds-raw-acceleration-enmo-mad.pdf) | Metrics. Derives ENMO and MAD thresholds that separate sedentary behaviour from light activity for hip and wrist ActiGraph and GENEActiv monitors in 33 adults. GENEActiv values ran slightly higher than ActiGraph at low intensities, so the thresholds are monitor- and site-specific. |
| P-B04 | Validation of Cut-Points for Evaluating the Intensity of Physical Activity with Accelerometry-Based Mean Amplitude Deviation (MAD) | Vähä-Ypyä H, Vasankari T, Husu P, Mänttäri A, Vuorimaa T, Suni J, Sievänen H | *PLOS ONE* 2015 | [10.1371/journal.pone.0134813](https://doi.org/10.1371/journal.pone.0134813) | **Verified OA** | [2015-vahaypya-plosone-validation-cut-points-mean-amplitude-deviation.pdf](literature/2015-vahaypya-plosone-validation-cut-points-mean-amplitude-deviation.pdf) | Metrics. Validates mean amplitude deviation (MAD) of the resultant acceleration against measured VO2 from slow walking to running in 29 participants with a hip monitor. MAD tracked VO2 closely within individuals, giving cut-points of 91 mg for 3 METs and 414 mg for 6 METs. |
| P-B05 | An Open-Source Monitor-Independent Movement Summary for Accelerometer Data Processing | John D, Tang Q, Albinali F, Intille S | *Journal for the Measurement of Physical Behaviour* 2019 | [10.1123/jmpb.2018-0068](https://doi.org/10.1123/jmpb.2018-0068) | **Free to read, not stored (licence)** | none, not stored | Metrics. Defines the open Monitor-Independent Movement Summary (MIMS) unit, which harmonises dynamic range and sampling rate and band-pass filters raw data before aggregation. On a shaker it varied less between devices than ActiGraph counts or ENMO and picked up small wrist movements that counts missed. Free copy is a PMC author manuscript. |
| P-B06 | Beyond Cut Points: Accelerometer Metrics that Capture the Physical Activity Profile | Rowlands AV, Edwardson CL, Davies MJ, Khunti K, Harrington DM, Yates T | *Medicine and Science in Sports and Exercise* 2018 | [10.1249/mss.0000000000001561](https://doi.org/10.1249/mss.0000000000001561) | **OA but not obtained this pass** | none, not stored | Metrics. Introduces the intensity gradient, the slope of the log-log relation between acceleration intensity bins and time spent in each, as a partner to average acceleration. Unlike total MVPA, it was only moderately correlated with average acceleration and carried independent associations with adiposity and physical function, so the pair can be compared across raw-data studies without cut-points. OpenAlex lists a CC BY Figshare copy. |
| P-B07 | Enhancing the value of accelerometer-assessed physical activity: meaningful visual comparisons of data-driven translational accelerometer metrics | Rowlands AV, Dawkins NP, Maylor B, Edwardson CL, Fairclough SJ, Davies MJ, Harrington DM, Khunti K, et al | *Sports Medicine - Open* 2019 | [10.1186/s40798-019-0225-9](https://doi.org/10.1186/s40798-019-0225-9) | **OA but not obtained this pass** | none, not stored | Metrics. Proposes MX metrics, the acceleration above which a person's most active X minutes are accumulated (for example M60, M30, M5), as interpretable translations of average acceleration and intensity gradient. Argues that cut-point outputs are easy to read but not comparable across studies, and shows radar plots of MX metrics for group comparisons. CC BY. |
| P-B08 | Comparison of Accelerometry-Based Measures of Physical Activity: Retrospective Observational Data Analysis Study | Karas M, Muschelli J, Leroux A, Urbanek JK, Wanigatunga AA, Bai J, Crainiceanu CM, Schrack JA | *JMIR mHealth and uHealth* 2022 | [10.2196/38077](https://doi.org/10.2196/38077) | **OA but not obtained this pass** | none, not stored | Metrics. Computes ActiGraph counts, MIMS, ENMO, MAD and activity intensity from the same wrist GT9X data in 655 adults of the Baltimore Longitudinal Study of Aging and fits harmonisation mappings between them. Counts correlated almost perfectly with MIMS (r 0.988) and less with ENMO (r 0.867), so mapping between metrics is feasible but not exact. CC BY; JMIR disallows scripted PDF access. |
| P-B09 | Comparability of accelerometer signal aggregation metrics across placements and dominant wrist cut points for the assessment of physical activity in adults | Migueles JH, Cadenas-Sanchez C, Rowlands AV, Henriksson P, Shiroma EJ, Acosta FM, Rodriguez-Ayllon M, Esteban-Cornejo I, et al | *Scientific Reports* 2019 | [10.1038/s41598-019-54267-y](https://doi.org/10.1038/s41598-019-54267-y) | **Verified OA** | [2019-migueles-scirep-comparability-aggregation-metrics-placements-cut-points.pdf](literature/2019-migueles-scirep-comparability-aggregation-metrics-placements-cut-points.pdf) | Metrics. Compared ENMO, low-pass filtered ENMO, MAD and ActiGraph counts across hip, dominant and non-dominant wrist in 45 adults over 7 days. Shared variance between site and metric pairs ranged from 0.19 to 0.97 and the dominant wrist read higher, so the authors derived separate dominant-wrist ENMO cut-points. |
| P-B10 | How fast is fast enough? Walking cadence (steps/min) as a practical estimate of intensity in adults: a narrative review | Tudor-Locke C, Han H, Aguiar EJ, Barreira TV, Schuna JM Jr, Kang M, Rowe DA | *British Journal of Sports Medicine* 2018 | [10.1136/bjsports-2017-097628](https://doi.org/10.1136/bjsports-2017-097628) | **OA but not obtained this pass** | none, not stored | Metrics. Narrative review of 38 studies linking walking cadence to measured intensity in adults. Finds 100 steps/min a consistent heuristic for absolutely defined moderate intensity (3 METs) despite individual variation, and notes that free-living mean daily cadence is very low. CC BY-NC. |
| P-B11 | Step Counting: A Review of Measurement Considerations and Health-Related Applications | Bassett DR Jr, Toth LP, LaMunion SR, Crouter SE | *Sports Medicine* 2017 | [10.1007/s40279-016-0663-1](https://doi.org/10.1007/s40279-016-0663-1) | **OA but not obtained this pass** | none, not stored | Metrics. Review of steps as a physical activity metric: device types and wear sites, their strengths and limitations, the 3 to 7 days needed for a reliable estimate because of day-to-day variability, and health associations. Calls for standard testing protocols and accuracy criteria for step counters. CC BY. |
| P-B12 | Impact of accelerometer data processing decisions on the sample size, wear time and physical activity level of a large cohort study | Keadle SK, Shiroma EJ, Freedson PS, Lee IM | *BMC Public Health* 2014 | [10.1186/1471-2458-14-1210](https://doi.org/10.1186/1471-2458-14-1210) | **OA but not obtained this pass** | none, not stored | Metrics. In 7,650 older women mailed hip ActiGraphs, compared wear-time methods (logs, Troiano, Choi) and vertical-axis versus vector magnitude cut-points. Algorithms alone counted mailing days as wear days, the wear algorithm shifted sedentary time by roughly 30 to 60 min, and vertical-axis cut-points gave about 60 min more sedentary time than vector magnitude ones. CC BY. |
| P-B13 | Impact of accelerometer wear time on physical activity data: a NHANES semisimulation data approach | Herrmann SD, Barreira TV, Kang M, Ainsworth BE | *British Journal of Sports Medicine* 2014 | [10.1136/bjsports-2012-091410](https://doi.org/10.1136/bjsports-2012-091410) | **Paywalled** | none, not stored | Metrics. Semi-simulation from NHANES 2005-2006 days with 14 h of wear, truncated to 10 to 13 h, to test valid-day wear-time rules. Wear-time criteria of 12 h per day or less underestimated steps and time in several intensity levels. |
| P-B14 | 2024 Adult Compendium of Physical Activities: A third update of the energy costs of human activities | Herrmann SD, Willis EA, Ainsworth BE, Barreira TV, Hastert M, Kracht CL, Schuna JM Jr, Cai Z, et al | *Journal of Sport and Health Science* 2024 | [10.1016/j.jshs.2023.10.010](https://doi.org/10.1016/j.jshs.2023.10.010) | **OA but not obtained this pass** | none, not stored | Metrics. Third update of the Compendium of Physical Activities for adults aged 19 to 59, the standard source of MET values for activity types: 1,114 activities, 912 with measured values. Used by researchers and by consumer technologies to convert activity type into energy cost. CC BY-NC-ND. |
| P-B15 | Errors in MET estimates of physical activities using 3.5 ml x kg(-1) x min(-1) as the baseline oxygen consumption | Kozey S, Lyden K, Staudenmayer J, Freedson P | *Journal of Physical Activity and Health* 2010 | [10.1123/jpah.7.4.508](https://doi.org/10.1123/jpah.7.4.508) | **Paywalled** | none, not stored | Metrics. Measured resting metabolic rate and activity VO2 in 252 adults across 11 activities. Using the standard 3.5 ml/kg/min as 1 MET underestimated activity METs and misclassified more activities by intensity than a corrected baseline, with errors falling hardest on the least active subgroups. |
| P-B16 | Quantification of acceleration as activity counts in ActiGraph wearable | Neishabouri A, Nguyen J, Samuelsson J, Guthrie T, Biggs M, Wyatt J, Cross D, Karas M, et al | *Scientific Reports* 2022 | [10.1038/s41598-022-16003-x](https://doi.org/10.1038/s41598-022-16003-x) | **Verified OA** | [2022-neishabouri-scirep-activity-counts-actigraph.pdf](literature/2022-neishabouri-scirep-activity-counts-actigraph.pdf) | Algorithms. Publishes the ActiGraph activity counts algorithms for five device generations and releases the current ActiLife and CentrePoint counts algorithm as an open Python package. Makes counts reproducible from raw data from any device, which had been blocked by proprietary implementations. |
| P-B17 | Generating ActiGraph Counts from Raw Acceleration Recorded by an Alternative Monitor | Brønd JC, Andersen LB, Arvidsson D | *Medicine and Science in Sports and Exercise* 2017 | [10.1249/mss.0000000000001344](https://doi.org/10.1249/mss.0000000000001344) | **OA but not obtained this pass** | none, not stored | Algorithms. Reverse-engineers the ActiGraph count band-pass filter so counts can be generated from another monitor's raw data, tested on a mechanical rig and in 24-h free-living Axivity AX3 recordings. Agreement in intensity classification was near perfect (kappa 0.945), allowing count-based cut-points to be applied to other devices. OpenAlex lists a CC BY-NC repository copy. |
| P-B18 | Validation of accelerometer wear and nonwear time classification algorithm | Choi L, Liu Z, Matthews CE, Buchowski MS | *Medicine and Science in Sports and Exercise* 2011 | [10.1249/mss.0b013e3181ed61a3](https://doi.org/10.1249/mss.0b013e3181ed61a3) | **Free to read, not stored (licence)** | none, not stored | Algorithms. Validated and revised the count-based wear and non-wear algorithm against true wear status in 49 adults and 76 youth in a room calorimeter. The revised rules use a 90-min zero-count window with a 2-min allowance for artefactual movement, now known as the Choi algorithm. Free copy is a PMC author manuscript. |
| P-B19 | Evaluating the performance of raw and epoch non-wear algorithms using multiple accelerometers and electrocardiogram recordings | Syed S, Morseth B, Hopstock LA, Horsch A | *Scientific Reports* 2020 | [10.1038/s41598-020-62821-2](https://doi.org/10.1038/s41598-020-62821-2) | **Verified OA** | [2020-syed-scirep-raw-epoch-non-wear-algorithms.pdf](literature/2020-syed-scirep-raw-epoch-non-wear-algorithms.pdf) | Algorithms. Benchmarks three epoch-based non-wear algorithms (Hecht, Troiano, Choi) and the raw-data van Hees algorithm against a reference built from two accelerometers and ECG. With default settings van Hees performed best and Hecht and Troiano poorly, but tuned epoch-based algorithms matched the raw-data method. |
| P-B20 | CAPTURE-24: A large dataset of wrist-worn activity tracker data collected in the wild for human activity recognition | Chan S, Hang Y, Tong C, Acquah A, Schonfeldt A, Gershuny J, Doherty A | *Scientific Data* 2024 | [10.1038/s41597-024-03960-3](https://doi.org/10.1038/s41597-024-03960-3) | **Verified OA** | [2024-chan-scidata-capture-24-wrist-worn-activity-dataset.pdf](literature/2024-chan-scidata-capture-24-wrist-worn-activity-dataset.pdf) | Algorithms. Describes CAPTURE-24, an open free-living dataset of wrist accelerometry from 151 participants with wearable camera and sleep diary annotation (3,883 h recorded, 2,562 h annotated). Built because models trained on laboratory activity data do not generalise to free living. |
| P-B21 | Self-supervised learning for human activity recognition using 700,000 person-days of wearable data | Yuan H, Chan S, Creagh AP, Tong C, Acquah A, Clifton DA, Doherty A | *npj Digital Medicine* 2024 | [10.1038/s41746-024-01062-3](https://doi.org/10.1038/s41746-024-01062-3) | **Verified OA** | [2024-yuan-npjdigitalmedicine-self-supervised-har-700000-person-days.pdf](literature/2024-yuan-npjdigitalmedicine-self-supervised-har-700000-person-days.pdf) | Algorithms. Pretrains self-supervised activity recognition models on 700,000 person-days of unlabelled UK Biobank wrist accelerometry and releases them openly. The models outperformed baselines on eight benchmark datasets and generalised across cohorts, settings and devices. |
| P-B22 | Self-Supervised Machine Learning to Characterize Step Counts from Wrist-Worn Accelerometers in the UK Biobank | Small SR, Chan S, Walmsley R, von Fritsch L, Acquah A, Mertes G, Feakins BG, Creagh A, et al | *Medicine and Science in Sports and Exercise* 2024 | [10.1249/mss.0000000000003478](https://doi.org/10.1249/mss.0000000000003478) | **OA but not obtained this pass** | none, not stored | Algorithms. Develops an open self-supervised step detection model for wrist accelerometry trained and externally validated on free-living, step-annotated data. Free-living mean absolute percent error was 12.5% against 65% to 231% for reference models; the model was then applied to 75,263 UK Biobank participants. CC BY. |
| P-B23 | Stepping towards More Intuitive Physical Activity Metrics with Wrist-Worn Accelerometry: Validity of an Open-Source Step-Count Algorithm | Maylor BD, Edwardson CL, Dempsey PC, Patterson MR, Plekhanova T, Yates T, Rowlands AV | *Sensors* 2022 | [10.3390/s22249984](https://doi.org/10.3390/s22249984) | **Verified OA** | [2022-maylor-sensors-open-source-step-count-algorithm-wrist.pdf](literature/2022-maylor-sensors-open-source-step-count-algorithm-wrist.pdf) | Algorithms. Tests two versions of the open Verisense step-count algorithm on non-dominant wrist data against thigh activPAL steps in 713 participants. Both overestimated total daily steps and underestimated MVPA steps; the optimised version was more accurate, and the authors stress judging step algorithms on more than total steps. |
| P-B24 | Calibration and validation of accelerometer-based activity monitors: A systematic review of machine-learning approaches | Farrahi V, Niemelä M, Kangas M, Korpelainen R, Jämsä T | *Gait and Posture* 2019 | [10.1016/j.gaitpost.2018.12.003](https://doi.org/10.1016/j.gaitpost.2018.12.003) | **OA but not obtained this pass** | none, not stored | Algorithms. Systematic review of 62 studies that used machine learning to calibrate accelerometers for activity type, intensity and energy expenditure. Sets out how data type (raw versus counts), sampling frequency, window size, features, placement and free-living versus laboratory training affect model performance, and finds that high laboratory accuracy did not carry over to free living. CC BY-NC-ND, behind a publisher bot check. |
| P-B25 | Cardiorespiratory fitness estimation using wearable sensors: Laboratory and free-living analysis of context-specific submaximal heart rates | Altini M, Casale P, Penders J, Ten Velde G, Plasqui G, Amft O | *Journal of Applied Physiology* 2016 | [10.1152/japplphysiol.00519.2015](https://doi.org/10.1152/japplphysiol.00519.2015) | **Free to read, not stored (licence)** | none, not stored | Algorithms. Estimates VO2max from heart rate during specific contexts (lying, walking at set speeds) detected in free-living data from a combined accelerometer and heart rate monitor, in 51 people with maximal tests. Adding context-specific free-living heart rate raised explained variance from 0.65 with anthropometrics to 0.77 and cut RMSE by 21%. Free on the publisher site, not CC. |
| P-B26 | Longitudinal cardio-respiratory fitness prediction through wearables in free-living environments | Spathis D, Perez-Pozuelo I, Gonzales TI, Wu Y, Brage S, Wareham N, Mascolo C | *npj Digital Medicine* 2022 | [10.1038/s41746-022-00719-1](https://doi.org/10.1038/s41746-022-00719-1) | **Verified OA** | [2022-spathis-npjdigitalmedicine-longitudinal-cardiorespiratory-fitness-prediction.pdf](literature/2022-spathis-npjdigitalmedicine-longitudinal-cardiorespiratory-fitness-prediction.pdf) | Algorithms. Neural network models that estimate VO2max from free-living wearable heart rate and movement plus other biomarkers, developed in the Fenland Study (11,059) and tested on a longitudinal subsample and the UK Biobank Validation Study. Holdout correlation with measured VO2max was 0.82 and the models detected fitness change over about 7 years. |
| P-B27 | Systematic review of the validity and reliability of consumer-wearable activity trackers | Evenson KR, Goto MM, Furberg RD | *International Journal of Behavioral Nutrition and Physical Activity* 2015 | [10.1186/s12966-015-0314-1](https://doi.org/10.1186/s12966-015-0314-1) | **OA but not obtained this pass** | none, not stored | Pooled accuracy. Systematic review of 22 studies of Fitbit and Jawbone trackers. Laboratory step counts correlated highly with criterion steps, energy expenditure was more often underestimated, and evidence for distance and free-living activity was thin. CC BY. |
| P-B28 | How well do activity monitors estimate energy expenditure? A systematic review and meta-analysis of the validity of current technologies | O'Driscoll R, Turicchi J, Beaulieu K, Scott S, Matu J, Deighton K, Finlayson G, Stubbs J | *British Journal of Sports Medicine* 2020 | [10.1136/bjsports-2018-099643](https://doi.org/10.1136/bjsports-2018-099643) | **Free to read, not stored (licence)** | none, not stored | Pooled accuracy. Meta-analysis of 60 studies (104 effect sizes) of wrist and arm monitor energy expenditure against calorimetry or doubly labelled water. Accuracy varied by activity type with large heterogeneity; adding heart rate or heat sensing to accelerometry reduced error. Free on the publisher site, not CC. |
| P-B29 | Validity of Estimating the Maximal Oxygen Consumption by Consumer Wearables: A Systematic Review with Meta-analysis and Expert Statement of the INTERLIVE Network | Molina-Garcia P, Notbohm HL, Schumann M, Argent R, Hetherington-Rauth M, Stang J, Bloch W, Cheng S, et al | *Sports Medicine* 2022 | [10.1007/s40279-021-01639-y](https://doi.org/10.1007/s40279-021-01639-y) | **OA but not obtained this pass** | none, not stored | Pooled accuracy. Meta-analysis of 14 studies of consumer wearable VO2max estimates against laboratory tests, with INTERLIVE best-practice recommendations for validation. Algorithms using resting data overestimated VO2max (bias 2.17 ml/kg/min, limits of agreement -13.07 to 17.41) while exercise-based algorithms had less bias and narrower limits. CC BY. |
| P-B30 | The validity and reliability of consumer-grade activity trackers in older, community-dwelling adults: A systematic review | Straiton N, Alharbi M, Bauman A, Neubeck L, Gullick J, Bhindi R, Gallagher R | *Maturitas* 2018 | [10.1016/j.maturitas.2018.03.016](https://doi.org/10.1016/j.maturitas.2018.03.016) | **OA but not obtained this pass** | none, not stored | Pooled accuracy. Systematic review of 7 studies (290 adults over 65) of eight consumer trackers against reference devices. Daily step counts correlated highly with criteria, but slower walking and impaired gait reduced agreement and five of the eight devices overestimated steps. OpenAlex lists a CC BY-NC-ND repository copy. |
| P-B31 | Accuracy and Acceptability of Wrist-Wearable Activity-Tracking Devices: Systematic Review of the Literature | Germini F, Noronha N, Borg Debono V, Abraham Philip B, Pete D, Navarro T, Keepanasseril A, Parpia S, et al | *Journal of Medical Internet Research* 2022 | [10.2196/30791](https://doi.org/10.2196/30791) | **OA but not obtained this pass** | none, not stored | Pooled accuracy. Systematic review of 65 studies of wrist-worn activity trackers across 14 outcomes, mainly steps, heart rate and energy expenditure. Heterogeneity prevented meta-analysis; some Fitbit models were accurate for steps, but no device measured energy expenditure accurately. CC BY; JMIR disallows scripted PDF access. |
| P-B32 | Validity of activity monitors in health and chronic disease: a systematic review | Van Remoortel H, Giavedoni S, Raste Y, Burtin C, Louvaris Z, Gimeno-Santos E, Langer D, Glendenning A, et al | *International Journal of Behavioral Nutrition and Physical Activity* 2012 | [10.1186/1479-5868-9-84](https://doi.org/10.1186/1479-5868-9-84) | **OA but not obtained this pass** | none, not stored | Pooled accuracy. Systematic review and meta-analysis of 134 validation studies of research activity monitors against doubly labelled water or calorimetry. Most were in healthy adults with only 16 in chronic disease; uniaxial devices underestimated total energy expenditure more than multisensor devices, and underestimation was most common at slow walking speeds. CC BY. |
| P-B33 | Comparison of step outputs for waist and wrist accelerometer attachment sites | Tudor-Locke C, Barreira TV, Schuna JM Jr | *Medicine and Science in Sports and Exercise* 2015 | [10.1249/mss.0000000000000476](https://doi.org/10.1249/mss.0000000000000476) | **Paywalled** | none, not stored | Physiological limits. Compared waist and non-dominant wrist ActiGraph steps against visually counted steps on a treadmill and over 7 free-living days. The waist was more accurate at most speeds, while the wrist recorded more steps per day in free living, so wrist and waist step counts are not interchangeable. |
| P-B34 | Accuracy of step count measured by physical activity monitors: The effect of gait speed and anatomical placement site | Chow JJ, Thom JM, Wewege MA, Ward RE, Parmenter BJ | *Gait and Posture* 2017 | [10.1016/j.gaitpost.2017.06.012](https://doi.org/10.1016/j.gaitpost.2017.06.012) | **OA but not obtained this pass** | none, not stored | Physiological limits. Five monitors on waist and wrists against video step counts at five treadmill speeds in 31 adults. Error ranged from about 41% for the wrist ActiGraph to near zero for waist devices, and waist placement beat wrist across speeds. OpenAlex lists a CC BY-NC-ND repository copy. |
| P-B35 | Comparison of Sedentary Estimates between activPAL and Hip- and Wrist-Worn ActiGraph | Koster A, Shiroma EJ, Caserotti P, Matthews CE, Chen KY, Glynn NW, Harris TB | *Medicine and Science in Sports and Exercise* 2016 | [10.1249/mss.0000000000000924](https://doi.org/10.1249/mss.0000000000000924) | **Free to read, not stored (licence)** | none, not stored | Physiological limits. In 62 adults with a mean age of 78, compared hip and wrist ActiGraph sedentary cut-points with thigh activPAL posture over 7 free-living days. The optimal hip cut-point (<22 counts/min) was far below the standard <100, and the authors caution that optimal cut-points may not hold in other populations. Free copy is a PMC author manuscript. |
| P-B36 | Resting heart rate is a population-level biomarker of cardiorespiratory fitness: The Fenland Study | Gonzales TI, Jeon JY, Lindsay T, Westgate K, Perez-Pozuelo I, Hollidge S, Wijndaele K, Rennie K, et al | *PLOS ONE* 2023 | [10.1371/journal.pone.0285272](https://doi.org/10.1371/journal.pone.0285272) | **Verified OA** | [2023-gonzales-plosone-resting-heart-rate-cardiorespiratory-fitness-fenland.pdf](literature/2023-gonzales-plosone-resting-heart-rate-cardiorespiratory-fitness-fenland.pdf) | Physiological limits. In about 10,800 Fenland adults, resting heart rate (seated, supine, sleeping) was inversely associated with exercise-test VO2max, and a 1 bpm rise in supine resting heart rate over about 6 years went with a 0.23 ml/kg/min fall in fitness. Physical activity adjustment attenuated the relationship by 50%, and the authors validate resting heart rate only as a population-level fitness marker. |

## 3. Records

```json
[
 {
  "id": "P-B01",
  "doi": "10.1371/journal.pone.0061691",
  "pmid": "23626718",
  "pmcid": "PMC3634007",
  "title": "Separating movement and gravity components in an acceleration signal and implications for the assessment of human daily physical activity",
  "year": 2013,
  "pdf": "module-05-measurement-science/activity/literature/2013-vanhees-plosone-separating-movement-gravity-acceleration-signal.pdf",
  "pdf_status": "stored"
 },
 {
  "id": "P-B02",
  "doi": "10.1249/mss.0000000000000289",
  "pmid": "24887173",
  "pmcid": null,
  "title": "Age group comparability of raw accelerometer output from wrist- and hip-worn monitors",
  "year": 2014,
  "pdf": null,
  "pdf_status": "free_not_redistributable"
 },
 {
  "id": "P-B03",
  "doi": "10.1371/journal.pone.0164045",
  "pmid": "27706241",
  "pmcid": "PMC5051724",
  "title": "Intensity Thresholds on Raw Acceleration Data: Euclidean Norm Minus One (ENMO) and Mean Amplitude Deviation (MAD) Approaches",
  "year": 2016,
  "pdf": "module-05-measurement-science/activity/literature/2016-bakrania-plosone-intensity-thresholds-raw-acceleration-enmo-mad.pdf",
  "pdf_status": "stored"
 },
 {
  "id": "P-B04",
  "doi": "10.1371/journal.pone.0134813",
  "pmid": "26292225",
  "pmcid": "PMC4546343",
  "title": "Validation of Cut-Points for Evaluating the Intensity of Physical Activity with Accelerometry-Based Mean Amplitude Deviation (MAD)",
  "year": 2015,
  "pdf": "module-05-measurement-science/activity/literature/2015-vahaypya-plosone-validation-cut-points-mean-amplitude-deviation.pdf",
  "pdf_status": "stored"
 },
 {
  "id": "P-B05",
  "doi": "10.1123/jmpb.2018-0068",
  "pmid": "34308270",
  "pmcid": "PMC8301210",
  "title": "An Open-Source Monitor-Independent Movement Summary for Accelerometer Data Processing",
  "year": 2019,
  "pdf": null,
  "pdf_status": "free_not_redistributable"
 },
 {
  "id": "P-B06",
  "doi": "10.1249/mss.0000000000001561",
  "pmid": "29360664",
  "pmcid": null,
  "title": "Beyond Cut Points: Accelerometer Metrics that Capture the Physical Activity Profile",
  "year": 2018,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "P-B07",
  "doi": "10.1186/s40798-019-0225-9",
  "pmid": "31808014",
  "pmcid": "PMC6895365",
  "title": "Enhancing the value of accelerometer-assessed physical activity: meaningful visual comparisons of data-driven translational accelerometer metrics",
  "year": 2019,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "P-B08",
  "doi": "10.2196/38077",
  "pmid": "35867392",
  "pmcid": "PMC9356340",
  "title": "Comparison of Accelerometry-Based Measures of Physical Activity: Retrospective Observational Data Analysis Study",
  "year": 2022,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "P-B09",
  "doi": "10.1038/s41598-019-54267-y",
  "pmid": "31796778",
  "pmcid": "PMC6890686",
  "title": "Comparability of accelerometer signal aggregation metrics across placements and dominant wrist cut points for the assessment of physical activity in adults",
  "year": 2019,
  "pdf": "module-05-measurement-science/activity/literature/2019-migueles-scirep-comparability-aggregation-metrics-placements-cut-points.pdf",
  "pdf_status": "stored"
 },
 {
  "id": "P-B10",
  "doi": "10.1136/bjsports-2017-097628",
  "pmid": "29858465",
  "pmcid": "PMC6029645",
  "title": "How fast is fast enough? Walking cadence (steps/min) as a practical estimate of intensity in adults: a narrative review",
  "year": 2018,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "P-B11",
  "doi": "10.1007/s40279-016-0663-1",
  "pmid": "28005190",
  "pmcid": "PMC5488109",
  "title": "Step Counting: A Review of Measurement Considerations and Health-Related Applications",
  "year": 2017,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "P-B12",
  "doi": "10.1186/1471-2458-14-1210",
  "pmid": "25421941",
  "pmcid": "PMC4247661",
  "title": "Impact of accelerometer data processing decisions on the sample size, wear time and physical activity level of a large cohort study",
  "year": 2014,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "P-B13",
  "doi": "10.1136/bjsports-2012-091410",
  "pmid": "22936409",
  "pmcid": null,
  "title": "Impact of accelerometer wear time on physical activity data: a NHANES semisimulation data approach",
  "year": 2014,
  "pdf": null,
  "pdf_status": "paywalled"
 },
 {
  "id": "P-B14",
  "doi": "10.1016/j.jshs.2023.10.010",
  "pmid": "38242596",
  "pmcid": "PMC10818145",
  "title": "2024 Adult Compendium of Physical Activities: A third update of the energy costs of human activities",
  "year": 2024,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "P-B15",
  "doi": "10.1123/jpah.7.4.508",
  "pmid": "20683093",
  "pmcid": null,
  "title": "Errors in MET estimates of physical activities using 3.5 ml x kg(-1) x min(-1) as the baseline oxygen consumption",
  "year": 2010,
  "pdf": null,
  "pdf_status": "paywalled"
 },
 {
  "id": "P-B16",
  "doi": "10.1038/s41598-022-16003-x",
  "pmid": "35831446",
  "pmcid": "PMC9279376",
  "title": "Quantification of acceleration as activity counts in ActiGraph wearable",
  "year": 2022,
  "pdf": "module-05-measurement-science/activity/literature/2022-neishabouri-scirep-activity-counts-actigraph.pdf",
  "pdf_status": "stored"
 },
 {
  "id": "P-B17",
  "doi": "10.1249/mss.0000000000001344",
  "pmid": "28604558",
  "pmcid": null,
  "title": "Generating ActiGraph Counts from Raw Acceleration Recorded by an Alternative Monitor",
  "year": 2017,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "P-B18",
  "doi": "10.1249/mss.0b013e3181ed61a3",
  "pmid": "20581716",
  "pmcid": "PMC3184184",
  "title": "Validation of accelerometer wear and nonwear time classification algorithm",
  "year": 2011,
  "pdf": null,
  "pdf_status": "free_not_redistributable"
 },
 {
  "id": "P-B19",
  "doi": "10.1038/s41598-020-62821-2",
  "pmid": "32246080",
  "pmcid": "PMC7125135",
  "title": "Evaluating the performance of raw and epoch non-wear algorithms using multiple accelerometers and electrocardiogram recordings",
  "year": 2020,
  "pdf": "module-05-measurement-science/activity/literature/2020-syed-scirep-raw-epoch-non-wear-algorithms.pdf",
  "pdf_status": "stored"
 },
 {
  "id": "P-B20",
  "doi": "10.1038/s41597-024-03960-3",
  "pmid": "39414802",
  "pmcid": "PMC11484779",
  "title": "CAPTURE-24: A large dataset of wrist-worn activity tracker data collected in the wild for human activity recognition",
  "year": 2024,
  "pdf": "module-05-measurement-science/activity/literature/2024-chan-scidata-capture-24-wrist-worn-activity-dataset.pdf",
  "pdf_status": "stored"
 },
 {
  "id": "P-B21",
  "doi": "10.1038/s41746-024-01062-3",
  "pmid": "38609437",
  "pmcid": "PMC11015005",
  "title": "Self-supervised learning for human activity recognition using 700,000 person-days of wearable data",
  "year": 2024,
  "pdf": "module-05-measurement-science/activity/literature/2024-yuan-npjdigitalmedicine-self-supervised-har-700000-person-days.pdf",
  "pdf_status": "stored"
 },
 {
  "id": "P-B22",
  "doi": "10.1249/mss.0000000000003478",
  "pmid": "38768076",
  "pmcid": "PMC11402590",
  "title": "Self-Supervised Machine Learning to Characterize Step Counts from Wrist-Worn Accelerometers in the UK Biobank",
  "year": 2024,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "P-B23",
  "doi": "10.3390/s22249984",
  "pmid": "36560353",
  "pmcid": "PMC9786909",
  "title": "Stepping towards More Intuitive Physical Activity Metrics with Wrist-Worn Accelerometry: Validity of an Open-Source Step-Count Algorithm",
  "year": 2022,
  "pdf": "module-05-measurement-science/activity/literature/2022-maylor-sensors-open-source-step-count-algorithm-wrist.pdf",
  "pdf_status": "stored"
 },
 {
  "id": "P-B24",
  "doi": "10.1016/j.gaitpost.2018.12.003",
  "pmid": "30579037",
  "pmcid": null,
  "title": "Calibration and validation of accelerometer-based activity monitors: A systematic review of machine-learning approaches",
  "year": 2019,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "P-B25",
  "doi": "10.1152/japplphysiol.00519.2015",
  "pmid": "26940653",
  "pmcid": null,
  "title": "Cardiorespiratory fitness estimation using wearable sensors: Laboratory and free-living analysis of context-specific submaximal heart rates",
  "year": 2016,
  "pdf": null,
  "pdf_status": "free_not_redistributable"
 },
 {
  "id": "P-B26",
  "doi": "10.1038/s41746-022-00719-1",
  "pmid": "36460766",
  "pmcid": "PMC9718831",
  "title": "Longitudinal cardio-respiratory fitness prediction through wearables in free-living environments",
  "year": 2022,
  "pdf": "module-05-measurement-science/activity/literature/2022-spathis-npjdigitalmedicine-longitudinal-cardiorespiratory-fitness-prediction.pdf",
  "pdf_status": "stored"
 },
 {
  "id": "P-B27",
  "doi": "10.1186/s12966-015-0314-1",
  "pmid": "26684758",
  "pmcid": "PMC4683756",
  "title": "Systematic review of the validity and reliability of consumer-wearable activity trackers",
  "year": 2015,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "P-B28",
  "doi": "10.1136/bjsports-2018-099643",
  "pmid": "30194221",
  "pmcid": null,
  "title": "How well do activity monitors estimate energy expenditure? A systematic review and meta-analysis of the validity of current technologies",
  "year": 2020,
  "pdf": null,
  "pdf_status": "free_not_redistributable"
 },
 {
  "id": "P-B29",
  "doi": "10.1007/s40279-021-01639-y",
  "pmid": "35072942",
  "pmcid": "PMC9213394",
  "title": "Validity of Estimating the Maximal Oxygen Consumption by Consumer Wearables: A Systematic Review with Meta-analysis and Expert Statement of the INTERLIVE Network",
  "year": 2022,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "P-B30",
  "doi": "10.1016/j.maturitas.2018.03.016",
  "pmid": "29704922",
  "pmcid": null,
  "title": "The validity and reliability of consumer-grade activity trackers in older, community-dwelling adults: A systematic review",
  "year": 2018,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "P-B31",
  "doi": "10.2196/30791",
  "pmid": "35060915",
  "pmcid": "PMC8817215",
  "title": "Accuracy and Acceptability of Wrist-Wearable Activity-Tracking Devices: Systematic Review of the Literature",
  "year": 2022,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "P-B32",
  "doi": "10.1186/1479-5868-9-84",
  "pmid": "22776399",
  "pmcid": "PMC3464146",
  "title": "Validity of activity monitors in health and chronic disease: a systematic review",
  "year": 2012,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "P-B33",
  "doi": "10.1249/mss.0000000000000476",
  "pmid": "25121517",
  "pmcid": null,
  "title": "Comparison of step outputs for waist and wrist accelerometer attachment sites",
  "year": 2015,
  "pdf": null,
  "pdf_status": "paywalled"
 },
 {
  "id": "P-B34",
  "doi": "10.1016/j.gaitpost.2017.06.012",
  "pmid": "28666177",
  "pmcid": null,
  "title": "Accuracy of step count measured by physical activity monitors: The effect of gait speed and anatomical placement site",
  "year": 2017,
  "pdf": null,
  "pdf_status": "oa_not_obtained"
 },
 {
  "id": "P-B35",
  "doi": "10.1249/mss.0000000000000924",
  "pmid": "27031744",
  "pmcid": "PMC4993533",
  "title": "Comparison of Sedentary Estimates between activPAL and Hip- and Wrist-Worn ActiGraph",
  "year": 2016,
  "pdf": null,
  "pdf_status": "free_not_redistributable"
 },
 {
  "id": "P-B36",
  "doi": "10.1371/journal.pone.0285272",
  "pmid": "37167327",
  "pmcid": "PMC10174582",
  "title": "Resting heart rate is a population-level biomarker of cardiorespiratory fitness: The Fenland Study",
  "year": 2023,
  "pdf": "module-05-measurement-science/activity/literature/2023-gonzales-plosone-resting-heart-rate-cardiorespiratory-fitness-fenland.pdf",
  "pdf_status": "stored"
 }
]
```

## 4. Already in the KB, and needs hand download

### Already in the KB

- Fuller D et al 2020, *Reliability and Validity of Commercially Available Wearable Devices for Measuring Steps, Energy
  Expenditure, and Heart Rate: Systematic Review*, JMIR mHealth uHealth, [10.2196/18694](https://doi.org/10.2196/18694).
  Pooled steps and energy expenditure accuracy. `module-01-wearables/sources.md` (S-VAL-03).
- Chevance G et al 2022, *Accuracy and Precision of Energy Expenditure, Heart Rate, and Steps Measured by
  Combined-Sensing Fitbits Against Reference Measures: Systematic Review and Meta-analysis*, JMIR mHealth uHealth,
  [10.2196/35626](https://doi.org/10.2196/35626). `module-01-wearables/sources.md` (S-VAL-04).
- Migueles JH et al 2019, *GGIR: A Research Community-Driven Open Source R Package*, J Meas Phys Behav,
  [10.1123/jmpb.2018-0063](https://doi.org/10.1123/jmpb.2018-0063). Core open method for raw activity data.
  `module-05-measurement-science/sleep/literature-library.md` (S-036).
- Willetts M et al 2018, *Statistical machine learning of sleep and physical activity phenotypes from sensor data in
  96,220 UK Biobank participants*, Sci Rep, [10.1038/s41598-018-26174-1](https://doi.org/10.1038/s41598-018-26174-1).
  Activity classification model. `module-05-measurement-science/sleep/literature-library.md` (S-040).
- Straczkiewicz M et al 2023, *Validation of an open-source step counting algorithm for smartphone data collected in
  clinical and non-clinical settings* (oak), JMIR Cancer, [10.2196/47646](https://doi.org/10.2196/47646), and
  Straczkiewicz M et al 2023, *A "one-size-fits-most" walking recognition method for smartphones, smartwatches, and
  wearable accelerometers*, npj Digit Med, [10.1038/s41746-022-00745-z](https://doi.org/10.1038/s41746-022-00745-z).
  `module-02-digital-phenotyping/literature-library.md` (L049, L058).
- Straczkiewicz M et al 2021, *A systematic review of smartphone-based human activity recognition methods for health
  research*, npj Digit Med, [10.1038/s41746-021-00514-4](https://doi.org/10.1038/s41746-021-00514-4).
  `module-02-digital-phenotyping/literature-library.md` (L071).
- Shcherbina A et al 2017, *Accuracy in Wrist-Worn, Sensor-Based Measurements of Heart Rate and Energy Expenditure in a
  Diverse Cohort*, J Pers Med, [10.3390/jpm7020003](https://doi.org/10.3390/jpm7020003). Seven-device energy
  expenditure error. `module-01-wearables/literature-library.md`.
- Johnston W et al, INTERLIVE step count recommendations. `module-04-methods-and-reviews/literature-library.md`
  (M4-022). Lane A material in any case.

### Needs hand download

CC-licensed (or a CC-licensed repository copy listed by OpenAlex), but every automated route hit a bot check, returned
HTML, or is disallowed by robots.txt this pass. Target folder `module-05-measurement-science/activity/literature/`.

- P-B06 Beyond Cut Points (MSSE; CC BY copy on Figshare per OpenAlex, check the licence on the file): https://doi.org/10.1249/mss.0000000000001561. Save as `2018-rowlands-msse-beyond-cut-points-accelerometer-metrics-activity-profile.pdf`.
- P-B07 Enhancing the value of accelerometer-assessed physical activity (Sports Med Open, CC BY): https://doi.org/10.1186/s40798-019-0225-9, PMC6895365. Save as `2019-rowlands-sportsmedopen-translational-accelerometer-metrics-visual-comparisons.pdf`.
- P-B08 Comparison of Accelerometry-Based Measures of Physical Activity (JMIR, CC BY): https://doi.org/10.2196/38077, PMC9356340. Save as `2022-karas-jmirmhealth-comparison-accelerometry-based-measures-physical-activity.pdf`.
- P-B10 How fast is fast enough? (BJSM, CC BY-NC): https://doi.org/10.1136/bjsports-2017-097628, PMC6029645. Save as `2018-tudorlocke-bjsm-walking-cadence-intensity-narrative-review.pdf`.
- P-B11 Step Counting: A Review of Measurement Considerations (Sports Med, CC BY): https://doi.org/10.1007/s40279-016-0663-1, PMC5488109. Save as `2017-bassett-sportsmed-step-counting-review-measurement-considerations.pdf`.
- P-B12 Impact of accelerometer data processing decisions (BMC Public Health, CC BY): https://doi.org/10.1186/1471-2458-14-1210, PMC4247661. Save as `2014-keadle-bmcpublichealth-accelerometer-data-processing-decisions.pdf`.
- P-B14 2024 Adult Compendium of Physical Activities (J Sport Health Sci, CC BY-NC-ND): https://doi.org/10.1016/j.jshs.2023.10.010, PMC10818145. Save as `2024-herrmann-jshs-adult-compendium-physical-activities-third-update.pdf`.
- P-B17 Generating ActiGraph Counts from Raw Acceleration (MSSE; CC BY-NC copy in NORA per OpenAlex, check the licence on the file): https://doi.org/10.1249/mss.0000000000001344. Save as `2017-brond-msse-actigraph-counts-raw-acceleration-alternative-monitor.pdf`.
- P-B22 Self-Supervised Machine Learning to Characterize Step Counts (MSSE, CC BY): https://doi.org/10.1249/mss.0000000000003478, PMC11402590. Save as `2024-small-msse-self-supervised-step-counts-wrist-uk-biobank.pdf`.
- P-B24 Calibration and validation of accelerometer-based activity monitors (Gait Posture, CC BY-NC-ND): https://doi.org/10.1016/j.gaitpost.2018.12.003. Save as `2019-farrahi-gaitposture-machine-learning-activity-monitors-review.pdf`.
- P-B27 Systematic review of the validity and reliability of consumer-wearable activity trackers (IJBNPA, CC BY): https://doi.org/10.1186/s12966-015-0314-1, PMC4683756. Save as `2015-evenson-ijbnpa-validity-reliability-consumer-wearable-activity-trackers.pdf`.
- P-B29 Validity of Estimating the Maximal Oxygen Consumption by Consumer Wearables (Sports Med, CC BY): https://doi.org/10.1007/s40279-021-01639-y, PMC9213394. Save as `2022-molinagarcia-sportsmed-vo2max-consumer-wearables-meta-analysis.pdf`.
- P-B30 Consumer-grade activity trackers in older, community-dwelling adults (Maturitas; CC BY-NC-ND copy at Edinburgh Napier per OpenAlex, check the licence on the file): https://doi.org/10.1016/j.maturitas.2018.03.016. Save as `2018-straiton-maturitas-consumer-activity-trackers-older-adults-review.pdf`.
- P-B31 Accuracy and Acceptability of Wrist-Wearable Activity-Tracking Devices (JMIR, CC BY): https://doi.org/10.2196/30791, PMC8817215. Save as `2022-germini-jmir-wrist-wearable-activity-trackers-systematic-review.pdf`.
- P-B32 Validity of activity monitors in health and chronic disease (IJBNPA, CC BY): https://doi.org/10.1186/1479-5868-9-84, PMC3464146. Save as `2012-vanremoortel-ijbnpa-activity-monitors-health-chronic-disease-review.pdf`.
- P-B34 Accuracy of step count: effect of gait speed and placement (Gait Posture; CC BY-NC-ND accepted manuscript at UNSWorks per OpenAlex, check the licence on the file): https://doi.org/10.1016/j.gaitpost.2017.06.012. Save as `2017-chow-gaitposture-step-count-gait-speed-placement.pdf`.

## 5. Gaps noticed

- No open, multi-device evaluation of how consumer wearables turn heart rate and motion into calories turned up beyond
  pooled reviews (P-B28, P-B31); vendor energy expenditure and VO2max algorithms stay undocumented, and P-B29 is the
  only meta-analysis of consumer VO2max. Nothing pooled covers gait aids or wheelchair users; the 2024 Wheelchair
  Compendium (10.1016/j.jshs.2023.11.003) and Older Adult Compendium (10.1016/j.jshs.2023.10.007) were seen but not catalogued.
- Smartphone-carried step and activity methods are thin here because the main open ones already sit in Module 2. Sedentary
  posture classification from thigh devices (activPAL) appears only through P-B35 and P-B23; a targeted pass on
  thigh-worn open algorithms and on doubly labelled water validations of free-living energy expenditure would help.
