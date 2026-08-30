import importlib.util
from pathlib import Path


def module():
    path = Path(__file__).parents[1] / "scripts" / "12a_1_bright_k2_wkb_gallery.py"
    spec = importlib.util.spec_from_file_location("gallery12a1", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_case_metadata_eta_filename_and_exact_k2():
    mod = module(); base = mod.stage12a()
    thresholds = {"eps_den": 1e-8, "exp_clip": 80.0, "z_cap": 1e6}
    for eta in (5.0, 0.2):
        record, colours, *_ = mod.evaluate_case(
            base, eta, "I", (-2, 1, -1, 1), 19, thresholds)
        assert record["eta"] == eta and record["k"] == 2
        assert len(record["applications"]) == 2
        assert set(colours) == set(mod.STYLES)
        tag = mod.case_tag(eta, 0.7, 0, "I", "test")
        assert f"eta{mod.slug(eta)}" in tag and "k2" in tag
        if eta == 0.2:
            assert "EXTRAPOLATION" in record["regime"]


def test_small_end_to_end_contact_sheet(tmp_path):
    mod = module()
    args = mod.parser().parse_args([
        "--preview-resolution", "13", "--high-resolution", "17",
        "--dpi", "50", "--output-dir", str(tmp_path)])
    payload, files = mod.run_gallery(args)
    assert payload["scope"] == "k=2 only"
    assert len(payload["scan_records"]) == 16
    assert all(len(record["applications"]) == 2 for record in payload["scan_records"])
    assert len(payload["shortlist"]) == 6
    assert all(item["k"] == 2 for item in payload["shortlist"])
    assert len(list(tmp_path.glob("style_contact_*.png"))) == 4
    assert (tmp_path / "shortlist_contact_sheet_k2.png").exists()
    assert (tmp_path / "shortlist_contact_sheet_k2.pdf").exists()
    assert (tmp_path / "bright_k2_gallery_data.json").exists()
    assert all(path.exists() for path in files)
