# Physical literature review: closed one-photon-driven Kerr quasienergies

## Scope and source standard

This review asks a deliberately narrow question: what was already known about
the spectrum and eigenstates of

\[
H={V\over2}a^{\dagger2}a^2+\hbar\omega_0a^\dagger a+
  F a^\dagger+\bar F a
\]

as a **closed** rotating-frame Hamiltonian, and what—if anything—was done with
its global holomorphic Bargmann–Fock eigenproblem? Full-text claims below come
from publisher, author-hosted, or arXiv copies. Publisher records were used to
verify metadata. Abstract-only evidence is labelled. Search snippets served
only as discovery aids.

The closest verified prior work is Maslova, Anikin, Gippius, and Sokolov
(2019). Their Eq. (30) is the same Hamiltonian for a real drive. They obtain
eigenstates by Hamiltonian-matrix diagonalization and plot selected coherent-
state amplitudes in the complex amplitude plane. This directly rules out any
claim that either the Hamiltonian's quasienergies or complex-amplitude plots of
selected eigenstates are new. It does not answer the global Bargmann–Fock,
DCHE, recurrence-minimality, or Stokes questions posed here.

## Laboratory-frame origin, rotation, and quasienergy

A standard monochromatically driven Kerr-mode model is

\[
H_{\rm lab}(t)=\hbar\omega_cN+{V\over2}a^{\dagger2}a^2+
 F e^{-i\omega_dt}a^\dagger+\bar F e^{i\omega_dt}a,
\qquad N=a^\dagger a .
\]

With \(U(t)=e^{i\omega_dtN}\) and
\(|\psi_{\rm rot}\rangle=U|\psi_{\rm lab}\rangle\),

\[
H_{\rm rot}=UH_{\rm lab}U^\dagger+i\hbar\dot U U^\dagger
={V\over2}a^{\dagger2}a^2+\hbar(\omega_c-\omega_d)N
 +Fa^\dagger+\bar F a .
\]

Thus the manuscript uses \(\omega_0=\omega_c-\omega_d\). Physics papers that
write \(-\Delta_E N\) use the energy detuning
\(\Delta_E=\hbar(\omega_d-\omega_c)\), while papers that write
\(-\hbar\Delta_\omega N\) use the frequency detuning
\(\Delta_\omega=\omega_d-\omega_c\). Hence
\(\hbar\omega_0=-\Delta_E=-\hbar\Delta_\omega\). If \(F\) is complex, a
number rotation \(a\mapsto e^{-i\phi}a\) can make it real for this
single-drive model.

For a laboratory Duffing oscillator with a quartic coordinate potential, the
same Kerr form follows only after expressing the coordinate in ladder
operators, transforming to the drive frame, and discarding counter-rotating
terms. Peano and Thorwart (2006) keep the time-periodic Duffing Hamiltonian and
compute its Floquet states numerically; their rotating-wave discussion explains
why eigenvalues of the effective rotating Hamiltonian approximate Floquet
quasienergies near resonance. Quasienergies are defined modulo
\(\hbar\omega_d\), and a different rotating-frame convention can add an
integer multiple of \(\hbar\omega_d\) or an overall scalar shift. The
manuscript's \(E\) is therefore an ordinary eigenvalue of its autonomous
\(H\), and a representative of a laboratory-frame Floquet quasienergy when
the rotating-frame model is derived as above.

The Kerr cavity laboratory Hamiltonian already has only the resonant drive
harmonics displayed above, so the rotation is exact for that chosen model. For
the coordinate-space Duffing model, the Kerr reduction is an RWA and has a
finite regime of validity.

## Closed quasienergy spectrum and multiphoton resonance

### Dykman and Fistul

Dykman and Fistul, *Physical Review B* **71**, 140508(R) (2005), DOI
10.1103/PhysRevB.71.140508, start from a weakly nonlinear oscillator under a
near-resonant periodic force and obtain a rotating-frame Hamiltonian of Kerr
form. Its eigenvalues are explicitly called quasienergies. They analyze the
weak-drive degeneracy between number states, simultaneous resonant mixing of
pairs, multiphoton Rabi splittings, and antiresonant response. Their treatment
is perturbative near an \(N\)-photon resonance; it does not formulate the
global Bargmann differential equation or a non-diagonalization condition for
the full spectrum. **Access:** full arXiv text inspected; APS metadata checked.

### Maslova, Anikin, Gippius, and Sokolov

Maslova et al., *Physical Review A* **99**, 043802 (2019), DOI
10.1103/PhysRevA.99.043802, use (their Eq. (30))

\[
H_0=-\Delta a^\dagger a+{\alpha\over2}a^{\dagger2}a^2
 +f(a+a^\dagger).
\]

The map to the manuscript is
\(V=\alpha\), \(\hbar\omega_0=-\Delta\), and \(F=f\in\mathbb R\).
Their text following Eq. (30) says that the exact eigenstates are obtained by
numerical diagonalization of the Hamiltonian matrix. They analyze the
\(f=0\) quasienergies
\(\epsilon_k^{(0)}=-\Delta k+\alpha k(k-1)/2\), the degeneracies when
\(2\Delta/\alpha\) is integral, tunnelling/mixing for \(f\ne0\), squeezing,
and the later open-system kinetics in this quasienergy basis.

This paper is the closest source found because it studies the exact closed
operator before introducing damping and displays selected eigenstates in a
coherent basis (Eq. (32), Fig. 6). It does not give the Bargmann ODE, the
Taylor recurrence, a continued fraction, an entire-function growth criterion,
DCHE/Stokes data, or zero geometry. **Access:** full arXiv text inspected; APS
journal metadata checked.

The same authors' *Physical Review A* **104**, 053106 (2021), DOI
10.1103/PhysRevA.104.053106, extends the rotating-frame oscillator by weak
higher-order nonlinearities and focuses on how those terms split multiphoton
resonances in dissipative stationary occupations. It is useful context but is
not the pure Kerr Hamiltonian studied here. **Access:** full arXiv text
inspected; APS related DOI and issue metadata checked.

## Floquet Duffing and dissipative quasienergy literature

Peano and Thorwart, *Chemical Physics* **322**, 135–143 (2006), DOI
10.1016/j.chemphys.2005.06.047, study a periodically driven quartic Duffing
oscillator. They numerically solve the unitary Floquet eigenproblem and display
avoided quasienergy crossings, then derive a Floquet–Born–Markov master
equation for weak environmental coupling. Their method is numerical Floquet
matrix diagonalization plus open-system kinetics, not a Bargmann/DCHE method.
**Access:** full arXiv/author text inspected; ScienceDirect metadata checked.

Leyton, Peano, and Thorwart, *New Journal of Physics* **14**, 093024 (2012),
DOI 10.1088/1367-2630/14/9/093024, reduce the weakly nonlinear Duffing
oscillator near resonance to a Kerr-type RWA Hamiltonian. They develop
quasidegenerate perturbation theory for multiphoton doublets and compute
stationary photon-noise spectra using a Markovian Liouvillian; Appendix A
states that the Liouvillian is diagonalized numerically. This supports the
physical importance of the quasienergy doublets but does not solve the closed
global Bargmann problem. **Access:** full published author-hosted PDF and
arXiv text inspected; direct IOP page blocked by robots.txt.

These works preserve an important distinction: the isolated Floquet spectrum
or rotating-frame spectrum supplies a basis and resonance structure, whereas
the long-time state after a bath is added is a density operator determined by
a master equation. The latter is not an eigenstate of the closed Hamiltonian.

## Coherent-state, Husimi, and Bargmann representations

Let
\(|z\rangle=e^{-|z|^2/2}e^{za^\dagger}|0\rangle\) and
\(|\psi\rangle=\sum_{n\ge0}\psi_n|n\rangle\). With the manuscript's
holomorphic convention

\[
\Psi(w)=\sum_{n\ge0}{\psi_n\over\sqrt{n!}}w^n,
\]

the normalized coherent-state amplitude is

\[
\langle z|\psi\rangle=e^{-|z|^2/2}\Psi(\bar z),
\qquad
Q_\psi(z)={1\over\pi}e^{-|z|^2}|\Psi(\bar z)|^2.
\]

Consequently, a coherent-state amplitude or Husimi \(Q\) plot is not the
holomorphic Bargmann function: it includes a Gaussian factor, uses the
conjugated coordinate in this convention, and may discard phase by taking a
modulus squared.

Maslova et al. plot selected eigenstates over complex coherent amplitude and
compare their maxima with classical quasienergy contours. Their Eq. (32)
writes \(\langle n|z\rangle\), whereas the Fig. 6 caption writes
\(\langle z|n\rangle\); the inspected text does not resolve this conjugation
inconsistency. Either form is closely related to \(\Psi\), but those selected,
Gaussian-weighted coherent-amplitude plots differ from the proposed systematic
study of the holomorphic function itself, its analytic continuation, zeros,
sectorial growth, phase, and unweighted modulus geometry.

Kirchmair et al., *Nature* **495**, 205–209 (2013), DOI
10.1038/nature11902, experimentally realize a single-photon Kerr interaction
stronger than loss in a superconducting cavity and reconstruct transient
Husimi and Wigner functions during collapse and revival. This establishes the
physical relevance of a single-mode quantum Kerr nonlinearity and complex
phase-space visualization, but concerns transient evolution of prepared states,
not stationary eigenfunctions of the one-photon-driven closed Hamiltonian.
**Access:** full author-hosted/arXiv text and Nature record inspected.

## Representative driven-dissipative background

Drummond and Walls, *Journal of Physics A* **13**, 725–741 (1980), DOI
10.1088/0305-4470/13/2/034, derive an exact generalized-\(P\) steady-state
solution for optical bistability. Roberts and Clerk, *Physical Review X* **10**,
021022 (2020), DOI 10.1103/PhysRevX.10.021022, construct exact steady states
for a broader driven-dissipative Kerr family using an auxiliary pure-state
Segal–Bargmann equation. Neither is a solution of \(H\Psi=E\Psi\): both solve
open-system stationary problems with loss, and the Roberts–Clerk auxiliary
holomorphic state has complex effective parameters and a different physical
role. **Access:** Drummond–Walls partial; Roberts–Clerk full arXiv/published
copy inspected.

Siddiqi et al., *Physical Review Letters* **93**, 207002 (2004), DOI
10.1103/PhysRevLett.93.207002, experimentally demonstrate switching between
two dynamical oscillation states of an RF-driven Josephson nonlinear
resonator. It is representative experimental motivation for the driven Duffing
regime, not a measurement of the closed quasienergy eigenfunctions. **Access:**
full arXiv text inspected; APS issue metadata checked.

## Comparison of the closest sources

| Source | Hamiltonian/model | Closed/open | Method | State representation | Diagonalization | Global Bargmann–Fock relevance |
|---|---|---|---|---|---|---|
| Dykman–Fistul 2005 | near-resonant weakly nonlinear oscillator; Kerr RWA | closed quasienergies | resonant perturbation theory | number-state multiphoton pairs | finite resonant blocks | same physical spectrum locally; no global Bargmann condition |
| Peano–Thorwart 2006 | laboratory Duffing oscillator | closed Floquet, then open | numerical Floquet plus Floquet–Born–Markov | Floquet states | yes | RWA genealogy only |
| Leyton–Peano–Thorwart 2012 | Duffing reduced to Kerr RWA | quasienergy doublets plus open steady noise | quasidegenerate perturbation and master equation | quasienergy/Fock states | Liouvillian numerically | no entire-function analysis |
| Maslova et al. 2019 | exactly the one-photon Kerr Hamiltonian for real drive | closed eigenstates, then weakly open kinetics | matrix spectrum, semiclassics, rate equation | coherent amplitudes and quasienergy states | explicitly yes | closest predecessor; no ODE/recurrence/Fock-growth condition |
| Anikin et al. 2021 | Kerr plus higher nonlinearities | closed basis plus damping | semiclassics/master equation/numerics | quasienergy states | numerical spectra/master equation | nearby but different Hamiltonian |
| Drummond–Walls 1980 | coherently driven lossy Kerr mode | open | exact generalized-\(P\) | phase-space distribution | no Hamiltonian spectrum | mathematically different steady state |
| Roberts–Clerk 2020 | generalized driven-dissipative Kerr mode | open | exact coherent-absorber/Segal–Bargmann construction | auxiliary Bargmann pure state and density operator | no closed spectrum | holomorphic method, different equation and boundary problem |
| Kirchmair et al. 2013 | transient single-photon Kerr evolution | open experimental platform | tomography and simulation | Husimi/Wigner functions | not a spectral study | validates platform/plots, not eigenfunction geometry |

## What appears not to have been done

In the full texts and databases searched, no work was found that combines the
closed one-photon-driven Kerr Hamiltonian with all of the following: its global
holomorphic Bargmann–Fock eigenproblem; the degenerate \(\varepsilon_D=0\)
double-confluent-Heun structure; a spectral condition derived from Fock growth,
minimal recurrence solutions, continued fractions, connection data, or Stokes
multipliers rather than Hamiltonian-matrix diagonalization; and a systematic
study of zeros and unweighted holomorphic modulus geometry across the complex
plane. This is a bounded negative search result, not proof of absence.

No inspected physical paper derived the manuscript's Bargmann ODE or its
three-term Taylor recurrence. No inspected paper imposed Bargmann–Fock
normalizability as a spectral condition for this model. No inspected paper
analyzed zeros of these eigenfunctions. Standard recurrence and continued-
fraction methods exist in special-function theory, as documented in the Stage
02 review, but direct applicability on the degenerate DCHE surface remains to
be established.

## Cautious novelty assessment

The literature establishes the Hamiltonian, its rotating-frame quasienergy
interpretation, multiphoton mixing and antiresonance, numerical quasienergy
spectra, semiclassical phase portraits, and selected coherent-amplitude plots.
Those are prior results. Subject to the unresolved searches below, a potentially
distinctive contribution is their combination with a global holomorphic
Bargmann–Fock treatment, degenerate-DCHE/Stokes analysis, a validated
non-matrix spectral condition, and systematic zero/modulus geometry. None of
these components should be called “first” or “novel” on present evidence.

## Unresolved questions and access limitations

- Citation trails in older Russian/Soviet work on quasienergy diffusion and
  driven anharmonic oscillators were not exhaustively inspected.
- Direct IOP access was blocked, although the full Leyton et al. article was
  available from the author and arXiv.
- Drummond–Walls was not re-inspected in full during this stage.
- The Maslova Fig. 6 bra/ket convention is inconsistent between Eq. (32) and
  the caption; the plotted normalization should be confirmed from source data
  before quantitative comparison.
- The bounded keyword/citation search cannot establish priority. Subscription
  databases and forward/backward citation searches remain desirable.
- No final theorem-level map from physical boundary conditions to a minimal
  recurrence or Stokes multiplier has yet been proved for
  \(\varepsilon_D=0\).

Because the closest source (Maslova et al.) and the main Dykman/Peano/Leyton
lines were inspected in full, the core comparison is source-supported. The
negative and novelty conclusions remain explicitly provisional.
