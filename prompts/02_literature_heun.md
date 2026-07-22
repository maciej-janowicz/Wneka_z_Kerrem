Stage 02 — Verified literature review and BibTeX bibliography

The repository is currently clean after completion of Stage 01 and the removal
of the obsolete Stage 00 review artifacts.

Do not modify the mathematical analysis in the manuscript during this stage.
Do not introduce new mathematical claims, spectral conditions, or changes of
notation.

Our model is the closed, coherently driven single-mode Kerr Hamiltonian

H = (V/2) a^{\dagger 2} a^2
    + hbar*omega_0 a^\dagger a
    + F a^\dagger + conjugate(F) a,

with Bargmann equation

(V/2) z^2 Psi''
+ (hbar*omega_0 z + conjugate(F)) Psi'
+ (F z - E) Psi = 0.

The canonical DCHE convention already adopted in the manuscript is

z^2 u''
+ (gamma_D + delta_D z + epsilon_D z^2) u'
+ (alpha_D z - q_D) u = 0,

with

gamma_D   = 2 conjugate(F)/V,
delta_D   = 2 hbar*omega_0/V,
epsilon_D = 0,
alpha_D   = 2F/V,
q_D       = mathcal{E} = 2E/V.

Preserve this convention exactly. In particular:

- retain the factor V/2 in the Hamiltonian and Bargmann equation;
- retain mathcal{E} = 2E/V;
- do not confuse the DCHE parameter epsilon_D with the energy;
- do not replace our convention with another DCHE normalization without giving
  an explicit transformation and parameter map.

Perform a careful, source-based literature review covering:

1. The general double-confluent Heun equation and the general asymptotic theory
   of linear ordinary differential equations with irregular singular points,
   including the treatments in:

   - Frank W. J. Olver, Asymptotics and Special Functions;
   - M. V. Fedoryuk, Asymptotic Analysis: Linear Ordinary Differential
     Equations.

2. Formal solutions at irregular singularities, including:

   - formal exponential factors;
   - characteristic powers;
   - Poincare rank and related rank conventions;
   - ramified irregular singularities;
   - sectorial asymptotic solutions;
   - Stokes and anti-Stokes curves;
   - Stokes multipliers and connection problems;
   - the distinction between formal, asymptotic, analytic, and convergent
     solutions.

3. Floquet or multiplicative solutions, characteristic exponents, and
   connection coefficients for the DCHE.

4. The degenerate epsilon_D = 0 parameter hypersurface and any genuinely
   applicable Whittaker–Ince-type limits or related degenerations.

5. Series solutions, three-term recurrences, continued fractions, minimal
   solutions, characteristic equations, and spectral conditions.

6. The Segal–Bargmann/Fock representation, including:

   - entire-function growth;
   - order and type where relevant;
   - the Bargmann–Fock normalizability condition;
   - the relation between local analyticity, global entire continuation, and
     membership in Bargmann–Fock space.

7. The closed coherently driven Kerr oscillator and previous treatments of its
   stationary spectrum, eigenfunctions, Bargmann representation, or coefficient
   recurrence.

8. Closely related driven-dissipative Kerr models, clearly marked as physically
   related but mathematically different from our closed stationary
   Schroedinger eigenvalue problem.

Pay particular attention to the following sources and source families:

- W. Bühring, “The double confluent Heun equation: Characteristic exponent
  and connection formulae,” Methods and Applications of Analysis 1 (1994),
  348–370;
- NIST Digital Library of Mathematical Functions, Chapter 31, especially
  Section 31.12;
- S. Yu. Slavyanov and W. Lay, Special Functions: A Unified Theory Based on
  Singularities;
- the volume on Heun equations edited by A. Ronveaux;
- Frank W. J. Olver, Asymptotics and Special Functions;
- M. V. Fedoryuk, Asymptotic Analysis: Linear Ordinary Differential
  Equations;
- work by Schmidt and Wolf;
- work by E. W. Leaver;
- work by L. J. El-Jaick and B. D. B. Figueiredo.

For Olver and Fedoryuk, identify the precise chapters, sections, and theorem
numbers relevant to:

- formal asymptotic solutions;
- irregular singular points and their rank;
- ramified asymptotic behaviour;
- sectorial validity;
- Stokes phenomena;
- connection of formal solutions with actual analytic solutions.

Do not cite Olver or Fedoryuk merely as generic background. State precisely
which result is being used and whether its hypotheses apply to our equation.

Important mathematical caution
------------------------------

Do not assume that results for a generic DCHE apply unchanged to our
epsilon_D = 0 degeneration.

Stage 01 classified:

- z = 0, for F != 0, as an unramified rank-1 irregular singularity;
- z = infinity as a ramified rank-1/2 irregular singularity;
- F = 0 as a separate regular-singular degeneration at z = 0.

For every potentially applicable result:

1. reproduce or identify the source equation;
2. record the source’s parameter convention;
3. derive the parameter transformation to our convention;
4. check all assumptions explicitly;
5. state whether the result applies:
   - directly;
   - after an explicit transformation;
   - only after adaptation;
   - only by analogy;
   - or not at all.

Do not identify epsilon_D = 0 automatically with a Whittaker–Ince limit.
Use that terminology only if the precise limiting procedure and resulting
equation agree with a verified source.

Prior-art search
----------------

Search specifically for previous papers or books that derive any of the
following for the closed coherently driven Kerr Hamiltonian:

- the same Bargmann differential equation;
- the same DCHE reduction;
- the same Taylor-coefficient recurrence;
- a continued-fraction or minimal-solution condition;
- an exact or quasi-exact spectral condition;
- entire Bargmann eigenfunctions;
- Bargmann–Fock normalizability conditions;
- zeros, nodal geometry, or complex-plane modulus plots of the eigenfunctions.

The Taylor recurrence to search for, in our convention, is

conjugate(F) (n+1) c_{n+1}
+ [(V/2)n(n-1) + hbar*omega_0 n - E] c_n
+ F c_{n-1}
= 0,

with c_{-1} = 0.

Allow for equivalent recurrences written with rescaled parameters, shifted
indices, different signs, or different normalizations of the Kerr term.

Search both the special-functions literature and the physics literature.
Distinguish carefully between:

- a closed Hamiltonian eigenvalue problem;
- quasienergies in a rotating frame;
- resonances;
- non-Hermitian effective Hamiltonians;
- Lindblad steady states;
- complex-P or generalized-P solutions;
- semiclassical stationary states.

Do not treat results for the latter cases as solutions of our closed spectral
problem.

Report negative search results cautiously. Use formulations such as:

“not found in the sources and databases searched”

and never:

“does not exist” or “has never been studied.”

Required outputs
----------------

Create:

1. docs/literature_review.md

For every relevant source include:

- full bibliographic identification;
- source type;
- DOI, stable publisher link, arXiv link, or other authoritative access link;
- access status: inspected in full, inspected partially, abstract only, or
  inaccessible;
- the equation and parameter convention used;
- the precise result relevant to our problem;
- page, section, equation, proposition, or theorem numbers whenever available;
- whether the result applies directly, after transformation, after adaptation,
  only by analogy, or not at all;
- any conflict, ambiguity, or uncertainty requiring manual checking.

Organize the review by subject rather than merely as an annotated alphabetical
bibliography.

Include a comparison table with at least the following columns:

- Source;
- Equation/class;
- Local behaviour at zero;
- Behaviour at infinity;
- Recurrence/continued fraction;
- Connection or Stokes data;
- Relation to epsilon_D = 0;
- Relevance to the Kerr–Bargmann problem;
- Applicability status.

End docs/literature_review.md with the following explicitly labelled sections:

- Established prior results
- Results requiring adaptation to epsilon_D = 0
- Apparently open questions relevant to this project
- Claims we must not present as novel
- Candidate contributions of the present work
- Unresolved questions requiring manual source inspection

The “Claims we must not present as novel” section must include, if confirmed by
the literature:

- the standard local formal theory at an irregular singular point;
- the existence and derivation of the Taylor recurrence;
- standard DCHE multiplicative or Floquet solutions;
- known connection-formula and continued-fraction methods.

The “Candidate contributions” section must be cautious and evidence-based.
In particular, investigate whether the following may remain genuinely useful:

- selecting the relevant entire solution through the Bargmann condition;
- translating Bargmann–Fock normalizability into a connection, Stokes, minimal-
  solution, or growth condition;
- a quasi-numerical algebraic or continued-fraction condition for the energy
  without direct Hamiltonian diagonalization;
- global geometry of zeros and modulus level sets throughout the complex plane;
- dependence of that geometry on the physical parameters.

Do not declare any of these novel merely because they were not found quickly.

2. manuscript/references.bib

Include only references whose metadata have been verified against at least one
authoritative source, such as:

- the original paper or its title page;
- the publisher’s page;
- a DOI record;
- an official arXiv record;
- DLMF;
- the title and copyright pages of a book.

BibTeX requirements:

- preserve diacritics correctly, especially B{\"u}hring;
- protect capitalization in titles, including {Heun}, {Bargmann}, {Kerr},
  {Fock}, {DCHE}, and other proper names or acronyms;
- include DOI whenever verified;
- include a stable URL and urldate for online reference works;
- include ISBN for books only when verified;
- do not invent missing fields;
- do not copy unverified metadata from search-result snippets;
- do not use search-result aggregators when a primary or publisher source is
  available;
- use stable, descriptive citation keys;
- avoid duplicate journal and arXiv entries unless there is a documented reason;
- keep mathematically related and driven-dissipative references in the same
  bibliography, but classify them clearly in the review.

Both Olver and Fedoryuk must be included in manuscript/references.bib, but only
after the exact edition, publisher, year, and other supplied metadata have been
verified. If more than one edition or translation exists, record the ambiguity
in the log and select only the edition actually inspected.

3. stage02_literature.log

The log must record:

- databases, catalogues, websites, and search routes used;
- exact search terms;
- sources inspected in full;
- sources inspected only partially;
- inaccessible sources;
- rejected false positives;
- duplicate records;
- alternative editions and translations;
- unresolved bibliographic uncertainties;
- claims for which only secondary evidence was found;
- searches producing no relevant result.

The log must make it possible to reproduce the literature search.

4. stage02_literature.diff

Generate a reviewable patch containing all Stage 02 changes.

Source discipline
-----------------

Prefer primary and authoritative sources.

For each important mathematical claim, trace the claim to the original source
where practical. A modern reference such as DLMF may be used to identify the
standard terminology and earlier literature, but it should not automatically
replace the original source for a specific theorem or connection formula.

Do not rely on an AI-generated summary, search-engine snippet, or citation
aggregator as evidence.

Do not infer theorem contents from titles or abstracts alone.

If a source is inaccessible, record it as inaccessible and do not claim to have
verified its detailed contents.

If optical character recognition is used for an older scan, manually check all
equations, names, page numbers, and bibliographic metadata quoted from it.

Do not silently merge incompatible uses of:

- rank;
- characteristic exponent;
- Floquet exponent;
- Thomé solution;
- normal solution;
- connection coefficient;
- minimal solution;
- Whittaker–Ince limit.

Record each source’s terminology and explain equivalences only when verified.

Repository and manuscript constraints
-------------------------------------

Do not rewrite the manuscript’s mathematical sections during this stage.

Do not add citations to mathematical claims in manuscript/manuscript.tex yet,
unless a citation command is already present and only requires a missing
BibTeX entry. Otherwise leave manuscript citation placement for a later,
separately reviewed stage.

Do not restructure the manuscript merely to force bibliography compilation.

Do not change the accepted ordering:

1. Introduction
2. Hamiltonian and Bargmann representation
3. Basic operator-theoretic properties
4. Liouville transformation and special-function form
5. Outlook

Preserve all existing labels, notation, equations, and cross-references.

Validation
----------

Before finishing:

- check manuscript/references.bib for duplicate citation keys;
- perform a basic BibTeX syntax check;
- verify that every entry cited in docs/literature_review.md exists in
  manuscript/references.bib, unless explicitly marked as bibliographically
  unresolved;
- verify that every BibTeX entry is discussed or classified in the review;
- compile the manuscript with the bibliography only if bibliography support is
  already configured;
- otherwise do not alter the manuscript merely to force bibliography support;
- run git diff --check;
- report git status;
- inspect the generated stage02_literature.diff;
- do not stage any changes;
- do not commit;
- leave all changes unstaged for manual review.

Final report
------------

At the end, report concisely:

- files created or modified;
- number of verified bibliography entries;
- number of sources inspected in full and partially;
- inaccessible sources;
- unresolved metadata or mathematical questions;
- whether prior work containing the same Kerr–Bargmann equation or recurrence
  was found;
- whether any result was found that applies directly to epsilon_D = 0;
- validation results;
- final git status.

Do not present Stage 02 as complete if essential claims rely only on inaccessible
or unverified sources. In that case, clearly identify the remaining manual
checks.

Do not commit.
