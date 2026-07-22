Work only in the current Git repository. Before making any changes, verify
that the following files exist:

- zarys.md
- manuscript/manuscript.tex
- prompts/00_initial_audit.md

Also run `git rev-parse --show-toplevel` and record the resulting repository
root in stage01_special_functions.log. Do not use or modify any other copy of
the manuscript.


At this stage, please modify manuscript/manuscript.tex to include:

- the substitution Psi(z) = A(z) Phi(z);
- the explicit derivation of A(z);
- the complete Liouville normal-form equation for Phi;
- the singularity and branch structure of A(z);
- the two formal local behaviours of Phi near z = 0;
- the compensation and enhancement of the singularity after returning to Psi;
- the special-function classification and exact parameter correspondence,
  but only where rigorously established.

Do not introduce an energy-quantization condition at this stage. Clearly
separate proved statements from conjectures and future research directions.

Compile manuscript/manuscript.tex accordingly and verify that the newly added
material is present in manuscript/manuscript.pdf.

Save:
- the complete Git patch as stage01_special_functions.diff;
- the full mathematical and verification report as
  stage01_special_functions.log.

Ensure that the generated .diff and .log files are not included in their own
patch. Do not create a Git commit.
