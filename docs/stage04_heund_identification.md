# Stage 04: `HeunD` identification audit and stopping obstruction

## Status

This stage stopped at the source-verification gate required by
`prompts/04_heund_entire_spectral_condition.md`.  It does **not** establish a
formula for the physical eigenfunction in terms of a standard computer-algebra
`HeunD`, and it does **not** identify the spectrum with a standard Heun
characteristic value.

The stopping rule is substantive.  The exact defining differential equation,
parameter order, distinguished normalization, and domain of applicability must
all be verified for every convention before a conversion table can be used.
Those data could not be recovered from all mandatory primary sources.

## Sources that could be verified

### DLMF

NIST DLMF §31.12(ii), equation 31.12.2, inspected on 2026-07-23, defines the
doubly-confluent Heun equation as

\[
 w''+\left(\frac{\delta}{z^2}+\frac{\gamma}{z}+1\right)w'
 +\frac{\alpha z-q}{z^2}w=0.
\]

Equivalently,

\[
 z^2w''+(\delta+\gamma z+z^2)w'+(\alpha z-q)w=0.
\]

DLMF states that this normalized equation has rank-one irregular
singularities at both zero and infinity.  The coefficient of \(z^2w'\) is
fixed to one.  A nonzero scaling of the independent variable changes that
coefficient by a nonzero factor and therefore cannot map the Kerr value zero
to the DLMF value one.

Primary location:
<https://dlmf.nist.gov/31.12.E2>.

### Bühring

W. Bühring, “The double confluent Heun equation: characteristic exponent and
connection formulae,” *Methods and Applications of Analysis* **1** (1994),
348–370, was inspected in the full publisher PDF.

Equation (1.1) is a normal-form equation with two unramified rank-one
irregular endpoints.  The abstract and §1 explicitly state that scope.
Bühring's multiplicative solutions and characteristic exponent therefore
belong to the generic two-rank-one problem.  The Kerr equation has a ramified
rank-\(1/2\) infinity when \(F\ne0\), as already derived in the manuscript.
Consequently Bühring's characteristic-exponent and connection formulae cannot
be specialized merely by setting a leading rank-one parameter to zero.

Primary PDF:
<https://www.intlpress.com/site/pub/files/_fulltext/journals/maa/1994/0001/0003/MAA-1994-0001-0003-a006.pdf>.

### Oxford metadata for Ronveaux

The authoritative Oxford record verifies:

- A. Ronveaux (editor), *Heun's Differential Equations*;
- Oxford University Press, 1995;
- print ISBN 978-0-19-859695-0;
- DOI 10.1093/oso/9780198596950.001.0001;
- Part C, “Double confluent Heun equation,” including “General features of
  the DCHE,” “The analytic theory of the DCHE,” and “Special results.”

The chapter text, its symmetric canonical equation, equation numbers,
parameter order, and hypotheses were not accessible.  The table of contents
is not sufficient evidence for a parameter conversion or theorem.

Authoritative record:
<https://academic.oup.com/book/54034>.

## Mandatory conventions that could not be verified

### Ronveaux/Schmidt–Wolf symmetric convention

The relevant Part C chapter was behind Oxford access control.  Attempts to
open the chapter pages did not return the primary text.  Therefore its exact
symmetric canonical equation and distinguished solutions remain unverified.

### Maple `HeunD`

Searches of the official Maplesoft help site did not resolve an authoritative
`HeunD` help page containing the defining equation and normalization.  General
Maple help and product pages are not substitutes for the function definition.
No formula from memory or a secondary page was used.

### Wolfram Language `HeunD`

The official page verifies the syntax

\[
\operatorname{HeunD}(q,\alpha,\gamma,\delta,\epsilon,z)
\]

and states that the function is a normalized power-series solution of a
double-confluent Heun equation.  However, on the accessible official page the
defining differential equation, series, and two normalization conditions are
embedded as image files.  Attempts to retrieve those four primary image
resources failed.  The exact formulas therefore remain unverified.

Official page:
<https://reference.wolfram.com/language/ref/HeunD.html>.

## Algebraic audit possible without naming a standard `HeunD`

Starting from

\[
 \frac V2z^2\Psi''+(\hbar\omega_0z+\overline F)\Psi'
 +(Fz-E)\Psi=0,
\]

multiplication by \(2/V\) gives

\[
 z^2\Psi''+(\beta+\alpha z)\Psi'
 +(\gamma z-\mathcal E)\Psi=0,
\]

where

\[
\alpha=\frac{2\hbar\omega_0}{V},\qquad
\beta=\frac{2\overline F}{V},\qquad
\gamma=\frac{2F}{V},\qquad
\mathcal E=\frac{2E}{V}.
\]

Thus the broader five-coefficient family written in the manuscript has
\(\varepsilon_{\rm D}=0\).  It is algebraically a degenerate DCHE-family
equation under that explicitly declared convention, but it is not in the
normalized DLMF chart, which fixes \(\varepsilon_{\rm D}=1\).  This audit does
not identify a standard normalized `HeunD` function.

Direct insertion of

\[
\Psi(z)=\sum_{k\ge0}c_kz^k
\]

gives

\[
\overline F(k+1)c_{k+1}
+\left[\frac V2k(k-1)+\hbar\omega_0k-E\right]c_k
+Fc_{k-1}=0,\qquad c_{-1}=0.
\]

In particular, \(\overline F c_1=Ec_0\).  This recurrence is an exact
algebraic check, but the present stopped audit does not promote its minimal
solution to a proved necessary-and-sufficient spectral condition: doing that
requires the convergence/minimality and Bargmann-norm theorem demanded by the
prompt.

For \(F=0\), direct substitution gives the Euler equation and

\[
E_n^{(0)}
=\frac V2n(n-1)+\hbar\omega_0n,\qquad n\in\mathbb N_0.
\]

No driven `HeunD` condition was established, so no claim about its
\(F\to0\) limit is made.

## Conversion table: verified extent only

| Convention | Canonical derivative coefficient | Endpoint type | Conversion status |
|---|---:|---|---|
| Manuscript's explicitly defined broad family | \(\gamma_D+\delta_Dz+\varepsilon_Dz^2\), with \(\varepsilon_D=0\) | rank 1 at zero; ramified rank \(1/2\) at infinity for \(F\ne0\) | direct algebraic identity |
| DLMF 31.12.2 | \(\delta+\gamma z+z^2\) | rank 1 at both endpoints | Kerr equation is outside this normalized chart |
| Bühring (1.1), after a gauge map | generic normal form with two nonzero rank-one endpoint scales | rank 1 at both endpoints | singular degeneration; published generic formulae not directly applicable |
| Ronveaux/Schmidt–Wolf | primary equation inaccessible | unverified here | conversion forbidden |
| Maple `HeunD` | official definition not recovered | unverified here | conversion forbidden |
| Wolfram `HeunD` | official equation/normalization images unavailable | official page says origin is singular and normalization is elsewhere | conversion forbidden |

## Consequence for the spectral claim

No source-verified basis was obtained for any assertion of the form

\[
\Psi_E=G\,\operatorname{HeunD}(\ldots),\qquad
\mathcal Q(E)=n.
\]

In particular, Bühring's characteristic exponent is not an integer
quantization rule for this ramified degeneration on the evidence inspected.
The integer \(n\) in the undeformed Euler problem is a monomial exponent; it
must not be transferred to the driven problem without a theorem.

The next legitimate step is to obtain the full primary Ronveaux chapter and
the exact official Maple and Wolfram definitions (including normalization and
exceptional-parameter restrictions).  Only then can the requested symbolic
substitution, complete conversion table, and comparison with a rigorously
proved recurrence/Wronskian characteristic function be completed.
