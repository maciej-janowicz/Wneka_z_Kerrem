# Stage 05b — Prompt delimiter repair, verification record update, and complete staged diff

Work in the existing `Wnęka_z_Kerrem` repository.

Read before editing:

* `AGENTS.md`;
* `README.md`;
* `prompts/05_taylor_and_infty.md`;
* `docs/stage05_taylor_and_infty.md`;
* `prompts/05a_limit_corrections.md`, if present;
* `stage05a_limit_corrections.log`, if present;
* the current Stage 05 and Stage 05a source and test files;
* the current manuscript;
* the complete current Git status and diff.

Do not commit or discard anything.

Do not use:

```bash
git add .
git add -A
```

Preserve every unrelated user change.

## Purpose

Stage 05a has undergone an independent audit.

Its mathematics, implementation, and tests were found to be substantially correct. In particular, do not redesign or rederive:

1. the Taylor recurrence at (z=0);
2. the asymptotic recurrence at infinity;
3. the explicit Taylor or asymptotic coefficients;
4. the fixed-square-root-branch parity relation;
5. the validation condition for caller-supplied
   `sqrt_minus_q`;
6. the exactly undriven Bargmann operator test;
7. the analytic continuation under
   (z\mapsto ze^{2\pi i}).

Stage 05b is a narrowly limited documentation, verification, and repository-record correction.

It has exactly four purposes:

1. repair malformed inline LaTeX delimiters in the historical Stage 05 prompt;
2. update the verification record in the Stage 05 technical note;
3. rerun the complete validation;
4. create a complete staged diff containing all Stage 05, Stage 05a, and Stage 05b project changes, including files that were previously untracked.

Do not make unrelated source-code, test, manuscript, API, or mathematical changes.

Before editing, run and record:

```bash
git status --short
git diff --stat
git diff --check
git diff --cached --stat
git diff --cached --check
```

If there are already staged files, inspect them and preserve them. Do not unstage, overwrite, or discard pre-existing staged changes.

---

## Correction 1 — Repair malformed LaTeX delimiters in the historical Stage 05 prompt

Edit only:

```text
prompts/05_taylor_and_infty.md
```

for this correction.

The file is a historical task specification. It must remain a prompt describing work that was still to be performed at Stage 05. It must not be rewritten retrospectively to match the completed implementation.

### Known defect

The prompt still contains many mathematical expressions written with ordinary parentheses instead of Markdown LaTeX delimiters. Examples include:

```text
Taylor expansion at (z=0)
arbitrary (N\ge0)
parameters ((B_1,B_2,B_3,q))
physical restriction (\overline F=F^*)
```

Repair them as:

```text
Taylor expansion at \(z=0\)
arbitrary \(N\ge0\)
parameters \((B_1,B_2,B_3,q)\)
physical restriction \(\overline F=F^*\)
```

Search the entire canonical prompt for analogous cases.

Typical indications that text inside ordinary parentheses is intended as mathematics include:

* TeX commands such as `\ge`, `\le`, `\sqrt`, `\sigma`, `\overline`,
  `\hbar`, `\omega`, `\Psi`, `\infty`, `\mapsto`, or `\neq`;
* subscripts or superscripts;
* parameter tuples;
* equations or inequalities;
* variable assignments;
* mathematical ranges;
* references to mathematical limits or expansions.

### Strict editing limits

Repair only demonstrable transcription and Markdown/LaTeX delimiter defects.

Do not:

* convert ordinary prose parentheses into mathematics;
* change mathematical targets;
* replace formulas with formulas learned from the implementation;
* add conclusions obtained during Stage 05 or Stage 05a;
* change the requested APIs;
* rewrite paragraphs for style;
* modernize the historical prompt;
* alter the scope of the historical task;
* claim that the prompt was restored from an exact original source unless such a
  source actually exists;
* manufacture missing substantive content.

Where the corrupted text contains doubled parentheses such as:

```text
((B_1,B_2,B_3,q))
```

restore the intended inline-mathematics form:

```text
\((B_1,B_2,B_3,q)\)
```

Do not leave the doubled prose parentheses around the LaTeX delimiters.

Preserve fenced code blocks literally unless a demonstrable corruption exists inside a block that was intended to show Markdown rather than executable code.

### Required prompt audit

After editing, inspect the complete prompt manually.

Search for previously identified corruption:

```bash
rg -n 'DeriveDerive|^=======|e\^\{,|q,c_\{n-1\}' prompts/05_taylor_and_infty.md
```

Search for likely remaining malformed mathematical parentheses. Use several narrow searches rather than blindly replacing every parenthesized expression. At minimum inspect matches containing:

```bash
rg -n '\([^)]*\\(ge|le|sqrt|sigma|overline|hbar|omega|Psi|infty|mapsto|neq|frac|sum|pm|cdot)[^)]*\)' prompts/05_taylor_and_infty.md
rg -n '\([^)]*[_^][^)]*\)' prompts/05_taylor_and_infty.md
```

These searches are diagnostic only. Some matches may be valid for another reason. Review every match individually.

Also check:

* balanced `\(` and `\)` delimiters;
* balanced `\[` and `\]` delimiters;
* balanced fenced code blocks;
* absence of conflict markers;
* valid Markdown heading structure;
* absence of competing Stage 05 prompt filenames;
* absence of accidental changes to mathematical content.

If no exact clean historical source exists, retain the existing truthful statement that the prompt was repaired typographically rather than restored exactly.

---

## Correction 2 — Update the Stage 05 technical note’s verification record

Edit:

```text
docs/stage05_taylor_and_infty.md
```

only where necessary to make its verification section accurately describe the tests that now exist.

Do not rewrite the mathematical derivation or other technical sections.

In the existing verification section, add concise and accurate entries for:

1. the fixed-root parity test, where one chosen
   (s=\sqrt{-q}) is held fixed and only
   (\sigma\mapsto-\sigma), checking
   [
   u_n^{(-\sigma)}=(-1)^n u_n^{(\sigma)}
   ]
   through (n=8);

2. the separate branch/sign relabelling test
   [
   (\sigma,s)\mapsto(-\sigma,-s),
   ]
   if it is retained in the actual test suite;

3. validation of both legitimate values (s) and (-s);

4. rejection of demonstrably inconsistent pairs ((q,s));

5. numerical validation for real or complex floating-point values using the
   tolerance actually implemented in the source;

6. acceptance of an appropriately rounded value within that tolerance and
   rejection of a value outside it;

7. rejection of the degenerate input required by the current API, such as
   (q=0) or (s=0);

8. the independent operator test for the exactly undriven case, applying
   [
   \mathcal L_E
   ============

   \frac V2z^2\frac{d^2}{dz^2}
   +
   \hbar\omega_0z\frac{d}{dz}
   --------------------------

   E
   ]
   to the full polynomial (z^n), for the values
   [
   n=0,1,2,3,5,8.
   ]

Verify all claimed test names, orders, parameter types, values of (n), and tolerances directly against the current source and test files. Do not copy claims from an earlier execution report without checking them.

If the actual implementation differs from any item above, do not silently change code in Stage 05b. Report the discrepancy and stop before staging.

The technical note must continue to distinguish:

* fixed-(s) parity under (\sigma\mapsto-\sigma);
* redundant relabelling under
  ((\sigma,s)\mapsto(-\sigma,-s));
* the exactly degenerate undriven problem;
* a limiting process (F\to0).

Do not add new claims about convergence, quantization, Stokes multipliers, or global connection problems.

---

## Correction 3 — Full validation without redesign

After the two documentation corrections, run the complete existing test suite using the repository’s established environment and command.

Do not run only `tests/test_local_series.py`.

Record:

* the exact command;
* the number of passed, failed, skipped, or xfailed tests;
* the runtime;
* every warning;
* every failure and its diagnosis.

Do not weaken, delete, skip, or rewrite a test merely to obtain a green suite.

If a failure is unrelated to Stage 05b, preserve it and report it precisely. Do not perform unrelated repair work.

Compile the manuscript using the repository’s established build procedure.

Record:

* the exact build command;
* whether the build succeeded;
* warnings relevant to the changed material;
* unresolved references or citations;
* overfull or underfull boxes on affected pages.

Inspect visually every PDF page affected by Stage 05 or Stage 05a, especially pages containing:

* the Taylor expansion;
* the formal expansion at infinity;
* (s=\sqrt{-q});
* fixed-root parity;
* branch/sign relabelling;
* analytic continuation under (z\mapsto ze^{2\pi i});
* the exactly undriven case.

Record the exact page numbers inspected.

Check for:

* malformed square roots;
* missing or duplicated delimiters;
* ambiguous branch notation;
* equation overflow;
* broken cross-references;
* misplaced equation numbers;
* inconsistent notation involving
  (F^*), (\overline F), (s), (\sigma), (q), and
  (u_n^{(\sigma)}).

Run:

```bash
git diff --check
```

before staging.

---

## Correction 4 — Create a complete staged diff

The previous file:

```text
stage05a_limit_corrections.diff
```

was incomplete because ordinary `git diff` did not include untracked Stage 05 files.

Create a complete diff only after identifying every project file belonging to Stage 05, Stage 05a, or Stage 05b.

### Safety requirements

First inspect:

```bash
git status --short
git diff --stat
git diff --cached --stat
```

Prepare an explicit list of files to be staged.

Do not use:

```bash
git add .
git add -A
```

Do not stage:

* unrelated user files;
* temporary files;
* rendered page images;
* build auxiliaries;
* caches;
* virtual environments;
* the generated diff itself;
* the execution log itself;
* files whose relationship to Stage 05 cannot be established.

If the repository already contains staged changes that are not part of Stage 05, Stage 05a, or Stage 05b, do not alter them. Report that the cached diff contains pre-existing staged material and create a path-limited Stage 05 diff instead.

### Staging

Stage only explicitly enumerated Stage 05, Stage 05a, and Stage 05b project files, including relevant files that were previously untracked.

Use commands of the form:

```bash
git add -- path/to/file1 path/to/file2 ...
```

Before executing `git add`, print and record the exact path list.

Do not commit.

After staging, inspect:

```bash
git status --short
git diff --cached --stat
git diff --cached --check
git diff --cached
```

Confirm that every intended new source, test, documentation, prompt, and manuscript file appears in the cached diff, and that no unrelated file appears.

Create:

```text
stage05b_updates_tests.diff
```

from the staged changes.

If the index contains only the intended Stage 05–05b changes, use:

```bash
git diff --cached --binary > stage05b_updates_tests.diff
```

If unrelated changes were already staged before Stage 05b and must be preserved, generate the diff with an explicit path list:

```bash
git diff --cached --binary -- path/to/stage05_file1 path/to/stage05_file2 ... > stage05b_updates_tests.diff
```

Do not stage `stage05b_updates_tests.diff`.

Verify that the generated diff contains:

* additions of previously untracked Stage 05 files;
* source changes;
* test changes;
* technical-note changes;
* historical-prompt changes;
* manuscript changes belonging to Stage 05 or Stage 05a;
* the new `prompts/05b_updates_tests.md` file, if it exists in the repository and
  is part of the intended project record.

Inspect the diff header list directly:

```bash
rg -n '^diff --git ' stage05b_updates_tests.diff
```

Do not assume completeness merely because the command succeeded.

---

## Final consistency checks

Run and record:

```bash
git diff --check
git diff --cached --check
git status --short
git diff --stat
git diff --cached --stat
```

Check for competing Stage 05 prompt filenames:

```bash
find prompts -maxdepth 1 -type f -printf '%f\n' | sort
```

Confirm that the canonical historical Stage 05 prompt remains:

```text
prompts/05_taylor_and_infty.md
```

and that the Stage 05b execution prompt, if saved in the repository, is:

```text
prompts/05b_updates_tests.md
```

These are different files with different purposes and are not competing duplicates.

Search the canonical Stage 05 prompt once more for known corruption:

```bash
rg -n 'DeriveDerive|^=======|e\^\{,|q,c_\{n-1\}' prompts/05_taylor_and_infty.md
```

Search the manuscript and technical note for the previously ambiguous orientation wording:

```bash
rg -n -i 'positive circuit.*infinity|positive circuit.*about infinity|positive circuit.*around infinity' manuscript docs
```

Confirm that no source code, mathematical formula, API, or test was changed during Stage 05b unless a discrepancy forced the work to stop before staging.

---

## Deliverables

Create a concise execution log:

```text
stage05b_updates_tests.log
```

Do not stage the log.

At completion, report:

1. the initial `git status --short`;
2. every file modified during Stage 05b;
3. the exact delimiter repairs made in
   `prompts/05_taylor_and_infty.md`;
4. whether any suspected parenthesized expression was deliberately left unchanged
   and why;
5. whether the historical prompt was restored from an exact clean source or only
   repaired typographically;
6. whether any substantive historical content remains unrestorable;
7. the exact additions made to the verification section of
   `docs/stage05_taylor_and_infty.md`;
8. confirmation that the documented test claims were checked against the actual
   source and tests;
9. the complete test-suite command and result;
10. the manuscript build command and result;
11. every affected PDF page visually inspected;
12. the result of `git diff --check`;
13. the exact list of files staged;
14. whether any files had already been staged before Stage 05b;
15. the result of `git diff --cached --check`;
16. the files contained in `stage05b_updates_tests.diff`;
17. confirmation that previously untracked Stage 05 source, test, prompt, and
    documentation files are now represented in that diff;
18. the final `git status --short`;
19. every warning, discrepancy, or requested item that could not be completed;
20. explicit confirmation that no commit was created.

Save the complete staged diff as:

```text
stage05b_updates_tests.diff
```

and the execution record as:

```text
stage05b_updates_tests.log
```

Do not stage those two generated audit artifacts.

Do not commit.

Stop after reporting the results and wait for independent review.
