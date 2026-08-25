import importlib.util
from pathlib import Path

import sympy as sp


def module():
    path = Path(__file__).parents[1] / "scripts" / "11c_verify_multiplicative_bb.py"
    spec = importlib.util.spec_from_file_location("weak11c", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_exact_dressed_equation_and_independent_z1_equation():
    mod = module()
    assert mod.dressed_equation_check() != 0
    assert mod.z1_equation_check() is not None


def test_z1_is_additive_y1_over_y0_as_a_series():
    mod = module()
    for N in (1, 2, 3):
        for delta in (sp.Rational(2, 3), sp.Rational(5, 4)):
            assert mod.quotient_series_check(N, delta, 6) is not None


def test_regular_n0_b2_and_other_n0_values():
    mod = module()
    stage11b = mod._load("weak11b_test_special", "11b_verify_bessel_wkb.py")
    for delta in (sp.Integer(1), sp.Rational(2, 3), sp.Rational(5, 4)):
        b, _e2, coeff = stage11b.subdiagonal_coefficients(0, delta, 5)
        assert coeff[-1] == 0
        if delta == 1:
            assert b == 2
        assert all(v == 0 for v in
                   stage11b.verify_subdiagonal_against_rs(0, delta, 6).values())


def test_n_positive_formula_and_rs_recurrence():
    mod = module()
    stage11b = mod._load("weak11b_test_positive", "11b_verify_bessel_wkb.py")
    d = sp.symbols("delta")
    for N in (1, 2, 3, 4):
        coeff = stage11b.subdiagonal_coefficients(N, d, 5)[2]
        assert sp.simplify(coeff[-1]+2*N/(N+d-1)) == 0
        stage11b.verify_subdiagonal_against_rs(N, d, 6)


def test_second_level_solvability_is_e4_and_s2_equation_exists():
    mod = module()
    d = sp.symbols("delta")
    for N in (2, 3, 4):
        assert mod.y2_solvability(N, d)["solvability_residual"] == 0
    equations = mod.exponential_equations()
    assert set(equations) == {"S1", "S2"}


def test_dominant_s1_contains_energy_and_gauge_wkb_terms():
    mod = module()
    e2 = sp.symbols("e2")
    terms = mod.dominant_s1_asymptotic()
    assert terms["x^-1/2"] == -2*e2
    # -2/x is exactly log(exp(lambda/z)) because lambda/z=-2lambda^2/x.
    assert sp.simplify(terms["x^-1"] + 2 + e2/2) == 0
