"""Exact-algebra audits for the formal Liouville--Green expansion."""

from __future__ import annotations

from typing import TypeVar

Scalar = TypeVar("Scalar")


def normal_form_coefficients(
    B1: Scalar, B2: Scalar, B3: Scalar, q: Scalar
) -> dict[int, Scalar]:
    """Return coefficients ``r_k`` in ``R(z) = sum r_k z**(-k)``."""

    return {
        1: q,
        2: B3 + B2 / 2 - B2 * B2 / 4,
        3: B1 * (1 - B2 / 2),
        4: -(B1 * B1) / 4,
    }


def normal_form_coefficient(
    z: Scalar, B1: Scalar, B2: Scalar, B3: Scalar, q: Scalar
) -> Scalar:
    """Evaluate the exact coefficient in ``Phi'' + R(z) Phi = 0``."""

    if z == 0:
        raise ValueError("the normal-form coefficient is singular at z = 0")
    return sum(value / z**power for power, value in normal_form_coefficients(B1, B2, B3, q).items())


def wkb_momentum_coefficients(
    B1: Scalar,
    B2: Scalar,
    B3: Scalar,
    q: Scalar,
    sqrt_minus_q: Scalar,
) -> tuple[Scalar, ...]:
    """Return ``c_0,...,c_3`` in ``p=s*z^-1/2 sum c_j z^-j``.

    The caller supplies ``s=sqrt(-q)``; the result is the formal square root
    ``p=sqrt(-R)`` with leading coefficient ``s``.
    """

    if q == 0 or sqrt_minus_q == 0:
        raise ValueError("the ramified WKB expansion requires q and sqrt_minus_q nonzero")
    if sqrt_minus_q * sqrt_minus_q != -q:
        raise ValueError("sqrt_minus_q must satisfy sqrt_minus_q**2 == -q")
    D = B3 + B2 / 2 - B2 * B2 / 4
    H = B1 * (1 - B2 / 2)
    return (
        1,
        D / (2 * q),
        H / (2 * q) - D * D / (8 * q * q),
        -B1 * B1 / (8 * q) - D * H / (4 * q * q) + D**3 / (16 * q**3),
    )


def integrated_phase_coefficients(
    B1: Scalar,
    B2: Scalar,
    B3: Scalar,
    q: Scalar,
    *,
    sigma: int,
    sqrt_minus_q: Scalar,
) -> dict[str, Scalar]:
    """Return the rate and first inverse-root term of ``sigma*integral p``."""

    if sigma not in (-1, 1):
        raise ValueError("sigma must be +1 or -1")
    wkb_momentum_coefficients(B1, B2, B3, q, sqrt_minus_q)
    D = B3 + B2 / 2 - B2 * B2 / 4
    return {"sqrt_z": 2 * sigma * sqrt_minus_q, "inverse_sqrt_z": sigma * D / sqrt_minus_q}


def prefactor_coefficients(
    B1: Scalar,
    B2: Scalar,
    B3: Scalar,
    q: Scalar,
    sqrt_minus_q: Scalar,
) -> dict[str, Scalar]:
    """Return the power and first integer correction of ``p**(-1/2)``."""

    coefficients = wkb_momentum_coefficients(B1, B2, B3, q, sqrt_minus_q)
    zero = B2 * 0
    return {"power": (zero + 1) / (zero + 4), "inverse_z": -coefficients[1] / 2}


def first_transport_correction(
    q: Scalar, *, sigma: int, sqrt_minus_q: Scalar
) -> Scalar:
    """Coefficient of ``z^-1/2`` from the first Riccati transport term."""

    if sigma not in (-1, 1):
        raise ValueError("sigma must be +1 or -1")
    if q == 0 or sqrt_minus_q == 0 or sqrt_minus_q * sqrt_minus_q != -q:
        raise ValueError("a nonzero consistent square root of -q is required")
    return -3 * sigma / (16 * sqrt_minus_q)


def first_inverse_root_coefficients(
    B2: Scalar,
    B3: Scalar,
    q: Scalar,
    *,
    sigma: int,
    sqrt_minus_q: Scalar,
) -> dict[str, Scalar]:
    """Compare Stage 05, leading WKB, and first-transport ``u_1``."""

    if sigma not in (-1, 1):
        raise ValueError("sigma must be +1 or -1")
    if q == 0 or sqrt_minus_q == 0 or sqrt_minus_q * sqrt_minus_q != -q:
        raise ValueError("a nonzero consistent square root of -q is required")
    D = B3 + B2 / 2 - B2 * B2 / 4
    leading = sigma * D / sqrt_minus_q
    correction = first_transport_correction(q, sigma=sigma, sqrt_minus_q=sqrt_minus_q)
    C = 4 * D - (B2 * 0 + 3) / 4
    return {"stage05": C / (4 * sigma * sqrt_minus_q), "leading_wkb": leading, "transport": correction, "corrected_wkb": leading + correction}
