#!/usr/bin/env python3
"""Iterated portraits of the local Kerr-cavity Fedoryuk--Weber map.

The iterated function is the manuscript's local Bargmann approximation

    Psi_loc[n,sigma](z) = z**(-delta) exp(eta/z)
        phi_n(c_sigma * 3**(1/4) * (z + eta**(1/3))),

where c_R=1, c_I=-1j and
phi_n(w)=pi**(-1/4)/(sqrt(2**n*n!))*exp(-w**2/2)*H_n(w).
It is called Psi (not W) in manuscript/manuscript.tex, equation
``fedoryuk-local-pullback`` in the subsection "Independent sectorial
complex-WKB formulation"; see also
docs/fedoryuk_weber_wavefunction_and_energy.md.  Here eta=|F|/V>0,
delta=hbar*omega_0/V, n is a nonnegative integer, z=eta**(1/3)y,
epsilon=eta**(-2/3), and X=z+eta**(1/3).  Branch I (default) is the
imaginary-axis sector candidate; branch R is the real-axis local problem.

This local, sectorial asymptotic expression excludes z=0 and is not proved
to be a global Bargmann eigenfunction.  Treating it as C -> C and iterating
it has no asserted physical time-evolution meaning and repeatedly evaluates
it outside its controlled close-turning-point neighbourhood.

All sqrt, powers, and logarithms use NumPy principal branches; branch cuts
are deliberately neither masked nor continued.  Numerical regularization is
naive and alters the map locally: denominators with |d|<eps_den become
eps_den*exp(i arg d) (phase zero at d=0); only Re(exponent) is clipped to
+/-exp_clip; after every map application non-finite values are marked invalid
and finite values with |z|>z_cap are capped radially with phase preserved.
Invalidity propagates and invalid pixels are black.  No smoothing is used.
"""

import argparse
import json
import math
from dataclasses import dataclass, asdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import hsv_to_rgb
import numpy as np
from PIL import Image, PngImagePlugin


@dataclass
class InterventionStats:
    denominator_floored: int = 0
    exponent_clipped: int = 0
    radial_capped: int = 0
    nonfinite: int = 0
    invalid_total: int = 0


def floor_complex_denominator(d, eps_den):
    """Floor small complex moduli, preserving phase (zero gets phase zero)."""
    values = np.asarray(d, dtype=np.complex128)
    small = np.abs(values) < eps_den
    phase = np.angle(values)
    replacement = eps_den * np.exp(1j * phase)
    replacement = np.where(values == 0, complex(eps_den, 0.0), replacement)
    return np.where(small, replacement, values), small


def clip_complex_exponent(exponent, exp_clip):
    """Clip only the real part, retaining the imaginary part exactly."""
    values = np.asarray(exponent, dtype=np.complex128)
    clipped_real = np.clip(values.real, -exp_clip, exp_clip)
    mask = clipped_real != values.real
    return clipped_real + 1j * values.imag, mask


def cap_complex_modulus(values, z_cap):
    """Cap finite complex values radially, preserving their phase."""
    z = np.asarray(values, dtype=np.complex128)
    modulus = np.abs(z)
    mask = np.isfinite(modulus) & (modulus > z_cap)
    safe_modulus = np.where(mask, modulus, 1.0)
    return np.where(mask, z * (z_cap / safe_modulus), z), mask


def hermite_function(n, w, exp_clip):
    """Vectorized normalized physicists' Hermite function and clip mask."""
    w = np.asarray(w, dtype=np.complex128)
    h0 = np.ones_like(w)
    if n == 0:
        hn = h0
    else:
        h1 = 2.0 * w
        if n == 1:
            hn = h1
        else:
            for level in range(1, n):
                h0, h1 = h1, 2.0 * w * h1 - 2.0 * level * h0
            hn = h1
    exponent, clipped = clip_complex_exponent(-0.5 * w * w, exp_clip)
    normalization = math.pi ** (-0.25) / math.sqrt(2.0**n * math.factorial(n))
    return normalization * np.exp(exponent) * hn, clipped


def wkb_map(z, *, eta=8.0, delta=0.7, n=0, branch="I",
            eps_den=1e-8, exp_clip=80.0):
    """Evaluate Psi_loc with principal branches and return intervention masks."""
    z = np.asarray(z, dtype=np.complex128)
    denominator, floored = floor_complex_denominator(z, eps_den)
    log_z = np.log(denominator)  # principal branch, intentionally discontinuous
    gauge_exponent, gauge_clipped = clip_complex_exponent(
        -delta * log_z + eta / denominator, exp_clip)
    c_sigma = 1.0 if branch == "R" else -1j
    w = c_sigma * 3.0**0.25 * (z + eta**(1.0 / 3.0))
    phi, hermite_clipped = hermite_function(n, w, exp_clip)
    with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
        result = np.exp(gauge_exponent) * phi
    return result, {
        "denominator_floored": floored,
        "exponent_clipped": gauge_clipped | hermite_clipped,
    }


def regularize_after_map(values, previous_invalid, z_cap):
    """Propagate invalidity, mark new non-finites, and radially cap finite values."""
    z = np.asarray(values, dtype=np.complex128)
    previous_invalid = np.asarray(previous_invalid, dtype=bool)
    nonfinite = ~np.isfinite(z.real) | ~np.isfinite(z.imag)
    invalid = previous_invalid | nonfinite
    working = np.where(invalid, 0.0 + 0.0j, z)
    capped, cap_mask = cap_complex_modulus(working, z_cap)
    return capped, invalid, nonfinite & ~previous_invalid, cap_mask & ~invalid


def iterate_map(initial, iteration_counts=(2, 3, 4), **parameters):
    """Return exactly requested iterates, invalid masks, and per-step statistics."""
    counts = tuple(sorted(set(iteration_counts)))
    if not counts or counts[0] < 1:
        raise ValueError("iteration counts must be positive")
    current = np.asarray(initial, dtype=np.complex128).copy()
    invalid = np.zeros(current.shape, dtype=bool)
    outputs, masks, statistics = {}, {}, []
    z_cap = parameters.pop("z_cap")
    for step in range(1, counts[-1] + 1):
        mapped, interventions = wkb_map(current, **parameters)
        current, invalid, new_nonfinite, capped = regularize_after_map(
            mapped, invalid, z_cap)
        stats = InterventionStats(
            denominator_floored=int(np.count_nonzero(interventions["denominator_floored"] & ~invalid)),
            exponent_clipped=int(np.count_nonzero(interventions["exponent_clipped"] & ~invalid)),
            radial_capped=int(np.count_nonzero(capped)),
            nonfinite=int(np.count_nonzero(new_nonfinite)),
            invalid_total=int(np.count_nonzero(invalid)),
        )
        statistics.append(stats)
        if step in counts:
            outputs[step] = current.copy()
            masks[step] = invalid.copy()
    return outputs, masks, statistics


def normalization_range(outputs, masks, percentiles=(2.0, 98.0)):
    samples = [np.log1p(np.abs(outputs[k][~masks[k]])) for k in outputs
               if np.any(~masks[k])]
    if not samples:
        return 0.0, 1.0
    low, high = np.percentile(np.concatenate(samples), percentiles)
    if not np.isfinite(low) or not np.isfinite(high) or high <= low:
        high = low + 1.0
    return float(low), float(high)


COLOUR_STYLES = ("legacy", "bright-phase-modulus", "bright-phase-only",
                 "bright-banded-modulus", "bright-equalized")


def empirical_cdf(values, valid):
    """Deterministic mid-rank empirical CDF; constants map to one half."""
    data = np.asarray(values, dtype=float)
    valid = np.asarray(valid, dtype=bool) & np.isfinite(data)
    result = np.full(data.shape, 0.5, dtype=float)
    sample = data[valid]
    if sample.size < 2 or np.all(sample == sample[0]):
        return result
    unique, inverse, counts = np.unique(sample, return_inverse=True,
                                        return_counts=True)
    cumulative = np.cumsum(counts)
    midranks = (cumulative - 0.5 * counts) / sample.size
    result[valid] = midranks[inverse]
    return result


def brightness_field(values, invalid, value_range, *, style="legacy",
                     brightness_min=0.50, brightness_max=0.98, gamma=0.65,
                     band_frequency=2.4, band_contrast=0.85):
    """Return bounded pre-RGB brightness without image-space filtering."""
    z = np.asarray(values)
    invalid = np.asarray(invalid, dtype=bool)
    log_modulus = np.log1p(np.abs(z))
    low, high = value_range
    normalized = np.clip((log_modulus - low) / (high - low), 0.0, 1.0)
    if style == "legacy":
        return 0.18 + 0.77 * normalized
    if style == "legacy-phase-only":
        return np.full(z.shape, 0.9)
    if style == "bright-phase-only":
        return np.full(z.shape, 0.92)
    if style == "bright-phase-modulus":
        transformed = normalized**gamma
    elif style == "bright-banded-modulus":
        # A continuous sinusoid: no posterization or discontinuous binning.
        wave = 0.5 + 0.5 * np.sin(2.0 * np.pi * band_frequency * normalized)
        transformed = (1.0 - band_contrast) * normalized + band_contrast * wave
    elif style == "bright-equalized":
        transformed = empirical_cdf(log_modulus, ~invalid)
    else:
        raise ValueError(f"unknown colour style: {style}")
    return brightness_min + (brightness_max - brightness_min) * transformed


def colour_diagnostics(brightness, invalid, brightness_min, brightness_max,
                       tolerance=0.5 / 255.0):
    valid = ~np.asarray(invalid, dtype=bool)
    total_valid = int(np.count_nonzero(valid))
    fraction = lambda mask: (float(np.count_nonzero(mask & valid)) / total_valid
                             if total_valid else 0.0)
    return {
        "valid_pixels": total_valid,
        "invalid_fraction": float(np.mean(~valid)),
        "lower_bound_fraction": fraction(brightness <= brightness_min + tolerance),
        "upper_bound_fraction": fraction(brightness >= brightness_max - tolerance),
    }


def domain_coloring(values, invalid, value_range, phase_only=False, *,
                    style=None, saturation=0.97, brightness_min=0.50,
                    brightness_max=0.98, gamma=0.65, band_frequency=2.4,
                    band_contrast=0.85, return_diagnostics=False):
    """Colour a complex field; black is reserved for invalid pixels."""
    z = np.asarray(values)
    invalid = np.asarray(invalid, dtype=bool)
    hue = (np.angle(z) + np.pi) / (2.0 * np.pi)
    selected = ("legacy-phase-only" if phase_only and style in (None, "legacy")
                else style or "legacy")
    effective_saturation = 0.82 if selected.startswith("legacy") else saturation
    value = brightness_field(
        z, invalid, value_range, style=selected,
        brightness_min=brightness_min, brightness_max=brightness_max,
        gamma=gamma, band_frequency=band_frequency,
        band_contrast=band_contrast)
    hsv = np.stack((hue, np.full(z.shape, effective_saturation), value), axis=-1)
    rgb = np.rint(255.0 * hsv_to_rgb(hsv)).astype(np.uint8)
    rgb[invalid] = 0
    diagnostics = colour_diagnostics(
        value, invalid, 0.18 if selected == "legacy" else
        (0.9 if selected == "legacy-phase-only" else brightness_min),
        0.95 if selected == "legacy" else
        (0.9 if selected == "legacy-phase-only" else brightness_max))
    return (rgb, diagnostics) if return_diagnostics else rgb


def parameter_tag(args):
    clean = lambda x: str(x).replace("-", "m").replace(".", "p")
    return f"eta{clean(args.eta)}_delta{clean(args.delta)}_n{args.n}_branch{args.branch}"


def metadata_text(args, value_range):
    return ("Exploratory iterates of manuscript Eq. fedoryuk-local-pullback; "
            "NumPy principal branches; naive regularization: "
            f"eps_den={args.eps_den:g}, exp_clip={args.exp_clip:g}, "
            f"z_cap={args.z_cap:g}; invalid=black; shared log1p modulus "
            f"range={value_range}; no branch-cut tracking or smoothing.")


def save_png(path, rgb, metadata):
    info = PngImagePlugin.PngInfo()
    info.add_text("Description", metadata)
    Image.fromarray(rgb, mode="RGB").save(path, pnginfo=info)


def make_outputs(args):
    x = np.linspace(args.xmin, args.xmax, args.width)
    y = np.linspace(args.ymin, args.ymax, args.height)
    grid = x[None, :] + 1j * y[:, None]
    counts = tuple(args.iterations)
    outputs, masks, stats = iterate_map(
        grid, counts, eta=args.eta, delta=args.delta, n=args.n,
        branch=args.branch, eps_den=args.eps_den, exp_clip=args.exp_clip,
        z_cap=args.z_cap)
    if args.value_range:
        value_range = tuple(args.value_range)
    else:
        value_range = normalization_range(outputs, masks, tuple(args.percentiles))
    rgbs = {k: domain_coloring(
        outputs[k], masks[k], value_range, args.phase_only, style=args.colour_style,
        saturation=args.saturation, brightness_min=args.brightness_min,
        brightness_max=args.brightness_max, gamma=args.gamma,
        band_frequency=args.band_frequency, band_contrast=args.band_contrast)
            for k in counts}
    outdir = Path(args.output_dir)
    outdir.mkdir(parents=True, exist_ok=True)
    tag = parameter_tag(args)
    meta = metadata_text(args, value_range)
    paths = []
    for k in counts:
        path = outdir / f"iterated_wkb_k{k}_{tag}.png"
        save_png(path, np.flipud(rgbs[k]), meta + f" Iteration depth k={k}.")
        paths.append(path)
    fig, axes = plt.subplots(1, len(counts), figsize=(5.2 * len(counts), 4.8),
                             constrained_layout=True, squeeze=False)
    for ax, k in zip(axes[0], counts):
        ax.imshow(rgbs[k], extent=(args.xmin, args.xmax, args.ymin, args.ymax),
                  origin="lower", interpolation="nearest")
        ax.set_title(f"Naively regularized $\\Psi^{{\\circ {k}}}$")
        ax.set_xlabel(r"$\Re z_0$")
        ax.set_ylabel(r"$\Im z_0$")
    fig.suptitle(f"Iterated local Fedoryuk--Weber portrait ({args.branch} branch)\n"
                 "principal branches; naive numerical regularization")
    panel_png = outdir / f"iterated_wkb_comparison_{tag}.png"
    panel_pdf = outdir / f"iterated_wkb_comparison_{tag}.pdf"
    fig.savefig(panel_png, dpi=args.dpi, metadata={"Description": meta})
    fig.savefig(panel_pdf, metadata={"Title": "Iterated local WKB portraits",
                                     "Subject": meta})
    plt.close(fig)
    paths.extend((panel_png, panel_pdf))
    sidecar = outdir / f"iterated_wkb_metadata_{tag}.json"
    payload = {
        "formula_source": "manuscript/manuscript.tex, eq:fedoryuk-local-pullback",
        "object": "Psi_loc (not W)", "parameters": vars(args),
        "value_range_log1p_modulus": value_range,
        "regularization": meta, "statistics": [asdict(item) for item in stats],
        "files": [str(path) for path in paths],
    }
    sidecar.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    paths.append(sidecar)
    total = grid.size
    print(f"domain=[{args.xmin},{args.xmax}]x[{args.ymin},{args.ymax}] grid={args.width}x{args.height}")
    print(f"eta={args.eta} delta={args.delta} n={args.n} branch={args.branch} "
          f"eps_den={args.eps_den} exp_clip={args.exp_clip} z_cap={args.z_cap}")
    print(f"colour: hue=arg, saturation=0.82, shared log1p|z| range={value_range}, "
          f"phase_only={args.phase_only}; invalid=black")
    for step, item in enumerate(stats, 1):
        print(f"iteration {step}: denominator_floor={item.denominator_floored} "
              f"({item.denominator_floored/total:.6%}), exponent_clip={item.exponent_clipped} "
              f"({item.exponent_clipped/total:.6%}), radial_cap={item.radial_capped} "
              f"({item.radial_capped/total:.6%}), new_nonfinite={item.nonfinite} "
              f"({item.nonfinite/total:.6%}), invalid_total={item.invalid_total} "
              f"({item.invalid_total/total:.6%})")
    print("outputs:", *(str(path) for path in paths), sep="\n  ")
    return paths, outputs, masks, stats, value_range


def parser():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--xmin", type=float, default=-5.5); p.add_argument("--xmax", type=float, default=2.5)
    p.add_argument("--ymin", type=float, default=-4.0); p.add_argument("--ymax", type=float, default=4.0)
    p.add_argument("--width", type=int, default=800); p.add_argument("--height", type=int, default=800)
    p.add_argument("--eta", type=float, default=8.0, help="eta=|F|/V > 0")
    p.add_argument("--delta", type=float, default=0.7, help="delta=hbar*omega_0/V")
    p.add_argument("--n", type=int, default=0, help="nonnegative local Weber/Hermite level")
    p.add_argument("--branch", choices=("R", "I"), default="I", help="local real- or imaginary-axis sector pair")
    p.add_argument("--iterations", type=int, nargs="+", default=[2, 3, 4])
    p.add_argument("--eps-den", type=float, default=1e-8, help="modulus floor for every z denominator")
    p.add_argument("--exp-clip", type=float, default=80.0, help="clip Re of every complex exponential to +/- this value")
    p.add_argument("--z-cap", type=float, default=1e6, help="post-map radial modulus cap")
    p.add_argument("--percentiles", type=float, nargs=2, default=(2.0, 98.0), help="shared finite log1p-modulus percentiles")
    p.add_argument("--value-range", type=float, nargs=2, help="fixed shared log1p-modulus range")
    p.add_argument("--phase-only", action="store_true", help="constant brightness 0.9")
    p.add_argument("--colour-style", choices=COLOUR_STYLES, default="legacy",
                   help="named colouring; legacy reproduces Prompt 12a")
    p.add_argument("--saturation", type=float, default=0.97)
    p.add_argument("--brightness-min", type=float, default=0.50)
    p.add_argument("--brightness-max", type=float, default=0.98)
    p.add_argument("--gamma", type=float, default=0.65,
                   help="nonlinear bright-phase-modulus exponent")
    p.add_argument("--band-frequency", type=float, default=2.4,
                   help="smooth cycles across normalized log modulus")
    p.add_argument("--band-contrast", type=float, default=0.85,
                   help="blend weight of smooth modulus bands")
    p.add_argument("--output-dir", default="figures/12a_iterated_wkb")
    p.add_argument("--dpi", type=int, default=180)
    return p


def main(argv=None):
    args = parser().parse_args(argv)
    if args.eta <= 0 or args.n < 0 or min(args.width, args.height) < 2:
        raise SystemExit("eta must be positive, n nonnegative, and both dimensions >=2")
    if args.eps_den <= 0 or args.exp_clip <= 0 or args.z_cap <= 0:
        raise SystemExit("regularization thresholds must be positive")
    if any(k < 1 for k in args.iterations):
        raise SystemExit("iteration counts must be positive")
    make_outputs(args)


if __name__ == "__main__":
    main()
