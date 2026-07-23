"""Exact-recurrence generators for local Whittaker--Ince expansions."""

from __future__ import annotations

from numbers import Integral, Number, Rational
from typing import TypeVar

Scalar = TypeVar("Scalar")
_SQRT_RELATIVE_TOLERANCE = 1e-12


def _validate_order(order: int) -> None:
    if isinstance(order, bool) or not isinstance(order, Integral) or order < 0:
        raise ValueError("order must be a nonnegative integer")


def _decidable_equality(value: object, target: object) -> bool | None:
    """Return a decided equality, or ``None`` for an undecidable symbolic one."""

    try:
        comparison = value == target
        if comparison is True or comparison is False:
            return comparison
        if comparison.__class__.__name__ in ("BooleanTrue", "BooleanFalse"):
            return bool(comparison)
    except (TypeError, ValueError):
        pass

    equals = getattr(value, "equals", None)
    if callable(equals):
        decision = equals(target)
        if decision is True or decision is False:
            return decision
    return None


def _validate_sqrt_minus_q(q: Scalar, sqrt_minus_q: Scalar) -> None:
    """Check ``sqrt_minus_q**2 == -q`` whenever the scalar type can decide it."""

    squared = sqrt_minus_q * sqrt_minus_q
    residual = squared + q
    if isinstance(q, Rational) and isinstance(sqrt_minus_q, Rational):
        valid = residual == 0
    elif isinstance(q, Number) and isinstance(sqrt_minus_q, Number):
        scale = max(1, abs(squared), abs(q))
        valid = abs(residual) <= _SQRT_RELATIVE_TOLERANCE * scale
    else:
        valid = _decidable_equality(residual, 0)

    if valid is False:
        raise ValueError(
            "sqrt_minus_q is inconsistent with q: expected "
            "sqrt_minus_q**2 + q == 0"
        )


def taylor_coefficients(
    B1: Scalar,
    B2: Scalar,
    B3: Scalar,
    q: Scalar,
    order: int,
) -> list[Scalar]:
    """Return ``[c_0, ..., c_order]`` for the normalized formal Taylor series.

    Arithmetic is inherited from the supplied scalar objects.  Consequently,
    fractions, symbolic objects, complex numbers, and arbitrary-precision
    numerical types can be used without conversion to machine precision.
    """

    _validate_order(order)
    if B1 == 0:
        raise ValueError("the normalized forward recurrence requires B1 != 0")

    coefficients = [B1 * 0 + 1]
    previous = B1 * 0
    for n in range(order):
        current = coefficients[n]
        diagonal = n * (n - 1) + B2 * n + B3
        following = -(diagonal * current + q * previous) / (B1 * (n + 1))
        coefficients.append(following)
        previous = current
    return coefficients


def asymptotic_coefficients(
    B1: Scalar,
    B2: Scalar,
    B3: Scalar,
    q: Scalar,
    order: int,
    *,
    sigma: int,
    sqrt_minus_q: Scalar,
) -> list[Scalar]:
    """Return ``[u_0, ..., u_order]`` for one formal infinity branch.

    ``sqrt_minus_q`` is the caller's chosen value of ``sqrt(-q)``.  Supplying
    it explicitly keeps the branch convention visible and permits exact or
    arbitrary-precision arithmetic.  The exponential parameter is
    ``a_sigma = 2*sigma*sqrt_minus_q``. Exact rational values are checked
    exactly, numerical values use a relative tolerance of ``1e-12``, and
    decidable symbolic zero relations are honored. An undecidable symbolic
    relation remains the caller's responsibility.
    """

    _validate_order(order)
    if sigma not in (-1, 1):
        raise ValueError("sigma must be +1 or -1")
    if _decidable_equality(q, 0) is True:
        raise ValueError("the square-root asymptotic expansion requires q != 0")
    if _decidable_equality(sqrt_minus_q, 0) is True:
        raise ValueError("sqrt_minus_q must be a nonzero square root of -q")
    _validate_sqrt_minus_q(q, sqrt_minus_q)

    a_sigma = 2 * sigma * sqrt_minus_q
    zero = B2 * 0
    p = (zero + 1) / (zero + 2) - B2
    characteristic = p * p + (2 * B2 - 2) * p + 4 * B3

    coefficients = [B1 * 0 + 1]
    for m in range(order):
        u_m = coefficients[m]
        u_m1 = coefficients[m - 1] if m >= 1 else B1 * 0
        u_m2 = coefficients[m - 2] if m >= 2 else B1 * 0
        numerator = (
            (m * (m + 1) + characteristic) * u_m
            + 2 * a_sigma * B1 * u_m1
            + 2 * B1 * (p - m + 2) * u_m2
        )
        coefficients.append(numerator / (2 * a_sigma * (m + 1)))
    return coefficients
