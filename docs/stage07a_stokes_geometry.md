# Stage 07a: Stokes geometry visualization

The figure `figures/stokes_geometry.pdf` plots only the leading exponential
geometry.  With \(z=t^2\), \(s^2=-q\), and
\(S_\pm(t)=\pm2st\), the exponential difference is
\(\Delta S=4st\).  We use the explicit convention

\[
\operatorname{Re}\Delta S=0\quad\text{(equal modulus; Stokes)},\qquad
\operatorname{Im}\Delta S=0\quad\text{(constant phase; anti-Stokes)}.
\]

The names are secondary to these equations because the literature sometimes
reverses them.  In the \(t\)-plane the curves are the straight lines
\(\operatorname{Re}(st)=0\) and \(\operatorname{Im}(st)=0\).  Opposite
points \(t\) and \(-t\) lie on the two sheets above the same \(z=t^2\), so
each pair of opposite covering rays maps to one physical \(z\)-ray.  However,
\(S_+(-t)=S_-(t)\) and \(S_-(-t)=S_+(t)\).  Thus the exponentials are
single-valued on the \(t\)-cover, while a dominance label in the physical
\(z\)-plane requires a sheet/branch choice.  An ordinary uncut \(z\)-plane
cannot carry globally sheet-independent \(S_+\)- and \(S_-\)-dominance
regions.  If \(q=|q|e^{i\phi}\), the mapped equal-modulus and constant-phase
rays have angles \(-\phi\) and \(\pi-\phi\), respectively.

For the reference case \(q=1\), choose \(s=i\).  If \(t=x+iy\), then
\(\operatorname{Re}(st)=-y\).  Consequently \(e^{S_+}\) dominates in the
lower half-plane and \(e^{S_-}\) in the upper half-plane.  The plotting code
computes each label from the sign of \(\operatorname{Re}(st)\).

Changing \(\arg F=\arg q\) rotates these rays in fixed Bargmann coordinates.
It does not change the spectrum: for \(U_\chi=e^{i\chi N}\),
\(U_\chi H(F)U_\chi^\dagger=H(Fe^{i\chi})\), so all drive phases are
unitarily equivalent and the spectrum depends on \(|F|\), not \(\arg F\).
Changing \(|q|\) cannot change a ray angle; it only rescales
\(\operatorname{Re}\Delta S=4\operatorname{Re}(st)\), strengthening or
weakening the dominance contrast.  The figure fixes \(|q|=1\) and uses
shading only on the covering plane to distinguish its dominance half-planes.

## Proposed LaTeX caption

Stokes geometry of the leading factors
\(S_\pm=\pm2\sqrt{-qz}=\pm2st\), with \(z=t^2\) and \(s^2=-q\).
Our convention is: dashed curves are equal-modulus curves
\(\operatorname{Re}\Delta S=0\) (Stokes), while solid curves are
constant-phase curves \(\operatorname{Im}\Delta S=0\) (anti-Stokes), where
\(\Delta S=4st\).  The exponentials are single-valued on the \(t\)-cover;
opposite points \(t\) and \(-t\) lie above the same \(z\) but exchange
\(S_+\leftrightarrow S_-\), so dominance in the physical \(z\)-plane requires
a sheet/branch choice.  On the cover, blue and orange indicate the regions
where \(e^{S_+}\) and \(e^{S_-}\) dominate, respectively.  Changing \(\arg F=\arg q\)
rotates the geometry in fixed Bargmann coordinates but, because
\(U_\chi H(F)U_\chi^\dagger=H(Fe^{i\chi})\), does not change the spectrum.
The angular geometry is independent of \(|q|\), which controls only the
strength of the exponential contrast.
