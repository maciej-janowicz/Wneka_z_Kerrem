# Stage 04a: Whittaker--Ince limit and the Bargmann spectral condition

## 1. Result in brief

For \(F\ne0\), the normalized Kerr Bargmann equation is exactly the
Whittaker--Ince limit of the double-confluent Heun equation in the
Leaver--Figueiredo convention:

\[
 z^2U''+(B_1+B_2z)U'+(B_3+qz)U=0,
\]

with

\[
 B_1=\frac{2\overline F}{V},\qquad
 B_2=\frac{2\hbar\omega_0}{V},\qquad
 B_3=-\frac{2E}{V},\qquad
 q=\frac{2F}{V}.
\]

The physical energy condition is not an integer characteristic exponent.
It is compatibility of the \(k=0\) Taylor relation with the unique minimal
solution of the three-term recurrence.  Pincherle's theorem converts that
compatibility into an infinite continued fraction.  The integer \(n\) only
labels the ordered real roots.

## 2. Primary-source convention and limit

El-Jaick and Figueiredo, arXiv:0807.2219v3, equations (1), (3), (5), and (7),
use the confluent Heun equation

\[
 z(z-z_0)U''+(B_1+B_2z)U'
 +[B_3-2\eta\omega(z-z_0)+\omega^2z(z-z_0)]U=0.
\]

The Leaver limit \(z_0\to0\) gives their DCHE,

\[
 z^2U''+(B_1+B_2z)U'
 +(B_3-2\eta\omega z+\omega^2z^2)U=0,
\qquad B_1\ne0,\quad\omega\ne0.
\]

Their Whittaker--Ince limit is

\[
\omega\to0,\qquad \eta\to\infty,\qquad 2\eta\omega=-q
\quad\hbox{fixed},
\]

and yields their equation (7),

\[
 z^2U''+(B_1+B_2z)U'+(B_3+qz)U=0.
\]

The same parent and limiting prescription are stated in El-Jaick and
Figueiredo, arXiv:1209.4673v2, equations (1)--(3).  Figueiredo's original
paper, *Journal of Mathematical Physics* **46**, 113503 (2005), DOI
10.1063/1.2104267, derives the same limit and supplies the earlier solution
families.

This is a singular parameter limit, not merely the substitution
\(\omega=0\): the product \(2\eta\omega\) remains finite.  Nor is it literally
the statement \(\varepsilon_{\rm D}=0\) in the broad coefficient convention
previously defined in the manuscript.  In the Leaver--Figueiredo parent,
\(\omega\) occurs in the potential term, not as a coefficient of \(z^2U'\).
The manuscript's \(\varepsilon_{\rm D}=0\) is an algebraic description of the
resulting differential equation; the Whittaker--Ince prescription supplies
its exact genealogy.

The limit changes infinity from an unramified rank-one irregular point with
\(e^{\pm i\omega z}\) behaviour to a subnormal, ramified rank-\(1/2\) point
with square-root exponentials.  The ramification is therefore expected and
does not place the limiting equation outside the confluent-Heun hierarchy.

## 3. Direct Kerr parameter map

Multiplication of

\[
 \frac V2z^2\Psi''
 +(\hbar\omega_0z+\overline F)\Psi'
 +(Fz-E)\Psi=0
\]

by \(2/V\) gives the limiting equation with the parameter map displayed in
§1.  A symbolic residual calculation returned zero identically.

For physical parameters,

\[
qB_1=\frac{4|F|^2}{V^2}>0
\]

when \(F\ne0\).  Thus the limiting equation satisfies the nonzero \(B_1q\)
condition used in the generic driven analysis.  The phase of \(F\) has not
been treated as independent of \(\overline F\).

## 4. Dominant balance at infinity

Insert

\[
U=e^{\sigma z^{1/2}}z^\rho(1+O(z^{-1/2}))
\]

with a fixed branch of \(z^{1/2}\).  The coefficients at orders \(z\) and
\(z^{1/2}\) give

\[
\frac{\sigma^2}{4}+q=0,\qquad
\sigma\left(\rho-\frac14+\frac{B_2}{2}\right)=0.
\]

For \(q\ne0\),

\[
\sigma=\pm2\sqrt{-q},\qquad
\rho=\frac14-\frac{B_2}{2},
\]

and hence

\[
 U(z)\sim
 e^{\pm2\sqrt{-qz}}z^{1/4-B_2/2}.
\]

This agrees with the subnormal Thomé behaviour stated for the
Whittaker--Ince limit in the cited Figueiredo papers.  It is a sectorial
formal description; it does not make an exact entire solution multivalued.

## 5. Published expansion families

Section 4.2 of arXiv:0807.2219v3 gives solutions for the Whittaker--Ince
limit of the DCHE.  Section 2.4 of arXiv:1209.4673v2 gives the enlarged
two-sided and one-sided families and convergence discussion.

A representative two-sided Bessel family is equation (222a) of the latter:

\[
 U_1^{(j)}(z)=z^{(1-B_2)/2}
 \sum_{m=-\infty}^{\infty}(-1)^m c_m
 Z_{2m+2\nu+1}^{(j)}(2\sqrt{qz}),
\]

where \(Z^{(j)}\) denotes a selected Bessel-cylinder solution.  Its
coefficients obey

\[
\alpha_m c_{m+1}+\beta_m c_m+\gamma_m c_{m-1}=0,
\]

with the explicit rational coefficients in equation (222e).  Companion
families (223a), (223c), and (224) include an \(e^{B_1/z}\) family and a
confluent-hypergeometric family.  The paper states the exceptional values of
\(\nu\) that must be excluded when recurrence denominators vanish, and
explains how one-sided families arise by left termination.

These published expansions establish the exact special-function
classification and useful representations on their stated domains.  They do
not by themselves identify the Kerr Bargmann eigenfunction: a generic
two-sided Bessel series is organized around a characteristic exponent
\(\nu\), while the Bargmann problem demands the Taylor relation at the
irregular origin and a Gaussian Hilbert norm.  No integer-\(\nu\) rule is
imported into the physical problem.

For the Bargmann solution, the direct Taylor representation is both simpler
and global once its recurrence is minimal.  It is therefore used below rather
than forcing the physical state into one of the two-sided Bessel notations.

## 6. Taylor recurrence and its two asymptotic branches

Write

\[
\Psi(z)=\sum_{k=0}^\infty c_kz^k,\qquad c_{-1}=0.
\]

Coefficient extraction gives

\[
\overline F(k+1)c_{k+1}
+[d_k-E]c_k+Fc_{k-1}=0,
\]

where

\[
d_k=\frac V2k(k-1)+\hbar\omega_0k.
\]

At \(k=0\),

\[
\overline F c_1=Ec_0.
\]

If \(F\ne0\), \(c_0=0\) forces every coefficient to vanish, so every nonzero
solution can be normalized by \(c_0=1\).

After division by \(\overline F(k+1)\), the recurrence is in the form used by
Gautschi, §2.  Its coefficients have powers \(a_k\sim
(V/2\overline F)k\) and \(b_k\sim(F/\overline F)k^{-1}\).  The
Perron--Kreuser theorem quoted as Gautschi's Theorem 2.3(a) therefore gives
two independent asymptotic branches:

\[
\frac{c_{k+1}^{\rm dom}}{c_k^{\rm dom}}
\sim-\frac{V}{2\overline F}k,
\qquad
\frac{c_k^{\min}}{c_{k-1}^{\min}}
\sim-\frac{2F}{V}\frac1{k^2}.
\]

Substitution of
\[
\frac{c_k^{\min}}{c_{k-1}^{\min}}
=-\frac{2F}{V}k^{-2}(1+b/k+O(k^{-2}))
\]
back into the exact recurrence gives
\[
b=1-B_2=1-\frac{2\hbar\omega_0}{V}.
\]
Consequently,
\[
c_k^{\min}
=C\,\frac{(-2F/V)^k}{(k!)^2}
k^{\,1-B_2}(1+O(k^{-1}))
\]
up to a nonzero normalization constant and the standard interpretation of
the accumulated power correction.

The dominant branch has factorial coefficient growth and hence zero Taylor
radius.  The minimal branch has infinite radius.  This resolves the apparent
paradox: the \(k=0\) relation produces a formal sequence for every \(E\), but
that sequence is a convergent Taylor series precisely when it coincides with
the minimal solution selected from infinity.

## 7. Exact characteristic condition

Let \(g=|F|^2\).  Pincherle's theorem, as stated and proved in Gautschi,
Theorem 1.1, equates the minimal-solution ratios with the convergent continued
fraction.  Define

\[
S_k(E)=E-d_k-\frac{(k+1)g}{
 E-d_{k+1}-\dfrac{(k+2)g}{
 E-d_{k+2}-\ddots}},
\qquad k\ge1,
\]

where the fraction means the Pincherle limit associated with the minimal
recurrence solution.  Then

\[
\frac{c_1^{\min}}{c_0^{\min}}=\frac{F}{S_1(E)}.
\]

The origin relation requires \(c_1/c_0=E/\overline F\).  The author-defined
characteristic function is therefore

\[
\boxed{\mathcal C(E)
=E-\frac{|F|^2}{
E-d_1-\dfrac{2|F|^2}{
E-d_2-\dfrac{3|F|^2}{
E-d_3-\ddots}}}.}
\]

At a pole, the equation is understood by the equivalent cross-multiplied
minimal-solution compatibility condition.  For \(F\ne0\), the Jacobi
off-diagonal coefficients never vanish, so eigenvalues of the full Jacobi
operator do not coincide with eigenvalues of its one-step tail; the displayed
root condition is therefore unambiguous at physical eigenvalues.

Necessity: a Bargmann eigenfunction has Taylor coefficients satisfying the
origin relation and
\(\sum k!|c_k|^2<\infty\); it must be the minimal recurrence branch, so
Pincherle gives \(\mathcal C(E)=0\).

Sufficiency: if \(\mathcal C(E)=0\), the minimal sequence also satisfies the
origin relation.  Its Taylor series has infinite radius and solves the
differential equation coefficientwise.  The coefficient estimate below puts
it in Bargmann--Fock space, so it is an eigenvector of the already
self-adjoint Hamiltonian.

Thus the zeros of \(\mathcal C\) give every physical eigenvalue and no
spurious value.  Self-adjointness and compact resolvent imply that these
zeros are real and discrete.  No Hamiltonian-matrix truncation enters the
definition.  The integer \(n\) only labels the ordered roots \(E_n\).

## 8. Entire order and Bargmann membership

The minimal coefficients have the form

\[
|c_k|\le C A^k k^M/(k!)^2
\]

for suitable constants after increasing \(C,A,M\) to cover finitely many
initial terms.  Hence the entire function has order \(1/2\); the leading
coefficient asymptotics give type

\[
2\sqrt{\frac{2|F|}{V}}
\]

in the standard order-\(1/2\) convention.

More directly,

\[
\sum_{k=0}^\infty k!|c_k|^2
\le C^2\sum_{k=0}^\infty
\frac{A^{2k}k^{2M}}{(k!)^3}<\infty.
\]

Therefore Bargmann--Fock membership is automatic for an entire Taylor
solution selected by this recurrence.  It is not inferred from decay in a
few sectors.

This statement is special to solutions of the present recurrence; it is not
the false general assertion that every entire function belongs to
Bargmann--Fock space.

## 9. Distinguished author-defined function

For \(F\ne0\) and only when \(\mathcal C(E)=0\), define

\[
\operatorname{HeunD}_{\rm BF}(B_1,B_2,B_3,q;z)
=\sum_{k=0}^\infty c_kz^k,
\]

where \(c_0=1\), \(c_{-1}=0\), and the coefficients obey

\[
(k+1)B_1c_{k+1}
+[k(k-1)+B_2k+B_3]c_k+qc_{k-1}=0.
\]

This notation is author-defined.  It is not Maple's, Wolfram Language's,
DLMF's, Bühring's, or Figueiredo's `HeunD`.  It exists only on the
Bargmann-characteristic locus and denotes the entire, Bargmann-admissible
solution normalized to one at the origin.

The physical eigenfunction is

\[
\Psi_n(z)=\mathcal N_n
\operatorname{HeunD}_{\rm BF}
\left(\frac{2\overline F}{V},
\frac{2\hbar\omega_0}{V},
-\frac{2E_n}{V},\frac{2F}{V};z\right),
\]

where \(\mathcal N_n\) supplies Hilbert-space normalization.

## 10. Undriven limit

The case \(F=0\) must be treated before dividing by \(F\).  It gives

\[
\frac V2z^2\Psi''+\hbar\omega_0z\Psi'-E\Psi=0.
\]

For \(\Psi=z^\lambda\),

\[
\frac V2\lambda(\lambda-1)+\hbar\omega_0\lambda-E=0.
\]

Single-valued entire Bargmann solutions require
\(\lambda=n\in\mathbb N_0\), hence

\[
E_n^{(0)}
=\frac V2n(n-1)+\hbar\omega_0n.
\]

The driven continued fraction is singular term by term as \(F\to0\): roots
near \(d_n\), \(n\ge1\), arise through poles of successive tails rather than
by substituting \(g=0\) into only the outermost level.  Nevertheless the
operator family converges to the diagonal \(H_0\) in the relative-perturbation
sense already used in the manuscript.  Its discrete eigenvalues therefore
converge, with multiplicity and possible relabelling at degeneracies, to the
set \(\{d_n:n\in\mathbb N_0\}\).  This is the controlled singular reduction
of the driven characteristic condition; it recovers the Euler spectrum but
does not turn the driven equation into an integer-exponent condition.

## 11. Sources and exact locations

- B. D. Bonorino Figueiredo, “Ince's limits for confluent and
  double-confluent Heun equations,” *J. Math. Phys.* **46**, 113503 (2005),
  DOI 10.1063/1.2104267; arXiv:math-ph/0509013.  Parent equations,
  Whittaker--Ince prescription, limiting DCHE solutions, and subnormal Thomé
  behaviour.
- L. Jaccoud El-Jaick and B. D. B. Figueiredo, arXiv:0807.2219v3;
  published in slightly different form as “Solutions for confluent and
  double-confluent Heun equations,” *J. Math. Phys.* **49**, 083508 (2008),
  DOI 10.1063/1.2970150.  Equations (1), (3), (5), (7), and §4.2.
- L. Jaccoud El-Jaick and B. D. B. Figueiredo, arXiv:1209.4673v2;
  partially published in *J. Phys. A* **46**, 085203 (2013), DOI
  10.1088/1751-8113/46/8/085203.  Equations (1)--(3), §2.4, especially
  equations (222a), (222e), (223a), (223c), and (224).
- W. Gautschi, “Computational aspects of three-term recurrence relations,”
  *SIAM Review* **9**, 24--82 (1967), DOI 10.1137/1009002.  Theorem 1.1
  (Pincherle), §2, and Theorem 2.3 (Perron--Kreuser).

## 12. Remaining limitations

- No equality between the author-defined
  \(\operatorname{HeunD}_{\rm BF}\) and a standard software `HeunD` is
  claimed.
- A detailed connection formula between the Taylor solution and each
  two-sided Bessel family has not been derived.
- The continued fraction is exact, but a certified numerical evaluation
  algorithm and error bounds remain future work.
- Degenerate undriven levels may split and exchange ordered labels as
  \(F\to0\); the limiting multiset, rather than a globally fixed label, is the
  invariant statement.
