# Stage 07.1 — Repair the sectorial theorem and technical defects

Work in the existing Wneka_z_Kerrem repository, on the uncommitted result of Stage 07. This is a corrective stage, not a new asymptotic or visual stage.

Read AGENTS.md if it exists, README.md, the complete current manuscript, the complete Stage 05–07 documentation and prompts, and every source and test file touched by Stage 07. Read in full the current audit artifacts

`stage07_olver_uniform_asymptotics.diff`
`stage07_olver_uniform_asymptotics.log`

and inspect the actual working tree rather than reconstructing it from those artifacts. The working tree is authoritative. Do not discard or overwrite unrelated user changes. Do not commit or push anything.

## Purpose

Correct the uncommitted Stage 07 result before review and commit. There are three required repairs:

close the logical gap between solutions constructed along individual paths/rays and genuinely holomorphic sectorial solutions;

repair the malformed Markdown/LaTeX in the Stage 07 documentation and in the stored copy of the Stage 07 prompt;

replace circular or tautological tests by independent checks of the exact covering transformation and Volterra kernel.

Preserve the verified fixed-parameter Olver construction, explicit error bounds, first-coefficient calculation, and Stokes/anti-Stokes geometry unless a new check reveals a genuine mathematical error. Do not begin Stage 07a and do not create any plot. Do not introduce continued fractions, a spectral determinant, eigenvalue asymptotics, or a large-parameter limit. In particular, do not introduce \(|F|/V\) in this corrective stage.

## Part A — Audit the present theorem before editing

Start from the exact covering equation already verified in Stage 07,

\[
w''(t)=\{a_\sigma^2+g(t)\}w(t),\qquad
g(t)=-\frac{C}{t^2}-\frac{4H}{t^4}+\frac{B_1^2}{t^6},
\]

and the Volterra equation for

\[
w_\sigma(t)=e^{a_\sigma t}h_\sigma(t),
\]

with kernel

\[
K_\sigma(t,u)=\frac{e^{2a_\sigma(u-t)}-1}{2a_\sigma}.
\]

Verify again the sign/orientation condition actually required for the bound on this kernel. With paths oriented from t to infinity, the present formula requires

\[
\Re{a_\sigma(u-t)}\le 0,
\]

not an incompatible verbal statement about increase/decrease. Make the words, inequality, orientation, and exponential normalization agree everywhere.

Identify precisely what the current proof establishes. In particular, do not accept the phrase “a continuously varying family of admissible paths with nested tails” as a proof that the resulting objects form one holomorphic solution throughout a sector. Radial tails belonging to distinct angles are not nested.

## Part B — Prefer a genuine sectorial repair

The preferred result is still a theorem about actual holomorphic sectorial solutions. Do not weaken it to a merely raywise theorem unless the sectorial repair below is shown to fail for a precise reason.

Construct a concrete complex domain near covering-space infinity and a coherent family of integration paths on it. A promising route, which must be checked rather than quoted, is the following.

Choose a fixed progressive direction \(d\) with \(|d|=1\) and \(\Re(a_\sigma d)\le 0\) (use a strict inequality first if equality causes a uniformity problem).

Use translated parallel half-rays

\[
\Gamma_{\sigma,d}(t)=\{t+sd:s\ge0\}
\]

inside a simply connected branch domain avoiding \(t=0\), or a rigorously specified deformation of these paths.

Specify a sector, half-plane, truncated sector, or finite covering by such domains on which every complete tail remains in the domain and

\[
\sup_{t\in\Omega}\int_{\Gamma_{\sigma,d}(t)}|g(u)|\,|du|
\]

has the required local/uniform control for sufficiently large \(|t|\).

Define the Volterra operator on holomorphic functions in that domain. Prove that its successive approximations converge locally uniformly (and uniformly on each stated closed truncated subsector or other stated uniformity domain).

Deduce holomorphy from locally uniform convergence, justify differentiation with respect to \(t\), recover the differential equation, and prove the asymptotic normalization and uniqueness in the claimed class.

Nested tails are not mandatory if translated paths and analytic dependence on \(t\) give a correct proof. Conversely, do not retain “nested tails” as an ornamental hypothesis if the paths actually used do not possess that property.

Explain how fixed-direction domains cover each desired proper progressive sector, and how solutions obtained in overlapping domains agree. Agreement must follow from a proved uniqueness statement with compatible normalization, or from a valid contour-deformation/Cauchy argument; it must not be inferred from uniform raywise estimates alone. State branch and simply-connectedness assumptions explicitly.

Treat boundary directions with \(\Re(a_\sigma d)=0\) separately. Include them in the theorem only if the kernel, integral convergence, holomorphic construction, and uniform bounds remain valid. It is acceptable for the principal theorem to use proper closed subsectors and for a corollary to state a raywise boundary estimate.

Retain the explicit Stage 07 estimates only on domains where the proof gives them. If a fixed translated ray does not admit the simple radial majorant, derive a correct comparable bound for that path family and keep the radial formula as a corollary. Never transfer a radial integral estimate to a nonradial contour without proof.

### Mandatory fallback if the sectorial proof genuinely cannot be closed

If, after a serious attempt, the sectorial construction cannot be proved within this stage, do not conceal the failure and do not keep the present theorem unchanged. Then:

- state and prove a strictly raywise/pathwise theorem with an exact domain of uniformity;

- replace every unsupported use of “sectorial solution” and “holomorphic on a sector” in the manuscript and documentation;

- add an explicit unresolved lemma describing the missing gluing/analytic continuation statement needed before Stokes matrices, connection coefficients, or \(D(E)\) can be defined;

- explain in the log exactly why the preferred translated-path or contour argument failed.

Do not choose this fallback merely because it is shorter.

## Part C — Check the one-term remainder at the same rigor level

After repairing the leading theorem, recheck the claimed result

\[
w_\sigma(t)=e^{a_\sigma t}\left(1+\frac{C}{2a_\sigma t}+\rho_{1,\sigma}(t)\right),\qquad \rho_{1,\sigma}(t)=O(t^{-2}).
\]

Verify that the inhomogeneous Volterra equation for \(\rho_{1,\sigma}\) has the correct sign and that the displayed bound follows on the same coherent path family as the theorem. Distinguish clearly among:

- a bound for an individual ray;

- a bound uniform over a specified family;

- a holomorphic sectorial remainder.

Retain the coefficient and explicit residual majorant only after these checks.

## Part D — Repair all Markdown and stored prompt corruption

Repair `docs/stage07_olver_uniform_asymptotics.md` completely. Search for raw control characters and malformed mathematics, including the already observed damage to `\rho`, `\theta`, `\quad`, delimiters, backslashes, and inline math. Use proper Markdown mathematics consistently (`\(...\)` and `\[...\]`).

Repair `prompts/07_olver_uniform_asymptotics.md` as a faithful, well-formatted copy of the Stage 07 execution prompt. Restore whitespace, headings, lists, code blocks, LaTeX delimiters, braces, and backslashes. Do not silently rewrite its historical scope to match Stage 07.1; the stored Stage 07 prompt is an audit artifact and must continue to record what Stage 07 was asked to do.

Run a byte-level audit over all new or modified text files for forbidden raw control characters other than newline and tab; tabs must not occur inside LaTeX commands or prose. Also run git diff --check.

## Part E — Make the tests independent

Improve tests/test_olver.py and, only where useful, src/kerr_heun/olver.py. Avoid adding a symbolic dependency merely for this repair.

### Exact covering transformation

The test must not compute D, H, and C from the same closed formulas as the implementation and then compare the two dictionaries. Independently perform the substitution

\[
Y(t)=A(t)w(t),\qquad A(t)=t^{1/2-B_2}e^{B_1/(2t^2)},
\]

into the normalized exact equation for Y. One acceptable exact-arithmetic test uses Laurent-polynomial dictionaries and independently combines

\[
L=A'/A,\qquad A''/A=L'+L^2,
\]

with the transformed coefficients of Y' and Y. It must verify both that the w' coefficient vanishes and that every Laurent coefficient of the w equation is correct, for several exact rational parameter sets. The tested result must pass through the public implementation rather than merely compare two handwritten copies of the target formula.

### Volterra kernel

The kernel test must exercise `volterra_kernel`. Do not “verify” it by defining the expected exponential and then algebraically cancelling a handwritten derivative against itself. Check \(K(t,t)=0\), and independently approximate \(\partial_t K\) and \(\partial_t^2 K\) by stable centered finite differences at several nondegenerate complex points, or introduce a small exact derivative helper whose implementation is independently exercised. Verify

\[
K_{tt}+2a_\sigma K_t=0,
\]

and verify by differentiating the integral equation, with the endpoint term from K(t,t)=0, that it recovers

\[
h''+2a_\sigma h'=gh.
\]

Choose tolerances justified by the finite-difference scale if that route is used.

### Code clarity

Remove constructions such as

```python
(B2 * 0 + 3) / (B2 * 0 + 4)
```

used only to manufacture 3/4. Replace them with a small, clearly named type-preserving helper or another readable solution compatible with the exact numeric types actually supported by the project. Do not claim support for arbitrary scalar types unless the tests substantiate it. Format long return expressions and comprehensions readably.

Retain and strengthen the existing tests for both signs, multiple parameter sets, Stage 05 coefficient agreement, explicit majorants, and invalid inputs.

## Part F — Manuscript language and scope

Make the theorem title, statement, proof, subsequent asymptotic formula, and limitations agree exactly with the rigor achieved in Part B. If the full sectorial repair succeeds, say explicitly that the constructed functions are holomorphic on the stated domains and explain the overlap/gluing argument. If only the fallback succeeds, do not leave a sectorial claim elsewhere in the paper.

Preserve these Stage 07 boundaries:

- locating equal-modulus and maximal-separation rays does not compute Stokes multipliers;

- “dominant” refers only to relative exponential size and does not by itself imply exclusion from Bargmann space;

- no analytic/entire origin solution, connection coefficient, spectral determinant, or quantization condition has yet been constructed;

- no large parameter is used;

- Stage 07a visualization is not part of this correction.

## Verification

Run at minimum:

- the focused Stage 05–07 tests;

- the complete test suite;

- the canonical manuscript build;

- log checks for errors, undefined references/citations, overfull and underfull boxes, and relevant warnings;

- rendering and visual inspection of every manuscript page affected by the correction, plus one page before and after;

- the raw-control-character audit on modified/new text files;

- `git diff --check` and `git diff --cached --check`;

- `git status --short`.

Do not stage, commit, or push.

## Audit artifacts and final report

Update the Stage 07 diff and log so that they describe the corrected working tree rather than preserving superseded claims. Also create:

`stage07_1_theorem_and_technical_corrections.diff`
`stage07_1_theorem_and_technical_corrections.log`

The Stage 07.1 log must state:

- whether the genuine sectorial theorem was proved or the raywise fallback was necessary;

- the exact complex domains and path families used;

- the proof of holomorphy and overlap agreement, if claimed;

- which estimates are uniform and on what sets;

- every repaired Markdown/control-character defect;

- how the new tests are independent of the implementation;

- every changed or added file;

- all test, build, visual, and Git-check results;

- every unresolved mathematical or technical issue.

The final response must be concise but must not describe Stage 07 as 
ready for commit if any theorem claim remains stronger than its proof, 
any audit file is stale, any Markdown corruption remains, or any required 
verification failed.
