#!/usr/bin/env python3
"""Dressed (multiplicative) Bender--Bettencourt iteration checks."""

from __future__ import annotations

import importlib.util
from pathlib import Path

import sympy as sp


def _load(name, filename):
    path = Path(__file__).with_name(filename)
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def dressed_equation_check():
    x, lam, N, delta, de = sp.symbols("x lambda N delta Delta_e", nonzero=True)
    b = 2*(N+delta)
    Y0 = sp.Function("Y0")(x)
    Z = sp.Function("Z")(x)
    Y = Y0*Z
    L = lambda q: (x**2*sp.diff(q, x, 2)/2+b*x*sp.diff(q, x)/2-x*q/2)
    full = L(Y)-lam**2*(2*sp.diff(Y, x)+2*N*Y/x)-de*Y
    edge_rule = (sp.diff(Y0, x, 2), (x*Y0-x*sp.diff(Y0, x)*b)/(x**2))
    reduced = sp.factor((full/Y0).subs(*edge_rule))
    r = sp.diff(Y0, x)/Y0
    expected = (x**2*sp.diff(Z, x, 2)/2
                +(x**2*r+b*x/2)*sp.diff(Z, x)
                -lam**2*(2*sp.diff(Z, x)+2*(r+N/x)*Z)-de*Z)
    assert sp.simplify(reduced-expected) == 0
    return sp.factor(expected)


def z1_equation_check():
    x, b, N, e2 = sp.symbols("x b N e2", nonzero=True)
    Y0 = sp.Function("Y0")(x)
    Z1 = sp.Function("Z1")(x)
    r = sp.diff(Y0, x)/Y0
    dressed = (x**2*sp.diff(Z1, x, 2)/2
               +(x**2*r+b*x/2)*sp.diff(Z1, x))
    source = 2*(r+N/x)+e2
    # Multiplying by Y0 recovers the additive Y1 equation identically.
    Y1 = Y0*Z1
    additive = (x**2*sp.diff(Y1, x, 2)/2+b*x*sp.diff(Y1, x)/2-x*Y1/2
                -2*sp.diff(Y0, x)-2*N*Y0/x-e2*Y0)
    edge_rule = (sp.diff(Y0, x, 2), (x*Y0-b*x*sp.diff(Y0, x))/x**2)
    assert sp.simplify(additive.subs(*edge_rule)-Y0*(dressed-source)) == 0
    return sp.Eq(dressed, source)


def y2_solvability(N, delta):
    """Second additive diagonal; its resonant m=0 equation returns e4."""
    stage11a = _load("weak11a_for_11c", "11a_verify_weak_drive.py")
    stage11b = _load("weak11b_for_11c", "11b_verify_bessel_wkb.py")
    b, e2, d = stage11b.subdiagonal_coefficients(N, delta, 4)
    e4 = stage11a.energy4_formula(N, delta)
    a = lambda m: stage11b.edge_coeff(m, b)
    q = {}
    for m in (-2, -1):
        prev = q.get(m-1, 0)
        rhs = 2*(m+1+N)*d.get(m+1, 0)+e2*d.get(m, 0)+e4*a(m)
        q[m] = sp.factor((prev+2*rhs)/(m*(m+b-1)))
    rhs0 = 2*(N+1)*d[1]+e2*d[0]+e4*a(0)
    condition = sp.factor(-q[-1]/2-rhs0)
    assert sp.simplify(condition) == 0
    return {"b": b, "e2": e2, "e4": e4, "negative_coefficients": q,
            "solvability_residual": condition}


def exponential_equations():
    x, b, N, e2, e4 = sp.symbols("x b N e2 e4")
    Y0 = sp.Function("Y0")(x)
    S1, S2 = sp.Function("S1")(x), sp.Function("S2")(x)
    r = sp.diff(Y0, x)/Y0
    A = lambda s: x**2*sp.diff(s, x, 2)/2+(x**2*r+b*x/2)*sp.diff(s, x)
    return {"S1": sp.Eq(A(S1), 2*(r+N/x)+e2),
            "S2": sp.Eq(A(S2), 2*sp.diff(S1, x)+e4
                         -x**2*sp.diff(S1, x)**2/2)}


def dominant_s1_asymptotic():
    """Coefficients S1=A*x^-1/2+B*x^-1 in the dominant Bessel sector."""
    b, e2 = sp.symbols("b e2")
    c = (1-2*b)/4  # Y0'/Y0=x^-1/2+c*x^-1+O(x^-3/2)
    A = -2*e2
    # Match the x^-1/2 term of A_b S1 to 2Y0'/Y0+2N/x+e2.
    B = sp.simplify(A*(-c/sp.Integer(2)+sp.Rational(3, 8)-b/4)-2)
    assert sp.simplify(B+2+e2/2) == 0
    return {"x^-1/2": A, "x^-1": B}


def quotient_series_check(N, delta, max_m=6):
    stage11b = _load("weak11b_quotient", "11b_verify_bessel_wkb.py")
    x = sp.symbols("x")
    b, _e2, d = stage11b.subdiagonal_coefficients(N, delta, max_m)
    y0 = sum(stage11b.edge_coeff(m, b)*x**m for m in range(max_m+2))
    y1 = sum(d[m]*x**m for m in range(-1, max_m+1))
    z1 = sp.series(y1/y0, x, 0, max_m+1).removeO()
    recovered = sp.series(y0*z1-y1, x, 0, max_m+1).removeO()
    assert sp.simplify(recovered) == 0
    return z1


def verify():
    d = sp.symbols("delta")
    assert dressed_equation_check() != 0
    assert z1_equation_check() is not None
    # Explicitly exercise the formerly singular regular case.
    stage11b = _load("weak11b_special", "11b_verify_bessel_wkb.py")
    for delta0 in (sp.Integer(1), sp.Rational(2, 3), sp.Rational(5, 4)):
        _b, _e2, coeff = stage11b.subdiagonal_coefficients(0, delta0, 5)
        assert coeff[-1] == 0
        stage11b.verify_subdiagonal_against_rs(0, delta0, 6)
    for N in (1, 2, 3):
        assert stage11b.subdiagonal_coefficients(N, d, 3)[2][-1] == -2*N/(N+d-1)
        quotient_series_check(N, sp.Rational(2, 3), 5)
    for N in (2, 3, 4):
        y2_solvability(N, d)
    return {"dressed": dressed_equation_check(), "Z1": z1_equation_check(),
            "exponential": exponential_equations(),
            "S1_dominant_asymptotic": dominant_s1_asymptotic(),
            "special_N0_delta1": stage11b.subdiagonal_coefficients(
                0, sp.Integer(1), 4)}


if __name__ == "__main__":
    for key, value in verify().items():
        print(f"{key} = {value}")
