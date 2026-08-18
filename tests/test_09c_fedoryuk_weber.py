import importlib.util
from pathlib import Path

import sympy as sp


def _module():
    path = Path(__file__).parents[1] / "scripts" / "09c_verify_fedoryuk_weber.py"
    spec = importlib.util.spec_from_file_location("fedoryuk_weber", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_complete_local_expansion_and_parity():
    result = _module().verify()
    X = next(x for x in result["R1"].free_symbols if x.name == "X")
    assert sp.expand(result["R1"].subs(X, -X) + result["R1"]) == 0
    assert sp.expand(result["R2"].subs(X, -X) - result["R2"]) == 0


def test_weber_branches_and_pullback():
    result = _module().verify()
    assert result["coupled_shifts"] == (-3, -1, 1, 3)
    assert str(result["pullback_X"]) == "eta**(1/3) + z"


def test_hermite_reduction_for_integer_indices():
    result = _module().verify()
    symbols = {x.name: x for x in result["hermite_factor"].free_symbols}
    s, n = symbols["s"], symbols["n"]
    for level in range(5):
        factor = result["hermite_factor"].subs(n, level)
        assert sp.simplify(factor - 2**(-sp.Rational(level, 2))
                           * sp.exp(-s**2/2)*sp.hermite(level, s)) == 0


def test_leading_residual_has_predicted_sqrt_epsilon_scaling():
    module = _module()
    for level, detuning, point in ((0, 0.7, 0.4), (1, -0.2, 0.3),
                                   (2, 1.1, -0.35)):
        _values, ratios = module.numerical_residual_ratios(level, detuning, point)
        assert all(1.8 < ratio < 2.2 for ratio in ratios)


def test_rotated_sign_ledger_and_all_matrix_elements():
    data = _module().perturbation_data()
    assert data["differential_I"][0] == sp.I*data["A"]
    assert data["differential_I"][1] == -sp.I*data["B_I"]
    assert data["operator_I"][0] == -sp.I*data["A"]
    assert data["operator_I"][1] == sp.I*data["B_I"]
    assert set(data["matrix_R"]) == {-3, -1, 1, 3}
    assert set(data["matrix_I"]) == {-3, -1, 1, 3}
    # This fails if cubic and linear terms accidentally receive one phase.
    assert sp.simplify(data["matrix_I"][-1]
                       - sp.I*(data["A"]
                       * _module().hermite_matrix_elements(data["n"])["x3"][-1]
                       - data["B_I"]
                       * _module().hermite_matrix_elements(data["n"])["x"][-1])) == 0


def test_both_finite_u1_sums_solve_the_inhomogeneous_equations():
    module = _module()
    for branch in ("R", "I"):
        for level in range(5):
            assert module.exact_order_q_identity(level, branch) == 0


def test_second_order_solvability_and_stage08_check():
    data = _module().perturbation_data()
    expected = (data["delta"]*(1-2*data["delta"])/6
                -(6*data["n"]**2+6*data["n"]+1)/72)
    assert sp.simplify(data["e2_R"]-expected) == 0
    assert sp.simplify(data["e2_I"]-expected) == 0
    assert data["difference_I_stage08"] == 0


def test_corrected_wavefunction_residual_is_quadratic_in_q():
    module = _module()
    for branch in ("R", "I"):
        for level, detuning in ((0, 0.7), (1, -0.2), (2, 1.1)):
            _values, ratios = module.numerical_wavefunction_residuals(
                level, detuning, orientation=branch)
            assert all(3.4 < ratio < 4.7 for ratio in ratios)
