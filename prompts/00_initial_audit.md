# Stage 00 — Initial mathematical audit

Read the following files carefully:

- `README.md`
- `zarys.md`
- `manuscript/manuscript.tex`

Perform a rigorous mathematical audit of the current manuscript, focusing on:

1. the definition and parameter conventions of the driven Kerr Hamiltonian;
2. the Bargmann-space differential equation;
3. the coefficient recurrence;
4. self-adjointness and the precise operator domains;
5. applicability of the Kato–Rellich theorem;
6. essential self-adjointness on the finite-particle subspace;
7. boundedness from below for \(V>0\), arbitrary real \(\omega_0\), and complex \(F\);
8. compactness of the resolvent and discreteness of the spectrum;
9. the distinction between entire solutions of the differential equation and vectors in Bargmann–Fock space;
10. the mathematical correctness and logical completeness of all proofs and claims.

For every gap, ambiguous convention, unjustified implication, or overly strong claim:

- explain the issue precisely;
- make the smallest correction needed;
- use wording suitable for a prospective Journal of Physics A manuscript.

Preserve the present scope and structure of the manuscript. Do not introduce numerical diagonalization or develop the later spectral theory at this stage.

After completing the audit:

1. apply only corrections that are mathematically justified by the current analysis;
2. compile `manuscript/manuscript.tex`;
3. record all performed checks and their results;
4. save the complete Git patch as `stage00_review.diff`;
5. save the audit and verification report as `stage00_review.log`;
6. ensure that the generated `.diff` and `.log` files are not accidentally included in their own patch;
7. do not create a Git commit.

At the end, report:

- the mathematical issues found;
- the corrections applied;
- the LaTeX compilation result;
- the paths of the two generated review files;
- the smallest logically coherent next step toward a non-diagonalization spectral condition derived from the coefficient recurrence.
