# Stage 07c: formal asymptotic solutions at infinity

This note is strictly local and formal. It constructs no analytic solution,
remainder estimate, Bargmann test, or global spectral condition.

## Covering equation and ansatz

The manuscript equation is
\[
z^2\Psi''+(B_1+B_2z)\Psi'+(B_3+qz)\Psi=0,
\quad (B_1,B_2,B_3,q)=
\left(\frac{2\bar F}{V},\frac{2\hbar\omega_0}{V},-\frac{2E}{V},\frac{2F}{V}\right),
\quad q\ne0.
\]
For \(z=t^2\), \(Y(t)=\Psi(t^2)\), the chain rule gives
\[
\Psi'=\frac{Y'}{2t},\qquad
\Psi''=\frac{Y''}{4t^2}-\frac{Y'}{4t^3},
\]
and hence
\[
Y''+\left(\frac{2B_2-1}{t}+\frac{2B_1}{t^3}\right)Y'
+\left(4q+\frac{4B_3}{t^2}\right)Y=0. \tag{1}
\]

Locally set \(A=2B_2-1\), \(C=2B_1\), \(D=4B_3\), choose
\(s^2=-q\), and substitute
\[
Y_\sigma=e^{\lambda_\sigma t}t^\rho f_\sigma(t),\quad
f_\sigma=\sum_{n\ge0}c_n^{(\sigma)}t^{-n},\quad c_0^{(\sigma)}=1.
\]
After removing \(e^{\lambda t}t^\rho\), equation (1) becomes
\[
f''+\left(2\lambda+\frac{2\rho+A}{t}+\frac C{t^3}\right)f'
+\left[\lambda^2+4q+\frac{\lambda(2\rho+A)}t
+\frac{\rho(\rho-1)+A\rho+D}{t^2}
+\frac{\lambda C}{t^3}+\frac{C\rho}{t^4}\right]f=0. \tag{2}
\]
Its constant and \(t^{-1}\) coefficients give
\[
\lambda_\sigma=2\sigma s,\qquad
\rho=-A/2=\frac12-B_2.
\]

## Auditable recurrence

For \(n\ge1\), the coefficient of \(t^{-n-1}\) in (2) is the sum
\[
-2\lambda n c_n,\quad
[(\rho-n+1)(\rho-n)+A(\rho-n+1)+D]c_{n-1},\quad
\lambda Cc_{n-2},\quad
C(\rho-n+3)c_{n-3}.
\]
Therefore, with \(c_{-1}=c_{-2}=0\),
\[
2\lambda_\sigma n c_n^{(\sigma)}=
[(\rho-n+1)(\rho-n)+A(\rho-n+1)+D]c_{n-1}^{(\sigma)}
+\lambda_\sigma Cc_{n-2}^{(\sigma)}
+C(\rho-n+3)c_{n-3}^{(\sigma)}. \tag{3}
\]
Define \(K=\rho^2+(2B_2-2)\rho+4B_3\). With \(m=n-1\), (3) is
the manuscript recurrence
\[
c_{m+1}^{(\sigma)}=
\frac{[m(m+1)+K]c_m^{(\sigma)}+2\lambda_\sigma B_1c_{m-1}^{(\sigma)}
+2B_1(\rho-m+2)c_{m-2}^{(\sigma)}}{2\lambda_\sigma(m+1)}.
\]
It yields
\[
c_1=\frac K{2\lambda},\qquad
c_2=\frac{B_1}{2}+\frac{K(K+2)}{8\lambda^2},
\]
\[
c_3=\frac{K(K+2)(K+6)}{48\lambda^3}
+\frac{B_1(3K+6+4\rho)}{12\lambda}.
\]
Substitution through \(c_3\) cancels the residual through \(t^{-4}\) in
the normalized equation (1); its first generic term is \(t^{-5}\).
Equivalently, after multiplying (1) by \(t^2\), it is \(t^{-3}\), the
equation that determines \(c_4\).

## Sheet exchange and scope

Induction in (3) gives \(c_n^{(-\sigma)}=(-1)^nc_n^{(\sigma)}\). For a
half-turn with \(\operatorname{Log}(-t)=\operatorname{Log}t+\varepsilon i\pi\),
\(\varepsilon=\pm1\), one has \((-t)^\rho=e^{\varepsilon i\pi\rho}t^\rho\)
and \((-t)^{-n}=(-1)^nt^{-n}\). Thus
\[
Y_\sigma(-t)=e^{\varepsilon i\pi\rho}Y_{-\sigma}(t)\quad\text{formally}. \tag{4}
\]
The phase in (4) cannot generally be omitted. The powers \(t^\rho\) and
\(z^{\rho/2}\) require logarithm branches unless their exponents are
integers. This swaps \(e^{2st}\leftrightarrow e^{-2st}\), consistently with
the stage-07a/07b equal-modulus geometry \(\Re(4st)=0\) and constant-phase
geometry \(\Im(4st)=0\). Dominance here means only formal exponential
dominance in a selected sector and on a selected sheet.

## Reproducible verification

Run `python scripts/07c_verify_formal_infinity.py` from the repository root.
SymPy uses commutative symbols with \(q,s\ne0\), followed by the exact
relations \(q=-s^2\), \(\rho=1/2-B_2\). The script independently checks the
chain rule, characteristic and power equations, recurrence shifts and signs,
the displayed coefficients, parity, and the exact generic example
\((B_1,B_2,B_3,q,s)=(2,3,5,-4,2)\) for both signs.
