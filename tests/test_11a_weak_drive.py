import importlib.util
from pathlib import Path

import sympy as sp


def module():
    path = Path(__file__).parents[1] / "scripts" / "11a_verify_weak_drive.py"
    spec = importlib.util.spec_from_file_location("weak_drive", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_energy_and_bargmann_residual_through_fourth_order():
    mod = module()
    d = sp.symbols("d")
    for N in range(5):
        energy, _ = mod.rs_series(N, d, 4)
        assert sp.simplify(energy[4] - mod.energy4_formula(N, d)) == 0
        assert mod.bargmann_residual(N, d, 4)[0] == 0


def test_parity_support_and_second_order_sign():
    mod = module()
    d = sp.symbols("d", positive=True)
    for N in range(5):
        energy, coeff = mod.rs_series(N, d, 4)
        assert energy[1] == energy[3] == 0
        assert sp.simplify(energy[2] - (1-d)/((N-1+d)*(N+d))) == 0
        for k in range(5):
            for n in range(max(0, N-k), N+k+1):
                if (n-N-k) % 2:
                    assert coeff.get((k, n), 0) == 0


def test_extreme_resummation_is_hypergeometric():
    assert module().numerical_check() < sp.Float("1e-45")
