# Prompt 12b — final iterated-WKB figures and a fully explicit manuscript section

Work in the repository root of `Wneka_z_Kerrem`. Read the complete outputs of
Prompts 12a and 12a_1 (scripts, tests, logs, metadata, galleries, and shortlisted
figures) and inspect the current `manuscript/manuscript.tex` before making any
changes. Preserve the WKB/Fedoryuk formula and the numerical regularization
machinery already verified in 12a/12a_1 unless a narrowly necessary bug fix is
found and documented.

This is the final figure-and-manuscript stage. The purpose is primarily
**aesthetic and exploratory**. Strong numerical regularization is allowed. It
is not a reason to reject an attractive portrait. Mathematical honesty here
means complete reproducibility and complete disclosure of what was iterated,
how it was regularized, where the approximation is asymptotically controlled,
and where it is not.

## 1. Fixed cases

Use exactly the following two principal cases:

\[
\eta=\frac{|F|}{V}=4.0,\qquad k=2,
\]

and

\[
\eta=\frac{|F|}{V}=0.25,\qquad k=3.
\]

These are deliberately different iteration depths. Do not present them as a
parameter-controlled like-for-like comparison. They are two distinct
exploratory portraits selected for their visual interest.

Use the established

\[
\Psi_{\mathrm{loc}}^{(n,\sigma)}(z)
=z^{-\delta}e^{\eta/z}
\phi_n\!\left(c_\sigma 3^{1/4}
\left[z+\eta^{1/3}\right]\right)
\]

with the existing definitions of `delta`, `n`, and branches `R`/`I`. Unless
there is a documented reason to do otherwise, retain `delta=0.7` and `n=0` so
that the figures remain continuous with 12a/12a_1.

The `eta=4.0, k=2` case is the strong-drive WKB-motivated portrait. The
`eta=0.25, k=3` case must be labelled everywhere as a **formal extrapolation far
outside the controlled strong-drive asymptotic regime**. Its aesthetic value
does not validate the WKB approximation there.

## 2. What is actually iterated

Do not write simply that the exact physical wavefunction is iterated. State
precisely that the local, sectorial Fedoryuk--Weber approximation is treated
formally as a self-map of the complex plane and combined with the disclosed
numerical regularization.

Introduce concise notation in the manuscript, for example

\[
z_{j+1}=\mathcal M_{\rm reg}(z_j)
=\mathcal R\!\left[\Psi_{\mathrm{loc}}^{(n,\sigma)}(z_j)\right],
\]

while making clear that denominator flooring and exponent clipping occur
inside the numerical evaluation of `Psi_loc`, and radial capping/nonfinite
handling occur after it. Do not use this schematic notation if it would conceal
that distinction; refine it in one sentence instead.

State explicitly that:

- this iteration is not physical time evolution;
- `Psi_loc` is local and sectorial, not a proved global Bargmann eigenfunction;
- NumPy principal branches are used for powers and logarithms;
- branch cuts are neither tracked nor analytically continued;
- the regularized map, rather than the unmodified analytic expression alone,
  generates the pixels;
- no smoothing, interpolation over singularities, denoising, or post-hoc image
  enhancement is applied;
- no claim or test of fractality is made.

Use restrained terminology such as "exploratory complex-plane portraits" or
"iterated-map portraits". Do not call them spectra, physical trajectories,
quantum evolution, Julia sets, or fractals.

## 3. Fully disclosed numerical hammer

Retain and state the exact naive regularization rules from 12a/12a_1:

1. a complex denominator `d` with `|d| < eps_den` is replaced by
   `eps_den exp(i arg d)`, with phase zero at `d=0`;
2. only the real part of every complex exponent is clipped to
   `[-exp_clip,+exp_clip]`, leaving the imaginary part unchanged;
3. nonfinite values after every map application are marked invalid and the
   mask is propagated;
4. every remaining value with modulus above `z_cap` is capped radially at
   `z_cap`, preserving its phase;
5. invalid pixels receive the fixed invalid colour;
6. principal-branch discontinuities remain visible.

Use explicit numerical values of `eps_den`, `exp_clip`, and `z_cap` in the
manuscript and captions/metadata. Strong intervention is acceptable. Report it
rather than minimizing, disguising, or apologizing for it. Do not retune the
thresholds solely to reduce the reported percentages; tune them only if the
chosen aesthetic construction requires it, then disclose both the reason and
the exact values.

For every selected final panel, compute and retain per-application statistics
from application 1 through the displayed depth `k`: denominator flooring,
exponent clipping, radial capping, new nonfinite values, and total invalid
pixels. Put the complete statistics in the 12b JSON sidecar and log. Include a
compact table or an economical textual summary in the manuscript giving at
least the exponent-clipping and radial-capping percentages at each application
(plus any nonzero flooring/nonfinite/invalid percentage). The reader must be
able to see how strongly the numerical hammer acts without consulting the
source code.

## 4. Final aesthetic selection: exactly four PNG files

Produce exactly four final, publication-resolution, lossless PNG source
figures: two for `eta=4.0, k=2` and two for `eta=0.25, k=3`.

For each parameter case, generate a small preview gallery first and select two
final variants primarily for aesthetic quality, while retaining complete
methodological disclosure. Vary only defensible items already exposed by
12a_1, such as:

- `R` versus `I` branch;
- complex-plane window;
- `bright-phase-modulus`, `bright-phase-only`, `bright-banded-modulus`, or
  `bright-equalized` colouring;
- documented colour parameters.

The two selected panels for a given `eta` should add visual information rather
than being nearly identical recolourings. A different branch, window, or a
genuinely informative colour encoding is preferable. The human author's stated
priority is visual attractiveness: vivid colour, balanced composition, and
little unnecessary near-black or near-white area. Pure black remains reserved
for invalid pixels, and valid pixels should not be pure white.

Do not create an uncontrolled mass of candidate binaries. Preview at modest
resolution, select four, then generate only those four as final PNGs at a
resolution adequate for publication (normally at least 1400 pixels on the
shorter side, unless repository/page-layout constraints justify another
choice). Use deterministic filenames containing `eta`, `k`, branch, domain
label, and colour style.

Each final PNG must contain the portrait only, without a large embedded title
or prose block; axes/ticks may be retained if they remain legible in the
manuscript. Put explanatory text in LaTeX captions. Store reproducibility
metadata in PNG text fields and in one JSON sidecar.

Visually inspect the four source PNGs at full size and after they are placed in
the compiled manuscript. Check orientation, labels, colour balance, accidental
black/white domination, raster artefacts, downsampling moire, and consistency
between captions and actual parameters.

## 5. Add a separate manuscript section

Add a concise, self-contained section to `manuscript/manuscript.tex`, placed
where it follows naturally from the Fedoryuk/WKB construction and before the
final conclusions/outlook. Choose a neutral title such as

`Exploratory iteration portraits of the local WKB map`.

The section must:

1. motivate the portraits as an exploratory visualization of a complex
   function treated formally as a map;
2. refer to the existing equation defining `Psi_loc` rather than unnecessarily
   rederive it;
3. define the iteration and the exact regularization transparently;
4. explain the phase/modulus colour encoding used in each panel;
5. distinguish the strong-drive `eta=4, k=2` portraits from the extrapolative
   `eta=0.25, k=3` portraits;
6. report the regularization-intervention percentages compactly;
7. state that the pictures have aesthetic and exploratory value and carry no
   claim of physical evolution, global Bargmann validity, or fractality;
8. discuss visible differences between the selected portraits descriptively,
   without inventing a physical interpretation.

Insert the four PNGs as one compact 2-by-2 multi-panel figure if the existing
LaTeX setup supports it cleanly. Otherwise use two two-panel figures, one for
each value of `eta`. Prefer the layout that remains legible and does not produce
large blank areas. Do not add a fragile package merely for subfigures if
minipages or the manuscript's existing figure conventions suffice.

Captions must identify for every panel:

- `eta`, `k`, `delta`, `n`, and branch;
- plotted complex-plane domain;
- colour style and what hue/brightness encode;
- the fact that principal branches and naive regularization are used;
- for `eta=0.25`, the explicit out-of-regime extrapolation warning.

Avoid repeating the complete threshold definition four times; put the full
definition in the main text and use a concise caption reference.

Keep the section compact. The manuscript was approximately 31 pages before
the iteration section. Prefer a final length of 32 pages and do not exceed 33
pages without a compelling documented reason. Do not shrink unrelated text or
figures merely to satisfy the page count.

## 6. Validation

Extend or add focused tests for:

- exact depths `k=2` and `k=3` in the final-generation path;
- exact metadata values `eta=4.0` and `eta=0.25`;
- deterministic filenames and four-and-only-four final PNG outputs;
- correct per-application statistics through the requested depth;
- colour bounds and invalid-pixel handling;
- JSON sidecar agreement with PNG metadata and manuscript captions where
  mechanically testable;
- a small-resolution end-to-end smoke generation.

Then:

1. run the focused tests;
2. run the full test suite;
3. compile the manuscript through its normal complete LaTeX/Biber workflow;
4. run `git diff --check`;
5. inspect LaTeX warnings for missing references/citations, overfull boxes,
   duplicate labels, and missing figures;
6. report the final page count;
7. render and visually inspect every manuscript page containing the new section
   and figures, plus the neighbouring pages, checking captions, panel labels,
   float placement, readability, and blank space.

Do not modify unrelated mathematical sections. Do not add new claims about the
validity of the Fedoryuk approximation. Do not commit and do not push.

## 7. Independent stage artifacts

Create new, independent artifacts:

- `prompt_12b_final_iterated_wkb_figures_and_manuscript_section.diff`
- `prompt_12b_final_iterated_wkb_figures_and_manuscript_section.log`

Do not overwrite 12a or 12a_1 artifacts. The 12b diff must be based on the
repository state at the start of 12b and contain only 12b changes.

The log must contain:

- the exact four selected PNG filenames and selection rationale;
- exact commands and all numerical parameters;
- domains, branches, colour formulae, and colour bounds;
- complete intervention statistics for every application and panel;
- the exact disclosure text added to the manuscript;
- focused/full test results;
- LaTeX/Biber compilation results and warnings audit;
- `git diff --check` result;
- final page count;
- visual inspection of source PNGs and rendered manuscript pages;
- complete created/modified file list;
- confirmation that no fractality or physical-evolution claim was added;
- one verdict:
  `FOUR ITERATED-WKB PORTRAITS INSERTED WITH FULL DISCLOSURE`,
  `FIGURES INSERTED; MANUSCRIPT DISCLOSURE REQUIRES REVISION`,
  `PARTIAL`, or `BLOCKED`, with a precise explanation.

The numerical hammer is permitted. Concealing it is not.
