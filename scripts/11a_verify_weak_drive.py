#!/usr/bin/env python3
"""Rayleigh--Schrodinger and Bargmann checks for the weak-drive Kerr cavity."""

from __future__ import annotations

import math
from typing import Dict, Tuple

import mpmath as mp
import sympy as sp


def energy0(n, delta):
    return sp.Rational(1, 2) * n * (n - 1) + delta * n


def rs_series(N, delta, order=4):
    """Return epsilon[k] and Fock coefficients c[k,n], with c[0,N]=1."""
    coeff: Dict[Tuple[int, int], sp.Expr] = {(0, N): sp.Integer(1)}
    energy = [energy0(N, delta)] + [sp.Integer(0)] * order
    for k in range(1, order + 1):
        # <N|W|psi_(k-1)>; W/lambda=a+a^dagger.
        energy[k] = sp.simplify(
            sp.sqrt(N) * coeff.get((k - 1, N - 1), 0)
            + sp.sqrt(N + 1) * coeff.get((k - 1, N + 1), 0))
        for n in range(max(0, N - k), N + k + 1):
            if n == N:
                coeff[(k, n)] = sp.Integer(0)
                continue
            wprev = (sp.sqrt(n) * coeff.get((k - 1, n - 1), 0)
                     + sp.sqrt(n + 1) * coeff.get((k - 1, n + 1), 0))
            folded = sum(energy[j] * coeff.get((k - j, n), 0)
                         for j in range(1, k))
            coeff[(k, n)] = sp.factor(
                (wprev - folded) / (energy0(N, delta) - energy0(n, delta)))
    return energy, coeff


def energy4_formula(N, delta):
    """Closed fourth-order coefficient, with nonexistent lower paths omitted."""
    A, B = N - 1 + delta, N + delta
    # Remove nonexistent lower states before division; this also avoids the
    # spurious 0/0 at the regular point N=0, delta=1.
    lower_one = sp.Integer(0) if N == 0 else N / A
    lower_fold = sp.Integer(0) if N == 0 else N / A**2
    e2 = lower_one - (N + 1) / B
    upper = -(N + 1) * (N + 2) / (B**2 * (2*N + 1 + 2*delta))
    lower = sp.Integer(0)
    if N >= 2:
        lower = N * (N - 1) / (A**2 * (2*N - 3 + 2*delta))
    return sp.factor(lower + upper - e2 * (lower_fold + (N + 1) / B**2))


def bargmann_residual(N, delta, order=4):
    lam, z = sp.symbols("lambda z")
    energy, coeff = rs_series(N, delta, order)
    psi = sum(lam**k * coeff.get((k, n), 0) * z**n / sp.sqrt(sp.factorial(n))
              for k in range(order + 1)
              for n in range(max(0, N-k), N+k+1))
    eps = sum(lam**k * energy[k] for k in range(order + 1))
    residual = (sp.Rational(1, 2)*z**2*sp.diff(psi, z, 2)
                + delta*z*sp.diff(psi, z)
                + lam*(z*psi + sp.diff(psi, z)) - eps*psi)
    truncated = sp.expand(residual).series(lam, 0, order + 1).removeO()
    truncated = sum(lam**k * sp.simplify(sp.expand(truncated).coeff(lam, k))
                    for k in range(order + 1))
    return sp.simplify(truncated), psi, eps


def extreme_sums(N, delta, lam, z, terms=30):
    """Upper 0F1 sum and terminating lower 1F1 sum of monotone paths."""
    upper = mp.hyper([], [2*(N+delta)], -2*lam*z)
    lower = mp.hyper([-N], [-2*(N-1+delta)], 2*lam/z)
    upper_raw = mp.nsum(
        lambda k: (-2*lam*z)**k/(mp.factorial(k)*mp.rf(2*(N+delta), k)),
        [0, terms])
    return upper, lower, upper_raw


def numerical_check():
    mp.mp.dps = 50
    cases = [(0, mp.mpf("0.7")), (1, mp.mpf("0.4")),
             (2, mp.mpf("0.8")), (3, mp.mpf("-0.2"))]
    errors = []
    for N, delta in cases:
        upper, _lower, raw = extreme_sums(N, delta, mp.mpf("0.03"),
                                          mp.mpc("8", "1"), 35)
        errors.append(abs(upper-raw))
    return max(errors)


def verify():
    d = sp.symbols("delta")
    for N in range(5):
        energy, coeff = rs_series(N, d, 4)
        assert energy[1] == energy[3] == 0
        assert sp.simplify(energy[2] - (N/(N-1+d) - (N+1)/(N+d))) == 0
        assert sp.simplify(energy[4] - energy4_formula(N, d)) == 0
        assert bargmann_residual(N, d, 4)[0] == 0
        for k in range(5):
            assert all(coeff.get((k, n), 0) == 0
                       for n in range(0, N+k+1) if abs(n-N) > k)
    error = numerical_check()
    assert error < mp.mpf("1e-45")
    return {"symbolic_N": "0,...,4", "order": 4,
            "max_0F1_partial_sum_error": error}


if __name__ == "__main__":
    print(verify())
