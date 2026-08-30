import importlib.util
from pathlib import Path

import numpy as np
from PIL import Image


def module():
    path = Path(__file__).parents[1] / "scripts" / "12a_iterated_wkb_portraits.py"
    spec = importlib.util.spec_from_file_location("iterated_wkb_12a", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_vectorized_matches_scalar_at_ordinary_points():
    mod = module()
    points = np.array([0.7+0.2j, -1.4+0.8j, 2.1-0.6j])
    for branch in ("R", "I"):
        vector, _ = mod.wkb_map(points, eta=5.0, delta=0.6, n=2,
                                branch=branch, eps_den=1e-9, exp_clip=100)
        scalar = np.array([mod.wkb_map(z, eta=5.0, delta=0.6, n=2,
                                      branch=branch, eps_den=1e-9,
                                      exp_clip=100)[0] for z in points])
        np.testing.assert_allclose(vector, scalar, rtol=2e-14, atol=2e-14)


def test_exact_iteration_counts_have_no_off_by_one():
    mod = module()
    initial = np.array([[0.8+0.3j]])
    outputs, _, _ = mod.iterate_map(initial, (2, 3, 4), eta=2.0, delta=0.4,
                                    n=0, branch="I", eps_den=1e-10,
                                    exp_clip=100, z_cap=1e100)
    current = initial
    direct = {}
    for k in range(1, 5):
        current = mod.wkb_map(current, eta=2.0, delta=0.4, n=0, branch="I",
                              eps_den=1e-10, exp_clip=100)[0]
        current = mod.regularize_after_map(current, np.zeros(current.shape, bool), 1e100)[0]
        direct[k] = current.copy()
    assert set(outputs) == {2, 3, 4}
    for k in outputs:
        np.testing.assert_allclose(outputs[k], direct[k])


def test_denominator_floor_preserves_phase_including_zero():
    mod = module()
    values = np.array([0j, 1e-12j, -1e-12+0j, 2+3j])
    floored, mask = mod.floor_complex_denominator(values, 1e-6)
    np.testing.assert_allclose(floored[:3], [1e-6, 1e-6j, -1e-6+0j], atol=1e-20)
    assert mask.tolist() == [True, True, True, False]
    assert floored[3] == values[3]


def test_exponent_clips_real_part_only():
    mod = module()
    values = np.array([100+2j, -90-3j, 4+7j])
    clipped, mask = mod.clip_complex_exponent(values, 20)
    np.testing.assert_array_equal(clipped.imag, values.imag)
    np.testing.assert_array_equal(clipped.real, [20, -20, 4])
    assert mask.tolist() == [True, True, False]


def test_radial_cap_preserves_phase():
    mod = module()
    values = np.array([3+4j, -6j, 0.5+0.5j])
    capped, mask = mod.cap_complex_modulus(values, 2.0)
    np.testing.assert_allclose(np.abs(capped[:2]), 2.0)
    np.testing.assert_allclose(np.angle(capped[:2]), np.angle(values[:2]))
    assert mask.tolist() == [True, True, False]


def test_invalid_mask_propagates():
    mod = module()
    previous = np.array([True, False, False])
    values = np.array([1+1j, np.inf+0j, 2+0j])
    _, invalid, new_nonfinite, _ = mod.regularize_after_map(values, previous, 10)
    assert invalid.tolist() == [True, True, False]
    assert new_nonfinite.tolist() == [False, True, False]


def test_deterministic_uint8_rgb_dimensions():
    mod = module()
    values = np.arange(24).reshape(4, 6).astype(complex) + 0.2j
    rgb1 = mod.domain_coloring(values, np.zeros((4, 6), bool), (0, 4))
    rgb2 = mod.domain_coloring(values, np.zeros((4, 6), bool), (0, 4))
    assert rgb1.shape == (4, 6, 3) and rgb1.dtype == np.uint8
    np.testing.assert_array_equal(rgb1, rgb2)


def test_all_bright_styles_are_deterministic_bounded_and_reserve_black():
    mod = module()
    values = (np.arange(30).reshape(5, 6) + 0.25j).astype(complex)
    invalid = np.zeros(values.shape, bool); invalid[1, 2] = True
    for style in mod.COLOUR_STYLES[1:]:
        rgb1 = mod.domain_coloring(values, invalid, (0, 4), style=style)
        rgb2 = mod.domain_coloring(values, invalid, (0, 4), style=style)
        np.testing.assert_array_equal(rgb1, rgb2)
        assert np.all(rgb1[invalid] == 0)
        assert not np.any(np.all(rgb1[~invalid] == 0, axis=-1))
        assert not np.any(np.all(rgb1[~invalid] >= 254, axis=-1))
        brightness = rgb1[~invalid].max(axis=-1) / 255.0
        assert brightness.min() >= 0.50 - 1/255
        assert brightness.max() <= 0.98 + 1/255


def test_equalization_constant_and_nonconstant_and_smooth_bands():
    mod = module()
    valid = np.ones((2, 3), bool)
    constant = mod.empirical_cdf(np.ones((2, 3)), valid)
    np.testing.assert_array_equal(constant, 0.5)
    varied = mod.empirical_cdf(np.array([[3, 1, 2], [6, 5, 4.]]), valid)
    assert np.all(np.isfinite(varied)) and np.ptp(varied) > 0
    values = np.exp(np.linspace(0, 3, 1000)) - 1
    bands = mod.brightness_field(values, np.zeros(1000, bool), (0, 3),
                                 style="bright-banded-modulus")
    assert bands.min() >= 0.50 and bands.max() <= 0.98
    assert np.max(np.abs(np.diff(bands))) < 0.02


def test_small_smoke_run_produces_all_outputs(tmp_path):
    mod = module()
    args = mod.parser().parse_args(["--width", "31", "--height", "23",
                                    "--output-dir", str(tmp_path), "--dpi", "60"])
    paths, *_ = mod.make_outputs(args)
    assert len(paths) == 6
    assert all(path.exists() and path.stat().st_size > 0 for path in paths)
    individual = sorted(tmp_path.glob("iterated_wkb_k*.png"))
    assert len(individual) == 3
    for path in individual:
        image = np.asarray(Image.open(path))
        assert image.shape == (23, 31, 3) and image.dtype == np.uint8
    assert len(list(tmp_path.glob("iterated_wkb_comparison_*.png"))) == 1
    assert len(list(tmp_path.glob("iterated_wkb_comparison_*.pdf"))) == 1
