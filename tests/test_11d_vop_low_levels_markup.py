import importlib.util
from pathlib import Path

import sympy as sp


def module():
    path = Path(__file__).parents[1] / "scripts" / "11d_verify_vop_low_levels_markup.py"
    spec = importlib.util.spec_from_file_location("weak11d", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_correct_standard_source_and_full_vop_representation():
    mod = module()
    assert mod.standard_source_check() != 0
    assert mod.variation_of_parameters_check() == 0


def test_additive_multiplicative_equivalence_and_dressed_regression():
    mod = module()
    assert mod.multiplicative_equivalence_check() is not None
    stage11c = mod._load("weak11c_test_11d", "11c_verify_multiplicative_bb.py")
    assert stage11c.dressed_equation_check() != 0
    assert stage11c.dominant_s1_asymptotic()["x^-1"] != 0


def test_second_level_n0_n1_and_general_against_rs_through_lambda6():
    mod = module()
    for N in (0, 1, 2, 3, 4):
        for delta in (sp.Rational(2, 3), sp.Rational(5, 4), sp.Rational(7, 5)):
            data = mod.second_level(N, delta)
            assert all(error == 0 for error in data["rs_errors"].values())
    assert mod.second_level(0, sp.Integer(1))["lowest_m"] == 0


def test_physical_lower_bound_is_imposed_before_recurrence():
    mod = module()
    assert mod.second_level(0, sp.Rational(2, 3))["q"][-2] == 0
    assert mod.second_level(0, sp.Rational(2, 3))["q"][-1] == 0
    assert mod.second_level(1, sp.Rational(2, 3))["q"][-2] == 0
    assert mod.second_level(1, sp.Rational(2, 3))["lowest_m"] == -1
    assert mod.second_level(2, sp.Rational(2, 3))["lowest_m"] == -2


def test_audit_markdown_has_balanced_math_and_no_corrupt_tokens():
    mod = module()
    result = mod.markdown_audit(
        Path(__file__).parents[1] / "docs" / "bender_bettencourt_weak_drive_resummation.md")
    assert result["tabs"] == result["control_characters"] == 0
    assert result["naked_token_hits"] == []
