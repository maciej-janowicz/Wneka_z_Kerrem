#!/usr/bin/env python3
"""Independent checks for the Weber identities and conditional reduction.

The numerical checks evaluate parabolic-cylinder functions themselves.  The
global transfer matrices remain unspecified and are tested only algebraically.
"""

import mpmath as mp
import sympy as sp


def symbolic_verify():
    nu = sp.symbols("nu")
    a = sp.exp(-sp.I * sp.pi * nu)
    c = (sp.sqrt(2 * sp.pi) * sp.exp(-sp.I * sp.pi * (nu + 1) / 2)
         / sp.gamma(-nu))
    d = (sp.sqrt(2 * sp.pi) * sp.exp(sp.I * sp.pi * nu / 2)
         / sp.gamma(nu + 1))

    # DLMF 12.2.17--12.2.20, specialized with a=-nu-1/2, imply
    # c*d=exp(i*pi*nu)-exp(-i*pi*nu).
    reflection = sp.simplify(
        (c * d).rewrite(sp.sin).subs(
            sp.gamma(-nu) * sp.gamma(nu + 1), -sp.pi / sp.sin(sp.pi * nu)))
    assert sp.simplify(reflection -
                       (sp.exp(sp.I * sp.pi * nu) - a)) == 0

    # A=(D_nu(Z),D_{-nu-1}(iZ))^T = M B, where
    # B=(D_nu(-Z),D_{-nu-1}(-iZ))^T.
    q = sp.exp(sp.I * sp.pi * nu)
    M = sp.Matrix([[q, -q * c], [d, -q]])
    # Exchanging the two bases performs the same involution, so M^{-1}=M.
    Minv = M.copy()
    # Do the matrix algebra independently with C*D=q-q^{-1}, the reflection
    # identity just established, avoiding a circular symbolic gamma simplifier.
    C, D, Q = sp.symbols("C D Q", nonzero=True)
    MA = sp.Matrix([[Q, -Q*C], [D, -Q]])
    reduce_cd = lambda x: sp.expand(x).subs(C*D, Q-1/Q)
    assert all(sp.simplify(reduce_cd(x)) == 0 for x in MA*MA-sp.eye(2))
    assert sp.simplify(reduce_cd(MA.det()) + 1) == 0

    theta = sp.pi * nu / 2
    WA = -sp.I * sp.exp(-sp.I * theta)
    WB = sp.I * sp.exp(-sp.I * theta)
    assert sp.simplify(WA / WB + 1) == 0
    determinant = sp.Integer(-1)
    assert sp.simplify(determinant - WA / WB) == 0

    # A generic boundary contraction sees all four Weber entries.
    l1, l2, r1, r2 = sp.symbols("l1 l2 r1 r2")
    scalar = sp.expand((sp.Matrix([[l1, l2]]) * M * sp.Matrix([r1, r2]))[0])
    at_zero = l1*r1*q + l2*r1*d - l2*r2*q
    assert at_zero != 0

    return {"nu": nu, "c_weber": c, "d_weber": d, "matrix": M,
            "inverse": Minv, "wronskian_A": WA, "wronskian_B": WB,
            "determinant": determinant,
            "inverse_product_verified": True,
            "global_scalar": scalar, "global_scalar_at_c_zero": at_zero}


def numerical_verify(dps=70, tol=mp.mpf("1e-55")):
    mp.mp.dps = dps
    nus = [mp.mpf("-1.7"), mp.mpf("-0.25"), mp.mpf("0.37"),
           mp.mpf("1.42"), mp.mpc("0.3", "0.2")]
    zs = [mp.mpc("0.4", "0.7"), mp.mpc("-1.1", "0.2"),
          mp.mpc("1.3", "-0.9")]
    max_residual = mp.mpf("0")
    max_wronskian_error = mp.mpf("0")
    for nu in nus:
        c = mp.sqrt(2 * mp.pi) * mp.e**(-0.5j * mp.pi * (nu + 1)) / mp.gamma(-nu)
        d = mp.sqrt(2 * mp.pi) * mp.e**(0.5j * mp.pi * nu) / mp.gamma(nu + 1)
        for z in zs:
            first = (mp.pcfd(nu, z) - mp.e**(-1j * mp.pi * nu) *
                     mp.pcfd(nu, -z) - c * mp.pcfd(-nu - 1, 1j * z))
            second = (mp.pcfd(-nu - 1, 1j * z) - d * mp.pcfd(nu, -z)
                      + mp.e**(1j * mp.pi * nu) *
                      mp.pcfd(-nu - 1, -1j * z))
            scale = 1 + sum(abs(q) for q in (mp.pcfd(nu, z),
                         mp.pcfd(nu, -z), mp.pcfd(-nu - 1, 1j*z),
                         mp.pcfd(-nu - 1, -1j*z)))
            max_residual = max(max_residual, abs(first)/scale,
                               abs(second)/scale)
        f = lambda z: mp.pcfd(nu, z)
        g = lambda z: mp.pcfd(-nu - 1, 1j*z)
        wr = f(0)*mp.diff(g, 0) - mp.diff(f, 0)*g(0)
        exact = -1j * mp.e**(-0.5j * mp.pi * nu)
        max_wronskian_error = max(max_wronskian_error, abs(wr-exact))
    assert max_residual < tol
    assert max_wronskian_error < tol

    # Near integers, c_W has a simple zero: c(n+h)/h tends to a nonzero limit.
    slopes = {}
    for n in range(6):
        expected = mp.sqrt(2*mp.pi) * mp.e**(-0.5j*mp.pi*(n+1)) * (-1)**(n+1) * mp.factorial(n)
        vals = []
        for h in (mp.mpf("1e-8"), mp.mpf("1e-12"), mp.mpf("1e-16")):
            c = mp.sqrt(2*mp.pi)*mp.e**(-0.5j*mp.pi*(n+h+1))/mp.gamma(-n-h)
            vals.append(c/h)
        assert abs(vals[-1]/expected - 1) < mp.mpf("1e-14")
        slopes[n] = vals[-1]
    return {"dps": dps, "tolerance": tol,
            "max_functional_residual": max_residual,
            "max_wronskian_error": max_wronskian_error,
            "simple_zero_slopes": slopes}


def verify():
    data = symbolic_verify()
    data["numerical"] = numerical_verify()
    return data


if __name__ == "__main__":
    for key, value in verify().items():
        print(f"{key} = {value}")
