# Global Olver--Weber connection: domain audit and obstruction

## Decision

**Outcome C (obstruction remains).**  The full coefficient can be absorbed
in a locally valid, parameter-dependent Weber map, and its origin endpoint
can be expanded exactly.  What is not available is a one-to-one comparison
domain, or a proved finite chain of comparison domains, carrying the
compensated origin germ through the relevant sheet continuation.  Hence no
physical Olver connection coefficient, small connection error, or zero
localization theorem is claimed.

## Exact coefficient and complete turning-point inventory

Put

\[
 Q_u=f+u^{-1}g+u^{-2}h,
 \quad e=-\frac32+\frac{e_1}{u}+O(u^{-2}),
 \quad c_h=4\delta^2-4\delta+\frac34.
\]

Apart from the pole of order six at (x=0), its zeros are the square roots
of the three roots of

\[
 P_u(y)=1-\frac{2(1-\delta)}u y+
 \left(2e+\frac{c_h}{4u^2}\right)y^2-2y^3.
\]

Writing (q=u^{-1/2}), the roots near the double root are

\[
 y_\pm=-1\pm vq+wq^2+O(q^3),\qquad
 v^2=\frac23(\delta-1-e_1),\qquad
 w=\frac{-\delta+4e_1+1}{9}.
\]

Each has two square roots.  On the branch near (i),

\[
 x_{\pm,i}=i\left[1\mp\frac v2q-
 \left(\frac w2+\frac{v^2}{8}\right)q^2+O(q^3)\right],
\]

and their negatives form the sheet-related pair near (-i).  The remaining
root and its two square roots are

\[
 y_s=\frac12+\frac{2\delta+e_1-2}{9u}+O(u^{-2}),\qquad
 x_{s,\pm}=\pm\frac1{\sqrt2}left[1+
 \frac{2\delta+e_1-2}{9u}+O(u^{-2})\right].
\]

Thus all six zeros have been retained.  In the original cover
(t=u^{1/4}x), and in the Bargmann plane (z=t^2=u^{1/2}y).  The two
near-(i) roots and the two near-(-i) roots therefore project pairwise to
the same two negative-(z) turning points, while the simple pair projects to
one positive-(z) turning point.  The pole is (t=z=0).

At (u=\infty), the quadratic differential (f(x),dx^2) has double zeros
at (x=\pm i), simple zeros at (x=\pm1/\sqrt2), a pole of order six at
zero, and a regular nonzero limit at infinity.  Stokes curves are the level
curves on which the real part of an action difference is constant; their
labels depend on the chosen square-root sheet.  A half-turn (x\mapsto-x)
exchanges the two covering sheets and the two formal origin exponentials.
The local data and the negative classical displacement do not decide which
global chain realizes Bargmann continuation.

## Local full-coefficient Weber map

Choose one split pair near (i), call it (\alpha_u,\beta_u), and a simply
connected neighbourhood cut away from zero, the other four zeros, and a
curve joining the selected pair.  Fix (\sqrt{Q_u}) there and define

\[
 \int_{\alpha_u}^x\sqrt{Q_u(s)}\,ds
 =\int_{-a_u}^{\zeta}\sqrt{v^2-a_u^2}\,dv,
 \qquad
 \frac{\pi i}{2}a_u^2
 =\int_{\alpha_u}^{\beta_u}\sqrt{Q_u(s)}\,ds.
\]

The sign of the last equation reverses if either integration orientation or
one square-root branch is reversed.  With the displayed compatible
orientation it maps the selected endpoints to (-a_u,+a_u).  The action is
single-valued only on the cut local domain; it has not been shown
single-valued on a domain joining the required origin sectors.

For (W=(d\zeta/dx)^{1/2}w), direct differentiation gives

\[
 W_{\zeta\zeta}=\{u^2(\zeta^2-a_u^2)+\psi_u(\zeta)\}W,
 \qquad
 \psi_u=\left(\frac{dx}{d\zeta}\right)^{1/2}
 \frac{d^2}{d\zeta^2}
 \left(\frac{dx}{d\zeta}\right)^{-1/2}.
\]

If (p=d\zeta/dx), the correction is exactly

\[
 p^{-1/2}\frac{d^2}{d\zeta^2}p^{1/2}
 =-\frac34p^{-4}p_x^2+\frac12p^{-3}p_{xx}.
\]

Consequently no order-(u) term remains.  The symbolic verifier checks both
identities.  This repairs the local comparison but does not enlarge its
domain.

With (Z=\sqrt{2u}\,\zeta), the comparison equation becomes

\[
 W_{ZZ}=\left(\frac{Z^2}{4}-p_u-\frac12\right)W,
 \qquad p_u+\frac12=\frac{u a_u^2}{2}.
\]

## Endpoint audit

In any fixed punctured sector at zero, with a fixed logarithm and the branch
whose leading square root is (2x^{-3}),

\[
 \sqrt{Q_u(x)}=\frac2{x^3}-\frac{2(1-\delta)}{u x}+O(x),
\]

uniformly for fixed (\delta,e_1) in compact sets.  Hence

\[
 \int^x\sqrt{Q_u(s)}\,ds=-\frac1{x^2}
 -\frac{2(1-\delta)}u\log x+O(1).
\]

Changing the square-root branch changes the signs; changing the logarithm
adds the expected constant.  The Weber action satisfies

\[
 \int^\zeta\sqrt{v^2-a_u^2}\,dv
 =\frac{\zeta^2}{2}-\frac{a_u^2}{2}\log\zeta+O(1).
\]

Thus (\zeta^2\sim-2/x^2), so (\zeta\sim\pm i\sqrt2/x), with the sign
and ray fixed sector by sector.  The two exponentials
(\exp(\pm u\zeta^2/2)) reproduce the two signs of the essential factor
(\exp(\mp u/x^2)).  This exponential correspondence alone does not
identify the compensated Bargmann germ: its algebraic power also contains
the logarithmic action, the Liouville prefactor, the earlier gauge, and the
cover (z=t^2).  Their global monodromy cannot be fixed until the sector
chain and its transition branches are fixed.

At infinity,

\[
 \sqrt{Q_u(x)}=\sqrt{-8}\left[1-
 \left(\frac e2+\frac{c_h}{16u^2}\right)x^{-2}+O(x^{-4})\right],
\]

so the action is (\sqrt{-8}\,x+O(x^{-1})) and
(\zeta^2/2\sim\sqrt{-8}\,x).  Therefore both (x=0) and (x=\infty)
map to (different sectors of) (\zeta=\infty).  Together with the excluded
simple turning points, this prevents treating the asserted origin--turning
pair--infinity region as one already proved one-to-one Weber domain.  Outer
Bessel matching is not needed for the local endpoint calculation and cannot
repair origin entireness by itself.

## Exact model connection formula, and why it is not yet physical

DLMF 12.2.5 gives (D_p(Z)=U(-p-1/2,Z)).  DLMF 12.2.19 states

\[
 U(a,Z)=\pm i e^{\pm i\pi a}U(a,-Z)
 +\frac{\sqrt{2\pi}}{\Gamma(1/2+a)}
 e^{\pm i\pi(a/2-1/4)}U(-a,\pm iZ).
\]

Putting (a=-p-1/2) makes the second coefficient proportional to
(1/\Gamma(-p)), whose zeros are (p=0,1,2,\ldots).  DLMF 12.2.4 verifies
the differential-equation convention, and DLMF 12.2.11 gives the associated
Wronskian.  These formulas are authoritative exact facts about the model.
They cannot be assigned to the compensated and essential Bargmann branches
until the missing domain chain fixes all rotations, endpoint sectors,
normalizations, and gauge monodromy.

## First failed hypothesis and minimal missing lemma

The first failure occurs before a Volterra estimate: the comparison map has
not been proved univalent on a simply connected domain containing the
selected pair and approaching both required origin sectors.  Olver,
*Asymptotics and Special Functions*, Chapter 12, Sections 1--4, treats two
coalescing turning points once the appropriate comparison domains and
progressive paths exist; it does not by citation alone supply them across
this pole endpoint and the additional turning points.  DLMF 2.8(vi) likewise
identifies parabolic-cylinder approximants for two coalescing turning points,
not this global domain.

The minimal missing result is a **domain-chain lemma**: construct finitely
many overlapping canonical domains (Weber near one selected coalescence,
Airy near any simple turning point that the physical continuation must
cross, and pole/outer domains at the ends), prove their action maps are
univalent, exhibit progressive paths with uniform endpoint limits, and
bound every transition operator by (o(1)), uniformly for fixed level and
(\delta) in a stated compact set.  It must also track the half-turn sheet
exchange and the full gauge/cover monodromy.  Only then can a coefficient

\[
 \mathcal C=A/\Gamma(-p_u)+\mathcal R
\]

be derived, rather than postulated, and only an explicit
(\mathcal R=o(1)) would permit a Rouch\'e localization argument.

No such bound is presently proved.  The formal fixed-level energy formula

\[
 \frac{E_n}{V}=-\frac32\eta^{4/3}
 +\left[\delta+\sqrt3\left(n+\frac12\right)-1\right]\eta^{2/3}
 +O(1)
\]

therefore retains its earlier status: the first coefficient is rigorous,
while the second is conditional on the global connection identification.
The exact determinant (\Delta_{\rm WI}=0) remains an independent
entireness result; no equality or asymptotic equality of its zeros with an
Olver coefficient has been established here.

## Sources

- F. W. J. Olver, *Asymptotics and Special Functions*, Chapter 12,
  Sections 1--4 (two coalescing turning points and comparison domains).
- NIST DLMF 12.2.4, 12.2.5, 12.2.11, and 12.2.19 (Weber equation,
  (D_p)--(U) convention, Wronskian, and exact connection formula).
- NIST DLMF 2.8(vi) (classification of two coalescing turning points).

