# Legacy and Adjacent Platforms

This file covers platforms and projects that are historically important to digital phenotyping but were not given full standalone profiles, either because they are discontinued/legacy, or because they are adjacent (a dataset, a research-only lab tool without external reuse, or a commercial company whose "platform" is not clearly deployable by outside researchers). Per CLAUDE.md's instruction, discontinued or legacy platforms are labeled clearly rather than excluded.

---

## Purple Robot

| Field | Details |
|---|---|
| Organization | Center for Behavioral Intervention Technologies (CBITS) / Precision Health Informatics Data Lab, Northwestern University |
| Status | **Legacy, status as actively maintained/current is Unclear.** Referenced consistently in the methods literature as a historical open-source digital-phenotyping platform alongside Beiwe, AWARE, and RADAR-base. |
| Platform coverage | **Android only**, search evidence describes it as having "the most complete coverage of Android sensors and features amongst the platforms reviewed," but explicitly **does not support iOS**. |

Purple Robot is one of the earliest open-source Android digital-phenotyping/sensing platforms, developed at Northwestern's CBITS (now folded into the Precision Health Informatics Data Lab). It is still referenced as a comparison baseline in current (2026) survey literature reviewing digital-phenotyping platforms, but this session found **no evidence of recent active development or maintenance** comparable to Beiwe, RADAR-base, mindLAMP, or AWARE, and its Android-only nature is a significant scope limitation for any modern multi-platform study. **Not given a full profile** because current maintenance status, current documentation, and current researcher-facing access mechanisms could not be established, a research team considering it should first confirm with the Precision Health Informatics Data Lab whether it is realistically deployable today.

**Second-pass update (2026-08-24):** a direct-fetch attempt was made on the lab's key page and on the lab's root domain (`https://phidatalab.org/`, `https://phidatalab.org/software/`, `https://phidatalab.org/software__trashed/purple-robot-android-apps/`). **The entire phidatalab.org domain returned HTTP 500 Internal Server Error on every path tested this session**, not a 404 or access-denied, but a server error suggesting the site itself may currently be broken, migrating, or offline, independent of the specific "software__trashed" URL slug question. This is new corroborating (not conclusive) evidence consistent with reduced institutional maintenance of the lab's public web presence generally, though a transient outage cannot be ruled out from a single session's fetch attempts. WebSearch corroborates that Purple Robot is still cited in current methods literature (2026) as a historical platform but returned no direct evidence of its live maintenance status either. **Status remains Unclear, resolution still requires either a successful fetch on a later attempt or direct contact with the Precision Health Informatics Data Lab; the domain-wide 500 errors are a new, mildly negative signal worth flagging rather than a confirmed retirement.**

Key link: https://phidatalab.org/software__trashed/purple-robot-android-apps/ (the URL slug itself, "software__trashed", is a notable signal about the project's likely retirement status; the domain-wide server errors found in the second pass neither confirm nor refute this, since the whole site was unreachable, not just this page).

## StudentLife

| Field | Details |
|---|---|
| Organization | Dartmouth College (Andrew Campbell's group) |
| Status | **Historical research study and its resulting open dataset, not a reusable platform for new studies.** |

StudentLife was a landmark 2013 to 2014 Dartmouth study (and the Android app built for it) that pioneered smartphone passive-sensing research on student mental health, academic performance, and behavioral trends. Its lasting artifact for the field is the **StudentLife dataset**, which remains widely used in secondary machine-learning and mental-health research (a `studentlife` R/data package exists on Zenodo for handling it). It is included here because it is frequently named alongside Beiwe, AWARE, and Purple Robot in platform-comparison literature, but it should not be confused with an actively deployable platform: it is a historical app tied to one study, whose primary continuing value to new researchers is the **dataset it produced**, not a tool for collecting new data today.

## Koa Health

| Field | Details |
|---|---|
| Organization | Koa Health (commercial digital-mental-health company) |
| Status | Active company with an active digital-phenotyping **research program**, but **not clearly a platform other research teams can deploy for their own independent studies.** |

Koa Health publishes substantial digital-phenotyping research (patents, papers on passive-smartphone-data-informed CBT, encrypted-network-traffic behavioral signals, and more) and explicitly describes digital phenotyping as core to its work. However, this session found no evidence of a publicly documented, externally deployable "Koa Health platform" comparable to Beiwe or Avicenna Research, its digital-phenotyping capability appears to be internal technology supporting its own commercial mental-health products and research collaborations, not a general-purpose research infrastructure product. **Explicitly deferred rather than profiled**, pending direct confirmation from Koa Health about whether any component is available to outside research teams.

**Second-pass update (2026-08-24):** direct fetch of https://www.koahealth.com/research confirms the site's own language frames digital phenotyping strictly as an internal method, "We use digital footprints, ethically acquired from personal devices, to quantify personal characteristics, behaviors, emotions and cognitive states", applied through partnerships with academic groups (London School of Economics, Universitat Pompeu Fabra) rather than offered as a product. **The page contains no mention of a deployable platform, SDK, API, or any mechanism for an outside research team to use Koa Health's technology on their own study**, the absence is itself informative, not just an unread gap. This upgrades the exclusion rationale from Reported/inferred to **Corroborated by direct primary-source absence**: nothing on Koa Health's own research page describes external platform availability. It remains short of fully Verified/resolved because the only way to rule out an unlisted partnership-only or enterprise-only offering is direct vendor contact (their consultation-booking flow), which this session did not initiate, that step still requires the user's decision to reach out, per this knowledge base's rule against fabricating vendor confirmations.

## PhoneStudy / other named-but-unverified candidates

CLAUDE.md's onboarding prompt for this module named several additional candidates for discovery: **PhoneStudy**, **Insight (Koa Health)**, and other StudentLife-derived or LAMP-adjacent tools. This session's searches surfaced Koa Health (above) but did **not** turn up a distinct, independently notable "PhoneStudy" platform separate from general academic phone-sensing research use of that generic term, nor any further LAMP-adjacent forks beyond what is already covered in `mindlamp.md`. These are recorded as **not found / not verified** rather than silently dropped, per CLAUDE.md's instruction to record uncertain inclusion decisions.

## Samsung Health Research Stack, cross-reference note

Samsung's Health Research Stack (open-source SDK + backend + web portal for wearable/phone health research) is already profiled in **Module 1** (`../../module-01-wearables/profiles/samsung.md`) because its primary identity in this knowledge base is as a wearable-ecosystem research access route. It has some digital-phenotyping-adjacent characteristics (a self-hosted open-source research backend), and a team building a passive-sensing study around Samsung devices specifically should consult that Module 1 profile alongside this module rather than expect a duplicate entry here.

---

## Sources

1. Search-summary characterization of Purple Robot via digital-phenotyping platform survey literature (accessed 2026-08-24), including "Sensing Apps and Public Data Sets for Digital Phenotyping of Mental Health: Systematic Review," PMC. https://pmc.ncbi.nlm.nih.gov/articles/PMC8895287/
2. Precision Health Informatics Data Lab, Purple Robot Android Apps page. https://phidatalab.org/software__trashed/purple-robot-android-apps/ (accessed 2026-08-24, first pass; **direct-fetch attempted again 2026-08-24 second pass, returned HTTP 500 across the whole domain, see profile text above**). URL slug used as a (still unconfirmed) retirement signal.
3. `studentlife` R package on Zenodo. https://zenodo.org/records/3371922 (accessed 2026-08-24, search summary). Establishes the dataset's continuing secondary-research use.
4. Koa Health, Research page and complete research-papers listing. https://www.koahealth.com/research ; https://koahealth.com/legal/complete-research-papers/ (accessed 2026-08-24, search summary first pass; **https://www.koahealth.com/research direct-fetched 2026-08-24 second pass, Primary/Corroborated**, confirmed no platform-availability language present on the page).
