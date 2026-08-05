# Stage 07: sectorial asymptotic existence and error bounds

## Exact covering normal form

The verified equation is

\[
z^2\Psi''+(B_1+B_2z)\Psi'+(B_3+qz)\Psi=0,\qquad q\ne0.
\]

With \(z=t^2\), direct differentiation gives

\[
t^2Y''+\left[(2B_2-1)t+\frac{2B_1}{t}\right]Y'
 +(4B_3+4qt^2)Y=0.
\]

Independent substitution of

\[
Y=t^{1/2-B_2}\exp\!\left(\frac{B_1}{2t^2}\right)w
\]

and transformation of the Stage 06 Liouville normal form both give

\[
w''=(a_\sigma^2+g)w,\qquad a_\sigma=2\sigma s,qquad s^2=-q,
\]

\[
g(t)=-\frac{C}{t^2}-\frac{4H}{t^4}+\frac{B_1^2}{t^6},\qquad
D=B_3+\frac{B_2}{2}-\frac{B_2^2}{4},\quad
H=B_1\left(1-\frac{B_2}{2}\right),\quad C=4D-\frac34.
\]

Thus \(a_\sigma^2=-4q\), independently of the label. The covering changes
the ramified rank-\(1/2\) infinity into an unramified rank-1 point, and
\(g=O(t^{-2})\) is integrable toward infinity.

## Holomorphic domains and coherent paths

First fix \(\sigma\in\{+1,-1\}\). Then choose \(|d|=1\) with
\(\Re(a_\sigma d)\le0\), choose a sufficiently large \(R>0\), and put

\[
\Omega_{d,R}=\{t:x_d(t):=\Re(\overline d t)>R\},\qquad
\Gamma_d(t)=\{t+sd:s\ge0\}.
\]

This is a simply connected half-plane avoiding zero. Every complete translated
tail remains in the domain and, oriented from \(t\) to infinity, satisfies

\[
\Re[a_\sigma(u-t)]=s\Re(a_\sigma d)\le0.
\]

For \(w_{\sigma,d}=e^{a_\sigma t}h_{\sigma,d}\), variation of constants gives

\[
h_{\sigma,d}(t)=1+\int_{\Gamma_d(t)}
K_\sigma(t,u)g(u)h_{\sigma,d}(u)\,du,\qquad
K_\sigma(t,u)=\frac{e^{2a_\sigma(u-t)}-1}{2a_\sigma}.
\]

Here \(K(t,t)=0\), \(K_t=-e^{2a_\sigma(u-t)}\), and
\(K_{tt}+2a_\sigma K_t=0\). Consequently, differentiation, including the
lower-endpoint term, recovers \(h''+2a_\sigma h'=gh\). The progressive
inequality gives \(|K|\le1/|a_\sigma|\).

Since \(|t+sd|\ge x_d(t)+s\),

\[
I_d(t):=\int_0^\infty|g(t+sd)|\,ds
\le \frac{|C|}{x_d(t)}+\frac{4|H|}{3x_d(t)^3}
 +\frac{|B_1|^2}{5x_d(t)^5}=:M_d(t).
\]

With \(G_d=I_d/|a_\sigma|\), successive approximations are bounded by
\(G_d^n/n!\) and converge locally uniformly. Each iterate is holomorphic;
the fixed-\(s\) integrands and their derivatives have locally uniform
integrable majorants. Weierstrass' theorem makes the limit holomorphic, and
differentiation under the integral recovers the ODE. The unique normalized
solution \(h_{\sigma,d}\) satisfies throughout \(\Omega_{d,R}\)

\[
|h_{\sigma,d}-1|\le e^{G_d}-1,\qquad
|h_{\sigma,d}'|\le I_d e^{G_d},
\]

uniformly as \(x_d(t)\to\infty\). Equality
\(\Re(a_\sigma d)=0\) is permitted: the kernel remains bounded and all
integrals still converge.
The construction for \(-\sigma\) generally requires a different progressive
direction and hence a different half-plane or sector.

Let \(\mathcal D\) be a connected closed arc of admissible unit directions
for this fixed \(\sigma\), and set
\(\mathcal S_{\sigma,R}=\bigcup_{d\in\mathcal D}\Omega_{d,R}\).
This is the precise glued sectorial domain. For neighboring directions assume
\(\Re(\overline d_1d_2)>0\). If
\(t\in\Omega_{d_1,R}\cap\Omega_{d_2,R}\), then for every \(s\ge0\)

\[
x_{d_1}(t+sd_2)=x_{d_1}(t)+s\Re(\overline d_1d_2)>R,
\qquad x_{d_2}(t+sd_2)=x_{d_2}(t)+s>R.
\]

Thus the complete \(d_2\)-ray remains in the overlap. The function constructed
along \(d_1\) is holomorphic there, and
\(x_{d_1}(t+sd_2)\to\infty\), so it and its derivative have the required
normalization along the \(d_2\)-ray. Variation of constants along that complete
ray shows that it satisfies the same \(d_2\)-Volterra equation. Uniqueness of
that equation identifies \(w_{\sigma,d_1}=w_{\sigma,d_2}\) on the overlap.
A finite chain of sufficiently close directions gives consecutive overlap
identities and glues the half-plane solutions holomorphically on exactly
\(\mathcal S_{\sigma,R}\).

For the radial path from \(t=re^{i\theta}\), take \(d=e^{i\theta}\). Then
\(x_d(t)=|t|\), and the preceding bound reduces to

\[
\int_{|t|}^{\infty}|g(re^{i\theta})|\,dr
\le\frac{|C|}{|t|}+\frac{4|H|}{3|t|^3}
 +\frac{|B_1|^2}{5|t|^5}.
\]

This radial formula is a proved corollary, not an estimate transferred to a
nonradial contour.

## First coefficient and holomorphic remainder

Set \(b_\sigma=C/(2a_\sigma)\), \(h_0=1+b_\sigma/t\), and
\(Lh=h''+2a_\sigma h'-gh\). Exact substitution gives

\[
Lh_0=\frac{b_\sigma(C+2)}{t^3}+\frac{4H}{t^4}
 +\frac{4Hb_\sigma}{t^5}-\frac{B_1^2}{t^6}
 -\frac{B_1^2b_\sigma}{t^7}.
\]

For \(\rho_{\sigma,d}=h_{\sigma,d}-h_0\), the correct inhomogeneous equation is
\(L\rho_{\sigma,d}=-Lh_0\). Its Volterra equation therefore has inhomogeneous term
\(-Lh_0\); only the absolute-value estimate loses this sign. Define

\[
J_{\sigma,d}(t)=\frac1{|a_\sigma|}
 \int_{\Gamma_d(t)}|Lh_0(u)|\,|du|.
\]

Then

\[
|\rho_{\sigma,d}(t)|\le J_{\sigma,d}(t)e^{G_d(t)},
\]

and \(|a_\sigma|J_{\sigma,d}\) is at most

\[
\frac{|b_\sigma(C+2)|}{2x_d^2}+\frac{4|H|}{3x_d^3}
 +\frac{|Hb_\sigma|}{x_d^4}+\frac{|B_1|^2}{5x_d^5}
 +\frac{|B_1|^2|b_\sigma|}{6x_d^6}.
\]

Thus \(\rho_{\sigma,d}\) is holomorphic and uniformly \(O(x_d^{-2})\) on the
half-plane, hence \(O(t^{-2})\) on covered closed proper subsectors. The
coefficient \(b_\sigma=C/(2a_\sigma)\) equals the Stage 05 recurrence value.
Undoing the exact transformation yields

\[
\Psi_\sigma(z)
=
e^{2\sigma\sqrt{-qz}}z^{1/4-B_2/2}
\left[
1+u_1^{(\sigma)}z^{-1/2}+O(z^{-1})
\right],\qquad
u_1^{(\sigma)}=\frac{C}{2a_\sigma},
\]

uniformly on the stated closed proper sector images.

## Phase geometry and limitations

For \(q=|q|e^{i\phi}\), \(z=re^{i\theta}\), with angles modulo \(2\pi\):

- equal moduli occur when \(\Re\sqrt{-qz}=0\), hence
  \(\theta=-\phi\pmod{2\pi}\); this paper calls it the Stokes ray;
- maximal separation occurs when \(\Im\sqrt{-qz}=0\), hence
  \(\theta=\pi-\phi\pmod{2\pi}\); this paper calls it the anti-Stokes ray.

On the cover these are \(\Re(st)=0\) and \(\Im(st)=0\). Opposite covering
rays are identified by \(z=t^2\). Locating them does not determine Stokes
multipliers.

The construction is Olver's fixed-parameter integral-equation error-control
method; no large parameter is introduced. It establishes actual holomorphic
sectorial solutions, uniqueness, explicit uniform bounds, and the first
coefficient. It does not establish Stokes switching or multipliers, global
connection coefficients, an analytic/entire origin solution, a Bargmann
determinant, quantization, eigenvalue asymptotics, or finite-turning-point
uniformization. Dominance refers only to relative exponential size and does
not exclude either branch from Bargmann space.

## Verification

`src/kerr_heun/olver.py` provides exact coefficient and error-control helpers.
`tests/test_olver.py` independently substitutes the exact gauge factor using
Laurent dictionaries, checks disappearance of the first derivative, exercises
the public kernel through centered finite differences and a numerical
integral-equation differentiation check, compares both signs with Stage 05,
and verifies the explicit majorants and invalid-input handling.
