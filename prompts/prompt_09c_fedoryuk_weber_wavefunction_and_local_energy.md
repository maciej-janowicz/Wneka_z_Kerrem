# Task 09c: Fedoryuk--Weber wavefunction and local strong-drive energy

You are working in the repository:

`~/Dokumenty/Prace_i_dnie/Wnęka_z_Kerrem`

The repository is synchronized with `origin/master`, but the working tree intentionally contains the uncommitted Stage 09a--09b changes. Preserve them and build on them in place.

Do not commit and do not push. Git operations will be performed only after the complete Stage 09 review series has been accepted.

## Scientific purpose

Stages 09a--09b established the exact direct Fedoryuk normal form

\[
\varepsilon^2u_{yy}
=
\{Q_0(y,e)+\varepsilon Q_1(y)+\varepsilon^2Q_2(y)\}u,
\qquad
\varepsilon=\eta^{-2/3},
\]

where

\[
Q_0(y,e)=\frac{P(y;e)}{y^4},
\qquad
P(y;e)=1+2ey^2-2y^3,
\]

\[
Q_1(y)=\frac{2(\delta-1)}{y^3},
\qquad
Q_2(y)=\frac{\delta(\delta-1)}{y^2},
\]

and

\[
\eta=\frac{|F|}{V},
\qquad
\delta=\frac{\hbar\omega_0}{V},
\qquad
\frac{\mathcal E}{2}=\frac{E}{V}=\eta^{4/3}e.
\]

At

\[
y_0=-1,
\qquad
e_0=-\frac32,
\]

two turning points of `Q0` coalesce, while `y=1/2` remains a simple turning point.

Stage 09b correctly classified the result only as:

> **Outcome A: a verified sectorial Fedoryuk applicability framework.**

The purpose of 09c is to go beyond geometry and construct:

1. the leading local uniform Fedoryuk--Weber approximation near the coalescing pair;
2. its explicit pullback to an approximate Bargmann wavefunction `Psi_n(z)`;
3. the local Weber connection zeros and the corresponding candidate strong-drive energy through the `eta^(2/3)` term;
4. if the calculation can be completed without hidden global assumptions, the first correction to the local Weber wavefunction.

This is still a local/sectorial calculation. Do not claim that a local Weber zero is a physical Bargmann eigenvalue until the missing global canonical-domain connection has been proved.

## Mandatory preliminary inspection

Before editing:

1. run and record `git status -sb`;
2. inspect all Stage 08 strong-drive material, especially:
   - `docs/strong_drive_olver_comparison.md`;
   - `docs/global_olver_connection.md`;
   - prompts 08c, 08d, and 08e;
   - the 08d and 08e reports, scripts, tests, logs, and diffs;
3. inspect all Stage 09a--09b files, including the corrected normal-form verifier, geometry code, documentation, manuscript section, prompts, diffs, and logs;
4. locate the exact Stage 08 formulas for:
   - the local Weber coordinate;
   - the parabolic-cylinder index;
   - the formal energy coefficient of `eta^(2/3)`;
   - the pullback to the Bargmann function;
5. inspect the displaced/Bogoliubov operator calculation and its phase convention;
6. preserve all existing user changes.

Do not copy the Stage 08 energy coefficient into the Fedoryuk derivation. Use Stage 08 only as an external check after the independent direct calculation.

## Fixed conventions and terminology

- Keep the Kerr coefficient `V/2`.
- Keep `V>0`.
- Use `F=|F|>0` only after explicitly invoking the established unitary phase rotation.
- Use `eta=|F|/V` and `epsilon=eta^(-2/3)`.
- Keep `mathcal E=2E/V` distinct from every epsilon symbol.
- In Polish discussion, use **separatrysa**, plural **separatrysy**. The manuscript remains in English.
- Do not put internal labels such as “Stage 09c” into the scientific manuscript.
- Do not use matrix diagonalization, continued fractions, Padé approximants, or an assumed exact Heun determinant as a derivation.

## A. Derive the close-pair scaling directly

Starting only from the exact Fedoryuk normal form, set

\[
e=e_0+\varepsilon e_1+\varepsilon^2e_2+\cdots,
\qquad
y=-1+\varepsilon^{1/2}X.
\]

Expand the complete coefficient

\[
Q_0(y,e)+\varepsilon Q_1(y)+\varepsilon^2Q_2(y)
\]

in powers of `epsilon^(1/2)` to sufficient order to identify:

1. the leading Weber equation;
2. the first perturbation of the Weber equation;
3. which terms are odd and which are even in the local coordinate;
4. where `e1`, `e2`, and `delta` enter.

Verify symbolically the leading balance. With the unscaled coordinate `X`, it should be equivalent to

\[
u_{XX}
=
\{3X^2+2(e_1+1-\delta)\}u
O(\varepsilon^{1/2})u,
\]

but derive this rather than assuming it.

Choose a normalized Weber coordinate, for example

\[
s=3^{1/4}X,

\]

or another explicitly equivalent convention, and reduce the leading equation to a standard parabolic-cylinder form. State precisely which DLMF/Fedoryuk convention for `D_nu` is used.

## B. Resolve the orientation/sign ambiguity

This is mandatory and must not be hidden by matching a previously known answer.

On the real local `X` axis, square-integrable decay at both ends of the formal Weber problem would select one sign of the Weber parameter. However, the physical Kerr/Bargmann continuation need not use that real pair of Weber sectors. The Stage 08 result suggests that the physically relevant pair may be related by a complex rotation of the local Weber coordinate.

Therefore:

1. identify all relevant subdominant sectors of the local Weber equation;
2. determine the connection-zero condition for each inequivalent opposite or nonadjacent sector pair that can arise from the corrected Stage 09b Stokes geometry;
3. derive the associated candidate values of `e1`;
4. show explicitly how rotations such as `s -> i s` change the sign of the quadratic term, the parabolic-cylinder index, and the connection-zero condition;
5. distinguish:
   - the real-axis decaying Weber problem;
   - the sector pair compatible with the candidate physical Bargmann continuation;
6. do not choose the physical sign merely because it agrees with Stage 08.

If the Stage 09b geometry is insufficient to select a unique physical sector pair, state this as a named local-to-global orientation hypothesis. Then present all mathematically distinct candidate branches and identify which branch is consistent with the independently obtained Stage 08/Bogoliubov coefficient.

In particular, investigate rather than conceal the apparent sign contrast between

\[
e_1=\delta-1-\sqrt3\left(n+\frac12\right)

\]

for the naive real-axis decaying Weber problem and the Stage 08 formal coefficient with the opposite `sqrt(3)` sign.

## C. Construct the leading local wavefunction

For each relevant Weber sector pair, write an explicit leading solution in terms of parabolic-cylinder functions, with:

- the precise argument;
- the precise index;
- the branch and sector convention;
- an explicit normalization convention;
- the domain on which the approximation is asserted.

At a connection zero indexed by fixed `n`, reduce the solution to the appropriate Hermite--Gaussian form whenever that reduction is valid:

\[
D_n(\sqrt2,s)
=
2^{-n/2}e^{-s^2/2}H_n(s),
\]

or the correctly rotated analogue.

Clearly distinguish:

1. a local Weber solution `u_n`;
2. an approximation uniform in a close-pair neighbourhood;
3. a global Bargmann eigenfunction, which has not yet been constructed.

## D. Pull the approximation back to the Bargmann function

Use the exact direct map

\[
\Psi(z)=z^{-\delta}e^{\eta/z}u(z),
\qquad
z=\eta^{1/3}y.
\]

Show explicitly that

\[
X=\frac{y+1}{\sqrt\varepsilon}

\]

reduces, with the established scaling, to a local coordinate centered at

\[
z=-\eta^{1/3}.

\]

Derive the explicit leading approximation

\[
\Psi_n^{\mathrm{loc}}(z)
=
\mathcal N_n(\eta,\delta),
z^{-\delta}e^{\eta/z}
\times
\{\text{parabolic-cylinder or Hermite factor in }z+\eta^{1/3}\},

\]

with all constants, rotations, and powers displayed.

Address all of the following:

1. the approximation is sectorial because `z^(-delta)` uses a fixed logarithm;
2. the gauge factor is not itself a Bargmann wavefunction;
3. the local expression need not be regular at `z=0` because its domain is centered near `z=-eta^(1/3)` and excludes the origin;
4. no global normalization in the Bargmann norm may be claimed from a local approximation alone;
5. `N_n` may therefore be fixed by a local normalization convention, but must not be mislabeled as the exact Bargmann normalization.

Compare the center, Gaussian width, and polynomial factor with the displaced/squeezed Bogoliubov approximation only after completing the independent Fedoryuk pullback.

## E. Derive the candidate energy

From the local connection-zero condition derive

\[
\frac{E_n}{V}
=
-\frac32\eta^{4/3}+e_{1,n}\eta^{2/3}+O(1),
\qquad n\ \text{fixed}.

\]

For every candidate sector pair, give the corresponding `e_(1,n)`.

Then classify the status of the result:

- **Local Weber result:** rigorously/formally implied by the local reduced equation and its chosen sector pair;
- **Conditional physical energy:** additionally assumes that the chosen local sector pair is the one selected by the missing global Bargmann continuation;
- **Independent consistency check:** comparison with the Stage 08/Bogoliubov expansion.

Do not write an unconditional physical eigenvalue formula if the sector-pair identification remains unproved.

## F. First correction to the wavefunction

Expand

\[
u=u_0+\varepsilon^{1/2}u_1+O(\varepsilon)

\]

and derive the inhomogeneous Weber equation for `u1`.

Where possible:

1. express `u1` in the parabolic-cylinder/Hermite basis;
2. impose a clear intermediate-normalization or local normalization condition;
3. identify the finite set of neighbouring indices coupled by the odd perturbation;
4. verify whether the first-order solvability correction to the energy vanishes by parity for the relevant orientation;
5. compare the structure, but not merely the final coefficients, with the cubic correction in the displaced-oscillator calculation.

If the rotated physical sector pair makes an `L2` inner-product solvability argument invalid, do not use it silently. Replace it by the appropriate bilinear/connection-coefficient perturbation or state the limitation explicitly.

The leading wavefunction and `eta^(2/3)` energy term are mandatory. The explicit closed form of `u1` is desirable but must not be fabricated if the correct sectorial normalization is unresolved.

Do not attempt the full `O(1)` physical energy coefficient in 09c unless it follows cleanly and independently from a justified local connection calculation. Otherwise reserve it for 09d.

## G. Symbolic and numerical verification

Create a symbolic verifier that checks at least:

1. the complete close-pair expansion through the order used;
2. the leading Weber rescaling;
3. substitution of the proposed parabolic-cylinder solution into the model equation;
4. the Hermite reduction at integer index;
5. the candidate `e1` formulas for every sector orientation;
6. the pullback coordinate in `z`;
7. the residual of the leading local approximation in the exact Fedoryuk equation and its predicted order in `epsilon`.

Add tests for all exact symbolic identities. Use numerical checks only for sectorial asymptotics, connection coefficients, or residual scaling that cannot reasonably be tested exactly.

For a few fixed values of `n` and `delta`, numerically verify that the exact-equation residual of the local approximation decreases with the predicted power of `epsilon` on compact sets of the scaled coordinate that avoid Stokes boundaries and zeros used in relative-error denominators.

Do not use agreement with matrix eigenvalues as a proof. If a small matrix calculation is used at all, label it as an optional external sanity check and keep it out of the derivation.

## H. Manuscript update

Add a concise continuation to the independent Fedoryuk subsection presenting only:

1. the close-pair scaling;
2. the leading Weber equation;
3. the explicit local wavefunction;
4. the candidate energy coefficient(s);
5. the orientation hypothesis if it remains necessary;
6. an explicit statement that the physical Bargmann assignment is conditional on the unproved global connection.

Do not duplicate the lengthy audit from the documentation. Do not call the result a global quantization theorem.

Keep the notation consistent with the existing manuscript and avoid excessively wide equations. Compile and visually inspect all affected pages.

## Deliverables

Create or update:

1. `docs/fedoryuk_weber_wavefunction_and_energy.md`
2. `scripts/09c_verify_fedoryuk_weber.py`
3. `tests/test_09c_fedoryuk_weber.py`
4. `manuscript/manuscript.tex`
5. `prompt_09c_fedoryuk_weber_wavefunction_and_local_energy.diff`
6. `prompt_09c_fedoryuk_weber_wavefunction_and_local_energy.log`

If a figure materially clarifies the sector orientations or local wavefunction, create it in both PDF and PNG form following repository conventions. Do not add a decorative or redundant figure.

The log must include:

- initial and final `git status -sb`;
- files inspected;
- files changed or created;
- the complete local scaling and Weber convention;
- every candidate sector pair and its `e1` branch;
- the status of the physical-orientation selection;
- the explicit local wavefunction obtained;
- the status of the first correction `u1`;
- symbolic and numerical verification results;
- all tests run;
- LaTeX/Biber compilation result;
- rendered manuscript pages inspected;
- unresolved mathematical assumptions;
- confirmation that no commit and no push were performed.

## Verification commands

Run at least:

```bash
python scripts/09a_verify_fedoryuk_normal_form.py
python scripts/09c_verify_fedoryuk_weber.py
PYTHONPATH=src pytest -q
git diff --check
```

Compile the manuscript using the established repository procedure. Render and inspect every affected page, including one page before and one page after the modified range.

At the end, report clearly:

1. the leading Fedoryuk--Weber approximation to `u_n`;
2. its explicit sectorial pullback to `Psi_n(z)`;
3. all candidate `eta^(2/3)` energy coefficients;
4. which candidate agrees with Stage 08 and why this agreement is only a consistency check;
5. whether the physical sector orientation has been proved or remains a named hypothesis;
6. whether an explicit first wavefunction correction was obtained;
7. what must be done in a possible Stage 09d.

Do not commit and do not push.
