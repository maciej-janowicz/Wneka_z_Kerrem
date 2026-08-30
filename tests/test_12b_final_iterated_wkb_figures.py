import importlib.util, json
from pathlib import Path
import numpy as np
from PIL import Image

def module():
    p=Path(__file__).parents[1]/"scripts"/"12b_final_iterated_wkb_figures.py"
    s=importlib.util.spec_from_file_location("stage12b",p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

def test_fixed_cases_depths_names_and_metadata():
    m=module(); assert [(s["eta"],s["k"]) for s in m.SPECS]==[(4.0,2),(4.0,2),(0.25,3),(0.25,3)]
    names=[m.filename(s) for s in m.SPECS]
    assert len(set(names))==4 and all("branch" in x and "domain" in x for x in names)

def test_statistics_have_exact_application_depth():
    m=module(); base=m.core()
    for spec in m.SPECS:
        record,rgb=m.evaluate(base,spec,17)
        assert len(record["applications"])==spec["k"]
        assert [x["application"] for x in record["applications"]]==list(range(1,spec["k"]+1))
        assert rgb.shape==(17,17,3) and rgb.dtype==np.uint8
        assert not np.any(np.all(rgb==255,axis=-1))

def test_small_end_to_end_exactly_four_and_sidecar_png_agreement(tmp_path):
    m=module(); args=m.parser().parse_args(["--output-dir",str(tmp_path),"--preview-resolution","11","--final-resolution","19"])
    payload=m.generate(args); pngs=sorted(tmp_path.glob("final_*.png"))
    assert len(pngs)==4 and [p.name for p in pngs]==sorted(payload["final_png_files"])
    side=json.loads((tmp_path/"final_iterated_wkb_metadata.json").read_text())
    for p in pngs:
        desc=json.loads(Image.open(p).info["Description"]); rec=next(x for x in side["finals"] if x["file"]==p.name)
        assert desc==rec and Image.open(p).size==(19,19)
        arr=np.asarray(Image.open(p)); invalid=rec["applications"][-1]["invalid_total"]
        assert np.count_nonzero(np.all(arr==0,axis=-1))==invalid

def test_manuscript_caption_names_all_final_files_and_extrapolation_warning():
    m=module(); root=Path(__file__).parents[1]
    tex=(root/"manuscript"/"manuscript.tex").read_text()
    for spec in m.SPECS:
        assert m.filename(spec) in tex
    assert "formal extrapolation far outside the controlled strong-drive asymptotic" in tex
    assert "no claim or test of fractality is made" in tex
