"""Exact fourth-order strong-drive perturbation theory.

States are finite dictionaries keyed by the shift from a formal number state
|n>.  This is ladder algebra, not a truncated Hamiltonian diagonalization.
"""

from functools import lru_cache

import sympy as sp

n = sp.symbols("n", integer=True, nonnegative=True)
delta = sp.symbols("delta", real=True)
lam = sp.symbols("lambda", positive=True)
epsilon = sp.symbols("epsilon", positive=True)
sqrt3 = sp.sqrt(3)


def _clean(states):
    return {k: v for k, v in states.items() if v != 0}


def add(*states_list):
    result = {}
    for states in states_list:
        for shift, value in states.items():
            result[shift] = result.get(shift, 0) + value
    return _clean(result)


def scale(states, factor):
    return _clean({shift: factor * value for shift, value in states.items()})


def annihilate(states, level=n):
    result = {}
    for shift, value in states.items():
        occupation = level + shift
        if occupation.is_number and occupation <= 0:
            continue
        result[shift - 1] = value * sp.sqrt(occupation)
    return _clean(result)


def create(states, level=n):
    return _clean({
        shift + 1: value * sp.sqrt(level + shift + 1)
        for shift, value in states.items()
    })


omega = sp.sqrt(3 + 4 * delta * lam**2 + delta**2 * lam**4)
ratio = (2 + delta * lam**2) / omega
C_exact = sp.sqrt((ratio + 1) / 2)
S_exact = -sp.sqrt((ratio - 1) / 2)
C = sp.series(C_exact, lam, 0, 5).removeO()
S = sp.series(S_exact, lam, 0, 5).removeO()
C0_exact, S0_exact = sp.expand(C).coeff(lam, 0), sp.expand(S).coeff(lam, 0)
c0, s0 = sp.symbols("c_0 s_0", real=True)
C0, S0 = c0, s0
C2 = c0 * delta * (-sp.Rational(1, 3) + sqrt3 / 6)
S2 = s0 * delta * (-sp.Rational(1, 3) - sqrt3 / 6)


def b_component(states, order):
    c_coeff, s_coeff = (C0, S0) if order == 0 else (C2, S2)
    return add(
        scale(annihilate(states), c_coeff),
        scale(create(states), s_coeff),
    )


def bdag_component(states, order):
    c_coeff, s_coeff = (C0, S0) if order == 0 else (C2, S2)
    return add(
        scale(create(states), c_coeff),
        scale(annihilate(states), s_coeff),
    )


def word(states, operators):
    for operator in reversed(operators):
        states = operator(states)
    return states


def number(states, level=n):
    return _clean({
        shift: value * (level + shift) for shift, value in states.items()
    })


@lru_cache(maxsize=None)
def _basis_coefficient_action(order, ket_shift):
    states = {ket_shift: sp.Integer(1)}
    b0 = lambda v: b_component(v, 0)
    bd0 = lambda v: bdag_component(v, 0)
    b2 = lambda v: b_component(v, 2)
    bd2 = lambda v: bdag_component(v, 2)
    omega2 = 2 * delta / sqrt3
    omega4 = -delta**2 / (6 * sqrt3)
    if order == 0:
        return scale(number(states), sqrt3)
    if order == 1:
        return scale(add(
            word(states, (bd0, bd0, b0)),
            word(states, (bd0, b0, b0)),
        ), -1)
    if order == 2:
        return add(
            scale(number(states), omega2),
            scale(word(states, (bd0, bd0, b0, b0)), sp.Rational(1, 2)),
        )
    if order == 3:
        terms = []
        for ops in (
            (bd2, bd0, b0), (bd0, bd2, b0), (bd0, bd0, b2),
            (bd2, b0, b0), (bd0, b2, b0), (bd0, b0, b2),
        ):
            terms.append(word(states, ops))
        return scale(add(*terms), -1)
    if order == 4:
        terms = []
        for ops in (
            (bd2, bd0, b0, b0), (bd0, bd2, b0, b0),
            (bd0, bd0, b2, b0), (bd0, bd0, b0, b2),
        ):
            terms.append(word(states, ops))
        return add(
            scale(number(states), omega4),
            scale(add(*terms), sp.Rational(1, 2)),
        )
    return {}


def coefficient_action(order, states):
    return add(*(
        scale(_basis_coefficient_action(order, shift), value)
        for shift, value in states.items()
    ))


def recursive_coefficients():
    """Intermediate-normalization recursion through lambda**4."""
    psi = [{0: sp.Integer(1)}]
    kappa = [sqrt3 * n]
    for order in range(1, 5):
        source = {}
        for j in range(1, order + 1):
            source = add(source, coefficient_action(j, psi[order - j]))
        kappa_j = sp.expand(source.get(0, 0))
        kappa.append(kappa_j)

        rhs = {}
        for j in range(1, order + 1):
            rhs = add(rhs, coefficient_action(j, psi[order - j]))
            rhs = add(rhs, scale(psi[order - j], -kappa[j]))
        correction = {}
        for shift, value in rhs.items():
            if shift != 0:
                correction[shift] = -value / (sqrt3 * shift)
        psi.append(_clean(correction))
    return tuple(kappa), tuple(psi)


@lru_cache(maxsize=None)
def matrix_element(operator_order, bra_shift, ket_shift):
    result = _basis_coefficient_action(operator_order, ket_shift)
    return result.get(bra_shift, 0)


def explicit_fourth_order():
    """Independent generalized finite-sum formula for kappa_4."""
    # Reachable shifts are bounded by four cubic actions.
    odd = (-3, -1, 1, 3)
    even = (-6, -4, -2, 2, 4, 6)
    D = lambda k: -sqrt3 * k  # E_n^(0)-E_(n+k)^(0)
    K = lambda j, a, b_: matrix_element(j, a, b_)

    e2 = K(2, 0, 0)
    for k in odd:
        e2 += K(1, 0, k) * K(1, k, 0) / D(k)

    e4 = K(4, 0, 0)
    for k in (-4, -3, -2, -1, 1, 2, 3, 4):
        e4 += (
            K(1, 0, k) * K(3, k, 0)
            + K(3, 0, k) * K(1, k, 0)
            + K(2, 0, k) * K(2, k, 0)
        ) / D(k)
        e4 -= e2 * K(1, 0, k) * K(1, k, 0) / D(k)**2
        for ell in odd + even:
            mixed = (
                K(1, 0, k) * K(1, k, ell) * K(2, ell, 0)
                + K(1, 0, k) * K(2, k, ell) * K(1, ell, 0)
                + K(2, 0, k) * K(1, k, ell) * K(1, ell, 0)
            )
            if mixed:
                e4 += mixed / (D(k) * D(ell))
            for m in odd:
                if ell in even:
                    quartic_cubic = (
                        K(1, 0, k) * K(1, k, ell)
                        * K(1, ell, m) * K(1, m, 0)
                    )
                    if quartic_cubic:
                        e4 += quartic_cubic / (D(k) * D(ell) * D(m))
    return sp.factor(e2), sp.factor(e4)


@lru_cache(maxsize=1)
def verify():
    # Exact sign audit for the Bogoliubov branch.
    A = 2 / lam**2 + delta
    Omega = omega / lam**2
    assert sp.simplify(C_exact**2 - S_exact**2 - 1) == 0
    assert sp.simplify((2 * C_exact * S_exact)**2 - 1 / omega**2) == 0
    leading_cs = sp.limit(2 * C_exact * S_exact, lam, 0, dir="+")
    assert leading_cs.is_negative
    assert sp.simplify(leading_cs**2 - sp.Rational(1, 3)) == 0
    # Inserting 2CS=-r^2/Omega and C^2+S^2=A/Omega cancels
    # the anomalous coefficient without relying on radical simplification.
    anomalous_reduced = A * (-1 / (2 * omega)) + (
        1 / (2 * lam**2)
    ) * (A / Omega)
    assert sp.simplify(anomalous_reduced) == 0

    kappa_raw, psi = recursive_coefficients()
    leading_subs = {c0: C0_exact, s0: S0_exact}
    kappa = tuple(sp.simplify(value.subs(leading_subs)) for value in kappa_raw)
    assert sp.simplify(kappa[1]) == 0
    assert sp.simplify(kappa[3]) == 0
    explicit2_raw, explicit4_raw = explicit_fourth_order()
    explicit2 = sp.simplify(explicit2_raw.subs(leading_subs))
    explicit4 = sp.simplify(explicit4_raw.subs(leading_subs))
    assert sp.simplify(kappa[2] - explicit2) == 0
    assert sp.simplify(kappa[4] - explicit4) == 0

    # Reconstruct the energy in r, then convert using epsilon=eta^(-1/3).
    r = sp.symbols("r", positive=True)
    k2 = sp.simplify(kappa[2])
    k4 = sp.simplify(kappa[4])
    omega_r = sp.sqrt(3 * r**4 + 4 * delta * r**2 + delta**2)
    vacuum = (
        -sp.Rational(3, 2) * r**4 - delta * r**2
        + omega_r / 2 - (2 * r**2 + delta) / 2
    )
    energy_r = vacuum + sqrt3 * n * r**2 + k2 + k4 / r**2

    r_eps = (
        epsilon**-1 - delta * epsilon / 3
        + delta**3 * epsilon**5 / 81
    )
    assert sp.series(
        r_eps**3 + delta * r_eps - epsilon**-3, epsilon, 0, 5
    ) == sp.O(epsilon**5)
    energy_eta = sp.series(energy_r.subs(r, r_eps), epsilon, 0, 4)
    K_eta = sp.factor(sp.expand(energy_eta.removeO()).coeff(epsilon, 2))

    spacing = sp.factor(K_eta.subs(n, n + 1) - K_eta)
    second_difference = sp.factor(
        K_eta.subs(n, n + 2) - 2 * K_eta.subs(n, n + 1) + K_eta
    )

    return {
        "C_series": C,
        "S_series": S,
        "kappa": kappa,
        "kappa2_explicit": explicit2,
        "kappa4_explicit": explicit4,
        "energy_r": sp.collect(sp.expand(energy_r), r),
        "energy_eta": energy_eta,
        "K_factorized": K_eta,
        "K_expanded": sp.expand(K_eta),
        "spacing_K": spacing,
        "second_difference_K": second_difference,
        "psi_shifts": tuple(tuple(sorted(state)) for state in psi),
    }


if __name__ == "__main__":
    for name, value in verify().items():
        print(f"{name} = {value}")
