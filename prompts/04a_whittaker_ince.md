# Stage 04a — Whittaker--Ince limit and the Bargmann spectral solution

## Purpose of this corrective stage

Stage 04 obtained a useful algebraic audit but stopped after observing the
ramified large-\(z\) behaviour

\[
 \Psi(z)\sim
 \exp\!\left(\pm2\sqrt{-qz}\right)
 z^{\,1/4-B_2/2}.
\]

That behaviour is not evidence that the Kerr equation lies outside the Heun
family.  It is the characteristic subnormal Thomé behaviour of the
Whittaker--Ince limit of the double-confluent Heun equation (DCHE).

Starting from

\[
 \frac{V}{2}z^2\Psi''(z)
 +\bigl(\hbar\omega_0z+\overline F\bigr)\Psi'(z)
 +(Fz-E)\Psi(z)=0,
 \qquad V>0,
\]

establish rigorously whether it is exactly the Whittaker--Ince limit

\[
 z^2U''+(B_1+B_2z)U'+(B_3+qz)U=0
\]

with

\[
 B_1=\frac{2\overline F}{V},\qquad
 B_2=\frac{2\hbar\omega_0}{V},\qquad
 B_3=-\frac{2E}{V},\qquad
 q=\frac{2F}{V}.
\]

Then identify and characterize the physical solution: an entire solution in
the Bargmann variable which belongs to Bargmann--Fock space.  Determine the
exact characteristic condition on \(E\), preferably in the established
Whittaker--Ince/DCHE theory and without Hamiltonian diagonalization.

This stage corrects and continues Stage 04.  Do not redo the entire earlier
survey, and do not treat the square-root exponential at infinity as an
unclassified obstruction.

## Central questions

Answer the following questions separately and explicitly.

1. Is the normalized Kerr equation exactly the Whittaker--Ince limit of a
   DCHE in a verified primary-source convention?
2. Which published power-series, Bessel-series, or other exact solutions of
   that limiting equation apply to the Kerr parameters?
3. Which solution is holomorphic at \(z=0\), and under what condition does it
   extend to an entire function?
4. Is Bargmann--Fock membership automatic for every entire solution of this
   equation because its order is \(1/2\), or does it impose an additional
   condition?
5. What exact condition selects the physical energies?
6. Is that condition a characteristic exponent, a characteristic value, a
   three-term-recurrence minimality condition, a continued fraction, a
   determinant, a connection coefficient, or a Wronskian?
7. Does an integer occur in the condition itself, or does
   \(n\in\mathbb N_0\) only label its discrete roots?
8. Does the condition reduce, in the singular limit \(F\to0\), to the Euler
   requirement \(\lambda=n\) and hence to the undriven Kerr spectrum?

The hoped-for result may be written schematically as

\[
 \Psi_n(z)=\mathcal N_n\,
 \operatorname{HeunD}_{\mathrm{reg}}
 \bigl(B_1,B_2,B_3(E_n),q;z\bigr),
\]

or, if preferable,

\[
 \Psi_n(z)=\mathcal N_n\,
 \operatorname{HeunD}_{\mathrm{BF}}
 \bigl(B_1,B_2,B_3(E_n),q;z\bigr).
\]

These are proposed manuscript notations, not assumed standard functions.
They may be introduced only after the solution has been defined
unambiguously by its differential equation, normalization, entire
continuation, and Bargmann--Fock condition.  State prominently that the
notation is author-defined.  Do not imply that Maple, Wolfram Language,
DLMF, Bühring, or Figueiredo uses it.

## Repository and preservation rules

Work only in the actual repository on this computer.

Before editing:

1. read `AGENTS.md` and every other repository instruction that exists;
2. record

   ```bash
   git status --short
   git log --oneline --decorate -n 15
   ```

3. read the complete current versions of:

   - `manuscript/manuscript.tex`;
   - `manuscript/references.bib`;
   - `README.md`;
   - `zarys.md` and `dalsze_kierunki.md`, if present;
   - `prompts/04_heund_entire_spectral_condition.md`;
   - `docs/stage04_heund_identification.md`;
   - `stage04_heund_entire_spectral_condition.log`;
   - the Stage 04 diff;
   - all directly relevant Stage 03 materials;

4. create `stage04a_whittaker_ince.log` immediately and maintain it
   throughout the work;
5. do not discard, overwrite, stage, or commit any existing user changes;
6. do not run a formatter over the manuscript.

Preserve every existing physical and mathematical discussion, citation,
equation, label, and bibliography entry except for the smallest local
correction required by a proved Stage 04a result.  Record every deletion and
its mathematical justification in the log before making it.

## Fixed physical notation

Retain

\[
 H=\frac{V}{2}a^{\dagger 2}a^2
 +\hbar\omega_0a^\dagger a
 +Fa^\dagger+\overline F\,a,
\]

where

\[
 V>0,\qquad \omega_0\in\mathbb R,\qquad F\in\mathbb C.
\]

The physical coefficients \(F\) and \(\overline F\) are complex conjugates,
not independent parameters.  A unitary phase rotation making \(F\) real and
nonnegative may be used only if it is explicitly derived and the final result
is translated back to the original variables.

Use the Bargmann--Fock convention

\[
 \Psi\ \hbox{entire},\qquad
 \|\Psi\|_{\mathrm B}^2
 =\int_{\mathbb C}|\Psi(z)|^2e^{-|z|^2}
   \frac{d^2z}{\pi}
 =\sum_{k=0}^{\infty}k!\,|c_k|^2<\infty
\]

for

\[
 \Psi(z)=\sum_{k=0}^{\infty}c_kz^k.
\]

Do not conflate formal regularity, convergence near zero, local holomorphy,
single-valued continuation, entireness, pointwise Gaussian damping, and
Bargmann--Fock square integrability.

## Part I — Verify the Whittaker--Ince classification

Use primary sources to state the exact parent DCHE, the limiting procedure,
and the resulting Whittaker--Ince equation.  Begin with, but do not
automatically limit the investigation to:

1. B. D. Bonorino Figueiredo, *Ince's limits for confluent and
   double-confluent Heun equations*, arXiv:math-ph/0509013 and its published
   version, if any;
2. B. D. Bonorino Figueiredo, *Generalized spheroidal wave equation and
   limiting cases*, arXiv:math-ph/0611048 and its published version, if any;
3. L. Jaccoud El-Jaick and B. D. B. Figueiredo, *On Certain Solutions for
   Confluent and Double-Confluent Heun Equations*, arXiv:0807.2219 and its
   published version;
4. L. Jaccoud El-Jaick and B. D. B. Figueiredo, *Confluent and
   Double-Confluent Heun Equations: Convergence of Solutions in Series of
   Coulomb Wavefunctions*, arXiv:1209.4673 and its published version;
5. original references by Ince, Whittaker, Leaver, or later authors when the
   cited papers explicitly depend on them.

For every formula used, record the source, equation number, parameter
hypotheses, and convergence domain.  Prefer the published version when it is
available, but a complete author manuscript or arXiv version is acceptable
when the journal text is inaccessible.  Do not stop merely because Maple's or
Wolfram Language's standard `HeunD` normalization is unavailable: this stage
concerns a verified limiting equation and may define its solutions directly.

Derive the limiting equation from the parent DCHE rather than identifying it
by visual resemblance alone.  Verify the map

\[
 (V,\hbar\omega_0,F,\overline F,E)
 \longmapsto (B_1,B_2,B_3,q)
\]

by direct substitution and a symbolic residual check.

Explain precisely:

- in which convention the limit corresponds to \(\epsilon_D=0\);
- whether setting \(\epsilon_D=0\) and taking the Whittaker--Ince limit are
  literally the same operation in that convention;
- what scaling of the remaining DCHE parameters is held fixed;
- how the singularity at infinity changes in the limit;
- why the appearance of \(\sqrt z\) in the exponential is expected rather
  than disqualifying.

If the manuscript's current broad DCHE form uses \(\epsilon_D=0\) only as a
formal coefficient specialization, replace that statement by the exact
limiting relation supported by the source.  Do not claim more than the
verified convention permits.

## Part II — Independent dominant-balance check

For

\[
 z^2U''+(B_1+B_2z)U'+(B_3+qz)U=0,
\]

derive the large-\(|z|\) formal behaviour by linear dominant balance in the
style of Bender and Orszag.  Insert

\[
 U(z)\sim e^{\sigma z^{1/2}}z^\rho
 \left(1+\sum_{j\ge1}a_jz^{-j/2}\right)
\]

and verify at least the first two balances:

\[
 \frac{\sigma^2}{4}+q=0,
\qquad
 \rho=\frac14-\frac{B_2}{2},
\]

so that

\[
 U(z)\sim
 \exp\!\left(\pm2\sqrt{-qz}\right)
 z^{\,1/4-B_2/2}.
\]

Check all signs and branch conventions.  Compare the result with the
primary-source Thomé formula.

Keep this subsection short.  Its present role is classification and
consistency checking.  Reserve a full discussion of Stokes sectors,
connection switching, higher asymptotic coefficients, and global
large-\(|z|\) plots for a later dedicated asymptotic stage.

Do not infer from a sectorial formal expansion that the exact solution is
multivalued.  The individual square-root formal branches may combine into an
entire solution.

## Part III — Exact solution families

Identify all published exact expansions applicable to the limiting equation,
especially:

- a solution represented by a power series or another expansion convergent
  for every finite \(z\);
- solutions represented by one-sided or two-sided series of Bessel or
  modified Bessel functions;
- their coefficient recurrences;
- their convergence domains;
- transformations generating companion solutions;
- connection relations between solutions sharing the same recurrence
  coefficients.

For each candidate solution, state:

1. its exact formula and normalization;
2. the recurrence for its coefficients;
3. the allowed parameter range;
4. its convergence domain;
5. its behaviour at \(z=0\);
6. its large-\(|z|\) behaviour;
7. whether it is single-valued and entire in \(z\);
8. how it maps to the Kerr wavefunction.

Do not call a locally convergent formal solution entire merely because the
differential equation has no other finite singular point: \(z=0\) is itself
an irregular singular point, and the convergence and continuation must be
proved.

If the literature's globally convergent solution is written as a series of
special functions rather than as one standardized named function, retain
that exact representation.  The absence of a universal software symbol is
not a negative mathematical result.

## Part IV — Taylor recurrence at the Bargmann origin

Independently insert

\[
 \Psi(z)=\sum_{k=0}^{\infty}c_kz^k
\]

into the original Kerr equation and verify

\[
 \overline F(k+1)c_{k+1}
 +\left[\frac V2k(k-1)+\hbar\omega_0k-E\right]c_k
 +Fc_{k-1}=0,
\qquad c_{-1}=0,
\]

with

\[
 \overline F\,c_1=Ec_0.
\]

Then determine rigorously:

1. whether the recurrence with the \(k=0\) relation produces a convergent
   Taylor series only for discrete \(E\);
2. the dominant and minimal asymptotic solutions of the recurrence;
3. whether the minimal branch satisfies

   \[
   c_k\sim
   C\,\frac{(-2F/V)^k}{(k!)^2}
   \times\hbox{an explicitly determined power correction};
   \]

4. the order and type of the resulting entire function;
5. the exact relation between this Taylor recurrence and the coefficient
   recurrence in the published Whittaker--Ince expansions.

Use an applicable theorem such as Perron--Kreuser, Pincherle, or a more
specific result only after stating and checking all hypotheses.

Resolve explicitly the apparent tension between:

- the differential equation fixing \(c_1\) from \(c_0\) for every formal
  \(E\);
- the generic forward recurrence developing a dominant factorial branch;
- the requirement that the Taylor series have nonzero radius of convergence;
- the existence of a minimal solution selected from infinity.

This point is central.  Do not conceal it with the phrase “regular solution at
zero”.

## Part V — Entire/Bargmann solution and characteristic condition

Determine the strongest exact necessary-and-sufficient condition for a
nonzero solution satisfying

\[
 \Psi\ \text{entire},\qquad \Psi\in\mathcal F_{\mathrm B}.
\]

Test, without presupposing the answer:

1. an integer characteristic exponent;
2. a characteristic value of \(B_3=-2E/V\);
3. compatibility between a globally convergent expansion and a Bessel-series
   solution;
4. minimality of the three-term recurrence;
5. an infinite continued fraction;
6. a Hill-type determinant;
7. a vanishing connection coefficient;
8. a Wronskian of two independently normalized solutions.

For the final condition:

- define every quantity explicitly;
- prove necessity and sufficiency, or state exactly which direction remains
  unproved;
- show that it produces all physical eigenvalues and no spurious values;
- state whether \(n\) appears in the equation or only labels ordered roots;
- establish its equivalence to the recurrence condition if both are used;
- ensure that it can be evaluated without diagonalizing a truncated
  Hamiltonian.

Investigate especially whether entireness is the true quantizing condition
and Bargmann membership then follows automatically.  If the admissible entire
solution has order \(1/2\), prove from its coefficients or a global growth
bound that

\[
 \int_{\mathbb C}|\Psi(z)|^2e^{-|z|^2}
 \frac{d^2z}{\pi}<\infty.
\]

Do not use a sectorial asymptotic alone as a proof of a global growth bound.

If no published Whittaker--Ince characteristic function has a standard name,
define a manuscript characteristic function \(\mathcal C(E)\) by a precise
recurrence, determinant, Wronskian, or connection coefficient.  State that
the notation is author-defined and explain its relation to the known
continued fraction.  Do not disguise a new notation as a standard `HeunD`
property.

## Part VI — Definition of the distinguished function

If the analysis succeeds, introduce one concise notation for the physical
solution.  The preferred candidates are

\[
 \operatorname{HeunD}_{\mathrm{reg}}
 (B_1,B_2,B_3,q;z)
\]

or

\[
 \operatorname{HeunD}_{\mathrm{BF}}
 (B_1,B_2,B_3,q;z).
\]

Choose only one for the manuscript.

Define it as the nonzero solution of

\[
 z^2U''+(B_1+B_2z)U'+(B_3+qz)U=0
\]

which:

1. is entire in \(z\);
2. belongs to Bargmann--Fock space after restoring the physical scaling, if
   any;
3. has a stated normalization, for example \(U(0)=1\), whenever that
   normalization is nonzero and well-defined.

If an eigenfunction has \(U(0)=0\), use a normalization that covers it without
division by zero, or explain why this cannot occur for \(F\ne0\).

The notation must exist only for parameter tuples satisfying the
characteristic condition.  Write this explicitly, for example:

\[
 \operatorname{HeunD}_{\mathrm{reg}}
 (B_1,B_2,B_3(E),q;z)
 \quad\text{exists iff}\quad
 \mathcal C(E)=0.
\]

Avoid saying “regular at infinity” without qualification.  Infinity remains
an irregular singular point.  The intended properties are entire
continuation, controlled growth, and Bargmann--Fock membership.

If the standard literature already supplies a more appropriate unambiguous
notation, prefer it and explain why a new symbol is unnecessary.

## Part VII — Mandatory undriven-limit test

Treat \(F=0\) directly before taking any limit of formulas that divide by
\(F\).  Recover

\[
 \frac V2z^2\Psi''+\hbar\omega_0z\Psi'-E\Psi=0.
\]

For \(\Psi=z^\lambda\), derive

\[
 \frac V2\lambda(\lambda-1)
 +\hbar\omega_0\lambda-E=0.
\]

Show that a single-valued entire Bargmann solution requires

\[
 \lambda=n\in\mathbb N_0,
\]

and hence

\[
 \boxed{
 E_n^{(0)}
 =\frac V2n(n-1)+\hbar\omega_0n.}
\]

Then analyse the singular limit \(F\to0\) of the driven
Whittaker--Ince characteristic condition.  Determine whether:

- it converges directly to \(\lambda(E)=n\);
- it requires rescaling or reindexing;
- it is singular but has a controlled limiting reduction;
- or it cannot be continued in the chosen normalization.

Reject any proposed spectral condition that does not recover the exact Euler
spectrum with the factor \(V/2\).

## Scope exclusions

Do not:

- diagonalize the Hamiltonian to define the spectrum;
- begin a full WKB or Stokes-geometry analysis;
- make global plots or study zeros of \(\Psi\);
- claim that the Whittaker--Ince solution is a standard software `HeunD`
  without documentation;
- infer a simple condition “something \(=n\)” merely from analogy;
- force polynomial termination if the physical functions are nonpolynomial;
- declare failure only because no universal one-symbol notation exists;
- claim novelty or priority.

A small diagonalization may be used only as an unpublished numerical
cross-check after an independent analytic characteristic condition has been
derived.  Record the truncation and convergence data, and never place that
diagonalization inside the definition of \(\mathcal C(E)\).

## Manuscript changes

Only after the classification, solution construction, and source verification
are complete, update `manuscript/manuscript.tex` minimally to include:

1. the exact Whittaker--Ince limiting equation and verified parameter map;
2. a correction of any misleading Stage 04 statement about ramification;
3. the exact expansion representing the physically relevant solution;
4. a proposition defining the entire/Bargmann solution;
5. the exact characteristic condition on \(E\), with proof or a precise proof
   outline;
6. the chosen author-defined notation, if useful;
7. the \(F=0\) Euler spectrum and the status of the driven-to-undriven limit;
8. a short dominant-balance formula, while reserving full asymptotic analysis
   for a later section;
9. an explicit list of anything still unproved.

Do not expand a modest verified result into a broad survey.  Preserve the
manuscript's physical motivation and existing rigorous operator-theoretic
results.

## Computational checks

Use symbolic algebra to verify:

- the normalized equation and parameter map;
- the parent-to-limit transformation;
- the Taylor recurrence;
- the dominant-balance exponents;
- the residual of every proposed exact transformation or solution;
- equivalence of recurrence forms;
- the \(F\to0\) reduction wherever algebraically meaningful.

Numerical work may be used to:

- evaluate the independently derived characteristic condition;
- test recurrence minimality;
- compare overlapping exact series;
- check a few energies against an independently converged reference.

Record precision, truncation rules, tolerances, and convergence diagnostics.
Do not hide unstable forward recurrence or numerical diagonalization behind a
special-function name.

## Deliverables

Produce:

1. the minimally updated `manuscript/manuscript.tex`;
2. verified additions, if any, to `manuscript/references.bib`;
3. `docs/stage04a_whittaker_ince.md`, containing the full derivation, source
   locations, solution formulas, recurrence comparison, convergence domains,
   and spectral-condition analysis;
4. `stage04a_whittaker_ince.log`;
5. `stage04a_whittaker_ince.diff`, containing the complete unstaged patch,
   including this prompt if it is untracked;
6. the successfully compiled `manuscript/manuscript.pdf`.

If the characteristic condition cannot yet be completed, still provide the
strongest verified result, the precise remaining obstruction, and the next
mathematical lemma or source needed.  Do not erase or overwrite the Stage 04
negative report; correct it additively and explain which conclusion changed.

## Validation and stopping rules

Before finishing:

1. compile the manuscript with the repository's documented procedure;
2. inspect the complete build log;
3. inspect every page of the PDF;
4. verify every transformation and recurrence independently;
5. check the dominant-balance result against the exact ODE;
6. verify the \(F=0\) spectrum;
7. run

   ```bash
   git diff --check
   ```

8. inspect the complete diff and confirm that no prior scientific content was
   lost;
9. report

   ```bash
   git status --short
   ```

10. do not stage or commit anything.

Stop and report a precise obstruction rather than improvising if:

- the claimed Whittaker--Ince equation cannot be verified in a primary
  source;
- a cited solution does not cover the Kerr parameter range;
- a convergence or minimality theorem's hypotheses fail;
- a proposed characteristic condition is conjectural;
- necessity or sufficiency is missing and cannot be supplied;
- a transformation divides by a vanishing parameter without treating the
  exceptional case;
- the \(F\to0\) test fails;
- manuscript preservation cannot be guaranteed.

Do not stop merely because a standard `HeunD` software definition is
unavailable or because the limiting solution lacks a universal one-symbol
name.

## Final report

End with a concise report stating:

1. the verified parent DCHE convention and Whittaker--Ince limiting
   procedure;
2. the exact Kerr-to-\((B_1,B_2,B_3,q)\) parameter map;
3. the exact solution representation and convergence domain;
4. the definition, if introduced, of
   \(\operatorname{HeunD}_{\mathrm{reg}}\) or
   \(\operatorname{HeunD}_{\mathrm{BF}}\);
5. the characteristic condition on \(E\);
6. whether \(n\) is part of the condition or only labels roots;
7. the proof status of entireness and Bargmann--Fock membership;
8. the large-\(|z|\) dominant-balance check;
9. the \(F\to0\) result;
10. all sources and exact equation/page locations;
11. every file changed or created;
12. compilation and validation results;
13. unresolved questions stated without speculation.
