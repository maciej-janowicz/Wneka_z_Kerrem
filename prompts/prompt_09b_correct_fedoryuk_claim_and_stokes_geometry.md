# Task 09b: Correct the Fedoryuk claim, Stokes geometry, and manuscript rendering

You are working in the repository:

`~/Dokumenty/Prace_i_dnie/Wnęka_z_Kerrem`

The repository is synchronized with `origin/master`, but the working tree intentionally contains the uncommitted Stage 09a changes. Preserve them and correct them in place.

Do not commit and do not push. Git operations will be performed only after the complete Stage 09 review series has been accepted.

## Purpose

Stage 09a produced a valuable independent reduction of the Kerr Bargmann equation to the exact Fedoryuk normal form

\[
\varepsilon^2u_{yy}
=
\left(Q_0+\varepsilon Q_1+\varepsilon^2Q_2\right)u,
\qquad
\varepsilon=\eta^{-2/3},
\]

with

\[
Q_0(y,e)=\frac{P(y;e)}{y^4},
\qquad
P(y;e)=1+2ey^2-2y^3,
\]

\[
Q_1(y)=\frac{2(\delta-1)}{y^3},
\qquad
Q_2(y)=\frac{\delta(\delta-1)}{y^2}.
\]

This exact reduction, the double root

\[
(y_0,e_0)=(-1,-3/2),
\]

and the energy power ladder are to be retained.

However, the Stage 09a review found three substantive issues:

1. the phrase “proved sectorial Fedoryuk theorem” is stronger than the checked evidence supports;
2. the numerical Stokes-geometry script launches trajectories from arbitrary equally spaced directions rather than from the analytically correct local separatrix directions;
3. the manuscript PDF contains a literal `qquad` rendering error and an overwide normal-form display.

There is also a duplicated `module_from_spec` line in the new test file.

Stage 09b must correct these issues without attempting the still-open global Bargmann connection problem.

## Mandatory preliminary inspection

Before editing:

1. run `git status -sb` and record it;
2. inspect all Stage 09a changes, including:
   - `manuscript/manuscript.tex`;
   - `docs/fedoryuk_applicability_and_geometry.md`;
   - `scripts/09a_verify_fedoryuk_normal_form.py`;
   - `scripts/09a_fedoryuk_stokes_geometry.py`;
   - `tests/test_fedoryuk_normal_form.py`;
   - `figures/fedoryuk_stokes_geometry.pdf`;
   - `figures/fedoryuk_stokes_geometry.png`;
   - the 09a prompt, diff, and log;
3. inspect the affected pages of the current manuscript PDF;
4. preserve unrelated user changes and all correct Stage 09a algebra.

## A. Correct the scientific status of the Fedoryuk result

The accessible source audit verified chapter and section locations in Fedoryuk, but did not verify complete theorem statements, theorem numbers, or every global hypothesis. In addition, Stage 09a identified candidate canonical domains but did not explicitly construct all of them and prove the required progressive-path property.

Therefore do not call the present result a “proved sectorial Fedoryuk theorem”.

Use a formulation no stronger than:

> **Outcome A: verified sectorial Fedoryuk applicability framework.**

The mathematical content should state precisely that:

- the exact Kerr normal form satisfies the local analytic prerequisites for ordinary sectorial WKB/Fedoryuk constructions on any cut canonical domain that avoids the pole and turning points and for which the required progressive paths are separately verified;
- the local simple-turning-point and close/double-turning-point models are identified;
- no explicit global canonical-domain chain has been proved;
- the construction of all required progressive paths has not been completed;
- no global connection coefficient or Bargmann spectral condition follows.

Revise both the documentation and manuscript language consistently. Do not weaken the exact algebraic reduction itself.

Do not introduce an invented theorem number or claim that full hypotheses were checked from an inaccessible theorem text.

## B. Derive the correct local separatrix directions

Let a turning point `y_j` have multiplicity `m` in the leading coefficient:

\[
Q_0(y,e)=a_j(y-y_j)^m\{1+O(y-y_j)\},
\qquad a_j\ne0.
\]

With a locally fixed square root,

\[
S_j(y)
=
\int_{y_j}^y\sqrt{Q_0(t,e)}\,dt
\sim
\frac{2\sqrt{a_j}}{m+2}(y-y_j)^{(m+2)/2}.
\]

Using the manuscript's convention

\[
\text{Stokes: }\Re S_j=0,
\qquad
\text{anti-Stokes: }\Im S_j=0,
\]

derive the initial ray directions rather than assigning arbitrary equally spaced angles.

For `theta=arg(y-y_j)` and `arg(a_j)` taken consistently, verify formulas equivalent modulo the appropriate ray periodicity to

\[
\theta^{(S)}_k
=
\frac{(2k+1)\pi-\arg a_j}{m+2},
\]

\[
\theta^{(A)}_k
=
\frac{2k\pi-\arg a_j}{m+2}.
\]

There must be `m+2` rays in each family.

Apply this explicitly to:

1. every simple root for the separated example, using
   \[
   a_j=\partial_yQ_0(y_j,e);
   \]
2. the double root at
   \[
   y_0=-1,\qquad e=-3/2,
   \]
   using the exact local coefficient. Verify in particular that
   \[
   Q_0(y,-3/2)=3(y+1)^2+O((y+1)^3),
   \]
   so that the four directions in each family follow from `a_0=3`, not from an arbitrary angular offset;
3. the remaining simple root `y=1/2` at coalescence.

Document branch conventions and the fact that reversing the square-root sign does not change the geometric ray set.

## C. Repair and validate the Stokes tracing algorithm

Modify `scripts/09a_fedoryuk_stokes_geometry.py` in place.

Requirements:

1. compute the multiplicity and local coefficient `a_j` for every turning point;
2. compute all initial Stokes and anti-Stokes directions analytically from the local phase;
3. start each numerical trajectory on the corresponding analytically determined ray at a sufficiently small controlled radius;
4. trace the correct level curves using continuous square-root continuation;
5. stop trajectories with explicit events or robust termination conditions near:
   - the pole;
   - another turning point;
   - the plotting boundary;
   - excessive integration length;
6. do not replace a derivative by zero and continue accumulating repeated stationary points after a stopping boundary is reached;
7. suppress duplicate trajectories only by a documented geometric criterion, not by deleting inconvenient curves manually;
8. keep numerical tracing explicitly illustrative rather than a proof of global connectivity.

Add an independent numerical validation of the plotted curves. For sample points along each displayed trajectory, evaluate the phase integral consistently and verify that:

- `Re(S_j)` remains zero within a stated numerical tolerance for Stokes curves;
- `Im(S_j)` remains zero within a stated numerical tolerance for anti-Stokes curves.

It is acceptable to validate the constant-level property relative to the finite-radius starting point and separately bound the local starting error using the analytic expansion. State both tolerances.

Do not label a curve as `Re S=0` or `Im S=0` unless this validation passes.

## D. Add focused tests for the geometry

Extend `tests/test_fedoryuk_normal_form.py`, or add a narrowly named Stage 09 geometry test file if cleaner.

Test at least:

1. the general local direction formulas for multiplicities `m=1` and `m=2`;
2. the exact double-root coefficient `a_0=3`;
3. the four Stokes directions and four anti-Stokes directions at `y=-1` modulo `2*pi`;
4. the three plus three directions at each simple root;
5. invariance of the geometric ray sets under reversal of the square-root branch;
6. the numerical constant-phase validation used for the final figure.

Remove the duplicated line

```python
module = importlib.util.module_from_spec(spec)
```

from `tests/test_fedoryuk_normal_form.py`.

Prefer exact symbolic comparisons for local coefficients and angles whenever possible. Use explicit justified tolerances only for trajectory integration.

## E. Regenerate and inspect the figure

Regenerate:

- `figures/fedoryuk_stokes_geometry.pdf`;
- `figures/fedoryuk_stokes_geometry.png`.

The corrected figure must:

- display the separated configuration and the exact coalescence configuration;
- show all analytically required local rays within the plotting window;
- distinguish turning points by multiplicity;
- mark the pole at `y=0` unambiguously;
- use the stated Fedoryuk convention consistently;
- avoid implying that numerically truncated curves prove global connectivity;
- remain legible at manuscript size.

Update the caption if necessary to say that the initial incidence directions are analytic while the continued curve shapes are numerical.

Render the figure independently and inspect it before compiling the manuscript.

## F. Correct the manuscript rendering

In `manuscript/manuscript.tex`:

1. replace the malformed literal `qquad` by the proper LaTeX command `\qquad`;
2. split the overwide normal-form display into a readable multiline construction, for example using `aligned`, `split`, or two equations;
3. ensure that `Q_1` and `Q_2` remain attached to their correct denominators;
4. revise the Outcome A language as required in part A;
5. keep internal workflow labels such as “Stage 09a” and “Stage 09b” out of the scientific manuscript;
6. preserve all earlier warnings that the global connection and physical quantization remain open.

Compile the manuscript and visually inspect every page affected by the revised text or floating figure, including one page before and one page after the affected range.

Explicitly check that the final PDF contains no visible strings such as:

- `qquad`;
- raw LaTeX commands;
- overfull or clipped equations;
- misplaced equation numbers;
- overlapping text or figures.

## G. Preserve the scope boundary

Stage 09b is a correction and validation stage. Do not attempt to:

- construct the complete global canonical-domain chain;
- derive a Fedoryuk spectral determinant;
- prove equivalence with `C_ess(E)=0`;
- prove equivalence with `Delta_WI=0`;
- assign the local Weber zeros to physical Bargmann eigenvalues;
- change the already verified formal energy coefficients from Stage 08e.

If the corrected geometry exposes an additional obstruction to the proposed chain, record it clearly for a possible Stage 09c rather than hiding it or expanding the present task without control.

## Deliverables

Create the following root-level audit files:

1. `prompt_09b_correct_fedoryuk_claim_and_stokes_geometry.diff`
2. `prompt_09b_correct_fedoryuk_claim_and_stokes_geometry.log`

Update in place all affected Stage 09a files, including the documentation, scripts, tests, figures, and manuscript.

The 09b log must include:

- initial and final `git status -sb`;
- files inspected;
- exact files changed;
- derivation of the local direction formulas;
- local coefficients and direction sets used for each plotted turning point;
- phase-integral validation method and numerical tolerances;
- tests run and results;
- figure-generation result;
- LaTeX/Biber compilation result;
- rendered manuscript pages inspected;
- unresolved mathematical assumptions;
- the final cautious wording of Outcome A;
- confirmation that no commit and no push were performed.

## Verification

Run at least:

```bash
python scripts/09a_verify_fedoryuk_normal_form.py
python scripts/09a_fedoryuk_stokes_geometry.py
PYTHONPATH=src pytest -q
git diff --check
```

Compile the manuscript using the established repository procedure.

Render and inspect:

- the corrected Stokes figure;
- all affected manuscript pages and adjacent pages.

Search the manuscript source and extracted PDF text for `qquad` and other leaked LaTeX tokens.

At the end, report:

1. the corrected scientific status of the Fedoryuk result;
2. the analytic direction formulas actually used;
3. the validation errors for the numerical Stokes and anti-Stokes curves;
4. all tests and compilation results;
5. every remaining issue that may require Stage 09c.

Do not commit and do not push.
