#!/usr/bin/env python3
"""Bounded k=2 diagnostic scan and bright gallery for Prompt 12a_1.

This imports the unchanged Fedoryuk--Weber map and disclosed principal-branch
regularization from 12a.  eta=5 is a strong-drive candidate; eta=0.2 is only
a formal extrapolation outside the controlled strong-drive asymptotic regime.
Only Psi_loc composed exactly twice is evaluated and displayed.
"""

import argparse
from dataclasses import asdict
import importlib.util
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


STYLES = ("bright-phase-modulus", "bright-phase-only",
          "bright-banded-modulus", "bright-equalized")
WINDOWS = {
    5.0: {
        "control": (-5.5, 2.5, -4.0, 4.0),
        "turning": (-4.2, 0.8, -2.5, 2.5),
        "left": (-4.5, -0.2, -2.2, 2.2),
        "local": (-3.4, -0.25, -1.6, 1.6),
    },
    0.2: {
        "control": (-5.5, 2.5, -4.0, 4.0),
        "turning": (-2.0, 1.0, -1.5, 1.5),
        "left": (-1.8, -0.1, -1.0, 1.0),
        "local": (-1.25, -0.08, -0.65, 0.65),
    },
}


def stage12a():
    path = Path(__file__).with_name("12a_iterated_wkb_portraits.py")
    spec = importlib.util.spec_from_file_location("iterated_wkb_12a_gallery", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def slug(value):
    return str(value).replace("-", "m").replace(".", "p")


def case_tag(eta, delta, n, branch, window):
    return f"eta{slug(eta)}_delta{slug(delta)}_n{n}_branch{branch}_domain{window}_k2"


def evaluate_case(mod, eta, branch, domain, resolution, thresholds,
                  delta=0.7, n=0):
    xmin, xmax, ymin, ymax = domain
    x = np.linspace(xmin, xmax, resolution)
    y = np.linspace(ymin, ymax, resolution)
    grid = x[None, :] + 1j * y[:, None]
    outputs, masks, stats = mod.iterate_map(
        grid, (2,), eta=eta, delta=delta, n=n, branch=branch,
        eps_den=thresholds["eps_den"], exp_clip=thresholds["exp_clip"],
        z_cap=thresholds["z_cap"])
    values, invalid = outputs[2], masks[2]
    value_range = mod.normalization_range(outputs, masks, (2.0, 98.0))
    phase = np.angle(values[~invalid])
    logs = np.log1p(np.abs(values[~invalid]))
    variation = {
        "circular_phase_resultant": float(abs(np.mean(np.exp(1j * phase)))) if phase.size else 1.0,
        "log_modulus_std": float(np.std(logs)) if logs.size else 0.0,
    }
    colours, occupancy = {}, {}
    for style in STYLES:
        rgb, diagnostics = mod.domain_coloring(
            values, invalid, value_range, style=style, return_diagnostics=True)
        colours[style], occupancy[style] = rgb, diagnostics
    total = grid.size
    record = {
        "eta": eta, "regime": ("strong-drive candidate" if eta == 5.0 else
            "FORMAL EXTRAPOLATION OUTSIDE CONTROLLED STRONG-DRIVE ASYMPTOTICS"),
        "delta": delta, "n": n, "branch": branch, "domain": list(domain),
        "k": 2, "resolution": [resolution, resolution], "thresholds": thresholds,
        "applications": [{**asdict(item), **{key + "_fraction": value / total
            for key, value in asdict(item).items()}} for item in stats],
        "normalization_range": value_range, "variation": variation,
        "brightness_occupancy": occupancy,
    }
    return record, colours, values, invalid


def rank_key(record):
    second = record["applications"][1]
    intervention = (second["exponent_clipped_fraction"] +
                    second["radial_capped_fraction"] +
                    second["denominator_floored_fraction"])
    invalid = second["invalid_total_fraction"]
    variation_penalty = (record["variation"]["circular_phase_resultant"] +
                         1.0 / (1.0 + record["variation"]["log_modulus_std"]))
    return intervention, invalid, variation_penalty


def save_contact_sheet(path_base, colours, title, domain, dpi=150):
    fig, axes = plt.subplots(2, 2, figsize=(10, 9), constrained_layout=True)
    xmin, xmax, ymin, ymax = domain
    for ax, style in zip(axes.flat, STYLES):
        ax.imshow(colours[style], extent=(xmin, xmax, ymin, ymax), origin="lower",
                  interpolation="nearest")
        ax.set_title(style)
        ax.set_xlabel(r"$\Re z_0$"); ax.set_ylabel(r"$\Im z_0$")
    fig.suptitle(title)
    png, pdf = path_base.with_suffix(".png"), path_base.with_suffix(".pdf")
    fig.savefig(png, dpi=dpi); fig.savefig(pdf)
    plt.close(fig)
    return [png, pdf]


def rgb_discrepancy(rgb_a, rgb_b):
    return {
        "mean_absolute_channel_difference": float(np.mean(
            np.abs(rgb_a.astype(float) - rgb_b.astype(float))) / 255.0),
        "changed_pixel_fraction": float(np.mean(np.any(rgb_a != rgb_b, axis=-1))),
    }


def run_gallery(args):
    mod = stage12a()
    outdir = Path(args.output_dir); outdir.mkdir(parents=True, exist_ok=True)
    thresholds = {"eps_den": args.eps_den, "exp_clip": args.exp_clip,
                  "z_cap": args.z_cap}
    records, selected, files = [], {}, []
    for eta in (5.0, 0.2):
        for branch in ("I", "R"):
            branch_cases = []
            for name, domain in WINDOWS[eta].items():
                record, colours, values, invalid = evaluate_case(
                    mod, eta, branch, domain, args.preview_resolution,
                    thresholds, args.delta, args.n)
                record["window"] = name
                records.append(record); branch_cases.append((record, colours, values, invalid))
            best = min(branch_cases, key=lambda item: rank_key(item[0]))
            selected[(eta, branch)] = best
            record, colours, _, _ = best
            tag = case_tag(eta, args.delta, args.n, branch, record["window"])
            warning = ("STRONG-DRIVE CANDIDATE" if eta == 5.0 else
                       "FORMAL EXTRAPOLATION; NOT ASYMPTOTICALLY CONTROLLED")
            files += save_contact_sheet(
                outdir / f"style_contact_{tag}", colours,
                f"{warning}\neta={eta}, delta={args.delta}, n={args.n}, branch={branch}, "
                f"domain={tuple(record['domain'])}, k=2", tuple(record["domain"]))

    # Threshold sensitivity on each selected case: default versus stricter,
    # never chosen to cosmetically lower intervention counts.
    sensitivity = []
    strict = {"eps_den": args.eps_den, "exp_clip": 60.0, "z_cap": 1e5}
    for (eta, branch), (base_record, base_colours, _, _) in selected.items():
        alt_record, alt_colours, _, _ = evaluate_case(
            mod, eta, branch, tuple(base_record["domain"]), args.preview_resolution,
            strict, args.delta, args.n)
        sensitivity.append({"eta": eta, "branch": branch,
                            "domain": base_record["domain"],
                            "baseline_thresholds": thresholds,
                            "alternative_thresholds": strict,
                            "baseline_applications": base_record["applications"],
                            "alternative_applications": alt_record["applications"],
                            "rgb_discrepancy_bright_phase_modulus": rgb_discrepancy(
                                base_colours["bright-phase-modulus"],
                                alt_colours["bright-phase-modulus"])})

    # Six high-resolution candidates: five eta=5, one explicitly extrapolative.
    shortlist_specs = [
        (5.0, "I", "bright-phase-modulus"), (5.0, "I", "bright-phase-only"),
        (5.0, "I", "bright-banded-modulus"), (5.0, "R", "bright-phase-modulus"),
        (5.0, "R", "bright-equalized"), (0.2, "I", "bright-phase-modulus"),
    ]
    shortlist = []
    for eta, branch, style in shortlist_specs:
        preview_record = selected[(eta, branch)][0]
        record, colours, _, _ = evaluate_case(
            mod, eta, branch, tuple(preview_record["domain"]),
            args.high_resolution, thresholds, args.delta, args.n)
        record["window"] = preview_record["window"]
        tag = case_tag(eta, args.delta, args.n, branch, record["window"])
        path = outdir / f"shortlist_{style}_{tag}.png"
        warning = ("strong-drive candidate" if eta == 5.0 else
                   "FORMAL EXTRAPOLATION OUTSIDE CONTROLLED REGIME")
        meta = (f"exploratory iterated-map portrait; {warning}; eta={eta}; "
                f"delta={args.delta}; n={args.n}; branch={branch}; "
                f"domain={tuple(record['domain'])}; k=2; style={style}; "
                "principal branches and naive regularization")
        mod.save_png(path, np.flipud(colours[style]), meta)
        files.append(path)
        shortlist.append({"file": str(path), "style": style, **record})

    fig, axes = plt.subplots(2, 3, figsize=(15, 9), constrained_layout=True)
    for ax, item in zip(axes.flat, shortlist):
        image = plt.imread(item["file"])
        xmin, xmax, ymin, ymax = item["domain"]
        ax.imshow(np.flipud(image), extent=(xmin, xmax, ymin, ymax), origin="lower",
                  interpolation="nearest")
        caveat = "strong-drive" if item["eta"] == 5.0 else "FORMAL EXTRAPOLATION"
        ax.set_title(f"{item['style']}\neta={item['eta']}, {item['branch']}, {caveat}, k=2")
        ax.set_xlabel(r"$\Re z_0$"); ax.set_ylabel(r"$\Im z_0$")
    fig.suptitle("Prompt 12a_1 shortlist: exploratory twice-iterated local WKB portraits")
    shortlist_png = outdir / "shortlist_contact_sheet_k2.png"
    shortlist_pdf = outdir / "shortlist_contact_sheet_k2.pdf"
    fig.savefig(shortlist_png, dpi=args.dpi); fig.savefig(shortlist_pdf); plt.close(fig)
    files += [shortlist_png, shortlist_pdf]
    payload = {
        "formula": "Psi_loc from manuscript eq:fedoryuk-local-pullback; unchanged from 12a",
        "scope": "k=2 only", "colour_defaults": {
            "styles": STYLES, "saturation": 0.97, "brightness_min": 0.50,
            "brightness_max": 0.98, "gamma": 0.65,
            "band_frequency": 2.4, "band_contrast": 0.85,
            "normalization": "per-case finite 2nd--98th percentile of log1p modulus"},
        "scan_records": records, "selected_windows": {
            f"eta={eta},branch={branch}": item[0]["window"]
            for (eta, branch), item in selected.items()},
        "threshold_sensitivity": sensitivity, "shortlist": shortlist,
        "files": [str(path) for path in files],
    }
    sidecar = outdir / "bright_k2_gallery_data.json"
    sidecar.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    files.append(sidecar)
    print(json.dumps({"selected_windows": payload["selected_windows"],
                      "sensitivity": sensitivity,
                      "shortlist_files": [x["file"] for x in shortlist]}, indent=2))
    return payload, files


def parser():
    p = argparse.ArgumentParser()
    p.add_argument("--preview-resolution", type=int, default=260)
    p.add_argument("--high-resolution", type=int, default=1000)
    p.add_argument("--delta", type=float, default=0.7); p.add_argument("--n", type=int, default=0)
    p.add_argument("--eps-den", type=float, default=1e-8)
    p.add_argument("--exp-clip", type=float, default=80.0)
    p.add_argument("--z-cap", type=float, default=1e6)
    p.add_argument("--dpi", type=int, default=160)
    p.add_argument("--output-dir", default="figures/12a_1_bright_k2_wkb_gallery")
    return p


if __name__ == "__main__":
    run_gallery(parser().parse_args())
