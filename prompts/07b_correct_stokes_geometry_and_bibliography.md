# Stage 07b — Correct the Stokes-geometry figure and standardize bibliography given names

## Goal

Correct the mathematical labelling and sheet interpretation in the Stokes/anti-Stokes visualization produced in Stage 07a, update the associated caption and explanatory text where necessary, and standardize all personal-author and personal-editor given names in the rendered bibliography to initials only.

This is a narrowly scoped corrective stage. Preserve all correct work from Stage 07a. Do not extend the analysis to spectral computation, quantization, Stokes multipliers, or the global connection problem.

## Repository safety and scope

Before editing:

1. inspect the repository structure and the current Git status;
2. identify the plotting script, generated figure files, manuscript source, bibliography database(s), and the Stage 07a explanatory note;
3. inspect the actual Stage 07a changes and the current rendered manuscript rather than relying only on filenames or this prompt;
4. preserve all unrelated pre-existing changes and untracked files.

Do not stage, commit, push, reset, restore, clean, rebase, or otherwise alter the Git index or repository history.

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

The leading exponential scales near infinity are

\[
S_\pm(z)=\pm2\sqrt{-qz}.
\]

On the two-sheeted covering

\[
z=t^2,
\qquad s^2=-q,
\]

they become

\[
S_\pm(t)=\pm2st,
\qquad
\Delta S(t)=S_+(t)-S_-(t)=4st.
\]

Use the convention already adopted in Stage 07a:

- equal-modulus curves satisfy
  \[
  \operatorname{Re}\Delta S=0;
  \]
- constant-phase curves satisfy
  \[
  \operatorname{Im}\Delta S=0.
  \]

Because the names “Stokes line” and “anti-Stokes line” are not universal, state this convention explicitly in the figure/caption or accompanying text.

## Required correction 1 — dominance labels in the covering \(t\)-plane

Check the implementation from first principles, not merely by exchanging two hard-coded strings.

For the Stage 07a reference case \(q=1\), take the branch \(s=i\). If

\[
t=x+iy,
\]

then

\[
\operatorname{Re}(st)
=\operatorname{Re}\!\left(i(x+iy)\right)
=-y.
\]

Therefore:

- in the lower half-plane, \(y<0\), one has \(\operatorname{Re}(st)>0\), and \(e^{S_+}=e^{2st}\) is dominant;
- in the upper half-plane, \(y>0\), one has \(\operatorname{Re}(st)<0\), and \(e^{S_-}=e^{-2st}\) is dominant.

In the current Stage 07a figure, the background colours appear to encode this correctly, but the two textual dominance labels are reversed. Correct the labels and verify that labels, signs, colours, legend entries, and the actual formula used for shading all agree.

The code must determine the labels from the sign of \(\operatorname{Re}(st)\); do not preserve a logically inconsistent hard-coded placement.

## Required correction 2 — sheet dependence in the physical \(z\)-plane

The map

\[
z=t^2
\]

identifies \(t\) and \(-t\), while

\[
S_+(-t)=S_-(t),
\qquad
S_-(-t)=S_+(t).
\]

Consequently, above a fixed point of the physical \(z\)-plane, the label “\(e^{S_+}\) dominant” versus “\(e^{S_-}\) dominant” depends on the sheet. A single uncut, one-layer \(z\)-plane must not be divided into sheet-independent dominance regions labelled by \(e^{S_+}\) and \(e^{S_-}\).

Correct panel (a) accordingly:

1. remove the upper/lower-half-plane shading and all labels that assign \(e^{S_+}\) or \(e^{S_-}\) dominance independently of the sheet;
2. retain and clearly distinguish the mapped equal-modulus and constant-phase rays;
3. mark the branch point at \(z=0\);
4. state visually or in a concise annotation that the exchange \(t\mapsto -t\) exchanges \(S_+\leftrightarrow S_-\);
5. make clear that dominance is well defined only after choosing a sheet/branch.

For

\[
q=|q|e^{i\phi},
\]

verify and retain the mapped ray directions

\[
\theta_{\mathrm{eq}}=-\phi
\pmod{2\pi},
\qquad
\theta_{\mathrm{phase}}=\pi-\phi
\pmod{2\pi}.
\]

For \(q>0\), the equal-modulus ray is the positive real ray and the constant-phase ray is the negative real ray. Do not draw either condition as a full line in the \(z\)-plane unless the mathematical mapping explicitly justifies doing so.

A pair of separate sheet-resolved \(z\)-plane mini-panels is permissible only if it materially improves clarity and if a branch cut and sheet convention are stated explicitly. The preferred minimal correction is a single unshaded physical \(z\)-plane panel plus an unambiguous explanation of sheet exchange.

## Required correction 3 — caption, note, and manuscript discussion

Update every affected textual description so that none of the following survives:

- a sheet-independent assignment of \(e^{S_+}\) dominance to one region of the physical \(z\)-plane and \(e^{S_-}\) dominance to another;
- the reversed dominance labels in the \(t\)-plane;
- a suggestion that the positive and negative \(t\)-values above one \(z\) point belong to one single-valued exponential branch;
- a claim that a mapped ray divides the ordinary one-layer \(z\)-plane into globally labelled \(S_+\)- and \(S_-\)-dominance sectors.

The revised caption and explanatory note must state, concisely and accurately, that:

- the exponentials are single-valued on the \(t\)-cover;
- \(t\) and \(-t\) lie above the same \(z\) but exchange \(S_+\) and \(S_-\);
- dominance labels in the physical \(z\)-plane require a sheet/branch choice;
- changing \(\arg F=\arg q\) rotates the ray geometry in fixed Bargmann coordinates;
- all phases of \(F\) remain unitarily equivalent, since
  \[
  U_\chi H(F)U_\chi^\dagger=H(Fe^{i\chi});
  \]
- changing \(|q|\) changes the strength of exponential contrast but not the angular positions of the rays.

Preserve the established terminology and notation of the manuscript. In particular, retain the factor \(V/2\) in the Hamiltonian and do not rename the physical parameters.

## Required correction 4 — bibliography initials

Inspect the bibliography as it is actually rendered in the current manuscript. Some personal authors presently appear with full given names, while others appear only with initials. Make the presentation uniform:

> Every personal author and personal editor in the rendered bibliography must have given names represented by initials only.

Use a consistent form such as

\[
\text{F. W. J. Olver}
\]

rather than mixing that form with fully spelled given names.

Requirements:

1. Determine whether the inconsistency originates in the `.bib` data, the bibliography style/configuration, manually written bibliography entries, or a combination of these.
2. Apply the smallest robust correction that makes the **rendered bibliography** uniform.
3. If the bibliography system supports a global “given names as initials” option, prefer a consistent style-level solution when it does not disrupt the journal style or other required formatting.
4. Otherwise, normalize the relevant personal-name fields in the bibliography source carefully and individually.
5. Preserve family names, name particles (for example `de`, `van`, `von`), suffixes, accents, diacritics, braces protecting capitalization, and the identity and order of authors.
6. Preserve meaningful hyphenation of given names in their initials where bibliographically appropriate.
7. Do not abbreviate corporate or institutional authors as though they were personal names.
8. Do not change citation keys, titles, journal names, volume/issue data, page ranges, DOIs, URLs, years, or citation order merely as part of this normalization.
9. Do not invent missing names or initials. Check authoritative metadata only if a source entry is genuinely ambiguous; record any such lookup and source in the report.
10. Rebuild the bibliography and inspect every rendered entry, not merely the entries that initially looked inconsistent.

The target concerns given names only. Do not introduce a wider bibliography-style redesign.

## Graphical and build requirements

- Modify the existing Stage 07a plotting script rather than creating a competing replacement unless the repository structure clearly requires otherwise.
- Regenerate the publication-quality vector figure and high-resolution PNG preview using deterministic code.
- Preserve equal aspect ratios, line-style distinctions that remain understandable without colour, restrained publication-quality colours, readable labels, and unclipped panel content.
- Rebuild the complete manuscript with the repository's established LaTeX/BibTeX or Biber workflow.
- Treat warnings seriously and distinguish pre-existing warnings from warnings introduced by Stage 07b.
- Do not silence errors or warnings merely to obtain a successful exit code.

## Validation and visual inspection

Before finishing:

1. run the plotting script and regenerate all affected figure outputs;
2. check the plotted geometry numerically for every displayed \(\arg F\), including the reference case \(q=1\), \(s=i\);
3. verify programmatically, where practical, that the label locations agree with the sign of \(\operatorname{Re}(st)\);
4. rebuild the manuscript from a clean-enough build state using only non-destructive build commands; do not clean the Git working tree;
5. render/open the corrected figure and the affected manuscript pages;
6. inspect them visually for mathematical correctness, overlaps, clipping, poor contrast, confusing sheet notation, and consistency between figure and caption;
7. inspect the complete rendered bibliography and confirm that all personal given names appear only as initials;
8. search the manuscript sources and generated review text for stale claims about sheet-independent dominance in the \(z\)-plane;
9. correct every problem found and rerun the relevant checks.

Do not declare success on the basis of source inspection alone. The final PDF must be visually inspected.

## Deliverables

Create or update, following the repository's existing paths and naming conventions:

1. the corrected plotting script;
2. the corrected vector figure, preferably PDF;
3. the corrected high-resolution PNG preview;
4. the revised LaTeX caption and affected manuscript text;
5. the revised Stage 07a/07b explanatory Markdown note, if such a note exists;
6. the bibliography source or style/configuration required to obtain initials-only given names;
7. the rebuilt manuscript PDF;
8. the two review artifacts specified below.

Do not create unnecessary duplicate versions of the figure, bibliography, or manuscript.

## Review artifacts

Create these two files in the repository, following the existing review-artifact directory convention if one exists:

1. `prompt_07b_correct_stokes_geometry_and_bibliography.diff`

   This must be a unified textual diff representing the final Stage 07b changes to all tracked files and the complete contents of every newly created text file.

   Generate it from the actual final working tree. Do not substitute a prose summary for the diff. Because ordinary Git diffs omit untracked files, include each new text file by a non-destructive comparison with `/dev/null` or an equivalent method.

   Do not include raw PDF or PNG bytes in the textual diff. Record binary paths, sizes, hashes if useful, generation commands, and validation results in the `.log` file.

   The `.diff` must isolate and document Stage 07b work as accurately as possible without staging files or overwriting unrelated user changes. If pre-existing changes prevent perfect isolation, explain the limitation precisely in the `.log` rather than manipulating the index.

2. `prompt_07b_correct_stokes_geometry_and_bibliography.log`

   This must contain the complete final report, including:

   - the initial Git status and the final Git status;
   - every file created, modified, or deleted;
   - the purpose of every changed or generated file;
   - the exact mathematical error found in Stage 07a;
   - the exact correction made to the \(t\)-plane dominance labels;
   - the exact correction made to the sheet interpretation in the \(z\)-plane;
   - the formulas used for all displayed rays and dominance regions;
   - the parameter values and branch choice used in every panel;
   - how \(t\mapsto -t\) and \(S_+\leftrightarrow S_-\) are represented;
   - all changes made to the caption and explanatory text;
   - the source of the bibliography inconsistency;
   - the precise bibliography normalization method used;
   - confirmation that all personal-author and personal-editor given names in the rendered bibliography use initials only;
   - confirmation that corporate/institutional authors and all non-name bibliographic metadata were preserved;
   - the commands used to regenerate figures, rebuild the bibliography, and compile the manuscript;
   - the commands and complete results of all validation checks;
   - the method and result of the visual inspection of the figure, affected manuscript pages, and full bibliography;
   - every correction made after visual inspection;
   - all warnings, limitations, ambiguities, and unresolved issues;
   - explicit confirmation that no continued fractions, eigenvalue calculations, spectral determinants, quantization conditions, Stokes multipliers, global connection matrices, eigenvalue asymptotics, or Fedoryuk analysis were introduced;
   - explicit confirmation that no Git staging, committing, pushing, resetting, restoring, cleaning, or history rewriting was performed.

Before finishing, verify that both review artifacts exist, are nonempty, and correspond to the final rather than an intermediate state.

## Strict exclusions

Do not:

- calculate eigenvalues;
- formulate or evaluate a spectral determinant;
- introduce \(D(E)\), \(\mathcal Q(E)\), or any other quantization function;
- use continued fractions in any form, including as a benchmark or numerical check;
- calculate Stokes multipliers;
- construct a global connection matrix;
- claim to solve the connection problem;
- derive eigenvalue asymptotics;
- introduce an artificial large-parameter scaling;
- discuss or apply Fedoryuk's method;
- add iterative maps or dynamical-system plots;
- redesign unrelated figures or rewrite unrelated sections of the manuscript;
- change bibliographic metadata beyond what is required to standardize personal given names to initials;
- stage, commit, push, reset, restore, clean, rebase, or otherwise alter the Git index or history.

The mathematical part of this stage is limited to correcting the visualization and explanation of the geometry implied by

\[
S_\pm(z)=\pm2\sqrt{-qz}
\]

on its natural two-sheeted covering.

## Final interactive response

The final response must reproduce the essential contents of the `.log` report and explicitly provide:

- every file created, modified, or deleted;
- the corrected dominance assignment for the reference \(t\)-plane;
- the final treatment of sheet dependence in the physical \(z\)-plane;
- the bibliography normalization method and the result of inspecting the complete rendered bibliography;
- all generation and build commands;
- all validation results and the outcome of visual inspection;
- every warning, limitation, or unresolved issue;
- the paths of the final `.diff` and `.log` files;
- confirmation that none of the strictly excluded computations or Git operations was performed.
