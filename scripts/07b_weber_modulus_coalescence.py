#!/usr/bin/env python3
"""Leading-order modulus |Psi_approx| of the Weber-approximate solution
near the coalescing turning-point pair of Section 7 (the strong-drive
Weber connection problem).

Parameters (fixed, agreed with the author, see
manuscripts/changelog_runda18_10_09_2026.md,
manuscripts/changelog_runda21_12_09_2026.md and
manuscripts/changelog_runda22_12_09_2026.md):

    delta = 0        (zero detuning)
    u     = 8         (so 2|F|/V = 2*u**1.5 ~= 45.25)
    n in {0, 3}       (ground state of the local branch, and n=3)

The local-branch energy e(n) = 2E_n/(V u^2) uses the boxed formula
eq:strong-drive-energy of the manuscript,

    E_n/V = -3/2 eta^{4/3} + [delta + sqrt(3)(n+1/2) - 1] eta^{2/3} + O(1),

with u = eta^{2/3} (so eta^{4/3} = u^2, eta^{2/3} = u), giving in this
script's notation e = e0 + e1/u with e0 = -3/2, e1 = delta +
sqrt(3)(n+1/2) - 1. The second (bracketed) coefficient of that formula
is conditional on the unfinished global error control noted at
eq:strong-drive-energy, so the energies used here are illustrative, not
certified eigenvalues -- see the figure caption in the manuscript.

Round 21 fixes (see changelog_runda21_12_09_2026.md, Section "Faza 1",
for full derivation and numerical verification) -- KEPT in Round 22:

1.A -- Continuous-branch tracking (picking, at each step, the root of a
    square root closer to the previous step's value, rather than always
    the principal branch) is applied not only to the denominator
    sqrt(zeta**2 - a_u**2) of the zeta(x) ODE (Round 18 fix) but also to
    (i) the numerator sqrt(Q_u(x)) of that same ODE, and (ii) the
    a_u**2 integral, which is computed by manual fixed-step RK4 stepping
    (tracking the branch node-by-node) instead of mp.quad (whose
    adaptive node placement cannot guarantee a consistent branch across
    the negative-real-axis crossing of Q_u along the integration path).
    Verified: a_u**2 for n=3 is ~0.893 (purely real to ~1e-12 at the
    dps=15 used below); for n=0, ~0.124 (also purely real). Both are
    real because Q_u at the path midpoint (on the imaginary axis, by
    the x -> -conj(x) symmetry of the coalescing pair) is real and
    negative for both n, forcing sqrt(Q_u) there onto the imaginary
    axis and (via the conjugation symmetry of the path) the whole
    integral onto the imaginary axis, i.e. a_u**2 = integral/(i*pi/2)
    onto the reals.

1.B -- Turning points and the ODE right-hand side use the full
    Q_u = f + g/u + h/u**2 (all three orders of the strong-drive
    expansion, eq:strong-drive-all-turning-points) instead of the
    leading order f alone, which is not neutral at u=8: it changes the
    topology of the n=0 pair from a real split (leading order f) to a
    genuinely complex pair (matching the coalescing-pair picture used
    for all other n). Checkpoints (reproduced exactly):
        n=0: xa=-0.1357121+1.0058173j  xb=0.1357121+1.0058173j
        n=3: xa=-0.3489516+0.9112620j  xb=0.3489516+0.9112620j

Round 22 change (see changelog_runda22_12_09_2026.md): Round 21's Phase
1.C (extended domain Im x in [-2,2], generalised multi-obstacle path
avoidance) is REVERTED. The extended window forced a lower grid density
to stay within the compute-time budget, which visibly blurred the
anti-Stokes fringes; recomputing the same (correct) 1.A/1.B physics in
the original small window (box=1.0 around the coalescing pair, as in
Round 20) at higher density brings the fringes back immediately -- this
was a resolution artifact, not a physics regression. The domain is once
again a box of half-width 1 centred on the midpoint of the coalescing
pair, with a single excluded disk around the order-six pole at x=0 (the
four other turning points are outside this window and need no avoidance
here), and the grid density is raised to NX=NY=300 (from 200 in Round
20) since the smaller window makes this affordable.

Integration method otherwise unchanged from Round 18: fixed-step RK4 in
double precision for the zeta(x) ODE; mpmath only for turning-point
root-finding, the a_u**2 integral, and the final D_p evaluation
(arbitrary complex order/argument, no scipy equivalent).

Run with no arguments; the only output is
    figures/weber_modulus_coalescence_12_09_2026.pdf
No intermediate files are written and no state outside this process is
required.
"""

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401  (registers 3d projection)

mp.mp.dps = 15

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures" / "weber_modulus_coalescence_12_09_2026.pdf"

DELTA = mp.mpf('0')
U = mp.mpf('8')
N_VALUES = (0, 3)
NX = NY = 300
BOX = 1.0
R_POLE = 0.2       # excluded neighbourhood of the order-six pole at x=0
STEPS_PER_UNIT = 120
A2_STEPS = 4000    # fixed RK4 steps for the a_u^2 line integral
VMIN, VMAX = -3.0, 6.0
ELEV, AZIM = 28, -60


# ---------------------------------------------------------------------
# Geometry: turning points from the full Q_u (Round 21, Phase 1.B), and
# a_u^2 with continuous branch tracking throughout (Round 21, Phase 1.A).
# ---------------------------------------------------------------------

def Q_full_mp(x, e, delta, u):
    """Full strong-drive Q_u = f + g/u + h/u**2
    (eq:strong-drive-all-turning-points), mpmath version."""
    f = 4/x**6 + 8*e/x**2 - 8
    g = -8*(1 - delta)/x**4
    h = (4*delta**2 - 4*delta + mp.mpf('0.75'))/x**2
    return f + g/u + h/u**2


def refined_roots(e, delta, u):
    """Roots y=x**2 of P_u(y)=0 (eq:strong-drive-all-turning-points),
    equivalent to y**3 * Q_u(sqrt(y)) == 0 after clearing denominators."""
    c2 = 2*e + (4*delta**2 - 4*delta + mp.mpf('0.75'))/(4*u**2)
    c1 = -2*(1 - delta)/u
    return mp.polyroots([-2, c2, c1, 1], maxsteps=200, extraprec=100)


def pick_pair(ys):
    """The two roots y nearest y=-1 (the coalescing pair)."""
    return sorted(ys, key=lambda y: abs(y + 1))[:2]


def x_near_plus_i(y):
    r = mp.sqrt(y)
    return -r if r.imag < 0 else r


def sqrt_branch_mp(w, prev):
    """mpmath sqrt(w), continued from `prev` by picking the closer root."""
    r = mp.sqrt(w)
    if prev is None:
        return r
    return r if abs(r - prev) <= abs(-r - prev) else -r


def a_u_squared(e, delta, u, xa, xb, steps=A2_STEPS):
    """Line integral of sqrt(Q_u) from xa to xb (fixed path, the same
    pair of turning points used for the local Weber comparison), by
    manual fixed-step RK4 with continuous branch tracking (Round 21,
    Phase 1.A -- replaces the old mp.quad call, whose adaptive node
    placement cannot guarantee a consistent branch across the
    negative-real-axis crossing of Q_u that occurs at the path
    midpoint)."""
    h = (xb - xa)/steps
    s = xa
    prev = None
    total = mp.mpc(0)
    for _ in range(steps):
        k1 = sqrt_branch_mp(Q_full_mp(s, e, delta, u), prev)
        k2 = sqrt_branch_mp(Q_full_mp(s + h/2, e, delta, u), k1)
        k3 = sqrt_branch_mp(Q_full_mp(s + h/2, e, delta, u), k2)
        k4 = sqrt_branch_mp(Q_full_mp(s + h, e, delta, u), k3)
        total += (h/6)*(k1 + 2*k2 + 2*k3 + k4)
        prev = k4
        s += h
    return total/(mp.j*mp.pi/2)


def e_of_n(n, delta, u):
    """e(n) = e0 + e1/u from eq:strong-drive-energy, e0=-3/2."""
    e1 = delta + mp.sqrt(3)*(n + mp.mpf('0.5')) - 1
    return mp.mpf('-1.5') + e1/u, e1


def local_branch_geometry(n, delta, u):
    """Return e, e1, the coalescing pair (xa,xb), and a_u^2."""
    e, e1 = e_of_n(n, delta, u)
    ya, yb = pick_pair(refined_roots(e, delta, u))
    xa, xb = x_near_plus_i(ya), x_near_plus_i(yb)
    a2 = a_u_squared(e, delta, u, xa, xb)
    return e, e1, xa, xb, a2


# ---------------------------------------------------------------------
# Field: continuous-branch fixed-step RK4 (double precision) for the
# zeta(x) ODE, with the branch fix applied to both the denominator
# sqrt(zeta**2-a_u**2) (Round 18) and the numerator sqrt(Q_u(x))
# (Round 21, Phase 1.A), plus single-obstacle (pole-only) path avoidance,
# as in Round 18/20 -- the small window means the other four turning
# points never come close to any integration path (Round 22).
# ---------------------------------------------------------------------

def Q_full_np(x, e, delta, u):
    f = 4.0/x**6 + 8.0*e/x**2 - 8.0
    g = -8.0*(1.0 - delta)/x**4
    h = (4.0*delta**2 - 4.0*delta + 0.75)/x**2
    return f + g/u + h/u**2


def sqrt_branch(w, prev):
    """sqrt(w), continued from `prev` by picking the closer root."""
    r = np.sqrt(w)
    if prev is None:
        return r
    return r if abs(r - prev) <= abs(-r - prev) else -r


def deriv_zeta_cont(x, zeta, e, delta, u, a2, num_prev, denom_prev, eps=1e-8):
    num = sqrt_branch(Q_full_np(x, e, delta, u), num_prev)
    w = zeta**2 - a2
    denom = sqrt_branch(w, denom_prev)
    if abs(denom) < eps:
        denom = eps
    return num/denom, num, denom


def rk4_leg(x0, zeta0, x1, e, delta, u, a2, num_prev, denom_prev, steps):
    h = (x1 - x0)/steps
    x, zeta = x0, zeta0
    np_, dp = num_prev, denom_prev
    for _ in range(steps):
        k1, np1, dp1 = deriv_zeta_cont(x, zeta, e, delta, u, a2, np_, dp)
        k2, np2, dp2 = deriv_zeta_cont(x + h/2, zeta + h*k1/2, e, delta, u, a2, np1, dp1)
        k3, np3, dp3 = deriv_zeta_cont(x + h/2, zeta + h*k2/2, e, delta, u, a2, np2, dp2)
        k4, np4, dp4 = deriv_zeta_cont(x + h, zeta + h*k3, e, delta, u, a2, np3, dp3)
        zeta = zeta + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
        x = x + h
        np_, dp = np4, dp4
    return x, zeta, np_, dp


def path_legs(x0, xt, r_pole=R_POLE):
    """Straight line x0->xt, bent around a disk of radius r_pole at the
    origin: the closest-approach point of the segment is pushed
    radially out to the disk boundary when the direct segment would
    cross it. Continuous in xt (reduces to the direct segment exactly
    when the closest approach already clears the disk), so this
    introduces no seam of its own."""
    d = xt - x0
    dd = d.real**2 + d.imag**2
    if dd == 0:
        return [(x0, xt)]
    tstar = min(1.0, max(0.0, -(x0.real*d.real + x0.imag*d.imag)/dd))
    p = x0 + tstar*d
    rp = abs(p)
    if rp >= r_pole or rp == 0:
        return [(x0, xt)]
    w = p*(r_pole/rp)
    return [(x0, w), (w, xt)]


def integrate_zeta(x0, zeta0, xt, e, delta, u, a2, steps_per_unit=STEPS_PER_UNIT):
    zeta = zeta0
    xcur = x0
    np_, dp = None, None
    for xa_leg, xb_leg in path_legs(x0, xt):
        length = abs(xb_leg - xa_leg)
        steps = max(30, int(steps_per_unit*length))
        xcur, zeta, np_, dp = rk4_leg(xa_leg, zeta, xb_leg, e, delta, u, a2, np_, dp, steps)
    dzdx, _, _ = deriv_zeta_cont(xcur, zeta, e, delta, u, a2, np_, dp)
    return zeta, dzdx


def compute_field(e_mp, delta_mp, u_mp, xa_mp, xb_mp, a2_mp, nx=NX, ny=NY, box=BOX):
    """Return (xs, ys, log10|Psi_approx| clipped to [VMIN,VMAX], x0, p)."""
    x0_mp = (xa_mp + xb_mp)/2
    e, a2 = complex(e_mp), complex(a2_mp)
    delta, u = float(delta_mp), float(u_mp)
    x0 = complex(x0_mp)
    xs = np.linspace(x0.real - box, x0.real + box, nx)
    ys = np.linspace(x0.imag - box, x0.imag + box, ny)
    p_mp = u_mp*a2_mp/2 - mp.mpf('0.5')
    c_mp = mp.sqrt(2*u_mp)
    W = np.full((ny, nx), np.nan)
    for j, yv in enumerate(ys):
        for i, xv in enumerate(xs):
            xt = complex(xv, yv)
            if abs(xt) < R_POLE:
                continue
            try:
                zeta, dzdx = integrate_zeta(x0, 0.0 + 0.0j, xt, e, delta, u, a2)
                pref = dzdx**(-0.5)
                val = pref*mp.pcfd(p_mp, c_mp*mp.mpc(zeta.real, zeta.imag))
                W[j, i] = float(abs(val))
            except Exception:
                W[j, i] = np.nan
    with np.errstate(divide='ignore', invalid='ignore'):
        L = np.clip(np.log10(W), VMIN, VMAX)
    return xs, ys, L, x0, complex(p_mp)


# ---------------------------------------------------------------------
# Plotting: two contour panels (top) + two matching 3D surfaces
# (bottom), shared log10|Psi_approx| scale.
# ---------------------------------------------------------------------

def add_contour_panel(ax, xs, ys, L, xa, xb, title, cmap):
    X, Y = np.meshgrid(xs, ys)
    pcm = ax.pcolormesh(X, Y, L, cmap=cmap, vmin=VMIN, vmax=VMAX, shading='auto')
    ax.plot([xa.real, xb.real], [xa.imag, xb.imag], 'o', color='cyan',
            markeredgecolor='k', markersize=5, zorder=5)
    ax.set_title(title, fontsize=10)
    ax.set_xlabel(r'$\mathrm{Re}\,x$')
    ax.set_ylabel(r'$\mathrm{Im}\,x$')
    ax.set_aspect('equal')
    return pcm


def add_surface_panel(ax, xs, ys, L, cmap):
    X, Y = np.meshgrid(xs, ys)
    ax.plot_surface(X, Y, L, rcount=NY, ccount=NX, cmap=cmap,
                     vmin=VMIN, vmax=VMAX, linewidth=0, antialiased=True)
    ax.set_zlim(VMIN, VMAX)
    ax.view_init(elev=ELEV, azim=AZIM)
    ax.set_xlabel(r'$\mathrm{Re}\,x$', labelpad=2, fontsize=8)
    ax.set_ylabel(r'$\mathrm{Im}\,x$', labelpad=2, fontsize=8)
    ax.set_zlabel(r'$\log_{10}|\Psi_{\rm approx}|$', labelpad=2, fontsize=8)
    ax.tick_params(labelsize=7)


def make_figure(field0, field3):
    xs0, ys0, L0, xa0, xb0 = field0
    xs3, ys3, L3, xa3, xb3 = field3
    cmap = plt.get_cmap('magma')

    fig = plt.figure(figsize=(11, 9.5))
    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    add_contour_panel(ax1, xs0, ys0, L0, xa0, xb0,
                       r'$n=0$ (ground state of local branch)', cmap)
    pcm3 = add_contour_panel(ax2, xs3, ys3, L3, xa3, xb3, r'$n=3$', cmap)
    cbar = fig.colorbar(pcm3, ax=[ax1, ax2], orientation='vertical',
                         fraction=0.046, pad=0.03)
    cbar.set_label(r'$\log_{10}|\Psi_{\rm approx}|$')

    ax3 = fig.add_subplot(2, 2, 3, projection='3d')
    ax4 = fig.add_subplot(2, 2, 4, projection='3d')
    add_surface_panel(ax3, xs0, ys0, L0, cmap)
    add_surface_panel(ax4, xs3, ys3, L3, cmap)

    fig.tight_layout(rect=[0, 0, 1, 1])
    return fig


# ---------------------------------------------------------------------

def main():
    fields = {}
    for n in N_VALUES:
        e, e1, xa, xb, a2 = local_branch_geometry(n, DELTA, U)
        xs, ys, L, x0, p = compute_field(e, DELTA, U, xa, xb, a2)
        print(f"n={n}: e={e} e1={e1}")
        print(f"  xa={xa} xb={xb} a2={a2} p={p}")
        fields[n] = (xs, ys, L, complex(xa), complex(xb))

    fig = make_figure(fields[N_VALUES[0]], fields[N_VALUES[1]])
    OUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT, dpi=200)
    plt.close(fig)
    print("saved:", OUT)


if __name__ == '__main__':
    main()
