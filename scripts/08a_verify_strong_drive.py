"""Exact symbolic checks for the strong-drive reduction (no diagonalization)."""

import sympy as sp


def _multiply_normal_ordered(left, right):
    """Multiply dictionaries whose keys are powers of (b_dagger, b).

    This helper is used only when every creation factor in ``left`` remains
    to the left of every annihilation factor in ``right``, as in
    (b_dagger-r)^2 (b-r)^2.  It therefore never commutes operators silently.
    """
    result = {}
    for (ld, la), lv in left.items():
        for (rd, ra), rv in right.items():
            assert la == 0 and rd == 0
            key = (ld + rd, la + ra)
            result[key] = sp.expand(result.get(key, 0) + lv * rv)
    return result


def shifted_hamiltonian_coefficients(r, delta, eta):
    creation_squared = {(2, 0): 1, (1, 0): -2 * r, (0, 0): r**2}
    annihilation_squared = {(0, 2): 1, (0, 1): -2 * r, (0, 0): r**2}
    result = {
        key: value / 2
        for key, value in _multiply_normal_ordered(
            creation_squared, annihilation_squared
        ).items()
    }
    additions = {
        (1, 1): delta,
        (1, 0): -delta * r + eta,
        (0, 1): -delta * r + eta,
        (0, 0): delta * r**2 - 2 * eta * r,
    }
    for key, value in additions.items():
        result[key] = sp.expand(result.get(key, 0) + value)
    return {key: sp.expand(value) for key, value in result.items()}


def verify():
    eta, delta, e, e1, u, x, y, n = sp.symbols(
        "eta delta e e1 u x y n", nonzero=True
    )
    energy = eta ** sp.Rational(4, 3) * e
    B1, B2, B3, q = 2 * eta, 2 * delta, -2 * energy, 2 * eta
    D = B3 + B2 / 2 - B2**2 / 4
    H = B1 * (1 - B2 / 2)
    C = 4 * D - sp.Rational(3, 4)
    assert sp.expand(C - (-8 * energy + 4 * delta - 4 * delta**2 - sp.Rational(3, 4))) == 0

    t = eta ** sp.Rational(1, 6) * x
    potential = -4 * q - C / t**2 - 4 * H / t**4 + B1**2 / t**6
    scaled = sp.expand(eta ** sp.Rational(1, 3) * potential)
    f = 4 / x**6 + 8 * e / x**2 - 8
    g = -8 * (1 - delta) / x**4
    h = (4 * delta**2 - 4 * delta + sp.Rational(3, 4)) / x**2
    assert sp.simplify(scaled - (eta ** sp.Rational(4, 3) * f + eta ** sp.Rational(2, 3) * g + h)) == 0

    polynomial = 1 + 2 * e * y**2 - 2 * y**3
    polynomial_y = sp.diff(polynomial, y)
    assert sp.expand(polynomial_y - 2 * y * (2 * e - 3 * y)) == 0
    double_root_e = sp.Rational(3, 2) * y
    double_root_equation = sp.expand(polynomial.subs(e, double_root_e))
    assert sp.expand(double_root_equation - (y**3 + 1)) == 0
    assert sp.factor(polynomial.subs(e, -sp.Rational(3, 2))) == -(y + 1) ** 2 * (2 * y - 1)
    assert polynomial.subs({e: -sp.Rational(3, 2), y: -1}) == 0
    assert sp.diff(polynomial, y).subs({e: -sp.Rational(3, 2), y: -1}) == 0

    nu_squared = sp.Rational(1, 4) - C
    assert sp.expand(nu_squared - (8 * energy + (2 * delta - 1) ** 2)) == 0

    f_local = 4 / x**6 + 8 * e / x**2 - 8
    assert sp.diff(f_local, x, 2).subs({x: sp.I, e: -sp.Rational(3, 2)}) / 2 == 48
    assert sp.diff(f_local, e).subs(x, sp.I) == -8
    assert g.subs(x, sp.I) == -8 * (1 - delta)

    x_l = sp.symbols("x_l")
    p_fun = sp.Function("p")(x_l)

    def d_dzeta(expression):
        return sp.diff(expression, x_l) / p_fun

    liouville_zeta = p_fun ** -sp.Rational(1, 2) * d_dzeta(
        d_dzeta(p_fun ** sp.Rational(1, 2))
    )
    liouville_x = (
        -sp.Rational(3, 4) * p_fun**-4 * sp.diff(p_fun, x_l) ** 2
        + sp.Rational(1, 2) * p_fun**-3 * sp.diff(p_fun, x_l, 2)
    )
    assert sp.simplify(liouville_zeta - liouville_x) == 0

    lam = -2 * (e1 + 1 - delta) / sp.sqrt(3)
    solved_e1 = sp.solve(sp.Eq(lam, -2 * n - 1), e1)[0]
    expected_e1 = delta + sp.sqrt(3) * (n + sp.Rational(1, 2)) - 1
    assert sp.simplify(solved_e1 - expected_e1) == 0

    eps = sp.symbols("eps", positive=True)
    eta_eps = eps ** -3
    r_plain = eps ** -1 - delta * eps / 3
    assert sp.series(r_plain**3 + delta * r_plain - eta_eps, eps, 0, 1) == sp.O(eps)
    r_exact = sp.symbols("r", nonzero=True)
    coefficients = shifted_hamiltonian_coefficients(r_exact, delta, eta)
    stationary = {eta: r_exact**3 + delta * r_exact}
    assert sp.simplify(coefficients[(1, 0)].subs(stationary)) == 0
    assert sp.simplify(coefficients[(0, 1)].subs(stationary)) == 0
    assert coefficients[(1, 1)] == 2 * r_exact**2 + delta
    assert coefficients[(2, 0)] == r_exact**2 / 2
    assert coefficients[(0, 2)] == r_exact**2 / 2
    assert coefficients[(2, 1)] == -r_exact
    assert coefficients[(1, 2)] == -r_exact
    assert coefficients[(2, 2)] == sp.Rational(1, 2)
    assert coefficients[(0, 0)] == r_exact**4 / 2 + delta * r_exact**2 - 2 * eta * r_exact

    A = 2 * r_plain**2 + delta
    omega = sp.sqrt(A**2 - r_plain**4)
    assert sp.expand(omega**2 - ((2 * r_plain**2 + delta) ** 2 - r_plain**4)) == 0
    classical = r_plain**4 / 2 + delta * r_plain**2 - 2 * eta_eps * r_plain
    bogoliubov = classical + omega * (n + sp.Rational(1, 2)) - A / 2
    expansion = sp.series(bogoliubov, eps, 0, 0)
    target = -sp.Rational(3, 2) / eps**4 + expected_e1 / eps**2
    remainder = sp.simplify(sp.series(bogoliubov - target, eps, 0, 2).removeO())
    assert sp.limit(eps**2 * remainder, eps, 0) == 0

    return {
        "C": C,
        "scaled": scaled,
        "factorization": sp.factor(polynomial.subs(e, -sp.Rational(3, 2))),
        "double_root_equation": double_root_equation,
        "liouville": liouville_x,
        "shifted_coefficients": coefficients,
        "nu_squared": nu_squared,
        "e1": solved_e1,
        "bogoliubov": expansion,
    }


if __name__ == "__main__":
    for key, value in verify().items():
        print(f"{key} = {value}")
