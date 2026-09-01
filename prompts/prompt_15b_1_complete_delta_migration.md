# Prompt 15b_1 — complete the detuning-symbol migration

Work in the repository:

```bash
cd ~/Dokumenty/Prace_i_dnie/Wnęka_z_Kerrem
```

## Purpose

This is a **strictly limited corrective micro-stage** following prompt 15b. The 15b audit incorrectly reported that every occurrence of the old detuning symbol had been removed. One occurrence survived because whitespace separated the TeX command from its subscript:

```tex
\delta=\frac{\hbar\omega _0}{V}.
```

The objectives are only to:

1. replace this surviving old model parameter by `\Delta`;
2. perform a whitespace-tolerant and syntax-tolerant search for every possible remaining form of the old symbol;
3. rebuild and reverify the canonical manuscript and the minimal arXiv staging tree;
4. correct the inaccurate statements in the 15b report and refresh the cumulative 15b patch;
5. create separate 15b_1 report and patch deliverables.

Do not reopen style, mathematics, bibliography, figures, metadata recommendations, or the already completed arXiv-readiness analysis except insofar as the single correction requires verification.

## Fixed convention

The signed detuning remains

```tex
\Delta:=\omega_c-\omega_d,
```

and the rotating-frame Hamiltonian remains

```tex
+\hbar\Delta N.
```

The dimensionless strong- and weak-drive parameter is

```tex
\delta=\frac{\hbar\Delta}{V}.
```

No sign, coefficient, definition, or scientific claim may change.

## Protect all existing work

The worktree intentionally contains the accepted changes from 15a and the otherwise accepted changes from 15b. Treat all tracked modifications and untracked files as user-owned. Do not overwrite the canonical manuscript from a snapshot. Do not use `git reset`, `git checkout`, `git restore`, or any destructive operation. Do not commit and do not push.

Before editing, record:

```bash
git status -sb
git log -1 --oneline --decorate
git status --porcelain=v1
git diff -- manuscript/manuscript.tex
```

Confirm that the expected 15a and 15b changes are present before proceeding.

## Required source correction

In `manuscript/manuscript.tex`, change the known surviving definition from the old parameter to:

```tex
\eta=\frac{|F|}{V},\qquad \delta=\frac{\hbar\Delta}{V},
```

Make no other manuscript edit unless another syntactic variant of the same old model parameter is found.

## Robust old-symbol audit

The previous literal searches were insufficient. Search the **entire canonical TeX source** for the semantic pattern “Greek lowercase omega with subscript zero,” allowing arbitrary TeX whitespace and common bracing variants. At minimum detect all of the following:

```tex
\omega_0
\omega _0
\omega_{0}
\omega _{0}
\omega  _  { 0 }
\omega{}_{0}
\omega {} _ {0}
```

Also search for plain-text and Unicode variants:

```text
omega_0
omega 0
omega0
ω₀
ω_0
ω 0
```

Use at least one regular expression that allows whitespace between `\omega`, optional empty braces, `_`, and zero. For example, adapt and test a pattern equivalent in intent to:

```regex
\\omega\s*(?:\{\s*\})?\s*_\s*(?:\{\s*0\s*\}|0)
```

Do not rely solely on `rg '\\omega_0'`. Record the exact commands and outputs.

Distinguish genuine old detuning occurrences from legitimate uses of an unrelated auxiliary special-function parameter `\omega`, the physical frequencies `\omega_c` and `\omega_d`, and prose/bibliography words. Those must remain unchanged.

Then extract text from the rebuilt PDF and search it for visible forms of omega with subscript zero, including spacing introduced by text extraction. Confirm manually on the formerly affected strong-drive page that the displayed definition now contains `\hbar\Delta/V`.

## Diff-integrity check

Compare the corrected canonical source against the source at the end of 15b. Apart from generated artifacts, the 15b_1 manuscript diff must consist only of the replacement

```tex
\hbar\omega _0/V  ->  \hbar\Delta/V
```

unless another old-symbol spelling is genuinely found. If anything else differs, stop and explain before modifying it.

Inspect the cumulative Git diff as well and verify that all accepted 15a/15b changes remain intact, including:

- the author's second-iteration wording;
- the 15a reference, bibliography, layout, and integrity corrections;
- the 15b definition `\Delta=\omega_c-\omega_d`;
- `+\hbar\Delta N` in the Hamiltonian;
- every other completed `\omega_0` to `\Delta` replacement;
- the absence of the unsupported continued-fraction convergence/rate claim.

## Canonical build and PDF verification

Run the established clean root-level build, including BibTeX and all required reruns. Check the final logs for errors, undefined references/citations, missing files, multiply defined labels, rerun warnings, and layout warnings.

Render and inspect at least:

- the page containing the corrected strong-drive definition;
- its preceding and following pages;
- the first Hamiltonian/rotating-frame definition pages;
- any page on which the correction changes line or page breaking.

Confirm that the canonical PDF has the expected page count and no visible regression.

## Isolated arXiv-style rebuild

Repeat the isolated staging-tree verification using the same exact minimal eight-file manifest established in 15b:

```text
manuscript/manuscript.tex
manuscript/references.bib
figures/stokes_geometry.pdf
figures/fedoryuk_stokes_geometry.pdf
figures/12b_final_iterated_wkb/final_eta0p25_k3_branchI_domainleft_bright-phase-modulus.png
figures/12b_final_iterated_wkb/final_eta0p25_k3_branchR_domainturning_bright-equalized.png
figures/12b_final_iterated_wkb/final_eta4p0_k2_branchI_domainlocal_bright-banded-modulus.png
figures/12b_final_iterated_wkb/final_eta4p0_k2_branchR_domainturning_bright-phase-modulus.png
```

Create a fresh temporary directory outside the tracked repository, preserve these relative paths, and compile from the staging-tree root with `pdflatex`/BibTeX via the same verified procedure used in 15b. Do not reuse the old staged PDF as evidence.

Confirm:

- clean compilation;
- resolved bibliography and cross-references;
- identical source manifest;
- no missing assets;
- a visually correct generated PDF;
- the corrected `\Delta` definition in extracted staged-PDF text;
- no old omega-sub-zero detuning in staged source or PDF.

Do not create a final upload archive and do not submit anything to arXiv.

## Correct the 15b deliverables

Update:

```text
prompt_15b_delta_notation_and_arxiv_readiness.log
prompt_15b_delta_notation_and_arxiv_readiness.diff
```

The corrected 15b log must not conceal the earlier miss. Add a short, explicit correction note stating:

- the initial 15b search was too literal and missed `\omega _0` because of TeX whitespace;
- 15b_1 corrected the surviving occurrence;
- the old-symbol audit was repeated with a whitespace-tolerant pattern;
- the canonical and isolated builds were repeated successfully;
- the final arXiv-readiness verdict applies only after this correction.

Update every affected count or claim. In particular, do not retain “eighteen occurrences” if the corrected total is nineteen; state the verified final count accurately and explain whether it counts source occurrences or conceptual locations.

Regenerate the cumulative 15b patch only after verification:

```bash
git diff --binary > prompt_15b_delta_notation_and_arxiv_readiness.diff
```

## New 15b_1 deliverables

Create at the repository root:

```text
prompt_15b_1_complete_delta_migration.log
prompt_15b_1_complete_delta_migration.diff
```

The 15b_1 `.diff` must document the corrective stage as clearly as normal Git semantics allow. Because the manuscript was already modified before 15b_1, first preserve a temporary copy of the exact pre-15b_1 canonical TeX source outside the repository, then produce a focused unified diff between that copy and the corrected source. Include that focused one-change diff in the 15b_1 report. Also generate the required repository-level cumulative patch with `git diff --binary`; explain clearly which file is focused and which is cumulative. Do not modify the Git index merely to manufacture a diff.

The 15b_1 log must include:

1. initial state and protected work;
2. the exact missed source line before correction;
3. the exact corrected line;
4. root cause of the miss: whitespace-sensitive search;
5. all robust regex/plain-text/Unicode searches and their outputs;
6. confirmation that unrelated `\omega`, `\omega_c`, and `\omega_d` uses remain intentionally;
7. focused pre/post-15b_1 diff;
8. cumulative-diff integrity result;
9. canonical build commands and results;
10. canonical PDF text and visual checks;
11. isolated staging-tree build and PDF checks;
12. corrected 15b report/diff status;
13. final `git diff --check` and `git status -sb` output;
14. final verdict: `PASS` or `BLOCKED`;
15. confirmation that no archive, submission, commit, or push was performed.

## Final checks

Run at least:

```bash
git diff --check
git status -sb
```

The final summary must state explicitly:

- whether the known `\omega _0` occurrence was replaced;
- whether **any whitespace/bracing variant** of omega-sub-zero remains;
- whether `\Delta=\omega_c-\omega_d` and `+\hbar\Delta N` remain correct;
- canonical compilation result;
- isolated arXiv-style compilation result;
- corrected arXiv-readiness verdict;
- files modified;
- confirmation that no archive was finalized, no arXiv action was taken, and no commit or push was performed.
