from fractions import Fraction

import mpmath as mp
import pytest

from kerr_heun.local_series import (
    asymptotic_coefficients,
    taylor_coefficients,
)


def _taylor_residual(B1, B2, B3, q, coefficients):
    residual = []
    for n, c_n in enumerate(coefficients):
        c_previous = coefficients[n - 1] if n else 0
        c_following = coefficients[n + 1] if n + 1 < len(coefficients) else 0
        residual.append(
            B1 * (n + 1) * c_following
            + (n * (n - 1) + B2 * n + B3) * c_n
            + q * c_previous
        )
    return residual


def _explicit_taylor(B1, B2, B3, q):
    A1 = B2 + B3
    A2 = 2 + 2 * B2 + B3
    A3 = 6 + 3 * B2 + B3
    c1 = -B3 / B1
    c2 = (B3 * A1 - q * B1) / (2 * B1**2)
    c3 = (q * B1 * (A2 + 2 * B3) - B3 * A1 * A2) / (6 * B1**3)
    c4 = (
        A3 * B3 * A1 * A2
        - q * B1 * A3 * (A2 + 2 * B3)
        - 3 * q * B1 * B3 * A1
        + 3 * q**2 * B1**2
    ) / (24 * B1**4)
    return [1, c1, c2, c3, c4]


def _asymptotic_residual(B1, B2, B3, q, sigma, root, coefficients):
    """Coefficients of t^{-m} after removing exp(a*t)t^p."""
    a = 2 * sigma * root
    p = mp.mpf("0.5") - B2
    C = p * p + (2 * B2 - 2) * p + 4 * B3
    residual = []
    for m in range(len(coefficients) - 1):
        u_m = coefficients[m]
        u_m1 = coefficients[m - 1] if m >= 1 else 0
        u_m2 = coefficients[m - 2] if m >= 2 else 0
        residual.append(
            -2 * a * (m + 1) * coefficients[m + 1]
            + (m * (m + 1) + C) * u_m
            + 2 * a * B1 * u_m1
            + 2 * B1 * (p - m + 2) * u_m2
        )
    return residual


def test_taylor_exact_coefficients_and_residual():
    parameters = tuple(map(Fraction, (2, 3, -5, 7)))
    coefficients = taylor_coefficients(*parameters, 4)
    assert coefficients[0] == 1
    assert coefficients == _explicit_taylor(*parameters)
    assert _taylor_residual(*parameters, coefficients)[:4] == [0] * 4


def test_taylor_arbitrary_order_complex_and_high_precision():
    mp.mp.dps = 80
    parameters = (
        mp.mpc("1.25", "-0.5"),
        mp.mpc("0.7", "0.2"),
        mp.mpc("-1.1", "0.3"),
        mp.mpc("0.4", "-0.9"),
    )
    high_precision = taylor_coefficients(*parameters, 12)
    machine = taylor_coefficients(*(complex(value) for value in parameters), 12)
    assert len(high_precision) == 13
    assert max(abs(high_precision[n] - machine[n]) for n in range(13)) < mp.mpf("1e-10")
    assert max(abs(value) for value in _taylor_residual(*parameters, high_precision)[:12]) < mp.mpf("1e-70")


@pytest.mark.parametrize("order", [-1, 2.5, True])
def test_taylor_invalid_order(order):
    with pytest.raises(ValueError):
        taylor_coefficients(1, 2, 3, 4, order)


def test_taylor_rejects_degenerate_B1():
    with pytest.raises(ValueError):
        taylor_coefficients(0, 2, 3, 4, 4)


@pytest.mark.parametrize("sigma", [-1, 1])
def test_asymptotic_coefficients_and_residual(sigma):
    mp.mp.dps = 80
    B1 = mp.mpc("0.8", "0.3")
    B2 = mp.mpc("1.2", "-0.2")
    B3 = mp.mpc("-0.7", "0.4")
    q = mp.mpc("0.6", "0.5")
    root = mp.sqrt(-q)
    coefficients = asymptotic_coefficients(
        B1, B2, B3, q, 7, sigma=sigma, sqrt_minus_q=root
    )
    a = 2 * sigma * root
    p = mp.mpf("0.5") - B2
    C = p * p + (2 * B2 - 2) * p + 4 * B3
    assert coefficients[0] == 1
    assert mp.almosteq(coefficients[1], C / (2 * a))
    assert mp.almosteq(coefficients[2], B1 / 2 + C * (C + 2) / (8 * a**2))
    assert mp.almosteq(
        coefficients[3],
        C * (C + 2) * (C + 6) / (48 * a**3)
        + B1 * (3 * C + 6 + 4 * p) / (12 * a),
    )
    assert max(abs(value) for value in _asymptotic_residual(
        B1, B2, B3, q, sigma, root, coefficients
    )) < mp.mpf("1e-70")


def test_asymptotic_branch_relabelling():
    q = 2 + 3j
    root = mp.sqrt(-q)
    positive = asymptotic_coefficients(1, 2, 3, q, 8, sigma=1, sqrt_minus_q=root)
    relabelled = asymptotic_coefficients(1, 2, 3, q, 8, sigma=-1, sqrt_minus_q=-root)
    assert all(mp.almosteq(left, right) for left, right in zip(positive, relabelled))


def test_asymptotic_fixed_root_sigma_parity_through_order_eight():
    q = mp.mpc("0.6", "0.5")
    root = mp.sqrt(-q)
    parameters = (
        mp.mpc("0.8", "0.3"),
        mp.mpc("1.2", "-0.2"),
        mp.mpc("-0.7", "0.4"),
        q,
    )
    positive = asymptotic_coefficients(
        *parameters, 8, sigma=1, sqrt_minus_q=root
    )
    negative = asymptotic_coefficients(
        *parameters, 8, sigma=-1, sqrt_minus_q=root
    )
    assert all(mp.almosteq(negative[n], positive[n]) for n in range(0, 9, 2))
    assert all(mp.almosteq(negative[n], -positive[n]) for n in range(1, 9, 2))


def test_asymptotic_exact_arithmetic_beyond_displayed_order():
    coefficients = asymptotic_coefficients(
        Fraction(2), Fraction(3), Fraction(-1), Fraction(-4), 9,
        sigma=1, sqrt_minus_q=Fraction(2),
    )
    assert len(coefficients) == 10
    assert all(isinstance(value, Fraction) for value in coefficients)


def test_asymptotic_rejects_invalid_parameters():
    with pytest.raises(ValueError):
        asymptotic_coefficients(1, 2, 3, 0, 3, sigma=1, sqrt_minus_q=1)
    with pytest.raises(ValueError):
        asymptotic_coefficients(1, 2, 3, 4, 3, sigma=0, sqrt_minus_q=2j)
    with pytest.raises(ValueError):
        asymptotic_coefficients(1, 2, 3, 4, -1, sigma=1, sqrt_minus_q=2j)


def test_asymptotic_validates_supplied_square_root():
    exact_parameters = (Fraction(2), Fraction(3), Fraction(-1), Fraction(-4))
    for root in (Fraction(2), Fraction(-2)):
        assert len(asymptotic_coefficients(
            *exact_parameters, 3, sigma=1, sqrt_minus_q=root
        )) == 4

    with pytest.raises(ValueError, match="inconsistent with q"):
        asymptotic_coefficients(1, 2, 3, 7, 3, sigma=1, sqrt_minus_q=123)

    complex_root = 1.25 - 0.75j
    complex_q = -(complex_root ** 2)
    asymptotic_coefficients(
        1, 2, 3, complex_q, 3, sigma=1, sqrt_minus_q=complex_root
    )
    asymptotic_coefficients(
        1, 2, 3, -4.0, 3, sigma=1,
        sqrt_minus_q=2.0 * (1.0 + 4e-13),
    )
    with pytest.raises(ValueError, match="inconsistent with q"):
        asymptotic_coefficients(
            1, 2, 3, -4.0, 3, sigma=1,
            sqrt_minus_q=2.0 * (1.0 + 2e-12),
        )
    with pytest.raises(ValueError):
        asymptotic_coefficients(1, 2, 3, 0, 3, sigma=1, sqrt_minus_q=0)


def _apply_undriven_operator(polynomial, V, hbar_omega, energy):
    """Apply the differential operator to an exact coefficient dictionary."""

    first = {
        power - 1: power * coefficient
        for power, coefficient in polynomial.items() if power >= 1
    }
    second = {
        power - 1: power * coefficient
        for power, coefficient in first.items() if power >= 1
    }
    result = {}
    for power, coefficient in second.items():
        result[power + 2] = result.get(power + 2, 0) + V * coefficient / 2
    for power, coefficient in first.items():
        result[power + 1] = result.get(power + 1, 0) + hbar_omega * coefficient
    for power, coefficient in polynomial.items():
        result[power] = result.get(power, 0) - energy * coefficient
    return {power: value for power, value in result.items() if value != 0}


@pytest.mark.parametrize("n", [0, 1, 2, 3, 5, 8])
def test_undriven_bargmann_operator_annihilates_eigenmonomials(n):
    V = Fraction(5, 2)
    hbar_omega = Fraction(-1, 3)
    energy = V * n * (n - 1) / 2 + hbar_omega * n
    assert _apply_undriven_operator(
        {n: Fraction(1)}, V, hbar_omega, energy
    ) == {}
