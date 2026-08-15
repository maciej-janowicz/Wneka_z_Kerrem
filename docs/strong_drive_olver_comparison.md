# Strong-drive Olver comparison and quantization

This note records the derivation integrated into the manuscript.  It is
deliberately explicit about the remaining global gap.

For positive drive, phase equivalence gives

\[
B_1=q=2\eta,\quad B_2=2\delta,\quad B_3=-2E/V,
\quad \eta=|F|/V.
\]

The definitions of \(D,H,C\) then yield

\[
w''=\left[-8\eta-C/t^2-8\eta(1-\delta)/t^4+4\eta^2/t^6\right]w,
\quad C=-8E/V+4\delta-4\delta^2-3/4.
\]

Balancing terms derives \(t=\eta^{1/6}x\), \(E/V=\eta^{4/3}e\), and
\(u=\eta^{2/3}\).  The scaled equation is

\[
w_{xx}=(u^2f+ug+h)w,
\quad f=4x^{-6}+8ex^{-2}-8,
\quad g=-8(1-\delta)x^{-4},
\quad h=(4\delta^2-4\delta+3/4)x^{-2}.
\]

With \(P(y;e)=1+2ey^2-2y^3\),

\[
P_y=4ey-6y^2=2y(2e-3y).
\]

A nonzero double root therefore has \(e=3y/2\); substitution gives
\(1+y^3=0\).  The real branch is \(y=-1\), \(e_0=-3/2\), and

\[
1-3y^2-2y^3=-(y+1)^2(2y-1).
\]

The local geometry selects \(x=i\), with \(x=-i\) on the other covering
sheet.  Both map to the negative Bargmann axis, and the negative classical
displacement suggests that this is the physically relevant pair.  Proving
that the actual global continuation contour traverses it still requires the
missing progressive-path construction and global connection map; the sheet
argument is motivation, not that proof.

Olver's two-coalescing-turning-point construction selects the Weber equation.
The manuscript defines the action-preserving variable \(\zeta\), its branch,
canonical rotated parabolic-cylinder solutions, the mapped progressive
paths, the exact transformed remainder, and the variation-of-constants
integral.  It supplies an absolute envelope bound conditional on finiteness
of that variation.  Uniform finiteness on a single domain extending from the
irregular origin through the turning pair to infinity has not been proved.
Accordingly the global Weber approximation and connection step are explicitly
conditional.

For \(p=d\zeta/dx\), \(W=p^{1/2}w\), direct differentiation of
\(w=p^{-1/2}W\) gives the exact Liouville contribution

\[
p^{-1/2}\frac{d^2}{d\zeta^2}p^{1/2}
=\left(\frac{dx}{d\zeta}\right)^{1/2}
 \frac{d^2}{d\zeta^2}
 \left(\frac{dx}{d\zeta}\right)^{-1/2}
=-\frac34p^{-4}p_x^2+\frac12p^{-3}p_{xx}.
\]

At the double point,

\[
f_{xx}/2=48,\quad f_e=-8,\quad g=-8(1-\delta).
\]

For \(e=e_0+e_1/u+\cdots\) and
\(X=48^{1/4}u^{1/2}(x-i)\), the local equation is

\[
w_{XX}=(X^2+\lambda)w,\qquad
\lambda=-2(e_1+1-\delta)/\sqrt3.
\]

Since \(D_n(\sqrt2X)\) has \(\lambda=-2n-1\), the canonical Weber zero gives

\[
E_n/V=-\tfrac32\eta^{4/3}+
[\delta+\sqrt3(n+\tfrac12)-1]\eta^{2/3}+O(1),
\]

for fixed \(n\).  The first coefficient is fixed rigorously by the double
root.  The second is conditional on the unfinished global identification of
the physical connection zero with the canonical Weber zero.

The exact, already proved entireness statement remains

\[
\Delta_{\rm WI}(2\eta,2\delta,-2E/V,2\eta)=0.
\]

It is inherited from the earlier entireness theorem, not derived as an Olver
connection condition.  Conditional on existence of canonical sectorial
solutions covering a punctured origin neighbourhood, holomorphic patching
would require all inadmissible Stokes coefficients to vanish.  Those
coefficients are only formally defined: their global construction,
evaluation, and reduction to one physical scalar condition remain open.  No
infinity exponential is discarded.
The outer modified-Bessel model is retained only at infinity because its
omitted inverse-sixth-power term is leading in the turning region.  Its
comparison error and its own asymptotic truncation error are distinct.

Finally, displacement by \(a=b-r\), \(r^3+\delta r=\eta\), gives exactly

\[
\begin{aligned}
H/V={}&\tfrac12r^4+\delta r^2-2\eta r
 +(2r^2+\delta)b^\dagger b
 +\tfrac12r^2(b^{\dagger2}+b^2)\\
&-r(b^{\dagger2}b+b^\dagger b^2)+\tfrac12b^{\dagger2}b^2.
\end{aligned}
\]

Thus \(A=2r^2+\delta\) and
\(\Omega^2=(2r^2+\delta)^2-r^4\).  The corrected quadratic Bogoliubov
reduction still reproduces the two displayed coefficients; its correction
begins at order one.  Cubic and quartic fluctuations also contribute there,
so no constant coefficient is claimed.
