# Mental health: what the evidence says

This page is for a study team measuring mood, depression, anxiety, stress or psychosis-related outcomes with smartphones, wearables and EMA. It was written on 2026-10-23 from the 53 papers in this domain's [catalogue](literature-library.md). Bracketed IDs point to catalogue rows. Where a point rests on guidance and not data, the bullet says so.

## What the field agrees on

- EMA response can match clinician-rated response. In one 6-week antidepressant trial of 36 adults, the two agreed in 33 of 36 cases [H-019]. That is one small trial, not a settled finding.
- Several EMA item sets have tested reliability. PANAS-X scales separated people and measured within-person change across four samples [H-015]. A 28-item suicidality set was reliable for all scales except anxiety [H-014].
- Single EMA items carry real measurement error. In two studies the error was close to a tenth of the scale [H-013].
- Single items still work in many cases. They correlated .24 to .61 with their multi-item scales [H-016]. Multi-item measures did better, but by a modest margin [H-016].
- EMA of suicidal ideation picked up more ideation than retrospective self-report. The review found no evidence of systematic mood reactivity [H-018].
- A few passive features recur with a consistent direction. Home stay, sleep duration and vigorous activity correlated consistently with depressive symptoms across 46 studies [H-035]. GPS location variance, entropy and circadian movement correlated with PHQ-9 in two small samples [H-024] [H-026].
- People with depression were less active than controls in a meta-analysis of 38 actigraphy studies. They also had longer wake after sleep onset [H-041].
- Reporting standards are a shared concern. Two groups have proposed reporting guidelines for remote mood data and ambulatory assessment [H-022] [H-023]. Both are recommendations from those groups.

## Where passive sensing falls short

- Models often fail to generalise. A GPS pipeline fell from AUC 0.82 in 57 students to 0.57 in a US-wide sample of 5,262 [H-051].
- Published depression algorithms barely beat a majority-class baseline across four datasets [H-047]. A related benchmark found cross-dataset generalisation still inadequate [H-032].
- Mood models applied to an unseen country performed worse [H-048].
- Sample-wide models of daily mood can fail outright. In 271 participants the median R squared was about 0 [H-033].
- Personalisation helps sometimes, not always. It helped most participants in one study [H-033]. It helped in only one case in another [H-052]. The best model and predictors differed from person to person [H-034].
- Some features flip direction between studies. SMS count, time between locations and screen activity did so [H-035].
- Record-wise cross-validation greatly overestimates accuracy [H-050]. Almost half of the smartphone and wearable studies reviewed used it [H-050].
- Pooled accuracy figures are not a guide to clinical use. Wearable AI for depression pooled a highest accuracy of 0.89 and a lowest of 0.70 [H-037]. The authors judged it not ready for clinical use on its own [H-037]. Anxiety estimates had wide confidence intervals [H-038]. Only 6 of 19 stress studies could be pooled [H-039].
- Quality features alone predicted operating system with up to 0.98 accuracy [H-053]. Operating system can therefore confound sensor features [H-053].
- Only 30 of 203 psychosis studies assessed data quality [H-045].
- Most bipolar studies had 50 or fewer participants [H-044].
- Whether a phone measure counts as a digital biomarker is disputed. One author argues the term should exclude most behavioural phone measures [H-010]. That is one author's position.

## What a study team should do

1. Define the construct and the reference scale before choosing sensors. The layered model of raw data, features, behaviours and states is one way to plan this [H-008].
2. Choose EMA items against a quality tool. ESM-Q gives 10 core criteria from an expert Delphi [H-012].
3. Prefer items with published reliability for your construct [H-014] [H-015]. Budget for measurement error if you use single items [H-013].
4. Use shared feature definitions. Options in the catalogue include standard GPS features [H-024], a location preprocessing framework [H-027], GeMAPS for voice [H-028] and an open feature pipeline [H-030].
5. Record operating system and model it as a possible confounder [H-053].
6. Validate subject-wise, never record-wise [H-050].
7. Test on an external dataset or population before claiming accuracy [H-047] [H-051].
8. Assess and report data quality and missingness [H-045] [H-044].
9. Follow published reporting guidance for mood and ambulatory data [H-022] [H-023].
10. Plan a long enough follow-up with repeated outcome ratings. One bipolar group names short assessment periods and rare outcome ratings as causes of inconsistent findings [H-009]. This is that group's view.
11. For negative symptoms in regulated trials, expect no agreed reference standard yet [H-002]. An ISCTM work group calls these digital measures early in maturity [H-001].

## Open gaps

The seeding pass searched for these and found nothing to catalogue:

- Test-retest reliability of passive features. Reliability work in the catalogue covers EMA items only [H-013] [H-015].
- Weather or season as a confounder of mobility, sleep or activity features.
- Measurement guidance written for stress. The catalogue's stress evidence is one meta-analysis of student studies [H-039].
- Measurement guidance written for social behaviour. Loneliness detection evidence was judged uncertain [H-046].

## Read these first

| Row | Why |
|---|---|
| [H-035] | Catalogue of 85 depression features and which ones hold direction across studies |
| [H-050] | Shows how record-wise validation inflates accuracy |
| [H-047] | Re-runs nine published depression algorithms across datasets |
| [H-045] | Review of how 203 psychosis studies processed passive data |
| [H-023] | Reporting recommendations for ambulatory assessment studies |

## Related in this library

- [Mental health hub](hub.md) lists 107 tagged papers and profiles in Modules 1 to 4.
- [Module 4 catalogue](../../module-04-methods-and-reviews/literature-library.md) holds general research practice, including EMA adherence, missing data and ethics.
- Platform profiles tagged primary for mental health on the hub are [LifeData](../../module-02-digital-phenotyping/profiles/lifedata.md) and [mindLAMP](../../module-02-digital-phenotyping/profiles/mindlamp.md). The hub lists all seven device and platform profiles.
- Module 3 deployments relevant to measurement:
  - [RADAR-MDD recruitment, retention and data availability, N=623](../../module-03-applied-studies/profiles/radar-mdd-recruitment-retention.md)
  - [CONNECT pilot comparing three wearables in psychosis, N=105](../../module-03-applied-studies/profiles/connect-multi-wearable-psychosis.md)
  - [Kivelä et al. 2024 on iatrogenic effects of suicidal ideation EMA](../../module-03-applied-studies/profiles/avicenna-ema-suicidal-ideation-iatrogenic.md)
