# Prompt 12a — iterated WKB portraits in the complex plane

Work in the repository root of `Wneka_z_Kerrem`. Read the current manuscript,
the stage-08/09 WKB/Fedoryuk documentation, the stage-11 BB material, and the
relevant tests before editing anything. Also inspect the supplied reference
notebook `Iterations_Binet.ipynb` if it is available in the repository or in the
path given to you when this prompt is run.

The notebook is only a visual and computational prototype. Its essential idea
is: assign every pixel a complex initial value, iterate one complex map a small
number of times, and colour the pixel from the final complex value. Do not copy
its accidental implementation defects (nested Python pixel loops, silent
overflow, invalid casts, or multiplying an already-`uint8` image by 255).

## Goal

Create a standalone Python program, analogous in purpose to the notebook, that
generates complex-plane portraits obtained by iterating the WKB approximation
to our Kerr-cavity Bargmann eigenfunction/map. Generate results for exactly

\[
k=2,3,4
\]

iterations. This is exploratory visualization, not a claim that iteration has
a direct physical time-evolution meaning.

## 1. Identify the WKB map before coding

Do not invent or silently reconstruct a formula. Locate the actual WKB
approximation currently used in this repository and state, in both the script
docstring and the report:

1. the exact formula implemented;
2. whether the iterated object is called `W`, `Psi`, or something else in the
   manuscript;
3. the equation/section or repository source from which it was taken;
4. all parameter conventions, scaling variables, and default numerical values;
5. the chosen sign/sector if the approximation has more than one WKB branch;
6. the limitations of treating this approximation as a self-map of the complex
   plane.

Preserve the manuscript's established convention distinguishing `W` from
`Psi`. If the repository contains several inequivalent WKB approximations, use
the one that is most complete and directly evaluable as a complex function,
but expose the branch/variant as a clearly named command-line option where this
is practical. If no unique choice can be justified from the repository, stop
and report the ambiguity instead of choosing silently.

## 2. Program and outputs

Add a clearly named script under `scripts/`, for example

`scripts/12a_iterated_wkb_portraits.py`.

The script must:

- use a vectorized NumPy mesh, not nested Python loops over pixels;
- accept command-line options for the rectangular complex domain, resolution,
  physical/dimensionless WKB parameters, WKB branch, output directory, and
  iteration counts;
- default to producing separate images for `k=2`, `k=3`, and `k=4` and one
  labelled comparison panel containing all three;
- save lossless PNG files; also save the comparison figure as PDF if the
  existing project convention makes that natural;
- use reproducible filenames containing the iteration count and the principal
  parameter values;
- include titles or captions that distinguish the three iteration depths and
  state that the pictures use naive numerical regularization;
- print a concise run summary including the domain, grid, parameters,
  regularization thresholds, and fractions of regularized/invalid pixels at
  every iteration;
- be usable at a modest preview resolution and at a higher publication-oriented
  resolution without source edits.

Choose conservative defaults that complete on an ordinary laptop. A preview
mode around 600–1000 pixels per side is preferable; do not make the notebook's
2000-by-2000 scalar loop the default.

## 3. Branch cuts: deliberately ignore them

Do **not** construct Riemann sheets, track analytic continuation, mask branch
cuts, or attempt Stokes-aware continuation for this visualization. Use the
standard principal branches supplied by NumPy/SciPy for `sqrt`, fractional
powers, and `log`, and say so explicitly in the source, figure metadata/caption,
and report. Discontinuities caused by principal-branch conventions are allowed
to appear in the plots. They must not be described as physical singularities or
as newly discovered fractal structure.

## 4. Naive but explicit regularization

Other numerical singularities are to be regularized in a deliberately simple,
fully disclosed way. Implement the policy in small testable helper functions,
with command-line thresholds. At minimum:

- for division by a complex denominator `d`, replace values with
  `|d| < eps_den` by `eps_den * exp(1j*arg(d))`; use phase `0` when `d == 0`;
- before complex exponentiation, clip only the real part of the exponent to
  `[-exp_clip, +exp_clip]`, retaining its imaginary part;
- after every application of the WKB map, replace non-finite values with a
  sentinel/mask and cap values with modulus above `z_cap` radially while
  preserving their phase;
- propagate an invalid-pixel mask across later iterates;
- colour invalid pixels with one fixed, conspicuous colour (preferably black)
  and report their fraction;
- keep counts for denominator flooring, exponent clipping, radial capping, and
  non-finite values separately.

Do not hide this policy behind vague words such as "stabilized". Put the exact
rules and default thresholds in the script help, module docstring, report, and
figure caption or sidecar metadata. Make clear that these operations alter the
map locally and that the resulting images are exploratory numerical portraits.

If the actual WKB formula has a different identifiable singular factor, extend
the same modulus-flooring rule explicitly to that factor. Do not add arbitrary
smoothing, interpolation over singular pixels, or post-processing that can
manufacture fine structure.

## 5. Simplified colouring

Use a simple, documented domain-colouring rule. A preferred default is:

- hue from `arg(z_k)` mapped continuously to `[0,1)`;
- fixed moderate-to-high saturation;
- brightness from a robustly normalized `log1p(|z_k|)`, using stated finite
  percentiles (or a fixed CLI range);
- invalid pixels black.

Avoid the opaque nested trigonometric RGB formula from the notebook. Provide an
optional `--phase-only` mode with constant brightness so that one can tell
whether visible structure comes from phase or modulus. Use the same colour
normalization for the `k=2,3,4` comparison unless a clearly documented option
requests per-panel normalization.

## 6. Validation

Add focused automated tests under `tests/` covering at least:

1. equality of vectorized WKB evaluation with scalar evaluation at several
   ordinary complex points;
2. exact iteration counts `2`, `3`, and `4` (guard against an off-by-one error);
3. denominator flooring with phase preservation, including zero;
4. real-part exponent clipping without changing the imaginary part;
5. radial modulus capping with phase preservation;
6. propagation of the invalid mask;
7. deterministic image dimensions and `uint8` RGB/RGBA output;
8. a small smoke run that produces all three individual PNGs and the comparison
   panel.

Run the new tests and the full existing test suite. Run `git diff --check`.
Execute at least one moderate-resolution example with scientifically sensible
parameters and inspect the generated images for blank panels, saturation,
striping caused only by array mistakes, mislabeled axes, and inconsistent colour
normalization. If possible, render/inspect the comparison PDF as well.

Do not claim that visually intricate boundaries are fractal. The report may call
them "quasi-fractal-looking" or "intricate iterated-map structure" unless a
dimension or scaling law has actually been computed (which is outside this
task).

## 7. Repository hygiene and report

Do not edit `manuscript/manuscript.tex` in this task. This stage produces a
reproducible exploratory script, tests, example figures, and documentation only.
Do not refactor unrelated code. Do not commit and do not push.

Create independent stage-12a artifacts, not cumulative copies of earlier logs:

- `prompt_12a_iterated_wkb_portraits.diff`
- `prompt_12a_iterated_wkb_portraits.log`

The log must include:

- the identified WKB formula and its exact repository source;
- the command(s) used to generate the example figures;
- parameter values and regularization thresholds;
- intervention statistics for each of iterations 1–4;
- the colouring rule and normalization range;
- test and full-suite results;
- `git diff --check` result;
- a concise list of created/modified files;
- limitations, especially principal-branch discontinuities and distortion due
  to regularization;
- one of the verdicts
  `ITERATED WKB PORTRAITS GENERATED AND VERIFIED`,
  `PARTIAL`, or `BLOCKED`, with a precise explanation.

Before finishing, ensure the `.diff` contains all and only the intended 12a
repository changes and that the `.log` does not make stronger mathematical or
physical claims than the implementation supports.
