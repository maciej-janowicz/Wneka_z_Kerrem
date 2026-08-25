#!/usr/bin/env python3
"""Checks for the Bessel--WKB match and first upper subdiagonal."""

from __future__ import annotations

import importlib.util
from pathlib import Path

import mpmath as mp
import sympy as sp


def _stage11a():
    path = Path(__file__).with_name("11a_verify_weak_drive.py")
    spec = importlib.util.spec_from_file_location("weak11a", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def edge_ode_residual():
    z, lam, b = sp.symbols("z lambda b", nonzero=True)
    Y = sp.Function("Y")(z)
    return sp.expand(z*sp.diff(Y, z, 2) + b*sp.diff(Y, z) + 2*lam*Y)


def exact_edge_residual():
    """Exact Bargmann residual after using the edge ODE."""
    z, lam, N, delta, de = sp.symbols("z lambda N delta Delta_e")
    Y = sp.Function("Y")(z)
    psi = z**N * Y
    e0 = sp.Rational(1, 2)*N*(N-1) + delta*N
    hpsi = (sp.Rational(1, 2)*z**2*sp.diff(psi, z, 2)
            + delta*z*sp.diff(psi, z) + lam*(z*psi + sp.diff(psi, z)))
    raw = sp.expand(hpsi-(e0+de)*psi)
    edge_rule = sp.diff(Y, z, 2), -(2*(N+delta)*sp.diff(Y, z)+2*lam*Y)/z
    reduced = sp.factor(raw.subs(*edge_rule))
    expected = z**N*(lam*sp.diff(Y, z)+lam*N*Y/z-de*Y)
    assert sp.simplify(reduced-expected) == 0
    return expected


def edge_coeff(m, b):
    if m < 0:
        return sp.Integer(0)
    return 1/(sp.factorial(m)*sp.rf(b, m))


def subdiagonal_coefficients(N, delta, max_m=5):
    """Laurent coefficients Y1=sum d_m x^m, m=-1,0,... ."""
    b = 2*(N+delta)
    if N == 0:
        e2 = -1/delta
    else:
        e2 = N/(N-1+delta) - (N+1)/(N+delta)
    # N=0 has no state |-1>; handle it before forming the expression that
    # becomes the spurious 0/0 at delta=1 (b=2).
    if N == 0:
        d_minus_one = sp.Integer(0)
    else:
        d_minus_one = sp.factor(-4*N/(b-2))
    d = {-1: d_minus_one, 0: sp.Integer(0)}
    # The m=0 equation is the solvability condition that reproduces e2.
    solvability = sp.simplify(-d[-1]/2 - (2*(N+1)*edge_coeff(1, b)+e2))
    assert solvability == 0
    for m in range(1, max_m+1):
        rhs_twice = (4*(m+1+N)*edge_coeff(m+1, b)
                     + 2*e2*edge_coeff(m, b))
        d[m] = sp.factor((d[m-1]+rhs_twice)/(m*(m+b-1)))
    return sp.factor(b), sp.factor(e2), d


def verify_subdiagonal_against_rs(N, delta, max_order=6):
    mod = _stage11a()
    _energy, coeff = mod.rs_series(N, delta, max_order)
    _b, _e2, d = subdiagonal_coefficients(N, delta, max_order-2)
    errors = {}
    for k in range(1, max_order+1):
        n, m = N+k-2, k-2
        if n < 0:
            continue
        relative = coeff.get((k, n), 0) * sp.sqrt(
            sp.factorial(N)/sp.factorial(n))
        predicted = (-2)**m*d[m]
        errors[k] = sp.simplify(relative-predicted)
        assert errors[k] == 0
    return errors


def numerical_bessel_identity(dps=70):
    """Principal Log/sqrt checks away from the negative-real branch cut."""
    mp.mp.dps = dps
    cases = [(mp.mpf("1.7"), mp.mpc("2.3", "0.8")),
             (mp.mpf("3.4"), mp.mpc("-1.2", "0.7")),
             (mp.mpc("2.2", "0.3"), mp.mpc("0.4", "-2.1"))]
    errors = []
    for b, x in cases:
        lhs = mp.hyper([], [b], x)
        root = mp.sqrt(x)  # principal square root
        rhs = mp.gamma(b)*mp.power(x, (1-b)/2)*mp.besseli(b-1, 2*root)
        errors.append(abs(lhs-rhs)/(1+abs(lhs)))
    return {"dps": dps, "cases": cases, "max_relative_error": max(errors)}


def numerical_edge_ode(dps=70):
    mp.mp.dps = dps
    lam, b = mp.mpf("0.037"), mp.mpc("3.1", "0.2")
    points = [mp.mpc("0.7", "0.4"), mp.mpc("-2.0", "1.3"),
              mp.mpc("5.0", "-0.6")]
    residuals = []
    fun = lambda z: mp.hyper([], [b], -2*lam*z)
    for z in points:
        residual = z*mp.diff(fun, z, 2)+b*mp.diff(fun, z)+2*lam*fun(z)
        residuals.append(abs(residual)/(1+abs(fun(z))))
    return {"dps": dps, "lambda": lam, "b": b, "points": points,
            "max_scaled_residual": max(residuals)}


def numerical_dominant_asymptotic(dps=70):
    """Test the dominant I-asymptotic for |arg x|<pi-epsilon."""
    mp.mp.dps = dps
    b = mp.mpf("3.2")
    errors = []
    points = []
    for radius in (mp.mpf("400"), mp.mpf("900"), mp.mpf("1600")):
        for theta in (mp.mpf("-1.0"), mp.mpf("0.2"), mp.mpf("1.1")):
            x = radius*mp.e**(1j*theta)
            exact = mp.hyper([], [b], x)
            approx = (mp.gamma(b)/(2*mp.sqrt(mp.pi))
                      * mp.power(x, (1-2*b)/4)*mp.e**(2*mp.sqrt(x)))
            errors.append(abs(exact/approx-1))
            points.append(x)
    return {"dps": dps, "b": b, "points": points,
            "max_relative_error": max(errors), "last_radius_errors": errors[-3:]}


def symbolic_verify():
    N, delta = sp.symbols("N delta")
    b, e2, d = subdiagonal_coefficients(N, delta, 4)
    assert sp.simplify(b-(2*N+2*delta)) == 0
    assert sp.simplify(e2-(1-delta)/((N-1+delta)*(N+delta))) == 0
    assert exact_edge_residual() != 0
    # Bessel prefactor: z^N*x^((1-2b)/4), x proportional to z.
    assert sp.simplify(N+(1-2*b)/4-(sp.Rational(1, 4)-delta)) == 0
    for fixed_N in range(1, 5):
        verify_subdiagonal_against_rs(fixed_N, delta, 6)
    return {"b": b, "e2": e2, "subdiagonal": d,
            "bargmann_residual": exact_edge_residual()}


def verify():
    symbolic = symbolic_verify()
    identity = numerical_bessel_identity()
    edge_ode = numerical_edge_ode()
    asymptotic = numerical_dominant_asymptotic()
    assert identity["max_relative_error"] < mp.mpf("1e-65")
    assert edge_ode["max_scaled_residual"] < mp.mpf("1e-65")
    assert max(asymptotic["last_radius_errors"]) < mp.mpf("0.04")
    return {"symbolic": symbolic, "bessel_identity": identity,
            "edge_ode": edge_ode,
            "dominant_asymptotic": asymptotic}


if __name__ == "__main__":
    data = verify()
    print("bessel_identity_max_error =", data["bessel_identity"]["max_relative_error"])
    print("asymptotic_last_radius_errors =",
          data["dominant_asymptotic"]["last_radius_errors"])
    print("subdiagonal =", data["symbolic"]["subdiagonal"])
