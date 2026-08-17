# Prompt 08e — Complete the \(\eta^{-2/3}\) energy coefficient and correct the symbolic assumptions

## Repository and working rules

Work exclusively in the existing repository

```text
~/Dokumenty/Prace_i_dnie/Wnęka_z_Kerrem
```

Begin by printing the absolute repository path and inspecting the complete working tree, including all uncommitted 08c and 08d results, the manuscript, both strong-drive documents, the 08d report, symbolic scripts, tests, and build procedure.

The tree may still contain uncommitted work from 08c and 08d. Preserve it exactly. Do not reset, restore, clean, delete, overwrite unrelated files, initialize or clone a repository, or change a remote.

Do not stage, commit, push, tag, create a release, or otherwise modify Git history or the index. Git operations belong to the user.

Save this prompt, if it is not already present verbatim, as

```text
prompts/08e_complete_eta_minus_two_thirds_energy.md
```

This task is a mathematical continuation of 08d. Its principal purpose is to evaluate the complete coefficient multiplying \(\eta^{-2/3}\), not to rewrite the exposition or enlarge the list of open problems.

## Established result and target

For

\[
\eta=\frac{|F|}{V}\to\infty,
\qquad
\delta=\frac{\hbar\omega_0}{V}\in\mathbb R\quad\text{fixed},
\qquad n\in\mathbb N_0\quad\text{fixed},
\]

08d established the independently verified formal operator expansion

\[
\frac{E_n}{V}
=-rac32\eta^{4/3}
+\left[\delta+\sqrt3\left(n+\frac12\right)-1\right]\eta^{2/3}
+\frac{\delta(1-2\delta)}6
-\frac{6n^2+6n+1}{72}
+O(\eta^{-2/3}).
\]

The mandatory target of 08e is an exact closed expression \(K_n(\delta)\) such that, as a formal fixed-level expansion,

\[
\boxed{
\frac{E_n}{V}
=-rac32\eta^{4/3}
+\left[\delta+\sqrt3\left(n+\frac12\right)-1\right]\eta^{2/3}
+\frac{\delta(1-2\delta)}6
-\frac{6n^2+6n+1}{72}
+K_n(\delta)\eta^{-2/3}
+O(\eta^{-4/3}).
}
\]

Do not guess \(K_n(\delta)\). Derive it by exact symbolic perturbation theory and verify it by an independent algebraic organization of the same finite contributions.

If a genuine inconsistency in the 08d coefficient is found, stop propagating it, identify the first incorrect equation, correct the manuscript, and record the correction explicitly. Agreement with 08d is evidence to be checked, not an axiom.

## Mandatory correction of symbolic assumptions

The 08d verifier currently declares \(n\), \(\delta\), and the expansion variable with the same nonnegative-integer assumptions. This is physically and mathematically inappropriate for \(\delta\).

Correct the declarations in the verifier and corresponding tests so that they express

```python
n = sp.symbols("n", integer=True, nonnegative=True)
delta = sp.symbols("delta", real=True)
eps = sp.symbols("eps", positive=True)
```

or an exactly equivalent set of assumptions. If separate expansion variables are used, distinguish clearly between

\[
\lambda=r^{-1}
\qquad\text{and}\qquad
\epsilon=\eta^{-1/3}.
\]

Do not impose \(\delta\ge0\): negative detuning is allowed. Rerun all 08d symbolic identities after this correction and verify that their values remain unchanged.

## Exact displaced and Bogoliubov form

Starting from

\[
\frac HV=rac12a^{\dagger2}a^2+\delta a^\dagger a
+\eta(a^\dagger+a),
\]

take

\[
a=b-r,qquad r^3+\delta r=\eta,qquad r>0.
\]

Recheck the exact identity

\[
\frac HV=C(r)
+(2r^2+\delta)b^\dagger b
+\frac{r^2}{2}(b^{\dagger2}+b^2)
-r\mathcal O_3
+\mathcal O_4,
\]

where

\[
C(r)=-\frac32r^4-\delta r^2,
\qquad
\mathcal O_3=b^{\dagger2}b+b^\dagger b^2,
\qquad
\mathcal O_4=\frac12b^{\dagger2}b^2.
\]

Use the real Bogoliubov transformation

\[
b=C_\lambda c+S_\lambda c^\dagger,
\]

with the branch \(C_\lambda>0\), \(S_\lambda<0\) for sufficiently small positive \(\lambda=r^{-1}\), and

\[
A=2r^2+\delta,
\qquad
\Omega=\sqrt{A^2-r^4},
\]

\[
C_\lambda^2=\frac12\left(\frac A\Omega+1\right),
\qquad
S_\lambda^2=\frac12\left(\frac A\Omega-1\right),
\qquad
2C_\lambda S_\lambda=-\frac{r^2}{\Omega}.
\]

Verify all signs directly by cancellation of the \(c^{\dagger2}+c^2\) term.

After diagonalizing the quadratic part, write the exact Hamiltonian as

\[
\frac HV
=E_{\rm vac}^{(2)}(r)
+\Omega N
-r\mathcal O_3(\lambda)
+\mathcal O_4(\lambda),
\qquad N=c^\dagger c,
\]

where

\[
E_{\rm vac}^{(2)}(r)=C(r)+\frac\Omega2-\frac A2.
\]

## Preferred perturbative organization

Use \(\lambda=r^{-1}\) and define the reduced fluctuation operator

\[
\mathcal K(\lambda)
=\lambda^2\left(\frac HV-E_{\rm vac}^{(2)}(r)\right)
=\omega(\lambda)N
-\lambda\mathcal O_3(\lambda)
+\lambda^2\mathcal O_4(\lambda),
\]

with

\[
\omega(\lambda)=\lambda^2\Omega
=\sqrt{3+4\delta\lambda^2+\delta^2\lambda^4}.
\]

Expand the complete operator, not merely its diagonal expectation value,

\[
\mathcal K(\lambda)
=K_0+\lambda K_1+\lambda^2K_2
+\lambda^3K_3+\lambda^4K_4+O(\lambda^5).
\]

This expansion must include:

- the \(\lambda^2\) and \(\lambda^4\) corrections to \(\omega(\lambda)N\);
- the \(\lambda^2\) correction to the Bogoliubov coefficients inside \(\mathcal O_3\), which contributes through \(K_3\);
- the \(\lambda^2\) correction to the Bogoliubov coefficients inside \(\mathcal O_4\), which contributes through \(K_4\);
- all signs and normal-ordering constants.

Do not infer the fourth-order energy from power counting alone.

## Recursive nondegenerate perturbation calculation

Implement intermediate-normalization Rayleigh–Schrödinger recursion for

\[
\mathcal K(\lambda)|\psi_n(\lambda)\rangle
=\kappa_n(\lambda)|\psi_n(\lambda)\rangle,
\]

\[
|\psi_n(\lambda)\rangle
=|n\rangle+\sum_{j=1}^4\lambda^j|\psi_n^{(j)}\rangle+O(\lambda^5),
\qquad
\langle n|\psi_n^{(j)}\rangle=0,
\]

\[
\kappa_n(\lambda)
=\sum_{j=0}^4\lambda^j\kappa_{n,j}+O(\lambda^5).
\]

Derive the recursion from the eigenvalue equation and implement it rather than copying a fourth-order formula from a table. At each order, retain every number state reachable from \(|n\rangle\). The operator shifts are finite, so the calculation terminates.

Verify explicitly that

\[
\kappa_{n,1}=\kappa_{n,3}=0
\]

by parity, rather than deleting them in advance.

The physical energy reconstructed from this organization is

\[
\frac{E_n}{V}
=E_{\rm vac}^{(2)}(r)+r^2\kappa_n(r^{-1}).
\]

Expand it through \(r^{-2}\).

## Independent verification through the finite sums left by 08d

Independently evaluate the explicit finite contributions catalogued in 08d:

1. finite-\(r\) corrections to the first-order quartic expectation;
2. finite-\(r\) corrections to the second-order cubic vertices and denominators;
3. the second-order \(V_4^2\) sum;
4. all normalized third-order \(V_3^2V_4\) permutations;
5. the normalized fourth-order \(V_3^4\) sum;
6. all normalization-subtraction terms.

With leading vertices

\[
X_{jk}=\langle j|V_3/r|k\rangle,
\qquad
Y_{jk}=\langle j|V_4|k\rangle,
\qquad
D_k=\sqrt3(n-k),
\]

audit the unfinished expression recorded in 08d, including the order and sign of every denominator and subtraction term. Do not assume that the recorded formula is complete merely because it is finite.

Compare the result from this explicit-sum organization with \(\kappa_{n,4}\) from the recursive calculation. They must simplify to the same exact expression. If they do not, diagnose the discrepancy before editing the manuscript.

## Conversion from \(r\) to \(\eta\)

Use a separate symbol \(\epsilon=\eta^{-1/3}\). Solve

\[
r^3+\delta r=\eta
\]

to sufficient order and verify by substitution. In particular audit

\[
r=\eta^{1/3}-\frac\delta3\eta^{-1/3}
+\frac{\delta^3}{81}\eta^{-5/3}
+O(\eta^{-7/3}).
\]

Substitute the series into the complete energy through \(r^{-2}\), re-expand in powers of \(\eta^{-2/3}\), and extract \(K_n(\delta)\). Do not simply identify the coefficient of \(r^{-2}\) with the final coefficient until all lower-order terms have been re-expanded.

The 08d calculation found the following contribution from the exact quadratic energy:

\[
K^{(2)}_n(\delta)
=\frac{\delta^3}{27}
+\frac{\sqrt3\,\delta^2 n}{18}
-\frac{\delta^2}{9}
+\frac{\sqrt3\,\delta^2}{36}.
\]

Re-derive this expression independently and then add all interaction contributions.

Do not assume in advance the polynomial degree of \(K_n(\delta)\) in either \(n\) or \(\delta\).

## Symbolic implementation and validation

Create a new exact verifier, preferably

```text
scripts/08e_verify_eta_minus_two_thirds.py
```

and focused tests, preferably

```text
tests/test_08e_eta_minus_two_thirds.py
```

The verifier must:

- use exact SymPy arithmetic;
- keep \(\sqrt3\) exact;
- use symbolic \(n\) and real symbolic \(\delta\);
- implement ladder actions algebraically, not through numerical matrix diagonalization;
- derive the perturbative coefficients recursively through fourth order;
- calculate the explicit finite-sum form independently;
- assert equality of the two results;
- reconstruct the energy first in \(r\), then in \(\eta\);
- print the final factorized and expanded forms of \(K_n(\delta)\);
- print the resulting corrections to the level spacing and second difference.

The tests must include:

- the corrected symbolic assumptions from 08d;
- unchanged verification of the \(O(1)\) coefficient;
- equality of recursive and explicit-sum fourth-order results;
- exact evaluation for several low levels \(n=0,1,2,3,4\), with automatic annihilation of forbidden negative-number states;
- symbolic agreement of the reconstructed energy coefficient;
- the first and second finite differences of \(K_n(\delta)\);
- parity cancellation of all odd orders.

Testing several levels is a boundary-state check, not polynomial interpolation and not a substitute for the symbolic identity.

Do not use a truncated Hamiltonian eigenvalue calculation, floating-point eigenvalues, continued fractions, Padé or Hermite–Padé approximants, or numerical fitting as proof or evidence for the coefficient.

## Manuscript integration

Update `manuscript/manuscript.tex` and the relevant strong-drive documentation.

Replace the unfinished \(\eta^{-2/3}\) finite-sum paragraph by:

- the evaluated exact coefficient \(K_n(\delta)\);
- a concise but reproducible explanation of the perturbative bookkeeping;
- the final energy expansion through \(\eta^{-2/3}\);
- the corresponding expansion of
  \[
  \frac{E_{n+1}-E_n}{V};
  \]
- the corresponding second difference
  \[
  \frac{E_{n+2}-2E_{n+1}+E_n}{V}.
  \]

Retain enough of the finite-sum structure to make clear which fourth-order contributions were included, but do not leave a page of unevaluated sums after they have been evaluated.

State the mathematical status accurately:

- the displaced Hamiltonian and algebraic transformations are exact;
- the coefficient is an exactly evaluated coefficient of a formal fixed-\(n\) Rayleigh–Schrödinger expansion;
- no rigorous operator remainder uniform in \(n\) has been established unless 08e actually proves one;
- the result is independent evidence for the energy expansion and is not a proof of the global Olver connection conjecture.

Update the energy prediction inside or immediately following the existing conjecture so that it contains the newly derived coefficient, while keeping the global domain chain, the equivalence with \(\Delta_{\rm WI}\), and the Weber connection remainder explicitly conjectural.

Preserve the complete \(W\mapsto\Psi\) pullback, the neutral labels \(W_1,W_2\), the cancellation/enhancement calculation, and the Wronskian definition of \(C_{\rm ess}\). Do not reopen or weaken those completed 08d results unless an actual algebraic error is demonstrated.

Remove no valid qualifications inherited from 08c or 08d.

Ensure that the publication manuscript contains no internal workflow terms such as “Stage”, “prompt”, “Codex”, “Codeks”, or task numbers.

## Required new artifacts

Create all four new artifacts:

```text
prompt_08e_complete_eta_minus_two_thirds_energy.diff
prompt_08e_complete_eta_minus_two_thirds_energy.log
reports/08e_complete_eta_minus_two_thirds_energy.tex
reports/08e_complete_eta_minus_two_thirds_energy.pdf
```

The standalone report must be self-contained and must include:

- corrected symbol assumptions;
- exact Bogoliubov coefficients and their expansions;
- the recursive perturbation derivation through fourth order;
- the independent finite-sum verification;
- the conversion from \(r\) to \(\eta\);
- the final exact \(K_n(\delta)\);
- level-spacing and anharmonicity corrections;
- a status table separating exact identities, formal asymptotics, conjectures, and open problems.

Compile the report and inspect every rendered page.

Rebuild the canonical manuscript PDF by the established repository procedure and inspect all changed pages together with their neighbouring pages. Synchronize a legacy manuscript PDF only if that is already the repository convention.

The `.diff` file must be a valid unified textual diff covering the task’s modified and newly created source files. Do not place PDF binary data in the diff. Do not stage files merely to generate it.

The `.log` file must record:

- initial and final repository status;
- exact files inspected, modified, and created;
- the corrected SymPy assumptions;
- the recursive formulas used;
- every contribution to \(K_n(\delta)\);
- the two independently obtained forms and their exact equality check;
- the final energy, spacing, and second-difference expansions;
- test commands and results;
- LaTeX build commands and results;
- PDF rendering and inspection results;
- the final classification of claims;
- every unresolved issue.

## Verification

At minimum run:

```text
PYTHONPATH=src python scripts/08d_verify_higher_energy.py
PYTHONPATH=src python scripts/08e_verify_eta_minus_two_thirds.py
PYTHONPATH=src pytest -q tests/test_08d_higher_energy.py tests/test_08e_eta_minus_two_thirds.py tests/test_strong_drive.py
PYTHONPATH=src pytest -q
```

Also run:

- the manuscript build and bibliography procedure;
- the standalone-report build twice, confirming that the second build is up to date;
- `git diff --check`;
- a source and extracted-PDF search for forbidden workflow terminology;
- checks that all four required 08e artifacts exist and are nonempty;
- visual inspection of every report page and all changed manuscript pages;
- final `git status -sb`.

Do not suppress a failing test or simplify an expression by inserting the expected answer.

## Outcome discipline

The intended outcome is the explicit coefficient \(K_n(\delta)\). If the two independent calculations disagree, do not average them, choose the prettier expression, or report completion. Instead:

1. isolate the first perturbative order and matrix element at which they differ;
2. determine whether the recursive implementation, explicit fourth-order formula, Bogoliubov expansion, or \(r\mapsto\eta\) conversion is responsible;
3. correct the error if possible;
4. otherwise preserve the exact discrepancy and report an obstruction outcome.

An obstruction outcome is acceptable only after the complete recursive calculation has been attempted and the discrepancy has been reduced to a specific finite identity. Merely repeating the unevaluated sum from 08d is not an acceptable completion.

## Completion criterion

The task is complete only if:

1. the SymPy assumptions for \(n\), \(\delta\), and the expansion variables have been corrected;
2. all 08d identities still pass under the corrected assumptions;
3. perturbation theory has been carried recursively through fourth order;
4. the explicit finite sums have been evaluated independently;
5. the two methods agree exactly, or a precise finite obstruction has been isolated;
6. the conversion from \(r\) to \(\eta\) has been performed after assembling the complete energy;
7. the manuscript contains the explicit \(K_n(\delta)\), unless a documented obstruction prevents it;
8. the spacing and second-difference corrections have been stated;
9. the Olver connection conjecture remains clearly conjectural;
10. the required `.diff`, `.log`, `.tex`, and `.pdf` artifacts have been created and checked;
11. no staging, commit, push, tag, release, reset, clean, or remote operation has been performed.

Finish with a concise summary giving the final formula for \(K_n(\delta)\), the two verification routes, the test and build results, the paths of all four artifacts, the exact status of the Olver conjecture, and the final Git status.
