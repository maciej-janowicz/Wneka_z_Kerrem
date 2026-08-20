# Corrected Weber connection and conditional global reduction

## Audit of stage 10

Stage 10 correctly retained the exact direct normal form, the double root at
\(y=-1\), the simple root at \(y=1/2\), both local Weber orientations, the
gauge monodromy, and the fact that no checked Fedoryuk result constructs the
required global chain.  Its scalar DLMF identity and the zeros
\(c_W(n)=0\) were also correct.  Two claims require correction: one scalar
identity was completed to a unimodular matrix without deriving its second
row, and the proposed ``minimal lemma'' assumed the orientation, gamma
factor, effective index, energy expansion, and Bargmann equivalence that it
was meant to derive.

The turning-point expansions, local Weber solvability and formal operator
coefficients remain local/formal results.  No global progressive domain
chain, pole passage, physical orientation, factorization through \(c_W\), or
equivalence with the exact Bargmann determinant is proved.

## Starting data and direct Fedoryuk normal form

After the unitary drive-phase rotation take \(F=|F|>0\) and define
\[
 y=\frac{z}{\eta^{1/3}},\qquad \varepsilon=\eta^{-2/3},\qquad
 \eta=\frac{|F|}{V},\qquad \delta=\frac{\hbar\omega _0}{V},\qquad
 e=\frac{E}{V\eta^{4/3}}.
\]
On a fixed punctured sector, with one fixed logarithm, the exact Liouville
gauge and normal form are
\[
 \Psi=z^{-\delta}e^{\eta/z}u,qquad
 \varepsilon^2u_{yy}=(Q_0+\varepsilon Q_1+\varepsilon^2Q_2)u,
\]
\[
 Q_0=\frac{P(y;e)}{y^4},\qquad Q_1=\frac{2(\delta-1)}{y^3},
 \qquad Q_2=\frac{\delta(\delta-1)}{y^2},\qquad
 P(y;e)=1+2ey^2-2y^3.
\]
There are no omitted higher powers of \(\varepsilon\).  At the real
critical value
\[
 e_0=-\frac32,\qquad P(y;e_0)=-(y+1)^2(2y-1),
\]
the point \(y=-1\) is double and \(y=1/2\) remains simple.  For
\(e=e_0+\varepsilon e_1+O(\varepsilon^2)\), the leading turning points are
\[
 y_\pm=-1\pm\sqrt{-\frac{2e_1}{3}}\,\varepsilon^{1/2}
 +\frac{4e_1}{9}\varepsilon+O(\varepsilon^{3/2}),\qquad
 y_s=\frac12+\frac{e_1}{9}\varepsilon+O(\varepsilon^2).
\]
Thus the close pair requires a Weber model on the
\(y+1=O(\varepsilon^{1/2})\) scale, while the separated point has the local
Airy class.  The pole at \(y=0\) is not part of either turning-point disk.

## Fedoryuk source audit

The checked source is M. V. Fedoryuk, *Asymptotic Analysis: Linear Ordinary
Differential Equations*, Springer, Berlin, 1993, translated by Andrew
Rodick, ISBN 978-3-540-54810-2, DOI 10.1007/978-3-642-58016-1.  The
accessible contents confirm Chapter III, Section 2, ``WKB Bounds in the
Complex Plane'' (from p. 87), and Section 4, ``Equations with Entire or
Meromorphic Coefficients'' (from p. 108).  They also confirm Chapter IV,
Section 2 on a simple complex turning point (from p. 182), Sections 4 and 6
on multiple turning points (from pp. 191 and 207), and the section on two
close turning points (from p. 211).

The preview available for the audit did not expose complete theorem
statements or theorem numbers, so none is invented.  The faithful limited
paraphrase is that WKB solutions with error bounds are constructed on
appropriate complex canonical domains carrying single-valued actions and
progressive paths; separate local constructions cover simple, multiple, and
close turning points.  These results require their domains and paths as
hypotheses.  The checked material does not itself construct one Kerr chain
that simultaneously crosses the required sheets, treats the fourth-order
pole, incorporates the remaining simple point, controls every overlap, and
identifies the result with a Bargmann-entire germ.

## Applicability table

| hypothesis | verification for the Kerr problem | status |
|---|---|---|
| large parameter | \(\varepsilon^{-1}=\eta^{2/3}\to\infty\) | verified |
| meromorphic coefficients | \(Q_0,Q_1,Q_2\) are rational | verified |
| local nonvanishing of \(Q_0\) | remove its roots and \(y=0\) from each WKB domain | verified locally |
| single-valued momentum and action | fix a sheet on a simply connected cut domain | verified locally |
| simple turning point | \(y_s=1/2+O(\varepsilon)\), with \(Q_0'(1/2)=-72\) at criticality | verified locally |
| close turning-point pair | \(y_\pm+1=O(\varepsilon^{1/2})\) | verified locally |
| analyticity near the pair | a fixed disk about \(-1\) excludes the pole and simple point | verified |
| progressive paths | available in deliberately local sectors | verified locally only |
| finite global domain chain (H1) | must connect sheet-related pole sectors through Weber and possibly Airy domains | not proved |
| fourth-order-pole transition | ordinary turning-point results do not cross \(y=0\) | not supplied |
| uniform overlap estimates | no complete family of overlaps has been constructed | not proved |
| sheet and gauge monodromy | reciprocal gauge multiplier is known; its realization by the path is not | not proved globally |
| Bargmann-germ identification | requires controlled cancellation of the essential and algebraic factors | not proved globally |
| scalar endpoint reduction (H2) | a candidate boundary contraction can be written | hypothesis only |
| structural factorization (H3) | requires exact/asymptotic alignment of transported boundary vectors | not proved; not implied by H1 or H2 |

## Momentum surface and candidate global geometry

The leading momentum lives on
\[
 \mathcal R_e=\{(y,w):w^2=P(y;e)\},\qquad p=\frac{w}{y^2}.
\]
For three simple roots this is a two-sheeted genus-one compact cover,
branched at the three finite roots and infinity.  At criticality the close
branch points merge and the surface degenerates to a nodal cover at the
double turning point.  The fourth-order pole at \(y=0\) is not a branch
point of \(p\), because the pole order is even, but it is a genuine
irregular endpoint of the differential equation.

One must choose cuts joining branch points and a sheet of \(w\) before the
actions
\(S_j(y)=\int_{y_j}^y p(t)\,dt\) are single-valued.  For example, the sheet
may be fixed by \(p>0\) immediately to the right of zero, with cuts adapted
to the close pair and the remaining root; this is a convention, not yet a
physical continuation cycle.  We use Fedoryuk's convention: Stokes curves
satisfy \(\Re S_j=0\), anti-Stokes curves satisfy \(\Im S_j=0\), and
separatrices form relevant canonical-domain boundaries.  At the double
point the Stokes directions are \(\pi/4+k\pi/2\) and anti-Stokes directions
are \(k\pi/2\).  At \(y=1/2\), each family has three rays.

A candidate chain contains: a punctured origin sector carrying the
gauge-compensated germ; an ordinary WKB overlap; a fixed close-pair Weber
disk; a second WKB overlap; an Airy disk if the actual topology forces
passage by \(y_s\); and a sheet-related terminal origin sector.  Each
overlap must carry a compatible action branch, progressive paths, and
uniform error constants.  The numerically traced curves in the companion
figure support this inventory only; they prove neither global connectivity
nor univalence.  Both exponentials at infinity have Bargmann-admissible
order-one-half growth, so rejecting an infinity branch cannot replace the
missing endpoint construction.

## Exact Weber bases and two connection identities

Consider
\[
 w''(Z)+\left(\nu+\frac12-\frac{Z^2}{4}\right)w(Z)=0
\]
and use principal arguments \(-\pi<\arg Z\leq\pi\), with rotations continued
through the indicated half-planes.  Define the ordered column bases
\[
 \mathcal A=\binom{D_\nu(Z)}{D_{-\nu-1}(iZ)},\qquad
 \mathcal B=\binom{D_\nu(-Z)}{D_{-\nu-1}(-iZ)}.
\]
Here \(D_\rho(z)\sim z^\rho e^{-z^2/4}\) is subdominant for
\(|\arg z|<3\pi/4\); hence the first members are subdominant about the
positive/negative real axes, and the second about the negative/positive
imaginary axes, respectively.  Dominance is reversed in the opposite Weber
sectors.  These sector statements concern canonical asymptotics, not a
choice of a physical Kerr path.

Starting from DLMF 12.2.17--12.2.20 and
\(D_\nu(Z)=U(-\nu-1/2,Z)\), choosing the minus rotation and substituting
\(a=-\nu-1/2\) gives
\[
 D_\nu(Z)=e^{-i\pi\nu}D_\nu(-Z)+c_W(\nu)D_{-\nu-1}(iZ),
 \quad c_W(\nu)=\frac{\sqrt{2\pi}e^{-i\pi(\nu+1)/2}}{\Gamma(-\nu)}.
 \tag{1}
\]
Apply the same formula independently with index \(-\nu-1\) and argument
\(iZ\).  This gives the second relation
\[
 D_{-\nu-1}(iZ)=d_W(\nu)D_\nu(-Z)
 -e^{i\pi\nu}D_{-\nu-1}(-iZ),
 \quad d_W(\nu)=\frac{\sqrt{2\pi}e^{i\pi\nu/2}}{\Gamma(\nu+1)}.
 \tag{2}
\]
The reflection formula yields
\[
 c_Wd_W=e^{i\pi\nu}-e^{-i\pi\nu}.
\]
Substitution of (2) into (1), rather than an algebraic completion of one
row, now gives
\[
 \mathcal A=M_W\mathcal B,
 \qquad M_W=\begin{pmatrix}
 e^{i\pi\nu}&-e^{i\pi\nu}c_W\\ d_W&-e^{i\pi\nu}
 \end{pmatrix},qquad M_W^{-1}=M_W,qquad\det M_W=-1.
 \tag{3}
\]
Direct multiplication using the displayed product \(c_Wd_W\) gives the
identity matrix.

With \(\mathscr W(f,g)=fg'-f'g\), evaluation at \(Z=0\), using the standard
values of \(D_\rho(0)\) and \(D'_\rho(0)\), gives
\[
 \mathscr W(\mathcal A)=-i e^{-i\pi\nu/2},\qquad
 \mathscr W(\mathcal B)= i e^{-i\pi\nu/2}.
\]
Thus \(\det M_W=\mathscr W(\mathcal A)/\mathscr W(\mathcal B)=-1\), as
required.  Both Wronskians are nonzero for every \(\nu\in\mathbb C\), so
both are entire, nondegenerate bases without an exceptional index.  At
\(\nu=n\in\mathbb N_0\), \(c_W(n)=0\), \(d_W(n)\ne0\), and (3) has the
regular limit
\[
 M_W(n)=\begin{pmatrix}(-1)^n&0\\d_W(n)&-(-1)^n\end{pmatrix}.
\]
The zero of \(c_W\) is simple because
\(1/\Gamma(-n-h)=(-1)^{n+1}n!h+O(h^2)\).  No singular renormalization in
\(\nu\) is needed.  Wronskian-normalized bases could change the determinant
to one, but that adds nothing to the local scalar zero and is not used.

## General global matrix algebra

Write
\[
 M_{\rm glob}=B_{\rm out}M_A^{\chi_A}B_2M_WB_1G_0=:L M_W R,
 \qquad \chi_A\in\{0,1\}.
\]
After the initial admissible vector and final inadmissible covector are
absorbed into \(r=Rv_{\rm in}=(r_1,r_2)^T\) and
\(\ell^T=q_{\rm bad}^TL=(\ell_1,\ell_2)\), the physical candidate scalar is
\[
 \mathcal C=\ell^TM_Wr
 =e^{i\pi\nu}\ell_1r_1-e^{i\pi\nu}c_W\ell_1r_2
 +d_W\ell_2r_1-e^{i\pi\nu}\ell_2r_2. \tag{4}
\]
Thus general invertible surrounding matrices mix all four entries.  At
\(c_W(n)=0\), the other three terms normally remain.  The elementary
counterexample \(L=R=I\), \(q_{\rm bad}^T=v_{\rm in}^T=(1,0)\) gives
\(\mathcal C=e^{i\pi\nu}\), so the Weber zero is absent.

For (4) to be exactly proportional to \(c_W\), the non-\(c_W\) combination
\[
 e^{i\pi\nu}(\ell_1r_1-\ell_2r_2)+d_W\ell_2r_1
\]
must vanish identically (and \(\ell_1r_2\ne0\)).  Vanishing only at
\(\nu=n\) is sufficient merely to retain that zero.  Triangular transport
and boundary alignment can impose such conditions, but sectorial
dominance alone only identifies asymptotic sizes; it does not prove exact
zeros of matrix entries.  An unknown Airy matrix is part of \(L\), and can
therefore shift or remove the Weber zero.  Factorization is not unambiguous
until paths, bases, and transition matrices are fixed.

## Global Fedoryuk--Bargmann connection hypotheses

**H1 (geometry and transport).**  For fixed level and \(\delta\) in a
compact set, suppose that a uniformly finite chain of canonical origin,
WKB, close-pair Weber and, if required, Airy domains exists; its overlaps
have uniform constants and progressive paths; WKB--Weber, WKB--Airy and
pole transitions are controlled; sheets and gauge monodromy agree; and its
initial solution is the gauge-compensated normalized analytic Bargmann germ.
H1 neither chooses the imaginary Weber pair nor states a gamma zero, energy
coefficient, energy form, or equivalence with entireness.

**H2 (scalar endpoint reduction).**  Suppose that continuation of the H1
germ has one analytic inadmissible endpoint coefficient, expressible as a
boundary contraction (or the corresponding minor/determinant) of the global
transfer matrix, with a uniform controlled remainder.  H2 does not identify
that scalar with \(1/\Gamma(-\nu_{\rm eff})\).

**H3 (structural factorization).**  To recover Weber quantization one must
add that the transported boundary vectors obey the cancellation condition
following (4), uniformly to the required order, with
\(-e^{i\pi\nu}\ell_1r_2\) nonzero.  Equivalently, the global scalar factors
through \(c_W\), up to a remainder small enough near its simple zero.  This
is not a consequence of H1 or H2 presently proved; in particular it includes
the needed protection against a possible Airy mixing.

Only after H1--H3 and an independently proved identification of the endpoint
coefficient with the exact Bargmann condition
\(\Delta_{\rm WI}(2\eta,2\delta,-2E/V,2\eta)=0\) may one use Rouch\'e's or
the implicit-function theorem.  The physical imaginary orientation must
also emerge from the constructed path; it is not assumed in H1.

## Missing global steps

The following statements remain unproved and logically distinct:

1. H1: existence of the physical finite domain chain with constants uniform
   in \(\varepsilon\);
2. progressive paths and uniform transition estimates on every overlap;
3. a controlled passage between compensated sectors at the fourth-order
   pole;
4. whether the physical continuation must use an Airy transition at the
   remaining simple point, or can avoid it;
5. realization of the required sheet exchange, logarithmic branch, and
   reciprocal gauge monodromy by one actual continuation path;
6. H2 together with identification of its endpoint scalar with the exact
   condition \(\Delta_{\rm WI}=0\);
7. H3, namely preservation of the factorizing/triangular boundary
   structure through all surrounding matrices;
8. selection of the imaginary Weber orientation by the constructed global
   path.

In particular, neither H1 nor H2 implies H3 on present evidence.  The local
identity \(c_W(n)=0\) is **not by itself a global spectral condition**.

## Proposed proof program

The following is a program for a proof, not a completed proof:

1. construct the critical Stokes graph on the momentum surface
   \(\mathcal R_e\), including its sheets, cuts, pole sectors, and the
   remaining simple point;
2. identify the continuation cycle belonging to the normalized physical
   Bargmann germ;
3. cover that cycle by finitely many canonical domains with controlled,
   uniform overlaps and progressive paths;
4. establish pole-end Volterra estimates for the gauge-compensated solution;
5. insert the close-pair Weber parametrix and, if the graph requires it, a
   correctly oriented Airy parametrix;
6. transport Wronskian-normalized bases while tracking sheets, the logarithm,
   and gauge monodromy;
7. compute the actual terminal covector \(\ell\) and initial vector \(r\),
   rather than replacing them by convenient model vectors;
8. test the cancellation condition in (4), thereby proving or disproving
   H3 and checking whether Airy mixing preserves the Weber zero;
9. only then compare the resulting global scalar with
   \(\Delta_{\rm WI}\) and, if a uniform small remainder is available near
   a simple zero, apply Rouch\'e's or the implicit-function theorem.

## Status of energy information and verdict

The coefficient \(-3/2\) at \(\eta^{4/3}\) follows from double-root
geometry.  The two local Weber orientations give
\(e_{1,n}^{(R)}=\delta-1-\sqrt3(n+1/2)\) and
\(e_{1,n}^{(I)}=\delta-1+\sqrt3(n+1/2)\).  Selecting the positive sign as a
physical eigenvalue is conditional on global orientation and H3.  The
constant
\[
 \frac{\delta(1-2\delta)}6-\frac{6n^2+6n+1}{72}
\]
is locally/formally verified but becomes a spectral consequence only with
sufficiently accurate global factorization and remainder control.
\(K_n(\delta)\eta^{-2/3}\) remains solely a formal
Rayleigh--Schr\"odinger coefficient.

The verifier evaluates both functional identities with 70 decimal digits at
five noninteger indices and three complex arguments, checks both Wronskians,
the inverse, integer limits, and simple gamma zeros.  The observed normalized
functional residual and Wronskian error are below \(2\times10^{-71}\),
against tolerance \(10^{-55}\).  These are independent local tests, not
evidence for H1--H3.

**Verdict: GLOBAL REDUCTION REQUIRES AN ADDITIONAL STRUCTURAL HYPOTHESIS.**
