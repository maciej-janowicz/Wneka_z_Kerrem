# Local Fedoryuk--Weber wavefunction and energy

## Status and conventions

After the established unitary phase rotation we take `F=|F|>0`, with
`eta=|F|/V`, `delta=hbar omega_0/V`, and
`epsilon=eta^(-2/3)`.  This note starts independently from

\[
 \varepsilon^2u_{yy}=(Q_0+\varepsilon Q_1+\varepsilon^2Q_2)u,
 \quad Q_0=y^{-4}+2ey^{-2}-2y^{-1},
\]
\[
 Q_1=2(\delta-1)y^{-3},\qquad
 Q_2=\delta(\delta-1)y^{-2}.
\]

The result is local and sectorial.  In particular, the **Fedoryuk--Bargmann
orientation hypothesis** is the assertion that the global compensated
Bargmann continuation selects the opposite subdominant sectors centred on
the imaginary local axis.  Stage 09b does not prove that assertion.  Thus a
local Weber zero is not, by itself, a physical eigenvalue.

## Complete close-pair expansion

Put `q=sqrt(epsilon)`,

\[
 y=-1+qX,\qquad
 e=-\frac32+q^2e_1+q^4e_2+\cdots .
\]

Because `d/dy=q^(-1)d/dX`, division of the exact equation by
`epsilon` gives `u_XX=R(X,q)u`, where direct expansion yields

\[
\begin{aligned}
R={}&3X^2+2(e_1+1-\delta)\\
&+q\{10X^3+(4e_1+6-6\delta)X\}\\
&+q^2\{22X^4+(6e_1+12-12\delta)X^2
 +\delta^2-\delta+2e_2\}+O(q^3).
\end{aligned}
\]

The leading and `q^2` coefficients are even, while the first and third
perturbations are odd.  Thus `e1` and `delta` already occur at leading
order; `e2` first occurs in the even `q^2` coefficient.

Set `s=3^(1/4)X`.  Then

\[
 u_{ss}=(s^2+\Lambda)u+qV_1(s)u+O(q^2),\qquad
 \Lambda={2(e_1+1-\delta)\over\sqrt3},
\]
\[
 V_1(s)={10\over3^{5/4}}s^3+
 {4e_1+6-6\delta\over3^{3/4}}s.
\]

Our DLMF convention is
`D_nu(Z)=U(-nu-1/2,Z)`, satisfying
`D_nu''(Z)=(Z^2/4-nu-1/2)D_nu(Z)`.  Hence
`D_nu(sqrt(2)s)` satisfies
`u_ss={s^2-(2nu+1)}u`.

## Sector orientations and connection zeros

The formal exponentials are `exp(+-s^2/2)`.  Their four Stokes boundaries
are `arg s=pi/4+k pi/2`.  The solution with the minus exponential is
subdominant in sectors centred at `0,pi`; the plus exponential is
subdominant in sectors centred at `pi/2,3pi/2`.  These give two inequivalent
opposite-sector problems:

1. **Real-axis pair.**  The solution is `D_nu(sqrt(2)s)`.  The coefficient
   connecting the two real-axis subdominant sectors is proportional to
   `1/Gamma(-nu)`, so its zeros are `nu=n=0,1,...`.  Therefore
   \[
   e_{1,n}^{(R)}=\delta-1-\sqrt3(n+1/2).
   \]
2. **Imaginary-axis pair.**  Put `t=-is`.  Then the leading equation is
   `u_tt=(t^2-Lambda)u`; its subdominant solution is
   `D_nu(sqrt(2)t)=D_nu(-i sqrt(2)s)`.  At the same model zero `nu=n`,
   \[
   e_{1,n}^{(I)}=\delta-1+\sqrt3(n+1/2).
   \]
   Equivalently, the rotation changes `s^2` to `-t^2`, changes the index
   relation from `Lambda=-(2nu+1)` to `Lambda=+(2nu+1)`, and reverses the
   sign in the zero condition.

Adjacent-sector connection formulae relate different canonical solutions
but do not produce a third discrete integer branch.  The corrected 09b
Stokes graph fixes the four local sectors, but not the global sector chain.
Consequently both branches must be retained.  The imaginary-axis branch is
the one consistent with the independent Stage 08 and displaced/Bogoliubov
coefficient; that agreement is a check, not an orientation proof.

At an integer zero define the locally normalized Hermite function

\[
 \phi_n(w)={e^{-w^2/2}H_n(w)\over
 \pi^{1/4}\sqrt{2^n n!}}.
\]

This uses
`D_n(sqrt(2)w)=2^(-n/2)e^(-w^2/2)H_n(w)`.  The leading local solutions are
therefore

\[
 u_{n,R}^{(0)}(X)=\phi_n(3^{1/4}X),\qquad
 u_{n,I}^{(0)}(X)=\phi_n(-i3^{1/4}X).
\]

They are uniform on compact subsets of a close-pair neighbourhood lying in
the selected sectors, with fixed `X` as `epsilon` tends to zero.  The first
is normalized on the real `s` axis; the second on the rotated contour
`t=-is`.  Neither normalization is a global Bargmann normalization.

## Exact pullback to the local Bargmann expression

Since `z=eta^(1/3)y` and `sqrt(epsilon)=eta^(-1/3)`, exactly

\[
 X={y+1\over\sqrt\varepsilon}=z+\eta^{1/3},\qquad
 s=3^{1/4}(z+\eta^{1/3}).
\]

Thus, on a fixed punctured sector carrying a fixed logarithm,

\[
 \Psi_{n,R}^{\rm loc}(z)=z^{-\delta}e^{\eta/z}
 \phi_n\!\left(3^{1/4}(z+\eta^{1/3})\right),
\]
\[
 \Psi_{n,I}^{\rm loc}(z)=z^{-\delta}e^{\eta/z}
 \phi_n\!\left(-i3^{1/4}(z+\eta^{1/3})\right).
\]

An arbitrary local constant may multiply either formula; the displayed
choice fixes the Hermite factor to unit norm on its local real or rotated
axis.  The centre is `z=-eta^(1/3)`, the scaled Gaussian width is
`3^(-1/4)`, and the polynomial degree is `n`.  These independently match
the centre, squeezing scale, and degree of the displaced/Bogoliubov model
for the imaginary-axis candidate after the relevant contour rotation.

The factor `z^(-delta) exp(eta/z)` is a sectorial gauge, not a Bargmann
wavefunction.  The displayed approximation excludes `z=0`, need not be
regular there, and cannot be normalized in the global Bargmann norm.
Cancellation of its branch and essential behaviour is a global connection
problem, not part of this local formula.

## Candidate energies through order one

For fixed `n`, the two local connection problems give

\[
 {E_{n,R}\over V}=-{3\over2}\eta^{4/3}
 +[\delta-1-\sqrt3(n+1/2)]\eta^{2/3}+e_{2,n}^{(R)}
 +O(\eta^{-2/3}),
\]
\[
 {E_{n,I}\over V}=-{3\over2}\eta^{4/3}
 +[\delta-1+\sqrt3(n+1/2)]\eta^{2/3}+e_{2,n}^{(I)}
 +O(\eta^{-2/3}).
\]

The independent local solvability calculation below gives, for both signs,

\[
 e_{2,n}^{(R)}=e_{2,n}^{(I)}=
 {\delta(1-2\delta)\over6}-{6n^2+6n+1\over72}.
\]

These are local Weber results for their stated sector pairs.  Only under the
Fedoryuk--Bargmann orientation hypothesis is the second a conditional
physical energy.  Its agreement with Stage 08/Bogoliubov is an independent
consistency check.  No unconditional physical spectrum is claimed.

## First local wavefunction correction

For the real branch write `u=phi_n+q u1+O(q^2)` and impose intermediate
normalization `<phi_n,u1>=0`.  If

\[
 A={10\over3^{5/4}},\qquad
 B_R={2-2\delta-4\sqrt3(n+1/2)\over3^{3/4}},
\]

let `M_j=<phi_(n+j),(A s^3+B_R s)phi_n>`.  Only
`j=-3,-1,1,3` occur, and

\[
 u_{1,R}=\sum_{j=-3,-1,1,3}-{M_j\over2j}\phi_{n+j},
\]

with negative-index terms omitted.  Explicitly, the `s^3` matrix elements
for these shifts are respectively

\[
 {\sqrt{n(n-1)(n-2)}\over2\sqrt2},\quad
 {3n\sqrt n\over2\sqrt2},\quad
 {3(n+1)\sqrt{n+1}\over2\sqrt2},\quad
 {\sqrt{(n+1)(n+2)(n+3)}\over2\sqrt2},
\]

and the `s` matrix elements are `sqrt(n/2)` and `sqrt((n+1)/2)` for
`j=-1,+1`.  Oddness gives zero diagonal matrix element, so there is no
order-`q` energy correction.

Writing `u1_R=sum c_(j,R) phi_(n+j)`, the four coefficients are

\[
\begin{aligned}
c_{-3,R}&={5\sqrt2\,3^{3/4}\sqrt{n(n-1)(n-2)}\over108},\\
c_{-1,R}&=-{\sqrt2\,3^{1/4}\sqrt n
 (2\delta-\sqrt3 n-2+2\sqrt3)\over12},\\
c_{1,R}&={\sqrt2\,3^{1/4}\sqrt{n+1}
 (2\delta-\sqrt3 n-3\sqrt3-2)\over12},\\
c_{3,R}&=-{5\sqrt2\,3^{3/4}\sqrt{(n+1)(n+2)(n+3)}\over108}.
\end{aligned}
\]

For the imaginary branch the sign must be derived before using oscillator
algebra.  Since `t=-is`, one has

\[
 {d^2\over ds^2}=-{d^2\over dt^2},\qquad s=it,
 \qquad s^3=-it^3.
\]

With
\(B_I=[2-2\delta+4\sqrt3(n+1/2)]/3^{3/4}\), the differential equation is

\[
 v_{tt}=\{t^2-(2n+1)\}v
 +qP_Iv+O(q^2),\qquad P_I=i(At^3-B_It).
\]

Thus harmonic-oscillator form contains `-P_I`, and

\[
 (H_0-2n-1)v_{1,I}=-P_I\phi_n,qquad
 c_{j,I}=-{\langle n+j|P_I|n\rangle_B\over2j}.
\]

The subscript denotes the analytic bilinear Hermite pairing on the oriented
contour `t` from minus to plus infinity, obtained from the imaginary `s`
contour.  There is no complex conjugation.  The corrected coefficients are

\[
\begin{aligned}
c_{-3,I}&={5i\sqrt2\,3^{3/4}\sqrt{n(n-1)(n-2)}\over108},\\
c_{-1,I}&={i\sqrt2\,3^{1/4}\sqrt n
 (2\delta+\sqrt3 n-2\sqrt3-2)\over12},\\
c_{1,I}&=-{i\sqrt2\,3^{1/4}\sqrt{n+1}
 (2\delta+\sqrt3 n-2+3\sqrt3)\over12},\\
c_{3,I}&=-{5i\sqrt2\,3^{3/4}\sqrt{(n+1)(n+2)(n+3)}\over108}.
\end{aligned}
\]

Negative-index states are omitted.  Exact Hermite recurrence substitution
verifies both inhomogeneous equations for `n=0,...,4`; the symbolic matrix
coefficient identities hold for general `n`.  Oddness makes both diagonal
bilinear matrix elements vanish.

## Residuals and second-order solvability

Two checks must be distinguished.  The coefficient check proves
`R-R0=q R1+O(q^2)`; numerically halving `q` halves this difference.  This is
also the differential residual divided by `u0` away from zeros, but is not a
check of the corrected wavefunction.  Direct substitution of
`u^[1]=u0+q u1` into the exact scaled equation instead gives an absolute
residual `O(q^2)`.  No Hermite factor is used as a denominator in the latter
test, so its zeros require no exclusion.  Both orientations and several
fixed `n,delta` values show the predicted factor four when `q` is halved.

At order `q^2`, let `W_R` be the even real-axis coefficient.  Intermediate
normalization gives

\[
 \langle W_R\rangle_B+\langle V_{1,R}u_{1,R}\rangle_B=0.
\]

On rotation, if `T_I=W_s(it)` is the even coefficient, then

\[
 (H_0-2n-1)v_{2,I}=-P_Iv_{1,I}+T_I\phi_n,
 \qquad
 \langle T_I\rangle_B-\langle P_Iv_{1,I}\rangle_B=0.
\]

Using
`<t^2>=n+1/2` and
`<t^4>=3(2n^2+2n+1)/4`, together with every `n+-1,n+-3`
intermediate state, both equations independently reduce to

\[
 e_2={\delta(1-2\delta)\over6}-{6n^2+6n+1\over72}.
\]

The imaginary result agrees exactly with Stage 08, whose displaced-operator
calculation is an external consistency check only.  The contour-bilinear
calculation is local: its normalization is not the Bargmann norm, and its
physical assignment remains conditional on the orientation hypothesis.

The next task is a domain-chain theorem that tracks the compensated origin
germ, all Weber/Airy overlaps, and gauge monodromy.  Only then can one select
the physical orientation and turn a local connection zero into a Bargmann
spectral statement.  A later stage must prove the domain chain and its
connection bounds; the local order-one coefficient does not supply them.
