# Stage 04b — HeunWI-first formulation and historical continued-fraction audit

## Purpose

Revise the manuscript after Stage 04a so that its logical order reflects the
special-function result rather than the computational recurrence.

The manuscript must present:

1. the author-defined Whittaker--Ince function `HeunWI`;
2. a characteristic quantity \(\Delta_{\mathrm{WI}}\) defined solely in terms
   of `HeunWI`;
3. the characteristic values \(B_n^{\mathrm{WI}}\), defined solely through
   the entireness of `HeunWI`, equivalently through the zeros of
   \(\Delta_{\mathrm{WI}}\);
4. the exact Kerr spectrum in terms of \(B_n^{\mathrm{WI}}\);
5. only afterwards, the three-term recurrence, minimal-solution theorem, and
   continued fraction as derived representations useful for computation.

Do not delete the continued-fraction result.  Demote it from a definition or
primary spectral statement to a theorem derived from the preceding
special-function formulation.

A second, equally important task is a serious primary-literature audit of
continued fractions in the coherently driven Kerr-cavity model.  The
continued fraction may have been used in quantum optics in the 1980s.  The
manuscript must not imply novelty for it until this has been checked.

## Repository and preservation rules

Work only in the actual repository on this computer.

Before editing:

1. read `AGENTS.md` and every other repository instruction that exists;
2. record:

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
   - `prompts/04a_whittaker_ince.md`;
   - all Stage 04 and Stage 04a logs, diffs, reports, and relevant source
     downloads;

4. create `stage04b_heunwi_characteristic_values.log` immediately and maintain
   it throughout the work;
5. do not discard, overwrite, stage, or commit existing user changes;
6. do not run a formatter over the manuscript;
7. preserve all correct Stage 04a mathematics, changing only its definitions,
   logical order, novelty language, and statements made obsolete by this
   stage.

## Fixed equation and parameter map

Retain the Whittaker--Ince equation

\[
 z^2U''+(B_1+B_2z)U'+(B_3+qz)U=0
\]

and the Kerr map

\[
 B_1=\frac{2\overline F}{V},\qquad
 B_2=\frac{2\hbar\omega_0}{V},\qquad
 B_3=-\frac{2E}{V},\qquad
 q=\frac{2F}{V},
\]

with \(V>0\), \(\omega_0\in\mathbb R\), and \(F\in\mathbb C\).

The symbols

\[
 \operatorname{HeunWI},\qquad
 \Delta_{\mathrm{WI}},\qquad
 B_n^{\mathrm{WI}}
\]

are author-defined notation.  State this prominently.  Do not attribute these
symbols to Figueiredo, El-Jaick, Maple, Wolfram Language, or DLMF.

Use \(B_n^{\mathrm{WI}}\), not \(B_{3,n}^{\mathrm{WI}}\).

## Part I — Define `HeunWI` before any spectral machinery

Give a mathematically precise definition of

\[
 \operatorname{HeunWI}(B_1,B_2,B_3,q;z).
\]

The definition must specify:

- the differential equation;
- the normalization at \(z=0\);
- whether the initial object is a formal power series, a holomorphic germ, or
  an analytically continued solution;
- the exceptional parameter cases, especially \(B_1=0\), \(q=0\), and any
  case in which the normalization or coefficient recursion degenerates;
- the dependence on the parameters and any phase convention.

Do not conceal the fact that \(z=0\) is an irregular singular point.  Do not
call a merely formal series a holomorphic function.  If the generic
normalization \(U(0)=1\) determines only a formal solution until the
characteristic condition is satisfied, say so explicitly and use notation
that remains logically sound.

This definition and its immediate discussion must contain no continued
fractions and no WKB-related language.  In particular, do not mention:

- Pincherle's theorem;
- minimal or dominant recurrence solutions;
- Perron--Kreuser theory;
- Thomé solutions;
- Stokes sectors or Stokes multipliers;
- WKB, Liouville--Green, or semiclassical terminology;
- large-\(|z|\) exponential balances.

Those notions may appear only later, after
\(\Delta_{\mathrm{WI}}\), \(B_n^{\mathrm{WI}}\), and the spectral formula have
been defined.

## Part II — Define \(\Delta_{\mathrm{WI}}\) solely from `HeunWI`

Define a concrete, normalized characteristic quantity

\[
 \Delta_{\mathrm{WI}}(B_1,B_2,B_3,q)
\]

using only the previously defined `HeunWI` object and standard operations on
that object.  No recurrence, determinant, continued fraction, Wronskian,
connection coefficient, asymptotic solution, or WKB-related object may occur
in this definition.

It is not sufficient merely to state

\[
 \Delta_{\mathrm{WI}}=0
 \iff \operatorname{HeunWI}\text{ is entire},
\]

because this specifies only a zero set and leaves the normalization of
\(\Delta_{\mathrm{WI}}\) undetermined.

First investigate the canonical coefficient-growth definition.  If

\[
 \operatorname{HeunWI}(B_1,B_2,B_3,q;z)
 =\sum_{k=0}^{\infty}c_k z^k
\]

denotes the normalized formal solution, test rigorously whether one may set

\[
 \boxed{
 \Delta_{\mathrm{WI}}(B_1,B_2,B_3,q)
 :=
 \limsup_{k\to\infty}|c_k|^{1/k}
 =
 \limsup_{k\to\infty}
 \left|
 [z^k]\operatorname{HeunWI}(B_1,B_2,B_3,q;z)
 \right|^{1/k}.}
\]

This is the inverse Cauchy--Hadamard radius and is defined exclusively in
terms of `HeunWI`.  Prove, under explicitly stated hypotheses, that

\[
 \Delta_{\mathrm{WI}}=0
 \iff
 \operatorname{HeunWI}\text{ has infinite radius of convergence}
 \iff
 \operatorname{HeunWI}\text{ is entire in }z.
\]

Audit the limitations of this candidate carefully:

- it is real and nonnegative rather than generally holomorphic in the
  parameters;
- the limsup may make parameter dependence nonsmooth;
- exceptional terminating or degenerate cases need separate treatment;
- a formal coefficient sequence must be well defined before the expression
  is used.

If these limitations make the notation \(\Delta_{\mathrm{WI}}\) misleading,
propose and justify a better concrete functional of `HeunWI` alone.  However,
do not replace it by an object defined through a continued fraction,
recurrence minimality, determinant, connection problem, Wronskian, or
asymptotics.  Record the alternatives and the final choice in the stage log.

## Part III — Define \(B_n^{\mathrm{WI}}\) without continued fractions

For fixed admissible \(B_1,B_2,q\), define

\[
 B_n^{\mathrm{WI}}(B_1,B_2,q),\qquad n\in\mathbb N_0,
\]

as the ordered characteristic values of \(B_3\) for which the normalized
`HeunWI` is entire:

\[
 \operatorname{HeunWI}
 \left(B_1,B_2,B_n^{\mathrm{WI}}(B_1,B_2,q),q;z\right)
 \quad\text{is entire in }z.
\]

Equivalently,

\[
 \boxed{
 \Delta_{\mathrm{WI}}
 \left(B_1,B_2,B_n^{\mathrm{WI}}(B_1,B_2,q),q\right)=0.}
\]

This section must explain the relation between \(\Delta_{\mathrm{WI}}\) and
\(B_n^{\mathrm{WI}}\) in words as well as formulas:

- \(\Delta_{\mathrm{WI}}\) is the entireness defect or characteristic
  quantity as a function of \(B_3\);
- \(B_n^{\mathrm{WI}}\) are its characteristic zeros with respect to \(B_3\);
- \(n\) labels the ordered discrete values and is not inserted into the
  differential equation.

Prove rather than assume discreteness, reality, ordering, multiplicity, and
completeness in the physical Kerr parameter family.  It is acceptable to use
the already proved self-adjointness and compact-resolvent results for the
physical slice of parameter space.  Do not claim these properties for
arbitrary complex \(B_1,B_2,q\) unless proved.

## Part IV — State the HeunWI spectral result before the continued fraction

State the physical result in the clean form

\[
 \boxed{
 E_n=-\frac V2\,
 B_n^{\mathrm{WI}}
 \left(
 \frac{2\overline F}{V},
 \frac{2\hbar\omega_0}{V},
 \frac{2F}{V}
 \right).}
\]

Write the corresponding Bargmann eigenfunction as a normalized entire
`HeunWI` function.

At this point the manuscript must still contain no continued fraction and no
WKB-related concepts.  The principal result must read as a special-function
entireness theorem, not as the vanishing of a continued fraction.

Verify the singular undriven limit \(F\to0\) separately and recover

\[
 E_n^{(0)}
 =\frac V2n(n-1)+\hbar\omega_0n.
\]

Do not substitute \(F=0\) blindly into formulas whose derivation divided by
\(F\), \(\overline F\), \(B_1\), or \(q\).

## Part V — Only now derive recurrence and continued-fraction representations

After Parts I--IV, introduce the power-series recurrence and prove the
equivalence

\[
 \operatorname{HeunWI}\text{ is entire}
 \iff
 \text{the coefficient sequence satisfies the appropriate global condition}
 \iff
 \text{the derived characteristic equation holds}.
\]

Only in this later section may the manuscript introduce Pincherle's theorem,
minimal solutions, Perron--Kreuser theory, or a continued fraction.

Derive the continued fraction with all indices and signs checked:

\[
 E-\cfrac{|F|^2}{
 E-d_1-\cfrac{2|F|^2}{
 E-d_2-\cfrac{3|F|^2}{
 E-d_3-\ddots}}}=0,
\qquad
 d_k=\frac V2k(k-1)+\hbar\omega_0k,
\]

if and only if the derivation confirms exactly this form.

Present it as:

- a derived representation of the condition
  \(\Delta_{\mathrm{WI}}=0\);
- an effective computational formula for the values
  \(B_n^{\mathrm{WI}}\) and energies \(E_n\);
- not the definition of `HeunWI`;
- not the definition of \(\Delta_{\mathrm{WI}}\);
- not the definition of \(B_n^{\mathrm{WI}}\);
- not automatically a new result.

Keep the existing continued-fraction material if correct, but move and
rewrite it to respect this hierarchy.

## Part VI — Historical audit in quantum optics and Kerr cavities

Perform a genuine backward and forward citation search for continued-fraction
methods applied to the coherently driven Kerr or Duffing cavity/oscillator.
Search from the 1970s through the 1990s, with special attention to the 1980s.

At minimum inspect the primary papers themselves, not merely later citations
or search snippets:

1. P. D. Drummond and D. F. Walls, *Quantum theory of optical bistability.
   I. Nonlinear polarisability model*, J. Phys. A 13, 725 (1980);
2. K. Vogel and H. Risken, work on quantum tunnelling and stationary
   solutions in dispersive optical bistability, including Phys. Rev. A 38,
   2409 (1988);
3. K. Vogel, *Quasiprobability distributions in dispersive optical
   bistability*, Phys. Rev. A 39, 4675 (1989);
4. F. Haake, H. Risken, C. Savage, and D. F. Walls, *Master equation for a
   damped nonlinear oscillator*, Phys. Rev. A 34, 3969 (1986);
5. earlier continued-fraction treatments of quantum anharmonic oscillators
   cited by these papers, where relevant;
6. later papers or reviews that explicitly identify the origin of the method.

For each candidate, determine precisely:

- whether the model is the same closed Hamiltonian eigenvalue problem as the
  present manuscript, or an open Lindblad/master-equation problem;
- whether the drive is one-photon coherent driving and whether the
  nonlinearity is Kerr;
- whether the continued fraction is scalar or matrix-valued;
- whether it computes Hamiltonian energies/eigenvectors, stationary
  quasidistributions, Liouvillian eigenvalues, tunnelling rates, correlation
  functions, or another quantity;
- whether its coefficients and boundary condition are algebraically
  identical to the present fraction after a documented parameter map;
- the exact equation and page numbers;
- whether the paper recognizes a Whittaker--Ince/Heun structure.

Do not call two continued fractions "the same" merely because both arise in
Kerr optics.  Conversely, do not claim novelty for the scalar spectral
fraction if an algebraically equivalent formula is found in an earlier
Hamiltonian treatment.

Create a compact evidence table in the stage log with columns:

| Reference | Year | Closed/open | Quantity computed | Scalar/matrix CF | Exact match? | Equation/page |
|---|---:|---|---|---|---|---|

Use cautious manuscript language:

- if the exact scalar spectral fraction is known, cite the earliest verified
  source and present the present result as its HeunWI interpretation;
- if only matrix continued fractions for the dissipative Drummond--Walls
  master equation are found, state that they are historically related but
  mathematically distinct;
- if the search remains incomplete, explicitly say so and remove all novelty
  claims rather than inferring novelty from absence of evidence.

Add verified bibliography entries with DOI, journal, volume, pages, and year.
Do not add a citation that has not been inspected sufficiently to support the
sentence attached to it.

## Part VII — Asymptotics belong later

Preserve the correct large-\(|z|\) balance

\[
 \operatorname{HeunWI}\sim
 \exp\!\left(\pm2\sqrt{-qz}\right)
 z^{1/4-B_2/2},
\]

but place it after the HeunWI, \(\Delta_{\mathrm{WI}}\),
\(B_n^{\mathrm{WI}}\), spectral, and continued-fraction sections, or reserve
it for a separate later section.

Do not use asymptotics, WKB language, Thomé solutions, or Stokes phenomena to
define any of the three author-defined objects.

## Verification

Before finishing:

1. check every displayed equation by direct substitution or symbolic
   residual where appropriate;
2. independently verify the recurrence indices and continued-fraction signs;
3. test several roots numerically against finite Fock-basis diagonalization
   only as validation, not as the derivation;
4. test the entire-solution coefficient decay at those roots and its failure
   away from them;
5. verify the \(F\to0\) spectrum;
6. compile the manuscript from a clean auxiliary-file state;
7. inspect the PDF for broken equations, references, and section order;
8. run `git diff --check`;
9. record commands, outputs, sources, equation numbers, unresolved issues,
   and every manuscript change in the stage log.

## Stop conditions

Stop without forcing the manuscript result if:

- `HeunWI` cannot be defined coherently at \(z=0\) for the claimed parameter
  range;
- no concrete \(\Delta_{\mathrm{WI}}\) can be defined solely from `HeunWI`
  while retaining the claimed zero-set property;
- the coefficient-growth definition fails to characterize entireness;
- the relation between entireness and the continued fraction cannot be
  proved;
- numerical tests contradict the claimed spectrum;
- the historical source cannot be inspected closely enough to support a
  priority statement.

In that event, preserve the existing manuscript, document the exact
obstruction, and propose the smallest rigorous next step.  Do not restore the
continued fraction to the definition of `HeunWI`,
\(\Delta_{\mathrm{WI}}\), or \(B_n^{\mathrm{WI}}\).

## Required deliverables

1. the minimally revised manuscript and compiled PDF;
2. updated verified bibliography;
3. `stage04b_heunwi_characteristic_values.log`;
4. a focused diff;
5. the historical evidence table;
6. a short final report stating:

   - the exact definitions adopted for `HeunWI`,
     \(\Delta_{\mathrm{WI}}\), and \(B_n^{\mathrm{WI}}\);
   - the proof of their relationship;
   - where the continued fraction now appears and what it represents;
   - the earliest verified related and exact-matching quantum-optics uses;
   - which novelty claims were retained, weakened, or removed;
   - all unresolved mathematical or historical issues.
