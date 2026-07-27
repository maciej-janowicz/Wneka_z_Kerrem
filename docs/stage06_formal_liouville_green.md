# Stage 06: formal Liouville–Green approximation at infinity

## Exact normal form

The normalized Bargmann equation is

\[
z^2\Psi''+(B_1+B_2z)\Psi'+(B_3+qz)\Psi=0,
\]

where $B_1=2\overline F/V$, $B_2=2\hbar\omega_0/V$,
$B_3=-2E/V$, and

\[
q=\frac{2F}{V}\in\mathbb C.
\]

The drive $F$, and hence $q$, may be genuinely complex; neither is assumed
real or positive. For real $V$, $B_1=2F^*/V=q^*$. After division by $z^2$,
$P=B_2/z+B_1/z^2$ and $Q=q/z+B_3/z^2$. Therefore

\[
\Psi=\exp\left(-\frac12\int P,dz\right)\Phi
=z^{-B_2/2}e^{B_1/(2z)}\Phi
\]

gives (Phi''+R\Phi=0), with

\[
R=Q-\frac{P'}2-\frac{P^2}4
=\frac qz+\frac D{z^2}+\frac H{z^3}-\frac{B_1^2}{4z^4},
\]

\[
D=B_3+\frac{B_2}{2}-\frac{B_2^2}{4},\qquad
H=B_1\left(1-\frac{B_2}{2}\right).
\]

This agrees term by term with the manuscript's earlier normal form under
((B_1,B_2,B_3,q)=(\beta,\alpha,-\mathcal E,\gamma)). The only finite
singularity is (z=0); generically it is a fourth-order pole. At infinity,
(R=q/z+O(z^{-2})). Coefficient cancellations can lower the pole order at
zero; (q=0) removes the ramified infinity scale entirely.

## Momentum, branches, and expansion

On a simply connected sector at infinity fix branches of $\sqrt q$ and
$\sqrt z$, and set

\[
s:=i\sqrt q,\qquad s^2=-q.
\]

For $q\ne0$, require the compatible product branch
$\sqrt{-qz}=s\sqrt z$, and define

\[
p=\sqrt{-R}\sim sz^{-1/2}(1+c_1z^{-1}+c_2z^{-2}+c_3z^{-3}+\cdots)
\]

using the root asymptotic to (sz^{-1/2}). Squaring and matching (-R)
gives

\[
c_1=\frac D{2q},\quad
c_2=\frac H{2q}-\frac{D^2}{8q^2},\quad
c_3=-\frac{B_1^2}{8q}-\frac{DH}{4q^2}+\frac{D^3}{16q^3}.
\]

Consequently,

\[
\int^z p(t),dt
=2s\sqrt z+\frac D{s}z^{-1/2}-\frac{sc_2}{3}z^{-3/2}+\cdots,
\]

and

\[
p^{-1/2}=s^{-1/2}z^{1/4}
\left(1-\frac D{4q}z^{-1}+O(z^{-2})\right).
\]

The omitted integration constant only changes normalization. Changing the
branch of $\sqrt q$, so that $s\mapsto-s$, merely interchanges the labels
$\sigma=+1$ and $\sigma=-1$. For the fixed branch of $\sqrt z$, the
$\sigma$ solution grows where $\Re(\sigma s\sqrt z)>0$, decays where it is
negative, and has equal exponential magnitude where it vanishes. Thus the
asymptotic sectors depend on $\arg(F)=\arg(q)$. Crossing a cut continues the
branches and can likewise relabel the two solutions. With the sheet fixed, equal
exponential magnitude occurs on
(Re\int^z p(t),dt=0); real action occurs on
(Im\int^z p(t),dt=0). These equations, not the non-universal names
“Stokes” and “anti-Stokes”, define the curves here.

## Direct-series comparison and transport

Undoing the Liouville transformation in
(Phi_\sigma^{[0]}=p^{-1/2}e^{\sigma\int p}) gives

\[
\Psi_\sigma^{[0]}\sim e^{2\sigma s\sqrt z}
z^{1/4-B_2/2}\left[1+\frac{\sigma D}{s}z^{-1/2}+O(z^{-1})\right].
\]

Stage 05 uses (a_\sigma=2\sigma s),
(p_\mathrm{Stage05}=1/2-B_2), and

\[
C=p_\mathrm{Stage05}^2+(2B_2-2)p_\mathrm{Stage05}+4B_3
=4D-\frac34.
\]

Thus its exact coefficient is

\[
u_1^{(\sigma)}=\frac{C}{2a_\sigma}
=\frac{D}{\sigma s}-\frac{3}{16\sigma s}.
\]

| quantity | Stage 05 direct series | leading WKB | corrected WKB |
|---|---:|---:|---:|
| (sqrt z) rate | (2\sigma s) | (2\sigma s) | (2\sigma s) |
| algebraic power | (1/4-B_2/2) | same | same |
| (u_1^{(\sigma)}) | (D/(\sigma s)-3/(16\sigma s)) | (D/(\sigma s)) | (D/(\sigma s)-3/(16\sigma s)) |

For (S=\Phi'/\Phi), (S'+S^2=p^2). The minimum next Riccati step is

\[
S_\sigma=\sigma p-\frac{p'}{2p}
+\sigma\left(\frac{p''}{4p^2}-\frac{3p'^2}{8p^3}\right)+\cdots.
\]

The parenthesis is (3z^{-3/2}/(32s)+O(z^{-5/2})), whose integral is
(-3z^{-1/2}/(16s)+O(z^{-3/2})). It supplies precisely the part absent
from leading WKB. Hence the rate and power agree already at leading order;
(u_1) agrees only after first transport.

## Assumptions and verification

The construction assumes (q\ne0), a nonzero explicit root (s^2=-q), a
fixed simply connected sector and sheet, and avoidance of zeros of (R).
Ordinary WKB becomes singular at those turning points. The calculation is
formal: it supplies neither uniform error bounds nor an asymptotic-existence
theorem. Those limitations are the reason for the later Olver analysis.

`src/kerr_heun/liouville_green.py` encodes the exact normal-form,
square-root, phase, prefactor, and first-transport coefficients without a
new symbolic dependency. Exact-rational tests independently check the
Liouville collection, square the truncated momentum to reconstruct (-R),
compare both signs with the Stage 05 generator for multiple nondegenerate
parameter sets, and reject zero, inconsistent-root, invalid-sign, and
singular-evaluation inputs. Numerical checks are not used as proof.

No unresolved algebraic discrepancy was found. Uniformity near turning
points and rigorous sectorial error bounds remain intentionally unresolved.
