# Weak-drive Kerr expansion and the Bender--Bettencourt reorganization

## Primary-source audit

The supplied file is the correct paper: C. M. Bender and L. M. A.
Bettencourt, *Multiple-scale analysis of quantum systems*, Physical Review D
**54**, 7710--7723 (1996), DOI 10.1103/PhysRevD.54.7710; arXiv:
hep-th/9607074.  Page numbers below are PDF pages (the printed article begins
on PDF p. 1).

Section IV, “Resummation of the conventional perturbation series for the
quantum anharmonic oscillator” (PDF pp. 14--24), studies

\[
 [-d^2/dx^2+x^2/4+\epsilon x^4/4-E(\epsilon)]\psi=0,
 \qquad \psi(\pm\infty)=0. \tag{BB 4.1--4.2}
\]

It starts from the divergent Rayleigh--Schrödinger series
\(\psi\sim\sum\epsilon^ny_n\), \(E\sim\sum\epsilon^nE_n\) (4.4), with
\(y_n=e^{-x^2/4}P_n\) (4.7).  The polynomials and their triangular recursion
are (4.8)--(4.11).  Keeping the highest power at every order gives
\(C_{n,2n}=(-1/4)^n/n!\) (4.12--4.13), hence the first partial sum
\(e^{-x^2/4-\epsilon x^4/16}\) (4.14).  This is not the WKB cubic
\(e^{-\sqrt\epsilon |x|^3/6}\) (4.3).  Successive diagonals
\(C_{n,2n-j}\), exemplified by (4.15)--(4.20), are then summed and absorbed
into an exponential times new polynomials (4.21).  Repeating the operation
with the new highest-power diagonals (4.22)--(4.25) produces a second
exponential reorganization (4.26).  Iteration generates the exponent shown
through several orders in (4.32).  With \(z=\epsilon x^2\) and
\(P_n^{(N)}(z)\) (4.33), the leading coefficient recursion (4.35)--(4.37)
and the large-\(N\) limit (4.38)--(4.44) yield the WKB expansion (4.45).
Thus: finite RS series, selected infinite diagonal sum, iterated
reorganization, large-order asymptotics, and WKB comparison are distinct
steps; (4.14) alone is not the WKB result.

Section V, “Multiple-scale perturbation theory applied to the Schrödinger
equation” (PDF pp. 24--28), derives the same exponent organization directly.
It introduces \(\xi_1=\epsilon f_1(x)\), treats \(x,\xi_1\) as independent
(5.2), and removes the resonant right-hand side of the first-order equation.
This fixes \(f_1=x^4/16+3x^2/8\), \(E_1=3/4\), and \(A=e^{-\xi_1}\)
(5.7--5.9).  Further scales \(\xi_j=\epsilon^jf_j(x)\) give (5.10)--(5.13),
including ordinary perturbative energy coefficients while resumming spatial
growth.  Multiple scales is therefore a direct mechanism for the same
implicit infinite resummation, not an extra claim that every reorganized
series converges.

## Kerr zeroth order and nondegeneracy

Put \(\delta=\hbar\omega_0/V\), \(f=F/V\), and rotate with
\(U_\phi=e^{i\phi N}\), \(\phi=-\arg f\), so that the transformed drive is
\(\lambda=|f|\).  The original coefficients are restored by multiplying the
Fock coefficient of \(|n\rangle\) relative to \(|N\rangle\) by
\(e^{i(n-N)\arg f}\).  Then

\[
 h_0={1\over2}z^2\partial_z^2+\delta z\partial_z,
 \quad h_1=\lambda(z+\partial_z),\quad
 \Psi_N^{(0)}={z^N\over\sqrt{N!}},\quad
 e_n={n(n-1)\over2}+\delta n.
\]

In particular \(e_N-e_{N-1}=N-1+\delta\) and
\(e_N-e_{N+1}=-(N+\delta)\).  Full nondegeneracy for fixed \(N\) is

\[
 \delta\ne-{n+N-1\over2}\quad(n\in\mathbb N_0,\ n\ne N).
\]

For \(N=0\) there is no lower channel; its resonances are
\(\delta=-(n-1)/2\), \(n\ge1\).  At any excluded value one must use a
degenerate finite-block calculation; no vanishing denominator is cancelled
formally here.

## Rayleigh--Schrödinger coefficients

Let \(\Delta_j=e_N-e_{N+j}=-j[N+\delta+(j-1)/2]\), omit states with
\(N+j<0\), and impose \(\langle N|\Psi_N\rangle=1\).  If
\(\Psi_N=|N\rangle+\sum_{k\ge1}\lambda^k\sum_nc_{n}^{(k)}|n\rangle\), then

\[
 e^{(k)}=\sqrt N c_{N-1}^{(k-1)}+\sqrt{N+1}c_{N+1}^{(k-1)},
\]
\[
 c_n^{(k)}={\sqrt n c_{n-1}^{(k-1)}+\sqrt{n+1}c_{n+1}^{(k-1)}
 -\sum_{j=1}^{k-1}e^{(j)}c_n^{(k-j)}\over e_N-e_n},\quad n\ne N,
 \qquad c_N^{(k)}=0. \tag{1}
\]

This is also a compact, unambiguous listing of *all* coefficients through
any desired order; the verification script expands (1) through order four.
Explicitly,

\[
 \Psi^{(1)}={\sqrt N\over\Delta_{-1}}|N-1\rangle
 +{\sqrt{N+1}\over\Delta_1}|N+1\rangle,
\]
\[
 \Psi^{(2)}={\sqrt{N(N-1)}\over\Delta_{-1}\Delta_{-2}}|N-2\rangle
 +{\sqrt{(N+1)(N+2)}\over\Delta_1\Delta_2}|N+2\rangle,
\]
\[
\begin{split}
 \Psi^{(3)}={}&{\sqrt{N(N-1)(N-2)}\over\Delta_{-1}\Delta_{-2}\Delta_{-3}}|N-3\rangle\\
 &+{\sqrt N[(N-1)/\Delta_{-2}-e^{(2)}]\over\Delta_{-1}^2}|N-1\rangle
 +{\sqrt{N+1}[(N+2)/\Delta_2-e^{(2)}]\over\Delta_1^2}|N+1\rangle\\
 &+{\sqrt{(N+1)(N+2)(N+3)}\over\Delta_1\Delta_2\Delta_3}|N+3\rangle .
\end{split}
\]

Terms with negative occupations are absent.  Only \(n-N\equiv k\pmod2\)
and \(|n-N|\le k\) occur.  The unitary parity \((-1)^N\) changes
\(\lambda\to-\lambda\), so all odd energy coefficients vanish.  The first
two nonzero corrections are

\[
 e^{(2)}={N\over N-1+\delta}-{N+1\over N+\delta}
 ={1-\delta\over(N-1+\delta)(N+\delta)},
\]
\[
\begin{split}
e^{(4)}={}&{N(N-1)\over (N-1+\delta)^2(2N-3+2\delta)}
-{(N+1)(N+2)\over (N+\delta)^2(2N+1+2\delta)}\\
&-e^{(2)}\left[{N\over(N-1+\delta)^2}
+{N+1\over(N+\delta)^2}\right]. \tag{2}
\end{split}
\]

The first term of (2) is omitted for \(N<2\), and every lower-channel term
proportional to \(N\) is omitted for \(N=0\) before division (in particular
at \(\delta=1\)).  The unsimplified formula gives
\(e_0^{(2)}=-1/\delta\).  Away from resonances the sign of the
simplified second-order expression is the sign of
\((1-\delta)/[(N-1+\delta)(N+\delta)]\), not universally negative.

## Exact Bargmann recurrence and BB analogue

For complex drive the exact equation gives

\[
 (e_n-\epsilon)c_n+f\sqrt n\,c_{n-1}
 +f^*\sqrt{n+1}\,c_{n+1}=0,
\]

and after the phase rotation both off-diagonal coefficients are \(\lambda\).
Expanding it reproduces (1), including normalization factors.  Order \(k\)
reaches at most \(N-k\) and \(N+k\), truncated at zero.

The BB operation that is actually available here is to select the monotone
edge paths of this triangular array and sum them over perturbative order.
After division by \(z^N/\sqrt{N!}\), the upper edge is

\[
 \sum_{k\ge0}{(-2\lambda z)^k\over k!(2N+2\delta)_k}
 ={}_0F_1(;2N+2\delta;-2\lambda z), \tag{3}
\]

while the lower edge terminates:

\[
 \sum_{k=0}^N{(-N)_k\over(-2N+2-2\delta)_k}
 { (2\lambda/z)^k\over k!}
 ={}_1F_1(-N;-2N+2-2\delta;2\lambda/z). \tag{4}
\]

Equations (3)--(4) sum two selected families, not the full RS series; their
union is obtained as upper + lower - 1, not their product.  The upper scaled
variable is \(\lambda z=O(1)\).  The formal lower variable is
\(\lambda/z=O(1)\), but for fixed \(N\) it is only a finite polynomial.
Multiplication by \(z^N\) cancels every apparent pole in (4); the physical
truncations and their order-by-order sum remain entire.  Likewise the local
logarithm \(\log(\Psi/z^N)\) may contain \(z,1/z\), and higher Laurent
powers, but is meaningful only off zero on a fixed branch and is not itself
a Bargmann entire function.

The raw fixed-order series is uniform on fixed compact sets as
\(\lambda\to0\).  Sum (3) extends the useful description into the upper
double scaling \(|z|=O(\lambda^{-1})\), away from its parameter poles and
from zeros where relative errors are ill-conditioned.  There is no analogous
infinite lower resummation for fixed \(N\).  The special function forced by
the edge recurrence is \({}_0F_1\) (equivalently a Bessel function), not a
Weber function.  It solves \(xY''+bY'-Y=0\) with
\(x=-2\lambda z\), \(b=2N+2\delta\).

This is still a weak-drive expansion around \(z^N\).  As shown below, its
large-argument Bessel asymptotics reproduce the formal leading WKB exponent
and leading algebraic prefactor, but not a global WKB solution or controlled
remainder.  It is distinct
from the strong-drive \(\eta\gg1\) Olver/Fedoryuk limit.  No controlled
overlap with that limit follows at fixed \(N\); a Weber equation can arise
there only after the separately derived coalescing-turning-point scaling.

## Edge equation, exact residual, and Bessel representation

Let \(b=2N+2\delta\), \(x=-2\lambda z\), and
\(Y_0={}_0F_1(;b;x)\).  Its coefficient recurrence directly gives

\[
 zY_0''+bY_0'+2\lambda Y_0=0. \tag{5}
\]

Writing \(\Psi=z^NY/\sqrt{N!}\), the exact equation becomes

\[
 {z^N\over\sqrt{N!}}\left\{
 {z^2\over2}Y''+(N+\delta)zY'+\lambda zY
 +\lambda Y'+{\lambda N\over z}Y-(\epsilon-e_N)Y\right\}=0. \tag{6}
\]

Thus (5) cancels the first three terms, and its exact residual is

\[
 \mathcal R_{\rm edge}={z^N\over\sqrt{N!}}
 \left[\lambda Y_0'+{\lambda N\over z}Y_0
 -(\epsilon-e_N)Y_0\right]. \tag{7}
\]

The first two pieces are the omitted downward action
\(\lambda\partial_z\); the energy term begins with
\(-\lambda^2e_N^{(2)}Y_0\).  They generate paths containing reversals and
the next diagonals.  At fixed \(x\), (7) is \(z^NO(\lambda^2)\), whereas the
edge operator is \(z^NO(1)\).  This is a formal double-scaling statement,
not a sectorially uniform relative-error bound, especially near zeros.

For \(b\notin\{0,-1,-2,\ldots\}\), and with a consistent branch of Log,

\[
 {}_0F_1(;b;x)=\Gamma(b)x^{(1-b)/2}I_{b-1}(2\sqrt{x})
 =\Gamma(b)(-x)^{(1-b)/2}J_{b-1}(2\sqrt{-x}). \tag{8}
\]

Although the factors in (8) are branch dependent, their products continue
to the single-valued entire function of \(x\).  On the principal branch,
\(-\pi<\arg x<\pi\), the dominant \(I\)-saddle away from its Stokes
boundaries gives

\[
 {}_0F_1(;b;x)\sim {\Gamma(b)\over2\sqrt\pi}
 x^{(1-2b)/4}e^{2\sqrt{x}}
 \left[1-{4(b-1)^2-1\over16\sqrt{x}}+O(x^{-1})\right]. \tag{9}
\]

Analytic continuation supplies the other saddle
\(x^{(1-2b)/4}e^{-2\sqrt{x}}\) with the sector-dependent phase inherited
from \(I_{b-1}\); its multiplier changes across the Stokes rays
\(\arg\sqrt{x}=\pm\pi/2\).  On oscillatory continuations the \(J\)-form in
(8) displays both exponentials with the usual phases
\(e^{\pm i(2\sqrt{-x}-\pi(b-1)/2-\pi/4)}\).  Consequently the two formal
exponents are exactly

\[
 \exp[\pm2\sqrt{-2\lambda z}]. \tag{10}
\]

## Independent formal WKB comparison

After division by \(z^2/2\), remove the first derivative with
\(\Psi=z^{-\delta}e^{\lambda/z}u\).  The exact normal form is

\[
 u''+K(z)u=0,
\quad K={2\lambda\over z}
 +{-2\epsilon+\delta-\delta^2\over z^2}
 +{2(1-\delta)\lambda\over z^3}-{\lambda^2\over z^4}. \tag{11}
\]

For large \(|z|\) with \(|\lambda z|\gg1\), the eikonal equation is
\(\tfrac12z^2(S')^2+\lambda z=0\), hence, on one fixed square-root branch,

\[
 S'=\pm\sqrt{-2\lambda/z},\qquad
 S=\pm2\sqrt{-2\lambda z}.
\]

The leading Liouville--Green transport factor is
\(z^{-\delta}(2\lambda/z)^{-1/4}\), after fixing the fourth-root branch, so
its \(z\)-power is \(z^{1/4-\delta}\).  Replacing (2\lambda/z) by
(-2\lambda/z) changes only a branch-dependent constant fourth-root phase,
but the positive-sign convention is used consistently here.  Equation (9), multiplied by \(z^N\) and using
\(b=2N+2\delta\), has precisely the same power because
\(N+(1-2b)/4=1/4-\delta\).  Thus both the formal leading WKB exponent and
leading algebraic prefactor agree.  The gauge factor \(e^{\lambda/z}\),
energy-dependent transport terms, and returning paths enter at subsequent
orders.  Merely keeping \(x=O(1)\) is not a large-argument WKB limit; the
comparison uses the further overlap \(1\ll|x|=2|\lambda z|\), in sectors
where a chosen saddle is asymptotically separated.

## First upper subdiagonal

Define the first upper subdiagonal at perturbative order \(k\) to be the
coefficient of \(|N+k-2\rangle\).  Relative to the upper endpoint it contains
one downward step; from \(k\ge3\) it also contains the fold generated by
\(e_N^{(2)}\).  In the double scaling it sums as

\[
 {\Psi_N\over z^N/\sqrt{N!}}=Y_0(x)+\lambda^2Y_1(x)+O(\lambda^4),
 \qquad Y_1=\sum_{m=-1}^\infty d_mx^m. \tag{12}
\]

The power is \(p=2\).  With \(a_m=[m!(b)_m]^{-1}\), \(a_m=0\) for \(m<0\),
the exact coefficient equations are

\[
 d_{-1}=\begin{cases}-4N/(b-2),&N\ge1,\\0,&N=0,\end{cases}
 \qquad d_0=0.
\]
\[
 d_m={d_{m-1}+4(m+N+1)a_{m+1}+2e_N^{(2)}a_m
 \over m(m+b-1)},\qquad m\ge1. \tag{13}
\]

The separate \(N=0\) clause is essential: at the regular, nondegenerate
point \(N=0,\delta=1\), hence \(b=2\), the formal quotient
\(4N/(b-2)\) is \(0/0\), while the nonexistent state
\(\lvert-1\rangle\) requires \(d_{-1}=0\).  The missing \(m=0\) equation is precisely the solvability condition
\(-d_{-1}/2=2(N+1)/b+e_N^{(2)}\).  Equivalently, (13) is summed by the
uniquely normalized Laurent solution of

\[
 \mathcal L_bY_1=2Y_0'+{2N\over x}Y_0+e_N^{(2)}Y_0,
 \quad \mathcal L_b={x^2\over2}{d^2\over dx^2}
 +{b x\over2}{d\over dx}-{x\over2}, \tag{14}
\]

with \(d_0=0\).  Here is the explicit local representation omitted in the
earlier audit.  On a simply connected zero-free domain choose \(x_*\ne0\),
put \(u=Y_0\), and define the reduction-of-order solution

\[
 v_*(x)=u(x)\int_{x_*}^{x}{dt\over t^b u(t)^2},\qquad
 W(u,v_*)=x^{-b}. \tag{15}
\]

After division of (14) by \(x^2/2\), its standard form and source are

\[
 Y_1''+{b\over x}Y_1'-{1\over x}Y_1=h(x),\qquad
 h(x)={4u'(x)\over x^2}+{4Nu(x)\over x^3}
       +{2e_N^{(2)}u(x)\over x^2}. \tag{14a}
\]

Variation of parameters, with \(W(u,v_*)=x^{-b}\), gives

\[
 Y_1(x)=C u(x)+Dv_*(x)-u(x)\int_{x_*}^{x}v_*(t)h(t)t^b\,dt
 +v_*(x)\int_{x_*}^{x}u(t)h(t)t^b\,dt. \tag{16}
\]

Direct differentiation of (16) gives
\(Y_1''+(b/x)Y_1'-Y_1/x=h\); the variable-upper-limit terms cancel and
the homogeneous constants drop out.  The constants \(C,D\) are fixed by
the Laurent coefficient \(d_{-1}\) and the zero constant coefficient of
\(Y_1\) only in the base chart connected to a punctured neighborhood of
\(x=0\), without crossing a zero of \(Y_0\) or changing the selected
branches.  On another local zero-free domain they must instead be
transported by overlap conditions or analytic continuation.  When
\(b\notin\mathbb Z\), one may use
\(v=x^{1-b}{}_0F_1(;2-b;x)\), whose Wronskian with \(u\) is
\((1-b)x^{-b}\), and insert the corresponding factor \(1/(1-b)\) in
(16).  At integral/resonant \(b\) this expression may coalesce or have a
singular parameter; (15), or its logarithmic limiting solution, is the
correct replacement.  Different zero-free domains have different base
points and constants related by homogeneous transition terms.

Expansion through order six agrees
identically with the RS recurrence (and hence through the order-four data of
11a).  This is one additional summed diagonal.  It gives a relative
\(\lambda^2Y_1/Y_0\) correction, which may be written locally as either a
prefactor or the first logarithmic correction; it is not merely a shift of
\(b\), and no claim of a completed BB hierarchy is made.

## Multiplicative dressing: the first genuine BB iteration

Summing a raw diagonal, algebraically writing
\(Y_0[1+\lambda^2Y_1/Y_0]\), and rebuilding perturbation theory with
\(Y_0\) in the zeroth approximation are logically distinct.  The third
operation starts from \(Y=Y_0Z\).  If \(r=Y_0'/Y_0\) and
\(\Delta e=\epsilon-e_N=\lambda^2e_N^{(2)}+\lambda^4e_N^{(4)}+\cdots\),
direct substitution in (6) gives the exact dressed equation

\[
 \mathcal A_bZ-\lambda^2\{2Z'+2(r+N/x)Z\}-\Delta e\,Z=0,
 \quad
 \mathcal A_b={x^2\over2}\partial_x^2+\left(x^2r+{bx\over2}\right)\partial_x.
 \tag{17}
\]

No term from (z\mapsto x=-2\lambda z) has been omitted.  With
\(Z=1+\lambda^2Z_1+\cdots\), (17) independently yields

\[
 \mathcal A_bZ_1=2(r+N/x)+e_N^{(2)}. \tag{18}
\]

Multiplying (18) by \(Y_0\) proves locally that \(Y_0Z_1=Y_1\); hence
\(Z_1=Y_1/Y_0\) on every zero-free domain.  Intermediate normalization means
that the Laurent expansion of \(Y_0Z_1\), not generally that of \(Z_1\), has
zero constant coefficient.  Equivalently, since

\[
 (x^bY_0^2Z_1')'=2x^{b-2}Y_0^2[2r+2N/x+e_N^{(2)}], \tag{19}
\]

\(Z_1\) has the explicit double-integral representation

\[
 Z_1(x)=C_*+D_*\int_{x_*}^{x}{ds\over s^bY_0(s)^2}
 +2\int_{x_*}^{x}{ds\over s^bY_0(s)^2}
 \int_{x_*}^{s}t^{b-2}Y_0(t)^2[2r(t)+2N/t+e_N^{(2)}]dt. \tag{20}
\]

The two constants are fixed by the same Laurent normalization as (16).
At a simple zero of (Y_0), (Z_1) generically has a pole; this is a
factorization artifact because the additive product (Y_0Z_1=Y_1) remains
regular there.  Consequently the multiplicative charts must be changed
across zeros, and no global nonvanishing factorization is asserted.

For the exponential form
\(Z=\exp(\lambda^2S_1+\lambda^4S_2+\cdots)\), the first two equations are

\[
 \mathcal A_bS_1=2(r+N/x)+e_N^{(2)},
\]
\[
 \mathcal A_bS_2=2S_1'+e_N^{(4)}-{x^2\over2}(S_1')^2. \tag{21}
\]

Thus \(S_1=Z_1=Y_1/Y_0\) and
\(S_2=Y_2/Y_0-\tfrac12(Y_1/Y_0)^2\), where
\(\mathcal L_bY_2=2Y_1'+2NY_1/x+e_N^{(2)}Y_1+e_N^{(4)}Y_0\).
Writing \(Y_2=\sum_{m=-2}^{\infty}q_mx^m\), impose the physical lower
boundary before forming any quotient.  For \(N=0\), the lowest state is
\(\lvert0\rangle\), so \(q_{-2}=q_{-1}=0\) and the resonant equation is
\[
 0=2d_1+e_0^{(4)}.
\]
For \(N=1\), the lowest state is again \(\lvert0\rangle\), now represented
by \(m=-1\); hence \(q_{-2}=0\),
\[
 q_{-1}={2e_1^{(2)}d_{-1}\over-(b-2)},\qquad
 -{q_{-1}\over2}=2(N+1)d_1+e_1^{(4)}.
\]
For \(N\ge2\), the lowest state on this diagonal is
\(\lvert N-2\rangle\), and
\[
 q_m={q_{m-1}+2[2(m+1+N)d_{m+1}+e_N^{(2)}d_m
                    +e_N^{(4)}a_m]\over m(m+b-1)},\quad m=-2,-1,
\]
with \(q_{-3}=0\).  The common resonant equation is
\[
 -{q_{-1}\over2}=2(N+1)d_1+e_N^{(2)}d_0+e_N^{(4)}a_0. \tag{21a}
\]
In all three cases it reproduces exactly the independently known
\(e_N^{(4)}\), with nonexistent lower paths omitted as in (2), and the
coefficients agree with the physical RS recurrence through \(\lambda^8\).
For every nonresonant parameter the complete recurrence is
\[
 q_m={q_{m-1}+2[2(m+1+N)d_{m+1}+e_N^{(2)}d_m
                    +e_N^{(4)}a_m]\over m(m+b-1)},\qquad m\ne0, \tag{21b}
\]
after setting \(q_m=0\) below \(m=\max(-2,-N)\), with \(q_0=0\).

This recurrence has a genuine summed representation.  Put
\[
 g_2=2Y_1'+2NY_1/x+e_N^{(2)}Y_1+e_N^{(4)}Y_0,qquad
 h_2={2g_2\over x^2}.
\]
With the same \(u=Y_0\), \(v_*\), \(x_*\), and
\(W(u,v_*)=x^{-b}\) as in (15),
\[
 Y_2=C_2u+D_2v_*-u(x)\int_{x_*}^{x}v_*(t)h_2(t)t^b\,dt
       +v_*(x)\int_{x_*}^{x}u(t)h_2(t)t^b\,dt. \tag{21c}
\]
The base-chart Laurent conditions above fix \(C_2,D_2\); elsewhere they
are transported analytically.  Twice differentiating (21c), using its
Wronskian, gives exactly the \(Y_2\) equation.  Thus (21c), rather than the
ODE alone, is the Green-operator sum of the second raw subdiagonal.
Although \(Y_2\) is Laurent at \(x=0\), \(z^NY_2(-2\lambda z)\) has no
negative power of \(z\); the coefficient recurrence has factorial decay
on the upper tail, so it is Bargmann--Fock for fixed nonresonant parameters.

The second cumulant also has an explicit local Green representation.  If
\(F_2=2S_1'+e_N^{(4)}-x^2(S_1')^2/2\), then
\[
 S_2=C_{2*}+D_{2*}\int_{x_*}^{x}{ds\over s^bY_0(s)^2}
 +2\int_{x_*}^{x}{ds\over s^bY_0(s)^2}
   \int_{x_*}^{s}t^{b-2}Y_0(t)^2F_2(t)\,dt. \tag{21d}
\]
Direct substitution proves
\(S_2=Y_2/Y_0-\tfrac12(Y_1/Y_0)^2\) with matched normalization.  At a
simple zero \(x_0\) of \(Y_0\), if \(Y_0=A(x-x_0)+\cdots\) and
\(Y_1=C+\cdots\), then \(S_1\sim C/[A(x-x_0)]\) and
\(S_2\sim-C^2/[2A^2(x-x_0)^2]+O((x-x_0)^{-1})\).  The cumulant therefore
does not remove the strongest local singularity: its double pole is needed
to reconstruct the regular additive term
\(Y_2=Y_0(S_2+S_1^2/2)\).  The truncated exponential has essential
singularities at such zeros and is not a global Bargmann function.

In a dominant Bessel sector, direct expansion of (21d) gives
\[
 S_2=-2e_N^{(4)}x^{-1/2}-{e_N^{(4)}\over2}x^{-1}
 +R_2x^{-3/2}+O(x^{-2}), \tag{21e}
\]
where, with \(c=(1-2b)/4\),
\(d=[4(b-1)^2-1]/32\),
\[
 R_2={2\over3}\left\{{(e_N^{(2)})^2\over2}
 +e_N^{(4)}d-{e_N^{(4)}\over2}(1-b/2-c)\right\}.
\]
The first two terms are the second energy and its transport correction;
the \((e_N^{(2)})^2/2\) part comes from the nonlinear term in (21).  Since
(21) follows from the exact normal form, these are the displayed
order-\(\lambda^4\) logarithmic WKB terms in a fixed dominant sector.  They
do not constitute a global connection statement.

For norms and expectation values one must return to the global additive
state.  Its Fock coefficients, for \(m=n-N\), are the rapidly convergent
series
\[
 \widetilde c_n=\sqrt{n!\over N!}\left[
 {(-2)^m\lambda^m\over m!(b)_m}{\bf1}_{m\ge0}
 +(-2)^m\lambda^{m+2}d_m+(-2)^m\lambda^{m+4}q_m\right], \tag{21f}
\]
where absent or unphysical coefficients are zero.  Hence
\[
 \mathcal E_N^{\rm R}=
 {\sum_ne_n|\widetilde c_n|^2+2\lambda\Re\sum_n
 \sqrt{n+1}\,\widetilde c_n^*\widetilde c_{n+1}
  \over\sum_n|\widetilde c_n|^2}. \tag{21g}
\]
This is a stable, non-diagonalization algorithm; the same coefficient
recurrences provide geometric majorants after the tail ratios fall below
one.  Cutoffs 45 and 65 agreed beyond 35 decimal places in the tested
weak-drive cases, with the last retained probability below \(10^{-70}\).

Stationarity makes the energy error quadratic in the Hilbert-space state
error, but the three *upper* diagonals are not the complete perturbative
state at a uniform order for all \(N\).  Direct RS comparison gives
\[
\begin{array}{c|c|c}
N&\|\widetilde\Psi_N-\Psi_N\|&
 \mathcal E_N^{\rm R}-E_N/V\\ \hline
0&O(\lambda^7)&O(\lambda^{14})\\
1&O(\lambda^5)&O(\lambda^{10})\\
2&O(\lambda^4)&O(\lambda^{8})\\
N\ge3&O(\lambda^3)&O(\lambda^{6})
\end{array} \tag{21h}
\]
Thus the quotient determines the exact \(e_N^{(6)}\) for \(N=0,1,2\),
but not for general \(N\ge3\); for \(N=0\) it agrees through
\(e_0^{(12)}\).  These claims were checked against an independent RS
recurrence, not inferred from the quotient itself.

Finally, applying the tridiagonal Hamiltonian to (21f) gives a convergent
residual series and
\[
 \sigma_N^2={\|(h-\mathcal E_N^{\rm R})\widetilde\Psi_N\|^2
 \over\|\widetilde\Psi_N\|^2}.
\]
It always implies \(\operatorname{dist}(\mathcal E_N^{\rm R},
\operatorname{spec}h)\le\sigma_N\).  For \(N=0\) the Rayleigh quotient is
an upper bound to the ground energy; a sharper Temple-type estimate needs
a verified gap.  For \(N>0\) it is not an upper bound to the selected level
without min--max orthogonality and spectral-separation hypotheses.

More generally, the dressed equation
generates a recursive local hierarchy, but every level requires a new
solvability condition and chart transitions at zeros; no closed global
hierarchy has been proved.

As an open direction, a full multiplicative reorganization
\(Y_0\exp(\lambda^2S_1+\lambda^4S_2+\cdots)\) could in principle become a
global Bargmann state only after the entire series and its moving zeros are
controlled.  No finite exponential truncation does so: the cumulants have
poles at zeros of \(Y_0\), their truncated exponential has essential
singularities, and a pure exponential is zero-free while the exact zeros
generally move.  A global representation would likely have to separate a
zero-carrying factor, perhaps a Weierstrass canonical product, from the
exponential part and control Bargmann growth.  Direct multiple scales for
the logarithmic-derivative Riccati equation might formally generate the
exponent, but moving poles, Stokes data, and global Bargmann admissibility
make a practical closure at best local or sectorial.  Riccati
quasilinearization in the sense studied by R. Krivec and V. B. Mandelzweig
is another untested possibility here; the spelling and metadata were checked
against their primary article, *Quasilinearization approach to quantum
mechanics*, Computer Physics Communications **152**, 165--174 (2003),
DOI 10.1016/S0010-4655(02)00821-4.  None of these possibilities is developed
or claimed as a result in the present work.

In a dominant Bessel sector, (r=x^{-1/2}+(1-2b)/(4x)+O(x^{-3/2})), and
(18) gives

\[
 S_1=-2e_N^{(2)}x^{-1/2}
 -\left(2+{e_N^{(2)}\over2}\right)x^{-1}+O(x^{-3/2}). \tag{22}
\]

The \(-2/x\) term is exactly the logarithm of the gauge factor because
\(\lambda/z=-2\lambda^2/x\); the \(x^{-1/2}\) term is the first energy
correction to the eikonal, and the remaining \(e_N^{(2)}/(2x)\) is the
associated transport correction.  This verifies the next nontrivial formal
WKB level sectorially.  It is still a local formal comparison, without a
global connection theorem or uniform error bound.
