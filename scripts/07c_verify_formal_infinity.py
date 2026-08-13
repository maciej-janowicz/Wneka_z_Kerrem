"""Deterministic SymPy checks for the stage-07c formal expansion."""
import sympy as sp

t = sp.symbols("t", nonzero=True)
B1, B2, B3, q, s = sp.symbols("B1 B2 B3 q s", nonzero=True)
rho, lam = sp.symbols("rho lam")
A, C, D = 2*B2-1, 2*B1, 4*B3
Y = sp.Function("Y")

# Chain rule checked independently of the displayed target.
pz = sp.diff(Y(t), t)/(2*t)
pzz = sp.diff(pz, t)/(2*t)
raw = sp.expand(t**4*pzz + (B1+B2*t**2)*pz + (B3+q*t**2)*Y(t))
target = t**2/4*(sp.diff(Y(t),t,2)+((2*B2-1)/t+2*B1/t**3)*sp.diff(Y(t),t)+(4*q+4*B3/t**2)*Y(t))
assert sp.simplify(raw-target) == 0

N = 7
c = sp.symbols(f"c0:{N}")
f = sum(c[n]*t**(-n) for n in range(N))
R = sp.diff(f,t,2)+(2*lam+(2*rho+A)/t+C/t**3)*sp.diff(f,t)+(lam**2+4*q+lam*(2*rho+A)/t+(rho*(rho-1)+A*rho+D)/t**2+lam*C/t**3+C*rho/t**4)*f
assert sp.simplify(sp.expand(R).coeff(t,0)-(lam**2+4*q)*c[0]) == 0
assert sp.simplify(sp.expand(R).coeff(t,-1).subs(q,-lam**2/4)-lam*(2*rho+A)*c[0]) == 0
for n in range(1,5):
    got = sp.expand(R).coeff(t,-n-1).subs(q,-lam**2/4).subs(rho,-A/2)
    want = -2*lam*n*c[n]+((rho-n+1)*(rho-n)+A*(rho-n+1)+D)*c[n-1]+lam*C*(c[n-2] if n>=2 else 0)+C*(rho-n+3)*(c[n-3] if n>=3 else 0)
    want = want.subs(rho,-A/2)
    assert sp.simplify(got-want) == 0

K = rho**2+(2*B2-2)*rho+4*B3
c1 = K/(2*lam)
c2 = B1/2+K*(K+2)/(8*lam**2)
c3 = K*(K+2)*(K+6)/(48*lam**3)+B1*(3*K+6+4*rho)/(12*lam)
vals = {c[0]:1,c[1]:c1,c[2]:c2,c[3]:c3, **{c[j]:0 for j in range(4,N)}}
for sig in (-1,1):
    num = {B1:2,B2:3,B3:5,q:-4,s:2,lam:4*sig,rho:sp.Rational(-5,2)}
    residual = sp.expand(R.subs(vals).subs(num))
    assert all(residual.coeff(t,k)==0 for k in (0,-1,-2,-3,-4))
    assert residual.coeff(t,-5) != 0
for n, cn in enumerate((sp.Integer(1),c1,c2,c3)):
    assert sp.simplify(cn.subs(lam,-lam)-(-1)**n*cn) == 0
print("PASS chain rule; characteristic and power equations")
print("PASS recurrence n=1,...,4; c1,c2,c3")
print("PASS normalized residual O(t^-5) (O(t^-3) after multiplication by t^2)")
print("PASS coefficient parity under sheet-label exchange")
