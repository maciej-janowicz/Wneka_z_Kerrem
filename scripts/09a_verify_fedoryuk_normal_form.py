#!/usr/bin/env python3
"""Exact checks for the direct Bargmann-to-Fedoryuk reduction."""

import sympy as sp


def verify():
    z, y = sp.symbols("z y", nonzero=True)
    eta, delta, e, eps = sp.symbols("eta delta e eps", positive=True)
    calE = sp.symbols("calE")

    # Psi'' + A Psi' + B Psi=0 after division by z**2.
    A = 2 * delta / z + 2 * eta / z**2
    B = 2 * eta / z - calE / z**2
    gauge_log_derivative = -A / 2
    assert sp.simplify(
        gauge_log_derivative - sp.diff(-delta * sp.log(z) + eta / z, z)
    ) == 0

    # Psi=exp(-integral A/2)u gives u''=R u.
    R = sp.simplify(sp.diff(A, z) / 2 + A**2 / 4 - B)
    expected_R = (
        eta**2 / z**4 + 2 * eta * (delta - 1) / z**3
        + (calE + delta**2 - delta) / z**2 - 2 * eta / z
    )
    assert sp.simplify(R - expected_R) == 0

    # z=eta**(1/3)y, calE=2 eta**(4/3)e, eps=eta**(-2/3).
    scaled = sp.expand(
        eta ** sp.Rational(2, 3)
        * R.subs({z: eta ** sp.Rational(1, 3) * y,
                  calE: 2 * eta ** sp.Rational(4, 3) * e})
    )
    Q0 = 1 / y**4 + 2 * e / y**2 - 2 / y
    Q1 = 2 * (delta - 1) / y**3
    Q2 = (delta**2 - delta) / y**2
    assert sp.simplify(
        scaled - eta ** sp.Rational(4, 3) * Q0
        - eta ** sp.Rational(2, 3) * Q1 - Q2
    ) == 0
    assert sp.simplify(
        scaled / eta ** sp.Rational(4, 3)
        - (Q0 + eps * Q1 + eps**2 * Q2).subs(
            eps, eta ** -sp.Rational(2, 3))
    ) == 0

    P = 1 + 2 * e * y**2 - 2 * y**3
    assert sp.simplify(Q0 - P / y**4) == 0
    Py = sp.diff(P, y)
    assert sp.expand(Py - (4 * e * y - 6 * y**2)) == 0
    point = {y: -1, e: -sp.Rational(3, 2)}
    assert P.subs(point) == 0
    assert Py.subs(point) == 0
    assert sp.diff(P, y, 2).subs(point) == 6
    assert sp.factor(P.subs(e, -sp.Rational(3, 2))) == -(y + 1)**2 * (2*y - 1)

    # Local double-turning-point balance: y+1=eps**(1/2)X and
    # e-e0=eps*e1.  Hence physical energy corrections occur in steps
    # eta**(4/3)*eps=eta**(2/3).
    X, e1 = sp.symbols("X e1")
    local = sp.series(
        P.subs({y: -1 + sp.sqrt(eps) * X,
                e: -sp.Rational(3, 2) + eps * e1}), eps, 0, 2
    ).removeO().expand()
    assert sp.simplify(local.coeff(eps, 1) - (2 * e1 + 3 * X**2)) == 0
    assert sp.simplify(
        eta ** sp.Rational(4, 3)
        * eta ** -sp.Rational(2, 3) - eta ** sp.Rational(2, 3)
    ) == 0

    # Discriminant: generic roots are simple; its zeros locate collisions.
    discriminant = sp.factor(sp.discriminant(P, y))
    assert sp.expand(discriminant + 4 * (8 * e**3 + 27)) == 0

    return {
        "gauge": z**(-delta) * sp.exp(eta/z),
        "normal_coefficient": R,
        "epsilon": eta ** -sp.Rational(2, 3),
        "Q0": Q0,
        "Q1": Q1,
        "Q2": Q2,
        "P": P,
        "discriminant": discriminant,
        "local_P": local,
    }


if __name__ == "__main__":
    for name, value in verify().items():
        print(f"{name} = {value}")
