# Stage 05 — Taylor expansion at the origin and formal asymptotics at infinity

Work in the existing `Wnęka_z_Kerrem` repository.

Read `AGENTS.md`, `README.md`, the current manuscript, the Stage 04 documentation, and all relevant source and test files before making changes. Preserve the notation and logical structure established in Stage 04, especially the definitions of `HeunWI`, \(\Delta_{\mathrm{WI}}\), \(B_n^{\mathrm{WI}}\), and the physical parameter mapping.

Do not commit anything.

## Objective

Derive, verify, document, and incorporate into the manuscript:

1. the Taylor expansion at \(z=0\) of the normalized Whittaker–Ince solution through \(z^4\);
2. an exact recurrence and a reusable arbitrary-order coefficient generator suitable for future Padé and Hermite–Padé calculations;
3. the two formal asymptotic solutions at \(z=\infty\), including the first three nontrivial correction coefficients;
4. a careful treatment of square-root branches and asymptotic sectors;
5. the exact degenerate boundary case \(F=\overline F=0\).

This stage concerns local Taylor series and formal asymptotics only. Do not yet develop Liouville–Green/WKB, Olver uniform asymptotics, Fedoryuk theory, inverse Laplace transforms, energy quantization from asymptotic connection formulae, numerical plots, or quasi-fractals. Those belong to later stages.

## Governing equation

Use the Whittaker–Ince equation already established in the manuscript:

\[
z^2\Psi''(z)
+\left(B_1+B_2z\right)\Psi'(z)
+\left(B_3+qz\right)\Psi(z)=0,
\qquad B_1\neq0
\]

for the nondegenerate driven problem, with the physical identification

\[
B_1=\frac{2\overline F}{V},
\qquad
B_2=\frac{2\hbar\omega_0}{V},
\qquad
B_3=-\frac{2E}{V},
\qquad
q=\frac{2F}{V}.
\]

First verify from the current manuscript and the original Bargmann equation that this equation and this parameter mapping are correct. If the repository uses a different but algebraically equivalent convention, reconcile the conventions explicitly before proceeding.

Do not silently assume that \(F\) and \(\overline F\) are independent in the physical problem. Distinguish clearly between algebraic continuation in complex parameters and the physical restriction \(\overline F=F^*\).

---

## Part A — Taylor expansion at \(z=0\)

Set

\[
\Psi(z)=\sum_{n=0}^{\infty}c_nz^n,
\qquad c_0=1,
\qquad c_{-1}=0.
\]

Derive the coefficient recurrence directly by substitution into the differential equation. Verify whether it is

\[
B_1(n+1)c_{n+1}
+
\left[n(n-1)+B_2n+B_3\right]c_n
+
q c_{n-1}=0,
\qquad n\ge0.
\]

Do not merely reproduce this formula: derive and independently check it.

Introduce a compact notation such as

\[
A_n=n(n-1)+B_2n+B_3
\]

only if it genuinely improves readability.

Derive completely explicit expressions for

\[
c_1,\qquad c_2,\qquad c_3,\qquad c_4.
\]

Present them:

1. in the parameters \((B_1,B_2,B_3,q)\);
2. after substitution of \((F,\overline F,V,\hbar\omega_0,E)\).

The physical-parameter expressions may use sensible intermediate abbreviations if full expansion would obscure the structure, but they must remain explicit and unambiguous.

Display the resulting Taylor expansion

\[
\Psi(z)
=1+c_1z+c_2z^2+c_3z^3+c_4z^4+O(z^5)
\]

in the manuscript.

Check every coefficient by direct symbolic substitution into the differential equation and confirm that the residual vanishes through the required order. The verification must not reuse the same algebraic implementation as the recurrence generator in a way that makes both checks fail identically from one shared mistake.

### Arbitrary-order Taylor generator

Implement a small, focused routine that generates

\[
c_0,c_1,\ldots,c_N
\]

from the exact recurrence for arbitrary \(N\ge0\).

Requirements:

* support exact or symbolic arithmetic when the repository’s existing dependencies make this reasonable;
* support high-precision numerical arithmetic for later Padé and Hermite–Padé work;
* do not restrict the implementation to \(N=4\);
* validate \(N\) and all singular assumptions explicitly;
* do not divide by \(B_1\) without checking \(B_1\neq0\);
* avoid ordinary machine-precision arithmetic as the only available path;
* keep the API narrow and documented.

If introducing a new symbolic dependency would be disproportionate, do not add it silently. Use the project’s existing stack and explain the chosen representation.

Add tests covering at least:

* \(c_0=1\);
* the explicit formulas for \(c_1,\ldots,c_4\);
* vanishing of the differential-equation residual to the expected order;
* agreement between exact/symbolic and high-precision numerical evaluation for representative nonsingular parameters;
* arbitrary order beyond \(N=4\);
* invalid \(N\);
* rejection or separate handling of \(B_1=0\);
* complex-valued parameters.

Design the coefficient output so it can later be used directly to construct Padé and Hermite–Padé approximants as functions of

\[
B_3=-\frac{2E}{V}.
\]

Do not implement those approximants in this stage.

---

## Part B — Formal asymptotic expansion at \(z=\infty\)

Derive the formal asymptotic solutions independently from the differential equation. Do not assume in advance that the tentative formulas below are correct.

Begin with a sufficiently general exponential-power ansatz. Determine the dominant exponential action \(S(z)\), the algebraic exponent \(r\), and the correct spacing of the inverse powers.

Explicitly test the initially suggested form

\[
\Psi(z)
=e^{S(z)}z^r
\sum_{n=1}^{m}u_nz^{-n}
\]

and explain why, for \(q\neq0\), a series in integer powers of \(z^{-1}\) is generally not closed under the recurrence.

Verify whether the correct formal structure is

\[
\Psi_\sigma(z)
\sim
e^{2\sigma\sqrt{-qz}}
z^{1/4-B_2/2}
\sum_{n=0}^{\infty}
u_n^{(\sigma)}z^{-n/2},
\qquad
\sigma=\pm1,
\qquad
u_0^{(\sigma)}=1.
\]

In particular, independently derive and check:

\[
S_\sigma(z)=2\sigma\sqrt{-qz},
\qquad
r=\frac14-\frac{B_2}{2}.
\]

The square root, its branch, and the meaning of \(\sqrt{-qz}\) must be stated precisely.

A convenient derivation may use

\[
t=\sqrt z,
\]

so that the formal expansion becomes an ordinary inverse-power series in \(t\). If this substitution is used, derive the transformed differential equation explicitly and use it consistently.

### Asymptotic recurrence and first coefficients

Derive a general recurrence for \(u_n^{(\sigma)}\). Then obtain explicit, simplified formulas for the first three nontrivial coefficients

\[
u_1^{(\sigma)},\qquad
u_2^{(\sigma)},\qquad
u_3^{(\sigma)}.
\]

The final displayed expansion should have the form

\[
\Psi_\sigma(z)
\sim
e^{2\sigma\sqrt{-qz}}
z^{1/4-B_2/2}
\left[
1+
u_1^{(\sigma)}z^{-1/2}
+
u_2^{(\sigma)}z^{-1}
+
u_3^{(\sigma)}z^{-3/2}
+
O(z^{-2})
\right].
\]

A previous informal calculation proposed formulas involving

\[
a_\sigma=2\sigma\sqrt{-q},
\qquad
\kappa=\frac12-B_2,
\]

and certain quantities \(D_n\). Treat those formulas only as conjectural scratch work. Re-derive all factors, signs, shifts, and powers from first principles. If the earlier formulas are wrong, replace them and document the discrepancy succinctly. Mathematical correctness takes precedence over preserving the tentative expressions.

Verify the recurrence and \(u_1,u_2,u_3\) by symbolic substitution into the original differential equation, after factoring out the common exponential and power prefactor. Report the first un-cancelled formal order of the residual.

Implement a focused arbitrary-order asymptotic coefficient generator if this fits naturally with the repository structure. It should generate \(u_0,\ldots,u_N\) for either sign \(\sigma\), under explicit assumptions \(q\neq0\) and a chosen square-root branch. Add tests for:

* both signs \(\sigma=\pm1\);
* the explicit first three coefficients;
* formal residual cancellation;
* complex parameters;
* rejection or separate treatment of \(q=0\);
* consistency under a coherent change of square-root branch and sign label.

Do not infer convergence of the asymptotic series. Call it a formal asymptotic expansion unless a stronger claim is actually proved.

---

## Part C — Branches, sectors, and dominance

State clearly that the two formal solutions are distinguished by

\[
\exp\!\left(2\sigma\sqrt{-qz}\right).
\]

For a fixed branch of the square root, describe the sectors in which each solution is exponentially dominant or subdominant according to the sign of

\[
\Re\!\left(\sigma\sqrt{-qz}\right).
\]

Identify the formal Stokes and anti-Stokes rays using an explicit convention, and state that terminology for “Stokes” versus “anti-Stokes” rays varies in the literature. Define the convention used in the manuscript instead of relying on terminology alone.

Do not yet derive connection matrices or Stokes multipliers.

Explain what changes when \(z\) is analytically continued once around infinity:

* the behavior of \(\sqrt z\);
* the interchange or relabelling of the two exponential branches;
* the algebraic factor \(z^r\);
* the status of the formal series.

Keep branch-dependent statements mathematically precise.

---

## Part D — Exact boundary check \(F=\overline F=0\)

Treat the undriven case separately.

When

\[
F=\overline F=0,
\]

we have

\[
B_1=0,\qquad q=0,
\]

and the Whittaker–Ince equation degenerates to the Euler equation

\[
z^2\Psi''+B_2z\Psi'+B_3\Psi=0.
\]

Using \(\Psi=z^\rho\), derive the indicial equation

\[
\rho(\rho-1)+B_2\rho+B_3=0.
\]

Then impose the Bargmann-space condition and show that the physical eigenfunctions and energies are

\[
\Psi_n(z)=\frac{z^n}{\sqrt{n!}},
\qquad
E_n=\hbar\omega_0n+\frac V2n(n-1),
\qquad n=0,1,2,\ldots.
\]

Verify the normalization convention used for Bargmann monomials in the current manuscript before inserting the factor \(1/\sqrt{n!}\).

Explain rigorously why this boundary case is singular relative to the normalized nondegenerate construction:

* for \(n>0\), \(\Psi_n(0)=0\), so the normalization \(c_0=1\) is unavailable;
* the Taylor recurrence solved forward by division by \(B_1\) ceases to exist when \(B_1=0\);
* the large-\(z\) expansion with \(e^{\pm2\sqrt{-qz}}\) degenerates when \(q=0\);
* direct substitution \(F=\overline F=0\) into formulas derived under \(B_1q\neq0\) is not a valid derivation.

Distinguish the exactly degenerate point \(F=\overline F=0\) from the limiting behavior as \(F\to0\) under the physical constraint \(\overline F=F^*\). Do not claim continuity of the \(c_0=1\) normalization for excited states.

If feasible within the scope of this stage, add a test verifying the Euler-equation eigenpairs directly against the undriven Bargmann Hamiltonian or differential equation.

---

## Manuscript changes

Add a coherent subsection, or a small sequence of subsections, to `manuscript/manuscript.tex` covering:

1. Taylor expansion at the origin;
2. formal asymptotic solutions at infinity;
3. branches and asymptotic sectors;
4. the exact undriven boundary case.

The exposition must distinguish theorem-level conclusions from formal calculations.

Requirements:

* preserve the manuscript’s notation and style;
* avoid overstating convergence or uniform validity;
* do not describe the formal infinity expansion as an Olver expansion;
* do not derive energy quantization from local infinity asymptotics alone;
* make clear that the Taylor generator is intended for later Padé and Hermite–Padé analysis;
* retain the logical primacy of the Stage 04 definitions of `HeunWI`, \(\Delta_{\mathrm{WI}}\), and \(B_n^{\mathrm{WI}}\);
* do not redefine the characteristic values through the asymptotic recurrence.

Add citations only if genuinely required. Do not perform a broad literature review in this stage.

Create a concise technical note:

`docs/stage05_taylor_and_infty.md`

It should contain the derivations in enough detail to audit every recurrence and coefficient, including the symbolic residual checks and all assumptions.

---

## Validation

Run all existing tests and all new tests.

Compile the manuscript using the repository’s established build procedure. Inspect the resulting PDF for:

* equation overflow;
* malformed square roots or branch notation;
* broken cross-references;
* misplaced equation numbers;
* awkward page breaks;
* consistency of \(F^*\), \(\overline F\), \(B_j\), \(q\), \(r\), \(\sigma\), \(c_n\), and \(u_n^{(\sigma)}\).

Run at least:

```bash
git diff --check
```

and the project’s complete test suite.

Do not suppress warnings without understanding them.

---

## Deliverables

At completion, report:

1. the files changed or added;
2. the verified Taylor recurrence;
3. explicit \(c_1,c_2,c_3,c_4\);
4. the arbitrary-order Taylor generator API;
5. the verified formal asymptotic form;
6. the general recurrence for \(u_n^{(\sigma)}\);
7. explicit \(u_1^{(\sigma)},u_2^{(\sigma)},u_3^{(\sigma)}\);
8. the first nonzero order of the checked asymptotic residual;
9. the adopted square-root branch and sector convention;
10. the exact \(F=\overline F=0\) result and the explanation of the singular normalization;
11. all test and manuscript-build results;
12. any discrepancy found in the tentative formulas supplied in this prompt.

Also save:

```bash
git diff > stage05_taylor_and_infty.diff
```

and provide a concise execution log as:

```text
stage05_taylor_and_infty.log
```

Do not stage or commit changes. Stop after reporting the results and wait for review.
