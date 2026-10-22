# Purple Robot (Northwestern CBITS): judgement, 2026-10-22

This was the cheaper variant: one researcher draft (`A.yaml`), no B and no gap hunter. I audited A instead of comparing two drafts. Inputs were `A.yaml` and the starter `facts/purple-robot.yaml` (all fields `unresearched`). The output is `facts/purple-robot.yaml` with 34 entries: 15 stated, 3 not_public, 16 not_applicable, 0 conflict, 0 unclear. It watches 14 pages.

- Quote check: all 61 quotes matched "exact" with `quote_probe.py` on 2026-10-22. One PMC quote failed once on a transient fetch and matched on retry.
- `validate.py --file facts/purple-robot.yaml`: 0 errors and 0 fields unresearched.
- `weekly.py --only purple-robot --no-state`: 32 pages checked. 0 quotes missing, 0 reworded, 0 dead links.

## Audit of A: what I changed and why

I opened the source for every stated fact. All 47 of A's quotes were exact and on the cited page. The changes below are about substance.

| Field | A | Final | Reason |
|---|---|---|---|
| academic_vs_commercial | not_applicable ("same GPL v3 terms for everyone") | **stated**, Corroborated | A missed the end of the cbitstech `LICENSE.GPLv3` notice: "Please contact Mark Begale at m-begale@northwestern.edu to discuss other licensing options as needed." That is a dual-licensing route, so the field has an answer. Corroborated, because the contact is from 2015 and I have not confirmed it is still current. |
| licence | "GPL v3", quote "GNU GENERAL PUBLIC LICENSE" | GPL v3 **or later**, plus the other-licensing offer | `LICENSE.GPLv3` is a 932-byte licence notice, not the GPL text. It says "either version 3 of the License, or (at your option) any later version". I replaced the quote with that wording. The same quote fix went into api_platform_fees. |
| hosting_price | not_public, Corroborated | **not_applicable** | hosting_options says no managed hosting exists, and nothing contradicts that. A missing price for a service that does not exist is not_applicable. AWARE was different: it has a hosting service with no published price, so not_public fit there. The pages checked are listed in the note. |
| history_depth | not_applicable | **stated**, Corroborated | This follows the AWARE precedent, where "no vendor-held copy, the phone holds data only until upload" counted as an answer. Sources are the Data Upload Reference retry quote and the Saeb 2015 deletion quote. |
| retention_terms | MD5 claim supported by the paper alone; value said "anonymised" | MD5 claim checked three ways; "anonymised" corrected | See point 3 below. Six quotes were added from the upload doc, `EncryptionManager.java` and `arrays.xml`. Confidence stays Verified. |
| raw_streams | Probe list in the value | Value completed | The GitHub API listing of `probes/builtin` also includes activity detection, humidity, linear acceleration, significant motion, NFC, network, address-book distances, calendar and wake-lock probes. A left all of these out. |
| app_availability | Prebuilt APK "from 2016", "build against API 22" | APK last committed 2015-11-03; targets API 23 on cbitstech master and API 28 on the audaciouscode continuation | The GitHub commits API for `Purple Robot.apk` gives 2015-11-03. `Purple Robot/build.gradle` sets targetSdkVersion 23. Only the README's SDK-install step mentions API 22. Added the build.gradle quote. |
| deprecations | Last commits for three repos | Adds cbitstech/Purple-Robot-Django, last commit 2016-12-27 | A cited only the audaciouscode Django repo. The GitHub API shows that repo is a fork of cbitstech/Purple-Robot-Django. The original is the one the README points to, and the profile cites it. |
| program_status | Verified, maintainer named as Chris Karr | Kept. The note now gives the evidence for the name and role | `api.github.com/users/audaciouscode` gives the name Chris Karr and the company Audacious Software. The issue-282 comments API marks him COLLABORATOR on the repository. |
| research_program | Note says phidatalab.org is unrelated | Kept, with a firmer note | See point 2. |
| fda_clearances | Note mentions PMA searches by applicant | Kept. Applicant PMA searches re-run | I re-ran all seven openFDA queries. Every one returned `"No matches found!"`. |
| watch | 13 pages | 14 pages | Added the cbitstech/Purple-Robot-Django commits API as a changelog. |

### Spot checks of not_applicable and not_public (kept)

- **program_eligibility, program_application, developer_program_status, user_cap:** no program exists. The source and build instructions are public. Kept as not_applicable.
- **device_price, subscription_price, academic_pricing, minimum_commitment, quote_required, rate_limits, ai_training_terms:** this is self-run open-source software with nothing for sale and no hosted API. Kept as not_applicable. For quote_required I checked audacious-software.com: it lists general services with no Purple Robot offer, and `/services/` returns 404.
- **baa, dpa, iso27001, soc2:** not_applicable, because no vendor receives or processes study data. Other platform records (AWARE, Beiwe) use not_public for these fields, but each of those has a hosted service that could be certified or sign an agreement. Purple Robot has none. Flagged below in case the coordinator wants these fields uniform across records.
- **hipaa_statement, gdpr_statement:** not_public. PRIVACY.md, the README, the wiki and the Django README contain no HIPAA or GDPR text. Kept.
- **fda_clearances:** not_public, Verified, from regulator_db searches that returned no matches. Kept.

### Own gap sweep

- **Licence notice:** found the dual-licensing offer and the "or later" wording, both missed by A. Now in academic_vs_commercial and licence.
- **Hashing details:** found in the Data Upload Reference and the source. Now in retention_terms (point 3).
- **Missing probes:** added to raw_streams.
- **Audacious Software homepage:** it describes Passive Data Kit as the developer's newer framework. Nothing ties it to Purple Robot as an official successor, and issue 282 does not name it, so I left it out of the record. A coordinator could ask the maintainer.
- **Open issues:** the GitHub API reports 43 open issues for cbitstech/Purple-Robot. The profile says 44. This count includes PRs and is minor.
- **Issue 282 state:** the issue itself is closed, and its last activity is housekeeping. No newer maintainer statement exists.

## Points the coordinator asked me to verify

1. **The 2023-12-20 "archived" statement versus GitHub's archive flag.** Confirmed through the issue and comments API. bartkamphorst opened issue 282 on 2022-12-13 and pinged audaciouscode on 2023-12-20. audaciouscode (Chris Karr, COLLABORATOR) replied the same day at 13:04 UTC: "This app is currently archived and no longer being currently developed." The GitHub API on 2026-10-22 reports `archived: false` for cbitstech/Purple-Robot, cbitstech/Purple-Robot-Django, audaciouscode/Purple-Robot-Android and audaciouscode/Purple-Robot-Django. It reports `true` only for NU-CBITS/PurpleRobotClient. The two signals do not conflict: "archived" is the developer's plain-English word for the project, not the GitHub setting. Recorded as stated, Verified, under program_status and deprecations, with the distinction in the notes.
2. **phidatalab.org.** Confirmed as the King's College London Precision Health Informatics Data Lab ("Bioinformatics and Biostatistics at the NIHR Maudsley BRC"). It was never part of CBITS. A site search for "purple robot" returns "Nothing found". The Wayback Machine has the old page `phidatalab.org/software__trashed/purple-robot-android-apps/` (capture 2021-02-25). It listed only the KCL lab's own Purple Robot configuration for a "Passive Sleep Monitor" (repo KHP-Informatics/slam_sleep_test, plus an .scm config file). So the "software__trashed" slug is KCL tidying its own WordPress site. It is not a signal that Purple Robot was retired. Contradictions are listed below.
3. **The MD5 claim.** Confirmed, and A's draft understated it. It is supported three ways:
   - Saeb et al. 2015, written by the developers: "using standard MD5 hashing and advanced encryption standard".
   - The Data Upload Reference: the UserHash "is an MD5 hash of the user identifier set in the app's settings", which "defaults to your Google account if not set explicitly". The payload checksum is also MD5.
   - The v3.0.13 source (`EncryptionManager.java`): the identifier hash defaults to `"MD5"` through `config_preferred_hash_function`, and `arrays.xml` labels the options "MD5 (Insecure, Legacy Default)" and "SHA-2 (Secure, Recommended)". `normalizedPhoneHash` always uses MD5 on a normalised 10-digit phone number. Local encryption is AES/CBC/PKCS5Padding.

   An unsalted MD5 hash of an email address or phone number is pseudonymisation, not anonymisation, because it can be reversed by dictionary attack. The note says so, and the value no longer says "anonymised".

## Profile and matrix statements the record contradicts

| File | Line | What it says | What the record says |
|---|---|---|---|
| `module-02-digital-phenotyping/profiles/legacy-and-adjacent-platforms.md` | 11 | Organization: "CBITS / Precision Health Informatics Data Lab, Northwestern University" | The PHI Data Lab (phidatalab.org) is at King's College London and the NIHR Maudsley BRC. It is not part of Northwestern. CBITS built Purple Robot, and its developer Chris Karr (Audacious Software) maintained it last (research_program, program_status). |
| same | 12 | "Legacy, unmaintained since 2016 (Corroborated)" | cbitstech master stopped in 2016, but development continued in audaciouscode/Purple-Robot-Android to v3.0.13 (2019-01-30, target API 28). The Django fork's last commit was 2020-06-22. The maintainer declared the app archived on 2023-12-20 (deprecations, program_status: Verified). |
| same | 15 | CBITS is "now folded into the Precision Health Informatics Data Lab"; teams should "confirm with the Precision Health Informatics Data Lab" | No such merger. The right contact is the maintainer, who asks to be e-mailed at the address in issue 282 (program_status). |
| same | 17 | Second-pass update treats phidatalab.org outages as evidence about Purple Robot's maintenance | That site belongs to an unrelated KCL lab. Its uptime says nothing about Purple Robot (research_program note). |
| same | 23, 28 | The lab's "Purple Robot page" returning 404, and "its 'software__trashed' slug was a retirement signal" | The page was KCL's own Passive Sleep Monitor configuration built on Purple Robot (Wayback, 2021-02-25). The slug reflects KCL's site clean-up, not a Purple Robot retirement (research_program note). |
| same | 24 | "No statement of retirement from the lab was found, which is why this is Corroborated rather than Verified" | The developer's statement now exists: "This app is currently archived and no longer being currently developed" (issue 282, 2023-12-20). program_status and deprecations are Verified. |
| same | 21 | "44 open issues" | The GitHub API reports 43 on 2026-10-22. Minor, and the count includes PRs. |
| same | 22 | The API 22 SDK in the README, API 23 in build.gradle | Consistent with the record. The record adds that the later audaciouscode code targets API 28 (deprecations, app_availability). |
| same | 26 | "Licence: GPL-3.0" | GPL v3 or any later version, with other licensing offered by contact (licence, academic_vs_commercial). |
| same | 65, 69 | Sources 2 and 6 attribute the phidatalab.org pages to Purple Robot's own lab | Same correction as line 11. |
| `module-02-digital-phenotyping/comparison-matrix.md` | 43 | "Northwestern CBITS / PHI Data Lab"; "Dormant since 2016 ... lab page removed (Corroborated)"; "GPL-3.0" | CBITS only; development ended in 2019, with a developer statement of archive in 2023 (Verified); the "lab page" was KCL's; GPL v3 or later. |
| same | 62 | "Not maintained since 2016" | Last Android code 2019-01-30; archived per the maintainer 2023-12-20. |
| same | 241 | "Purple Robot unmaintained since 2016" | As above. |
| `module-02-digital-phenotyping/README.md` | 64 | "unmaintained since 2016" | As above. |
| `shared/unresolved-questions.md` | 398 (Q92) | Names the Precision Health Informatics Data Lab as the organisation that could answer, and says "The lab never states it retired the app." | The answering party is the maintainer (issue 282). His retirement statement exists. |

## For the coordinator to check by hand

- **Compliance fields:** baa, dpa, iso27001 and soc2 are not_applicable here but not_public in records for platforms that run a hosted service. Decide whether you want the two cases treated differently or the status made uniform.
- **Licensing contact:** the alternative-licensing contact (Mark Begale, 2015) may no longer be at Northwestern. I did not contact anyone.
- **Passive Data Kit:** only the maintainer can confirm whether it is the "replacement" he refers to.
- **Wayback citation:** the profile corrections in the table above rely on a Wayback capture that is not cited in the record, since the record cites only live pages. If the profile is edited, cite `web.archive.org/web/20210225233643/https://phidatalab.org/software__trashed/purple-robot-android-apps/`.
