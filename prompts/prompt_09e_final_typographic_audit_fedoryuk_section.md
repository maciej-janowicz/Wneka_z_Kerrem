# Task 09e: Final typographic audit of the Fedoryuk section

You are working in the repository:

`~/Dokumenty/Prace_i_dnie/Wnęka_z_Kerrem`

The repository is synchronized with `origin/master`, but the working tree intentionally contains all uncommitted Stage 09a--09d changes. Preserve them.

Do not commit and do not push.

## Scope

This is a micro-correction and final verification task only.

Do not change any mathematical result, coefficient, sign convention, asymptotic status, scientific claim, script logic, or test logic unless an unmistakable typographic transcription error is found.

Do not introduce or discuss Bender--Bettencourt resummation. That topic belongs to a later, separate section.

## Required correction

In `docs/fedoryuk_weber_wavefunction_and_energy.md`, the displayed explicit coefficients of `u1_R` and `u1_I` contain accidental commas where multiplication spacing was intended, for example

```latex
5\sqrt2,3^{3/4}
```

Correct such expressions to unambiguous LaTeX multiplication, preferably

```latex
5\sqrt2\,3^{3/4}
```

or an exactly equivalent clear form.

Inspect all eight displayed coefficients

\[
c_{-3,R},c_{-1,R},c_{1,R},c_{3,R},
c_{-3,I},c_{-1,I},c_{1,I},c_{3,I}
\]

and ensure that punctuation is not accidentally placed inside a product.

Do not alter their mathematical signs or factors.

## Focused audit

Before editing, run and record `git status -sb`.

Inspect the Stage 09 documentation and manuscript additions for similar mechanical artifacts, including:

- commas accidentally used instead of multiplication or spacing;
- literal leaked commands such as `qquad`;
- missing backslashes;
- raw ASCII placeholders inside displayed mathematics;
- malformed `sqrt`, fraction, exponent, index, or differential notation;
- doubled words or visibly broken punctuation;
- inconsistencies between the documented coefficients and the exact symbolic output of `scripts/09c_verify_fedoryuk_weber.py`.

The audit should cover at least:

- `docs/fedoryuk_applicability_and_geometry.md`;
- `docs/fedoryuk_weber_wavefunction_and_energy.md`;
- the independent Fedoryuk subsection in `manuscript/manuscript.tex`;
- the Stage 09a--09d prompts, diffs, and logs only insofar as needed to confirm the authoritative formulas.

Do not perform broad stylistic rewriting.

## Verification

After the correction, run at least:

```bash
python scripts/09a_verify_fedoryuk_normal_form.py
python scripts/09c_verify_fedoryuk_weber.py
PYTHONPATH=src pytest -q
git diff --check
```

Compile the manuscript with the established LaTeX/BibTeX procedure.

Render and inspect the affected Fedoryuk pages and at least one adjacent page on each side. Confirm:

- no clipping or overlap;
- no malformed mathematical notation;
- no visible raw LaTeX commands;
- no change to equations, numbering, cross-references, or scientific status;
- no mention of Bender or Bettencourt in the Fedoryuk subsection.

Search both the source and extracted PDF text for known leaked-token patterns, including `qquad`.

## Deliverables

Create:

1. `prompt_09e_final_typographic_audit_fedoryuk_section.diff`
2. `prompt_09e_final_typographic_audit_fedoryuk_section.log`

The log must contain:

- initial and final `git status -sb`;
- exact files inspected;
- every typographic correction made, with before/after form;
- confirmation that no mathematical coefficient or scientific claim changed;
- test results;
- `git diff --check` result;
- compilation result;
- rendered pages inspected;
- any remaining warning;
- confirmation that no commit and no push were performed.

At the end, report whether the accumulated Stage 09a--09e result is ready for final review before Git staging.

Do not commit and do not push.
