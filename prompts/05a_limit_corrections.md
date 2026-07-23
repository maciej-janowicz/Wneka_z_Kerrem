# Stage 05a — Strictly limited corrections after the Stage 05 review

Work in the existing `Wnęka_z_Kerrem` repository.

Read, before editing:

- `AGENTS.md`;
- `README.md`;
- the current manuscript;
- `docs/stage05_taylor_and_infty.md`;
- all source and test files changed during Stage 05;
- the Stage 05 diff and execution log, if present;
- every existing Stage 05 prompt file under `prompts/`.

Do not commit, stage, or discard anything.

## Purpose

Stage 05 has already undergone an independent mathematical review.

The following principal results were found to be substantially correct and are
not to be re-derived or redesigned in this correction stage:

1. the Taylor recurrence at \(z=0\);
2. the explicit coefficients \(c_1,c_2,c_3,c_4\);
3. the arbitrary-order Taylor coefficient generator;
4. the formal asymptotic structure
   \[
   \Psi_\sigma(z)
   \sim
   e^{2\sigma\sqrt{-qz}}
   z^{1/4-B_2/2}
   \sum_{n=0}^{\infty}u_n^{(\sigma)}z^{-n/2};
   \]
5. the recurrence for the asymptotic coefficients;
6. the explicit coefficients
   \(u_1^{(\sigma)},u_2^{(\sigma)},u_3^{(\sigma)}\);
7. the separate treatment of the exactly undriven case
   \(F=\overline F=0\).

Make only the corrections explicitly listed below.

Do not:

- repeat Stage 05 from the beginning;
- replace correct derivations merely with algebraically equivalent ones;
- redesign the APIs;
- add new mathematical stages;
- introduce Padé or Hermite–Padé approximants;
- introduce WKB, Liouville–Green, Olver, Fedoryuk, Borel, or Laplace methods;
- add plots or numerical studies;
- introduce new dependencies;
- perform unrelated cleanup;
- update the historical Stage 05 prompt retrospectively so that it matches the
  implementation obtained after executing it.

Before editing, inspect and record:

```bash
git status --short
git diff --stat
git diff --check
```

Preserve all unrelated user changes.

---

## Correction 1 — Restore the historical Stage 05 prompt without reconstructing it from the results

Inspect all existing Stage 05 prompt files, especially possible files named:

```text
prompts/05_taylor_infty.md
prompts/05_taylor_and_infty.md
```

The intended canonical filename is:

```text
prompts/05_taylor_and_infty.md
```

A Stage 05 prompt may contain obvious copy/paste corruption, including examples
such as:

```text
DeriveDerive
`=======`
q,c_{n-1}
e^{,2\sigma...}
```

It may also contain:

- duplicated words;
- malformed Markdown;
- malformed LaTeX delimiters;
- truncated equations;
- missing operators or symbols;
- conflict-marker-like lines;
- accidental punctuation;
- equations written with plain `[` and `]` where `\[` and `\]` were intended.

The Stage 05 prompt is a historical task specification. It is not a technical
note and it is not an authoritative record of the final mathematical results.

Therefore:

1. restore the clean historical prompt under the exact filename

   ```text
   prompts/05_taylor_and_infty.md
   ```

2. remove `prompts/05_taylor_infty.md` only if it is an incorrectly named,
   corrupted duplicate of the same prompt;

3. leave exactly one canonical Stage 05 prompt;

4. repair only demonstrable transcription, formatting, filename, and
   copy/paste errors;

5. do not rewrite its mathematical targets using formulas learned from the
   completed implementation, technical note, manuscript, tests, diff, or log;

6. do not turn the prompt into a retrospective description of what Stage 05
   produced;

7. preserve instructions that the Taylor and asymptotic formulas are to be
   derived and independently verified, rather than treated as already proved.

If an exact clean source supplied by the user exists in the repository, use it
as the authoritative source.

Do not reconstruct the prompt from:

- `docs/stage05_taylor_and_infty.md`;
- the manuscript;
- source code;
- tests;
- Stage 05 output;
- the Stage 05 diff;
- the execution log.

If no exact clean source is available, make only corrections that are
unambiguously typographical. Do not invent missing substantive passages.
Report precisely which portions could not be restored without the original
source.

In particular, do not falsely claim that the historical prompt has been
restored exactly if only an editorial reconstruction was possible.

Verify the final prompt by checking:

- its exact path;
- Markdown structure;
- LaTeX delimiters;
- absence of conflict markers;
- absence of the known corrupted fragments;
- absence of duplicated or competing Stage 05 prompt files.

---

## Correction 2 — Add the missing genuine fixed-branch parity test

This correction is mandatory.

The current branch-related test changes both

\[
\sigma\mapsto-\sigma
\]

and

\[
s\mapsto-s,
\qquad s=\sqrt{-q}.
\]

Because

\[
a_\sigma=2\sigma s,
\]

the simultaneous transformation

\[
(\sigma,s)\mapsto(-\sigma,-s)
\]

leaves \(a_\sigma\) unchanged.

Consequently, that test checks only invariance under a redundant relabelling of
the same effective asymptotic branch. It does not verify the nontrivial parity
relation between the coefficient sequences for \(\sigma=+1\) and
\(\sigma=-1\) at a fixed square-root branch.

### Required implementation

Add a separate test in which:

1. \(q\neq0\) is fixed;
2. one particular value
   \[
   s=\sqrt{-q}
   \]
   is chosen and held fixed;
3. the same \(B_1,B_2,B_3,q,s\) are passed to both generator calls;
4. only \(\sigma\) is changed:
   \[
   \sigma=+1
   \quad\longrightarrow\quad
   \sigma=-1;
   \]
5. the generated coefficients are checked against
   \[
   u_n^{(-\sigma)}
   =
   (-1)^n u_n^{(\sigma)}
   \]
   for every tested order.

Test at least through \(n=8\), not merely through the three coefficients
displayed in the manuscript.

Use a genuinely complex parameter set if supported by the existing arithmetic
path. The chosen \(s\) must satisfy \(s^2=-q\).

The test must independently distinguish even and odd orders:

\[
u_{2k}^{(-\sigma)}=u_{2k}^{(\sigma)},
\]

\[
u_{2k+1}^{(-\sigma)}=-u_{2k+1}^{(\sigma)}.
\]

Do not construct the expected sequence by calling the same generator with
unchanged effective data and comparing identical outputs.

### Existing relabelling test

If the existing simultaneous transformation test is retained, rename or
document it accurately. It may verify the invariance

\[
(\sigma,s)\mapsto(-\sigma,-s),
\]

but it must not be described as the fixed-branch parity test.

The test suite must clearly distinguish:

1. fixed-branch sign parity:
   \[
   \sigma\mapsto-\sigma,\qquad s\ \text{fixed};
   \]

2. branch/sign relabelling:
   \[
   (\sigma,s)\mapsto(-\sigma,-s).
   \]

### Documentation correction

Inspect both the manuscript and

```text
docs/stage05_taylor_and_infty.md
```

Any statement of

\[
u_n^{(-\sigma)}=(-1)^n u_n^{(\sigma)}
\]

must say explicitly that the chosen value \(s=\sqrt{-q}\) is held fixed.

Do not leave the branch convention implicit.

---

## Correction 3 — Validate the caller-supplied `sqrt_minus_q`

Inspect the asymptotic coefficient generator and its public API.

The generator may currently reject

```python
sqrt_minus_q == 0
```

but still accept inconsistent input such as:

```python
q = 7
sqrt_minus_q = 123
```

although

\[
123^2\neq-7.
\]

The generator must not silently accept such obviously inconsistent data.

### Required mathematical condition

For

\[
s=\texttt{sqrt\_minus\_q},
\]

validate

\[
s^2=-q,
\]

equivalently,

\[
s^2+q=0.
\]

Do not silently replace the supplied \(s\) with a newly computed principal
square root. The caller is allowed to choose either valid branch.

### Validation contract

Preserve every arithmetic mode already supported by the generator.

Use:

- exact equality for exact values when meaningful;
- symbolic simplification or an exact symbolic zero test when the existing
  symbolic framework can decide the relation;
- a documented numerical tolerance for floating-point real or complex values;
- a clear, informative exception for demonstrably inconsistent \(q\) and \(s\).

Continue to reject \(s=0\) in the nondegenerate \(q\neq0\) asymptotic
generator.

If a symbolic relation is genuinely undecidable, do not convert the symbolic
expression blindly to `bool` and do not guess. Implement the narrowest explicit
contract compatible with the current API and document:

- which exact inputs are checked;
- which numerical inputs are checked;
- what tolerance is used;
- which symbolic cases remain the caller’s responsibility.

Do not overstate the implemented validation in documentation or the execution
log.

### Required tests

Add tests for at least:

1. one valid branch \(s\);
2. the other valid branch \(-s\);
3. an obviously inconsistent value;
4. a valid complex floating-point pair \((q,s)\);
5. a slightly rounded but acceptable numerical value within the documented
   tolerance;
6. a numerical value outside the tolerance;
7. the existing rejection of \(q=0\) or \(s=0\), as appropriate to the current
   API.

Ensure that the new validation does not accidentally force the principal
square-root branch.

---

## Correction 4 — Replace the tautological undriven-limit test with an operator test

Inspect the tests for the exactly undriven case

\[
F=\overline F=0.
\]

A test is insufficient if it:

1. defines
   \[
   E_n=\hbar\omega_0n+\frac V2n(n-1),
   \]
2. substitutes that same expression into an algebraically identical formula,
3. checks that the subtraction gives zero.

Such a test repeats the claimed formula rather than checking the differential
equation.

### Required independent test

Apply the undriven Bargmann differential operator

\[
\mathcal L_E
=
\frac V2z^2\frac{d^2}{dz^2}
+
\hbar\omega_0z\frac{d}{dz}
-
E
\]

directly to

\[
\Psi_n(z)=\frac{z^n}{\sqrt{n!}},
\]

or to \(z^n\) when normalization is irrelevant.

Then verify that

\[
\mathcal L_{E_n}\Psi_n(z)=0
\]

for

\[
E_n
=
\hbar\omega_0n+\frac V2n(n-1).
\]

Test at least:

\[
n=0,\qquad n=1,\qquad n=2,
\]

and at least two additional values with \(n>2\).

Prefer exact symbolic polynomial arithmetic or an exact coefficient-level
operator application.

Do not test the identity only at a single numerical value of \(z\).

The test should fail if any one of the following is independently perturbed:

- the coefficient of \(z\Psi'(z)\);
- the coefficient of \(z^2\Psi''(z)\);
- the \(n\)-dependence of the claimed energy.

If the repository already has a representation of the undriven Bargmann
Hamiltonian, use it only if that produces a genuinely independent application
of the operator rather than a second spelling of the energy formula.

---

## Correction 5 — Remove the ambiguity concerning orientation at infinity

Search the manuscript and technical note for wording such as:

```text
positive circuit of z about infinity
```

or any equivalent expression whose orientation is not explicitly defined.

Replace it with an unambiguous analytic continuation in the finite
\(z\)-plane:

\[
z\mapsto ze^{2\pi i},
\]

described as one counterclockwise circuit of \(z\) around the origin.

State consistently that under this continuation:

\[
\sqrt z\mapsto-\sqrt z,
\]

the two exponential expressions are interchanged or relabelled according to
the adopted fixed-branch convention, and

\[
z^r\mapsto e^{2\pi ir}z^r.
\]

Describe what happens to the half-integer formal series consistently with the
same continuation.

Do not use the phrase “positive circuit around infinity” unless its orientation
is explicitly defined, because the induced orientation around the point at
infinity is convention-dependent.

Do not expand this correction into a calculation of Stokes multipliers or
connection matrices.

---

## Consistency audit after the five corrections

After implementing the corrections, inspect the manuscript, technical note,
source, tests, and prompts together.

Confirm explicitly that they distinguish:

1. a chosen square-root branch \(s=\sqrt{-q}\);
2. the sign label \(\sigma=\pm1\);
3. the fixed-branch transformation
   \[
   \sigma\mapsto-\sigma,\qquad s\ \text{fixed};
   \]
4. the redundant relabelling
   \[
   (\sigma,s)\mapsto(-\sigma,-s);
   \]
5. the exactly degenerate point \(q=B_1=0\);
6. the limiting process \(F\to0\), which is not identical to direct
   substitution into formulas derived for \(B_1q\neq0\).

Do not introduce new claims about convergence, quantization, Stokes
multipliers, or global connection problems.

---

## Validation

Run the complete existing and new test suite.

Compile the manuscript using the repository’s established build procedure.

Inspect visually every affected PDF page, especially the pages containing:

- the formal expansion at infinity;
- the definition of \(s=\sqrt{-q}\);
- the parity relation;
- analytic continuation under \(z\mapsto ze^{2\pi i}\);
- the exactly undriven case.

Check for:

- malformed square roots;
- ambiguous branch notation;
- equation overflow;
- broken cross-references;
- misplaced equation numbers;
- inconsistent uses of \(F^*\) and \(\overline F\);
- inconsistent uses of \(s\), \(\sigma\), \(q\), and \(u_n^{(\sigma)}\).

Run:

```bash
git diff --check
```

Inspect:

```bash
git status --short
git diff --stat
```

Search the canonical Stage 05 prompt for known corruption:

```bash
rg -n 'DeriveDerive|^=======|e\^\{,|q,c_\{n-1\}' prompts
```

Also search for competing Stage 05 prompt filenames and for the ambiguous
orientation wording.

Do not weaken or remove a failing test merely to obtain a green suite.
Diagnose every failure while remaining within the strict scope of Stage 05a.

---

## Deliverables

At completion, report:

1. every file changed, added, renamed, or removed;
2. the exact final path of the canonical Stage 05 prompt;
3. whether that prompt was restored from an exact clean source or only repaired
   typographically;
4. any part of the historical prompt that could not be restored without an
   exact source;
5. the old branch/sign test and what it actually tested;
6. the new fixed-branch parity test, including the highest tested order;
7. whether the manuscript and technical note now state explicitly that \(s\)
   is fixed in the parity relation;
8. the exact `sqrt_minus_q` validation contract;
9. the numerical tolerance, if any;
10. the tests for both valid branches and inconsistent inputs;
11. the independent undriven operator test and the tested values of \(n\);
12. the exact corrected analytic-continuation wording;
13. the complete test-suite result;
14. the manuscript build result;
15. the PDF pages visually inspected;
16. the result of `git diff --check`;
17. the final `git status --short`;
18. any requested correction that could not be completed, with the precise
    reason.

Save:

```bash
git diff > stage05a_limit_corrections.diff
```

and create a concise execution log:

```text
stage05a_limit_corrections.log
```

The log must distinguish clearly between:

- checks actually performed;
- assumptions explicitly validated;
- assumptions left to the caller;
- corrections completed;
- corrections blocked by the absence of an exact historical source.

Do not stage or commit changes.

Stop after reporting the results and wait for review.
