# Cardiac: what the evidence says

This page is for a study team choosing how to measure heart rate, HRV, rhythm (AF) or blood pressure with wearables or phones. It was written on 2026-10-23 from the 68-row [catalogue](literature-library.md). Many rows rest on abstracts only, so this page adds no detail beyond them. Where a point rests on guidance rather than data, the bullet says so.

## What the field agrees on

- Wrist PPG heart rate is close to ECG or chest strap at rest, in sleep and on a treadmill. Mean error was near zero in those conditions across 44 studies and 15 brands [C-053].
- Daily resting heart rate is mostly stable within a person, while it varies widely between people. That supports comparing each participant with their own baseline [C-038].
- An AF diagnosis needs an ECG. A PPG irregularity alert is not enough on its own. This is guidance, stated by the EHRA practical guide [C-001], the ESC 2024 guideline [C-024] and the AF-SCREEN report [C-019]. The ESC guideline accepts a single-lead strip of 30 s or more [C-024].
- Pulse rate variability from PPG is not interchangeable with ECG-derived HRV in every setting. It works reasonably at rest but degrades with activity and some stressors [C-036, C-037]. Cold exposure made PRV diverge from HRV, and the size of the gap depended on the body site [C-064].
- RMSSD holds up better than SDNN in short recordings. A single 10 s ECG gave a valid RMSSD in 3,387 adults, and agreement was near perfect at 120 s [C-034].
- Cuff validation protocols do not fit cuffless BP devices. Calibration, tracking of BP change and stability over time all need their own tests [C-014, C-027]. ESH has published a six-test procedure for intermittent cuffless devices [C-026].

## Where devices fall short

- Wrist heart rate error grows during resistance training (-7.3 bpm) and cycling (-4.6 bpm). In resistance training it rose by about 3 bpm for every 10 bpm rise in heart rate [C-053]. Absolute error during activity was about 30% higher than at rest, and devices differed from each other [C-061].
- Open-source PPG beat detectors scored F1 of 90% or more at rest. Performance fell during exercise and in AF [C-042].
- Nocturnal HRV is not equally reliable for every metric. LF power and LF/HF were poorly reproducible across three nights in all sleep stages [C-040].
- Skin tone evidence is split. Four of ten studies found lower accuracy in darker skin, and four found no effect [C-060]. A light-transport model showed darker skin and higher BMI cutting the PPG signal by up to 61%, depending on sensor layout [C-063].
- Pooled AF accuracy figures look high but rest on weak studies. Smartphone PPG pooled 94% sensitivity and 97% specificity, and the authors call those figures unrealistically high [C-056]. Smartwatch pooling showed very high heterogeneity [C-057].
- Consumer AF screening has not shown a clinical benefit. Clinician-led ECG screening trials have not shown a significant stroke reduction [C-022]. USPSTF found the evidence insufficient to weigh benefits and harms [C-023].
- Three societies advise against relying on current cuffless BP devices in clinical care. These are the positions of ESH [C-014], AHA [C-015] and Hypertension Canada [C-016]. Pooled device bias was small but highly heterogeneous [C-059].
- Pulse arrival time includes the pre-ejection period, so it is a poor stand-in for pulse transit time [C-066, C-067]. In phenylephrine tests the pre-ejection period changed by 5.5 ms on average [C-068].

## What a study team should do

1. Write down whether you need heart rate, HRV, rhythm or BP. The evidence differs for each one.
2. Use the SPR design, analysis and reporting checklists before you lock the protocol [C-010].
3. For heart rate during strength or cycling work, check the device against ECG in a subsample, or accept wider error [C-053, C-061].
4. For HRV, prefer RMSSD and record at least 120 s where you can [C-034]. Fix body position and report the metric you used, since those moderate error [C-055].
5. If the device gives PRV rather than ECG HRV, call it PRV in the protocol and the paper [C-037, C-064].
6. Keep your own beat detection and signal quality steps auditable. Open benchmarks exist for beat detectors [C-042] and signal quality indices [C-043, C-044].
7. For AF, plan an ECG confirmation step and a clinician over-read [C-001, C-024].
8. For BP, keep a cuff device as the measure of record. Treat cuffless values as exploratory, which is the society position in [C-014], [C-015] and [C-016].
9. Analyse change within a person against their own baseline [C-038].
10. Report skin tone and BMI, and check accuracy across both [C-060, C-063].

## Open gaps

- The core standards are sold, not free. IEEE 1708 [C-029], ISO 81060-3 [C-030] and both CTA heart rate standards [C-031, C-032] could not be read.
- The ESH cuffless statement and validation protocol are paywalled. Their content here comes from the abstracts [C-014, C-026].
- No catalogue row gives clinical guidance on when to act on wearable heart rate data. The ESC e-cardiology position paper says no such guideline exists [C-003].
- No well-powered skin tone study with objective skin tone measurement was found [C-060].
- The cuffless BP guidance document with the most practical detail is industry-authored. Five of its nine authors list the device maker, Aktiia SA, as their affiliation [C-018]. Treat it as vendor guidance, not a society statement.
- Some rows were not read in full. HeartPy [C-048] and the EHRA screening consensus [C-020] are summarised from metadata or scope only.

## Read these first

| Row | Why |
|---|---|
| [C-010] | Society checklists for designing, analysing and reporting HR and HRV studies. |
| [C-053] | Shows where wrist heart rate holds and where it drifts, by activity type. |
| [C-042] | Open benchmark of PPG beat detectors, with the code and data public. |
| [C-001] | EHRA guide on matching rhythm devices to the clinical question, and on ECG confirmation. |
| [C-027] | Explains why cuff validation does not cover cuffless BP devices. |

## Related in this library

- [Cardiac hub](hub.md) lists every paper and profile in Modules 1 to 4 tagged cardiac.
- Module 1 profiles: [Polar](../../module-01-wearables/profiles/polar.md) (H10 ECG strap and RR intervals), [Movesense](../../module-01-wearables/profiles/movesense.md) (single-lead ECG and RR intervals), [Apple Watch / HealthKit](../../module-01-wearables/profiles/apple-watch-healthkit.md) (ECG, AF and hypertension notifications).
- Module 3 studies: [Fitbit Heart Study siteless AF trial](../../module-03-applied-studies/profiles/fitbit-heart-study-afib.md) and [Apple Heart Study data-management lessons](../../module-03-applied-studies/profiles/apple-heart-data-management-lessons.md).
