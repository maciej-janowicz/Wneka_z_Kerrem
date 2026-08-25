#!/usr/bin/env python3
"""Stage 11d: VOP, low-level second diagonal, and Markdown checks."""

from __future__ import annotations

import importlib.util
import re
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).parents[1]


def _load(name, filename):
    path = Path(__file__).with_name(filename)
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def standard_source_check():
    x, b, N, e2 = sp.symbols("x b N e2", nonzero=True)
    u = sp.Function("u")(x)
    source = 2*sp.diff(u, x)+2*N*u/x+e2*u
    h = sp.factor(2*source/x**2)
    expected = 4*sp.diff(u, x)/x**2+4*N*u/x**3+2*e2*u/x**2
    assert sp.simplify(h-expected) == 0
    return h


def variation_of_parameters_check():
    """Differentiate the full VOP formula using its defining derivatives."""
    x, b = sp.symbols("x b", nonzero=True)
    u, v, h = (sp.Function(name)(x) for name in ("u", "v", "h"))
    # For A'=-v*h/W and B'=u*h/W, u*A'+v*B'=0.  After the
    # homogeneous terms cancel, differentiating once more leaves this.
    wronskian = u*sp.diff(v, x)-sp.diff(u, x)*v
    residual = h*x**b*wronskian-h
    # W(u,v)=u*v'-u'*v=x^-b.
    residual = sp.factor(residual.subs(wronskian, x**(-b)))
    assert residual == 0
    return residual


def multiplicative_equivalence_check():
    x, b, N, e2 = sp.symbols("x b N e2", nonzero=True)
    u, z = sp.Function("u")(x), sp.Function("Z1")(x)
    r = sp.diff(u, x)/u
    additive = (x**2*sp.diff(u*z, x, 2)/2+b*x*sp.diff(u*z, x)/2
                -x*u*z/2-2*sp.diff(u, x)-2*N*u/x-e2*u)
    edge = {sp.diff(u, x, 2): u/x-b*sp.diff(u, x)/x}
    dressed = (x**2*sp.diff(z, x, 2)/2
               +(x**2*r+b*x/2)*sp.diff(z, x)
               -2*r-2*N/x-e2)
    assert sp.simplify(additive.subs(edge)-u*dressed) == 0
    divergence = sp.diff(x**b*u**2*sp.diff(z, x), x)
    expected = 2*x**(b-2)*u**2*(2*r+2*N/x+e2)
    converted = sp.factor(divergence-2*x**(b-2)*u**2*(
        x**2*sp.diff(z, x, 2)/2+(x**2*r+b*x/2)*sp.diff(z, x)))
    assert converted == 0
    return sp.Eq(divergence, expected)


def second_level(N, delta, max_m=2):
    """Physical Y2 recurrence, imposing the Fock lower boundary first."""
    s11a = _load("weak11a_for_11d", "11a_verify_weak_drive.py")
    s11b = _load("weak11b_for_11d", "11b_verify_bessel_wkb.py")
    b, e2, d = s11b.subdiagonal_coefficients(N, delta, max_m+1)
    a = lambda m: s11b.edge_coeff(m, b)
    q = {-3: sp.Integer(0)}
    lowest_m = max(-2, -N)
    for m in range(-2, lowest_m):
        q[m] = sp.Integer(0)
    for m in range(lowest_m, 0):
        rhs = 2*(m+1+N)*d.get(m+1, 0)+e2*d.get(m, 0)
        q[m] = sp.factor((q.get(m-1, 0)+2*rhs)/(m*(m+b-1)))
    q[0] = sp.Integer(0)
    e4_from_resonance = sp.factor(
        -q.get(-1, 0)/2-2*(N+1)*d[1]-e2*d[0])
    e4_rs = s11a.energy4_formula(N, delta)
    assert sp.simplify(e4_from_resonance-e4_rs) == 0
    for m in range(1, max_m+1):
        rhs = (2*(m+1+N)*d.get(m+1, 0)+e2*d.get(m, 0)
               +e4_from_resonance*a(m))
        q[m] = sp.factor((q[m-1]+2*rhs)/(m*(m+b-1)))
    energy, coeff = s11a.rs_series(N, delta, 6)
    assert sp.simplify(energy[4]-e4_from_resonance) == 0
    assert energy[1] == energy[3] == energy[5] == 0
    errors = {}
    for k in range(2, 7):
        m, n = k-4, N+k-4
        if n < 0:
            continue
        relative = coeff.get((k, n), 0)*sp.sqrt(
            sp.factorial(N)/sp.factorial(n))
        errors[k] = sp.simplify(relative-(-2)**m*q[m])
        assert errors[k] == 0
    return {"lowest_state": 0 if N < 2 else N-2, "lowest_m": lowest_m,
            "e4": e4_from_resonance, "q": q, "rs_errors": errors}


def _outside_math(text):
    """Return prose after removing fenced code and TeX math spans."""
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    patterns = [r"\\\[.*?\\\]", r"\$\$.*?\$\$", r"\\\(.*?\\\)"]
    for pattern in patterns:
        text = re.sub(pattern, "", text, flags=re.S)
    return text


def markdown_audit(path):
    text = Path(path).read_text(encoding="utf-8")
    assert "\t" not in text
    assert not re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]", text)
    inline_open = len(re.findall(r"\\\(", text))
    inline_close = len(re.findall(r"\\\)", text))
    display_open = len(re.findall(r"(?<![A-Za-z])\\\[", text))
    display_close = len(re.findall(r"(?<![A-Za-z])\\\]", text))
    assert inline_open == inline_close
    assert display_open == display_close
    assert text.count("$$") % 2 == 0
    prose = _outside_math(text)
    suspicious = re.compile(
        r"(?<![\\\w])(lambda|delta|epsilon|mathcal|frac|left|right|"
        r"lvert|rangle|cdots)(?![\w-])")
    hits = [(i, line) for i, line in enumerate(prose.splitlines(), 1)
            if suspicious.search(line)]
    assert not hits, hits
    return {"tabs": 0, "control_characters": 0, "naked_token_hits": hits,
            "inline_pairs": inline_open, "display_pairs": display_open}


def verify():
    s11c = _load("weak11c_for_11d", "11c_verify_multiplicative_bb.py")
    s11c.dressed_equation_check()
    assert s11c.dominant_s1_asymptotic()["x^-1"] != 0
    cases = {}
    for N in (0, 1, 2, 3, 4):
        for delta in (sp.Rational(2, 3), sp.Rational(5, 4), sp.Rational(7, 5)):
            cases[(N, delta)] = second_level(N, delta)
    # Explicit nonregression at N=0,b=2 (delta=1).
    cases[(0, sp.Integer(1))] = second_level(0, sp.Integer(1))
    markup = markdown_audit(ROOT / "docs/bender_bettencourt_weak_drive_resummation.md")
    return {"standard_h": standard_source_check(),
            "vop_residual": variation_of_parameters_check(),
            "multiplicative": multiplicative_equivalence_check(),
            "low_level_cases": cases, "markup": markup}


if __name__ == "__main__":
    result = verify()
    print("standard_h =", result["standard_h"])
    print("vop_residual =", result["vop_residual"])
    print("multiplicative =", result["multiplicative"])
    for key, value in result["low_level_cases"].items():
        print("low_level", key, "lowest_state =", value["lowest_state"],
              "lowest_m =", value["lowest_m"], "e4 =", value["e4"])
    print("markup =", result["markup"])
