# Prompt 18a — JMP declarations, appendix order and data availability

Work in `~/Dokumenty/Prace_i_dnie/Wnęka_z_Kerrem`. This is a focused follow-up to the audit in prompt 18, not another full mathematical review. Read `prompt_18_jmp_prefinal_audit_and_dedication.log` and inspect the current canonical `manuscript/manuscript.tex`, `manuscript/manuscript.bib`, and final PDF before editing. Preserve the dedication exactly as printed: “To the memory of my Mother.” Preserve the existing AI-assistance acknowledgment. Do not edit the submitted `arxiv/` package.

## Established author facts

- There is one author, Maciej Janowicz, who takes responsibility for the whole work.
- His affiliation, supplied by him verbatim, is: `Katedra Zastosowań Matematyki, Instytut Informatyki Technicznej, Szkoła Główna Gospodarstwa Wiejskiego, ul. Nowoursynowska 166, 02-787 Warszawa, Poland`.
- The author confirms `maciej_janowicz@sggw.edu.pl` as his official corresponding-author email. Include it in the front matter and verify its rendering.
- The author declares no conflicts of interest. Insert the AIP-compatible statement: `The author has no conflicts to disclose.`
- For CRediT, use this author-approved list, with the journal's appropriate formatting: `Maciej Janowicz: Conceptualization, Methodology, Formal analysis, Investigation, Software, Validation, Visualization, Writing – original draft, Writing – review and editing.` The acknowledgment records the tools' assistance separately; do not list AI as an author or imply that it assumes responsibility.
- The author prefers a public GitHub repository for data/code availability if it actually contains the necessary materials. Find and verify the correct repository yourself. Do not invent a URL, DOI, funding source, ORCID, or email.

Use the affiliation exactly as supplied, including its Polish institutional names and address; do not translate the names without a verified institutional English form and the author's approval. Typeset Polish characters correctly. Use the author-confirmed email above; do not substitute a Git `user.email` or a commit author's address.

Funding has not been confirmed. Inspect existing acknowledgments and records for an explicit funding statement; do not infer “no funding” from silence. Report the exact missing author decision if still unknown.

## Initial-state safety

Record `pwd`, `git status -sb`, `git log -1 --oneline --decorate`, `git status --porcelain=v1`, and `git diff --binary` before edits. The prompt-18 dedication may be an uncommitted change; treat it and all other tracked/untracked files as author-owned. Do not require a clean tree, reset the index, or overwrite the manuscript from a snapshot. Do not commit or push.

## Verify official AIP/JMP requirements

Check the current official [AIP Author Instructions](https://publishing.aip.org/resources/researchers/author-instructions/) and [Research Data Policy](https://publishing.aip.org/resources/researchers/open-science/research-data-policy/), plus the JMP-specific section and the linked accessibility guidance. Record access dates and distinguish mandatory instructions from recommendations. The audit-18 report may contain mistaken conclusions; recheck the actual source/PDF, particularly the following.

### 1. Order, declarations and front matter

Determine the actual order of Outlook/conclusion, Acknowledgment, author declarations, Data Availability, appendix, and References. The AIP order is acknowledgments, author declarations, data availability, appendixes, references. Move the existing Acknowledgment and appendix only if needed, with minimal source movement and no changes to their content. Rebuild and check all references, floats, figure/table numbers and page breaks. Place the author's exact affiliation in the front matter. Add Conflict of Interest and Author Contributions/CRediT in the appropriate location using the confirmed text above.

Do not insert an unverified funding statement or correspondence email. Keep a clear list of any still-missing author facts. Ensure a prospective Data Availability section appears in the correct position **only when its factual statement has been verified**; otherwise do not claim public availability and report the exact blocker. AIP permits an accurate on-request statement for JMP, if public deposition proves unavailable and the author chooses that route; do not choose it on the author's behalf.

### 2. Appendix and table conventions

Inspect actual appendix equation numbers in source and PDF. For the single appendix, make them `(A1), (A2), …` if they currently continue the main-text numbering; use a robust LaTeX counter/reference solution and verify every `\eqref` target. Check that figures and tables in the appendix continue their respective main-text numbering. Identify every `tabular` and `table` environment, including the intervention-rate table: check whether each real table has a caption, a number and a textual citation as required by AIP. If a clear deficiency exists, fix it conservatively without altering numerical entries; add suitable descriptive captions and references, and check the final layout. Do not falsely report “all tables captioned” based only on figure environments.

### 3. Accessible descriptions

Inventory every figure and real table, not merely each included image file. Draft concise, scientifically accurate alt text for each, including multi-panel figures. Follow the current AIP implementation guidance and the capabilities of the actual LaTeX class/submission workflow. Implement alt text in the source or submission-ready companion material if a documented, compatible route is available; do not invent a macro or claim that a caption alone satisfies the requirement. If portal entry or author verification remains necessary, supply a numbered mapping from each figure/table to exact proposed alt text and label the remaining step explicitly.

### 4. Find and verify the GitHub repository

Inspect `git remote -v`, repository documentation, source/figure-generation scripts, metadata and any trustworthy project links. Resolve the canonical GitHub URL and verify that it is publicly accessible; a remote URL or a locally present branch by itself is not proof of public accessibility. Inspect the public repository at the intended release/tag/commit and compare it against the minimal materials necessary to interpret and reproduce the manuscript's numerical figures and checks: code, parameters, inputs or generated data, dependencies, instructions and licensing where relevant. Identify what is present, missing, ignored, private, or uncommitted. Do not expose private files, tokens, or local-only data.

If the public repository is sufficient, add an accurate Data Availability statement naming GitHub, the exact URL and an immutable tag or commit; distinguish data from code where useful. AIP permits a public repository without a DOI, although a DOI-bearing archive is an option. If the public repository is incomplete or unverified, **do not** write that the data/code are publicly available. Provide a concrete minimal file list to add and a proposed statement for later approval. Do not create a GitHub release, publish missing files, or push without explicit authorization.

## Scope and verification

Keep edits limited to the author-supplied affiliation and declarations, order/numbering/caption fixes, and a verified data-availability statement. Do not revisit the mathematical proofs, rewrite the author's prose, convert the entire document to the JMP template, modify scientific figures, or strengthen claims. If a substantive conflict emerges, report it rather than improvising.

Compile the canonical manuscript from a clean generated-artifact state using the established build procedure, including BibTeX and all required reruns. Inspect full compiler and bibliography diagnostics; run `git diff --check`; check references, citations, appendix equation numbers and all affected figure/table references. Render and visually inspect front matter, declarations, appendix/table pages and bibliography. Compare against the prompt-18 PDF for unintended changes.

## Deliverables

Create at repository root:

```text
prompt_18a_jmp_declarations_appendix_data.log
prompt_18a_jmp_declarations_appendix_data.diff
```

The `.log` must include initial/final status, official sources and access date, exact edits with reasons, verified author facts and email, source/PDF order, appendix/table numbering, figure/table alt-text mapping, GitHub discovery and public-content evidence, reproducibility gaps, any funding item still requiring author input, build/test/PDF results, and a verdict: `READY FOR AUTHOR FINAL CHECK`, `READY AFTER SPECIFIED AUTHOR DECISIONS`, or `BLOCKED`. State the remaining decisions precisely; do not convert a missing funding fact into a generic warning.

Generate the full tracked patch at the end with `git diff --binary > prompt_18a_jmp_declarations_appendix_data.diff`. State that this is cumulative from `HEAD` and may include the uncommitted prompt-18 dedication; include a focused list of changes attributable to 18a in the log. Untracked and ignored files do not appear in ordinary Git diff. Do not commit, push, modify `arxiv/`, submit to JMP, or contact the journal.
