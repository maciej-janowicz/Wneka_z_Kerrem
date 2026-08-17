import importlib.util
from pathlib import Path

import sympy as sp


def _module():
    path = (
        Path(__file__).parents[1]
        / "scripts"
        / "08e_verify_eta_minus_two_thirds.py"
    )
    spec = importlib.util.spec_from_file_location("eta_minus_two_thirds", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


MODULE = _module()
RESULT = MODULE.verify()


def test_symbol_assumptions_and_odd_parity():
    module = MODULE
    assert module.n.is_integer and module.n.is_nonnegative
    assert module.delta.is_real
    assert module.delta.is_nonnegative is None
    assert module.lam.is_positive
    assert module.epsilon.is_positive
    result = RESULT
    assert result["kappa"][1] == 0
    assert result["kappa"][3] == 0


def test_recursive_and_explicit_fourth_order_agree_symbolically():
    result = RESULT
    assert sp.simplify(result["kappa"][2] - result["kappa2_explicit"]) == 0
    assert sp.simplify(result["kappa"][4] - result["kappa4_explicit"]) == 0


def test_eta_coefficient_and_finite_differences():
    module = MODULE
    result = RESULT
    K = result["K_factorized"]
    assert sp.simplify(
        K - sp.expand(result["energy_eta"].removeO()).coeff(module.epsilon, 2)
    ) == 0
    assert sp.simplify(
        result["spacing_K"] - (K.subs(module.n, module.n + 1) - K)
    ) == 0
    assert sp.simplify(
        result["second_difference_K"]
        - (K.subs(module.n, module.n + 2)
           - 2 * K.subs(module.n, module.n + 1) + K)
    ) == 0


def test_low_levels_and_forbidden_negative_states():
    module = MODULE
    result = RESULT
    for level in range(5):
        recursive = sp.simplify(result["kappa"][4].subs(module.n, level))
        explicit = sp.simplify(
            result["kappa4_explicit"].subs(module.n, level)
        )
        assert recursive == explicit
        # Every coefficient leading from |level> to a negative occupation
        # contains a vanishing annihilation factor.
        for order in range(1, 5):
            for bra_shift in range(-12, -level):
                element = sp.sympify(
                    module.matrix_element(order, bra_shift, 0)
                )
                assert sp.simplify(element.subs(module.n, level)) == 0


def test_08d_constant_is_unchanged():
    module = MODULE
    result = RESULT
    constant = (
        module.delta * (1 - 2 * module.delta) / 6
        - (6 * module.n**2 + 6 * module.n + 1) / 72
    )
    assert sp.simplify(
        sp.expand(result["energy_eta"].removeO()).coeff(module.epsilon, 0)
        - constant
    ) == 0
