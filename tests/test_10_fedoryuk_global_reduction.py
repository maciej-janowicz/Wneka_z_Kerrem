import importlib.util
from pathlib import Path

import sympy as sp


def _module():
    path = Path(__file__).parents[1] / "scripts" / "10_verify_fedoryuk_global_reduction.py"
    spec = importlib.util.spec_from_file_location("fedoryuk_global", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_two_exact_weber_relations_numerically():
    result = _module().numerical_verify()
    assert result["max_functional_residual"] < result["tolerance"]


def test_wronskians_inverse_and_natural_determinant():
    data = _module().symbolic_verify()
    assert data["determinant"] == -1
    assert sp.simplify(data["wronskian_A"] / data["wronskian_B"] + 1) == 0
    assert data["inverse_product_verified"]


def test_model_zero_is_simple_but_not_a_generic_global_zero():
    module = _module()
    numeric = module.numerical_verify()
    assert all(abs(value) > 1 for value in numeric["simple_zero_slopes"].values())
    data = module.symbolic_verify()
    # l=(1,0), r=(1,0) is the explicit counterexample: scalar=M_11.
    names = {s.name: s for s in data["global_scalar_at_c_zero"].free_symbols}
    value = data["global_scalar_at_c_zero"].subs(
        {names["l1"]: 1, names["l2"]: 0, names["r1"]: 1, names["r2"]: 0})
    assert sp.simplify(value) != 0
