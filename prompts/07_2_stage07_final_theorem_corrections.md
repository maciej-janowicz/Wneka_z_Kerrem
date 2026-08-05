# Stage 07.2 — Final correction of the sectorial theorem and Markdown sources

Work in the authoritative `Wneka_z_Kerrem` repository containing the completed but not yet committed Stage 07 and Stage 07.1 changes.

This is a narrow corrective stage. Do not redesign Stage 07, do not begin Stage 07a, and do not commit or push anything.

## 1. Preflight inspection

Before editing:

1. Run:

   ```bash
   git status --short
   git diff --check
   git diff --stat
   ```
2. Locate and read in full:

   * the current Stage 07 manuscript changes;
   * `docs/stage07_olver_uniform_asymptotics.md`;
   * `prompts/07_olver_uniform_asymptotics.md`;
   * `prompts/07_1_stage07_theorem_and_technical_corrections.md`;
   * the Stage 07 and Stage 07.1 logs and diffs, if present;
   * the relevant implementation and tests.

Preserve all correct Stage 07.1 mathematics, code, and tests. Make only the corrections required below unless inspection reveals a directly related error.

## 2. Correct the quantifiers in the sectorial existence theorem

The current theorem must not choose one direction \(d\) and then claim the construction simultaneously for both \(\sigma=\pm1\).

Since

\[
a_{-\sigma}=-a_\sigma,
\]

a direction satisfying

\[
\Re(a_\sigma d)\le 0
\]

for one sign need not satisfy it for the other sign.

Rewrite the statement so that the order of choices is explicit:

1. fix \(\sigma\in\{+1,-1\}\);
2. choose a unit direction \(d\) satisfying

   \[
   \Re(a_\sigma d)\le 0;
   \]

3. choose a sufficiently large \(R\);
4. construct the corresponding solution \(w_{\sigma,d}\) on

   \[
   \Omega_{d,R}
   =
   \left\{
   t:\Re(\overline d\,t)>R
   \right\}.
   \]

Make clear that the construction for the other sign generally uses another admissible direction or sector.

Check every theorem, proposition, proof, summary, and notation table affected by this quantifier order. Do not fix only the headline statement while leaving contradictory wording elsewhere.

## 3. Complete the overlap and gluing argument

The current phrase “uniqueness identifies the two solutions” is too compressed. Supply the missing argument.

For two admissible directions \(d_1,d_2\), assume the directions are sufficiently close that

\[
\Re(\overline{d_1}d_2)>0.
\]

For a point

\[
t\in\Omega_{d_1,R}\cap\Omega_{d_2,R},
\]

show explicitly that the complete translated ray

\[
t+s d_2,\qquad s\ge 0,
\]

remains in the overlap. Indeed,

\[
\Re\!\left(\overline{d_1}(t+s d_2)\right)
=
\Re(\overline{d_1}t)
+
s\,\Re(\overline{d_1}d_2)
>R,
\]

and

\[
\Re\!\left(\overline{d_2}(t+s d_2)\right)
=
\Re(\overline{d_2}t)+s
>R.
\]

Then explain why the solution constructed in direction \(d_1\):

- is defined and holomorphic along the entire \(d_2\)-ray inside the overlap;
- has the required normalization at infinity along that ray;
- satisfies, by variation of constants, the same Volterra equation associated with direction \(d_2\).

Only after these facts have been established may uniqueness of that Volterra equation be invoked to conclude

\[
w_{\sigma,d_1}=w_{\sigma,d_2}
\]

on the overlap.

Use this pairwise identification to justify the gluing of the half-plane solutions into a holomorphic canonical solution on the claimed sectorial domain. State precisely the domain on which the gluing is proved. Do not claim a larger sector than the overlap geometry and admissibility conditions actually support.

If the proof requires a chain of sufficiently close admissible directions, state this explicitly and explain how consecutive overlap identities produce the sectorial solution.

Retain the borderline case

\[
\Re(a_\sigma d)=0
\]

only if the existing estimates genuinely cover it.

## 4. Repair the asymptotic formula

In `docs/stage07_olver_uniform_asymptotics.md`, and wherever else the same error occurs, replace the erroneous additive expression

\[
\Psi_\sigma(z)
=
e^{2\sigma\sqrt{-qz}}z^{1/4-B_2/2}
+
\left[\cdots\right]
\]

by the multiplicative asymptotic form

\[
\Psi_\sigma(z)
=
e^{2\sigma\sqrt{-qz}}z^{1/4-B_2/2}
\left[\cdots\right].
\]

Check the complete bracketed expansion, its powers, coefficients, remainder term, branch conventions, and domain of validity against the derivation. Do not alter a correct coefficient merely for stylistic uniformity.

## 5. Fully restore the Markdown and LaTeX sources

Carefully repair both archived prompts:

- `prompts/07_olver_uniform_asymptotics.md`;
- `prompts/07_1_stage07_theorem_and_technical_corrections.md`.

They must remain faithful archival copies of the prompts, but they must also be readable and syntactically well formed.

Repair, in particular:

- concatenated words such as `resultof`, `sectorialsolutions`, `cannotbe`, and `ready forcommit`;
- missing spaces and punctuation;
- missing or malformed Markdown mathematics delimiters;
- damaged braces, brackets, backslashes, set-builder notation, and absolute-value notation;
- malformed expressions such as

  ```text
  [\Gamma_{\sigma,d}(t)={t+sd\ge0}]
  ```

  which should be rendered as

  \[
  \Gamma_{\sigma,d}(t)=\{t+sd:s\ge0\};
  \]

- remnants such as malformed `\(|g(u)|,|du|\)` notation;
- damaged versions of the asymptotic ansatz;
- any raw control characters, tabs inside mathematical commands, carriage returns inside lines, or other encoding damage.

Also inspect `docs/stage07_olver_uniform_asymptotics.md` and the manuscript additions for the same classes of corruption.

Do not rely only on a byte-level control-character scan: visually inspect the rendered logical structure and search for accidentally concatenated English words.

## 6. Scope restrictions

Do not:

* begin Stage 07a or generate Stokes-geometry figures;
* introduce continued fractions, a spectral determinant, connection coefficients, Stokes multipliers, or a quantization condition;
* introduce a large-parameter limit;
* start a Fedoryuk-type analysis;
* alter the physical model;
* weaken the repaired sectorial theorem back to a merely raywise theorem unless a new, explicit contradiction is discovered;
* perform broad stylistic rewriting of the manuscript;
* modify working mathematical code or tests merely to create activity;
* commit or push.

The only expected code changes are none. If a code change becomes unavoidable because a directly related mathematical defect is discovered, stop and document the defect before editing it.

## 7. Verification

After editing, run:

```bash
git diff --check
```

Run the complete project test suite using the repository’s established command.

Also perform targeted textual checks for:

* raw carriage returns and disallowed control characters;
* tabs occurring inside mathematical commands;
* the known concatenated strings listed above;
* malformed occurrences of `Gamma`, `rho`, `theta`, `quad`, and the asymptotic ansatz;
* every occurrence of the sectorial theorem’s quantifiers;
* every occurrence of the gluing or uniqueness claim;
* every occurrence of the incorrect additive asymptotic form.

Compile the manuscript using the project’s established build command. If the project has a documentation-rendering or Markdown-linting command, run it as well.

Do not claim that a check passed unless it was actually executed successfully.

## 8. Deliverables

Create or update the usual Stage 07.2 audit artifacts, following the repository’s existing naming convention. They must include at least:

1. a unified diff containing the Stage 07.2 corrections;
2. a log or report stating:

   * which files changed;
   * the exact theorem and proof corrections;
   * how the overlap/gluing argument was completed;
   * which Markdown corruptions were repaired;
   * test results;
   * manuscript compilation result;
   * `git diff --check` result;
   * confirmation that no Stage 07a work was begun;
   * confirmation that no commit or push was performed.

End by printing:

```bash
git status --short
git diff --stat
```

Leave all accepted Stage 07, Stage 07.1, and Stage 07.2 changes uncommitted for human review.
