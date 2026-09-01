# Prompt 15b — global detuning notation and arXiv-readiness audit

Work in the repository:

```bash
cd ~/Dokumenty/Prace_i_dnie/Wnęka_z_Kerrem
```

## Purpose

This stage has two tightly bounded tasks:

1. replace the detuning symbol `\omega_0` by the Greek capital `\Delta` throughout the manuscript, **without changing any sign, equation, approximation, or scientific result**;
2. determine rigorously whether the resulting manuscript source is ready for submission to arXiv under the current arXiv TeX-submission requirements.

This is a notation migration plus a technical submission audit. It is not a new stylistic rewrite, mathematical-development stage, bibliographical expansion, or authorization to submit anything to arXiv.

## Fixed physical convention — do not reinterpret it

Use everywhere the signed detuning

```tex
\Delta := \omega_c-\omega_d,
```

where `\omega_c` is the bare cavity resonance frequency and `\omega_d` is the drive frequency. Therefore the rotating-frame Hamiltonian remains

```tex
H=\frac{V}{2}a^{\dagger 2}a^2+\hbar\Delta a^\dagger a
  +F a^\dagger+\overline F\,a.
```

Equivalently, its number term is `+\hbar\Delta N`. This is **exactly the old convention** `\omega_0=\omega_c-\omega_d`; only the symbol changes. Do not introduce a minus sign. Do not redefine `\Delta` as `\omega_d-\omega_c`.

State clearly, near the first definition of the model, that:

- the analysis is performed in the frame rotating at the drive frequency `\omega_d`;
- `\Delta=\omega_c-\omega_d` is the signed drive--cavity detuning used in this manuscript;
- sources using the opposite convention `\omega_d-\omega_c` have detuning `-\Delta` relative to ours.

Use concise, neutral English and avoid repeating this convention throughout the paper once it has been defined unambiguously.

## Preserve the accepted 15a work

Stage 15a has already been reviewed and accepted but has not yet been committed. Preserve all its corrections, including:

- the repaired `\ref{sec:sectorial-solutions}` and its label;
- symbolic replacements for stale literal section numbers;
- restored bibliography style/path;
- removal of the unsupported blanket continued-fraction convergence/rate claim;
- `\clearpage` before the bibliography;
- the author's deliberate passive constructions and other subjective wording.

Do not overwrite `manuscript/manuscript.tex` from an older snapshot. Work on the current canonical source containing the accepted 15a changes. Treat all pre-existing modifications and untracked files as user-owned.

## Initial-state inspection

Before any edit, run and record:

```bash
git status -sb
git log -1 --oneline --decorate
git status --porcelain=v1
git diff -- manuscript/manuscript.tex
git diff -- manuscript/references.bib
```

The worktree is expected to be non-clean because stage 15a is uncommitted. Do not stop merely for that reason. Do not use `git reset`, `git checkout`, `git restore`, or any command that could discard existing work. Do not commit and do not push.

## Task A — controlled global notation migration

Read the full canonical manuscript before and after editing. Replace every use of the old model parameter `\omega_0` by `\Delta`, including but not limited to:

- Hamiltonians and differential equations;
- parameter declarations and prose definitions;
- the rotating-frame derivation;
- operator polynomials such as `p(n)`;
- Whittaker--Ince parameter maps;
- Liouville, Olver, Fedoryuk, strong-drive, and weak-drive formulas;
- dimensionless parameters, especially every definition formerly containing `\hbar\omega_0/V`;
- assumptions, denominators, captions, theorem statements, remarks, and explanatory prose.

This must be a semantically controlled replacement, not a blind substitution. Distinguish the model parameter formerly denoted `\omega_0` from genuinely different frequencies, such as `\omega_c`, `\omega_d`, an auxiliary special-function parameter `\omega`, or frequencies appearing inside bibliographical titles. Do not alter any of those.

Retain existing dimensionless symbols such as `\delta` where they are already used; only update their definitions and all prose interpreting them. For example, if the manuscript currently defines

```tex
\delta=\frac{\hbar\omega_0}{V},
```

it must become

```tex
\delta=\frac{\hbar\Delta}{V}.
```

Do not replace the lowercase `\delta` by uppercase `\Delta` where `\delta` is an independently defined dimensionless parameter.

After editing, verify with token-aware searches that no occurrence of the old parameter remains. Search at least for:

```text
\omega_0
omega_0
omega0
ω₀
```

If a remaining occurrence is intentional, identify and justify it explicitly in the report. Also verify that `\Delta` has not collided with an existing symbol for a level spacing, discriminant, finite difference, or another quantity. If such a collision exists, resolve it conservatively without changing the fixed detuning convention.

Inspect the full diff to ensure that this migration has changed no signs, powers, coefficients, denominators, asymptotic orders, hypotheses, labels, citations, or scientific status statements.

## Task B — complete compilation and PDF verification

Use the repository's established root-level build procedure. Clean only generated LaTeX artifacts, never source or user files. Rebuild fully with BibTeX and all required reruns. Examine the complete logs for:

- errors or emergency stops;
- undefined citations or references;
- multiply defined labels;
- missing files, fonts, figures, or bibliography data;
- remaining rerun warnings;
- PDF-string problems;
- visible overfull boxes or other layout regressions caused by the wider `\Delta` glyph.

Render and visually inspect every page affected by the notation migration, plus the title/abstract, first model-definition pages, parameter-map pages, strong- and weak-drive sections, Outlook, appendix, figures, and bibliography. Verify that no formula is clipped and no line break makes the new notation ambiguous.

## Task C — current arXiv-readiness audit

Use current official arXiv documentation as the authority, starting with:

- <https://info.arxiv.org/help/submit_tex.html>
- <https://info.arxiv.org/help/faq/texlive.html>
- <https://info.arxiv.org/help/sizes.html>
- <https://info.arxiv.org/help/tar.html>

Record the access date and the specific requirements applied. If these pages have changed, follow the current official text rather than assumptions embedded in this prompt.

Audit both the manuscript and the exact set of files needed for an arXiv source submission. At minimum check:

1. **Processor and compatibility**
   - identify the intended processor (`pdflatex` unless the source demonstrably requires another);
   - check compatibility with arXiv's currently supported/default TeX Live environment;
   - verify that every document class and package is supplied by that environment or included legally and necessarily in the source package;
   - reject shell escape, unsupported converters, external network access, local absolute paths, and machine-specific dependencies.

2. **Root-level reproducibility**
   - remember that arXiv compiles from the root of the uploaded submission tree even when the top-level `.tex` file is in a subdirectory;
   - create a temporary clean staging directory outside the repository's tracked tree;
   - copy into it only the files genuinely required for compilation, preserving whatever relative paths the canonical source uses;
   - compile from the staging directory root using the intended arXiv-like command sequence;
   - run BibTeX and all required reruns;
   - inspect the resulting log and PDF;
   - delete or retain the temporary staging directory only as appropriate for verification, but do not add it to Git.

3. **Bibliography**
   - include the required `.bib` file or a correctly named matching `.bbl` according to current arXiv rules;
   - verify every citation resolves in the isolated package;
   - do not include stale `.aux`, `.log`, `.blg`, or unrelated bibliography files;
   - check whether bibliographical arXiv identifiers, where already available and reliable, are formatted so automatic extraction can recognize them; do not start a broad bibliography rewrite solely to add identifiers.

4. **Figures and file paths**
   - include every and only the figure files used by the manuscript;
   - verify all formats are supported directly by the selected processor and require no on-the-fly conversion;
   - identify dimensions, color mode, alpha/transparency, interlacing, metadata/profile chunks, megapixel count, and byte size of raster figures where tools permit;
   - flag images exceeding current arXiv warnings or creating an unnecessarily large submission;
   - do not alter, recompress, or regenerate scientific figures during this audit unless a minimal lossless normalization is unquestionably necessary; otherwise report a recommendation.

5. **Package hygiene**
   - exclude generated PDF, auxiliary files, logs, diffs, prompts, reports, repository metadata, backup snapshots, unused figures, notebooks, scripts, test data, and hidden files/directories;
   - check for problematic filenames, case mismatches, spaces, nonportable characters, symlinks, and files referenced only through local paths;
   - ensure no JavaScript, movies, embedded attachments, or active content is present in the generated PDF or submitted source assets;
   - verify that the source contains no `\today` date, referee/double-spacing mode, comments disclosing private material, TODOs, merge markers, or editing debris.

6. **Submission size and exact manifest**
   - compute the total byte size of the minimal staged source tree and list every included file with its size and purpose;
   - compare relevant images against current official arXiv size/megapixel guidance;
   - state the exact proposed archive manifest;
   - do **not** create a final upload archive unless explicitly requested in a later stage.

7. **Metadata and moderation-facing readiness**
   - report the exact title and author string extracted from the manuscript;
   - propose, but do not insert into the TeX source, a concise arXiv abstract text only if the current abstract cannot be used verbatim in arXiv metadata;
   - identify a plausible primary arXiv category and optional cross-list as a recommendation, clearly separated from technical compliance;
   - note that account, endorsement, license choice, author identity/ORCID, subject classification, submission agreement, and the mandatory inspection of arXiv's generated PDF are user-side submission steps and cannot be certified from the repository.

Do not upload, submit, create an arXiv draft, select a license on the user's behalf, or contact arXiv.

## Editing boundary for the arXiv audit

You may make minimal edits to `manuscript/manuscript.tex` when they are necessary for the fixed notation migration, correct compilation, or definite arXiv technical compatibility. Do not make optional editorial changes, rewrite the abstract for discoverability, change scientific claims, add affiliations not supplied by the author, or alter figures merely to optimize them.

If a technical arXiv issue can be fixed safely and locally, fix it and document it. If it requires an author choice or could affect scientific presentation, report it without editing.

## Required deliverables

Create at the repository root:

```text
prompt_15b_delta_notation_and_arxiv_readiness.log
prompt_15b_delta_notation_and_arxiv_readiness.diff
```

After all edits and verification, generate the complete tracked patch with:

```bash
git diff --binary > prompt_15b_delta_notation_and_arxiv_readiness.diff
```

The `.log` must contain:

1. initial branch, `HEAD`, and worktree state;
2. confirmation that accepted stage-15a changes were preserved;
3. every file modified in 15b;
4. the exact physical convention `\Delta=\omega_c-\omega_d` and confirmation that no sign changed;
5. a categorized inventory of every notation replacement, including updated dimensionless definitions;
6. results of the old-symbol search and the symbol-collision audit;
7. compilation commands, exit codes, final warnings, and reference/citation status;
8. PDF visual-inspection results;
9. official arXiv pages consulted, access date, and requirements applied;
10. arXiv processor/TeX Live/package compatibility findings;
11. the isolated staging-tree build procedure and result;
12. the exact proposed arXiv source manifest with file sizes and purposes;
13. total staged-package size and raster-image diagnostics;
14. package-hygiene and active-content results;
15. technical blockers, non-blocking recommendations, and user-side submission steps, clearly separated;
16. final `git diff --check` and `git status -sb` output;
17. one of these final verdicts:
    - `ARXIV-READY`;
    - `ARXIV-READY AFTER USER-SIDE METADATA STEPS`;
    - `NOT ARXIV-READY — TECHNICAL BLOCKERS REMAIN`.

Do not issue an arXiv-ready verdict unless the minimal isolated staging tree compiles successfully from its root, the bibliography and every reference resolve, all required figures are present, the generated PDF has been inspected, and the exact manifest has been audited.

## Final checks

Run at least:

```bash
git diff --check
git status -sb
```

End with a concise summary stating:

- notation-migration result;
- confirmation that the Hamiltonian still contains `+\hbar\Delta N`;
- old-symbol search result;
- normal repository build result;
- isolated arXiv-style build result;
- exact arXiv-readiness verdict;
- remaining technical blockers, if any;
- user-side steps still required;
- files modified;
- confirmation that no archive was finalized, no submission was made, and no commit or push was performed.
