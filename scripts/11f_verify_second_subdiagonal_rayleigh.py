#!/usr/bin/env python3
"""Second subdiagonal, S2, and Rayleigh-quotient checks for stage 11f."""

from __future__ import annotations

import importlib.util
from pathlib import Path

import mpmath as mp
import sympy as sp


def _load(name, filename):
    path = Path(__file__).with_name(filename)
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def second_subdiagonal(N, delta, max_m=8):
    """Return b,e2,e4 and normalized q_m through max_m."""
    s11a = _load("weak11a_for_11f", "11a_verify_weak_drive.py")
    s11b = _load("weak11b_for_11f", "11b_verify_bessel_wkb.py")
    b, e2, d = s11b.subdiagonal_coefficients(N, delta, max_m+1)
    e4 = s11a.energy4_formula(N, delta)
    a = lambda m: s11b.edge_coeff(m, b)
    q = {-3: sp.Integer(0)}
    lowest = max(-2, -N)
    for m in range(-2, lowest):
        q[m] = sp.Integer(0)
    for m in range(lowest, 0):
        rhs = 2*(m+1+N)*d.get(m+1, 0)+e2*d.get(m, 0)
        q[m] = sp.factor((q.get(m-1, 0)+2*rhs)/(m*(m+b-1)))
    solvability = sp.factor(
        -q.get(-1, 0)/2-2*(N+1)*d[1]-e2*d[0]-e4)
    assert sp.simplify(solvability) == 0
    q[0] = sp.Integer(0)  # intermediate normalization
    for m in range(1, max_m+1):
        rhs = (2*(m+1+N)*d.get(m+1, 0)+e2*d.get(m, 0)+e4*a(m))
        q[m] = sp.factor((q[m-1]+2*rhs)/(m*(m+b-1)))
    return {"b": b, "e2": e2, "e4": e4, "d": d, "q": q,
            "lowest_m": lowest, "solvability": solvability}


def verify_against_rs(N, delta, max_order=8):
    s11a = _load("weak11a_rs_for_11f", "11a_verify_weak_drive.py")
    data = second_subdiagonal(N, delta, max_order-4)
    energy, coeff = s11a.rs_series(N, delta, max_order)
    errors = {}
    for k in range(2, max_order+1):
        m, n = k-4, N+k-4
        if n < 0:
            continue
        relative = coeff.get((k, n), 0)*sp.sqrt(
            sp.factorial(N)/sp.factorial(n))
        errors[k] = sp.simplify(relative-sp.Integer(-2)**m*data["q"][m])
        assert errors[k] == 0
    return errors


def green_representation_check():
    """Differentiate the normalized VOP/Green representation abstractly."""
    x, b = sp.symbols("x b", nonzero=True)
    h2 = sp.Function("h2")(x)
    W = sp.Symbol("W")
    residual = sp.factor((h2*x**b*W-h2).subs(W, x**(-b)))
    assert sp.simplify(residual) == 0
    return residual


def s2_identity_check():
    x, b, N, e2, e4 = sp.symbols("x b N e2 e4", nonzero=True)
    y0, y1, y2 = (sp.Function(name)(x) for name in ("Y0", "Y1", "Y2"))
    r = sp.diff(y0, x)/y0
    S1 = y1/y0
    S2 = y2/y0-S1**2/2
    A = lambda f: x**2*sp.diff(f, x, 2)/2+(x**2*r+b*x/2)*sp.diff(f, x)
    rules = {
        sp.diff(y0, x, 2): y0/x-b*sp.diff(y0, x)/x,
        sp.diff(y1, x, 2): (x*y1-b*x*sp.diff(y1, x)
                            +4*sp.diff(y0, x)+4*N*y0/x+2*e2*y0)/x**2,
        sp.diff(y2, x, 2): (x*y2-b*x*sp.diff(y2, x)
                            +4*sp.diff(y1, x)+4*N*y1/x
                            +2*e2*y1+2*e4*y0)/x**2,
    }
    residual = sp.factor((A(S2)-2*sp.diff(S1, x)-e4
                          +x**2*sp.diff(S1, x)**2/2).subs(rules))
    assert sp.simplify(residual) == 0
    return residual


def zero_structure():
    """Principal parts at a simple zero Y0=A*t+..., for generic Y1,Y2."""
    t = sp.symbols("t")
    A, B, C, D, E, F = sp.symbols("A B C D E F", nonzero=True)
    y0, y1, y2 = A*t+B*t**2, C+D*t, E+F*t
    s1 = sp.series(y1/y0, t, 0, 1).removeO()
    s2 = sp.series(y2/y0-sp.Rational(1, 2)*(y1/y0)**2, t, 0, 0).removeO()
    assert sp.expand(s1).coeff(t, -1) == C/A
    assert sp.expand(s2).coeff(t, -2) == -C**2/(2*A**2)
    exact_s1 = y1/y0
    exact_s2 = y2/y0-exact_s1**2/2
    assert sp.simplify(y0*(exact_s2+exact_s1**2/2)-y2) == 0
    return {"S1": s1, "S2": s2, "S2_double_pole": -C**2/(2*A**2)}


def s2_dominant_asymptotic():
    """S2=P*x^-1/2+Q*x^-1+R*x^-3/2 in a dominant Bessel sector."""
    b, e2, e4 = sp.symbols("b e2 e4")
    c = (1-2*b)/4
    d = (4*(b-1)**2-1)/32
    P = -2*e4
    Q = P/4
    other = -P*d/2+Q*(1-b/2-c)
    R = sp.factor(sp.Rational(2, 3)*(other+e2**2/2))
    return {"x^-1/2": P, "x^-1": Q, "x^-3/2": R,
            "nonlinear_source_x^-1": -e2**2/2}


def fock_coefficients(N, delta, lam, max_n=80):
    """Global additive Y0+lambda^2 Y1+lambda^4 Y2 coefficients."""
    s11b = _load("weak11b_fock_for_11f", "11b_verify_bessel_wkb.py")
    max_m = max_n-N
    if isinstance(delta, mp.mpf):
        delta = sp.Rational(str(delta))
    data = second_subdiagonal(N, delta, max_m)
    b, d, q = data["b"], data["d"], data["q"]
    out = []
    for n in range(max_n+1):
        m = n-N
        relative = sp.Integer(0)
        if m >= 0:
            relative += sp.Integer(-2)**m*lam**m*s11b.edge_coeff(m, b)
        if m in d:
            relative += sp.Integer(-2)**m*lam**(m+2)*d[m]
        if m in q:
            relative += sp.Integer(-2)**m*lam**(m+4)*q[m]
        out.append(mp.mpc(sp.N(sp.sqrt(sp.factorial(n)/sp.factorial(N))*relative, 50)))
    return out


def rayleigh_and_variance(N, delta, lam, cutoff=70):
    """Convergent Fock sums; returns norm, Rayleigh quotient, and variance."""
    c = fock_coefficients(N, delta, lam, cutoff+1)
    e = lambda n: mp.mpf(n*(n-1))/2+mp.mpf(delta)*n
    norm = mp.fsum(abs(c[n])**2 for n in range(cutoff+1))
    diag = mp.fsum(e(n)*abs(c[n])**2 for n in range(cutoff+1))
    off = mp.fsum(mp.sqrt(n+1)*c[n].conjugate()*c[n+1]
                  for n in range(cutoff+1))
    energy = (diag+2*mp.mpf(lam)*mp.re(off))/norm
    residual = []
    for n in range(cutoff+1):
        hc = e(n)*c[n]
        if n:
            hc += mp.mpf(lam)*mp.sqrt(n)*c[n-1]
        hc += mp.mpf(lam)*mp.sqrt(n+1)*c[n+1]
        residual.append(hc-energy*c[n])
    variance = mp.fsum(abs(v)**2 for v in residual)/norm
    return {"norm": norm, "energy": energy, "variance": variance,
            "sigma": mp.sqrt(variance), "last_probability": abs(c[cutoff])**2/norm}


def rayleigh_series(N, delta, order=12):
    """Exact formal series of the additive-state Rayleigh quotient."""
    lam = sp.symbols("lambda")
    max_n = N+order
    coeff = fock_coefficients_symbolic(N, delta, lam, max_n)
    norm = sum(v**2 for v in coeff.values())
    diag = sum((sp.Rational(1, 2)*n*(n-1)+delta*n)*v**2
               for n, v in coeff.items())
    off = sum(sp.sqrt(n+1)*coeff.get(n, 0)*coeff.get(n+1, 0)
              for n in range(max_n))
    quotient = sp.series((diag+2*lam*off)/norm, lam, 0, order+1).removeO()
    return sp.collect(sp.expand(quotient), lam)


def fock_coefficients_symbolic(N, delta, lam, max_n):
    s11b = _load("weak11b_symbolic_for_11f", "11b_verify_bessel_wkb.py")
    data = second_subdiagonal(N, delta, max_n-N)
    out = {}
    for n in range(max_n+1):
        m = n-N
        relative = sp.Integer(0)
        if m >= 0:
            relative += sp.Integer(-2)**m*lam**m*s11b.edge_coeff(m, data["b"])
        if m in data["d"]:
            relative += sp.Integer(-2)**m*lam**(m+2)*data["d"][m]
        if m in data["q"]:
            relative += sp.Integer(-2)**m*lam**(m+4)*data["q"][m]
        if relative != 0:
            out[n] = sp.sqrt(sp.factorial(n)/sp.factorial(N))*relative
    return out


def rayleigh_reliable_order(N):
    """Last exact energy order and first omitted state order."""
    if N == 0:
        return 12, 7
    if N == 1:
        return 8, 5
    if N == 2:
        return 6, 4
    return 4, 3


def rayleigh_series_matches_rs(N, delta, order=12):
    s11a = _load("weak11a_energy_for_11f", "11a_verify_weak_drive.py")
    lam = sp.symbols("lambda")
    quotient = rayleigh_series(N, delta, order)
    energy, _ = s11a.rs_series(N, delta, order)
    exact = sum(energy[k]*lam**k for k in range(order+1))
    residual = sp.expand(quotient-exact)
    reliable, state_error_order = rayleigh_reliable_order(N)
    assert all(sp.simplify(residual.coeff(lam, k)) == 0
               for k in range(min(order, reliable)+1))
    first_bad = next((k for k in range(reliable+1, order+1)
                      if sp.simplify(residual.coeff(lam, k)) != 0), None)
    if reliable < order:
        assert first_bad == reliable+2
    return {"rayleigh": quotient, "e6": sp.factor(energy[6]),
            "residual": residual, "reliable_through": reliable,
            "state_error_order": state_error_order, "first_bad": first_bad}


def verify():
    mp.mp.dps = 50
    for N in (0, 1, 2, 3, 4):
        for delta in (sp.Rational(2, 3), sp.Rational(5, 4)):
            verify_against_rs(N, delta, 8)
    series = {N: rayleigh_series_matches_rs(N, sp.Rational(2, 3), 12)
              for N in (0, 1, 2, 3)}
    convergence = {}
    for N in (0, 1, 2):
        small = rayleigh_and_variance(N, mp.mpf("0.75"), mp.mpf("0.08"), 45)
        large = rayleigh_and_variance(N, mp.mpf("0.75"), mp.mpf("0.08"), 65)
        assert abs(small["energy"]-large["energy"]) < mp.mpf("1e-35")
        assert large["last_probability"] < mp.mpf("1e-70")
        assert large["variance"] >= 0
        convergence[N] = large
    return {"green_residual": green_representation_check(),
            "s2_identity": s2_identity_check(), "zeros": zero_structure(),
            "s2_asymptotic": s2_dominant_asymptotic(),
            "rayleigh_series": series, "numerical": convergence}


if __name__ == "__main__":
    result = verify()
    for key, value in result.items():
        print(key, "=", value)
