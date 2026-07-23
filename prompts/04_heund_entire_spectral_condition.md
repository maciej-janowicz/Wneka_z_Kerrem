# Stage 04 — Exact HeunD identification and the entire-function spectral condition

## Central objective

Starting from the exact Bargmann eigenvalue equation for the coherently
one-photon-driven Kerr oscillator,

\[
 \frac{V}{2}z^2\Psi''(z)
 +(\hbar\omega_0 z+\overline F)\Psi'(z)
 +(Fz-E)\Psi(z)=0,
\qquad V>0,
\]

determine rigorously whether its physical eigenfunctions can be represented by
a precisely defined double-confluent Heun function and whether the
quantization of \(E\) follows from a standard Heun characteristic condition.

The desired result, if it is true, has the conceptual form

\[
 \Psi_E(z)
 =G(z)\operatorname{HeunD}\!\bigl(\boldsymbol{\alpha}(E);w(z)\bigr),
\]

together with an exact condition selecting the entire Bargmann--Fock
solutions,

\[
 \mathcal Q\!\bigl(\boldsymbol{\alpha}(E)\bigr)
 =n,\qquad n\in\mathbb N_0,
\]

or an equally explicit standard Heun characteristic-value condition.

This is a hypothesis to be tested, not a conclusion to be assumed.  If the
correct condition is instead the vanishing of a connection coefficient,
Wronskian, determinant, or another characteristic function, establish that
fact precisely.  Do not force the answer into the form
\(\mathcal Q(E)=n\) if the theory does not support it.

## Scope of this stage

This stage is about:

1. the exact canonical special-function identification;
2. the solution selected by holomorphy at \(z=0\);
3. its continuation to an entire function;
4. its admissible growth at infinity and membership in Bargmann--Fock space;
5. the resulting exact spectral condition;
6. the reduction of that condition to the elementary Euler quantization when
   \(F\to0\).

Do not begin a WKB analysis.  Do not introduce Stokes curves, anti-Stokes
curves, resurgent analysis, Borel summation, or sectorial approximations unless
one of these notions is logically unavoidable for stating an exact theorem
from the primary literature.  If unavoidable, state only the minimum needed
and explain why it cannot be avoided.  Do not make global plots or begin the
study of zeros in this stage.

Do not diagonalize a truncated Hamiltonian matrix.  Numerical work may be used
only as a secondary consistency check of an independently derived exact or
quasi-exact condition, never as the definition of the spectrum.

## Repository and preservation rules

Work only in the actual repository on this computer.

Before doing anything:

1. read `AGENTS.md` and all other repository instructions;
2. record

   ```bash
   git status --short
   git log --oneline --decorate -n 15
   ```

3. read the complete current versions of:

   - `manuscript/manuscript.tex`;
   - `manuscript/references.bib`, if present;
   - `README.md`;
   - `zarys.md` and `dalsze_kierunki.md`, if present;
   - all Stage 03, 03a, 03b, 03c, and 03d prompts, logs, and diffs;
   - all existing notes concerning the Liouville transformation, DCHE,
     Bühring, Ronveaux, or `HeunD`.

4. create `stage04_heund_entire_spectral_condition.log` immediately and
   maintain it throughout the work;
5. do not discard, overwrite, stage, or commit any existing user changes;
6. do not run a formatter over the manuscript.

Preserve all existing physical and mathematical literature-review content.
Do not delete, shorten, replace, or reorder any section, paragraph, citation,
proof, equation, label, bibliography entry, or other scientifically relevant
content merely to simplify the Stage 04 insertion.

If the current special-function section contains a mathematical error that
cannot be corrected additively, make only the smallest necessary local
replacement.  Before doing so, record the exact old text and the mathematical
reason for the correction in the log.  No unrelated rewriting is permitted.
At the end, inspect the manuscript diff line by line and confirm that every
deletion is both local to the Stage 04 mathematics and strictly necessary.

## Fixed notation and physical problem

Retain the manuscript Hamiltonian and notation:

\[
 H=\frac{V}{2}a^{\dagger 2}a^2+\hbar\omega_0a^\dagger a
   +Fa^\dagger+\overline F\,a,
\qquad V>0,\quad \omega_0\in\mathbb R,\quad F\in\mathbb C.
\]

The physical problem has \(\overline F\) equal to the complex conjugate of
\(F\).  Do not silently treat them as independent parameters.  A phase rotation
that makes \(F\) real and nonnegative may be used if it is derived explicitly,
shown to be unitary, and translated back to the original notation.

The Bargmann--Fock condition is

\[
 \Psi\ \text{entire},\qquad
 \|\Psi\|_{\mathrm B}^2
 =\int_{\mathbb C}|\Psi(z)|^2e^{-|z|^2}
   \frac{d^2z}{\pi}<\infty.
\]

Distinguish carefully among:

- formal regularity at \(z=0\);
- convergence of a formal Taylor series;
- holomorphy in a neighbourhood of \(0\);
- single-valued analytic continuation;
- entire continuation on \(\mathbb C\);
- admissible pointwise growth;
- Bargmann--Fock square integrability.

Do not assert that any one of these automatically implies the others without a
proof or a precisely cited theorem.

## Part I — Re-derive and audit the differential equation

Independently re-derive the Bargmann equation from the Hamiltonian using

\[
 a^\dagger\mapsto z,\qquad a\mapsto\frac{d}{dz}.
\]

Check every coefficient, factor of \(2\), complex conjugation, sign, and
dimension.  Verify the result by direct symbolic substitution.

Treat separately:

1. \(F\neq0\), the main driven problem;
2. \(F=0\), the singular undeformed limit;
3. any exceptional parameter values such as
   \(\hbar\omega_0/V\in\mathbb Z\), but only where they genuinely affect the
   analysis.

Do not infer the \(F=0\) result merely by substituting \(F=0\) into a formula
whose derivation divided by \(F\).

## Part II — Identify the exact DCHE convention

The phrase “double-confluent Heun equation” is not sufficient.  Find and state
the exact canonical equation, parameter ordering, independent variable,
normalization, and distinguished solution used in each relevant convention.

At minimum, compare:

1. the convention used by Bühring in his work on the double-confluent Heun
   equation;
2. the symmetric canonical treatment in the relevant chapter of Ronveaux's
   volume;
3. DLMF's current convention and notation;
4. Maple's `HeunD`, including its defining differential equation and
   normalization;
5. Wolfram Language's `HeunD`, including its defining differential equation
   and normalization.

Use primary sources, the original book/paper, DLMF, and official computer
algebra documentation.  Do not rely on search-result snippets, informal web
pages, autogenerated summaries, or remembered formulas.  Record exact
bibliographic data and equation/page/section numbers in the log.

Construct an explicit parameter-conversion table among all conventions that
are genuinely applicable.  Every conversion must be verified by substitution
into the differential equation.  Do not identify two functions merely because
their equations have the same name.

In particular, audit the canonical equation and parameter map already present
in the manuscript.  Determine whether its degenerate coefficient
\(\epsilon_D=0\):

- is a legitimate generic or degenerate DCHE case in the cited convention;
- changes the type or rank of either singular point;
- falls outside the domain in which a standard `HeunD` normalization is
  defined;
- reduces to another named special-function equation after a gauge, Möbius,
  inversion, or scaling transformation.

Search explicitly for a simpler exact reduction before concluding that DCHE is
irreducible.

## Part III — Determine the distinguished exact solution

Find a transformation

\[
 \Psi(z)=G(z)\,u(w(z))
\]

that maps the Bargmann equation to the selected canonical equation.  Derive
\(G\), \(w\), and every canonical parameter explicitly in terms of
\(V,\hbar\omega_0,F,\overline F,E\).

Then determine exactly what the notation

\[
 \operatorname{HeunD}(\ldots;w)
\]

means in that convention:

- which local or global solution it denotes;
- where it is normalized;
- whether that normalization is meaningful at the image of \(z=0\);
- whether it is single-valued;
- whether it is holomorphic at \(z=0\);
- whether prefactors introduced by the transformation cancel or create
  powers, branch points, poles, or essential singularities.

Do not call an arbitrary linear combination `HeunD`.  If no standard
normalized `HeunD` is simultaneously appropriate at \(0\) and infinity, say
so explicitly and define any necessary solution symbol unambiguously by its
equation and normalization.

Substitute the final candidate solution back into the original Bargmann
equation symbolically and simplify the residual to zero.  This direct
substitution is mandatory.

## Part IV — Taylor recurrence and analyticity at the origin

Independently insert

\[
 \Psi(z)=\sum_{k=0}^{\infty}c_kz^k
\]

into the original Bargmann equation and derive the exact coefficient
recurrence, including the \(k=0\) relation.

For \(F\neq0\), determine rigorously:

1. how many formal power-series solutions are fixed by \(c_0\);
2. whether the formal series converges for arbitrary \(E\);
3. whether generic forward solutions contain a dominant factorial branch;
4. whether convergence, holomorphy, or entireness itself already imposes a
   condition on \(E\);
5. how the admissible solution relates to a minimal solution of the
   recurrence.

Do not state that “the solution regular at zero exists for every \(E\)” unless
the convergence of the corresponding formal series has actually been proved.
Conversely, do not identify formal factorial growth with a theorem about the
exact solution without establishing the relevant recurrence asymptotics.

Use the recurrence as an independent check of the Heun identification, not as
a substitute for it.  A continued fraction may be derived or cited for
comparison, but Stage 04 must determine whether the same condition has a
standard Heun-theoretic meaning.

## Part V — The exact quantization condition

This is the central task.

Determine which exact Heun datum, if any, enforces the existence of a
nonzero solution that is entire and belongs to Bargmann--Fock space.  Test the
following possibilities rather than assuming one of them:

1. an integer characteristic or Floquet exponent,
   \(\nu(E)=n\);
2. a characteristic value of an accessory parameter,
   \(q(E)=q_n(\ldots)\);
3. a polynomial or series-termination condition;
4. simultaneous termination and determinant conditions of Heun-polynomial
   type;
5. vanishing of a connection coefficient;
6. vanishing of a Wronskian between independently normalized admissible
   solutions;
7. zero of a standard characteristic function or Hill-type determinant;
8. a condition equivalent to minimality of the Taylor recurrence.

For every candidate:

- state the theorem or derivation on which it rests;
- state all hypotheses and check them for the present degenerate DCHE;
- distinguish necessity from sufficiency;
- explain whether \(n\) is an actual integer appearing in the condition or
  merely an index labelling ordered roots;
- establish whether the condition gives every eigenvalue and no spurious
  values;
- explain whether it selects holomorphy, entire continuation, admissible
  growth, Bargmann--Fock membership, or some combination of these.

If a standard Heun characteristic condition exists, write it explicitly in
the manuscript notation and map it to \(E\).  A placeholder such as
“\(\operatorname{HeunD}(\text{something})=0\)” is not an acceptable result.

If the best exact result is a named characteristic function
\(\mathcal C(E)\), define \(\mathcal C\) precisely enough that it can be
evaluated without Hamiltonian diagonalization.  If it reduces algebraically to
the known continued fraction, prove or document that equivalence.

If no published standard `HeunD` condition supplies the quantization, record
this negative result clearly.  Do not disguise a newly defined
\(\mathcal C(E)=0\) as a standard property of `HeunD`.

## Part VI — Mandatory undeformed-limit test

For \(F=0\), derive the Euler equation directly:

\[
 \frac{V}{2}z^2\Psi''+\hbar\omega_0z\Psi'-E\Psi=0.
\]

For \(\Psi=z^\lambda\), derive the indicial equation and show that entire
single-valued Bargmann solutions require

\[
 \lambda=n\in\mathbb N_0,
\]

giving

\[
 \boxed{
 E_n^{(0)}
 =\frac V2n(n-1)+\hbar\omega_0n.}
\]

Then take the limit \(F\to0\) of the driven characteristic condition with full
care.  Determine whether it:

- tends continuously to \(\lambda(E)=n\);
- becomes singular but has a controlled asymptotic reduction to that
  condition;
- or cannot be continued to \(F=0\) in the chosen Heun normalization.

Any proposed Stage 04 quantization formula that fails to reproduce the Euler
spectrum, with the correct factor \(V/2\), must be rejected or corrected.

## Part VII — Bargmann growth and completeness of the criterion

Prove, or cite an applicable theorem proving, the relationship between the
selected recurrence/Heun solution and Bargmann--Fock membership.

At minimum, establish a rigorous coefficient criterion using

\[
 \Psi(z)=\sum_{k=0}^{\infty}c_kz^k,
\qquad
 \|\Psi\|_{\mathrm B}^2
 =\sum_{k=0}^{\infty}k!\,|c_k|^2.
\]

Determine the order and, if accessible without a separate asymptotic project,
the type of the admissible entire solution.  It is acceptable to prove a
sufficient growth bound rather than a sharp asymptotic formula.  Do not assume
that pointwise decay of \(e^{-|z|^2/2}\Psi(z)\) in selected directions is
equivalent to the two-dimensional Bargmann norm.

Use the already established self-adjointness and compact resolvent of \(H\) as
a consistency check: the final condition should describe a real, discrete
spectrum for the physical parameters.  Do not use those operator-theoretic
facts as a substitute for deriving the analytic spectral condition.

## Manuscript changes

Only after completing the derivation and source verification, update
`manuscript/manuscript.tex` so that it contains:

1. the exact, fully specified special-function convention;
2. the verified transformation and parameter map;
3. an unambiguous notation for the distinguished solution;
4. a theorem or proposition stating the entire/Bargmann spectral condition,
   with proof or a precise proof outline;
5. the \(F=0\) Euler case and the limiting test;
6. an explicit statement of what remains unproved, if the hoped-for simple
   Heun condition cannot be established.

Do not introduce WKB or Stokes geometry into the main exposition merely to
name solutions.  The conceptual presentation should parallel the elementary
logic:

\[
 \text{regular/entire solution}
 +\text{Bargmann admissibility}
 \Longrightarrow
 \text{quantized energy}.
\]

Use `HeunD` only if its exact convention and normalization have been stated.
Do not claim novelty or priority.  Add bibliography entries only for sources
actually inspected and cited in the manuscript.  Preserve all existing
physical and mathematical references.

## Computational verification

Symbolic algebra may be used to:

- verify changes of variables and gauge transformations;
- verify parameter maps;
- substitute candidate solutions formally into the ODE;
- derive and compare recurrences;
- check the \(F\to0\) reduction.

If a computer algebra system has a built-in `HeunD`, first verify its exact
documented convention.  Do not trust the function name alone.

A small numerical check is permitted for a few parameter values:

- solve the derived characteristic equation without Hamiltonian
  diagonalization;
- compare the resulting energies with an independently converged reference
  calculation only as a validation;
- record all numerical methods and tolerances.

Do not make the numerical reference calculation part of the published
derivation, and do not hide numerical diagonalization inside the definition of
the characteristic values.

## Deliverables

Produce:

1. the updated `manuscript/manuscript.tex`;
2. any verified bibliography additions in `manuscript/references.bib`;
3. `docs/stage04_heund_identification.md`, containing the full convention
   comparison, derivation, parameter-conversion table, and source locations;
4. `stage04_heund_entire_spectral_condition.log`;
5. `stage04_heund_entire_spectral_condition.diff`, containing the complete
   unstaged Stage 04 patch, including this prompt if it is untracked;
6. the successfully compiled `manuscript/manuscript.pdf`.

If the research establishes that the hoped-for simple condition does not
exist, the deliverables must still contain the exact strongest result obtained,
the obstruction, and a precise statement of what would be required next.

## Validation and stopping rules

Before finishing:

1. compile the manuscript from the current source using the repository's
   documented build procedure;
2. inspect the complete compilation log and resolve Stage 04 errors;
3. inspect every page of the resulting PDF for missing text, broken equations,
   bad page breaks, unresolved references, and bibliography problems;
4. verify all transformations by direct substitution;
5. verify the coefficient recurrence independently;
6. verify the \(F=0\) spectrum and the driven-condition limit;
7. verify

   ```bash
   git diff --check
   ```

8. inspect the full diff and confirm that no pre-existing scientific content
   has been lost;
9. report the final

   ```bash
   git status --short
   ```

10. do not stage or commit anything.

Stop and report the obstruction instead of improvising if:

- the primary definition of a claimed `HeunD` convention cannot be verified;
- the current degenerate equation lies outside the hypotheses of the cited
  theorem;
- the transformation requires division by a parameter that may vanish and the
  exceptional case has not been treated;
- the alleged characteristic condition is only conjectural;
- the condition is necessary but sufficiency for Bargmann--Fock membership
  cannot be established;
- the \(F\to0\) limit fails to recover the Euler spectrum;
- manuscript preservation cannot be guaranteed.

## Final report

End with a concise report stating:

1. the exact canonical equation and convention selected;
2. the exact formula, if any, for the physical solution in terms of `HeunD`;
3. the precise spectral condition and whether \(n\) occurs as a mathematical
   integer condition or only labels its roots;
4. the proof status of entireness and Bargmann--Fock membership;
5. the result of the \(F\to0\) test;
6. the sources and exact locations supporting the special-function claims;
7. every file changed or created;
8. compilation and validation results;
9. unresolved questions, without speculative answers.
