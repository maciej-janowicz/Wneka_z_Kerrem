# Prompt 08a — Strong-drive Olver comparison problem, quantization, and energy asymptotics

## Repository and working rules

Work in the existing local repository:

```text
~/Dokumenty/Prace_i_dnie/Wnęka_z_Kerrem
```

Inspect the current repository, manuscript, bibliography, tests, scripts, and all relevant documentation before editing. Preserve the notation and equation numbering already established unless a change is mathematically necessary and explicitly documented.

Do not stage, commit, push, reset, restore, clean, initialize, clone, or change any Git remote. The user alone performs commits and pushes.

This task is time-boxed to approximately 90 minutes. Mathematical correctness takes precedence over apparent completeness. If a requested global claim cannot be proved from the available theory within the time box, state the strongest rigorously supported conditional result and record the precise missing step. Never fill a gap with an unsupported assertion.

## Overall goal

Complete the manuscript's Olver-methodology discussion for the strongly driven Kerr oscillator by addressing, in one logically coherent development:

1. a uniform approximate solution obtained through the correct Olver comparison equation;
2. an Olver/Stokes connection formulation of the quantization condition;
3. the strong-drive expansion of the quantized energies in the appropriate powers of \(|F|/V\);
4. removal from the manuscript of all references to internal working-stage names.

The new analysis must not use continued fractions, direct Hamiltonian-matrix diagonalization, or an unverified numerical spectral fit.

## Physical regime and phase reduction

The relevant experimental regime is

\[
\eta:=\frac{|F|}{V}\longrightarrow\infty,
\qquad
\delta:=\frac{\hbar\omega_0}{V}\quad\text{fixed}.
\]

Use the already established unitary phase equivalence to reduce the physical problem to \(F=|F|>0\) for the derivation. State how the result is transported back to arbitrary \(\arg F\). On this positive-drive slice verify

\[
B_1=q=2\eta,
\qquad B_2=2\delta,
\qquad B_3=-2\frac EV.
\]

Do not reuse a manuscript symbol already assigned to the dimensionless DCHE energy. In particular, inspect the current notation before naming the scaled strong-drive energy. A neutral symbol such as \(e\) may be used if it creates no collision.

## Exact covering equation

Begin from the exact normal-form covering equation already derived in the manuscript. Independently verify that it can be written as

\[
w''(t)=
\left[
-8\eta-\frac{C}{t^2}
-\frac{8\eta(1-\delta)}{t^4}
+\frac{4\eta^2}{t^6}
\right]w(t),
\]

where

\[
C=-8\frac EV+4\delta-4\delta^2-\frac34.
\]

Check all signs directly from the manuscript definitions

\[
D=B_3+\frac{B_2}{2}-\frac{B_2^2}{4},
\qquad
H=B_1\left(1-\frac{B_2}{2}\right),
\qquad
C=4D-\frac34.
\]

Do not proceed from the displayed target formula unless the independent derivation agrees.

## Strong-drive scaling and large parameter

Derive rather than assume the distinguished scaling

\[
t=\eta^{1/6}x,
\qquad
\frac EV=\eta^{4/3}e,
\qquad
u=\eta^{2/3}.
\]

Verify that the exact equation becomes

\[
\frac{d^2w}{dx^2}
=\left[u^2 f(x;e)+u\,g(x)+h(x)\right]w,
\]

with

\[
f(x;e)=\frac4{x^6}+\frac{8e}{x^2}-8,
\]

\[
g(x)=-\frac{8(1-\delta)}{x^4},
\qquad
h(x)=\frac{4\delta^2-4\delta+\tfrac34}{x^2}.
\]

Verify all powers of \(\eta\) symbolically and by direct substitution. Explain why the natural expansion parameter after extracting the leading energy scale is

\[
u^{-1}=\eta^{-2/3},
\]

not \(\eta^{-1}\) and not a small-\(\eta\) Taylor series.

## Turning-point geometry and choice of comparison equation

Put \(y=x^2\). The turning-point equation for the leading coefficient is

\[
1+2e\,y^2-2y^3=0.
\]

Derive the double-root condition. Verify that the real strong-drive value

\[
e_0=-\frac32
\]

gives

\[
1-3y^2-2y^3=-(y+1)^2(2y-1),
\]

so that the relevant pair of turning points coalesces at

\[
x=+i\quad\text{and, on the symmetry-related sheet,}\quad x=-i.
\]

Audit the Stokes geometry and identify which coalescing pair and which contour correspond to the physical low-lying eigenvalue problem at fixed \(n\) as \(\eta\to\infty\). Do not infer the physical contour merely from a real-axis Schrödinger analogy; justify it from the Bargmann equation, its sheets, and the analyticity condition.

The expected Olver comparison problem for two coalescing simple turning points is the Weber/parabolic-cylinder equation. Verify this against a precise theorem or construction in Olver or another primary authoritative source already present in or legitimately added to the bibliography. Check every hypothesis and state the applicable complex domains.

Do not force a Bessel comparison equation if the turning-point classification requires parabolic-cylinder functions.

## Role of the modified-Bessel comparison

Retain and clarify the useful outer comparison equation

\[
w_0''=\left(a^2-\frac{C}{t^2}\right)w_0,
\qquad a^2=-8\eta,
\]

whose solutions can be written as

\[
\sqrt t\,I_\nu(at),
\qquad
\sqrt t\,K_\nu(at),
\qquad
\nu^2=\frac14-C
=8\frac EV+(2\delta-1)^2.
\]

Check the transformation and Wronskian directly. Explain that in the strong-drive scaling both \(at\) and \(\nu\) are of order \(u=\eta^{2/3}\), generally with complex argument and order.

However, explicitly verify that the omitted term \(4\eta^2/t^6\) is leading order when \(t=\eta^{1/6}x\). Consequently, the Bessel equation is an outer approximation at infinity, not by itself a uniform global comparison equation for the strong-drive quantization region.

Use Bessel functions only where their error-control hypotheses are satisfied. If used for outer matching, distinguish:

1. the error between the exact solution and the Bessel comparison solution;
2. the intrinsic truncation error in the large-order/large-argument Bessel expansion.

Do not combine these two errors into an unjustified single \(O(\cdot)\) statement.

## Uniform comparison solution and error bounds

Construct the appropriate Olver transformation from the scaled equation to a Weber/parabolic-cylinder comparison equation in a domain containing the relevant coalescing turning-point pair and the progressive paths needed for matching.

The manuscript must state explicitly:

- the comparison variable and its branch;
- the comparison parameter;
- the canonical parabolic-cylinder solutions selected in each sector;
- the mapping of the original Stokes curves to the comparison problem;
- the domain of uniform validity;
- whether the estimate is absolute, relative, or expressed using modulus/weight/envelope functions;
- the exact error-control integral or variation whose finiteness is required;
- a concrete bound, not merely the phrase "with a controlled error".

Relative-error claims must not be made across zeros of the comparison solution. Use an absolute bound or appropriate Olver modulus and weight functions there.

If a complete explicit bound cannot be obtained in the time box, give the precise transformed remainder and the exact error-control integral whose evaluation remains, and label the approximation conditional. Do not call it a theorem with proved error bounds unless the proof is actually supplied.

## Quantization condition

Formulate quantization in a way appropriate to this Bargmann problem.

The Gaussian Bargmann weight does not select only one of the two infinity exponentials, because both have growth \(\exp(O(|z|^{1/2}))\). Therefore, do not impose quantization merely by discarding the exponentially dominant infinity branch.

The physical condition is the existence of a single-valued entire solution at the irregular origin, equivalently the cancellation of the inadmissible essential-singular/Stokes component, together with the already established Bargmann-growth result.

Using the canonical Olver solutions and their connection data:

- define precisely the relevant sectorial solutions near the irregular origin;
- identify every Stokes multiplier or connection coefficient that must vanish for the normalized formal regular branch to patch to a holomorphic germ;
- state whether one scalar condition suffices or whether several conditions are required before physical conjugation or symmetry is used;
- prove any reduction to a single real condition on the physical slice;
- express the quantization condition as the vanishing of a correctly normalized Wronskian, connection coefficient, Stokes multiplier, or determinant only after proving that its zeros are exactly the eigenvalues;
- state its dependence on normalization and show that its zero set is normalization-independent.

Do not claim to have evaluated a Stokes multiplier or global connection coefficient if it has only been defined. An implicit but exact condition is acceptable; an invented explicit formula is not.

Relate the new condition to the already proved entireness/Bargmann spectral formulation, but do not use the manuscript's continued-fraction representation in the derivation or as a numerical check.

## Strong-drive energy quantization

For fixed level index \(n\) and \(\eta\to\infty\), seek

\[
\frac{E_n}{V}
\sim e_{n,0}\eta^{4/3}
+e_{n,1}\eta^{2/3}
+e_{n,2}
+e_{n,3}\eta^{-2/3}+\cdots.
\]

Derive from the turning-point/Weber quantization condition every coefficient that can be justified within the time box. At minimum, rigorously derive or clearly mark as conditional the expected first two coefficients

\[
e_{n,0}=-\frac32,
\]

\[
e_{n,1}
=\delta+\sqrt3\left(n+\frac12\right)-1.
\]

Do not present these as proved by Olver merely because they agree with an independent physical calculation. Show exactly how the double-turning-point condition gives \(e_{n,0}\) and how the parabolic-cylinder quantization parameter gives \(e_{n,1}\).

As an independent check only, displace the oscillator by the real amplitude \(r>0\) satisfying

\[
r^3+\delta r=\eta
\]

and perform the quadratic Bogoliubov analysis. Verify that it produces

\[
\frac{E_n}{V}
=-\frac32\eta^{4/3}
+\left[\delta+\sqrt3\left(n+\frac12\right)-1\right]\eta^{2/3}
+O(1).
\]

This operator calculation is a consistency check, not a substitute for the Olver derivation.

If the \(O(1)\) coefficient is computed, include all contributions of the cubic and quartic fluctuation terms; the quadratic Bogoliubov Hamiltonian alone is insufficient at that order. Otherwise retain an honest \(O(1)\) remainder.

State explicitly that the expansion is for fixed \(n\). Do not claim uniformity for \(n\) growing with \(\eta\) without a separate double-scaling analysis.

## Removal of internal workflow language

Search the complete manuscript source, captions, footnotes, headings, appendices, and bibliography-related text for case-insensitive occurrences of internal workflow language, including at least:

```text
Stage
stage
Stage 05
next stage
prompt
07a
07b
07c
08a
```

Remove or replace every such occurrence in the manuscript. Known examples in the current PDF include:

- "This reproduces exactly the Stage 05 exponential rate ...";
- "... the same ... as the Stage 05 recurrence";
- "The next stage will remain within Olver's framework ...".

Replace them by timeless mathematical cross-references such as "the direct formal expansion", "recurrence (54)", or "the subsequent connection analysis".

Internal stage names may remain in filenames under `prompts/`, review artifacts, development notes, and logs. They must not appear in the publication manuscript or rendered PDF.

At the end run a case-insensitive search proving that the rendered manuscript contains no occurrence of `Stage` and that the source contains no internal prompt identifier in publication text.

## Literature discipline

Use primary and authoritative sources only for technical claims. Identify the exact Olver theorem, section, or comparison-equation construction used. Verify applicability to complex variables, complex order/argument, coalescing turning points, and the domains actually claimed.

Do not cite a general chapter as though it automatically proves this specialized result. Do not use Fedoryuk's method. Preserve the bibliography convention of initials only for personal authors and editors.

## Reproducible verification

Create a deterministic symbolic verification script if appropriate, following repository conventions. It should check at least:

- the physical-parameter substitution;
- the exact covering equation;
- the \(t=\eta^{1/6}x\) scaling;
- the functions \(f,g,h\);
- the double-root condition at \(e=-3/2\);
- the Bessel order identity \(\nu^2=8E/V+(2\delta-1)^2\);
- every algebraic step used for the first two energy coefficients;
- the independent displaced-oscillator/Bogoliubov check.

Use exact symbolic arithmetic where possible. Numerical examples may supplement but not replace exact checks. Do not diagonalize a truncated Hamiltonian matrix.

Run the complete existing regression suite after the changes.

## Manuscript integration

Integrate the new material into the existing Olver discussion without duplicating the current fixed-parameter theorem. Clearly distinguish:

- fixed-parameter asymptotics at \(z=\infty\);
- strong-drive uniform asymptotics with \(u=\eta^{2/3}\);
- outer Bessel matching;
- the coalescing-turning-point comparison problem;
- the exact implicit quantization condition;
- the derived strong-drive energy expansion.

Do not leave contradictory claims about which comparison equation is uniform in which region. Update the abstract, introduction, conclusion, or roadmap only if necessary to keep their claims accurate.

## Build and visual inspection

Rebuild the complete manuscript with the repository's established procedure. Inspect the final LaTeX and bibliography logs for errors, undefined references, bibliography failures, overfull or underfull boxes, and new warnings.

Render and visually inspect every modified manuscript page and its neighboring pages. Correct clipped equations, overly dense displays, broken page transitions, inconsistent notation, and unreadable quantization formulas. Confirm that all fonts are embedded and that the bibliography still uses initials consistently.

## Deliverables

Create or modify, following repository conventions:

1. the manuscript source;
2. any necessary verified bibliography entries;
3. a detailed Markdown derivation note;
4. deterministic symbolic verification code and tests, if appropriate;
5. the rebuilt manuscript PDF;
6. the prompt copy under `prompts/`;
7. the two review artifacts specified below.

## Review artifacts

Create:

```text
prompt_08a_strong_drive_olver_comparison_quantization.diff
prompt_08a_strong_drive_olver_comparison_quantization.log
```

The `.diff` must be a unified diff of the complete final change set, including the full contents of every newly created text file. Generate it non-destructively from the final working tree. Do not stage files to create it.

The `.log` must contain the complete final report, including:

- repository path and final `git status -sb`;
- every created, modified, or deleted file and its purpose;
- all exact scalings and parameter definitions;
- the verified turning-point factorization and geometry;
- the selected comparison equation and the precise reason for selecting it;
- the role and limitations of the outer Bessel comparison;
- the exact approximation and error bound, or the precise unproved remainder if conditional;
- the exact quantization condition and its normalization;
- which connection coefficients were actually computed and which were only defined;
- every derived energy coefficient and its domain of validity;
- the displaced-oscillator consistency check;
- all symbolic commands and outputs;
- all regression-test commands and results;
- build commands, warnings, and results;
- pages rendered and visually inspected;
- the exact results of the searches for forbidden internal workflow language;
- all limitations and unresolved mathematical steps;
- confirmation that no continued fraction, matrix diagonalization, Fedoryuk analysis, or prohibited Git operation was used.

Verify that both review artifacts exist, are nonempty, and describe the final rather than an intermediate state.

## Strict exclusions

Do not:

- assume \(|F|/V\ll1\);
- expand about \(F=0\);
- treat \(4\eta^2/t^6\) as a small perturbation in the strong-drive turning-point region;
- force a Bessel comparison where the Olver classification requires a Weber/parabolic-cylinder model;
- discard an infinity solution merely because it is exponentially dominant;
- invent or claim to evaluate an uncomputed Stokes multiplier or connection coefficient;
- claim an explicit global quantization formula without proving equivalence to entireness and Bargmann admissibility;
- use continued fractions in any form, including as a benchmark;
- use direct or truncated Hamiltonian-matrix diagonalization;
- use Padé or Hermite-Padé approximants as a substitute for the Olver analysis;
- use Fedoryuk's method;
- introduce an artificial large parameter unrelated to \(\eta=|F|/V\);
- claim fixed-\(n\) results to be uniform for growing \(n\);
- hide an incomplete proof behind numerical agreement;
- leave any internal stage or prompt identifier in the publication manuscript;
- stage, commit, push, reset, restore, clean, or otherwise alter the Git index or history.

## Final interactive response

The final response must summarize the actual mathematical status, not merely the intended result. It must list all files changed or created, state the comparison equation and error bound, reproduce the quantization condition and derived energy coefficients, distinguish proved from conditional claims, give the paths of the `.diff` and `.log`, report the build and visual inspection, confirm removal of internal workflow language, and confirm compliance with every strict exclusion.
