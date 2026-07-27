from fractions import Fraction

import pytest

from kerr_heun.liouville_green import (
    first_inverse_root_coefficients,
    integrated_phase_coefficients,
    normal_form_coefficient,
    normal_form_coefficients,
    prefactor_coefficients,
    wkb_momentum_coefficients,
)
from kerr_heun.local_series import asymptotic_coefficients


@pytest.mark.parametrize("parameters", [
    tuple(map(Fraction, (2, 3, -1, -4, 2))),
    tuple(map(Fraction, (-3, -2, 5, -9, -3))),
])
def test_liouville_transformation_and_normal_form(parameters):
    B1, B2, B3, q, _ = parameters
    coefficients = normal_form_coefficients(B1, B2, B3, q)
    # Q-P'/2-P^2/4, collected independently.
    assert coefficients == {
        1: q,
        2: B3 + B2 / 2 - B2**2 / 4,
        3: B1 - B1 * B2 / 2,
        4: -B1**2 / 4,
    }
    z = Fraction(7)
    assert normal_form_coefficient(z, B1, B2, B3, q) == sum(
        value / z**power for power, value in coefficients.items()
    )


@pytest.mark.parametrize("sigma", [-1, 1])
@pytest.mark.parametrize("raw", [(2, 3, -1, -4, 2), (-3, -2, 5, -9, -3)])
def test_momentum_square_reconstructs_normal_form_and_stage05(sigma, raw):
    B1, B2, B3, q, root = map(Fraction, raw)
    c0, c1, c2, c3 = wkb_momentum_coefficients(B1, B2, B3, q, root)
    assert c0 == 1
    # Coefficients through z^-3 in (sum c_j z^-j)^2.
    square = [c0**2, 2*c1, c1**2 + 2*c2, 2*c3 + 2*c1*c2]
    R = normal_form_coefficients(B1, B2, B3, q)
    expected = [1, R[2]/q, R[3]/q, R[4]/q]
    assert square == expected

    phase = integrated_phase_coefficients(B1, B2, B3, q, sigma=sigma, sqrt_minus_q=root)
    assert phase["sqrt_z"] == 2 * sigma * root
    assert prefactor_coefficients(B1, B2, B3, q, root)["power"] == Fraction(1, 4)

    comparison = first_inverse_root_coefficients(B2, B3, q, sigma=sigma, sqrt_minus_q=root)
    direct = asymptotic_coefficients(B1, B2, B3, q, 1, sigma=sigma, sqrt_minus_q=root)[1]
    assert comparison["stage05"] == direct
    assert comparison["leading_wkb"] != direct
    assert comparison["corrected_wkb"] == direct


def test_branches_and_degenerate_inputs_are_explicit():
    positive = first_inverse_root_coefficients(Fraction(3), Fraction(-1), Fraction(-4), sigma=1, sqrt_minus_q=Fraction(2))
    negative = first_inverse_root_coefficients(Fraction(3), Fraction(-1), Fraction(-4), sigma=-1, sqrt_minus_q=Fraction(2))
    assert all(negative[key] == -positive[key] for key in positive)
    with pytest.raises(ValueError):
        wkb_momentum_coefficients(1, 2, 3, 0, 0)
    with pytest.raises(ValueError):
        wkb_momentum_coefficients(1, 2, 3, -4, 3)
    with pytest.raises(ValueError):
        first_inverse_root_coefficients(2, 3, -4, sigma=0, sqrt_minus_q=2)
    with pytest.raises(ValueError):
        normal_form_coefficient(0, 1, 2, 3, 4)
