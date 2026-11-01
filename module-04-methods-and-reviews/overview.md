# Methods and reviews: what the literature says

This page is for a study team planning how to run a wearable or phone-sensing study. It was written on 2026-11-01 from the 51-row [catalogue](literature-library.md). Every open-access PDF was read in full (48 of 51). Three rows are paywalled and rest on their abstracts, and the bullets that cite them say so. Where a point rests on guidance or opinion rather than data, the bullet says so.

The eight sections follow the topic labels in the catalogue. The ten L rows carried over from Module 2 have no label. L086 sits under Ethics and consent and the other nine under Digital phenotyping and passive sensing reviews.

## Adherence and engagement

Six papers are catalogued here. Three are meta-analyses of self-report sampling, and the others review wearable adherence reporting, dementia protocols and social determinants.

### What the literature agrees on

- Short self-report protocols get most prompts answered. Pooled compliance was 78.7 percent across 79 studies in severe mental disorders [M4-001]. It was 79 percent across 477 EMA articles from many fields [M4-003].
- Long protocols do worse. In 77 mood monitoring studies lasting about seven months on average, pooled adherence was 0.64 and pooled attrition 0.28 [M4-005].
- Money raises compliance. Higher incentives went with higher compliance [M4-001]. So did paying money [M4-003]. Financial incentives raised adherence but did not change attrition [M4-005].
- Study length did not predict compliance in two meta-analyses [M4-001, M4-003].
- Who takes part matters. Samples with more men or with psychosis had lower compliance and retention [M4-001]. A review of 48 studies found compliance differed by routine, sex, age, income, language, education and race [M4-006].
- Passive mood monitoring did no better than active monitoring on adherence or attrition [M4-005].
- Reporting is poor. Of 177 wearable studies screened, 30 percent gave no sensor-based adherence measure [M4-002]. The other 100 used 37 definitions across 110 devices [M4-002].
- Long wearable studies in dementia need simple waterproof devices, carer support and repeated consent checks [M4-004]. This is qualitative, not effect data.

### Where it disagrees or is thin

- Prompt density is contested. Each extra prompt per day cut compliance by about one point [M4-001]. Prompts per day did not predict compliance in the larger review [M4-003].
- Sex effects differ. One review found lower compliance with more men overall [M4-001]. The other found the gap only in studies with about 60 or more prompts [M4-003].
- Reminders went with lower adherence, possibly confounded by longer follow-up [M4-005].
- Nearly all pooled rates come from self-report sampling. No row pools wear-time adherence for wearables.

### What a study team should do

1. Report device adherence first as a continuous measure, such as wear time or readings taken. Add categories only if needed [M4-002].
2. Describe the sensor, algorithm and software version behind the adherence figure [M4-002].
3. Report mean compliance with its SD, retention, the response window and any exclusion threshold [M4-001].
4. Build expected data loss into the sample size [M4-001]. Set acceptable adherence and attrition from the power calculation [M4-005].
5. Budget for payment, but note it may bias who enrols [M4-005].
6. Where the analysis allows, prefer longer protocols with fewer prompts per day. This is the authors' advice from pooled data [M4-001].

How Module 3 deployments define retention differently is set out in the definitions warning in the [feasibility matrix](../module-03-applied-studies/feasibility-matrix.md).

## Missing data and data quality

Six papers are catalogued here. They include a review of 36 trials, a trial framework, a rapid review, a youth EMA meta-analysis, a perspective and an operational framework.

### What the literature agrees on

- Missing data in this field are often not random. Attrition in active arms was about twice that of passive controls in 36 smartphone mental health trials [M4-008]. That makes data missing not at random likely [M4-008].
- Common fixes assume data are missing at random. Multiple imputation and maximum likelihood do not remove bias when that fails [M4-008]. None of the 36 trials tested the not-at-random case [M4-008].
- Zeros are ambiguous. A still wearer and a removed device can look the same [M4-009, M4-010]. Published nonwear rules range from 10 to 60 minutes of zero counts [M4-010].
- The definition of a valid day or a missing outcome varies, and it changes results [M4-009, M4-010].
- Heterogeneity is a quality problem too, and it rises when people bring their own devices [M4-010].
- Quality is easier to protect during a study than to repair after. With set-up checks, monitoring and troubleshooting, one mindLAMP study reached median GPS data quality of 0.92 [M4-012]. Earlier mindLAMP studies reported medians of 0.12 to 0.80 [M4-012]. There was no control group [M4-012].
- Low quality distorts features. Home time was underestimated by two to four hours once GPS sampling intervals passed 30 minutes [M4-012].
- In youth EMA, pooled acceptance was 67.27 percent, compliance 71.97 percent and retention 96.57 percent across 285 samples [M4-011].

### Where it disagrees or is thin

- Methods differ. One framework treats short days as censored and imputes at the day level [M4-009]. Another allows complete cases if missing and observed groups are similar [M4-007].
- Evidence is thin. The trial framework covers step count only [M4-009]. LINC comes from one short study of mostly iOS students [M4-012].
- Youth compliance fell 0.8 percent per publication year, and the paper cannot say why [M4-011].
- Two rows are guidance, not data [M4-007, M4-010].

### What a study team should do

1. Define missingness before collection. State wear-time rules, valid-day rules and how short days are handled [M4-009, M4-010].
2. Record device brand, model and software version with the data, and report them [M4-010].
3. Monitor quality in real time with set thresholds, and contact flagged participants [M4-012]. In LINC this took 1.3 contacts per participant and two research assistants [M4-012].
4. Compare people with and without missing data, and report the difference [M4-007].
5. Plan a not-at-random sensitivity analysis, above all when arms lose people at different rates [M4-008].

The LINC deployment also has a row in the [feasibility matrix](../module-03-applied-studies/feasibility-matrix.md) (Table 7).

## Validation frameworks

Six papers are catalogued here, two frameworks, a lessons paper, two expert statements and a risk of bias tool. All six are guidance, not tests of it.

### What the literature agrees on

- Validation has distinct steps. V3 separates verification of the sensor, analytical validation of the algorithm and clinical validation of the measure [M4-018].
- Validity holds only for a stated use. Clinical validation must be tailored to a context of use [M4-018]. INTERLIVE ties acceptable step error to the use case [M4-022]. The DACIA authors say the research question should drive device choice [M4-020].
- Verification is usually the maker's job, since it needs access to hardware and firmware that may be proprietary [M4-018].
- Usability is now a fourth component. V3+ adds a use specification, a use-related risk analysis, formative evaluation and summative evaluation [M4-019]. In one Parkinson's study, half of participants lost tremor data after device permissions were switched off by accident [M4-019].
- Devices should be tested where they will be used. One wrist tracker's step error was at most 5.2 percent on a treadmill but 17.5 to 22.8 percent in free living [M4-022]. INTERLIVE asks for laboratory, semi-free-living and free-living stages [M4-022].
- Both INTERLIVE statements ask for Bland-Altman limits of agreement with confidence intervals [M4-021, M4-022].
- Past validation studies were inconsistent. Reviews behind INTERLIVE covered 44 heart rate and 85 step articles [M4-021, M4-022]. Only 8 of the 85 used video with two observers [M4-022].

### Where it disagrees or is thin

- Thresholds differ. INTERLIVE asks for step error of 5 percent or less in trials, and 10 to 15 percent for general use [M4-022]. The heart rate statement sets no fixed level [M4-021].
- Free-living reference methods are impractical. Video for 45 people over one day means 450 to 630 hours to review, and no cheaper method is accepted [M4-022].
- DACIA rests on one multiple sclerosis pilot cohort [M4-020]. None of the frameworks targets phone sensing.

### What a study team should do

1. Write an intended use statement before choosing a device [M4-019].
2. Ask the maker for verification documents, and check analytical validation used a population like yours [M4-018].
3. Test usability with target users before launch, including permission settings [M4-019].
4. If you validate a device yourself, follow the INTERLIVE protocols for heart rate or steps [M4-021, M4-022].
5. Report error in full rather than calling a device valid, unless a powered test was planned [M4-022].
6. Use WEAR-BOT to judge published validation studies [M4-023].
7. Plan how wearable data become a marker. DACIA covers data, aggregation, context, interpretation and action [M4-020].

## Reporting guidelines

Five papers are catalogued here. They are a heart rate guideline with checklists, a STROBE extension built on a review of 20 studies, a scoping review of accelerometry guidance, a preregistration template and one paywalled review.

### What the literature agrees on

- Reporting is inconsistent. In 20 location-linked EMA studies, 45 percent did not say who owned the devices [M4-025]. Only 4 gave the window allowed to answer a prompt [M4-025]. A review of wearable tracker papers found no standard approach [M4-039]. That point rests on the abstract only.
- Report the device in full. The heart rate checklist asks for maker, type, version, firmware, sensor and sampling rate [M4-024]. Accelerometry guidance agrees on model, settings and protocol [M4-026].
- Report how data were cleaned. Wear-time rules, valid days and missing data handling were broadly agreed items [M4-026]. The heart rate guideline asks for nonwear definitions and advises against listwise deletion [M4-024].
- Report participant factors that affect sensors. The heart rate guideline asks for skin tone, wrist circumference and wrist placement [M4-024].
- Fix analysis choices in advance. The preregistration template covers six themes, from constructs to open science [M4-027]. The heart rate guideline also urges preregistration [M4-024].
- Location EMA has its own checklist. STROBE-GEMA has 70 items in 27 categories, including a new consent category [M4-025].

### Where it disagrees or is thin

- There is too much guidance. One review found 380 items in 47 publications, merging to 124 unique items [M4-026]. Only 17 percent described stakeholder involvement [M4-026].
- Guidance agrees on methods but not on which metrics to report [M4-026]. Little of it covers reporting algorithm validation [M4-026].
- No catalogued row gives a reporting checklist for phone sensing. The preregistration template is the closest [M4-027].
- No row tests whether any of these guidelines improves papers.

### What a study team should do

1. For wrist heart rate, complete the two Nelson checklists and add them to the supplement [M4-024].
2. For EMA linked to GPS, follow STROBE-GEMA [M4-025].
3. For accelerometry, report collection, processing, derivation and summary metrics [M4-026].
4. Preregister passive sensing studies with the template [M4-027]. Disclose what you cannot know, such as closed commercial algorithms [M4-027].
5. State the reliability your study needs and why. The heart rate guideline declines a single threshold [M4-024].

Why reported figures cannot be compared at face value is shown in the definitions warning in the [feasibility matrix](../module-03-applied-studies/feasibility-matrix.md).

## Ethics and consent

- Eight papers. Two are scoping reviews [M4-013, M4-016], two are Delphi studies [M4-015, L086], two are consent-form methods papers [M4-014, M4-017] and two are paywalled ethics essays [M4-040, M4-041].

### What the literature agrees on

- Privacy dominates the ethics literature. It appeared in all 13 papers of one review [M4-016]. It topped the list of issues across 151 publications in another [M4-013].
- Most of this literature is technical, not ethical [M4-013].
- Consent forms for digital health studies miss a lot. None of 25 real forms held every required or optional element [M4-017]. The best form covered 50 of 68 mandatory elements, or 73.5 percent [M4-017].
- The gaps cluster on technology. Seventeen NIH-recommended technology elements appeared in no more than two forms [M4-017]. One worked example covered only 2 of 7 privacy prompts and 2 of 10 data management prompts [M4-014].
- Consent text is hard to read. Rewriting one sensor consent form cut its grade level from 12.6 to 9.2 [M4-014]. It still missed the 6th to 8th grade target [M4-014].
- Experts want plain disclosure. A Delphi panel asked for sixth-grade forms naming data types, possible inferences and who receives data [M4-015]. This is guidance, not data.
- In suicide-risk studies, experts agreed not to exclude high-risk participants (90.5 percent) [L086]. They agreed to respond to imminent risk within 24 hours (94.4 percent) [L086]. This is panel opinion.

### Where it disagrees or is thin

- Experts split on whether raw sensor data can ever be non-identifying [M4-015].
- The suicide-risk panel reached no consensus on risk levels or on whether a safety monitoring board is needed [L086]. Calling 911 for high risk got only 50 percent [L086].
- The evidence base is small. The two Delphi panels ended with 17 and 21 respondents [M4-015, L086]. One consent method rests on a single form [M4-014].
- Return of results [M4-040] and research with vulnerable groups [M4-041] rest on abstracts only.

### What a study team should do

1. Check your consent form against the NIH-aligned framework [M4-017] or the Digital Health Checklist [M4-014].
2. Name the data controller, retention, deletion and vendor terms in the form [M4-017].
3. Disclose bystander recording if you use a microphone [M4-014].
4. Run readability tools and add visuals [M4-014]. Aim for a sixth-grade level [M4-015].
5. In suicide-risk studies, test alerts before launch and review data every weekday [L086]. Tell participants monitoring is not a safety net [L086].
6. Plan with communities when studying vulnerable groups [M4-041]. This point rests on the abstract.

## Equity and representativeness

- Three papers. One is a conceptual review [M4-028], one a narrative review of 23 studies [M4-029] and one a scoping review of 42 frameworks [M4-030].

### What the literature agrees on

- Wearable benefits flow mostly to people with more money and digital skill [M4-028]. This is argument, not data.
- Older adults and children are underrepresented in wearable datasets [M4-028].
- Skin tone may affect wrist PPG for some devices. The review reports underestimation of 10 to 15 bpm on some WearOS watches in darker skin during exercise [M4-029]. It reports under 5 bpm variation for Apple Watch [M4-029].
- Regulators do not require validation across skin tones [M4-029]. This is the review's reading of FDA and CE rules.
- Equity frameworks rarely define their subject. Only 5 of 44 publications defined digital health equity [M4-030].
- Frameworks cluster at the organisational level (79.4 percent) and neglect the interpersonal level (17.6 percent) [M4-030]. Only one framework covered every level [M4-030].

### Where it disagrees or is thin

- The skin tone evidence conflicts. The review itself calls its findings conflicting [M4-029]. Several abstract figures cannot be traced to any included study [M4-029].
- No catalogued paper measures how sample makeup changes digital phenotyping results. The case rests on argument [M4-028].
- The framework review covers digital health broadly, not wearables [M4-030].
- No framework offers a validated equity measure [M4-030].

### What a study team should do

1. Assess how representative your sample is before you start [M4-028].
2. Check device validation by Fitzpatrick skin type and activity level [M4-029]. Treat errors over 10 bpm as meaningful, as the review does [M4-029].
3. Report skin tone, age and income in device studies, so others can check bias [M4-028, M4-029].
4. Choose an equity framework that spans several levels, including interpersonal and community [M4-030].
5. Work with community organisations on recruitment and design [M4-030].

## Privacy and governance

- Two papers. One is a perspective on governance [M4-031] and one a scored review of 17 manufacturers' privacy policies [M4-032].

### What the literature agrees on

- Almost any personal data can now become health data [M4-031]. This is argument.
- Consumer devices move health inference outside research ethics review [M4-031].
- Legal protection is uneven. GDPR gives a baseline [M4-031]. HIPAA depends on who holds the data [M4-031]. US general law has no concept of sensitive data [M4-031].
- Wearable privacy policies have clear weak spots. Transparency reporting was high risk at 76 percent of companies [M4-032]. Vulnerability disclosure was high risk at 65 percent [M4-032]. Breach notification was high risk at 59 percent [M4-032].
- Companies differ widely. Total risk scores ran from 33 (Google) to 60 (Xiaomi and Wyze) on a 24 to 72 scale [M4-032]. Apple scored 35, and Oura and Polar 38 [M4-032].
- Policies are long. They averaged 6113 words, about 26 minutes to read [M4-032].
- Genomics offers working models, such as data access committees, safe havens and tiered consent [M4-031].

### Where it disagrees or is thin

- A policy is not a practice. The scoring authors say so as their main limit [M4-032]. Two low-risk firms had large privacy settlements [M4-032].
- Privacy tools carry costs. Differential privacy is hard to apply [M4-031]. Dynamic consent can shrink data for secondary studies [M4-031].
- Neither paper looks at research platforms. Both look at consumer devices.

### What a study team should do

1. Read each vendor's policy before you choose a device. Use the 24 criteria as a checklist [M4-032].
2. Get explicit consent for secondary use [M4-031]. Consider tiered consent through the phone [M4-031].
3. Prefer sharing models over sharing raw data where you can [M4-031].
4. Add noise to GPS before sharing [M4-031].
5. Ask vendors about breach notification and third-party requests, since policies often say nothing [M4-032].

## Digital phenotyping and passive sensing reviews

- Fifteen papers. Five are systematic, umbrella or scoping reviews [M4-034, M4-036, M4-038, L071, L084]. One synthesises seven reviews [M4-037]. Nine are narrative reviews or perspectives [M4-033, M4-035, L073, L090, L092, L095, L102, L110, L111].

### What the literature agrees on

- Most studies are small and short. In 51 depression studies the median sample was 58 [M4-034]. In 65 smartphone studies the median was 52 and the median length 8 weeks [M4-038]. Most activity recognition studies had fewer than 30 people [L071].
- Reporting is poor. Only 6 of 65 studies reported missingness by stream [M4-038]. Only 4 reported sampling rates [M4-038]. In depression studies 63 percent did not report ethnicity [M4-034].
- Code and data are rarely shared. Only 4 of 108 activity studies shared code [L071]. Only 1 of 65 studies gave a working data link [M4-038].
- Lab results may not hold in daily life. Activity accuracy was typically above 95 percent [L071]. There was little evidence it generalises to free living [L071].
- Measures do not line up across studies. Depression studies used 423 different passive performance measures [M4-037].
- Passive measures are not ready to replace standard outcomes [M4-037]. In bipolar disorder they correlated weakly [M4-037].
- Some signals recur. Homestay was linked to depression in every study that measured it [M4-034].
- iOS and Android differ. Every iPhone since 2018 has a barometer, against 31 percent of 2024 Android phones [M4-036].

### Where it disagrees or is thin

- Most syntheses count votes without weighting by size or quality [M4-034].
- Hardware being present does not mean the data are usable [M4-036].
- Screening needs very high specificity. At a 0.6 percent prevalence, a bipolar test needs at least 99.4 percent [M4-033]. The best study reached 87.2 percent [M4-033].
- All mood-monitoring evidence comes from Western countries [M4-037].
- One row is an intervention meta-analysis, not a sensing review [L084].

### What a study team should do

1. Collect raw data where possible [L090, L111]. Vendor API data are not truly raw [M4-035].
2. Report phone model, OS, sensor streams, sampling rate and missingness per stream [M4-038].
3. Check results for OS differences, which can stand in for income [L090, L102].
4. Confirm passive measures with a validated self-report [M4-037].
5. Build cross-platform studies on sensors present on every phone [M4-036].
6. Report specificity, not only sensitivity [M4-033].
7. Share feature code and, where allowed, anonymised data [M4-034, L071].

## Open gaps

- One reporting row is paywalled and was read from its abstract only [M4-039].
- No row pools wear-time adherence for consumer wearables.
- No validation framework or reporting guideline targets phone sensing directly.
- No row tests whether following a framework or checklist changes study results.
- Two ethics rows are paywalled and were read from their abstracts only [M4-040, M4-041].
- Equity has three rows and privacy two. Both were searched several ways, and the open-access literature there is small.
- L084 is a meta-analysis of mHealth interventions for quality of life in cancer, not a sensing review. It sits under phenotyping reviews only because it has no better home.
