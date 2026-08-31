# Prompt 13a — repair theorem references and balance the manuscript's scientific tone

Work in:

```bash
cd ~/Dokumenty/Prace_i_dnie/Wnęka_z_Kerrem
```

This is a narrowly controlled follow-up to Prompt 13. Do not repeat the full mathematical audit and do not broaden the scientific scope of the paper.

## 0. Verify the starting state

The approved pre-audit baseline remains commit `d0c1911a4b3dd470faec8761bad5fe433393095a`. Prompt 13 has already modified the manuscript and bibliography and has produced its report and patch. This prompt has now also been copied into the repository as `prompts/prompt_13a_balance_scope_and_fix_theorem_refs.md`.

Before editing, run:

```bash
git status -sb
git log -1 --oneline --decorate
git rev-parse HEAD
git rev-parse origin/master
git status --porcelain=v1
```

Proceed only if:

- `HEAD` and `origin/master` both equal `d0c1911a4b3dd470faec8761bad5fe433393095a`;
- the branch is `master...origin/master`, with no ahead/behind indication;
- the tracked changes from Prompt 13 are limited to:
  - `manuscript/manuscript.tex`;
  - `manuscript/references.bib`;
- the expected untracked files are limited to:
  - `prompt_13_prefinal_integrity_audit.diff`;
  - `prompts/prompt_13_prefinal_integrity_audit.md`;
  - `prompts/prompt_13a_balance_scope_and_fix_theorem_refs.md`;
- `prompt_13_prefinal_integrity_audit.log` and rebuilt PDF files may exist without appearing in status because of ignore rules;
- there are no staged changes, conflicts, deletions, renames, or other modified/untracked paths.

If the actual state differs, stop without modifying anything and report the exact discrepancy. Do not edit either prompt file.

## 1. Correct the theorem-reference inconsistency

Inspect the source labels before editing; use symbolic LaTeX cross-references rather than hard-coded theorem numbers wherever possible.

The continued-fraction result is **Theorem 4.3**, not Theorem 4.2. The latter is a remark on the undriven problem. Correct the end of the proof so that it states unambiguously that:

1. all equivalences asserted in the continued-fraction theorem have been proved; and
2. this argument also completes the deferred proof of the HeunWI spectral theorem, Theorem 4.1.

The intended sense is:

> This proves all equivalences in Theorem 4.3 and completes the proof of Theorem 4.1.

Implement this with existing or newly added `\label`/`\ref` commands if the local theorem structure permits it cleanly. Do not renumber the theorem, remark, equations, or sections.

Correct the Prompt 13 audit report wherever it calls this result “Theorem 4.2”; it must say “Theorem 4.3”. Check the report for any further references made stale by this correction, but do not rewrite the report wholesale.

## 2. Balance honesty with a confident scientific presentation

Review the abstract, introduction, transitions into and out of the Olver/Fedoryuk sections, captions, conclusion/Outlook, and nearby passages that describe limitations. The manuscript must remain mathematically honest, but it must not read as an extended apology for results that remain open.

Use the following editorial principle:

> State each limitation once, at the point where it is mathematically needed; state it precisely and neutrally; then emphasize the positive result that is established and the concrete role of the open step.

### Preserve without weakening

The manuscript must continue to make clear that:

- the operator-theoretic results and the continued-fraction spectral condition are exact;
- the sectorial Volterra construction and its displayed bounds have the status actually proved in the manuscript;
- the local Olver/Fedoryuk/Weber constructions do not by themselves establish the global Bargmann connection or a global WKB quantization theorem;
- the strong-drive fixed-level expansion has the formal/conditional status established in the audit and no proved global uniform remainder for growing `n`;
- `C_ess=0`, the relevant orientation/connection hypotheses, and the global Fedoryuk contraction remain conjectural or conditional as presently formulated;
- the weak-drive multiplicative construction is local/finite-order where stated and is not a proved global zero-controlled hierarchy;
- the iteration portraits are exploratory visualizations of the disclosed regularized map, not physical time evolution, a proof of fractality, or a substitute for a global eigenfunction construction.

Do not turn any of these qualifications into stronger claims.

### Remove or soften only rhetorical overemphasis

Look for:

- repeated disclaimers saying essentially the same thing in adjacent or multiple sections;
- phrases such as “we have not”, “cannot”, “does not prove”, “missing”, “failed”, or “only”, when a neutral scope statement would be clearer;
- sentences that foreground absence before stating the achieved result;
- long catalogues of unproved global ingredients when one precise sentence plus a cross-reference would suffice;
- language that makes rigorous local, sectorial, exact-recursive, or carefully verified formal results sound scientifically negligible;
- captions or Outlook prose that repeat caveats already made in the mathematical section.

Where appropriate, prefer formulations such as:

- “The present result is local/sectorial; its global completion requires …”
- “Under Hypotheses H1–H3, the construction yields …”
- “This identifies the remaining global connection problem as …”
- “The exact continued-fraction condition supplies the spectral anchor for …”
- “The local Weber analysis determines …, while the global connection coefficient remains to be established.”
- “The portraits visualize the regularized iterated map defined above.”

Do not mechanically replace every negative construction. Sometimes “does not imply” is the mathematically sharpest wording and should remain. The goal is not promotional language; it is proportion, economy, and confidence.

### Positive hierarchy of results

Ensure that the abstract and introduction lead with what the paper accomplishes:

1. rigorous operator-theoretic control and discrete spectrum;
2. exact Bargmann/continued-fraction spectral characterization;
3. controlled sectorial asymptotics;
4. independently checked strong- and weak-drive expansions with their proper status;
5. local Olver/Fedoryuk structure that isolates a precise global connection problem;
6. exploratory iteration portraits as a secondary visualization.

The abstract should not become a list of disclaimers. One concise sentence distinguishing established results from the conjectural global connection is enough. Do not add priority, novelty, universality, or application claims unsupported by the paper.

## 3. Scope of edits

Make only changes that are clearly justified by Sections 1–2 above. In particular:

- do not alter formulas, coefficients, assumptions, conjectures, numerical data, figures, or scientific conclusions;
- do not remove a necessary hypothesis or caveat;
- do not convert conjectures into propositions or formal expansions into rigorous asymptotics;
- do not undertake a general stylistic rewrite;
- preserve established notation, normalization, terminology, and bibliography except for any mechanically necessary cross-reference adjustment;
- do not reintroduce removed bibliography entries merely to enlarge the bibliography.

If, after careful inspection, a passage is already well balanced, leave it unchanged. Minimality is preferred.

## 4. Reports and patches

Create:

- `prompt_13a_balance_scope_and_fix_theorem_refs.log` — a concise but complete report listing:
  - verified initial state;
  - the theorem-reference correction;
  - every tone-related passage changed, with location, old rhetorical problem, and reason the new wording remains mathematically honest;
  - important caveats deliberately retained;
  - files changed;
  - build/tests/checks and exact outcomes;
  - pages visually inspected;
  - final `git status -sb`;
  - explicit confirmation: no commit and no push.

- `prompt_13a_balance_scope_and_fix_theorem_refs.diff` — the incremental patch made by Prompt 13a, excluding pre-existing Prompt 13 changes. Capture the pre-13a state safely before editing so that this incremental patch is reproducible.

Also update `prompt_13_prefinal_integrity_audit.log` minimally to correct “Theorem 4.2” to “Theorem 4.3” and, if necessary, add a short clearly marked 13a addendum recording the corrected proof closure and tone review. Do not falsify the original test record or issue counts.

Finally regenerate `prompt_13_prefinal_integrity_audit.diff` so that it remains the complete cumulative textual patch from `d0c1911` to the final post-13a worktree. Ensure that it includes the corrected audit report if that report is intentionally part of the cumulative patch.

Do not include generated PDF binaries in textual `.diff` files.

## 5. Validation

After editing:

1. compile the manuscript using the established clean `latexmk` procedure;
2. run the relevant fast test set needed to ensure that no mathematical or cross-reference regression was introduced; a full 106-test rerun is optional if no formula/code changed, but explain the choice;
3. scan LaTeX/BibTeX logs for undefined references/citations, duplicate labels, missing entries, TeX errors, and serious layout warnings;
4. verify that all theorem references resolve correctly in the PDF;
5. visually inspect at least the abstract/introduction pages, the corrected Theorem 4.3 proof page, every page whose prose changed, the iteration-figure caption if changed, and the Outlook/bibliography transition;
6. run repository searches for stale “Theorem 4.2” references to the continued-fraction result;
7. run `git diff --check`;
8. verify both the incremental 13a patch and the regenerated cumulative Prompt 13 patch with appropriate reverse-apply checks;
9. report the final `git status -sb`.

Successful compilation does not authorize stronger mathematical language.

## 6. Final response

Report briefly:

- whether the theorem-reference inconsistency was corrected;
- how many tone-related passages were changed and how many caveats were deliberately retained;
- whether any scientific claim was strengthened (the expected answer is no);
- files changed/created;
- build and validation status;
- locations of the incremental 13a `.log` and `.diff` and the refreshed cumulative Prompt 13 `.diff`;
- final `git status -sb`;
- confirmation that no commit or push was performed.

Do **not** commit, push, tag, reset, stash, or discard changes.
