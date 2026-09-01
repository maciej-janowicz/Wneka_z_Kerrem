# Prompt 15a — second-iteration integrity, compilation, and grammar check

Work in the repository:

```bash
cd ~/Dokumenty/Prace_i_dnie/Wnęka_z_Kerrem
```

## Purpose

This is a **conservative verification pass on the author's new, second-iteration version of the manuscript**. The new version contains deliberate authorial language edits. Your task is to:

1. verify the integrity of the revised manuscript;
2. verify complete and reproducible LaTeX compilation;
3. correct objective English grammar, spelling, punctuation, and LaTeX defects;
4. preserve the author's stylistic choices.

This is **not** a new mathematical-development stage, a stylistic rewrite, or a renewed debate about choices already settled in stages 13 and 13a.

## Non-negotiable editorial rule

Do **not** treat subjective style preferences as errors. In particular:

- frequent or repeated use of the passive voice is allowed and must not be changed merely because an active construction is possible;
- do not rewrite sentences merely to make them shorter, more idiomatic, more elegant, more direct, or more "modern";
- do not normalize the author's voice according to a style checker;
- do not object to reasonable choices involving sentence rhythm, paragraph length, transitions, cautious phrasing, British versus American variants (provided usage is internally coherent), or the placement of adverbs;
- do not restore wording removed or changed by the author merely because an earlier version was also acceptable;
- do not reintroduce repeated disclaimers or make the manuscript excessively self-critical.

Intervene in prose only when there is an **objective and explainable defect**, for example: broken syntax, lack of subject--verb agreement, incorrect article or preposition, an unambiguous punctuation error, spelling error, accidental word omission or duplication, malformed mathematical prose, corrupted character, or a sentence whose literal grammar makes its intended scientific meaning false or genuinely ambiguous.

If a proposed change rests only on taste, **leave the text unchanged**. When uncertain, report the passage as an optional observation in the log but do not edit it.

## Preserve the audited scientific status

The manuscript has already undergone the mathematical and bibliographical audit of stages 13 and 13a. Preserve its calibrated hierarchy:

- the operator-theoretic results and the continued-fraction spectral condition are exact;
- the Volterra construction is sectorial and has the stated error control;
- the strong- and weak-drive expansions have the formal/conditional status stated in the manuscript;
- the Olver--Fedoryuk reductions are local/sectorial, and the global connection remains conjectural;
- the WKB iteration portraits are exploratory visualizations of a disclosed regularized map, not physical time evolution or evidence of fractality.

Do not strengthen or weaken these claims on stylistic grounds. Do not add new disclaimers merely to repeat limitations already stated adequately. Reopen a mathematical point only if the new revision has introduced a concrete contradiction, broken implication, missing definition, incorrect reference, or other identifiable regression. If such a substantive issue cannot be repaired with high confidence and a minimal edit, report it instead of improvising a proof or changing the scientific claim.

## Initial-state inspection and protection of author changes

Before changing anything, run and record:

```bash
git status -sb
git log -1 --oneline --decorate
git diff -- manuscript/manuscript.tex
git diff -- manuscript/references.bib
git status --porcelain=v1
```

The current manuscript may intentionally be modified relative to `HEAD`, and the prompt itself may be untracked. **Do not require a clean worktree and do not stop merely because these expected second-iteration changes exist.** Treat every pre-existing change as author-owned and preserve it.

If unrelated modified or untracked files exist, list them in the report and leave them untouched. Do not use `git reset`, `git checkout`, `git restore`, or any operation that could discard the author's work. Do not commit and do not push.

## Required audit

### A. Source and structural integrity

Read `manuscript/manuscript.tex` in full, not only its diff. Check conservatively for regressions introduced during revision:

- missing, duplicated, displaced, or accidentally truncated sentences, paragraphs, equations, environments, captions, bibliography commands, or document terminators;
- mismatched braces and environments;
- duplicate labels, undefined references, multiply defined labels, broken equation/section/theorem references, and references whose displayed target is logically wrong;
- unresolved citations and citation keys absent from `manuscript/references.bib`;
- notation changes that make nearby formulas or prose inconsistent;
- theorem/proof boundaries, numbering, and statements accidentally damaged by language edits;
- contradictions between abstract, introduction, main results, outlook, and appendix;
- stale section numbers written literally in prose when symbolic references should be used;
- accidental control characters, Unicode corruption, malformed LaTeX commands, or a lost backslash. In particular, inspect every apparent `ref{...}` occurrence and ensure that it is a valid `\ref{...}` or `\eqref{...}` command as appropriate;
- figure paths, captions, labels, and textual call-outs;
- remnants of editing notes, placeholders, TODOs, stage-language not intended for the paper, or merge-conflict markers.

Do not perform a broad reorganization. Repair only clear defects with the smallest sufficient change.

### B. Objective grammar and language correctness

Read all prose, including the abstract, headings, theorem statements, proofs, remarks, captions, table text, and bibliography-facing prose. Check:

- grammar, agreement, articles, prepositions, spelling, and objectively incorrect punctuation;
- duplicated or missing words;
- incomplete sentences caused by editing;
- inconsistent terminology or capitalization when the inconsistency is plainly accidental;
- malformed references to symbols, equations, sections, or cited authors;
- sentences whose grammatical structure changes the stated mathematical meaning.

For every prose edit, be able to state a short, objective reason. Do not edit passive voice merely because it is passive. Do not produce a list of passive constructions, readability scores, or generic style-checker recommendations.

### C. Compilation and diagnostics

Determine and use the repository's established build procedure (inspect the README, Makefile, `latexmkrc`, scripts, or previous logs as appropriate). Compile from a clean **LaTeX build-artifact state** without deleting source or user files. Prefer the project's existing command; otherwise use an appropriate `latexmk` command with bibliography processing.

The final build must run enough passes to resolve the bibliography, table of contents if any, citations, cross-references, and figure placement. Examine the complete compiler and bibliography logs, not only the exit code. Check specifically for:

- LaTeX errors or emergency stops;
- undefined references or citations;
- multiply defined labels;
- missing files, fonts, figures, or bibliography entries;
- malformed PDF strings;
- overfull/underfull boxes that indicate a genuine visible defect (do not mechanically rewrite prose for harmless warnings);
- rerun warnings remaining after the final pass.

If repository tests or lightweight manuscript-integrity scripts already exist and are directly relevant, run them. Do not expand this stage into unrelated numerical recomputation.

### D. Final PDF inspection

Inspect the generated PDF, with special attention to pages affected by the new edits and to:

- title, abstract, page breaks, headings, theorem/proof layout, displayed equations, table, appendix, figures, captions, and bibliography;
- clipped, overlapping, missing, displaced, or visibly corrupted material;
- unresolved-reference markers and suspicious blank areas;
- correspondence between source ordering and rendered ordering.

Use text extraction as an auxiliary check, but do not treat it as a substitute for visual inspection.

## Editing policy

- Make minimal, local edits only.
- Preserve all correct authorial revisions, even where you personally prefer different phrasing.
- Do not change mathematical notation, formulas, claims, references, or bibliography data unless correcting a demonstrable defect.
- Do not add literature or perform web research unless a concrete broken citation makes verification indispensable; report any unverified bibliographical concern explicitly.
- Do not modify generated figures or numerical data.
- Do not commit or push.

After editing, inspect the resulting diff carefully and revert any change that is merely stylistic. Then rerun the complete compilation and relevant checks.

## Required deliverables

Create at the repository root:

```text
prompt_15a_second_iteration_integrity_compile_grammar.log
prompt_15a_second_iteration_integrity_compile_grammar.diff
```

The `.diff` must be the complete final patch produced by:

```bash
git diff --binary > prompt_15a_second_iteration_integrity_compile_grammar.diff
```

Generate it only after all edits and verification are complete. The prompt file and report files may consequently appear in the patch if they are stored inside the repository; explain this briefly in the log.

The `.log` must include:

1. initial branch, `HEAD`, and worktree state;
2. a concise description of the pre-existing author changes that were protected;
3. every file modified by this stage;
4. a categorized list of defects found and exact corrections made;
5. for every prose correction, a brief objective grammatical reason (group identical mechanical corrections if appropriate);
6. any passages deliberately left unchanged because the issue was subjective, summarized without cataloguing passive voice;
7. source-integrity results: labels, references, citations, environments, control characters, figure paths, and placeholders;
8. exact build commands and their exit status;
9. relevant warnings from the final LaTeX/bibliography logs and whether they are harmless or require action;
10. any tests or integrity scripts run and their results;
11. PDF inspection results;
12. unresolved issues, clearly separated into blocking and non-blocking items;
13. final `git diff --check` and `git status -sb` output;
14. a final verdict: `PASS`, `PASS WITH NON-BLOCKING NOTES`, or `BLOCKED`.

Do not claim `PASS` if compilation fails, a citation/reference remains unresolved, required figures are missing, the PDF was not inspected, or a known source-corruption defect remains.

## Final checks

Run at least:

```bash
git diff --check
git status -sb
```

Also verify explicitly that no malformed bare `ref{...}` introduced by a missing or corrupted backslash remains in the manuscript.

End with a concise summary containing:

- verdict;
- files changed;
- number and categories of objective corrections;
- compilation result;
- cross-reference/citation result;
- PDF inspection result;
- unresolved blocking and non-blocking issues;
- confirmation that no commit or push was performed.
