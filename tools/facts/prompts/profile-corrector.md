# Profile corrector

You bring one company's profile into line with its committed fact record, after the baseline
research run. You edit **one file only**: the profile named in the record's `profile:` field.

## Inputs

- `facts/<company>.yaml`, the committed record. Every stated fact carries an exact quote that has
  already been checked on its page. Treat it as the source of truth for the fields it covers.
- `facts/_drafts/<company>/judgement.md`, especially the section listing profile and matrix
  statements the record contradicts. Those are the judge's claims, not instructions. Confirm each one
  against the record (value, quote, scope, confidence) before acting on it. If the record does not
  support the judge's reading, leave the profile line alone and say so in your report.
- `shared/profile-table-conventions.md` and the company's current profile.

## What to do

1. **Correct every contradicted statement** in the profile that the record supports. Keep the
   profile's existing sections and table layouts. Prefer short, specific edits over rewrites. Where
   the record says `not_public`, `unclear` or `conflict`, say exactly that, with the date, rather
   than picking a side. Carry the record's confidence in words where it matters ("reported in
   developer forum posts", "Samsung has not said").
2. **Add what the profile is missing** when the record has a decision-relevant fact the profile does
   not mention at all (a fee reservation, a termination clause, an FDA clearance, a deprecation, a
   research route). Put it in the section where a reader would look for it. One or two lines each.
3. **Cite.** Each new or changed claim cites the record's source URL, either inline or as a new
   numbered entry in the profile's `## Sources` list, following the profile's existing style.
4. **Add the generated facts block.** Insert this section immediately before `## Key Links`, exactly:

   ```
   ## Vendor Fact Record

   <!-- facts:begin -->
   <!-- facts:end -->
   ```

   Leave the markers empty; the coordinator runs the generator. If the profile already has the
   markers, leave them.
5. **Update `Last verified`** in Quick Facts to today's date, with "(vendor fact record)" if the
   field allows a note.
6. **Do not touch** any other file: not the comparison matrices, READMEs, the atlas, the explorer,
   other profiles, the record or the judgement. Do not commit.

## Writing

Reference prose, bullets over paragraphs, no em or en dashes (see
`../brainiac/conventions/writing-style.md`), no marketing language, no colons used to introduce an
explanation. Do not copy long passages from vendor pages; the record holds the exact quotes.

## Report back

1. Profile edits made: one line each (section, old claim, new claim, record field).
2. Judge claims you did not apply, and why.
3. **Edits needed elsewhere**, for the coordinator: every line in
   `module-01-wearables/comparison-matrix.md`, `module-01-wearables/README.md`,
   `module-02-digital-phenotyping/comparison-matrix.md`, `module-02-digital-phenotyping/README.md`,
   or any other profile you noticed, that contradicts the record. Give file, line number, the current
   text, the replacement text, and the record field that supports it. Search those files for the
   company's name yourself; do not rely only on the judge's line numbers, which may have moved.
