import importlib.util
from pathlib import Path

import sympy as sp


def test_exact_strong_drive_symbolics():
    path = Path(__file__).parents[1] / "scripts" / "08a_verify_strong_drive.py"
    spec = importlib.util.spec_from_file_location("strong_drive_verifier", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    result = module.verify()
    assert str(result["factorization"]) == "-(y + 1)**2*(2*y - 1)"
    assert str(result["double_root_equation"]) == "y**3 + 1"
    assert sp.simplify(
        result["pair_v_squared"] - sp.Rational(2, 3) * (sp.Symbol("delta", nonzero=True) - 1 - sp.Symbol("e1", nonzero=True))
    ) == 0
    assert "a_u**2*u/2 - 1/2" == str(result["weber_index"])


def test_shifted_hamiltonian_exact_normal_ordered_coefficients():
    path = Path(__file__).parents[1] / "scripts" / "08a_verify_strong_drive.py"
    spec = importlib.util.spec_from_file_location("strong_drive_operator", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    r, delta, eta = sp.symbols("r delta eta")
    c = module.shifted_hamiltonian_coefficients(r, delta, eta)
    stationary = {eta: r**3 + delta * r}
    assert sp.simplify(c[(1, 0)].subs(stationary)) == 0
    assert sp.simplify(c[(0, 1)].subs(stationary)) == 0
    assert c[(1, 1)] == 2 * r**2 + delta
    assert c[(2, 0)] == c[(0, 2)] == r**2 / 2
    assert c[(2, 1)] == c[(1, 2)] == -r
    assert c[(2, 2)] == sp.Rational(1, 2)
