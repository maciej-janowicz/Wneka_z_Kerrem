# Stage 07a — Visualization of the Stokes and anti-Stokes geometry

## Goal

Create a publication-quality visualization of the Stokes and anti-Stokes geometry associated with the leading exponential factors obtained in Section 7 by Olver's asymptotic procedure.

This stage is deliberately limited to the geometry of the asymptotic exponentials. Do not attempt any spectral computation, quantization condition, connection problem, or evaluation of Stokes multipliers.

## Mathematical setting

The Bargmann eigenvalue equation is

\[
z^2\Psi''(z)+(B_1+B_2z)\Psi'(z)+(B_3+qz)\Psi(z)=0,
\qquad q\neq0,
\]

with

\[
B_1=\frac{2\overline F}{V},
\qquad
B_2=\frac{2\hbar\omega_0}{V},
\qquad
B_3=-\frac{2E}{V},
\qquad
q=\frac{2F}{V}.
\]

At leading order near infinity, the two exponential scales are

\[
S_\pm(z)=\pm 2\sqrt{-qz}.
\]

Introduce the two-sheeted covering

\[
z=t^2
\]

and choose \(s\) such that

\[
s^2=-q.
\]

On the \(t\)-plane the exponentials become single-valued:

\[
S_\pm(t)=\pm 2st.
\]

The relevant exponential difference is

\[
\Delta S(t)=S_+(t)-S_-(t)=4st.
\]

Use the following explicit convention throughout the code, figure labels, and caption:

- equal-modulus curves satisfy
  \[
  \operatorname{Re}\Delta S=0;
  \]
- constant-phase curves satisfy
  \[
  \operatorname{Im}\Delta S=0.
  \]

Because the terminology “Stokes line” versus “anti-Stokes line” is not universal, state this convention explicitly rather than relying only on the names.

## Required figure

Produce one coherent multi-panel figure showing:

1. **The physical Bargmann \(z\)-plane**

   Show the rays obtained by mapping the corresponding straight lines from the \(t\)-plane through \(z=t^2\).

   Indicate:

   - equal-modulus rays;
   - constant-phase rays;
   - representative sectors of dominance of \(e^{S_+}\) and \(e^{S_-}\);
   - the branch point at \(z=0\);
   - the fact that the square-root exponentials live naturally on a two-sheeted covering.

2. **The covering \(t\)-plane**

   Show the straight-line geometry determined by

   \[
   \operatorname{Re}(st)=0,
   \qquad
   \operatorname{Im}(st)=0.
   \]

   Label the sectors in which

   \[
   \operatorname{Re}(st)>0
   \quad\text{or}\quad
   \operatorname{Re}(st)<0,
   \]

   and hence identify which of \(e^{S_+}\) and \(e^{S_-}\) is dominant.

   Make the relation between \(t\) and \(-t\), which represent the two sheets above the same point \(z=t^2\), visually clear.

3. **Rotation with \(\arg F\)**

   Include a compact comparison for several representative phases, for example

   \[
   \arg F=0,\quad \frac{\pi}{4},\quad \frac{\pi}{2}.
   \]

   The figure must demonstrate that changing \(\arg F\) rotates the Stokes geometry in fixed Bargmann coordinates.

   Do not suggest that this rotation changes the spectrum.

## Physical equivalence of the phase of \(F\)

The text accompanying the figure must state that all values of \(\arg F\) are physically unitarily equivalent.

With

\[
U_\chi=e^{i\chi N},
\qquad N=a^\dagger a,
\]

one has

\[
U_\chi H(F)U_\chi^\dagger
   =H\!\left(Fe^{i\chi}\right).
\]

Consequently, the spectrum depends on \(|F|\), not on \(\arg F\). The plotted sector geometry nevertheless rotates when \(\arg F\) is changed while the Bargmann coordinate system is kept fixed.

This distinction must be explicit in the caption or the accompanying explanatory paragraph.

## Role of \(|q|\)

The angular positions of the rays depend only on \(\arg q=\arg F\).

Changing \(|q|\) must not rotate the rays. It changes only the magnitude of

\[
\operatorname{Re}\Delta S
   =4\operatorname{Re}(st),
\]

and therefore the strength of the dominance contrast between the two exponentials.

If different values of \(|q|\) are illustrated, represent their effect through shading, opacity, or dominance intensity—not through a change in ray positions.

## Numerical and graphical requirements

- Implement the figure in a reproducible Python script using NumPy and Matplotlib.
- Inspect the repository structure before choosing final paths and follow the existing project conventions.
- Use mathematical labels rendered consistently with the manuscript.
- Use a restrained, publication-appropriate colour palette.
- The figure must remain legible in print and after reduction to journal column width.
- Do not encode the distinction between the two kinds of rays by colour alone; also use different line styles.
- Use equal aspect ratios for all complex-plane panels.
- Avoid decorative three-dimensional effects.
- Avoid unnecessary legends inside crowded panels.
- Add clear panel labels `(a)`, `(b)`, etc.
- Ensure that no label is clipped.
- Use deterministic output with no random elements.

## Deliverables

Create:

1. the complete plotting script;
2. a publication-quality vector version of the figure, preferably PDF;
3. a high-resolution PNG preview;
4. a concise proposed LaTeX caption;
5. a short Markdown note explaining:
   - the equations used to determine the plotted lines;
   - the line-naming convention;
   - how the \(t\)-plane geometry maps to the \(z\)-plane;
   - why changing \(\arg F\) rotates the plotted geometry but does not change the spectrum;
   - why changing \(|q|\) affects only the dominance contrast;
6. a unified `.diff` file containing all changes made to tracked repository files and the full contents of every newly created text file;
7. a complete `.log` file containing the full final report specified below.

Before finishing, open or render the resulting figure and inspect it visually. Correct overlaps, clipped labels, confusing sector shading, or misleading branch information.

## Review artifacts and final report

Create two additional review artifacts in the repository, following the existing naming and directory conventions:

1. `prompt_07a_stokes_geometry_visualization.diff`

   This file must be a unified diff containing all changes made to tracked repository files during this stage.

   Generate it from the actual final working tree. Do not write a prose summary in place of the diff. Include additions, modifications, and deletions of tracked files. Since ordinary Git diffs do not contain untracked files, ensure that the full contents of every newly created text file are also represented for review—for example by generating the diff against `/dev/null` or by using an equivalent non-destructive method.

   Binary outputs such as PDF and PNG need not have their bytes embedded in the textual diff, but their creation, paths, sizes, and validation results must be recorded in the `.log` file.

   Do not stage, commit, push, reset, restore, clean, or otherwise alter the repository state merely to produce this file.

2. `prompt_07a_stokes_geometry_visualization.log`

   This file must contain the complete final report, not merely a short summary. Record:

   - every file created, modified, or deleted;
   - the purpose of every output file;
   - the parameter values used in every panel;
   - the exact formulas implemented;
   - the precise convention used for equal-modulus and constant-phase curves;
   - how the \(t\)-plane lines were mapped to the \(z\)-plane;
   - the commands used to generate the PDF and PNG outputs;
   - the commands and results of all validation checks;
   - the method and result of the visual inspection;
   - all corrections made after visual inspection;
   - any warnings, approximations, limitations, or unresolved issues;
   - confirmation that the phase of \(F\) was treated as spectrally irrelevant but geometrically rotational in fixed Bargmann coordinates;
   - confirmation that \(|q|\) was not allowed to change ray positions;
   - explicit confirmation that no continued fractions, eigenvalue calculations, spectral determinants, quantization conditions, Stokes multipliers, or global connection matrices were introduced.

The final interactive response must reproduce the essential contents of the `.log` report and explicitly give the paths of the `.diff` and `.log` files.

Before finishing, verify that both review artifacts exist, are nonempty, and correspond to the final—not an intermediate—state of the work.

## Strict exclusions

Do not:

- calculate eigenvalues;
- formulate or evaluate a spectral determinant;
- introduce \(D(E)\) or any other quantization function;
- use continued fractions in any form;
- use continued fractions even as a benchmark or numerical check;
- calculate Stokes multipliers;
- construct a global connection matrix;
- claim to solve the connection problem;
- derive eigenvalue asymptotics;
- introduce artificial large-parameter scaling;
- discuss Fedoryuk's method;
- add iterative maps or dynamical-system plots;
- modify the mathematical content of Section 7 beyond adding the figure reference, caption, or the short phase-equivalence explanation if explicitly requested;
- stage, commit, push, reset, restore, clean, or otherwise alter the Git working tree or index.

This stage concerns only the geometry implied by

\[
S_\pm(z)=\pm2\sqrt{-qz}
\]

and its transparent visualization in the \(z\)- and \(t\)-planes.

## Final response checklist

At the end, report:

- every file created, modified, or deleted;
- the parameter values used in the figure;
- the precise convention used for Stokes and anti-Stokes lines;
- the commands used to generate the outputs;
- the commands and results of all validation checks;
- the method and result of the visual inspection;
- any warnings, limitations, or unresolved issues;
- the paths of the final `.diff` and `.log` review artifacts;
- confirmation that no continued-fraction, spectral, connection, or quantization computation was introduced;
- confirmation that the Git working tree and index were not staged, committed, pushed, reset, restored, or cleaned.
