# Stage 06 — Formal Liouville–Green approximation at infinity

Work only in the existing `Wnęka_z_Kerrem` repository.

Stage 06: derive and add Subsection 5.1 on the formal
Liouville–Green (WKB) approximation at complex infinity.

The purpose of this stage is to build a mathematically explicit bridge
between the direct large-|z| asymptotic analysis completed in Stage 05
and the subsequent uniform asymptotic analysis following Olver.

Before changing anything:

1. Read all repository instructions, including every applicable
   AGENTS.md file.
2. Inspect the current Git status and do not overwrite or discard any
   existing user changes.
3. Read the current manuscript carefully, especially:
   - the exact Bargmann differential equation;
   - its reduction to normal form;
   - the notation for all physical and dimensionless parameters;
   - the Stage 05 local analysis at z = 0;
   - the two formal asymptotic branches at z = infinity;
   - the previously derived exponents, powers, and recurrence
     coefficients.
4. Inspect the Stage 05 documentation, source code, tests, prompts, and
   audit artifacts insofar as they are available in the repository.
5. Reuse the established notation exactly. Do not reconstruct equations
   from memory, and do not silently change conventions.

Create the prompt file:

    prompts/06_formal_liouville_green.md

containing this complete task specification, adapted only if necessary
to match the repository’s established formatting conventions.

MATHEMATICAL TASK
=================

Starting from the exact differential equation already established in
the manuscript, derive the formal Liouville–Green approximation
explicitly for this driven Kerr-mode problem.

A. Exact reduction to normal form
---------------------------------

1. Begin with the actual second-order Bargmann equation in the notation
   of the manuscript.

2. If it has the form

       psi''(z) + P(z) psi'(z) + Q(z; E) psi(z) = 0,

   perform the Liouville transformation explicitly:

       psi(z) = exp[-(1/2) integral P(z) dz] Phi(z).

3. Derive and simplify the exact normal-form coefficient:

       Phi''(z) + R(z; E) Phi(z) = 0,

   where

       R(z; E) = Q(z; E) - P'(z)/2 - P(z)^2/4,

   subject to the manuscript’s actual sign and notation conventions.

4. Verify algebraically that the displayed R(z; E) agrees with any
   normal form already present in the manuscript. If there is a
   discrepancy, stop and diagnose it rather than silently choosing one
   version.

5. State all singularities of R(z; E), its behavior at z = 0, and its
   leading structure as z tends to complex infinity.

B. Branch conventions and WKB solutions
---------------------------------------

1. Define the WKB momentum consistently. For example, if the normal
   form is

       Phi'' + R Phi = 0,

   use

       p(z; E) = sqrt[-R(z; E)]

   and

       Phi_WKB^(sigma)(z; E)
         = p(z; E)^(-1/2)
           exp[sigma integral^z p(t; E) dt],

       sigma in {+1, -1},

   or use the equivalent convention appropriate to the actual equation.

2. State explicitly:
   - the branch of the square root;
   - the branch of log z;
   - the chosen cuts;
   - the sectors in the complex z-plane in which the expansion is
     interpreted;
   - how analytic continuation changes the branches.

3. Avoid relying only on the words “Stokes” and “anti-Stokes”, because
   their naming conventions vary. Whenever these notions are mentioned,
   define the relevant curves by equations involving the real or
   imaginary part of the WKB action.

4. This subsection is formal. Do not claim uniform validity or rigorous
   error bounds. Clearly state that ordinary WKB fails or becomes
   singular at turning points, which motivates the following Olver
   subsection.

C. Explicit expansion at large |z|
----------------------------------

1. Expand p(z; E) to sufficient order:

       p(z; E)
         = p_0 + p_1/z + p_2/z^2 + p_3/z^3 + ...

   using the actual coefficient R(z; E).

2. Integrate term by term, retaining all contributions required to
   determine:
   - the exponential factor exp(sigma s z);
   - the logarithmic contribution and therefore the power of z;
   - the first inverse-power correction;
   - preferably the second inverse-power correction if this can be
     obtained cleanly and checked.

3. Expand the WKB prefactor p(z; E)^(-1/2).

4. Undo the Liouville transformation and obtain the two asymptotic
   branches in the established Stage 05 notation:

       psi_sigma(z)
         ~ exp(sigma s z) z^(mu_sigma)
           [1 + u_1^(sigma)/z + O(z^(-2))],

   or the exact equivalent dictated by the manuscript.

5. Derive s and mu_sigma explicitly in terms of the physical or
   dimensionless parameters.

6. Compare these expressions, coefficient by coefficient, with the
   direct dominant-balance and formal-series results from Stage 05.

D. Required distinction between leading WKB and transport corrections
---------------------------------------------------------------------

Do not assume that the lowest-order Liouville–Green formula reproduces
the complete Stage 05 coefficient u_1^(sigma).

Determine explicitly:

1. which parts of the Stage 05 asymptotics are reproduced by the
   lowest-order WKB phase and prefactor;

2. whether u_1^(sigma) is reproduced exactly;

3. if it is not reproduced exactly, what term is missing and why;

4. whether the missing contribution is recovered by the first formal
   higher-order WKB/transport correction.

If a higher-order correction is needed, derive only the minimum formal
transport equation required to recover and verify u_1^(sigma). Do not
turn this stage into the full Olver analysis.

Present the comparison in a compact table in the documentation and,
if suitable, in the manuscript:

    quantity | Stage 05 direct series | leading WKB | corrected WKB

The table must use exact symbolic expressions whenever feasible.

E. Symbolic and numerical verification
--------------------------------------

Add a small, focused implementation using the project’s established
Python structure. The implementation is an audit and verification tool,
not part of the scientific narrative of the manuscript.

1. Add a module with clearly documented pure functions for:
   - the normal-form coefficient;
   - the large-z expansion of the WKB momentum;
   - the integrated WKB phase coefficients;
   - the prefactor coefficients;
   - any first transport correction needed for comparison with Stage 05.

2. Prefer exact symbolic algebra where practical. If the project does
   not already depend on SymPy, do not add it casually: first determine
   whether the checks can be implemented using exact algebra encoded
   directly or with the existing dependencies.

3. Add tests that check:
   - the Liouville normal-form transformation;
   - the asymptotic expansion of the square root;
   - reconstruction of R from the truncated momentum expansion;
   - agreement of s and mu_sigma with Stage 05;
   - agreement or precisely documented disagreement of u_1^(sigma) at
     leading WKB order;
   - recovery of u_1^(sigma) after the first transport correction, if
     applicable;
   - both sigma branches;
   - several nondegenerate parameter choices;
   - rejection or explicit handling of degenerate parameter values and
     branch-sensitive cases.

4. If numerical spot checks are useful, compare the exact normal-form
   residual with the asymptotic residual for increasing |z| along
   several rays that stay away from cuts and turning points.

5. Do not claim a numerical check proves an asymptotic theorem.

F. Manuscript subsection
------------------------

Add Subsection 5.1, with a title such as:

    Formal Liouville–Green approximation at infinity

unless the existing section structure requires a slightly different
number or title.

The subsection must:

1. be self-contained enough to follow without reading the source code;

2. show the exact Liouville transformation and normal form;

3. display the two leading WKB branches;

4. carry out the large-|z| expansion explicitly rather than merely
   quoting the generic WKB formula;

5. compare the result with the Stage 05 direct asymptotics;

6. distinguish leading WKB from any higher transport correction;

7. specify branch and sector conventions;

8. explain briefly why turning points require Olver’s uniform method;

9. contain no references to Python, source-code directories, module
   names, scripts, tests, repository layout, or implementation details.

The implementation may be described in separate technical
documentation, but the manuscript must remain a mathematical physics
paper rather than a software report.

Do not yet:
- perform the full Olver construction;
- derive rigorous error bounds;
- develop the Fedoryuk approach;
- introduce the V/|F| strong-driving expansion;
- generate Stokes-line figures;
- generate or iterate quasi-fractal maps;
- alter unrelated sections of the manuscript.

G. Documentation
----------------

Create:

    docs/stage06_formal_liouville_green.md

It must contain:

1. the complete derivation in audit-friendly form;
2. branch and sign conventions;
3. the comparison with Stage 05;
4. the distinction between leading and corrected WKB;
5. assumptions and excluded degenerate cases;
6. a description of every verification performed;
7. any unresolved mathematical issue stated explicitly.

H. Build and visual verification
--------------------------------

1. Run the focused new tests.
2. Run the complete existing test suite.
3. Build the manuscript using the repository’s established build
   procedure.
4. Inspect the build log for errors, unresolved references, undefined
   citations, overfull boxes, and suspicious warnings.
5. Render and visually inspect every page affected by the new
   subsection, including the preceding and following pages.
6. Check equation wrapping, page breaks, table layout, notation,
   headings, and consistency with the surrounding manuscript.
7. Correct any problems caused by this stage and repeat the necessary
   checks.

I. Audit artifacts and Git discipline
-------------------------------------

Create a self-contained log:

    stage06_formal_liouville_green.log

The .log file must be self-contained and must contain the complete final
report verbatim, including every requested deliverable. The final
terminal response may repeat or briefly summarize it, but must not be
the only location of the report.

The log must include:

1. the initial Git status;
2. the files inspected;
3. the mathematical derivation summary;
4. the exact comparison with Stage 05;
5. every command used for tests and manuscript building;
6. complete test results or faithful concise summaries with pass/fail
   counts;
7. manuscript build results;
8. visual-inspection results;
9. warnings and unresolved issues;
10. the final Git status;
11. the complete final report specified below.

Also create:

    stage06_formal_liouville_green.diff

containing the final relevant Git diff, including staged and unstaged
project changes as appropriate, but excluding unrelated pre-existing
user changes and excluding the audit artifacts themselves if they are
intentionally untracked.

Do not commit.

Stage only the intended project files if that matches the established
workflow of the preceding stages. Leave the .log and .diff audit
artifacts untracked unless repository instructions explicitly require
otherwise.

Before finishing, run:

    git diff --check

and, if files were staged:

    git diff --cached --check

Resolve genuine whitespace errors. Do not disguise mathematical or
merge conflicts merely to make the commands quiet.

FINAL REPORT
============

The complete final report must appear verbatim inside
`stage06_formal_liouville_green.log`.

It must include:

1. a concise statement of what was implemented;
2. the exact normal-form coefficient R(z; E);
3. the chosen definition and branches of the WKB momentum;
4. the derived expressions for the exponential rate and algebraic
   powers of both branches;
5. the derived first inverse-power coefficient at leading WKB order;
6. the comparison with the Stage 05 coefficient u_1^(sigma);
7. the result of any first transport correction;
8. a clear statement of what agrees exactly and what does not;
9. the domain/sector and nondegeneracy assumptions;
10. all added or modified files;
11. focused and full test results;
12. manuscript build and visual-inspection results;
13. Git diff-check results;
14. unresolved mathematical or technical issues;
15. the final `git status --short`.

Do not report success if:
- the exact equation was not taken from the current repository;
- the sign or branch conventions remain ambiguous;
- the Stage 05 comparison was not actually performed;
- the tests fail;
- the manuscript does not build;
- the affected pages were not visually inspected;
- the complete final report is absent from the .log file.
