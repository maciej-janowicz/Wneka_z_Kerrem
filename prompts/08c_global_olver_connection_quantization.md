# Prompt 08c — Global Olver–Weber connection and asymptotic quantization

## Repository and working rules

Work in the existing local repository:

~~~text
~/Dokumenty/Prace_i_dnie/Wnęka_z_Kerrem
~~~

Begin by confirming the repository path and inspecting the complete current working tree, the committed 08a/08b changes, the manuscript, bibliography, documentation, symbolic verifier, tests, build procedure, and relevant earlier Stokes-geometry material.

The 08a/08b work is an accepted checkpoint, not a completed global quantization theorem. Preserve every correct result and every explicit qualification. Do not silently revert or weaken the corrections made in 08b.

Do not stage, commit, push, reset, restore, clean, initialize, clone, or change a Git remote. The user alone performs commits and pushes. Preserve unrelated user changes if the working tree is not clean.

This task is time-boxed to approximately 90 minutes. Mathematical correctness and a decisive result take precedence over the amount of prose produced. Do not spend the first hour rewriting exposition. Audit the global geometry and feasibility first.

## Purpose

Attempt to close the precise gap left by 08a/08b:

1. construct a global or sufficiently large uniform Olver–Weber comparison domain joining the relevant origin sectors through the coalescing-turning-point region;
2. identify the compensated and essential origin branches with canonical Weber branches;
3. derive the corresponding connection coefficient, including a quantified perturbation of the exact Weber connection formula;
4. prove that its zeros give the required Bargmann entireness condition, or prove the strongest asymptotic equivalence that is actually justified;
5. derive the fixed-level strong-drive quantization rule and its error from that connection problem.

The desired end product is not another definition of an unknown Stokes multiplier. It is either:

- a proved Olver connection theorem with a usable scalar quantization condition and error estimate; or
- a sharply delimited obstruction result identifying the first false hypothesis or the single missing lemma, with all new partial results proved and integrated without overclaiming.

Do not describe a conditional restatement of 08a as completion.

## Established starting point

On the positive-drive slice,

\[
\eta=\frac{|F|}{V}\to\infty,
\qquad
\delta=\frac{\hbar\omega_0}{V}\quad\hbox{fixed},
\qquad
t=\eta^{1/6}x,
\qquad
u=\eta^{2/3},
\qquad
\frac EV=\eta^{4/3}e.
\]

The exact scaled equation is

\[
\frac{d^2w}{dx^2}
=\left[u^2f(x;e)+u\,g(x)+h(x)\right]w,
\]

where

\[
f(x;e)=\frac4{x^6}+\frac{8e}{x^2}-8,
\qquad
g(x)=-\frac{8(1-\delta)}{x^4},
\qquad
h(x)=\frac{4\delta^2-4\delta+\tfrac34}{x^2}.
\]

At

\[
e_0=-\frac32,
\]

the turning polynomial in \(y=x^2\) satisfies

\[
1-3y^2-2y^3=-(y+1)^2(2y-1).
\]

Thus there are coalescences over \(y=-1\), at \(x=i\) and \(x=-i\), together with the additional simple turning points over \(y=1/2\). The latter must not be ignored in any global-domain claim.

The local Weber calculation gives, for fixed \(n\),

\[
\frac{E_n}{V}
=-\frac32\eta^{4/3}
+\left[\delta+\sqrt3\left(n+\frac12\right)-1\right]\eta^{2/3}
+O(1),
\]

but its second coefficient is currently conditional on the global connection identification.

The exact scalar spectral condition already established independently is

\[
\Delta_{\rm WI}(2\eta,2\delta,-2E/V,2\eta)=0.
\]

It must not be relabelled as a result derived by Olver’s method.

## First task: audit the entire turning-point and sheet geometry

Before constructing a comparison map, inventory all zeros and poles of the scaled coefficient for

\[
e=e_0+\frac{e_1}{u}+O(u^{-2}).
\]

Track:

- the two simple turning points that coalesce near \(x=i\);
- their sheet-related partners near \(x=-i\);
- the simple turning points perturbing \(x=\pm1/\sqrt2\);
- the pole of order six at \(x=0\);
- the images of all these objects in the \(t\)- and \(z=t^2\)-planes;
- the Stokes and anti-Stokes curves relevant to continuation of the compensated origin branch.

Determine whether the physical analyticity continuation actually uses the pair near \(x=i\), the pair near \(x=-i\), both through sheet exchange, or a different chain of canonical domains. Do not infer this from the negative classical displacement alone.

Construct or rigorously characterize the proposed cut domain. State:

- its boundary and excluded singularities;
- the chosen sheets and square-root branches;
- which turning points it contains;
- whether it is simply connected after the cuts;
- the progressive paths on which the error integral is to be controlled;
- how its endpoints approach the appropriate origin sectors;
- whether the other simple turning points obstruct the path.

A diagnostic Stokes plot or exact numerical root plot may be created if it is necessary to audit topology, but it is evidence for choosing the domain, not a substitute for proof. Do not use numerical eigenvalues.

If no single Weber domain can perform the required continuation, determine whether a finite chain of Weber, Airy, and outer canonical domains can be matched within Olver’s framework. Do not force a one-domain theorem when the topology requires a chain.

## Incorporate the order-\(u\) term into the comparison mapping

The 08a transformation mapped only \(f\) and left \(uG\) in the transformed equation. Finiteness of a variation containing an order-\(u\) remainder does not by itself give an asymptotic approximation. Repair this before making any global error claim.

Define the full scaled coefficient

\[
Q_u(x;e,\delta)
=f(x;e)+\frac1u g(x)+\frac1{u^2}h(x),
\]

so that

\[
w_{xx}=u^2Q_u(x;e,\delta)\,w.
\]

Investigate the \(u\)-dependent turning points \(\alpha_u,\beta_u\) near the selected coalescence and define an action-preserving comparison variable by

\[
Q_u(x)\left(\frac{dx}{d\zeta}\right)^2
=\zeta^2-a_u^2,
\]

equivalently

\[
\int_{\alpha_u}^{x}\sqrt{Q_u(s)}\,ds
=\int_{-a_u}^{\zeta}\sqrt{v^2-a_u^2}\,dv,
\]

with compatible branches and

\[
\frac{\pi i}{2}a_u^2
=\int_{\alpha_u}^{\beta_u}\sqrt{Q_u(s)}\,ds,
\]

subject to verification of the sign and orientation convention.

Do not assume these formulas globally before checking that the selected action is single-valued on the proposed cut domain. If incorporating all of \(h/u^2\) creates an avoidable technical obstruction, it is acceptable to map \(f+g/u\) and retain \(h\) in the remainder, but the remaining perturbation must then be genuinely lower order and explicitly bounded.

With

\[
W=\left(\frac{d\zeta}{dx}\right)^{1/2}w,
\]

derive the transformed equation directly. If the full \(Q_u\) is absorbed, it should have the form

\[
W_{\zeta\zeta}
=\left[u^2(\zeta^2-a_u^2)+\psi_u(\zeta)\right]W,
\]

where the Liouville correction is

\[
\psi_u(\zeta)
=\left(\frac{dx}{d\zeta}\right)^{1/2}
\frac{d^2}{d\zeta^2}
\left(\frac{dx}{d\zeta}\right)^{-1/2}.
\]

Verify this identity symbolically and by direct differentiation. Do not reintroduce the reversed Liouville expression corrected in 08b.

## Endpoint analysis at the irregular origin

The central new step is to determine how \(x=0\) is represented in the Weber variable.

Derive the asymptotic action as \(x\to0\) in every relevant sector. In particular, independently check the expected structure

\[
\int^x\sqrt{Q_u(s)}\,ds
=-\frac1{x^2}
-\frac{2(1-\delta)}{u}\log x
+O(1)
\]

up to branch-dependent signs, additive constants, and terms required at the claimed precision.

Compare this with

\[
\int^\zeta\sqrt{v^2-a_u^2}\,dv
=\frac{\zeta^2}{2}
-\frac{a_u^2}{2}\log\zeta
+O(\zeta^{-2})
\qquad (\zeta\to\infty),
\]

again verifying branches and constants. Determine:

- which rays \(\zeta\to\infty\) correspond to the relevant \(x\to0\) sectors;
- the leading relation between \(\zeta\) and \(x^{-1}\);
- how the essential exponentials at the origin map to the two Weber exponentials;
- how the logarithmic term, Liouville amplitude, gauge factor, and covering transformation reproduce the correct algebraic powers and monodromy;
- which canonical Weber solution corresponds, after undoing every transformation, to the compensated formal Bargmann branch;
- which coefficient multiplies the inadmissible essential branch.

Undo all transformations explicitly. It is not sufficient to compare only exponential signs in the \(w\)-equation.

Also derive the \(x\to\infty\) image of the comparison map and verify whether outer Bessel matching is actually required for the entireness argument. If it is used, keep the exact-to-Bessel comparison error separate from the intrinsic Bessel asymptotic truncation error.

## Canonical Weber solutions and exact connection coefficient

For the unperturbed comparison equation, introduce

\[
Z=\sqrt{2u}\,\zeta.
\]

Verify the precise relation between the Weber index \(p_u\) and \(a_u\). With the convention

\[
\frac{d^2W}{dZ^2}
=\left(\frac{Z^2}{4}-p_u-\frac12\right)W,
\]

the expected relation is

\[
p_u+\frac12=\frac{u a_u^2}{2},
\]

but its sign depends on the action and turning-point convention and must be checked rather than copied.

Select normalized canonical parabolic-cylinder solutions in the origin images and in the turning-point sectors. Quote and verify the exact parabolic-cylinder connection formula used. In the appropriate convention, the inadmissible coefficient should contain a factor proportional to

\[
\frac1{\Gamma(-p_u)},
\]

whose unperturbed zeros occur at

\[
p_u=n,\qquad n=0,1,2,\ldots.
\]

Do not use this factor until all phase, rotation, normalization, and sector conventions have been checked against an authoritative primary source or the NIST DLMF. Record the exact formula and source location.

## Perturbed connection problem and error control

Construct the exact Volterra integral equation comparing the canonical exact solution with the chosen Weber solution along each required progressive path.

State the modulus, weight, and envelope functions used and define the error-control variation explicitly. Prove, on the proposed domain or chain of domains:

- convergence of the integral equation;
- uniformity for fixed \(n\) and \(\delta\) in a stated compact set;
- the size of the solution error;
- the size of the induced connection-coefficient error;
- whether the estimate is absolute or relative;
- how zeros of the Weber solution are handled;
- how the bound behaves at the origin endpoint \(\zeta=\infty\).

The desired scalar structure is of the form

\[
\mathcal C(E,u)
=A(E,u)\frac1{\Gamma(-p_u(E))}
+\mathcal R(E,u),
\]

where \(A\) is nonzero on the domain of interest and \(\mathcal R\) has an explicit bound. This displayed form is a target, not an assumption. Derive it or state precisely why it cannot be derived from the available theorem.

Finiteness alone is insufficient if it does not imply a small error. Establish an actual asymptotic order, such as \(O(u^{-1})\), or the strongest order supported by the calculation. Track how the connection error depends on \(E\) near a fixed level.

Use Rouché’s theorem, the analytic implicit-function theorem, or another rigorous zero-localization argument to pass from a small connection-coefficient error to an eigenvalue statement. Agreement of formal series is not enough.

## Equivalence to Bargmann entireness

Prove the logical bridge between the Olver connection coefficient and the physical spectrum.

At minimum establish:

1. existence and uniqueness, up to normalization, of the relevant compensated canonical solution in its initial origin sector;
2. continuation through the chosen domain or domain chain;
3. equivalence between vanishing of the inadmissible connection coefficient and patching to a holomorphic germ at \(z=0\);
4. cancellation of algebraic monodromy after undoing the gauge and covering transformations;
5. entire continuation in the finite \(z\)-plane;
6. Bargmann–Fock admissibility using the already proved growth theorem;
7. normalization independence of the zero set;
8. on the physical positive-drive slice, the conjugation or symmetry argument reducing the condition to the correct number of real scalar equations.

Then compare zero sets with

\[
\Delta_{\rm WI}(2\eta,2\delta,-2E/V,2\eta).
\]

An exact identity between the two functions is not required; equality of their zeros with multiplicities on the stated domain is sufficient. Do not claim even that unless it is proved. If only asymptotic zero correspondence is obtained, say so explicitly.

Do not use the continued-fraction representation of \(\Delta_{\rm WI}\), directly or indirectly.

## Energy quantization and error

From the proved connection relation, derive the quantization rule for fixed \(n\) as \(\eta\to\infty\).

Recover

\[
\frac{E_n}{V}
=-\frac32\eta^{4/3}
+\left[\delta+\sqrt3\left(n+\frac12\right)-1\right]\eta^{2/3}
+O(1),
\]

and state exactly which part is now unconditional.

If the analysis controls the next correction, do not infer it from the quadratic Bogoliubov Hamiltonian. Include the cubic and quartic fluctuation contributions or leave the result at \(O(1)\).

Provide an explicit eigenvalue error or localization disk in terms of \(u\), rather than merely writing a formal asymptotic series. State the dependence on fixed \(n\) and on the allowed range of \(\delta\). Do not claim uniformity for growing \(n\).

As a consistency check only, compare with the corrected displaced-oscillator formula

\[
\Omega^2=(2r^2+\delta)^2-r^4,
\qquad
r^3+\delta r=\eta.
\]

Do not use operator diagonalization as the proof of the Olver result.

## Mandatory decision checkpoint

After auditing the global geometry and the origin endpoint, make an explicit decision before substantial manuscript editing:

### Outcome A — global theorem succeeds

Proceed only if all required domains, branches, endpoint limits, error variations, and zero-identification steps have been proved. Integrate the theorem, scalar connection condition, and eigenvalue error into the manuscript.

### Outcome B — asymptotic connection theorem succeeds

If exact equivalence to the full entireness determinant is not proved but a canonical Olver coefficient has been constructed with a controlled error and its zeros are rigorously localized near \(p=n\), integrate precisely that asymptotic theorem. State the remaining exact-global gap.

### Outcome C — obstruction remains

If the domain cannot be completed, the other turning points obstruct it, the origin endpoint violates the theorem’s hypotheses, or the variation cannot be made small, do not enlarge the manuscript with speculative formulas. Instead:

- prove and document every new valid local or endpoint result;
- identify the first failed hypothesis by theorem number;
- state the minimal missing lemma;
- explain whether a chain involving an Airy region can repair the problem;
- leave the manuscript’s conditional status unchanged except for useful rigorously proved clarifications.

In every outcome, the final report must say A, B, or C prominently.

## Literature discipline

Use primary and authoritative sources. For every theorem invoked, record the exact theorem, chapter, section, equation, and hypotheses.

Prioritize:

- Olver’s treatment of two coalescing turning points and error bounds;
- exact parabolic-cylinder connection formulas from Olver or the NIST DLMF;
- a primary source such as Sibuya or Wasow only if Olver does not supply the required sectorial existence theorem.

Do not cite a general chapter as if it automatically covers a pole endpoint or a complex domain with additional turning points. Verify applicability to:

- complex variables;
- a \(u\)-dependent comparison map;
- coalescing turning points;
- the pole at \(x=0\);
- unbounded comparison domains;
- the selected progressive paths.

Preserve the bibliography convention of initials only for authors and editors.

Do not use Fedoryuk in 08c. Fedoryuk is reserved for the separate subsequent analysis and must not be mixed into the proof being tested here.

## Symbolic and computational verification

Extend or complement the existing deterministic verifier. Check at least:

- all roots and multiplicities of the turning polynomial at \(e_0\);
- perturbative locations of every turning point needed in the global audit;
- the definition of \(Q_u\);
- the \(u\)-dependent comparison transformation;
- the corrected Liouville identity;
- the origin action expansion, including the logarithmic coefficient;
- the relation between \(p_u\) and \(a_u\);
- the local expansion of the action quantization condition;
- every coefficient in the retained energy formula;
- any Rouché disk or connection-error algebra used in the proof.

Use exact symbolic arithmetic whenever possible. Numerical plots may audit topology but may not serve as spectral proof. Do not diagonalize a Hamiltonian matrix.

Run the focused tests and the complete existing regression suite.

## Manuscript integration

If Outcome A or B is obtained, integrate the new result immediately after the current strong-drive subsection, avoiding duplication. Clearly distinguish:

- the exact scaled equation;
- the \(u\)-dependent comparison map;
- the exact Weber connection coefficient;
- the perturbative connection coefficient;
- the exact entireness determinant;
- exact equivalence versus asymptotic zero correspondence;
- proved versus conditional statements.

If Outcome C is obtained, make only those manuscript changes that add proved endpoint or obstruction information and improve the accuracy of existing claims.

Audit the abstract, introduction, headings, conclusion, and outlook so that none claims more than the selected outcome supports.

The publication manuscript and rendered PDF must contain no internal workflow terms, prompt identifiers, or labels such as “Stage”, “08a”, “08b”, or “08c”.

## Build and visual inspection

Rebuild the complete manuscript using the repository’s established procedure. Inspect the LaTeX and bibliography logs for errors, undefined references, bibliography failures, overfull or underfull boxes, and new warnings.

Render and visually inspect every changed page and its immediate neighbours. Correct clipped equations, excessively dense connection formulas, bad page breaks, inconsistent notation, and unreadable error bounds. Confirm that all fonts are embedded.

Search both source and extracted PDF text for forbidden internal workflow language.

## Deliverables

Create or update, following repository conventions:

1. manuscript source and rebuilt PDF;
2. verified bibliography entries, only if necessary;
3. a detailed derivation and domain-audit note, preferably 'docs/global_olver_connection.md';
4. deterministic symbolic verification code and focused tests;
5. the prompt copy 'prompts/08c_global_olver_connection_quantization.md';
6. the two review artifacts below.

## Review artifacts

Create:

~~~text
prompt_08c_global_olver_connection_quantization.diff
prompt_08c_global_olver_connection_quantization.log
~~~

The '.diff' must be a non-destructive unified diff of the complete final 08c working-tree change set against the current 'HEAD', including complete contents of every new text file. Do not stage files to generate it and do not attempt to include the '.diff' inside itself.

The '.log' must record:

- repository path and final 'git status -sb';
- Outcome A, B, or C;
- every file created, modified, or deleted;
- the complete turning-point and sheet inventory;
- the chosen domain or domain chain;
- all cuts, branches, and progressive paths;
- the exact \(Q_u\) comparison map;
- the origin and infinity endpoint mappings;
- the selected Weber solutions and exact connection formula;
- the comparison index \(p_u\);
- the error-control function, its variation, and the proved asymptotic order;
- the exact or asymptotic relation to Bargmann entireness;
- the zero-localization argument;
- every energy coefficient and eigenvalue-error statement;
- every theorem and source location used;
- symbolic commands and exact outputs;
- focused and complete test results;
- build commands, warnings, and results;
- rendered pages inspected;
- searches for internal workflow language;
- every remaining limitation and the minimal missing lemma;
- confirmation that no continued fraction, matrix diagonalization, Fedoryuk analysis, or prohibited Git operation was used.

Verify that both artifacts exist, are nonempty, and describe the final rather than an intermediate state.

## Strict exclusions

Do not:

- leave \(uG\) untreated while calling the resulting Weber approximation asymptotic;
- assume that a finite error-control variation is small without proving its order;
- ignore the simple turning points near \(x=\pm1/\sqrt2\);
- infer the physical contour solely from the displaced classical minimum;
- quote \(1/\Gamma(-p)\) without checking rotations, phases, and normalization;
- define a Stokes multiplier and call that an evaluation;
- identify the exact entireness determinant with an Olver coefficient without proof;
- infer eigenvalue zeros from formal agreement alone;
- claim a scalar condition before proving the symmetry or monodromy reduction;
- use continued fractions in any form;
- use direct or truncated Hamiltonian-matrix diagonalization;
- use numerical eigenvalues as evidence;
- use Padé or Hermite–Padé approximants;
- use Fedoryuk’s method in this task;
- compute an \(O(1)\) energy coefficient from the quadratic Hamiltonian alone;
- claim uniformity for \(n\) growing with \(u\);
- leave internal workflow language in the publication manuscript;
- stage, commit, push, reset, restore, clean, or otherwise alter Git history or the index.

## Final interactive response

Lead with Outcome A, B, or C and one sentence explaining why.

Then report:

- the actual theorem or obstruction obtained;
- the domain and endpoint mapping;
- the connection coefficient and its error;
- the precise relation to Bargmann entireness;
- the quantization rule and eigenvalue error;
- what is proved, conditional, defined only, or open;
- all files changed or created;
- paths to the '.diff' and '.log';
- focused and complete test results;
- build and visual-inspection results;
- compliance with all exclusions.

Do not conclude with “the programme is complete” unless Outcome A has actually been proved.
