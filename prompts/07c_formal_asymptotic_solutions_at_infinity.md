# Stage 07c — Formal asymptotic solutions at infinity

## Repository and working rules

Work in the existing local repository:

```text
~/Dokumenty/Prace_i_dnie/Wnęka_z_Kerrem
```

Inspect the repository, the current manuscript, the notation already used in the relevant asymptotic section, and the completed stages 07a–07b before editing anything. Follow the existing directory and naming conventions.

Do not stage, commit, push, reset, restore, clean, initialize, clone, or change any Git remote. The user alone performs commits and pushes.

## Goal

Derive, verify, and present the two **formal asymptotic solutions** of the Bargmann eigenvalue equation near (z=\infty), on the two-sheeted covering (z=t^2). Determine the algebraic prefactor, a recurrence for all formal coefficients, the first few coefficients, and the transformation under (t\mapsto -t).

This stage is strictly formal and local at infinity. Do not claim existence of actual analytic solutions with these expansions, do not prove remainder estimates, and do not address the global connection or spectral problem.

## Mathematical setting

Use the equation and notation currently present in the manuscript. In particular, verify that the working equation is

\[
z^2\Psi''(z)+(B_1+B_2z)\Psi'(z)+(B_3+qz)\Psi(z)=0,
\qquad q\ne0,
\]

with

\[
B_1=\frac{2\overline F}{V},\qquad
B_2=\frac{2\hbar\omega_0}{V},\qquad
B_3=-\frac{2E}{V},\qquad
q=\frac{2F}{V}.
\]

If the current manuscript uses an equivalent but notationally different form, preserve its notation and explicitly document the translation. Do not silently overwrite an established convention.

Introduce

\[
z=t^2,\qquad s^2=-q,
\]

and write

\[
Y(t)=\Psi(t^2).
\]

First derive the transformed differential equation directly by the chain rule and check it independently. It should reduce to

\[
Y''(t)+\left(\frac{2B_2-1}{t}+\frac{2B_1}{t^3}\right)Y'(t)
+\left(4q+\frac{4B_3}{t^2}\right)Y(t)=0.
\]

Do not assume this displayed formula without verification.

## Formal ansatz

Seek two formal solutions in the form

\[
Y_\sigma(t)\sim
e^{\lambda_\sigma t}t^\rho
\sum_{n=0}^{\infty}c_n^{(\sigma)}t^{-n},
\qquad
\lambda_\sigma=2\sigma s,
\qquad \sigma\in\{+1,-1\},
\]

with normalization

\[
c_0^{(\sigma)}=1.
\]

Equivalently, on a chosen sheet in the (z)-variable,

\[
\Psi_\sigma(z)\sim
e^{2\sigma\sqrt{-qz}}z^{\rho/2}
\sum_{n=0}^{\infty}c_n^{(\sigma)}z^{-n/2}.
\]

Derive rather than assume the value of (\rho). Verify whether

\[
\rho=\frac12-B_2
\]

is correct. State clearly that (t^\rho), and hence (z^{\rho/2}), requires a branch choice when (\rho\notin\mathbb Z).

## Recurrence

Derive a recurrence valid for all (n\ge1). For checking purposes, introduce only locally if useful

\[
A=2B_2-1,\qquad C=2B_1,\qquad D=4B_3,
\]

so that (\rho=-A/2). Independently verify that the coefficient recurrence is equivalent to

\[
2\lambda_\sigma n c_n^{(\sigma)}=
\Big[(\rho-n+1)(\rho-n)+A(\rho-n+1)+D\Big]c_{n-1}^{(\sigma)}
+\lambda_\sigma Cc_{n-2}^{(\sigma)}
+C(\rho-n+3)c_{n-3}^{(\sigma)},
\]

where

\[
c_{-1}^{(\sigma)}=c_{-2}^{(\sigma)}=0.
\]

Do not copy this recurrence into the manuscript unless a direct substitution confirms every index and sign. Simplify it if doing so improves clarity without hiding parameter dependence.

Compute and display at least (c_1^{(\sigma)},c_2^{(\sigma)},c_3^{(\sigma)}), preferably in a compact recurrence-generated form rather than as unreadably expanded expressions. Check them by substituting the truncated series back into the transformed equation and reporting the order of the residual.

## Sheet exchange and sector interpretation

Explain precisely what happens under

\[
t\mapsto -t.
\]

This exchange lies above the same point (z=t^2) and swaps the exponential factors:

\[
e^{2st}\longleftrightarrow e^{-2st}.
\]

Track also the algebraic factor and coefficient series. Do not state merely that (Y_+(-t)=Y_-(t)) unless this equality follows with the chosen normalizations and branches. Give the exact formal relation, including any phase from ((-t)^\rho) and the parity dependence of (t^{-n}).

Relate the two formal solutions to the equal-modulus and constant-phase geometry established in stages 07a–07b, but do not redo or modify the figure unless a genuine inconsistency is found. Distinguish clearly between:

- formal exponential dominance in a selected sector and on a selected sheet;
- the existence of an actual solution having the formal expansion;
- Bargmann-space integrability;
- a global spectral or quantization condition.

Only the first item belongs to this stage.

## Verification requirements

Perform at least two independent algebraic checks, for example:

1. a hand-derived coefficient collection documented in the note or report;
2. a symbolic substitution using SymPy or another available computer-algebra tool;
3. a direct residual check for several generic numerical parameter values with (q\ne0), avoiding singular or accidentally simplifying choices.

The computer-algebra check must verify the mathematics; it must not replace the derivation. Record exact commands, assumptions, and results in the final log.

Check explicitly:

- the chain-rule transformation (z=t^2);
- the characteristic equation for (\lambda_\sigma);
- the equation determining (\rho);
- every shift and sign in the recurrence;
- the first three nontrivial coefficients;
- the sheet-exchange statement;
- consistency with the notation and claims already present in the manuscript.

## Manuscript changes

Add a concise, publication-quality subsection or continuation to the existing Olver/asymptotic discussion. It should include:

- the (t)-plane equation;
- the formal ansatz;
- the value of the algebraic exponent;
- the coefficient recurrence;
- the first few coefficients or a compact specification of them;
- a careful statement about (t\mapsto -t);
- an explicit warning that these are formal solutions only.

Do not call a divergent formal series a convergent series. If convergence or Gevrey order is not proved, make no claim about it.

Do not attribute a theorem to Olver without identifying the precise theorem and checking all hypotheses. The theorem on actual solutions and remainder estimates belongs to stage 07d, not 07c.

## Supporting note

Create a short Markdown note, following existing conventions, containing the full derivation in more detail than the manuscript. It must be possible to audit the recurrence from this note alone.

If a reusable symbolic verification script is created, place it in the existing scripts directory, make it deterministic, and document how to run it. Do not create a script merely to inflate the deliverables if a transparent reproducible command is sufficient.

## Build and visual inspection

Rebuild the complete manuscript using the repository's established build procedure. Inspect the build log for errors, undefined references, bibliography failures, overfull boxes, and relevant warnings.

Render and visually inspect every changed manuscript page. Correct clipped equations, poor line breaks, overfull displays, inconsistent notation, or unreadably long recurrence formulas. Confirm that the bibliography remains consistently formatted with initials only, as established in stage 07b.

## Review artifacts

Create, following the repository's naming conventions:

1. `prompt_07c_formal_asymptotic_solutions_at_infinity.diff`

   A unified diff representing the final changes to all tracked files and the complete contents of all newly created text files. Generate it non-destructively from the actual final working tree. Do not stage files merely to generate the diff.

2. `prompt_07c_formal_asymptotic_solutions_at_infinity.log`

   A complete final report containing:

   - repository path and final `git status -sb`;
   - every created, modified, or deleted file and its purpose;
   - the exact transformed equation;
   - the derived values of (\lambda_\sigma) and (\rho);
   - the final recurrence and first three nontrivial coefficients;
   - the exact sheet-exchange relation;
   - all symbolic or residual checks, commands, assumptions, and results;
   - manuscript build commands and results;
   - warnings and whether they are new or pre-existing;
   - pages visually inspected and corrections made after inspection;
   - limitations and unresolved questions reserved for stage 07d;
   - confirmation that no prohibited method or computation was introduced.

Before finishing, verify that both files exist, are nonempty, and describe the final rather than an intermediate state.

## Strict exclusions

Do not:

- calculate or approximate eigenvalues;
- formulate a quantization condition;
- introduce a spectral determinant or a function such as (D(E));
- use continued fractions in any form, including as a benchmark;
- calculate Stokes multipliers;
- solve or claim to solve the connection problem;
- construct a global connection matrix;
- prove existence of actual sectorial solutions;
- claim an error bound or remainder estimate without proof;
- invoke the stage-07d theorem prematurely;
- decide Bargmann-space admissibility from exponential dominance alone;
- derive eigenvalue asymptotics;
- introduce artificial large-parameter scaling;
- discuss or use Fedoryuk's method;
- add numerical spectral experiments, diagonalization, iterative maps, or dynamical-system plots;
- modify the Stokes-geometry figure unless a genuine error is found and fully reported;
- alter unrelated sections or bibliography formatting;
- stage, commit, push, reset, restore, clean, or otherwise alter Git history or index state.

## Final response

In the final interactive response, reproduce the essential mathematical and validation results from the `.log`, list all changed and created files, give the paths of the `.diff` and `.log`, and explicitly confirm compliance with every strict exclusion.
