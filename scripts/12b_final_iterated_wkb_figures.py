#!/usr/bin/env python3
"""Final Prompt-12b exploratory portraits of the regularized local WKB map."""
import argparse
from dataclasses import asdict
import importlib.util
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, PngImagePlugin


SPECS = (
    {"eta": 4.0, "k": 2, "branch": "R", "domain_label": "turning",
     "domain": (-4.0, 0.8, -2.4, 2.4), "style": "bright-phase-modulus"},
    {"eta": 4.0, "k": 2, "branch": "I", "domain_label": "local",
     "domain": (-3.2, -0.2, -1.5, 1.5), "style": "bright-banded-modulus"},
    {"eta": 0.25, "k": 3, "branch": "R", "domain_label": "turning",
     "domain": (-2.0, 1.0, -1.5, 1.5), "style": "bright-equalized"},
    {"eta": 0.25, "k": 3, "branch": "I", "domain_label": "left",
     "domain": (-1.8, -0.1, -1.0, 1.0), "style": "bright-phase-modulus"},
)
THRESHOLDS = {"eps_den": 1e-8, "exp_clip": 80.0, "z_cap": 1e6}
COLOUR = {"saturation": 0.97, "brightness_min": 0.50,
          "brightness_max": 0.98, "gamma": 0.65,
          "band_frequency": 2.4, "band_contrast": 0.85}


def core():
    path = Path(__file__).with_name("12a_iterated_wkb_portraits.py")
    spec = importlib.util.spec_from_file_location("wkb12a_core", path)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod


def slug(x):
    return str(x).replace("-", "m").replace(".", "p")


def filename(spec):
    return (f"final_eta{slug(spec['eta'])}_k{spec['k']}_branch{spec['branch']}_"
            f"domain{spec['domain_label']}_{spec['style']}.png")


def evaluate(mod, spec, resolution, delta=0.7, n=0):
    xmin, xmax, ymin, ymax = spec["domain"]
    x = np.linspace(xmin, xmax, resolution)
    y = np.linspace(ymin, ymax, resolution)
    grid = x[None, :] + 1j*y[:, None]
    outputs, masks, stats = mod.iterate_map(
        grid, (spec["k"],), eta=spec["eta"], delta=delta, n=n,
        branch=spec["branch"], **THRESHOLDS)
    value_range = mod.normalization_range(outputs, masks, (2.0, 98.0))
    rgb, diagnostics = mod.domain_coloring(
        outputs[spec["k"]], masks[spec["k"]], value_range,
        style=spec["style"], return_diagnostics=True, **COLOUR)
    total = grid.size
    applications = []
    for index, item in enumerate(stats, 1):
        raw = asdict(item)
        applications.append({"application": index, **raw,
            **{key + "_fraction": value / total for key, value in raw.items()}})
    record = {**spec, "domain": list(spec["domain"]), "delta": delta, "n": n,
              "resolution": [resolution, resolution], "thresholds": THRESHOLDS,
              "colour_parameters": COLOUR, "normalization_percentiles": [2.0, 98.0],
              "normalization_range_log1p_modulus": list(value_range),
              "colour_diagnostics": diagnostics, "applications": applications,
              "regime": ("strong-drive WKB-motivated portrait" if spec["eta"] == 4.0
                         else "FORMAL EXTRAPOLATION FAR OUTSIDE THE CONTROLLED STRONG-DRIVE ASYMPTOTIC REGIME")}
    return record, np.flipud(rgb)


def metadata(record):
    return json.dumps(record, sort_keys=True, separators=(",", ":"))


def save_png(path, rgb, record):
    info = PngImagePlugin.PngInfo(); info.add_text("Description", metadata(record))
    Image.fromarray(rgb, "RGB").save(path, pnginfo=info, compress_level=9)


def generate(args):
    mod = core(); out = Path(args.output_dir); previews = out / "previews"
    out.mkdir(parents=True, exist_ok=True); previews.mkdir(exist_ok=True)
    preview_records = []
    fig, axes = plt.subplots(2, 2, figsize=(9, 9), constrained_layout=True)
    for ax, spec in zip(axes.flat, SPECS):
        rec, rgb = evaluate(mod, spec, args.preview_resolution, args.delta, args.n)
        preview_records.append(rec)
        ax.imshow(rgb, extent=spec["domain"], origin="upper", interpolation="nearest")
        ax.set_title(f"eta={spec['eta']}, k={spec['k']}, {spec['branch']}, {spec['style']}")
        ax.set_xlabel(r"$\Re z_0$"); ax.set_ylabel(r"$\Im z_0$")
    preview_path = previews / "candidate_gallery.png"
    fig.savefig(preview_path, dpi=120); plt.close(fig)

    finals = []
    for spec in SPECS:
        rec, rgb = evaluate(mod, spec, args.final_resolution, args.delta, args.n)
        rec["file"] = filename(spec)
        save_png(out / rec["file"], rgb, rec); finals.append(rec)
    payload = {
        "formula_source": "manuscript/manuscript.tex, eq:fedoryuk-local-pullback",
        "object": "local sectorial Fedoryuk--Weber approximation treated formally as a regularized self-map",
        "principal_branches": "NumPy principal logarithm/powers; cuts not tracked or continued",
        "regularization": THRESHOLDS,
        "postprocessing": "none: no smoothing, singularity interpolation, denoising, or enhancement",
        "preview_gallery": str(preview_path), "preview_records": preview_records,
        "finals": finals, "final_png_files": [item["file"] for item in finals],
    }
    sidecar = out / "final_iterated_wkb_metadata.json"
    sidecar.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True)); return payload


def parser():
    p = argparse.ArgumentParser(); p.add_argument("--output-dir", default="figures/12b_final_iterated_wkb")
    p.add_argument("--preview-resolution", type=int, default=240)
    p.add_argument("--final-resolution", type=int, default=1400)
    p.add_argument("--delta", type=float, default=0.7); p.add_argument("--n", type=int, default=0)
    return p


if __name__ == "__main__":
    generate(parser().parse_args())
