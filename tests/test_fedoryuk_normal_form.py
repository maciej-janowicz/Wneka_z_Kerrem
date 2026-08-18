import importlib.util
from pathlib import Path

import sympy as sp


def _result():
    path = Path(__file__).parents[1] / "scripts" / "09a_verify_fedoryuk_normal_form.py"
    spec = importlib.util.spec_from_file_location("fedoryuk_verifier", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.verify()


def _geometry_module():
    path = Path(__file__).parents[1] / "scripts" / "09a_fedoryuk_stokes_geometry.py"
    spec = importlib.util.spec_from_file_location("fedoryuk_geometry", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_direct_normal_form_and_small_parameter():
    result = _result()
    eta = sp.symbols("eta", positive=True)
    assert result["epsilon"] == eta ** -sp.Rational(2, 3)
    assert sp.simplify(result["Q0"] - result["P"] / sp.Symbol("y", nonzero=True)**4) == 0


def test_turning_point_discriminant_and_local_balance():
    result = _result()
    e = sp.symbols("e", positive=True)
    assert sp.expand(result["discriminant"] + 4 * (8 * e**3 + 27)) == 0
    symbols = {symbol.name: symbol for symbol in result["local_P"].free_symbols}
    X, e1, eps = symbols["X"], symbols["e1"], symbols["eps"]
    expected = eps * (3 * X**2 + 2 * e1) + eps**sp.Rational(3, 2) * (
        -2 * X**3 - 4 * X * e1
    )
    assert sp.expand(result["local_P"] - expected) == 0


def test_exact_coefficient_terminates_at_epsilon_squared():
    result = _result()
    y = sp.Symbol("y", nonzero=True)
    delta = sp.symbols("delta", positive=True)
    assert result["Q1"] == 2 * (delta - 1) / y**3
    assert sp.simplify(result["Q2"] - delta * (delta - 1) / y**2) == 0


def _angle_sets_close(left, right, tolerance=1e-12):
    left = sorted(float(value % (2 * sp.pi)) for value in left)
    right = sorted(float(value % (2 * sp.pi)) for value in right)
    return len(left) == len(right) and all(
        abs(a - b) < tolerance for a, b in zip(left, right)
    )


def test_general_direction_formulas_and_branch_invariance():
    module = _geometry_module()
    for multiplicity in (1, 2):
        for family in ("stokes", "anti"):
            positive = module.local_directions(multiplicity, 3 + 4j, family, 1)
            negative = module.local_directions(multiplicity, 3 + 4j, family, -1)
            assert len(positive) == multiplicity + 2
            assert _angle_sets_close(positive, negative)


def test_exact_double_root_coefficient_and_directions():
    module = _geometry_module()
    points = module.turning_points(-1.5)
    double = next(point for point in points if point.multiplicity == 2)
    assert double.root == -1
    assert double.coefficient == 3
    stokes = module.local_directions(2, double.coefficient, "stokes")
    anti = module.local_directions(2, double.coefficient, "anti")
    assert _angle_sets_close(stokes, [sp.pi/4, 3*sp.pi/4, 5*sp.pi/4, 7*sp.pi/4])
    assert _angle_sets_close(anti, [0, sp.pi/2, sp.pi, 3*sp.pi/2])


def test_every_simple_root_has_three_plus_three_rays():
    module = _geometry_module()
    for energy in (-1.45, -1.5):
        for point in module.turning_points(energy):
            if point.multiplicity == 1:
                assert len(module.local_directions(1, point.coefficient, "stokes")) == 3
                assert len(module.local_directions(1, point.coefficient, "anti")) == 3
    remaining = next(point for point in module.turning_points(-1.5)
                     if point.multiplicity == 1)
    assert remaining.root == 0.5
    assert remaining.coefficient == -72


def test_numerical_constant_phase_validation():
    module = _geometry_module()
    for energy in (-1.45, -1.5):
        _points, trajectories = module.compute_panel(energy)
        validation = module.validate_trajectories(trajectories)
        expected = 18 if energy == -1.45 else 14
        assert validation["trajectory_count"] == expected
        assert validation["max_relative_phase_error"] <= module.PHASE_TOLERANCE
        assert validation["max_local_start_error"] <= module.LOCAL_START_TOLERANCE
