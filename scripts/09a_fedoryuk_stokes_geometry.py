#!/usr/bin/env python3
"""Trace and validate the leading Fedoryuk quadratic-differential geometry.

Initial directions are derived from the local phase.  Continued curve shapes
are numerical illustrations and do not establish global connectivity.
"""

from dataclasses import dataclass
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures" / "fedoryuk_stokes_geometry"
BLUE, ORANGE, INK = "#35618d", "#b66a3c", "#252525"
X_LIMITS, Y_LIMITS = (-2.25, 1.55), (-1.65, 1.65)
START_RADIUS = 0.010
STEP = 0.00025
MAX_LENGTH = 7.0
POLE_RADIUS = 0.035
TURNING_RADIUS = 0.020
PHASE_TOLERANCE = 2.0e-4
LOCAL_START_TOLERANCE = 2.0e-3


@dataclass(frozen=True)
class TurningPoint:
    root: complex
    multiplicity: int
    coefficient: complex


@dataclass
class Trajectory:
    source: complex
    family: str
    direction: float
    points: np.ndarray
    relative_phase_error: float
    local_start_error: float
    stop_reason: str


def polynomial(z, e):
    return 1 + 2 * e * z**2 - 2 * z**3


def polynomial_derivative(z, e):
    return 4 * e * z - 6 * z**2


def q0(z, e):
    return polynomial(z, e) / z**4


def turning_points(e):
    """Return roots, multiplicities, and exact local leading coefficients."""
    if abs(e + 1.5) < 1e-13:
        return [TurningPoint(-1.0 + 0j, 2, 3.0 + 0j),
                TurningPoint(0.5 + 0j, 1, -72.0 + 0j)]
    result = []
    for root in np.roots([-2.0, 2.0 * e, 0.0, 1.0]):
        # At a simple zero, Q0'(yj)=P'(yj)/yj**4.
        coefficient = polynomial_derivative(root, e) / root**4
        result.append(TurningPoint(complex(root), 1, complex(coefficient)))
    return sorted(result, key=lambda item: (item.root.real, item.root.imag))


def local_directions(multiplicity, coefficient, family, branch_sign=1):
    """Analytic separatrix rays modulo 2*pi.

    Reversing sqrt(a) adds pi to its argument and merely permutes the ray set.
    ``branch_sign`` is retained to test that invariance explicitly.
    """
    if family not in {"stokes", "anti"}:
        raise ValueError("family must be 'stokes' or 'anti'")
    arg_a = np.angle(coefficient)
    if branch_sign not in {1, -1}:
        raise ValueError("branch_sign must be +1 or -1")
    # sqrt(a)->-sqrt(a) sends S to -S.  Both zero-level conditions, and hence
    # their geometric ray sets, are unchanged.
    offset = 0
    numerator_shift = 1 if family == "stokes" else 0
    angles = [
        ((2 * k + numerator_shift + offset) * np.pi - arg_a)
        / (multiplicity + 2)
        for k in range(multiplicity + 2)
    ]
    return np.mod(angles, 2 * np.pi)


def _continuous_sqrt(value, reference=None):
    root = np.sqrt(value)
    if reference is not None and abs(-root - reference) < abs(root - reference):
        root = -root
    return root


def _initial_momentum(start, e, direction, phase):
    root = _continuous_sqrt(q0(start, e))
    candidates = (root, -root)
    radial = np.exp(1j * direction)
    return max(candidates, key=lambda p: np.real((phase / p) * np.conj(radial)))


def _unit_tangent(z, e, phase, reference):
    momentum = _continuous_sqrt(q0(z, e), reference)
    tangent = phase / momentum
    return tangent / abs(tangent), momentum


def _stop_reason(z, source, points, travelled):
    if abs(z) <= POLE_RADIUS:
        return "pole"
    if not (X_LIMITS[0] <= z.real <= X_LIMITS[1]
            and Y_LIMITS[0] <= z.imag <= Y_LIMITS[1]):
        return "plot boundary"
    if travelled >= MAX_LENGTH:
        return "maximum integration length"
    for point in points:
        if abs(point.root - source) > 1e-8 and abs(z - point.root) <= TURNING_RADIUS:
            return "another turning point"
    return ""


def _independent_phase_integral(path, e):
    """Midpoint quadrature with independent square-root continuation."""
    total = 0j
    previous = None
    for left, right in zip(path[:-1], path[1:]):
        midpoint = (left + right) / 2
        momentum = _continuous_sqrt(q0(midpoint, e), previous)
        previous = momentum
        total += momentum * (right - left)
    return total


def _local_start_phase(point, direction, radius):
    power = (point.multiplicity + 2) / 2
    coefficient = 2 * np.sqrt(point.coefficient) / (point.multiplicity + 2)
    return coefficient * (radius * np.exp(1j * direction))**power


def _radial_start_phase(point, e, direction, radius, order):
    """Gauss--Legendre integral from the turning point to the start."""
    nodes, weights = np.polynomial.legendre.leggauss(order)
    rho = radius * (nodes + 1) / 2
    direction_vector = np.exp(1j * direction)
    previous = None
    values = []
    for distance in rho:
        z = point.root + distance * direction_vector
        momentum = _continuous_sqrt(q0(z, e), previous)
        # At the first (nearest-root) node select the local branch implied by
        # sqrt(a)*(z-yj)^(m/2); subsequent nodes use continuity.
        if previous is None:
            expected = np.sqrt(point.coefficient) * (
                distance * direction_vector
            ) ** (point.multiplicity / 2)
            momentum = _continuous_sqrt(q0(z, e), expected)
        previous = momentum
        values.append(momentum * direction_vector)
    return radius / 2 * np.dot(weights, values)


def trace_trajectory(point, all_points, e, family, direction):
    phase = 1j if family == "stokes" else 1.0 + 0j
    start = point.root + START_RADIUS * np.exp(1j * direction)
    momentum = _initial_momentum(start, e, direction, phase)
    path = [start]
    travelled = 0.0
    reason = ""
    while not reason:
        z = path[-1]
        tangent1, momentum1 = _unit_tangent(z, e, phase, momentum)
        predicted = z + STEP * tangent1
        tangent2, momentum2 = _unit_tangent(predicted, e, phase, momentum1)
        new = z + STEP * (tangent1 + tangent2) / 2
        if abs(new - z) < STEP * 0.2:
            reason = "step collapse"
            break
        path.append(new)
        travelled += abs(new - z)
        momentum = momentum2
        reason = _stop_reason(new, point.root, all_points, travelled)

    path = np.asarray(path, dtype=complex)
    phase_values = [0j]
    previous = None
    for left, right in zip(path[:-1], path[1:]):
        midpoint = (left + right) / 2
        p_mid = _continuous_sqrt(q0(midpoint, e), previous)
        previous = p_mid
        phase_values.append(phase_values[-1] + p_mid * (right - left))
    phase_values = np.asarray(phase_values)
    component = phase_values.real if family == "stokes" else phase_values.imag
    relative_error = float(np.max(np.abs(component - component[0])))
    # The leading local phase has an exactly vanishing forbidden component on
    # an analytic ray.  Bound the finite-radius remainder numerically by the
    # 64-point value plus the 32/64 Gauss--Legendre difference.
    leading_phase = _local_start_phase(point, direction, START_RADIUS)
    assert abs(leading_phase.real if family == "stokes" else leading_phase.imag) < 1e-12
    local32 = _radial_start_phase(point, e, direction, START_RADIUS, 32)
    local64 = _radial_start_phase(point, e, direction, START_RADIUS, 64)
    forbidden = local64.real if family == "stokes" else local64.imag
    local_error = float(abs(forbidden) + abs(local64 - local32))
    if relative_error > PHASE_TOLERANCE or local_error > LOCAL_START_TOLERANCE:
        raise RuntimeError(
            f"{family} validation failed at {point.root}: "
            f"relative={relative_error:.3e}, local={local_error:.3e}"
        )
    return Trajectory(point.root, family, direction, path, relative_error,
                      local_error, reason)


def compute_panel(e):
    points = turning_points(e)
    trajectories = []
    # No curves are manually deleted.  Each analytic local ray is traced once;
    # coincident later portions remain visible and document genuine merging.
    for point in points:
        for family in ("stokes", "anti"):
            for direction in local_directions(
                    point.multiplicity, point.coefficient, family):
                trajectories.append(trace_trajectory(
                    point, points, e, family, float(direction)))
    return points, trajectories


def validate_trajectories(trajectories):
    return {
        "max_relative_phase_error": max(t.relative_phase_error for t in trajectories),
        "max_local_start_error": max(t.local_start_error for t in trajectories),
        "trajectory_count": len(trajectories),
        "stop_reasons": sorted({t.stop_reason for t in trajectories}),
    }


def panel(ax, e, title):
    points, trajectories = compute_panel(e)
    for trajectory in trajectories:
        color, style = ((BLUE, "-") if trajectory.family == "stokes"
                        else (ORANGE, "--"))
        # The short source-to-start segment is the analytic local ray; the
        # remainder is the numerical continuation.
        ax.plot([trajectory.source.real, trajectory.points[0].real],
                [trajectory.source.imag, trajectory.points[0].imag], style,
                color=color, lw=1.05, alpha=0.95)
        ax.plot(trajectory.points.real, trajectory.points.imag, style,
                color=color, lw=0.82, alpha=0.84)
    for point in points:
        ax.scatter(point.root.real, point.root.imag,
                   s=34 if point.multiplicity == 2 else 23,
                   marker="D" if point.multiplicity == 2 else "o",
                   color=INK, zorder=5)
    ax.scatter([0], [0], s=48, marker="x", color="#8b2e2e", lw=1.5, zorder=6)
    ax.set(xlim=X_LIMITS, ylim=Y_LIMITS, xlabel=r"$\Re y$", ylabel=r"$\Im y$")
    ax.axhline(0, color="#dddddd", lw=.5)
    ax.axvline(0, color="#dddddd", lw=.5)
    ax.set_aspect("equal")
    ax.set_title(title, fontsize=9)
    return validate_trajectories(trajectories)


def generate_figure():
    mpl.rcParams.update({"font.family": "serif", "mathtext.fontset": "stix",
                         "font.size": 8.5, "pdf.fonttype": 42})
    fig, axes = plt.subplots(1, 2, figsize=(7.15, 3.45), constrained_layout=True)
    separated = panel(axes[0], -1.45, r"separated roots: $e=-1.45$")
    coalesced = panel(axes[1], -1.5, r"coalescence: $e=-3/2$")
    axes[0].plot([], [], color=BLUE, label=r"Fedoryuk Stokes: $\Re S=0$")
    axes[0].plot([], [], "--", color=ORANGE, label=r"anti-Stokes: $\Im S=0$")
    axes[0].scatter([], [], marker="o", color=INK, label="simple turning point")
    axes[0].scatter([], [], marker="D", color=INK, label="double turning point")
    axes[0].scatter([], [], marker="x", color="#8b2e2e", label=r"pole $y=0$")
    axes[0].legend(frameon=False, fontsize=6.5, loc="lower right")
    fig.suptitle(r"Leading geometry of $p(y,e)^2=P(y;e)/y^4$", fontsize=10)
    fig.savefig(OUT.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(OUT.with_suffix(".png"), dpi=450, bbox_inches="tight")
    plt.close(fig)
    return {"separated": separated, "coalesced": coalesced}


if __name__ == "__main__":
    for name, values in generate_figure().items():
        print(name, values)
