# Stage 05: Taylor series and formal infinity expansions

## 1. Equation and scope

The normalized driven equation is

\[
z^2\Psi''+(B_1+B_2z)\Psi'+(B_3+qz)\Psi=0,\qquad B_1\ne0,
\]

with

\[
B_1=\frac{2\overline F}{V},\quad
B_2=\frac{2\hbar\omega_0}{V},\quad
B_3=-\frac{2E}{V},\quad
q=\frac{2F}{V}.
\]

Multiplying the original Bargmann equation by \(2/V\) verifies this map
identically. Algebraically the four parameters may be continued independently.
On the physical slice, \(V>0\), \(B_2\) is real, and
\(q=\overline{B_1}\); \(F\) and \(\overline F\) are not independent.

## 2. Taylor coefficients at the irregular origin

Let

\[
\Psi=\sum_{n\ge0}c_nz^n,\qquad c_{-1}=0,\qquad c_0=1.
\]

The coefficient of \(z^n\) in the four terms of the equation is,
respectively,

\[
n(n-1)c_n,\quad B_1(n+1)c_{n+1},\quad
B_2nc_n,\quad B_3c_n+qc_{n-1}.
\]

Therefore

\[
B_1(n+1)c_{n+1}+A_nc_n+qc_{n-1}=0,\qquad
A_n=n(n-1)+B_2n+B_3.
\]

Set

\[
A_1=B_2+B_3,\quad A_2=2+2B_2+B_3,\quad
A_3=6+3B_2+B_3.
\]

Successive use of the recurrence gives

\[
\begin{aligned}
c_1={}&-\frac{B_3}{B_1},\\
c_2={}&\frac{B_3A_1-qB_1}{2B_1^2},\\
c_3={}&\frac{qB_1(A_2+2B_3)-B_3A_1A_2}{6B_1^3},\\
c_4={}&\frac{
A_3B_3A_1A_2-qB_1A_3(A_2+2B_3)
-3qB_1B_3A_1+3q^2B_1^2}{24B_1^4}.
\end{aligned}
\]

For the physical parameters define

\[
d_n=\frac V2n(n-1)+\hbar\omega_0n,\qquad
R_n=E-d_n,\qquad g=|F|^2.
\]

Then the same coefficients are

\[
\begin{aligned}
c_1={}&\frac{E}{\overline F},\\
c_2={}&\frac{R_1E-g}{2\overline F^2},\\
c_3={}&\frac{R_2(R_1E-g)-2gE}{6\overline F^3},\\
c_4={}&\frac{R_3[R_2(R_1E-g)-2gE]-3g(R_1E-g)}
{24\overline F^4}.
\end{aligned}
\]

An independent symbolic expansion of the differential operator, rather than
reuse of the generator, returned zero coefficients through \(z^3\). Thus the
displayed polynomial has residual \(O(z^4)\), as expected when its
unspecified \(c_5\) term is omitted.

The implementation

```python
taylor_coefficients(B1, B2, B3, q, order)
```

returns `[c_0, ..., c_order]`. It performs no scalar conversion, so
`fractions.Fraction`, symbolic scalar objects, complex numbers, and
`mpmath` arbitrary-precision values retain their arithmetic. It rejects a
negative or nonintegral order and \(B_1=0\).

## 3. Transformation at infinity

Put \(z=t^2\) and \(Y(t)=\Psi(t^2)\). Direct differentiation gives

\[
\Psi'=\frac{Y'}{2t},\qquad
\Psi''=\frac{Y''}{4t^2}-\frac{Y'}{4t^3},
\]

and hence

\[
t^2Y''+\left[(2B_2-1)t+\frac{2B_1}{t}\right]Y'
+(4B_3+4qt^2)Y=0.
\]

Use

\[
Y=e^{a_\sigma t}t^p f(t),\qquad
f(t)=\sum_{n\ge0}u_n^{(\sigma)}t^{-n},\qquad u_0^{(\sigma)}=1.
\]

The \(t^2\) and \(t^1\) balances yield

\[
a_\sigma^2+4q=0,\qquad
2p+2B_2-1=0.
\]

For a chosen square root \(s=\sqrt{-q}\),

\[
a_\sigma=2\sigma s,\qquad p=\frac12-B_2,\qquad
r=\frac p2=\frac14-\frac{B_2}{2}.
\]

This proves that integer powers of \(z^{-1}\) are not generally closed:
differentiation of \(e^{a_\sigma\sqrt z}\) introduces \(z^{-1/2}\). The
closed scale is \(t^{-n}=z^{-n/2}\).

After removal of \(e^{a_\sigma t}t^p\), the equation for \(f\) is

\[
t^2f''+2a_\sigma t^2f'+\frac{2B_1}{t}f'
+Cf+\frac{2a_\sigma B_1}{t}f+\frac{2B_1p}{t^2}f=0,
\]

where

\[
C=p^2+(2B_2-2)p+4B_3
=-\frac{4B_2^2-8B_2-16B_3+3}{4}.
\]

Equating the coefficient of \(t^{-m}\) gives, with \(u_j=0\) for \(j<0\),

\[
u_{m+1}^{(\sigma)}
=\frac{[m(m+1)+C]u_m^{(\sigma)}
+2a_\sigma B_1u_{m-1}^{(\sigma)}
+2B_1(p-m+2)u_{m-2}^{(\sigma)}}
{2a_\sigma(m+1)}.
\]

The first coefficients simplify to

\[
\begin{aligned}
u_1^{(\sigma)}={}&\frac{C}{2a_\sigma},\\
u_2^{(\sigma)}={}&\frac{B_1}{2}
+\frac{C(C+2)}{8a_\sigma^2},\\
u_3^{(\sigma)}={}&
\frac{C(C+2)(C+6)}{48a_\sigma^3}
+\frac{B_1(3C+6+4p)}{12a_\sigma}.
\end{aligned}
\]

Substitution independent of the generator cancels the reduced residual
coefficients \(t^0,t^{-1},t^{-2}\). With the series truncated after \(u_3\),
the first uncancelled reduced order is \(t^{-3}=z^{-3/2}\); it is cancelled
by the recurrence value of \(u_4\). No convergence is claimed.

The implementation

```python
asymptotic_coefficients(
    B1, B2, B3, q, order,
    sigma=+1,
    sqrt_minus_q=chosen_root,
)
```

returns `[u_0, ..., u_order]`. The explicit `sqrt_minus_q` argument records
the branch and supports exact or arbitrary-precision scalar types. Exact
rational pairs are checked by exact equality. Numerical real and complex
pairs must satisfy
\[
|s^2+q|\leq 10^{-12}\max(1,|s^2|,|q|).
\]
For symbolic inputs, a decisive exact equality or `equals(0)` result is
honored; if the symbolic relation is genuinely undecidable, consistency
remains the caller's responsibility. The routine rejects \(q=0\), a zero or
demonstrably inconsistent root, invalid order, and
\(\sigma\notin\{-1,1\}\), without selecting a principal root.

## 4. Branch and sector convention

Choose a simply connected sector and a logarithm there. Define

\[
\sqrt{-qz}=\exp\!\left(\frac12\Log(-qz)\right),\qquad
z^r=\exp(r\Log z).
\]

The \(\sigma\) branch is dominant where
\(\Re(\sigma\sqrt{-qz})>0\), subdominant where it is negative, and of equal
exponential magnitude where it vanishes.

This note calls the rays

\[
\Re\sqrt{-qz}=0
\]

**Stokes rays** (equal exponential magnitudes), and the rays

\[
\Im\sqrt{-qz}=0
\]

**anti-Stokes rays** (maximal growth/decay). Some literature reverses these
names, so the equations are the operative convention.

With the chosen value \(s=\sqrt{-q}\) held fixed, changing only
\(\sigma\mapsto-\sigma\) gives
\(u_n^{(-\sigma)}=(-1)^nu_n^{(\sigma)}\). In contrast, the simultaneous
change \((\sigma,s)\mapsto(-\sigma,-s)\) leaves
\(a_\sigma=2\sigma s\), and hence the coefficient sequence, unchanged.

Under the analytic continuation \(z\mapsto ze^{2\pi i}\), one
counterclockwise circuit of \(z\) around the origin in the finite
\(z\)-plane, \(\sqrt z\mapsto-\sqrt z\),
\(z^r\mapsto e^{2\pi ir}z^r\), and
\(z^{-n/2}\mapsto(-1)^nz^{-n/2}\). Thus the two exponential expressions are
interchanged (equivalently relabelled with the fixed \(s\)), while the
half-integer formal series acquires its termwise factors \((-1)^n\), apart
from the algebraic monodromy factor. This is a formal statement, not a
connection-matrix or Stokes-multiplier calculation.

## 5. Exactly undriven boundary

At \(F=\overline F=0\), also \(B_1=q=0\), and the equation is Euler:

\[
z^2\Psi''+B_2z\Psi'+B_3\Psi=0.
\]

For \(\Psi=z^\rho\),

\[
\rho(\rho-1)+B_2\rho+B_3=0.
\]

The Bargmann monomial norm is
\(\|z^n\|_{\mathrm B}^2=n!\). Therefore

\[
\Psi_n(z)=\frac{z^n}{\sqrt{n!}},\qquad
E_n=\hbar\omega_0n+\frac V2n(n-1).
\]

This point is singular relative to both generators. For \(n>0\),
\(\Psi_n(0)=0\), so the normalization \(c_0=1\) is unavailable; division by
\(B_1\) fails; and the square-root exponential scale collapses at \(q=0\).
The exactly degenerate point is not a derivation of the physical limit
\(F\to0\), and the excited-state \(c_0=1\) normalization is not continuous
there.

## 6. Verification

`tests/test_local_series.py` independently checks:

- exact rational Taylor coefficients and differential-equation residuals;
- arbitrary order through order 12;
- complex and 80-digit arithmetic;
- invalid orders and \(B_1=0\);
- both infinity signs and the three explicit coefficients;
- formal residual cancellation through the generated order;
- fixed-root parity with one complex \(s=\sqrt{-q}\) held fixed and only
  \(\sigma\mapsto-\sigma\), verifying
  \(u_n^{(-\sigma)}=(-1)^nu_n^{(\sigma)}\) through \(n=8\), with even and
  odd orders checked separately;
- the distinct branch/sign relabelling
  \((\sigma,s)\mapsto(-\sigma,-s)\), which leaves \(a_\sigma\) and the
  coefficient sequence unchanged;
- acceptance of both exact roots \(s=2\) and \(s=-2\) for \(q=-4\), and
  rejection of the inconsistent pair \(q=7,\ s=123\);
- validation of a complex floating-point pair and numerical enforcement of
  \(|s^2+q|\leq10^{-12}\max(1,|s^2|,|q|)\), including acceptance of the
  tested \(4\times10^{-13}\) relative root perturbation and rejection of the
  tested \(2\times10^{-12}\) perturbation;
- rejection of the degenerate \(q=0,\ s=0\) input;
- exact coefficient-level application of
  \[
  \mathcal L_E=\frac V2z^2\frac{d^2}{dz^2}
  +\hbar\omega_0z\frac{d}{dz}-E
  \]
  to the full monomial \(z^n\), verifying the undriven eigenpairs for
  \(n=0,1,2,3,5,8\).
