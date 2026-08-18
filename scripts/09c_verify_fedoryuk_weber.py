#!/usr/bin/env python3
"""Symbolic checks for the local direct Fedoryuk--Weber reduction."""

import sympy as sp

SQRT3 = sp.sqrt(3)


def hermite_matrix_elements(n):
    """Bilinear Hermite matrix elements <n+j|x^k|n>."""
    return {
        "x": {-1: sp.sqrt(n/2), 1: sp.sqrt((n+1)/2)},
        "x3": {
            -3: sp.sqrt(n*(n-1)*(n-2))/(2*sp.sqrt(2)),
            -1: 3*n*sp.sqrt(n)/(2*sp.sqrt(2)),
            1: 3*(n+1)*sp.sqrt(n+1)/(2*sp.sqrt(2)),
            3: sp.sqrt((n+1)*(n+2)*(n+3))/(2*sp.sqrt(2)),
        },
    }


def perturbation_data():
    """Exact first corrections and second-order solvability data."""
    n = sp.symbols("n", integer=True, nonnegative=True)
    delta, e2 = sp.symbols("delta e2", real=True)
    N = n + sp.Rational(1, 2)
    A = 10/3**sp.Rational(5, 4)
    B_R = (2-2*delta-4*SQRT3*N)/3**sp.Rational(3, 4)
    B_I = (2-2*delta+4*SQRT3*N)/3**sp.Rational(3, 4)
    matrices = hermite_matrix_elements(n)
    shifts = (-3, -1, 1, 3)
    M_R = {j: sp.simplify(A*matrices["x3"].get(j, 0)
                           + B_R*matrices["x"].get(j, 0)) for j in shifts}
    # In the rotated differential equation P_I=i(A*t^3-B_I*t).
    M_I = {j: sp.simplify(sp.I*(A*matrices["x3"].get(j, 0)
                                - B_I*matrices["x"].get(j, 0)))
           for j in shifts}
    u1_R = {j: sp.factor(-M_R[j]/(2*j)) for j in shifts}
    u1_I = {j: sp.factor(-M_I[j]/(2*j)) for j in shifts}

    x2 = N
    x4 = sp.Rational(3, 4)*(2*n**2+2*n+1)
    e1_R = delta-1-SQRT3*N
    e1_I = delta-1+SQRT3*N
    W_R_mean = (22/(3*SQRT3)*x4
                +(6*e1_R+12-12*delta)/3*x2
                +(delta**2-delta+2*e2)/SQRT3)
    # T_I=W_s(i t): even powers acquire signs (+,-,+).
    T_I_mean = (22/(3*SQRT3)*x4
                -(6*e1_I+12-12*delta)/3*x2
                +(delta**2-delta+2*e2)/SQRT3)
    square_R = {j: sp.powdenest(M_R[j]**2, force=True) for j in shifts}
    solv_R = sp.factor(W_R_mean-sum(square_R[j]/(2*j) for j in shifts))
    # Operator equation: (H-E)u2=-P_I u1+T_I u0.
    square_I = {j: sp.powdenest(M_I[j]**2, force=True) for j in shifts}
    solv_I = sp.factor(T_I_mean+sum(square_I[j]/(2*j) for j in shifts))
    e2_R = sp.factor(sp.solve(sp.Eq(solv_R, 0), e2)[0])
    e2_I = sp.factor(sp.solve(sp.Eq(solv_I, 0), e2)[0])
    target = delta*(1-2*delta)/6-(6*n**2+6*n+1)/72
    return {
        "n": n, "delta": delta, "A": A, "B_R": B_R, "B_I": B_I,
        "operator_R": (A, B_R), "differential_I": (sp.I*A, -sp.I*B_I),
        "operator_I": (-sp.I*A, sp.I*B_I),
        "matrix_R": M_R, "matrix_I": M_I,
        "u1_R": u1_R, "u1_I": u1_I,
        "solvability_R": solv_R, "solvability_I": solv_I,
        "e2_R": e2_R, "e2_I": e2_I,
        "stage08_target": target,
        "difference_I_stage08": sp.simplify(e2_I-target),
    }


def _phi(level, variable):
    if level < 0:
        return sp.Integer(0)
    return (sp.pi**(-sp.Rational(1, 4))/sp.sqrt(2**level*sp.factorial(level))
            * sp.exp(-variable**2/2)*sp.hermite(level, variable))


def exact_order_q_identity(level, orientation):
    """Return the exact inhomogeneous-equation residual for fixed n."""
    data = perturbation_data()
    x = sp.symbols("x", real=True)
    subs = {data["n"]: level}
    coeffs = data["u1_R" if orientation == "R" else "u1_I"]
    u0 = _phi(level, x)
    u1 = sum(value.subs(subs)*_phi(level+j, x)
             for j, value in coeffs.items() if level+j >= 0)
    if orientation == "R":
        forcing = (data["A"]*x**3+data["B_R"].subs(subs)*x)*u0
    else:
        forcing = sp.I*(data["A"]*x**3-data["B_I"].subs(subs)*x)*u0
    residual = sp.diff(u1, x, 2)-(x**2-(2*level+1))*u1-forcing
    return sp.simplify(sp.expand_func(residual))


def numerical_wavefunction_residuals(level=0, delta_value=0.7,
                                     point=0.37, orientation="R"):
    """Absolute residual of u0+q*u1; predicted order is q**2.

    No division by a Hermite factor is used, so its zeros cause no issue.
    The imaginary branch is evaluated on X=i*t/3**(1/4), t real.
    """
    data = perturbation_data()
    q, X, delta, e1, e2 = sp.symbols("q X delta e1 e2", real=True)
    y = -1+q*X
    e = -sp.Rational(3, 2)+q**2*e1+q**4*e2
    exact_R = (y**-4+2*e*y**-2-2*y**-1
               +q**2*2*(delta-1)*y**-3
               +q**4*delta*(delta-1)*y**-2)/q**2
    a = 3**sp.Rational(1, 4)
    var = a*X if orientation == "R" else -sp.I*a*X
    subs_n = {data["n"]: level, data["delta"]: delta_value}
    u0 = _phi(level, var)
    coeffs = data["u1_R" if orientation == "R" else "u1_I"]
    u1 = sum(value.subs(subs_n)*_phi(level+j, var)
             for j, value in coeffs.items() if level+j >= 0)
    u = u0+q*u1
    e1_value = (delta_value-1 + (-1 if orientation == "R" else 1)
                *SQRT3*(level+sp.Rational(1, 2)))
    e2_value = data["e2_R" if orientation == "R" else "e2_I"].subs(subs_n)
    residual = sp.diff(u, X, 2)-exact_R*u
    X_value = point if orientation == "R" else sp.I*point/a
    expression = residual.subs({X: X_value, delta: delta_value,
                                e1: e1_value, e2: e2_value})
    values = [float(abs(sp.N(expression.subs(q, value))))
              for value in (sp.Rational(1, 20), sp.Rational(1, 40),
                            sp.Rational(1, 80))]
    ratios = tuple(values[j]/values[j+1] for j in range(2))
    assert all(3.4 < ratio < 4.7 for ratio in ratios)
    return values, ratios


def verify():
    q, X, e1, e2, delta = sp.symbols("q X e1 e2 delta", real=True)
    y = -1 + q * X
    e = -sp.Rational(3, 2) + q**2 * e1 + q**4 * e2
    Q0 = y**-4 + 2 * e * y**-2 - 2 * y**-1
    Q1 = 2 * (delta - 1) * y**-3
    Q2 = delta * (delta - 1) * y**-2
    local = sp.series((Q0 + q**2 * Q1 + q**4 * Q2) / q**2,
                      q, 0, 4).removeO().expand()
    coefficients = tuple(sp.factor(local.coeff(q, k)) for k in range(4))
    expected = (
        3*X**2 + 2*(e1 + 1 - delta),
        10*X**3 + (4*e1 + 6 - 6*delta)*X,
        22*X**4 + (6*e1 + 12 - 12*delta)*X**2
        + delta**2 - delta + 2*e2,
        40*X**5 + (8*e1 + 20 - 20*delta)*X**3
        + (2*delta**2 - 2*delta + 4*e2)*X,
    )
    assert all(sp.expand(a-b) == 0 for a, b in zip(coefficients, expected))

    s, nu = sp.symbols("s nu", real=True)
    a = 3**sp.Rational(1, 4)
    Lambda = 2 * (e1 + 1 - delta) / sp.sqrt(3)
    # D_nu(sqrt(2)s) obeys U_ss=(s^2-2nu-1)U.
    model_from_D = s**2 - 2*nu - 1
    real_e1 = delta - 1 - sp.sqrt(3)*(nu + sp.Rational(1, 2))
    rotated_e1 = delta - 1 + sp.sqrt(3)*(nu + sp.Rational(1, 2))
    assert sp.simplify(Lambda.subs(e1, real_e1) - model_from_D + s**2) == 0
    assert sp.simplify(Lambda.subs(e1, rotated_e1) - (2*nu+1)) == 0

    n = sp.symbols("n", integer=True, nonnegative=True)
    hermite_identity = sp.simplify(
        2**(-n/sp.Integer(2))*sp.exp(-s**2/2)*sp.hermite(n, s)
    )
    # Coordinate pullback: X=(y+1)/sqrt(epsilon)=z+eta^(1/3).
    eta, z = sp.symbols("eta z", positive=True)
    eps = eta**(-sp.Rational(2, 3))
    pullback_X = sp.simplify(
        (z/eta**sp.Rational(1, 3) + 1) / sp.sqrt(eps)
    )
    assert pullback_X == eta**sp.Rational(1, 3) + z

    # The odd first perturbation has only Delta n=+-1,+-3 in a Hermite basis.
    N = n + sp.Rational(1, 2)
    A = 10 / 3**sp.Rational(5, 4)
    Bminus = (2 - 2*delta - 4*sp.sqrt(3)*N) / 3**sp.Rational(3, 4)
    Bplus = (2 - 2*delta + 4*sp.sqrt(3)*N) / 3**sp.Rational(3, 4)
    shifts = (-3, -1, 1, 3)

    # Exact residual of the leading model in the scaled exact equation.
    residual = sp.expand(local - coefficients[0])
    assert sp.simplify(residual.coeff(q, 0)) == 0
    assert sp.simplify(sp.limit(residual/q, q, 0) - expected[1]) == 0

    return {
        "local_coefficient": local,
        "R0": coefficients[0], "R1": coefficients[1],
        "R2": coefficients[2], "R3": coefficients[3],
        "weber_scale": a, "Lambda": Lambda,
        "real_axis_e1": real_e1, "rotated_e1": rotated_e1,
        "hermite_factor": hermite_identity,
        "pullback_X": pullback_X, "coupled_shifts": shifts,
        "cubic_coefficient": A, "linear_real": Bminus,
        "linear_rotated": Bplus, "residual": residual,
    }


def numerical_residual_ratios(n_value=0, delta_value=0.7, X_value=0.4):
    """Absolute leading-model residual divided by |u|; it is O(sqrt(eps))."""
    data = verify()
    symbols = {symbol.name: symbol for symbol in data["residual"].free_symbols}
    q, X, e1, e2, delta = (symbols[name]
                            for name in ("q", "X", "e1", "e2", "delta"))
    n = sp.Integer(n_value)
    branch = delta - 1 - sp.sqrt(3)*(n + sp.Rational(1, 2))
    expression = data["residual"].subs(e1, branch).subs(
        {X: X_value, e2: 0, delta: delta_value})
    values = []
    for epsilon in (sp.Rational(1, 100), sp.Rational(1, 400),
                    sp.Rational(1, 1600)):
        values.append(float(abs(expression.subs(q, sp.sqrt(epsilon)))))
    ratios = tuple(values[j] / values[j+1] for j in range(2))
    assert all(1.8 < ratio < 2.2 for ratio in ratios)
    return values, ratios


if __name__ == "__main__":
    for name, value in verify().items():
        print(f"{name} = {value}")
    print("numerical residual values, ratios =", numerical_residual_ratios())
    correction = perturbation_data()
    for name in ("A", "B_R", "B_I", "operator_R", "differential_I",
                 "operator_I", "matrix_R", "matrix_I", "u1_R", "u1_I",
                 "solvability_R", "solvability_I", "e2_R", "e2_I",
                 "difference_I_stage08"):
        print(f"{name} = {correction[name]}")
    for branch in ("R", "I"):
        for level in range(5):
            assert exact_order_q_identity(level, branch) == 0
        print(f"order-q identities {branch}: PASS")
        print(f"wavefunction residual {branch}:",
              numerical_wavefunction_residuals(1, 0.7, orientation=branch))
