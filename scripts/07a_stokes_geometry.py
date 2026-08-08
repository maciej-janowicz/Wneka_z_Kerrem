#!/usr/bin/env python3
"""Plot the leading Stokes geometry for S_+-S_-=4 s t, z=t^2."""

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures" / "stokes_geometry"
BLUE = "#35618d"
ORANGE = "#b66a3c"
INK = "#252525"
GREY = "#777777"


def setup_axis(ax, limit=1.13):
    ax.set_aspect("equal")
    ax.set_xlim(-limit, limit)
    ax.set_ylim(-limit, limit)
    ax.axhline(0, color="#dddddd", lw=0.55, zorder=0)
    ax.axvline(0, color="#dddddd", lw=0.55, zorder=0)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_color("#aaaaaa")
        spine.set_linewidth(0.6)


def ray(ax, angle, style, color=INK, radius=1.04, lw=1.7):
    ax.plot([0, radius * np.cos(angle)], [0, radius * np.sin(angle)],
            ls=style, color=color, lw=lw, solid_capstyle="round", zorder=4)


def line(ax, angle, style, color=INK, radius=1.04, lw=1.7):
    v = radius * np.array([np.cos(angle), np.sin(angle)])
    ax.plot([-v[0], v[0]], [-v[1], v[1]], ls=style, color=color,
            lw=lw, solid_capstyle="round", zorder=4)


def disk_sector(ax, start, stop, color, alpha=0.13, radius=1.0):
    theta = np.linspace(start, stop, 180)
    ax.fill(np.r_[0, radius * np.cos(theta), 0],
            np.r_[0, radius * np.sin(theta), 0],
            color=color, alpha=alpha, linewidth=0, zorder=1)


def dominance_at(t, s, atol=1e-12):
    """Return the dominant exponential label from the sign of Re(s*t)."""
    value = np.real(s * t)
    if value > atol:
        return "+", value
    if value < -atol:
        return "-", value
    return "equal", value


def z_panel(ax, phi):
    setup_axis(ax)
    # q=|q| exp(i phi): equal-modulus at -phi, constant-phase at pi-phi.
    equal = -phi
    phase = np.pi - phi
    ray(ax, equal, "--")
    ray(ax, phase, "-")
    ax.scatter([0], [0], s=33, facecolor="white", edgecolor=INK,
               linewidth=1.2, zorder=6)
    ax.text(0.04, 0.20, r"branch point $z=0$", fontsize=7.2)
    ax.text(0.92, 0.08, "equal modulus", ha="right", fontsize=7)
    ax.text(-0.92, -0.11, "constant phase", ha="left", fontsize=7)
    ax.text(0, -0.48, r"dominance requires a sheet/branch choice",
            ha="center", fontsize=7.5, color=GREY)
    ax.text(0, 0.55, r"$t\mapsto-t$ exchanges $S_+\leftrightarrow S_-$",
            ha="center", fontsize=7.5, color=GREY)
    ax.set_xlabel(r"$\operatorname{Re}z$", labelpad=1)
    ax.set_ylabel(r"$\operatorname{Im}z$", labelpad=1)
    ax.set_title(r"physical $z$-plane ($\arg q=0$)", fontsize=9, pad=5)
    ax.text(0.02, 0.98, "(a)", transform=ax.transAxes, va="top",
            fontweight="bold")


def t_panel(ax, phi):
    setup_axis(ax)
    # Principal illustrative choice arg(s)=(phi+pi)/2; changing its sign
    # only interchanges t and -t / the sheet labels.
    alpha = (phi + np.pi) / 2
    s = np.exp(1j * alpha)
    phase_angle = -alpha
    equal_angle = np.pi / 2 - alpha
    disk_sector(ax, equal_angle - np.pi, equal_angle, BLUE)
    disk_sector(ax, equal_angle, equal_angle + np.pi, ORANGE)
    line(ax, equal_angle, "--")
    line(ax, phase_angle, "-")
    for ang, label in [(0.28, r"$t$ (sheet I)"), (0.28 + np.pi, r"$-t$ (sheet II)")]:
        p = 0.74 * np.array([np.cos(ang), np.sin(ang)])
        ax.scatter(*p, s=20, color=INK, zorder=6)
        offset = np.array([0.05, 0.05]) if np.cos(ang) > 0 else np.array([-0.25, 0.09])
        ax.text(*(p + offset), label, fontsize=7.2,
                ha="left")
    ax.annotate(r"same $z=t^2$", xy=(-0.71, -0.21), xytext=(0.30, -0.83),
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-.33",
                                color=GREY, lw=0.8), color=GREY, fontsize=7.2)
    # Place and determine both labels from sample points normal to the
    # equal-modulus line, rather than assigning signs to hard-coded quadrants.
    samples = [(0.57 * np.exp(-1j * alpha), BLUE),
               (0.57 * np.exp(1j * (np.pi - alpha)), ORANGE)]
    for sample, color in samples:
        branch, value = dominance_at(sample, s)
        sign = ">" if value > 0 else "<"
        ax.text(sample.real, sample.imag,
                rf"$\Re(st){sign}0$" "\n" rf"$e^{{S_{branch}}}$ dominant",
                color=color, ha="center", va="center", fontsize=8)
    ax.set_xlabel(r"$\operatorname{Re}t$", labelpad=1)
    ax.set_ylabel(r"$\operatorname{Im}t$", labelpad=1)
    ax.set_title(r"two-sheeted cover: $z=t^2$, $s^2=-q$", fontsize=9, pad=5)
    ax.text(0.02, 0.98, "(b)", transform=ax.transAxes, va="top",
            fontweight="bold")


def rotation_panel(ax):
    ax.axis("off")
    ax.text(0.0, 1.02, "(c)", transform=ax.transAxes, va="top",
            fontweight="bold")
    ax.text(0.51, 1.00, r"rotation in fixed $z$ coordinates",
            transform=ax.transAxes, ha="center", va="top", fontsize=9)
    phases = [0, np.pi/4, np.pi/2]
    labels = [r"0", r"\pi/4", r"\pi/2"]
    centers = [(0.20, 0.59), (0.51, 0.59), (0.82, 0.59)]
    for phi, lab, center in zip(phases, labels, centers):
        ins = ax.inset_axes([center[0]-0.14, center[1]-0.20, 0.28, 0.40])
        setup_axis(ins, 1.10)
        ray(ins, -phi, "--", radius=1.0, lw=1.35)
        ray(ins, np.pi-phi, "-", radius=1.0, lw=1.35)
        ins.scatter([0], [0], s=12, facecolor="white", edgecolor=INK,
                    linewidth=0.8, zorder=6)
        ins.set_title(r"$\arg F={}$".format(lab), fontsize=7.5, pad=2)
    ax.plot([], [], "--", color=INK, lw=1.5, label=r"equal modulus: $\Re\Delta S=0$")
    ax.plot([], [], "-", color=INK, lw=1.5, label=r"constant phase: $\Im\Delta S=0$")
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, 0.14), frameon=False,
              fontsize=7.6, handlelength=2.7, ncol=2)
    ax.text(0.5, 0.05, r"$U_\chi H(F)U_\chi^\dagger=H(Fe^{i\chi})$: rotation, not a spectral change",
            transform=ax.transAxes, ha="center", fontsize=7.5)


def main():
    mpl.rcParams.update({
        "font.family": "serif", "mathtext.fontset": "stix",
        "font.size": 8.5, "axes.linewidth": 0.6,
        "pdf.fonttype": 42, "ps.fonttype": 42,
    })
    fig = plt.figure(figsize=(7.15, 5.35), constrained_layout=True)
    grid = fig.add_gridspec(2, 2, height_ratios=[1.03, 0.82])
    z_panel(fig.add_subplot(grid[0, 0]), phi=0.0)
    t_panel(fig.add_subplot(grid[0, 1]), phi=0.0)
    rotation_panel(fig.add_subplot(grid[1, :]))
    fig.suptitle(r"Leading exponential geometry: $S_\pm=\pm2st$, $\Delta S=4st$",
                 fontsize=10.5)
    fig.savefig(OUT.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(OUT.with_suffix(".png"), dpi=450, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
