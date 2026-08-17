import importlib.util
from pathlib import Path

import sympy as sp


def _module():
    path = Path(__file__).parents[1] / "scripts" / "08d_verify_higher_energy.py"
    spec = importlib.util.spec_from_file_location("higher_energy", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_exact_cubic_and_quartic_polynomials():
    result = _module().corrections()
    n = sp.symbols("n", integer=True, nonnegative=True)
    delta = sp.symbols("delta", real=True)
    expected = delta * (1 - 2 * delta) / 6 - (6*n**2 + 6*n + 1) / 72
    assert sp.simplify(result["energy_constant"] - expected) == 0
    assert result["o3_shifts"] == (-3, -1, 1, 3)
    assert result["o4_shifts"] == (-4, -2, 0, 2, 4)


def test_spacing_and_anharmonicity():
    result = _module().corrections()
    n = sp.symbols("n", integer=True, nonnegative=True)
    assert sp.simplify(result["spacing_constant"] + (n + 1) / 6) == 0
    assert result["anharmonicity_constant"] == -sp.Rational(1, 6)
