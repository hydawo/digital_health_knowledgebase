# Legacy and Adjacent Platforms

This file covers platforms and projects that are historically important to digital phenotyping but were not given full standalone profiles, either because they are discontinued/legacy, or because they are adjacent (a dataset, a research-only lab tool without external reuse, or a commercial company whose "platform" is not clearly deployable by outside researchers). Per CLAUDE.md's instruction, discontinued or legacy platforms are labeled clearly rather than excluded.

---

## Purple Robot

| Field | Details |
|---|---|
| Organization | Center for Behavioral Intervention Technologies (CBITS), Northwestern University. Last maintained by its developer, Chris Karr (GitHub user audaciouscode, Audacious Software). Sources 10, 11. |
| Status | **Archived, no longer developed (Verified, 2026-10-22).** The maintainer wrote on 2023-12-20 that the app "is currently archived and no longer being currently developed" (issue 282). Last code: `cbitstech/Purple-Robot` master 2016-04-11 (v2.0.9); the `audaciouscode/Purple-Robot-Android` continuation 2019-01-30 (v3.0.13, target API 28). No formal end-of-life date was announced, and GitHub's archive flag is not set on the main repositories. Referenced in the methods literature as a historical open-source platform alongside Beiwe, AWARE, and RADAR-base. Sources 10, 12. |
| Platform coverage | **Android only**, search evidence describes it as having "the most complete coverage of Android sensors and features amongst the platforms reviewed," but explicitly **does not support iOS**. No longer in any store: the Google Play listing returns 404 and there is no F-Droid listing, so teams build the APK from source (Verified, 2026-10-22). Source 13. |
| Last verified | 2026-10-22 (vendor fact record) |

Purple Robot is one of the earliest open-source Android digital-phenotyping/sensing platforms, developed at Northwestern's CBITS as infrastructure for its own intervention and sensing studies. It is still referenced as a comparison baseline in current (2026) survey literature reviewing digital-phenotyping platforms. Development stopped in January 2019 and the maintainer declared the app archived in December 2023, so it is not comparable to Beiwe, RADAR-base, mindLAMP, or AWARE as a live option, and its Android-only nature is a significant scope limitation for any modern multi-platform study. **Not given a full profile** because it is archived. A team still considering it should contact the maintainer, who asks would-be users to e-mail him (issue 282); CBITS publishes no Purple Robot program, service or support offer, and its current site lists the personal sensing work only under completed projects. Sources 10, 11.

**Correction (2026-10-22):** `phidatalab.org` is the King's College London Precision Health Informatics Data Lab (NIHR Maudsley BRC), not part of Northwestern and not a CBITS successor. Its former page `phidatalab.org/software__trashed/purple-robot-android-apps/` listed only that lab's own Purple Robot configuration for a "Passive Sleep Monitor" (`KHP-Informatics/slam_sleep_test`), per the Wayback capture of 2021-02-25. Its outages, its 404s and its "software__trashed" slug therefore say nothing about Purple Robot's maintenance. The second and third passes below are kept for provenance, with the claims that rested on that site corrected. Sources 2, 6, 14.

**Second-pass update (2026-08-24):** a direct-fetch attempt on `https://phidatalab.org/`, `/software/` and `/software__trashed/purple-robot-android-apps/` returned HTTP 500 on every path. This was later shown to be an outage of the KCL lab's site (see the correction above), so it is not evidence about Purple Robot. WebSearch corroborated that Purple Robot is still cited in current methods literature (2026) as a historical platform.

**Third-pass update (2026-10-09), status set to unmaintained; superseded 2026-10-22 by the maintainer's statement (Verified).**

- The source repository, `cbitstech/Purple-Robot`, has its last commit on 2016-04-11 ("Dependency updates and cleanups") and its last push on 2017-04-07. It is not formally archived on GitHub and had 43 open issues on 2026-10-22 (the GitHub count includes pull requests; 44 on 2026-10-09). The companion `cbitstech/Purple-Robot-Django` server repo's last commit is 2016-12-27; the `audaciouscode/Purple-Robot-Django` fork's is 2020-06-22. `NU-CBITS/PurpleRobotClient` is archived. Source 12.
- Development did not stop in 2016. It continued in `audaciouscode/Purple-Robot-Android` to v3.0.13, last commit 2019-01-30, target API 28 (Verified, 2026-10-22). Source 12.
- The `cbitstech` README build instructions call for the Android 5.1.1 (API 22) SDK platform, Build-tools 21.1.2 and Gradle 2.2.1, while `Purple Robot/build.gradle` on master sets compileSdkVersion and targetSdkVersion 23 (Android 6.0) and minSdkVersion 10 (corrected 2026-10-10: the app targets API 23, not API 22). Even the 2019 continuation (API 28) predates Android 10 onward and current Play Store target-SDK rules, so a new study would first have to port the app forward. This deployability point is an inference from the build targets, not a documented statement. The prebuilt `Purple Robot.apk` in the cbitstech repository was last changed 2015-11-03.
- Conclusion: archived and not realistically deployable for a new study without significant porting work. The 2026-10-09 pass rated this Corroborated for want of a retirement statement; the maintainer's 2023-12-20 statement makes it Verified. Sources 5, 10, 12.

- Licence: GPL v3 or any later version (`LICENSE.GPLv3` in the `cbitstech` repository root, a short notice rather than the full licence text). The notice also offers other licensing options by contacting Mark Begale at Northwestern; that contact dates from 2015 and was not confirmed as current. `audaciouscode/Purple-Robot-Android` and the Django server app are GPL v3. No fees (Verified, 2026-10-22; other-licensing route Corroborated). Source 15.
- Hosting: self-hosting only. The app POSTs JSON payloads, with store-and-forward retry, to an endpoint the research team runs, either the Purple-Robot-Django app (pins Django 1.6, long out of support) or a documented CherryPy starter server. No managed hosting exists (Verified, 2026-10-22). Source 16.
- Identifiers: the user identifier (by default the Google account) is sent as an unsalted MD5 hash, and phone numbers in communication data are always MD5-hashed; later builds let the researcher pick SHA-256 for the identifier. On-device storage uses AES. Unsalted hashes of emails or phone numbers are pseudonymous, not anonymous, despite the CBITS paper's "anonymizes" wording (Verified, 2026-10-22). Source 16.
- Compliance: no HIPAA or GDPR statement anywhere checked (not public, 2026-10-22); the privacy note makes each research site responsible. No FDA clearance found in openFDA (2026-10-22). No vendor receives study data, so BAA, DPA, SOC 2 and ISO 27001 do not apply.

Key link: https://github.com/cbitstech/Purple-Robot (the former phidatalab.org page, https://phidatalab.org/software__trashed/purple-robot-android-apps/, belonged to King's College London's Passive Sleep Monitor configuration, not to Purple Robot's developers; see the correction above).

## Vendor Fact Record

### Purple Robot

<!-- facts:begin purple-robot -->
<!-- facts:end -->

## StudentLife

| Field | Details |
|---|---|
| Organization | Dartmouth College (Andrew Campbell's group) |
| Status | **Historical research study and its resulting open dataset, not a reusable platform for new studies.** |

StudentLife was a landmark 2013 to 2014 Dartmouth study (and the Android app built for it) that pioneered smartphone passive-sensing research on student mental health, academic performance, and behavioral trends. Its lasting artifact for the field is the **StudentLife dataset**, which remains widely used in secondary machine-learning and mental-health research (a `studentlife` R/data package exists on Zenodo for handling it). It is included here because it is frequently named alongside Beiwe, AWARE, and Purple Robot in platform-comparison literature, but it should not be confused with an actively deployable platform: it is a historical app tied to one study, whose primary continuing value to new researchers is the **dataset it produced**, not a tool for collecting new data today. Access route: the dataset was distributed from https://studentlife.cs.dartmouth.edu/dataset.html, which refused connections on 2026-10-10 (Unverifiable whether it is still served); the companion `studentlife` R package ("studentlife: Tidy Handling and Navigation of a Valuable Mobile-Health Dataset", Zenodo record 3371922, 2019-08-20, GPL-2.0, open access) is openly available.

## Koa Health

| Field | Details |
|---|---|
| Organization | Koa Health (commercial digital-mental-health company) |
| Status | Active company with an active digital-phenotyping **research program**, but **not clearly a platform other research teams can deploy for their own independent studies.** |

Koa Health publishes substantial digital-phenotyping research (patents, papers on passive-smartphone-data-informed CBT, encrypted-network-traffic behavioral signals, and more) and explicitly describes digital phenotyping as core to its work. However, this session found no evidence of a publicly documented, externally deployable "Koa Health platform" comparable to Beiwe or Avicenna Research, its digital-phenotyping capability appears to be internal technology supporting its own commercial mental-health products and research collaborations, not a general-purpose research infrastructure product. **Explicitly deferred rather than profiled**, pending direct confirmation from Koa Health about whether any component is available to outside research teams.

**Second-pass update (2026-08-24):** direct fetch of https://www.koahealth.com/research confirms the site's own language frames digital phenotyping strictly as an internal method, "We use digital footprints, ethically acquired from personal devices, to quantify personal characteristics, behaviors, emotions and cognitive states", applied through partnerships with academic groups (London School of Economics, Universitat Pompeu Fabra) rather than offered as a product. **The page contains no mention of a deployable platform, SDK, API, or any mechanism for an outside research team to use Koa Health's technology on their own study**, the absence is itself informative, not just an unread gap. This upgrades the exclusion rationale from Reported/inferred to **Corroborated by direct primary-source absence**: nothing on Koa Health's own research page describes external platform availability. It remains short of fully Verified/resolved because the only way to rule out an unlisted partnership-only or enterprise-only offering is direct vendor contact (their consultation-booking flow), which this session did not initiate, that step still requires the user's decision to reach out, per this knowledge base's rule against fabricating vendor confirmations.

**Re-checked 2026-10-10:** the research page's partner links point to the London School of Economics, Universitat Pompeu Fabra (Center for Brain and Cognition) and Birmingham and Solihull Mental Health NHS Foundation Trust (bsmhft.nhs.uk). Still no outside-researcher programme, platform, SDK or API. Whether an unlisted partnership offering exists was not ruled out and is not being pursued.

## PhoneStudy / other named-but-unverified candidates

CLAUDE.md's onboarding prompt for this module named several additional candidates for discovery: **PhoneStudy**, **Insight (Koa Health)**, and other StudentLife-derived or LAMP-adjacent tools. This session's searches surfaced Koa Health (above) but did **not** turn up a distinct, independently notable "PhoneStudy" platform separate from general academic phone-sensing research use of that generic term, nor any further LAMP-adjacent forks beyond what is already covered in `mindlamp.md`. These are recorded as **not found / not verified** rather than silently dropped, per CLAUDE.md's instruction to record uncertain inclusion decisions.

## Samsung Health Research Stack, cross-reference note

Samsung's Health Research Stack (open-source SDK + backend + web portal for wearable/phone health research) is already profiled in **Module 1** (`../../module-01-wearables/profiles/samsung.md`) because its primary identity in this knowledge base is as a wearable-ecosystem research access route. It has some digital-phenotyping-adjacent characteristics (a self-hosted open-source research backend), and a team building a passive-sensing study around Samsung devices specifically should consult that Module 1 profile alongside this module rather than expect a duplicate entry here. Status note (2026-10-10, GitHub API): all five S-HealthStack repositories were last pushed between 2024-08-20 and 2024-10-24, and the newest backend-system commit is the "Release v2.0-beta" commit (author date 2024-09-27), so the stack has had no public activity for about two years; confirm maintenance with Samsung before building on it.

---

## Sources

1. Search-summary characterization of Purple Robot via digital-phenotyping platform survey literature (accessed 2026-08-24), including "Sensing Apps and Public Data Sets for Digital Phenotyping of Mental Health: Systematic Review," PMC. https://pmc.ncbi.nlm.nih.gov/articles/PMC8895287/
2. King's College London Precision Health Informatics Data Lab (NIHR Maudsley BRC), "Purple Robot Android Apps" page. https://phidatalab.org/software__trashed/purple-robot-android-apps/ (dead link, HTTP 404 since 2026-10-09; accessed 2026-08-24, first pass; HTTP 500 across the whole domain on the 2026-08-24 second pass). A KCL page about that lab's own Purple Robot configuration, not a page of Purple Robot's developers; corrected 2026-10-22, see source 14.
3. `studentlife` R package on Zenodo. https://zenodo.org/records/3371922 (accessed 2026-08-24, search summary). Establishes the dataset's continuing secondary-research use.
4. Koa Health, Research page and complete research-papers listing. https://www.koahealth.com/research ; https://koahealth.com/legal/complete-research-papers/ (accessed 2026-08-24, search summary first pass; **https://www.koahealth.com/research direct-fetched 2026-08-24 second pass, Primary/Corroborated**, confirmed no platform-availability language present on the page).
5. `cbitstech/Purple-Robot` repository, README and commit history via the GitHub API. https://github.com/cbitstech/Purple-Robot (accessed 2026-10-09). **Primary/Direct.** Last commit 2016-04-11, last push 2017-04-07, Android 5.1 build target.
6. King's College London Precision Health Informatics Data Lab site re-check. https://phidatalab.org/ (accessed 2026-10-09). **Direct.** Root HTTP 200; the former Purple Robot page and `/software/` HTTP 404; site search for "purple robot" returns nothing. Not a CBITS site, so not evidence about Purple Robot's status (corrected 2026-10-22).
7. `cbitstech/Purple-Robot` README, `Purple Robot/build.gradle` and repository root listing (accessed 2026-10-10). **Primary/Verified.** API 22 SDK in the README build instructions; compile and target SDK 23 in build.gradle; LICENSE.GPLv3 (GPL v3 or later, see source 15).
8. Zenodo record 3371922 via the Zenodo API (accessed 2026-10-10). **Primary/Verified.** `studentlife` R package, 2019-08-20, GPL-2.0, open access. StudentLife dataset page refused connections the same day.
9. GitHub API, S-HealthStack organization repositories and backend-system commits (accessed 2026-10-10). **Primary/Verified.**
10. `cbitstech/Purple-Robot` issue 282, maintainer comment of 2023-12-20 ("This app is currently archived and no longer being currently developed"; "If you're looking for a replacement, e-mail me"). https://github.com/cbitstech/Purple-Robot/issues/282 (accessed 2026-10-22). **Primary/Verified.** Commenter audaciouscode (profile name Chris Karr, Audacious Software), marked COLLABORATOR. Fact record field program_status.
11. CBITS completed research projects page. https://cbits.northwestern.edu/our-research/our-research-projects/completed-projects.html ; `cbitstech/Purple-Robot` README, https://github.com/cbitstech/Purple-Robot (accessed 2026-10-22). **Primary/Corroborated.** Personal sensing listed as completed; no Purple Robot program or support offer. Fact record field research_program.
12. GitHub commits API for `cbitstech/Purple-Robot` (2016-04-11), `audaciouscode/Purple-Robot-Android` (2019-01-30, v3.0.13, `app/build.gradle` targetSdkVersion 28), `cbitstech/Purple-Robot-Django` (2016-12-27) and `audaciouscode/Purple-Robot-Django` (2020-06-22). https://api.github.com/repos/audaciouscode/Purple-Robot-Android/commits?per_page=1 and https://github.com/audaciouscode/Purple-Robot-Android (accessed 2026-10-22). **Primary/Verified.** Fact record field deprecations.
13. Google Play listing `edu.northwestern.cbits.purple_robot_manager`, HTTP 404. https://play.google.com/store/apps/details?id=edu.northwestern.cbits.purple_robot_manager (accessed 2026-10-22). **Direct.** Fact record field app_availability.
14. Wayback Machine capture of the phidatalab.org Purple Robot page, 2021-02-25. https://web.archive.org/web/20210225233643/https://phidatalab.org/software__trashed/purple-robot-android-apps/ (accessed 2026-10-22). **Direct.** Shows a KCL "Passive Sleep Monitor" configuration (`KHP-Informatics/slam_sleep_test`). Fact record field research_program (note).
15. `cbitstech/Purple-Robot` `LICENSE.GPLv3` notice. https://github.com/cbitstech/Purple-Robot/blob/master/LICENSE.GPLv3 (accessed 2026-10-22). **Primary/Verified.** "either version 3 of the License, or" any later version; other licensing options by contact. Fact record fields licence, academic_vs_commercial, api_platform_fees.
16. Purple Robot wiki Data Upload Reference, https://github.com/cbitstech/Purple-Robot/wiki/Data-Upload-Reference ; `cbitstech/Purple-Robot-Django`, https://github.com/cbitstech/Purple-Robot-Django ; `EncryptionManager.java` and `PRIVACY.md` in https://github.com/audaciouscode/Purple-Robot-Android (accessed 2026-10-22). **Primary/Verified.** Self-hosted upload endpoint, MD5 identifier hash, AES storage, site-level privacy responsibility. Fact record fields hosting_options, export_routes, retention_terms, hipaa_statement.
