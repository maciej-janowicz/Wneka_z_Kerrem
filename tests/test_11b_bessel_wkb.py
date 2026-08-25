import importlib.util
from pathlib import Path

import mpmath as mp
import sympy as sp


def module():
    path = Path(__file__).parents[1] / "scripts" / "11b_verify_bessel_wkb.py"
    spec = importlib.util.spec_from_file_location("weak11b", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_edge_ode_and_exact_bargmann_residual():
    mod = module()
    assert mod.numerical_edge_ode(dps=70)["max_scaled_residual"] < mp.mpf("1e-65")
    residual = mod.exact_edge_residual()
    names = {s.name for s in residual.free_symbols}
    assert {"lambda", "N", "Delta_e", "z"} <= names


def test_principal_branch_0f1_bessel_identity():
    result = module().numerical_bessel_identity(dps=70)
    assert result["max_relative_error"] < mp.mpf("1e-65")


def test_dominant_bessel_exponent_in_three_sectors():
    result = module().numerical_dominant_asymptotic(dps=70)
    assert max(result["last_radius_errors"]) < mp.mpf("0.04")


def test_first_subdiagonal_recurrence_and_sum_matches_rs():
    mod = module()
    d = sp.symbols("delta")
    for N in range(1, 5):
        assert all(v == 0 for v in mod.verify_subdiagonal_against_rs(N, d, 6).values())


def test_energy_regression_and_order_four_wavefunction():
    mod = module()
    stage11a = mod._stage11a()
    d = sp.symbols("delta")
    for N in range(5):
        energy, _ = stage11a.rs_series(N, d, 4)
        assert sp.simplify(energy[4]-stage11a.energy4_formula(N, d)) == 0
        assert stage11a.bargmann_residual(N, d, 4)[0] == 0
