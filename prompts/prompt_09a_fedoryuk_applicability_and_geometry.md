# Task 09a: Fedoryuk applicability audit and independent complex-WKB formulation

You are working in the repository:

`~/Dokumenty/Prace_i_dnie/Wnęka_z_Kerrem`

The repository is synchronized with `origin/master`. Do not commit and do not push.

## Scientific purpose

Stage 08 completed the Olver-based strong-drive analysis. It produced:

- the complete inverse transformation from the Olver variable \(W\) to the Bargmann eigenfunction \(\Psi\);
- the conjectural condition \(C_{\mathrm{ess}}(E)=0\);
- a formal fixed-\(n\) energy expansion through order \(\eta^{-2/3}\);
- no proved global Olver connection theorem.

Here

\[
\eta=\frac{|F|}{V}\to\infty.
\]

Stage 09 must develop an independent approach based on Fedoryuk's complex WKB theory. Do not merely rename or paraphrase the Olver analysis.

The purpose of 09a is not yet to claim a complete quantization theorem. Its purpose is to determine precisely which theorem or construction of Fedoryuk applies to the Kerr Bargmann equation, derive the correct Fedoryuk normal form directly from the original equation, and identify all remaining global obstructions.

## Mandatory preliminary inspection

Before editing anything, inspect:

1. `manuscript/manuscript.tex`;
2. all Stage 08 prompts, especially 08c, 08d, and 08e;
3. the Stage 08 reports, logs, diffs, and supporting documentation;
4. the scripts and tests used to verify the strong-drive scaling;
5. the bibliography entries for Fedoryuk, Olver, Sibuya, Evgrafov, Voros, and related complex-WKB references.

Recover the exact notation and formulas already used in the repository. Do not reconstruct coefficients from memory when they are available in the files.

Record the current `git status -sb` before making changes. Preserve all pre-existing user changes.

## Fixed conventions

Preserve the conventions of the manuscript:

- the Kerr coefficient is \(V/2\);
- \(V>0\);
- the dimensionless energy is
  \[
  \mathcal E=\frac{2E}{V};
  \]
- the strong-drive parameter is
  \[
  \eta=\frac{|F|}{V};
  \]
- do not use \(\varepsilon_D\) as an energy;
- use “driven” or “externally driven”, not an inappropriate mechanical synonym;
- do not insert internal labels such as “Stage 09” into the scientific manuscript;
- keep the established phase convention for \(F\), or explain explicitly any gauge rotation used to make \(F\) real.

The previously verified turning-point polynomial is

\[
P(y;e)=1+2ey^2-2y^3,
\qquad
P_y(y;e)=4ey-6y^2.
\]

Its nonzero double root on the real branch is

\[
y_0=-1,
\qquad
e_0=-\frac32.
\]

Treat these formulas as checkpoints, not as substitutes for deriving the Fedoryuk equation from the original Bargmann problem.

## Prohibited shortcuts

Do not use:

- matrix diagonalization as a derivation;
- continued fractions;
- Padé or Hermite–Padé approximants;
- an assumed exact Heun spectral determinant;
- the unproved identification
  \[
  C_{\mathrm{ess}}(E)=0
  \iff
  \Delta_{\mathrm{WI}}(E)=0;
  \]
- the unproved global Olver connection theorem;
- a Bohr–Sommerfeld condition written down before the relevant contour, branch, Stokes sectors, and connection path have been derived;
- numerical agreement as a proof of a connection formula.

Numerical calculations may be used only as checks of symbolic formulas and Stokes geometry.

## Main mathematical work

### A. Derive the Fedoryuk normal form

Starting from the exact Bargmann eigenvalue equation, derive all gauge and scaling transformations needed to obtain a singularly perturbed second-order equation of the form

\[
\varepsilon^2 u''(y)
=
Q(y,e,\varepsilon)u(y),
\]

or the closest standard form used by Fedoryuk.

Determine the correct relation between \(\varepsilon\) and \(\eta\). In particular, check carefully whether

\[
\varepsilon=\eta^{-1/3}
\]

is the natural Fedoryuk small parameter, or whether a different power appears after the exact removal of the first derivative.

Write

\[
Q(y,e,\varepsilon)
=
Q_0(y,e)
+\varepsilon Q_1(y,e)
+\varepsilon^2Q_2(y,e)+\cdots
\]

to the order justified by the exact equation.

Show explicitly how \(P(y;e)\) is related to \(Q_0(y,e)\). Track every prefactor, pole, branch point, and singularity introduced by the transformations.

### B. Classify singularities and turning points

For the transformed equation:

1. list all finite and infinite singularities;
2. distinguish genuine singularities of the differential equation from artifacts of gauge or Liouville transformations;
3. determine the turning points of \(Q_0\);
4. classify them for generic \(e\);
5. analyze the coalescence at
   \[
   (y,e)=(-1,-3/2);
   \]
6. state whether the relevant Fedoryuk theorem concerns separated simple turning points, a double turning point, or requires two overlapping descriptions.

Do not silently apply a theorem for polynomial potentials if the transformed coefficient is rational or meromorphic.

### C. Construct the Fedoryuk geometry

Define the complex momentum

\[
p(y,e)=\sqrt{Q_0(y,e)}
\]

with an explicit branch convention.

Define the phase integrals

\[
S_j(y,e)=\int_{y_j(e)}^y p(t,e)\,dt
\]

and determine the Stokes and anti-Stokes curves using one consistent convention. State the convention explicitly.

Construct, analytically as far as possible and numerically only for verification:

- the relevant Stokes graph near \(e=-3/2\);
- the candidate Fedoryuk canonical domains;
- the sectors containing subdominant solutions;
- the candidate chain of canonical domains that might connect the local condition at \(z=0\) with the Bargmann-admissible sectors at infinity.

Explain whether such a chain can avoid all turning points and singularities. If it cannot, identify precisely which local connection problem is required.

### D. Identify the applicable Fedoryuk result

Locate the precise theorem, proposition, or construction in Fedoryuk's *Asymptotic Analysis: Linear Ordinary Differential Equations* that is relevant to each of the following:

1. existence of exact solutions with prescribed WKB asymptotics in a canonical domain;
2. error estimates away from turning points;
3. connection across a simple turning point;
4. treatment of two coalescing turning points or a double turning point;
5. global continuation through a chain of canonical domains.

Give chapter/section/page/theorem information only after verifying it from an accessible source. If the exact theorem numbering or page cannot be verified, say so explicitly and cite only the verified chapter or section. Do not invent theorem numbers.

For every invoked result, list its hypotheses and check them individually against the Kerr equation.

### E. Determine the strongest justified result

Classify the possible outcome as one of the following.

**Outcome A — proved sectorial Fedoryuk theorem**

The hypotheses suffice to construct exact solutions with uniform WKB asymptotics on explicitly identified canonical domains, but they do not yet yield a global spectral condition.

**Outcome B — conditional global connection formula**

A chain of domains and local turning-point connections can be constructed, but one remaining global identification with the Bargmann boundary condition must be stated as a named hypothesis.

**Outcome C — asymptotic Fedoryuk quantization theorem**

A complete argument connects the solution regular/entire at the origin with the required subdominant behavior at infinity and yields a scalar asymptotic quantization condition.

Select only the strongest outcome actually supported by checked hypotheses. Outcome A is a scientifically useful result and must not be inflated into B or C.

### F. Relation to the Stage 08 expansion

Only after completing A–E, compare the Fedoryuk scaling with the formal fixed-\(n\) expansion obtained in 08e.

Determine:

- which action integral would generate the leading energy term;
- how the coalescing-turning-point scaling produces powers of \(\eta^{-2/3}\);
- whether the \(n\)-dependent coefficient can in principle be recovered from the local connection problem;
- which coefficients can already be independently checked;
- which coefficients still depend on an unproved global connection statement.

Do not copy the 08e coefficients as input into the Fedoryuk derivation. Use them only as an external consistency check after the independent derivation.

## Deliverables

Create:

1. `docs/fedoryuk_applicability_and_geometry.md`

   This must contain the complete derivation, theorem-hypothesis audit, Stokes geometry, outcome classification, and comparison with Stage 08.

2. `scripts/09a_verify_fedoryuk_normal_form.py`

   The script must symbolically verify:
   - the transformations from the Bargmann equation;
   - removal of the first derivative;
   - the resulting \(Q(y,e,\varepsilon)\);
   - the relation to \(P(y;e)\);
   - the double-root equations at \(y=-1,\ e=-3/2\);
   - all asymptotic power countings used in the report.

3. `tests/test_fedoryuk_normal_form.py`

   Add focused tests for the symbolic identities. Do not make the tests depend on graphical output or arbitrary floating-point tolerances when exact symbolic checks are possible.

4. A Stokes-geometry figure in both PDF and PNG form, following the repository's existing figure conventions. Distinguish analytic information from numerically traced curves in the caption and documentation.

5. A concise manuscript subsection presenting only results justified by the audit. Do not include internal workflow terminology. If only Outcome A is established, state a sectorial Fedoryuk result and explicitly label the global spectral connection as open.

6. `prompt_09a_fedoryuk_applicability_and_geometry.diff`

7. `prompt_09a_fedoryuk_applicability_and_geometry.log`

The log must include:

- initial and final `git status -sb`;
- files inspected;
- files changed or created;
- commands run;
- test results;
- manuscript compilation result;
- warnings and unresolved mathematical assumptions;
- the selected Outcome A, B, or C and the reason for that classification.

## Verification

Run at least:

```bash
python scripts/09a_verify_fedoryuk_normal_form.py
pytest -q
```

Then compile the manuscript using the repository's established LaTeX/Biber procedure.

Check:

- that all symbolic identities are exact;
- that no earlier Stage 08 result was silently strengthened;
- that the manuscript contains no broken citations or cross-references;
- that no generated auxiliary files were accidentally added as source files;
- that the final diff contains only intentional changes.

Do not commit and do not push.

At the end, report the exact files changed, the tests run, the compilation status, and the strongest justified Fedoryuk outcome.
