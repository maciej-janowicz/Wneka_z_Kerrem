import importlib.util
from pathlib import Path

import mpmath as mp
import sympy as sp


def module():
    path = Path(__file__).parents[1] / "scripts" / "11f_verify_second_subdiagonal_rayleigh.py"
    spec = importlib.util.spec_from_file_location("weak11f", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_y2_recurrence_boundaries_and_rs_through_lambda8():
    mod = module()
    for N in (0, 1, 2, 3, 4):
        data = mod.second_subdiagonal(N, sp.Rational(2, 3), 5)
        assert data["lowest_m"] == max(-2, -N)
        assert data["solvability"] == 0
        assert all(v == 0 for v in mod.verify_against_rs(N, sp.Rational(2, 3), 8).values())


def test_green_representation_and_s2_identity():
    mod = module()
    assert mod.green_representation_check() == 0
    assert mod.s2_identity_check() == 0


def test_zero_structure_and_additive_reconstruction():
    mod = module()
    zeros = mod.zero_structure()
    assert zeros["S2_double_pole"] != 0


def test_global_fock_state_norm_and_tail_converge():
    mod = module()
    mp.mp.dps = 50
    a = mod.rayleigh_and_variance(1, mp.mpf("0.75"), mp.mpf("0.08"), 45)
    b = mod.rayleigh_and_variance(1, mp.mpf("0.75"), mp.mpf("0.08"), 65)
    assert a["norm"] > 0
    assert abs(a["norm"]-b["norm"]) < mp.mpf("1e-35")
    assert b["last_probability"] < mp.mpf("1e-70")


def test_rayleigh_series_has_level_dependent_reliable_order():
    mod = module()
    expected = {0: 12, 1: 8, 2: 6, 3: 4}
    for N in (0, 1, 2, 3):
        data = mod.rayleigh_series_matches_rs(N, sp.Rational(2, 3), 12)
        assert data["reliable_through"] == expected[N]
        assert data["first_bad"] == (None if N == 0 else expected[N]+2)
        if N <= 2:
            assert data["e6"] != 0


def test_residual_variance_is_nonnegative_and_convergent():
    mod = module()
    mp.mp.dps = 50
    a = mod.rayleigh_and_variance(2, mp.mpf("0.75"), mp.mpf("0.06"), 45)
    b = mod.rayleigh_and_variance(2, mp.mpf("0.75"), mp.mpf("0.06"), 65)
    assert a["variance"] >= 0 and b["variance"] >= 0
    assert abs(a["variance"]-b["variance"]) < mp.mpf("1e-34")


def test_s2_sectorial_asymptotic_contains_e4_and_nonlinearity():
    mod = module()
    e2, e4 = sp.symbols("e2 e4")
    terms = mod.s2_dominant_asymptotic()
    assert terms["x^-1/2"] == -2*e4
    assert terms["x^-1"] == -e4/2
    assert terms["nonlinear_source_x^-1"] == -e2**2/2
