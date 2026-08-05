"""Exact audits and error controls for the sectorial infinity solutions."""

from __future__ import annotations

import cmath
from numbers import Real
from typing import TypeVar

from .local_series import _validate_sqrt_minus_q

Scalar = TypeVar("Scalar")


def _three_quarters(reference: Scalar) -> Scalar:
    """Return ``3/4`` without coercing exact numeric inputs to float."""

    one = reference * 0 + 1
    return 3 * one / 4


def covering_normal_form_coefficients(
    B1: Scalar, B2: Scalar, B3: Scalar
) -> dict[int, Scalar]:
    """Return coefficients of ``g(t)=sum g_k/t**k`` after ``z=t**2``."""

    D = B3 + B2 / 2 - B2 * B2 / 4
    H = B1 * (1 - B2 / 2)
    C = 4 * D - _three_quarters(B2)
    return {2: -C, 4: -4 * H, 6: B1 * B1}


def volterra_kernel(t: Scalar, u: Scalar, a_sigma: Scalar) -> Scalar:
    """Kernel for ``h''+2*a_sigma*h'=g*h`` normalized by ``h(infinity)=1``."""

    if t == 0 or u == 0 or a_sigma == 0:
        raise ValueError("t, u, and a_sigma must be nonzero")
    return (cmath.exp(2 * a_sigma * (u - t)) - 1) / (2 * a_sigma)


def radial_error_majorant(
    radius: Scalar, B1: Scalar, B2: Scalar, B3: Scalar
) -> Scalar:
    """Explicit upper bound for the radial integral of ``abs(g)``."""

    if radius <= 0:
        raise ValueError("radius must be positive")
    D = B3 + B2 / 2 - B2 * B2 / 4
    H = B1 * (1 - B2 / 2)
    C = 4 * D - _three_quarters(B2)
    return (
        abs(C) / radius
        + 4 * abs(H) / (3 * radius**3)
        + abs(B1) ** 2 / (5 * radius**5)
    )


def radial_progressive(
    q: Scalar,
    sqrt_minus_q: Scalar,
    *,
    sigma: int,
    theta: float,
    tolerance: float = 1e-12,
) -> bool:
    """Test ``Re(a_sigma*exp(i*theta)) <= 0`` for the outward radial path."""

    if sigma not in (-1, 1):
        raise ValueError("sigma must be +1 or -1")
    if q == 0 or sqrt_minus_q == 0:
        raise ValueError("q and sqrt_minus_q must be nonzero")
    _validate_sqrt_minus_q(q, sqrt_minus_q)
    if isinstance(theta, bool) or not isinstance(theta, Real):
        raise ValueError("theta must be a real number")
    if tolerance < 0:
        raise ValueError("tolerance must be nonnegative")
    a_sigma = 2 * sigma * sqrt_minus_q
    value = (a_sigma * cmath.exp(1j * theta)).real
    return value <= tolerance * max(1.0, abs(a_sigma))


def first_coefficient(
    B2: Scalar,
    B3: Scalar,
    q: Scalar,
    *,
    sigma: int,
    sqrt_minus_q: Scalar,
) -> Scalar:
    """Return the proved/formal common coefficient ``C/(2*a_sigma)``."""

    if sigma not in (-1, 1):
        raise ValueError("sigma must be +1 or -1")
    if q == 0 or sqrt_minus_q == 0:
        raise ValueError("q and sqrt_minus_q must be nonzero")
    _validate_sqrt_minus_q(q, sqrt_minus_q)
    D = B3 + B2 / 2 - B2 * B2 / 4
    C = 4 * D - _three_quarters(B2)
    return C / (4 * sigma * sqrt_minus_q)


def one_term_residual_coefficients(
    B1: Scalar,
    B2: Scalar,
    B3: Scalar,
    q: Scalar,
    *,
    sigma: int,
    sqrt_minus_q: Scalar,
) -> dict[int, Scalar]:
    """Return coefficients of ``L(1+b/t)`` for ``Lh=h''+2ah'-g h``."""

    b = first_coefficient(
        B2, B3, q, sigma=sigma, sqrt_minus_q=sqrt_minus_q
    )
    D = B3 + B2 / 2 - B2 * B2 / 4
    H = B1 * (1 - B2 / 2)
    C = 4 * D - _three_quarters(B2)
    return {
        3: b * (C + 2),
        4: 4 * H,
        5: 4 * H * b,
        6: -(B1 * B1),
        7: -(B1 * B1) * b,
    }


def radial_one_term_residual_majorant(
    radius: Scalar,
    B1: Scalar,
    B2: Scalar,
    B3: Scalar,
    q: Scalar,
    *,
    sigma: int,
    sqrt_minus_q: Scalar,
) -> Scalar:
    """Bound the radial integral of ``abs(L(1+b/t))`` explicitly."""

    if radius <= 0:
        raise ValueError("radius must be positive")
    coefficients = one_term_residual_coefficients(
        B1, B2, B3, q, sigma=sigma, sqrt_minus_q=sqrt_minus_q
    )
    return sum(
        abs(value) / ((power - 1) * radius ** (power - 1))
        for power, value in coefficients.items()
    )
