# Stage 02 literature review: the degenerate DCHE and the Kerr–Bargmann problem

## Scope, conventions, and evidential standard

The equation under review is

\[
 z^2u''+(\gamma_D+\delta_Dz+\epsilon_Dz^2)u'
 +(\alpha_Dz-q_D)u=0,
\]

with \(\gamma_D=2\bar F/V\), \(\delta_D=2\hbar\omega_0/V\),
\(\epsilon_D=0\), \(\alpha_D=2F/V\), and \(q_D=\mathcal E=2E/V\).
No result below changes the factor \(V/2\), the energy scaling, or this
notation.  “Inspected in full” means that the full text available from the
publisher or arXiv was read for the cited result; it does not mean every page
was read.  Search snippets were used only to locate sources, never as evidence.

The principal negative finding is deliberately limited: the same closed
Hamiltonian Bargmann equation, its Taylor recurrence, and a Bargmann–Fock
spectral condition were **not found in the sources and databases searched**.
This is not a claim that they do not exist.

## Canonical DCHE and the parameter mismatch

The NIST DLMF, §31.12(ii), equation 31.12.2, uses

\[
 w''+\left({\delta\over z^2}+{\gamma\over z}+1\right)w'
       +{\alpha z-q\over z^2}w=0.
\]

After multiplication by \(z^2\), this is our family only on the chart
\(\epsilon_D=1\), with
\((\gamma_D,\delta_D,\epsilon_D,\alpha_D,q_D)
=(\delta,\gamma,1,\alpha,q)\).  A scaling \(z=\lambda x\) changes the
constant derivative coefficient to \(\lambda\epsilon_D\); it cannot turn
zero into one.  Thus the project lies outside that normalized chart.  DLMF's
statement that both endpoints have rank 1 applies to its nondegenerate form,
not directly to this hypersurface.  **Access:** §31.12 inspected in full,
online; §31.13 and §31.18 inspected partially.  **Applicability:** after
adaptation for terminology; not direct for endpoint ranks or connection data.

Bühring [1994, pp. 348–370], equation (1.1), treats

\[
z^2f''+z f'+[-a^2z^2+2az(B+1)-2C+2D/z-b^2/z^2]f=0,
\]

and constructs multiplicative solutions (his §2), characteristic exponent
and recurrence, formal solutions at zero and infinity (§3), and connection
coefficients (§§4–6).  A gauge transformation is needed to compare his normal
form to an equation with a first derivative.  His leading \(-a^2z^2\) and
\(-b^2z^{-2}\) terms encode unramified rank-1 irregular behaviour at both
ends.  In our \(\epsilon_D=0\) problem the infinity balance is ramified
(rank \(1/2\) in the Stage 01 convention), so the hypotheses behind his two
rank-1 formal bases fail there.  Setting a leading parameter to zero is a
singular degeneration of his recurrences and connection formulas, not a
verified substitution.  **Access:** full publisher PDF inspected.  Precise
items: (1.1); multiplicative ansatz (2.1) and recurrence (2.3); formal
solutions (3.1)–(3.4); connection relations (4.1)–(4.4); coefficient formulas
in §§5–6.  **Applicability:** only after a new degenerate derivation.

Ronveaux's edited volume (Oxford, 1995) and Slavyanov–Lay (Oxford, 2000) are
standard source families named by DLMF for confluent Heun equations and
singularity-based classification.  Their publisher/catalogue metadata and
tables of contents were checked, but the relevant chapters were paywalled.
No theorem, equation, or page-specific claim from them is used here.
**Access:** partial (front matter/catalogue only). **Applicability:** unresolved
pending full inspection.

## Formal and sectorial theory at irregular singularities

The formal analysis must distinguish four levels:

1. a *formal solution* is an algebraic formal series (possibly with an
   exponential and characteristic power) satisfying the equation coefficient
   by coefficient;
2. an *asymptotic solution* is an actual function admitting that series in a
   specified limiting region;
3. an *analytic solution* solves the ODE on a domain and may have a formal
   asymptotic expansion there;
4. a *convergent series solution* defines an analytic function by convergence.

Formal exponential factors and characteristic powers come from dominant
balance after normal-form reduction.  Fractional powers require a ramified
cover.  Actual solutions asymptotic to formal ones generally exist only in
sectors; crossing singular directions changes subdominant coefficients by
Stokes multipliers.  Authors interchange “Stokes” and “anti-Stokes” for curves
where exponent differences are respectively oscillatory or have equal real
part.  Every later use must state the adopted convention.

Olver, *Asymptotics and Special Functions*, 1997 A K Peters reprint of the
1974 text, has the relevant material in Chapter 7, “Differential Equations
with Irregular Singularities; Bessel and Confluent Hypergeometric Functions,”
and Chapter 13, “Connection Formulas for Solutions of Differential
Equations.”  The publisher table of contents and edition metadata were
verified, but theorem-level text was not accessible in this search.  It would
be unsafe to invent theorem numbers or claim that an unramified theorem covers
the ramified infinity.  **Access:** partial. **Required manual check:** exact
§§ and theorem numbers for existence of analytic sectorial representatives,
sector widths, branch hypotheses, and Stokes continuation.

Fedoryuk, *Asymptotic Analysis: Linear Ordinary Differential Equations*,
English translation by A. Rodick, Springer, 1993, has Part I, Chapter 1,
§3 “Irregular Singular Points”; Part II, Chapter 2, §§3–4 for polynomial and
meromorphic coefficients in the complex plane; and later chapters on multiple
and fractional turning points.  The accessible preview explicitly says that
his “Stokes line” equals “anti-Stokes line” in physics usage.  The preview did
not expose theorem numbering or enough hypotheses for a theorem-level
application.  **Access:** partial. **Required manual check:** theorem numbers,
the independent-variable versus large-parameter setting, and whether the
fractional/ramified results cover the project’s \(z^{1/2}\) exponential scale.

Consequently, the local classifications established in Stage 01 are
consistent with general formal theory, but neither Olver nor Fedoryuk is cited
here as a proved, directly applicable existence theorem.  That is an
essential outstanding source check.

## Multiplicative solutions, recurrences, and connection problems

Bühring's multiplicative (Floquet-type) solution has a bilateral Laurent
series multiplied by a characteristic power.  Its characteristic exponent is
fixed by convergence/minimality of a recurrence; the paper also relates this
quantity to connection coefficients.  These are established prior methods
for generic DCHEs.  They do not automatically produce an entire function at
the project’s irregular origin or a Bargmann–Fock vector at infinity.

Leaver (1986) develops series and continued-fraction spectral methods for the
generalized spheroidal wave equation and physical boundary conditions.  The
method is highly relevant by analogy: a three-term recurrence has two
asymptotic branches, a minimal branch can be characterized by a continued
fraction, and a boundary condition yields a characteristic equation.  His
equation and boundary conditions are not this Kerr equation.  **Access:**
partial (publisher metadata and accessible text portions); **applicability:**
methodological analogy only.

El-Jaick and Figueiredo (2008), especially §§2–4, derive series solutions of
CHEs, a Leaver limit to the DCHE, and Whittaker–Ince limits.  Their 2013 paper
gives one-sided and two-sided Coulomb-wave series, coefficient recurrences,
convergence domains, and explicit limiting routes.  Both arXiv full texts were
inspected.  Their terminology “Whittaker–Ince limit” denotes a simultaneous
parameter limit in a specified source equation; it is **not** the statement
that one coefficient happens to vanish.  No verified map makes our lone
condition \(\epsilon_D=0\) equal to that limit.  **Applicability:** after an
explicit new transformation/limit, if one can be derived; currently not
direct.

Ishkhanyan et al. (2014) use a DCHE normalization and construct confluent-
hypergeometric expansions whose coefficients obey three-, five-, or
seven-term recurrences; finite sums require termination conditions.  The
arXiv full text was inspected.  Its generic expansions assume the source
normalization and do not establish Bargmann entire/Fock conditions on our
degenerate chart.  **Applicability:** after adaptation; termination results
are not an energy condition for this Hamiltonian without a parameter map and
endpoint analysis.

For the Kerr equation itself, insertion of
\(\Psi(z)=\sum_{n\ge0}c_nz^n\) gives, algebraically,

\[
\bar F(n+1)c_{n+1}+
\left[{V\over2}n(n-1)+\hbar\omega_0n-E\right]c_n+Fc_{n-1}=0,
\quad c_{-1}=0.
\]

This derivation is elementary and must not be claimed as novel.  For
\(F\ne0\), prescribing \(c_0\) determines every subsequent coefficient
through the recurrence and hence determines the local analytic germ; the
nonzero solutions are unique up to overall normalization, while \(c_0=0\)
gives the zero solution.  What remains nonlocal is whether the entire
continuation belongs to Bargmann–Fock space; a formal or recurrence-minimal
solution alone does not establish that.

## Segal–Bargmann/Fock requirements

Bargmann (1961), Part I, defines the Hilbert space of entire functions with a
Gaussian norm, proves the integral-transform realization, and identifies the
holomorphic creation/annihilation actions.  **Access:** partial full-text
inspection plus authoritative Wiley metadata; equations needed for the space
and transform were checked.  **Applicability:** direct to the representation,
after matching the manuscript’s normalization.

Membership in the one-variable Bargmann–Fock space is

\[
\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,{d^2z\over\pi}<\infty,
\]

equivalently \(f(z)=\sum c_nz^n\) with
\(\sum n!|c_n|^2<\infty\).  Local analyticity at zero supplies a germ; analytic
continuation across every finite point supplies an entire function; neither
alone implies the weighted norm.  A global growth estimate, coefficient
criterion, or connection/Stokes condition is still needed.  Fock membership
imposes growth no worse than order two with the critical type controlled
directionally; crude order/type statements at the boundary are not by
themselves equivalent to the norm.

## Closed Kerr prior art and physically related open systems

Targeted searches covered exact strings and algebraically equivalent forms of
the Hamiltonian, ODE, “double confluent Heun,” “Bargmann,” “continued
fraction,” and the three-term recurrence.  No inspected source gave the same
closed stationary problem and the same DCHE reduction or Fock spectral
condition.  This is only a negative result for the routes logged below.

Drummond and Walls (1980) solve a driven **dissipative** optical-bistability
model by an exact steady-state generalized-\(P\) distribution.  Roberts and
Clerk (2020) give exact steady states for driven-dissipative Kerr resonators
using a Segal–Bargmann construction.  These are valuable physical neighbours,
but their Liouvillian/non-Hermitian steady-state equations are not the closed
self-adjoint Schrödinger eigenproblem.  Neither can be cited as solving the
present spectrum.  **Access:** Drummond–Walls partial; Roberts–Clerk full
arXiv text. **Applicability:** physically related, mathematically different.

## Comparison table

| Source | Equation/class | Local behaviour at zero | Behaviour at infinity | Recurrence/continued fraction | Connection or Stokes data | Relation to \(\epsilon_D=0\) | Kerr–Bargmann relevance | Status |
|---|---|---|---|---|---|---|---|---|
| DLMF §31.12 | normalized DCHE | rank 1 | rank 1 | pointers only | pointers only | normalization excludes zero constant derivative coefficient | taxonomy and map | adaptation |
| Bühring 1994 | normal-form DCHE | unramified rank 1 | unramified rank 1 | bilateral recurrence/characteristic exponent | explicit connection coefficients | singular degeneration at infinity | method, not result | adaptation only |
| Olver 1997 | general asymptotic ODE theory | formal/sectorial framework | formal/sectorial framework | not DCHE-specific | Stokes/connection theory | ramified hypotheses need checking | foundation | manual inspection required |
| Fedoryuk 1993 | asymptotic linear ODEs | irregular-point theory | large-argument complex theory | not DCHE-specific | Stokes geometry | fractional case needs checking | foundation | manual inspection required |
| Slavyanov–Lay 2000 | singularity classification | generic | generic | generic | generic | chapter inaccessible | contextual | unresolved |
| Ronveaux 1995 | Heun family | generic DCHE | generic DCHE | source-family methods | source-family methods | chapter inaccessible | contextual | unresolved |
| Leaver 1986 | generalized spheroidal | equation-specific | radiative/asymptotic BC | three-term CF | physical connection problem | no direct map | methodological analogy | analogy only |
| El-Jaick–Figueiredo 2008/2013 | CHE/DCHE and limits | series domains specified | series domains specified | three-term series recurrences | via overlapping series | Whittaker–Ince is a precise limit, not \(\epsilon_D=0\) | possible adapted basis | adaptation only |
| Ishkhanyan et al. 2014 | normalized DCHE | hypergeometric series | convergence analyzed | 3/5/7-term; termination | not Kerr Stokes data | no verified direct specialization | possible computational basis | adaptation only |
| Bargmann 1961 | holomorphic Fock representation | entire functions | Gaussian-norm growth | coefficient norm | not DCHE data | independent | direct Hilbert-space criterion | direct |
| Drummond–Walls 1980 | dissipative Kerr steady state | generalized-\(P\) | phase-space tails | moment relations | none for closed ODE | none | physical neighbour | not applicable |
| Roberts–Clerk 2020 | Lindblad Kerr resonator | Segal–Bargmann auxiliary states | open-system normalizability | exact recursion/construction | open-system data | none | physical/methodological neighbour | not applicable |

## Established prior results

- Generic DCHE multiplicative solutions, characteristic exponents, formal
  endpoint solutions, and connection formulas are established in Bühring.
- General irregular-singularity theory distinguishes formal expansions from
  sectorial analytic representatives and supplies Stokes phenomena, subject
  to theorem hypotheses still to be checked precisely in Olver/Fedoryuk.
- Three-term recurrence, minimal-solution, continued-fraction, and connection
  methods are established techniques; Leaver is a prominent physical use.
- The Segal–Bargmann representation and Gaussian Hilbert norm are classical.
- Exact driven-dissipative Kerr steady states exist, but solve a different
  mathematical problem.

## Results requiring adaptation to epsilon_D = 0

- Bühring's two rank-1 endpoint bases and all connection coefficients built
  from them.
- DLMF's normalized DCHE endpoint-rank statement.
- Coulomb/hypergeometric expansions and their continued fractions from generic
  DCHE conventions.
- Any identification with a Whittaker–Ince limit.
- Sectorial existence theorems whose stated hypotheses assume integral rank or
  an unramified independent variable.

## Apparently open questions relevant to this project

Within the sources and databases searched, the following remain unresolved:
an explicit degenerate connection problem between the analytic germ at zero
and ramified infinity; an equivalence between Fock normalizability and a
minimal/continued-fraction condition; and global zero/modulus geometry for
closed Kerr eigenfunctions.  “Open” here means apparently open after this
bounded search, not a priority claim.

## Claims we must not present as novel

- Standard local formal theory at an irregular singular point, including
  exponential factors, characteristic powers, sectorial solutions, and Stokes
  multipliers.
- The elementary derivation of the displayed Taylor recurrence.
- Standard DCHE multiplicative/Floquet solutions and characteristic exponents.
- Known connection-formula, three-term-recurrence, minimal-solution, and
  continued-fraction methods.
- The Segal–Bargmann realization and coefficient/norm criterion.

## Candidate contributions of the present work

Subject to the manual checks below, useful contributions may be: selecting the
entire solution by the Bargmann condition on the degenerate chart; converting
Fock normalizability into explicit connection/Stokes/minimal-solution data; a
validated continued-fraction energy condition without direct Hamiltonian
diagonalization; and global zero and modulus-level-set geometry and its
parameter dependence.  None is claimed novel on present evidence.

## Unresolved questions requiring manual source inspection

1. Inspect the physical 1997 Olver edition and record exact Chapter 7 and 13
   section/theorem numbers, hypotheses, sector widths, and ramification rules.
2. Inspect the 1993 Springer Fedoryuk translation and record exact theorem
   numbers for irregular points, sectorial actual solutions, Stokes curves,
   and fractional behaviour.
3. Inspect the DCHE chapters of Ronveaux and Slavyanov–Lay, including
   D. Schmidt and G. Wolf, “The double confluent Heun equation,” in *Heun's
   Differential Equations*, edited by A. Ronveaux.  Bühring cited this chapter
   as forthcoming with a 1994 date, whereas the published Ronveaux volume is
   dated 1995; its final year, title, authors, and page range must be checked
   against the published volume or an authoritative table of contents before
   adding a bibliography entry.
4. Derive (rather than assume) any limiting map from Bühring, Leaver, or
   El-Jaick–Figueiredo to \(\epsilon_D=0\), and check recurrence convergence.
5. Extend the closed-Kerr prior-art search to subscription databases and cited-
   reference chains unavailable here, especially older quantum-optics papers.

Because items 1–3 are essential to the requested theorem-level audit, this
Stage 02 review is a documented, validated partial result and **must not yet be
treated as complete**.
