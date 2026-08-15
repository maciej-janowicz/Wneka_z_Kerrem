# Prompt 08b — Correct the strong-drive Olver analysis and its verification

## Repository and working rules

Work in the existing local repository:

```text
~/Dokumenty/Prace_i_dnie/Wnęka_z_Kerrem
```

This is a narrowly scoped correction of the still-uncommitted result of prompt 08a. Inspect the current working tree, the manuscript, `docs/strong_drive_olver_comparison.md`, `scripts/08a_verify_strong_drive.py`, `tests/test_strong_drive.py`, the 08a prompt copy, and the existing 08a review artifacts before editing.

Preserve all correct 08a work. Do not revert, replace, or redesign the strong-drive analysis. Make only the mathematical corrections and qualifications specified below, plus any directly necessary consistency edits.

Do not stage, commit, push, reset, restore, clean, initialize, clone, or change any Git remote. The user alone performs commits and pushes. Do not use continued fractions, direct or truncated Hamiltonian-matrix diagonalization, Padé or Hermite–Padé approximants, or Fedoryuk's method.

## Goal and acceptance status

The present 08a result is not yet accepted. Correct three mathematical errors, strengthen the symbolic regression test so that it detects the operator error, qualify two global statements that are currently stronger than the analysis proves, rebuild and inspect the manuscript, and overwrite the existing 08a `.diff` and `.log` so that they describe the corrected complete working tree.

Do not expand the task into a new attempt to compute the unresolved global Weber connection coefficient. Do not claim that the Olver quantization programme has been completed. The global connection problem remains open unless an actual proof is supplied; merely renaming, defining, or postulating a connection coefficient is not such a proof.

## Correction 1: double-root calculation

The turning-point polynomial is

\[
P(y;e)=1+2ey^2-2y^3.
\]

Correct every occurrence of the erroneous derivative relation. The exact derivative is

\[
P_y(y;e)=4ey-6y^2=2y(2e-3y).
\]

For a nonzero double root,

\[
e=\frac32y.
\]

Substitution into $P=0$ gives

\[
1+y^3=0.
\]

On the real branch,

\[
y=-1,
\qquad
e_0=-\frac32,
\]

and hence

\[
P\!\left(y;-\frac32\right)
=1-3y^2-2y^3
=-(y+1)^2(2y-1).
\]

The previous final values $y=-1$ and $e_0=-3/2$ are correct; only their displayed derivation was wrong. Correct the manuscript, derivation note, report, and any explanatory comments without suggesting that the leading energy coefficient has changed.

Add explicit exact symbolic assertions for $P_y$, the nonzero-double-root relation, and $1+y^3=0$, not only substitution checks at the already known solution.

## Correction 2: exact Liouville remainder

The manuscript defines

\[
p(x)=\frac{d\zeta}{dx},
\qquad
W=p^{1/2}w,
\]

equivalently $w=p^{-1/2}W$. For

\[
w_{xx}=\bigl[u^2f(x)+u g(x)+h(x)\bigr]w
\]

and the comparison mapping

\[
f(x)\left(\frac{dx}{d\zeta}\right)^2
=\zeta^2-\zeta_0^2,
\]

the transformed equation has the exact correction

\[
\psi(\zeta)=
h(x(\zeta))\left(\frac{dx}{d\zeta}\right)^2
+
\left(\frac{dx}{d\zeta}\right)^{1/2}
\frac{d^2}{d\zeta^2}
\left(\frac{dx}{d\zeta}\right)^{-1/2}.
\]

Equivalently, in terms of $p=d\zeta/dx$, the Liouville contribution is

\[
p^{-1/2}\frac{d^2}{d\zeta^2}p^{1/2}.
\]

The current manuscript instead contains the inverse expression. Correct it everywhere, including the derivation note and 08a report. Re-derive it directly by differentiating $w=p^{-1/2}W$; do not rely only on pattern matching with a standard formula.

Add a deterministic symbolic identity check. One acceptable equivalent $x$-derivative form is

\[
-\frac34p^{-4}(p_x)^2+\frac12p^{-3}p_{xx}.
\]

Verify that the implemented expression agrees with the displayed $\zeta$-derivative formula. Review all subsequent definitions of $R_u$, the variation-of-constants equation, and the conditional error-control integral. Change them wherever the reversed Liouville term propagated. Do not promote the conditional error estimate to a proved global bound: uniform finiteness of the required variation on a domain connecting the origin and outer sectors remains unproved.

## Correction 3: displaced-oscillator consistency check

For $F=|F|>0$, use

\[
\frac HV=
\frac12a^{\dagger 2}a^2+
\delta a^\dagger a+
\eta(a^\dagger+a),
\qquad
a=b-r,
\qquad
r^3+\delta r=\eta.
\]

Expand the normally ordered operator exactly. The linear term must cancel, and the result must be

\[
\begin{aligned}
\frac HV={}&
\left(\frac12r^4+\delta r^2-2\eta r\right)
+(2r^2+\delta)b^\dagger b
+\frac{r^2}{2}\left(b^{\dagger 2}+b^2\right)\\
&-r\left(b^{\dagger 2}b+b^\dagger b^2\right)
+\frac12b^{\dagger 2}b^2.
\end{aligned}
\]

In particular, the exact quadratic coefficient is

\[
A=2r^2+\delta,
\]

not $2r^2+\delta-1$. Therefore the quadratic Bogoliubov frequency and energy are

\[
\Omega=\sqrt{(2r^2+\delta)^2-r^4},
\]

\[
\frac{E_n^{(2)}}V=
\frac12r^4+\delta r^2-2\eta r
+\Omega\left(n+\frac12\right)
-\frac{2r^2+\delta}{2}.
\]

Correct the manuscript, derivation note, script, tests, and report. State explicitly that this correction changes terms at order $O(1)$, but does not change the two displayed fixed-$n$ coefficients

\[
\frac{E_n}{V}
=-\frac32\eta^{4/3}
+\left[\delta+\sqrt3\left(n+\frac12\right)-1\right]\eta^{2/3}
+O(1).
\]

Do not infer or publish the actual $O(1)$ coefficient from the quadratic Hamiltonian, because the cubic and quartic fluctuation terms also contribute at that order.

### Required stronger regression test

The existing test passed despite the wrong $A$, because it checked only the $\eta^{4/3}$ and $\eta^{2/3}$ coefficients. Strengthen it so that this exact error cannot recur.

At minimum, the verification must independently expand the shifted normally ordered Hamiltonian and assert exactly that:

- the coefficient of $b^\dagger+b$ is zero after using $r^3+\delta r=\eta$;
- the coefficient of $b^\dagger b$ is $2r^2+\delta$;
- the anomalous quadratic coefficient is $r^2/2$ for each of $b^{\dagger2}$ and $b^2$;
- the cubic and quartic coefficients agree with the exact formula above;
- $\Omega^2=(2r^2+\delta)^2-r^4$;
- the corrected quadratic check still reproduces the two stated strong-drive coefficients.

Use noncommutative symbols or an explicit normally ordered monomial dictionary; a commutative polynomial expansion that silently identifies distinct operator orderings is insufficient.

## Qualification 1: physical contour and turning-point pair

The present text states as fact that the pair $x=\pm i$ is the saddle traversed by the physical continuation contour and that the contour passes through this pair. The local algebra and negative classical displacement motivate this identification, but the report itself admits that the global Weber connection and the required progressive domain have not been proved.

Replace categorical statements by a precise conditional formulation. For example, describe $x=\pm i$ as the coalescing pair selected by the local strong-drive geometry and suggested as physically relevant by the negative displacement and covering-sheet structure. State that identifying it with the actual global continuation contour requires the still-missing construction of the progressive paths and global connection map.

Do not remove the useful sheet-geometric argument, but do not present it as a completed global contour proof.

## Qualification 2: origin-sector patching and quantization status

Qualify the assertion that the regular formal branch patches to a holomorphic germ precisely when all inadmissible Stokes coefficients vanish. State it conditionally on the existence of the required canonical sectorial solutions with the stated asymptotics and on their covering a punctured neighbourhood of the irregular origin. Distinguish carefully between:

1. formal sectorial definitions of the coefficients $s_j(E)$;
2. a proved global construction of the canonical sectorial solutions;
3. evaluation of the connection coefficients;
4. reduction to a single physical scalar condition;
5. the previously established exact entireness condition
   \[
   \Delta_{\mathrm{WI}}(2\eta,2\delta,-2E/V,2\eta)=0.
   \]

Do not describe the last condition as a newly derived Olver quantization formula. It is an exact fallback inherited from the earlier entireness theorem. The individual Stokes multipliers and the global Weber connection coefficient have been defined but not evaluated, and a scalar Olver connection condition equivalent to the spectrum has not yet been derived.

Audit the abstract, introduction, roadmap, section headings, conclusions, and final report for any wording that says or implies that 08a completes the Olver quantization programme. Replace it with the strongest accurate statement: the local Weber comparison structure and the leading fixed-$n$ strong-drive energy expansion have been identified, with the second coefficient conditional on the unresolved global Weber connection.

## Preserve the correct 08a results

Unless an independently verified inconsistency is found, preserve the following:

- $\eta=|F|/V\to\infty$, with fixed $\delta=\hbar\omega_0/V$;
- $t=\eta^{1/6}x$, $u=\eta^{2/3}$, and $E/V=\eta^{4/3}e$;
- the scaled coefficients
  \[
  f=4x^{-6}+8ex^{-2}-8,
  \qquad
  g=-8(1-\delta)x^{-4},
  \qquad
  h=(4\delta^2-4\delta+3/4)x^{-2};
  \]
- the Weber/parabolic-cylinder classification for the local coalescing-turning-point problem;
- the modified-Bessel equation as an outer comparison only;
- the warning that $4\eta^2/t^6$ is leading in the strong-drive turning region;
- the fixed-$n$ scope of the energy expansion;
- the distinction between proved and conditional error statements;
- the absence of internal workflow language from the publication manuscript.

Do not alter equation numbering unnecessarily. Update cross-references if a correction forces a numbering change.

## Documentation and review artifacts

Update all affected publication and development files consistently, including at least:

```text
manuscript/manuscript.tex
docs/strong_drive_olver_comparison.md
scripts/08a_verify_strong_drive.py
tests/test_strong_drive.py
```

Retain a copy of this prompt as:

```text
prompts/08b_correct_strong_drive_olver_analysis.md
```

Do not create new `prompt_08b_*.diff` or `prompt_08b_*.log` artifacts. Instead overwrite:

```text
prompt_08a_strong_drive_olver_comparison_quantization.diff
prompt_08a_strong_drive_olver_comparison_quantization.log
```

They remain the review artifacts for the complete, corrected 08a change set. The `.diff` must be regenerated non-destructively against `HEAD` from the final working tree and must contain the complete reviewable textual change set, not merely the incremental 08b corrections. Do not attempt to include the `.diff` artifact within itself. The `.log` must describe only the corrected final state and must explicitly record:

- all three corrections and their exact formulas;
- why the first two energy coefficients are unchanged;
- the strengthened exact operator test;
- the corrected Liouville identity check;
- the conditional status of the global Weber error bound;
- the qualified status of the physical contour;
- the precise distinction between the previous entireness condition and the unresolved Olver connection condition;
- which assertions are proved, conditional, defined only, or still open.

Remove obsolete erroneous formulas from both artifacts. Verify that searches for `4y(e-3y)`, `e=3y`, `1+4y^3`, `2r^2+\delta-1`, and the reversed Liouville term return no occurrence in publication or derivation text except, if unavoidable, an explicitly labelled description of the corrected error in the final report.

## Verification, build, and visual inspection

Run:

1. the corrected deterministic symbolic verifier directly;
2. its focused regression test;
3. the complete existing test suite;
4. the repository's established full manuscript build.

Inspect the LaTeX and bibliography logs for errors, undefined references, bibliography failures, and new overfull or underfull boxes. Render and visually inspect every changed page and its neighbours. Confirm that equations, page breaks, headings, and cross-references remain readable and that all fonts are embedded.

Repeat the case-insensitive searches for internal publication workflow language, including `Stage`, prompt identifiers, and internal stage names. Such terms may occur in filenames under `prompts/` and in review artifacts, but not in publication prose or the rendered manuscript.

Verify that both overwritten 08a review artifacts exist, are nonempty, and correspond to the final corrected working tree.

## Strict exclusions

Do not:

- change the physical regime to small $|F|/V$;
- claim that the global Weber connection coefficient has been computed;
- claim that the Olver quantization condition has been reduced to a proved scalar equation when it has not;
- relabel the pre-existing $\Delta_{\mathrm{WI}}=0$ condition as a new Olver result;
- promote the conditional error estimate to a global theorem;
- compute an $O(1)$ energy coefficient from the quadratic Bogoliubov Hamiltonian alone;
- introduce new numerical spectral evidence;
- use continued fractions, matrix diagonalization, Padé methods, or Fedoryuk's method;
- create separate 08b `.diff` or `.log` files;
- stage, commit, push, reset, restore, clean, or otherwise alter the Git index or history.

## Final interactive response

Report the corrected mathematical status rather than the intended status. List every modified or created file; reproduce the corrected double-root equations, Liouville remainder, exact quadratic Hamiltonian, and retained energy expansion; state clearly what is proved and what remains conditional; give the paths of the overwritten 08a `.diff` and `.log`; report all test and build results and the pages visually inspected; confirm the absence of internal workflow language from the manuscript; and confirm compliance with all exclusions.
