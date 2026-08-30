# Prompt 12a_1 — bright second-iterate WKB gallery and parameter diagnostics

Work in the repository root of `Wneka_z_Kerrem`. This is a narrow follow-up to
Prompt 12a. Read the 12a script, tests, log, metadata, and generated figures
before editing. Preserve the correctly identified iterated map

\[
\Psi_{\mathrm{loc}}^{(n,\sigma)}(z)
=z^{-\delta}e^{\eta/z}
\phi_n\!\left(c_\sigma 3^{1/4}
\bigl[z+\eta^{1/3}\bigr]\right),
\qquad \eta=|F|/V,
\]

with the same `R`/`I` branch conventions and the same explicit principal-branch
and naive-regularization policy as in 12a. Do not change the WKB formula.

## Purpose and strict scope

The 12a gallery established that only the second iterate is visually useful.
The third and fourth iterates are also overwhelmingly dominated by exponent
clipping and radial capping. Therefore this task concerns **only**

\[
k=2.
\]

Do not generate, discuss, or insert final figures for `k=3` or `k=4`. Do not
edit `manuscript/manuscript.tex`. Prompt 12b will later select and insert the
final figures. Prompt 12a_1 is a diagnostic and aesthetic selection stage.

No proof or numerical test of fractality is requested. Do not compute fractal
dimensions, box-counting exponents, Lyapunov exponents, or scaling laws. Call
the output an exploratory iterated-map portrait, not a fractal.

## 1. Parameter cases

Generate diagnostic portraits for both

\[
\eta=|F|/V=5
\qquad\text{and}\qquad
\eta=|F|/V=1/5.
\]

Keep the established default values of the remaining parameters unless the
12a documentation gives a compelling reason to change them. At minimum use
`n=0` and the `I` branch. Also test the `R` branch at preview resolution so that
the report can state whether it supplies visually or numerically better
candidates.

Every filename, title, caption, metadata record, and report table must clearly
identify `eta`, `delta`, `n`, branch, domain, and `k=2`.

The strong-drive Fedoryuk--Weber approximation is asymptotically motivated for
`eta >> 1`. Hence:

- describe `eta=5` as the strong-drive candidate used for possible manuscript
  figures;
- label `eta=1/5` explicitly as a **formal extrapolation outside the controlled
  strong-drive asymptotic regime**;
- do not imply that an attractive `eta=1/5` image validates the approximation
  there;
- keep `eta=1/5` in the diagnostic gallery even if it looks attractive, but do
  not mark it as recommended for the manuscript without a strong, explicit
  caveat.

## 2. Diagnose the excessive black/white appearance

The 12a default used hue from phase, saturation `0.82`, and brightness in
`[0.18,0.95]` from a shared 2nd--98th percentile range of
`log1p(|Psi^{circ k}|)`. This produced too much near-black and pale/near-white
area. Modify the script cleanly rather than applying external image filters.

Retain the original 12a colouring as a named legacy option for reproducibility,
but add several explicit bright styles. At minimum implement and compare:

1. `bright-phase-modulus`: phase controls hue; saturation is at least `0.95`;
   brightness is a nonlinear robust transform of `log1p(|z_2|)` constrained,
   by default, to approximately `[0.50,0.98]`;
2. `bright-phase-only`: phase controls hue, saturation is at least `0.95`, and
   brightness is constant in approximately `[0.88,0.95]`;
3. `bright-banded-modulus`: phase controls hue while a smooth periodic function
   of `log1p(|z_2|)` creates visible modulus bands, but brightness must remain
   within approximately `[0.48,0.98]` and must not introduce discontinuous
   posterization;
4. `bright-equalized`: phase controls hue and brightness uses a deterministic
   empirical-CDF/histogram-equalized transform of finite `log1p(|z_2|)`, again
   with bounded brightness and high saturation.

Expose the colour style, saturation, minimum/maximum brightness, nonlinear
gamma (where applicable), band frequency/contrast (where applicable), and
normalization policy as command-line options. Use perceptually vivid colours,
but do not add sharpening, denoising, interpolation over singularities,
contrast filters after RGB conversion, or any smoothing that could manufacture
fine structure.

Pure black remains reserved for genuinely invalid pixels. Avoid pure white in
valid pixels. Add automated checks for these two rules, allowing ordinary
8-bit rounding tolerance. If invalid pixels are absent, the resulting portrait
should contain no black pixels.

The report must explain which part of the old black/white appearance came from
the brightness interval and which from the modulus distribution. Do not blame
invalid pixels unless their count is nonzero.

## 3. Domain and regularization diagnostics

The 12a example at `eta=8`, domain `[-5.5,2.5] x [-4,4]`, had at application 2
approximately 77.85% exponent clipping and 41.35% radial capping. This makes the
second iterate too dependent on the numerical regularization for immediate use
in the manuscript.

Before producing high-resolution candidates, perform a modest-resolution,
bounded scan of a small, documented set of plausible rectangular windows. Use
the WKB turning-point scale and the visual information from 12a to choose the
candidate windows; do not perform an unbounded optimization. Include the old
window as a control, suitably reconsidered for each value of `eta`.

For every tested `(eta, branch, domain)` record separately at applications 1
and 2:

- denominator flooring fraction;
- exponent-clipping fraction;
- radial-capping fraction;
- new nonfinite fraction;
- total invalid fraction;
- finite fractions lying exactly at the lower or upper brightness bound for
  each relevant colour style.

Rank candidate windows lexicographically by:

1. lower intervention rates at the second application;
2. absence of invalid pixels;
3. non-degenerate phase and modulus variation;
4. visual usefulness.

Do not tune `exp_clip` or `z_cap` merely to make intervention percentages look
smaller. Include a small sensitivity comparison using at least two defensible
threshold pairs and show how much the **portrait itself** changes. Quantify the
change with a simple reproducible RGB or circular-phase discrepancy measure in
addition to visual inspection. Keep the regularization rules from 12a; this
task may expose their thresholds but must not replace them with an undisclosed
method.

If no domain gives acceptably lower intervention at `k=2`, say so explicitly.
An attractive but heavily regularized picture may remain in the diagnostic
gallery, but it must not be recommended as a mathematical illustration without
the warning.

## 4. Gallery outputs

At preview resolution, generate compact labelled contact sheets that allow the
four bright colour styles to be compared on exactly the same complex data for
each selected `(eta, branch, domain)` case. Avoid creating dozens of redundant
full-resolution binary files.

Then choose, on stated numerical and visual criteria, a small shortlist of no
more than eight high-resolution PNG candidates overall. The shortlist should
normally contain:

- several `eta=5`, `k=2` candidates suitable for later consideration in 12b;
- useful comparisons between the best colour styles and/or branches;
- at most a small number of clearly labelled `eta=1/5` extrapolative examples.

Create a final shortlist contact sheet with every panel labelled legibly. Save
it as PNG and PDF. Save the underlying parameter and intervention data in a
machine-readable JSON or CSV sidecar. Do not overwrite the original 12a
figures; write all new outputs under a distinct `figures/12a_1_...` directory.

Visually inspect all contact sheets and shortlisted images. Check especially
for accidental black/white domination, blank panels, clipped labels, wrong
vertical orientation, inconsistent normalization, colour discontinuities not
explained by phase/principal branches, and structures caused only by array or
RGB conversion errors.

## 5. Code quality and tests

Refactor the existing 12a program only as much as needed to support the new
styles, `k=2` gallery workflow, diagnostic window scan, and sidecar data. Keep
the original command-line behaviour reproducible where practical.

Extend the focused tests to cover at least:

- deterministic output for every new colour style;
- high saturation and configured brightness bounds for valid pixels;
- black reserved for invalid pixels and no pure white valid pixels;
- equalization on constant and nonconstant arrays without division by zero;
- smooth bounded modulus bands;
- correct `eta=5` and `eta=0.2` metadata and filenames;
- exact iteration depth `k=2` in the new gallery path;
- intervention table generation at applications 1 and 2;
- a small end-to-end contact-sheet smoke test.

Run the focused tests, the full test suite, and `git diff --check`. Do not alter
the established WKB/Fedoryuk mathematics, manuscript text, or unrelated files.
Do not commit and do not push.

## 6. Independent artifacts and verdict

Create new, independent stage-12a_1 artifacts:

- `prompt_12a_1_bright_k2_wkb_gallery.diff`
- `prompt_12a_1_bright_k2_wkb_gallery.log`

They must not overwrite or cumulatively reproduce the 12a `.diff` and `.log`.
The new diff must be based on the repository state at the start of 12a_1 and
contain only 12a_1 changes.

The log must include:

- exact commands used;
- all tested parameter cases and domains;
- colour formulae and default bounds;
- complete intervention tables for applications 1 and 2;
- brightness-bound occupancy and invalid-pixel statistics;
- threshold-sensitivity comparison;
- shortlist criteria and filenames;
- a clear warning for every `eta=1/5` result;
- visual-inspection findings;
- focused and full-suite test results;
- `git diff --check` result;
- created/modified file list;
- a recommendation of which candidates, if any, should be considered by Prompt
  12b;
- one verdict:
  `BRIGHT K2 WKB GALLERY GENERATED; CANDIDATES READY FOR SELECTION`,
  `GALLERY GENERATED BUT REGULARIZATION REMAINS DOMINANT`,
  `PARTIAL`, or `BLOCKED`, with a precise explanation.

Do not edit the manuscript and do not preselect four publication figures as a
fait accompli. The human author will inspect the shortlist before Prompt 12b.
