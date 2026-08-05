import cmath
from fractions import Fraction

import pytest

from kerr_heun.local_series import asymptotic_coefficients
from kerr_heun.olver import (
    covering_normal_form_coefficients,
    first_coefficient,
    one_term_residual_coefficients,
    radial_error_majorant,
    radial_one_term_residual_majorant,
    radial_progressive,
    volterra_kernel,
)


@pytest.mark.parametrize("raw", [(2, 3, -1), (-3, -2, 5)])
def test_exact_covering_transformation(raw):
    B1, B2, B3 = map(Fraction, raw)
    # Independently collect A''/A + P A'/A + Q after Y=A w.  Laurent
    # dictionaries map a power of t to its exact coefficient.
    p = Fraction(1, 2) - B2
    logarithmic_derivative = {-1: p, -3: -B1}
    derivative = {-2: -p, -4: 3 * B1}

    def multiply(left, right):
        result = {}
        for left_power, left_value in left.items():
            for right_power, right_value in right.items():
                power = left_power + right_power
                result[power] = result.get(power, 0) + left_value * right_value
        return {power: value for power, value in result.items() if value}

    def add(*terms):
        result = {}
        for term in terms:
            for power, value in term.items():
                result[power] = result.get(power, 0) + value
        return {power: value for power, value in result.items() if value}

    # Divide the exact Y equation by t^2: Y''+P Y'+Q Y=0.
    P = {-1: 2 * B2 - 1, -3: 2 * B1}
    Q = {-2: 4 * B3, 0: Fraction(-16)}  # choose q=-4 below
    w_prime = add({power: 2 * value for power, value in logarithmic_derivative.items()}, P)
    potential = add(
        derivative,
        multiply(logarithmic_derivative, logarithmic_derivative),
        multiply(P, logarithmic_derivative),
        Q,
    )
    assert w_prime == {}
    constant = potential.pop(0)
    assert constant == -16
    right_hand_side = {-power: -value for power, value in potential.items()}
    assert right_hand_side == covering_normal_form_coefficients(B1, B2, B3)


@pytest.mark.parametrize("a,t,u", [(-1 + 0.4j, 1.1 + 0.2j, 2.3 + 0.5j), (-2j, 2 - 0.3j, 3.2 - 0.1j)])
def test_volterra_kernel_finite_difference_identity(a, t, u):
    step = 2e-4
    center = volterra_kernel(t, u, a)
    plus = volterra_kernel(t + step, u, a)
    minus = volterra_kernel(t - step, u, a)
    first = (plus - minus) / (2 * step)
    second = (plus - 2 * center + minus) / step**2
    assert abs(volterra_kernel(t, t, a)) < 1e-14
    assert abs(second + 2 * a * first) < 2e-6


def test_differentiated_volterra_equation_includes_endpoint_term():
    # For a fixed upper endpoint and f(u)=1, numerically integrate H(t)=int K du.
    # Centered differences must recover H''+2aH'=f(t); the unit right-hand
    # side is exactly the lower-endpoint contribution -K_t(t,t)f(t).
    a = -1.3
    upper = 6.0

    def integral(t):
        panels = 20000
        width = (upper - t) / panels
        total = 0.5 * (volterra_kernel(t, t, a) + volterra_kernel(t, upper, a))
        total += sum(volterra_kernel(t, t + j * width, a) for j in range(1, panels))
        return width * total

    t = 1.4
    step = 1e-3
    center = integral(t)
    plus = integral(t + step)
    minus = integral(t - step)
    first = (plus - minus) / (2 * step)
    second = (plus - 2 * center + minus) / step**2
    assert abs(second + 2 * a * first - 1) < 3e-5


@pytest.mark.parametrize("sigma", [-1, 1])
@pytest.mark.parametrize("raw", [(2, 3, -1, -4, 2), (-3, -2, 5, -9, -3)])
def test_first_coefficient_matches_stage05_and_residual(sigma, raw):
    B1, B2, B3, q, root = map(Fraction, raw)
    b = first_coefficient(B2, B3, q, sigma=sigma, sqrt_minus_q=root)
    direct = asymptotic_coefficients(
        B1, B2, B3, q, 1, sigma=sigma, sqrt_minus_q=root
    )[1]
    assert b == direct
    residual = one_term_residual_coefficients(
        B1, B2, B3, q, sigma=sigma, sqrt_minus_q=root
    )
    assert min(residual) == 3


def test_explicit_radial_majorants():
    B1, B2, B3 = map(Fraction, (2, 3, -1))
    R = Fraction(5, 2)
    D = B3 + B2 / 2 - B2**2 / 4
    H = B1 * (1 - B2 / 2)
    C = 4 * D - Fraction(3, 4)
    expected = abs(C) / R + 4 * abs(H) / (3 * R**3) + abs(B1)**2 / (5 * R**5)
    assert radial_error_majorant(R, B1, B2, B3) == expected
    residual = one_term_residual_coefficients(
        B1, B2, B3, Fraction(-4), sigma=1, sqrt_minus_q=Fraction(2)
    )
    assert radial_one_term_residual_majorant(
        R, B1, B2, B3, Fraction(-4), sigma=1, sqrt_minus_q=Fraction(2)
    ) == sum(abs(v) / ((k - 1) * R ** (k - 1)) for k, v in residual.items())


def test_validation_and_progressive_sectors():
    assert radial_progressive(-4, 2, sigma=1, theta=cmath.pi)
    assert radial_progressive(-4, 2, sigma=-1, theta=0)
    assert radial_progressive(-4, 2, sigma=1, theta=cmath.pi / 2)
    assert not radial_progressive(-4, 2, sigma=1, theta=0)
    with pytest.raises(ValueError):
        radial_error_majorant(0, 1, 2, 3)
    with pytest.raises(ValueError):
        radial_progressive(0, 0, sigma=1, theta=0)
    with pytest.raises(ValueError):
        radial_progressive(-4, 3, sigma=1, theta=0)
    with pytest.raises(ValueError):
        radial_progressive(-4, 2, sigma=0, theta=0)
    with pytest.raises(ValueError):
        volterra_kernel(1, 2, 0)
    with pytest.raises(ValueError):
        volterra_kernel(0, 2, 1)
    with pytest.raises(ValueError):
        radial_progressive(-4, 2, sigma=1, theta=1j)
