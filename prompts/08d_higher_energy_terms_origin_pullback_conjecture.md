# Prompt 08d — Higher strong-drive energy terms, complete pullback to \(\Psi\), and the essential-connection conjecture

## Repository and working rules

Work exclusively in the existing repository

```text
~/Dokumenty/Prace_i_dnie/Wnęka_z_Kerrem
```

Begin by printing the absolute repository path and inspecting:

- the complete working tree;
- all current 08a–08c changes;
- `manuscript/manuscript.tex`;
- the strong-drive documentation;
- the existing symbolic verification scripts and tests;
- the current build procedure;
- the latest compiled manuscript.

The existing working tree may contain uncommitted user changes. Preserve them. Do not reset, restore, clean, delete, overwrite unrelated files, initialize or clone a repository, or change a remote.

Do not stage, commit, push, tag, or create a GitHub release. Git operations belong to the user.

Save this prompt, if it is not already present verbatim, as

```text
prompts/08d_higher_energy_terms_origin_pullback_conjecture.md
```

This task must produce substantive new mathematics. Merely renaming solutions, rearranging paragraphs, or adding qualifications is not an acceptable completion.

## Principal objectives

The work has three mandatory mathematical objectives:

1. derive and independently verify at least the complete \(O(1)\) term in the fixed-level strong-drive expansion of \(E_n/V\), including its nonlinear dependence on \(n\);
2. undo every transformation from the Weber comparison function \(W\) back to the physical Bargmann wavefunction \(\Psi\), displaying explicitly where the essential singularity at \(z=0\) cancels and where it is enhanced;
3. formulate a mathematically precise conjecture defining the essential-branch connection coefficient \(C_{\mathrm{ess}}(E)\), preferably by Wronskians, and stating the conjectural physical quantization condition
   \[
   C_{\mathrm{ess}}(E)=0.
   \]

In addition, attempt to calculate the next coefficient of order \(\eta^{-2/3}\). If that calculation cannot be completed reliably within this task, give a precise perturbative inventory of all terms contributing to it and identify the smallest remaining algebraic task. Do not invent or guess the coefficient.

Throughout,

\[
\eta=\frac{|F|}{V}\to\infty,\qquad
\delta=\frac{\hbar\omega_0}{V}\quad\text{fixed},\qquad
u=\eta^{2/3},
\]

and \(n\) is fixed.

## Part I — Higher strong-drive energy terms

Use the exact displaced-oscillator calculation as an independent operator derivation, not as a consequence of the still-incomplete global Olver connection theorem.

For \(F=|F|>0\), put

\[
a=b-r,\qquad r>0,\qquad r^3+\delta r=\eta.
\]

Verify from the original Hamiltonian, without relying on a previously copied formula, that

\[
\frac{H}{V}
=
-\frac32r^4-\delta r^2
+
(2r^2+\delta)b^\dagger b
+
\frac{r^2}{2}(b^{\dagger2}+b^2)
-r(b^{\dagger2}b+b^\dagger b^2)
+\frac12b^{\dagger2}b^2.
\]

Diagonalize the exact quadratic part by a real Bogoliubov transformation. Verify

\[
\Omega^2=(2r^2+\delta)^2-r^4.
\]

Organize the calculation systematically in powers of \(r^{-1}\). The cubic interaction is of order \(r\), the quartic interaction is of order one, and the quadratic level spacing is of order \(r^2\). Consequently:

- the first-order cubic correction vanishes by parity;
- the first-order quartic correction contributes at order \(O(1)\);
- the second-order cubic correction also contributes at order \(O(1)\);
- both contributions must be retained;
- higher-order contributions must be power-counted before being discarded.

Compute the matrix elements algebraically in the Bogoliubov number basis. Do not use numerical diagonalization of a truncated Hamiltonian as a derivation or proof. A finite symbolic ladder-operator representation may be used solely to verify exact matrix elements.

The following formula is a candidate to be tested, not an assumption:

\[
\frac{E_n}{V}
=
-\frac32\eta^{4/3}
+
\left[
\delta+\sqrt3\left(n+\frac12\right)-1
\right]\eta^{2/3}
+
\frac{\delta(1-2\delta)}6
-
\frac{6n^2+6n+1}{72}
+
O(\eta^{-2/3}).
\]

Derive or falsify it term by term. In particular, verify independently whether

\[
\Delta_{4,n}^{(1)}
=
\frac{
18n^2+(18-16\sqrt3)n+15-8\sqrt3
}{24},
\]

\[
\Delta_{3,n}^{(2)}
=
-\frac{
30n^2+(30-24\sqrt3)n+23-12\sqrt3
}{36},
\]

and hence

\[
\Delta_{4,n}^{(1)}+\Delta_{3,n}^{(2)}
=
-\frac{6n^2+6n+1}{72}.
\]

Also verify carefully the conversion

\[
r=\eta^{1/3}-\frac{\delta}{3}\eta^{-1/3}
+O(\eta^{-5/3})
\]

to sufficient order and show explicitly how the \(n\)-dependent \(O(1)\) terms from the exact quadratic energy cancel or combine with the interaction terms.

State the corresponding level-spacing and anharmonicity expansions. If the candidate coefficient is correct, they should include

\[
\frac{E_{n+1}-E_n}{V}
=
\sqrt3\,\eta^{2/3}
-\frac{n+1}{6}
+O(\eta^{-2/3})
\]

and

\[
\frac{E_{n+2}-2E_{n+1}+E_n}{V}
=
-\frac16+O(\eta^{-2/3}).
\]

Distinguish clearly among:

- exact operator identities;
- formal Rayleigh–Schrödinger asymptotics;
- estimates that have actually been proved;
- conjectural consequences of the global Olver connection problem.

### Next coefficient

Attempt to derive the coefficient multiplying \(\eta^{-2/3}\). Include every contribution of the relevant perturbative order, including as applicable:

- the further expansion of \(r\), \(\Omega\), and the exact quadratic energy;
- finite-\(r\) corrections to the Bogoliubov coefficients;
- corrections to the cubic second-order denominators and vertices;
- second-order quartic terms;
- mixed cubic–quartic terms;
- third- and fourth-order perturbative terms containing the cubic interaction;
- all parity cancellations.

The result, if obtained, must be an exact expression in \(n\) and \(\delta\), checked symbolically. If it is not obtained, record the exact unfinished finite sum rather than replacing it with an unspecified \(O(\eta^{-2/3})\) calculation.

Create or extend an exact symbolic verifier, preferably as

```text
scripts/08d_verify_higher_energy.py
```

and add focused tests, preferably in

```text
tests/test_08d_higher_energy.py
```

Use exact SymPy arithmetic, including exact \(\sqrt3\). Tests must check polynomial identities for symbolic \(n,\delta\), not merely several floating-point examples.

## Part II — Undo every transformation back to \(\Psi\)

Replace the premature labels \(W_{\mathrm{reg}}\) and \(W_{\mathrm{sing}}\) by the neutral notation

\[
W_1,\qquad W_2.
\]

Do not call either Weber solution regular or singular before undoing every transformation.

Starting from the transformations already used in the manuscript, derive and display the complete pullback

\[
\boxed{
\Psi(z)=
t^{1/2-B_2}
\exp\!\left(\frac{B_1}{2t^2}\right)
\left(\frac{d\zeta}{dx}\right)^{-1/2}
W(\zeta(x)),
}
\]

with

\[
z=t^2,\qquad t=\eta^{1/6}x,\qquad
B_1=2\eta,\qquad B_2=2\delta.
\]

Near \(x=0\), use the full endpoint information, including the logarithmic term,

\[
u\int^x\sqrt{Q_u(s)}\,ds
=
-\frac{u}{x^2}
-2(1-\delta)\log x+O(1),
\]

together with

\[
\zeta\sim\frac{\pm i\sqrt2}{x},
\qquad
\left(\frac{d\zeta}{dx}\right)^{-1/2}
\sim {\rm const}\,x.
\]

For a consistent sector and square-root branch, show explicitly that the two Weber behaviours may be normalized so that

\[
W_1
\sim
x^{-3/2+2\delta}
\exp\!\left(-\frac{u}{x^2}\right),
\]

\[
W_2
\sim
x^{5/2-2\delta}
\exp\!\left(\frac{u}{x^2}\right).
\]

After applying the complete pullback, prove at the formal endpoint level that

\[
\mathcal T_uW_1\sim1,
\]

whereas

\[
\mathcal T_uW_2
\sim
x^{4-4\delta}\exp\!\left(\frac{2u}{x^2}\right)
\sim
z^{2-2\delta}\exp\!\left(\frac{2\eta}{z}\right).
\]

Explain that changing the square-root or action branch exchanges the labels \(W_1,W_2\), but does not change the invariant distinction between cancellation and enhancement of the gauge exponential.

For a general continued solution, display

\[
\Psi(z;E)
\sim
C_1(E)\,[1+\cdots]
+
C_{\mathrm{ess}}(E)\,
z^{2-2\delta}
\exp\!\left(\frac{2\eta}{z}\right)[1+\cdots].
\]

State explicitly:

- a generic Weber linear combination retains the essential singularity;
- the cancellation is not automatic;
- local formal cancellation does not prove global holomorphic patching;
- Stokes continuation can reintroduce a \(W_2\) component;
- the vanishing of its global coefficient is the proposed quantization condition.

Ensure that this discussion is consistent with the earlier \(\Phi\mapsto\Psi\) formulas and does not duplicate them without explaining the relation.

## Part III — A precise conjecture for \(C_{\mathrm{ess}}\)

Add a numbered conjecture to the manuscript, with a title such as

```text
Conjecture (Global compensated-to-essential connection coefficient)
```

Use \(W_1,W_2\), not \(W_{\mathrm{reg}},W_{\mathrm{sing}}\).

Let \(W_1^{(0)},W_2^{(0)}\) and \(W_1^{(m)},W_2^{(m)}\) denote canonically normalized bases in the initial and terminal origin sectors of the proposed physical domain chain. Normalize them through the complete pullback by

\[
\mathcal T_uW_1^{(j)}\sim1,
\qquad
\mathcal T_uW_2^{(j)}
\sim
z^{2-2\delta}e^{2\eta/z}.
\]

Let \(\mathcal A_{\Gamma_{\mathrm{phys}}}\) denote analytic continuation along the conjectural physical sheet-exchanging chain. Define

\[
\mathcal A_{\Gamma_{\mathrm{phys}}}W_1^{(0)}
=
C_1(E;u,\delta)W_1^{(m)}
+
C_{\mathrm{ess}}(E;u,\delta)W_2^{(m)}
\]

and therefore

\[
\boxed{
C_{\mathrm{ess}}(E;u,\delta)
=
\frac{
\mathscr W_\zeta\!\left(
\mathcal A_{\Gamma_{\mathrm{phys}}}W_1^{(0)},
W_1^{(m)}
\right)}
{
\mathscr W_\zeta\!\left(
W_2^{(m)},W_1^{(m)}
\right)}.
}
\]

Check the Wronskian order and the resulting sign. Explain why the zero set is unchanged by nonzero renormalizations of the canonical bases.

The conjecture must state that:

1. the required finite canonical domain chain exists;
2. the relevant sectorial solutions and continuation operator exist with the stated normalizations;
3. physical conjugation and sheet symmetries reduce the cancellation conditions to
   \[
   C_{\mathrm{ess}}(E;u,\delta)=0;
   \]
4. this condition is equivalent to patching into a single-valued holomorphic germ at \(z=0\);
5. on the physical slice its zeros, with multiplicities, coincide with
   \[
   \Delta_{\mathrm{WI}}
   \left(2\eta,2\delta,-\frac{2E}{V},2\eta\right)=0;
   \]
6. equivalently, locally in \(E\), there is a holomorphic nonvanishing factor \(G\) such that
   \[
   C_{\mathrm{ess}}
   =
   G\,
   \Delta_{\mathrm{WI}}
   \left(2\eta,2\delta,-\frac{2E}{V},2\eta\right);
   \]
7. the expected Weber form is
   \[
   C_{\mathrm{ess}}(E;u,\delta)
   =
   \frac{A(E;u,\delta)}{\Gamma[-p_u(E)]}
   +R(E;u,\delta),
   \]
   with \(A\neq0\) and conjecturally
   \[
   R=O(u^{-1}A)
   \]
   uniformly near a fixed level.

This entire statement must be labelled explicitly as a conjecture. Do not present the domain chain, the equivalence with \(\Delta_{\mathrm{WI}}\), or the \(O(u^{-1})\) connection remainder as proved.

If the \(O(1)\) energy coefficient is verified, include it as the energy prediction associated with the conjecture, while stating that its independent operator derivation does not prove the Olver connection conjecture.

Do not use the continued-fraction representation of \(\Delta_{\mathrm{WI}}\) in this section.

## Manuscript discipline

Integrate the new material into the mathematical narrative rather than appending disconnected notes.

Remove all occurrences in the manuscript of internal workflow labels such as “Stage”, “stage 08”, “prompt”, “Codeks”, “Codex”, or similar project-management language. Internal filenames may retain their established numbering, but the published manuscript must not expose it.

Preserve all correct qualifications from 08c concerning:

- the unproved global comparison-domain chain;
- the absence of a proved global Olver error estimate;
- the distinction between the exact entireness determinant and the conjectural Olver coefficient;
- fixed \(n\) versus growing \(n\);
- formal endpoint asymptotics versus actual sectorial solutions.

Do not make cosmetic rewriting the main output.

## Required new artifacts

Create all four of the following new artifacts:

```text
prompt_08d_higher_energy_terms_origin_connection.diff
prompt_08d_higher_energy_terms_origin_connection.log
reports/08d_higher_energy_terms_origin_connection.tex
reports/08d_higher_energy_terms_origin_connection.pdf
```

Create the `reports/` directory if it does not exist.

The standalone `.tex` report must be self-contained and compilable. It must contain:

- the displaced-oscillator derivation;
- the separate cubic and quartic corrections;
- the resulting energy expansion;
- any completed calculation of the \(\eta^{-2/3}\) coefficient;
- the full \(W\mapsto\Psi\) pullback;
- the cancellation/enhancement calculation;
- the precise definition and statement of the conjecture;
- a final table distinguishing proved, formally derived, conjectured, and still open statements.

Compile it to the required PDF and inspect the rendered PDF for broken equations, overfull text, missing symbols, or page-layout defects.

Also rebuild the canonical manuscript PDF according to the repository’s established procedure. Keep any legacy synchronized manuscript copy synchronized only if that is already an explicit repository convention.

The `.diff` file must be a valid unified textual diff covering all modified and newly created text/source files. Do not include PDF binary data in it. Since staging is forbidden, include untracked textual files by a safe no-index or equivalent unified-diff procedure.

The `.log` file must record:

- repository path and initial status;
- files inspected;
- files created and modified;
- exact formulas obtained;
- status of the \(O(1)\) coefficient;
- status of the \(\eta^{-2/3}\) coefficient;
- symbolic verification results;
- test commands and results;
- LaTeX build commands and results;
- PDF inspection result;
- search result for forbidden internal manuscript terminology;
- final `git status -sb`;
- a clear list of theorem-level results, formal results, conjectures, and remaining gaps.

Do not manufacture a successful result. If the next energy coefficient remains unfinished, state exactly where the calculation stops.

## Verification

At minimum run:

- the new focused 08d tests;
- the existing strong-drive tests;
- the full test suite if its runtime remains reasonable;
- the repository’s LaTeX build;
- bibliography checks required by the existing build;
- `git diff --check`;
- a manuscript search for internal workflow terminology;
- a check that all four required artifacts exist and are nonempty;
- a check that the standalone `.tex` reproduces its `.pdf`;
- a final clean inspection of the generated PDF pages.

Do not silence warnings without investigating them. Distinguish harmless pre-existing warnings from new failures.

## Completion criterion

The task is complete only if:

1. the full \(O(1)\) coefficient has been derived and independently verified or decisively falsified;
2. the nonlinear dependence on \(n\) has been made explicit;
3. the complete \(W\mapsto\Psi\) pullback has been displayed;
4. cancellation and enhancement of the essential exponential have been shown algebraically;
5. \(W_1,W_2\) replace the premature regular/singular labels;
6. \(C_{\mathrm{ess}}\) has a precise Wronskian definition;
7. the conjectural quantization condition is stated without being promoted to a theorem;
8. the manuscript and standalone report compile;
9. the required `.diff`, `.log`, `.tex`, and `.pdf` files have been created;
10. no commit, push, tag, release, staging operation, or remote change has been performed.

Finish with a concise summary containing the principal new formula, the exact status of the next coefficient, the status of the conjecture, the paths of all four new artifacts, the tests performed, and the final Git status.
