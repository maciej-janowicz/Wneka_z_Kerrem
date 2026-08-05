# Stage 07.3 — Final Markdown and audit cleanup

Work in the authoritative `Wneka_z_Kerrem` repository containing the completed but still uncommitted Stage 07, Stage 07.1, and Stage 07.2 changes.

This is a strictly editorial and technical cleanup. The mathematics of the sectorial theorem and its proof has already been accepted. Do not redesign, weaken, or extend it. Do not modify mathematical code or tests. Do not begin Stage 07a. Do not commit or push.

## 1. Preflight inspection

Before editing, run:

```bash
git status --short
git diff --check
git diff --stat
```

Read in full:

- `docs/stage07_olver_uniform_asymptotics.md`;
- `prompts/07_olver_uniform_asymptotics.md`;
- `prompts/07_1_stage07_theorem_and_technical_corrections.md`;
- `prompts/07_2_stage07_final_theorem_corrections.md`;
- the current Stage 07.2 report or log;
- the Stage 07 manuscript additions, only to confirm that no corresponding textual defect remains there.

Preserve every accepted Stage 07.2 mathematical statement and proof.

## 2. Correct the remaining documentation formula

In `docs/stage07_olver_uniform_asymptotics.md`, remove the erroneous additive sign in the asymptotic formula. The expression must be multiplicative:

```latex
\[
\Psi_\sigma(z)
=
e^{2\sigma\sqrt{-qz}}z^{1/4-B_2/2}
\left[
1+u_1^{(\sigma)}z^{-1/2}+O(z^{-1})
\right].
\]
```

It must not contain a `+` between the prefactor and the bracket. Search all Stage 07 documentation and prompts for copies of the same defective additive form and correct them where present. Do not change any accepted coefficient, exponent, branch convention, or remainder order.

## 3. Restore the archived Stage 07.2 prompt

Repair `prompts/07_2_stage07_final_theorem_corrections.md` as readable, ordinary Markdown faithful to the prompt that was executed.

Correct all damage caused by copying or rendering, including:

- mathematics lacking `\(...\)` or `\[...\]` delimiters;
- malformed sets, braces, brackets, backslashes, subscripts, and inequalities;
- isolated `+` signs or other fragments separated from their equations;
- accidental Setext headings produced by lines of `===` or `---` that belonged to mathematical content;
- accidental block quotes produced by `>` inside formulas;
- equations broken into headings or prose;
- missing spaces, punctuation, or Markdown structure.

In particular, repair malformed text such as

```text
fix (\sigma\in{+1,-1});
```

to a properly delimited form such as

```markdown
fix \(\sigma\in\{+1,-1\}\);
```

and ensure that definitions such as

```latex
\[
\Omega_{d,R}
=
\left\{t:\Re(\overline d\,t)>R\right\}
\]
```

remain inside display-math delimiters and are not interpreted as Markdown headings.

Do not paraphrase the prompt or change its instructions. Restore its formatting and legibility only.

## 4. Remove residual corruption from the Stage 07 and 07.1 prompts

Inspect and repair:

- `prompts/07_olver_uniform_asymptotics.md`;
- `prompts/07_1_stage07_theorem_and_technical_corrections.md`.

At minimum, correct the known residual defects:

```text
Prove abound of the form
```

must become

```text
Prove a bound of the form
```

and

```text
and“anti-Stokes line”
```

must have proper spacing and punctuation, for example:

```text
and “anti-Stokes line”
```

Also search visually for:

- concatenated English words;
- missing spaces adjacent to opening quotation marks;
- malformed inline and display mathematics;
- damaged occurrences of `Gamma`, `rho`, `theta`, and `quad`;
- malformed absolute-value notation;
- damaged asymptotic ansatzes;
- raw tabs, carriage returns, or other control characters within prose or LaTeX commands.

Do not rely only on a control-character scan. Read all three archived prompts from beginning to end after editing.

## 5. Correct the Stage 07.2 report

Update the Stage 07.2 report or log so that it accurately records what Stage 07.2 accomplished and what Stage 07.3 subsequently had to repair.

In particular:

- do not retain an unqualified claim that all archived prompts were already restored as readable Markdown;
- do not state `Unresolved issues — None` for the pre-07.3 state;
- record that the sectorial theorem, quantifiers, overlap argument, gluing argument, and manuscript asymptotic formula were accepted after Stage 07.2;
- record that one additive sign remained in the documentation and that the archived prompts still contained copy/rendering corruption;
- distinguish mathematical acceptance from editorial readiness for commit.

Keep the report factual. Do not rewrite history as though Stage 07.2 had already made the Stage 07.3 corrections.

## 6. Scope restrictions

Do not:

- change the accepted sectorial theorem, its quantifiers, or its gluing proof;
- change the manuscript mathematics, except for a directly corresponding typographical defect discovered during the required cross-check;
- modify implementation code or tests;
- begin Stage 07a or generate figures;
- introduce connection coefficients, Stokes multipliers, continued fractions, a spectral determinant, a quantization condition, a large parameter, or Fedoryuk-type analysis;
- perform broad stylistic rewriting;
- commit or push.

If inspection appears to require a mathematical, code, or test change, stop and report the issue instead of making that change.

## 7. Verification

After editing:

1. Read each edited Markdown file in full.
2. Run:

   ```bash
   git diff --check
   ```

3. Search for all known defects and suspicious remnants, including:

   ```text
   +[1+u_1
   Prove abound
   and“anti-Stokes
   resultof
   sectorialsolutions
   cannotbe
   ready forcommit
   Unresolved issues — None
   ```

   Adapt the search syntax safely as needed; absence of one literal string is not a substitute for reading the files.

4. Check for carriage returns and disallowed control characters.
5. Confirm that no source-code or test file changed during Stage 07.3.
6. Compile the manuscript using the established project command, solely to confirm that the editorial cleanup did not damage the build.

Do not claim that any check passed unless it was actually executed successfully.

## 8. Deliverables

Create the usual Stage 07.3 audit artifacts, following the repository's established naming convention:

1. a unified diff containing the Stage 07.3 corrections;
2. a concise report or log stating:
   - every file changed;
   - the documentation formula corrected;
   - the prompt-formatting defects repaired;
   - the Stage 07.2 report corrections;
   - the result of the full-file visual inspection;
   - the control-character check result;
   - the `git diff --check` result;
   - the manuscript compilation result;
   - confirmation that no code or tests changed;
   - confirmation that Stage 07a was not begun;
   - confirmation that no commit or push was performed.

End by printing:

```bash
git status --short
git diff --stat
```

Leave all Stage 07, 07.1, 07.2, and 07.3 changes uncommitted for human review.
