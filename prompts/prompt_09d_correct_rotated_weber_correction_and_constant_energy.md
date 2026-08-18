# Task 09d: Correct the rotated Fedoryuk--Weber correction and derive the local constant energy term

You are working in the repository:

`~/Dokumenty/Prace_i_dnie/Wnęka_z_Kerrem`

The repository is synchronized with `origin/master`, but the working tree intentionally contains all uncommitted Stage 09a--09c changes. Preserve them and correct them in place.

Do not commit and do not push. Git operations will be performed only after the complete Stage 09 review series has been accepted.

## Scope

This is a strictly Fedoryuk--Weber correction and extension stage.

Do **not** introduce, discuss, test, or cite the Bender--Bettencourt resummation idea in this task. That idea is deliberately reserved for a later, separate manuscript section and a later prompt.

Stage 09d must:

1. remove the sign error in the first wavefunction correction for the rotated/imaginary Weber branch;
2. verify both first corrections by direct substitution into their inhomogeneous Weber equations;
3. correct the overstated residual-verification language from Stage 09c;
4. derive, if justified by the local sectorial perturbation calculation, the fixed-`n` energy coefficient of order `O(1)` for both Weber orientations;
5. keep the physical imaginary-axis assignment explicitly conditional on the Fedoryuk--Bargmann orientation hypothesis.

## Mandatory preliminary inspection

Before editing:

1. run and record `git status -sb`;
2. inspect all Stage 09a--09c prompts, documentation, scripts, tests, diffs, logs, manuscript changes, and generated figures;
3. inspect the Stage 08d--08e displaced/Bogoliubov calculation and exact formal `O(1)` coefficient, but use it only as an external check after the independent Fedoryuk derivation;
4. reproduce manually and symbolically the transformation `t=-i s` before accepting any existing rotated-branch formula;
5. preserve every unrelated user change.

## Fixed starting point

Use

\[
q=\sqrt\varepsilon=\eta^{-1/3},
\qquad
y=-1+qX,
\qquad
s=3^{1/4}X,
\]

\[
e=-\frac32+q^2e_1+q^4e_2+O(q^6).
\]

The exact scaled equation through the required order is

\[
u_{XX}=\{R_0+qR_1+q^2R_2+O(q^3)\}u,
\]

where

\[
R_0=3X^2+2(e_1+1-\delta),
\]

\[
R_1=10X^3+(4e_1+6-6\delta)X,
\]

\[
R_2=22X^4+(6e_1+12-12\delta)X^2
+\delta^2-\delta+2e_2.
\]

Re-derive and verify these formulas; do not merely copy them.

## A. Correct the rotated first-order equation

For the real branch, retain

\[
e_{1,n}^{(R)}=\delta-1-\sqrt3\left(n+\frac12\right).
\]

In the normalized coordinate `s`, write the first perturbation as

\[
V_{1,R}(s)=A s^3+B_Rs,
\]

with `A` and `B_R` derived exactly.

For the rotated branch, use

\[
t=-is,
\qquad s=it,
\qquad
e_{1,n}^{(I)}=\delta-1+\sqrt3\left(n+\frac12\right).
\]

Derive the transformed differential equation including all signs from:

\[
\frac{d^2}{ds^2}=-\frac{d^2}{dt^2},
\qquad
s^3=-it^3,
\qquad
s=it.
\]

The result must be equivalent, in a clearly declared convention, to an odd rotated perturbation containing the relative combination

\[
i\left(A t^3-B_I t\right),

\]

not a common phase multiplying `A t^3+B_I t`.

Track separately:

- the perturbation as it appears on the right-hand side of the differential equation;
- the perturbation after rewriting the problem in harmonic-oscillator operator form;
- the sign in the coefficient formula for `u1`.

Do not reuse the Stage 09c statement that every matrix element is simply multiplied by `-i`.

## B. Derive and verify both first wavefunction corrections

Use

\[
u=u_0+qu_1+q^2u_2+\cdots

\]

with intermediate normalization in the appropriate bilinear form.

For the real branch:

1. derive the inhomogeneous equation for `u_(1,R)`;
2. expand it in the Hermite basis;
3. compute explicitly the coefficients for shifts `j=-3,-1,1,3`;
4. omit negative-index states;
5. verify the intermediate-normalization condition.

For the imaginary branch:

1. derive the inhomogeneous equation on the `t` contour independently;
2. use the corrected relative sign between the cubic and linear matrix elements;
3. compute explicit coefficients for every allowed shift;
4. state the contour orientation and bilinear normalization convention;
5. do not import a real-axis Hermitian inner product without analytic justification.

The verification must not stop at confirming the set of shifts. Symbolically substitute each proposed finite Hermite sum into the complete order-`q` inhomogeneous equation and prove that the residual is identically zero for symbolic `n` where possible. If symbolic `n` makes boundary cases awkward, prove a general coefficient identity and separately test several values including `n=0,1,2,3,4`.

Add exact tests for:

- every matrix element of `s`, `s^3`, `t`, and `t^3` used;
- the real correction coefficients;
- the rotated correction coefficients;
- the relative cubic/linear sign after rotation;
- the order-`q` inhomogeneous equation for both branches;
- vanishing diagonal solvability at order `q`.

## C. Clarify the residual calculation

Stage 09c described the numerical check too broadly as a residual of the complete local wavefunction. The existing code essentially verifies

\[
R(X,q)-R_0(X)=O(q),

\]

equivalently the differential-equation residual divided by `u0` away from zeros of `u0`.

Correct the documentation, log, docstrings, and manuscript wording wherever necessary.

Provide two distinct checks:

1. **Coefficient truncation check:** verify `R-R0=O(q)` exactly and numerically.
2. **Wavefunction residual check:** substitute
   \[
   u^{[1]}=u_0+qu_1
   \]
   into the exact scaled equation and verify that the absolute residual is `O(q^2)` on compact subsets of the relevant scaled sector.

For relative residuals, exclude or separately handle zeros of the Hermite factor. State exactly what denominator is used.

Perform the wavefunction-residual check for both orientations and several fixed values of `n` and `delta`.

## D. Derive the local `O(1)` energy coefficient

At order `q^2`, derive the solvability condition for `e2` independently for each orientation.

Include all contributions:

1. the direct even perturbation `R2`;
2. the `e2` term;
3. the second-order iteration of the odd `R1` perturbation through `u1`;
4. all signs caused by the `t=-is` rotation;
5. the normalization/bilinear convention appropriate to the chosen contour.

Do not infer `e2` by copying the Stage 08 result.

Give explicit formulas

\[
e_{2,n}^{(R)}(\delta),
\qquad
e_{2,n}^{(I)}(\delta),

\]

if both local sector problems yield well-defined solvability conditions.

Then compare the imaginary-orientation result with the independently established Stage 08 formal coefficient

\[
\frac{\delta(1-2\delta)}6-
\frac{6n^2+6n+1}{72}.

\]

Agreement is a consistency check only. If there is disagreement, stop and diagnose it rather than altering signs to force agreement.

The candidate local energies should be stated as

\[
\frac{E_{n,\sigma}}V
=
-\frac32\eta^{4/3}
+e_{1,n}^{(\sigma)}\eta^{2/3}
+e_{2,n}^{(\sigma)}
+O(\eta^{-2/3}),
\qquad \sigma=R,I,

\]

only to the extent supported by the local calculation.

Maintain the classification:

- real-axis formula: a local Weber-sector result;
- imaginary-axis formula: a local result and a conditional physical candidate under the Fedoryuk--Bargmann orientation hypothesis;
- neither formula: an unconditional Bargmann spectral theorem.

If the contour-bilinear solvability at order `q^2` cannot be justified, do not fabricate `e_(2,n)^(I)`. State precisely what additional connection or bilinear theorem is needed.

## E. Improve the Fedoryuk presentation

Update `docs/fedoryuk_weber_wavefunction_and_energy.md` so that:

- the corrected rotated `u1` is explicit;
- the sign derivation is displayed, not merely asserted;
- both inhomogeneous equations are stated;
- the residual terminology is exact;
- the `O(1)` energy coefficient is included only if justified;
- the distinction between local normalization, contour bilinear form, and Bargmann norm remains explicit.

Update the manuscript concisely:

1. correct any statement about the rotated first correction;
2. include the `O(1)` candidate energy only if verified;
3. retain the named orientation hypothesis;
4. retain the warning that the global canonical-domain chain and Bargmann assignment remain open;
5. do not add internal workflow terminology;
6. do not mention Bender or Bettencourt in this subsection.

Avoid wide equations and visually inspect all affected pages.

## F. Verification architecture

Extend `scripts/09c_verify_fedoryuk_weber.py` or create a narrowly focused `scripts/09d_...` verifier if this keeps the logic clearer. In either case, keep all earlier checks working.

The verifier must expose, not merely print:

- `A`, `B_R`, and `B_I`;
- both order-`q` perturbation operators;
- every nonzero Hermite matrix element;
- explicit `u1` coefficients for both branches;
- exact order-`q` residual identities;
- the order-`q^2` solvability expressions;
- `e2_R` and `e2_I`, if derived;
- the exact difference between `e2_I` and the Stage 08 consistency target.

Tests must fail if the cubic and linear terms in the rotated perturbation are accidentally assigned the same relative sign.

## Deliverables

Create or update:

1. `docs/fedoryuk_weber_wavefunction_and_energy.md`
2. the relevant Stage 09c/09d symbolic verifier script or scripts;
3. the relevant Stage 09c/09d tests;
4. `manuscript/manuscript.tex`
5. `prompt_09d_correct_rotated_weber_correction_and_constant_energy.diff`
6. `prompt_09d_correct_rotated_weber_correction_and_constant_energy.log`

Do not create a Bender--Bettencourt document, subsection, bibliography entry, or exploratory script in this task.

The log must contain:

- initial and final `git status -sb`;
- files inspected;
- exact files changed or created;
- the full `s -> t` sign ledger;
- corrected `u1_R` and `u1_I` coefficients;
- exact substitution results for both order-`q` equations;
- coefficient-truncation and wavefunction-residual results;
- complete order-`q^2` solvability calculations;
- `e2_R` and `e2_I`, or a precise explanation of why either is not justified;
- comparison with the Stage 08 consistency target;
- tests run and results;
- LaTeX/Biber compilation result;
- rendered pages inspected;
- unresolved local and global assumptions;
- confirmation that no commit and no push were performed.

## Required commands

Run at least:

```bash
python scripts/09a_verify_fedoryuk_normal_form.py
python scripts/09c_verify_fedoryuk_weber.py
PYTHONPATH=src pytest -q
git diff --check
```

Run any additional Stage 09d verifier explicitly.

Compile the manuscript using the established repository procedure. Render and inspect every affected page, including one page before and one page after the changed range.

At the end report clearly:

1. the corrected rotated perturbation and corrected `u1_I`;
2. whether both order-`q` substitutions vanish identically;
3. the true residual orders for `u0` and `u0+q u1`;
4. the independently derived `e2_R` and `e2_I`;
5. whether `e2_I` agrees with Stage 08;
6. which statements remain conditional on the orientation hypothesis;
7. what global Fedoryuk problem remains for a later stage.

Do not commit and do not push.
