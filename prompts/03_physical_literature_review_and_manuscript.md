Stage 03 — Physical literature review and manuscript integration
Driven single-mode Kerr oscillator in the closed rotating-frame formulation

Goal
----

Perform a careful, source-verified review of the physical literature relevant to
the closed, coherently driven, single-mode Kerr oscillator

    H = (V/2) a^{\dagger 2} a^2
        + hbar*omega_0 a^\dagger a
        + F a^\dagger
        + conjugate(F) a,

and use the verified results to enrich both:

    manuscript/references.bib
    manuscript/manuscript.tex

The central prior-art question is:

    Who has studied the quasienergy spectrum and eigenstates of the closed,
    one-photon-driven Kerr oscillator, and has anyone treated its global
    Bargmann–Fock eigenvalue problem analytically or quasi-analytically without
    Hamiltonian-matrix diagonalization?

The aim is not to claim novelty prematurely. The aim is to establish the physical
genealogy of the model, identify the closest prior work, and state precisely how
the present mathematical programme differs from earlier physical analyses.

Before editing
--------------

1. Read completely:

   - README.md
   - zarys.md, if present
   - dalsze_kierunki.md, if present
   - docs/literature_review.md
   - manuscript/manuscript.tex
   - manuscript/references.bib
   - all repository instructions, including AGENTS.md, if present

2. Inspect the present manuscript structure, notation, citation style, and existing
   bibliography support.

3. Record the initial git status.

4. Do not alter the accepted manuscript ordering:

   1. Introduction
   2. Hamiltonian and Bargmann representation
   3. Basic operator-theoretic properties
   4. Liouville transformation and special-function form
   5. Outlook

Physical scope
--------------

The primary scope is the closed, one-photon-driven Kerr oscillator in the rotating
frame. Search under all physically equivalent or closely related descriptions,
including:

- driven Kerr oscillator;
- coherently driven Kerr resonator;
- one-photon-driven Kerr oscillator;
- resonantly driven nonlinear oscillator;
- quantum Duffing oscillator under the rotating-wave approximation;
- quasienergy spectrum of a driven anharmonic oscillator;
- multiphoton resonances and antiresonances;
- dynamical tunnelling in a driven nonlinear oscillator;
- Floquet states of the driven Duffing oscillator;
- coherent-state or Husimi representations of quasienergy eigenstates;
- Bargmann representation of the driven Kerr oscillator;
- exact or quasi-exact spectrum of a driven Kerr Hamiltonian;
- continued-fraction, minimal-solution, recurrence, Heun, or complex-WKB
  treatments of the same eigenvalue problem.

Search also by the explicit rotating-frame Hamiltonian and by equivalent
coefficient conventions, for example

    H = -Delta*n + (alpha/2)*n*(n-1) + f*(a + a^\dagger),

and

    H = -Delta*a^\dagger*a
        + (alpha/2)*a^{\dagger 2}*a^2
        + f*(a + a^\dagger).

Distinctions that must be preserved
-----------------------------------

Do not conflate the following problems:

1. the closed spectral problem for the time-independent rotating-frame
   Hamiltonian;

2. the Floquet quasienergy problem for the periodically driven laboratory-frame
   Hamiltonian;

3. the stationary state of a Lindblad master equation;

4. transient unitary dynamics of an initially prescribed state;

5. semiclassical fixed points, attractors, and bistability;

6. the two-photon-driven Kerr oscillator or Kerr parametric oscillator;

7. coupled Kerr resonators, Kerr lattices, Bose–Hubbard models, or multimode
   systems.

Explain verified equivalences between items 1 and 2, including the rotating-frame
transformation and the quasienergy interpretation. State all sign and energy-shift
conventions explicitly.

Open-system literature is relevant physical background, but it must not be
presented as solving the closed Bargmann–Fock eigenvalue problem.

Two-photon-driven, multimode, and many-body models should be cited only when they
clarify the broader physical context. They must be labelled as mathematically
different models.

Priority sources
----------------

Locate and inspect the closest available primary sources, including, but not
limited to, the following research lines.

1. Maslova, Anikin, Gippius, and Sokolov:
   work containing the rotating-frame Hamiltonian

       H_0 = -Delta*a^\dagger*a
             + (alpha/2)*a^{\dagger 2}*a^2
             + f*(a + a^\dagger),

   numerical quasienergies, eigenstates, and coherent-state-plane
   visualizations.

2. Dykman and Fistul:
   multiphoton resonances, quasienergy degeneracies, Rabi splittings,
   antiresonance, and related results for a resonantly driven nonlinear
   oscillator.

3. Peano and Thorwart:
   Floquet/quasienergy analysis of the quantum Duffing oscillator in the
   drive-induced bistable regime.

4. Leyton, Peano, and Thorwart:
   multiphoton quasienergy states and related spectral/noise phenomena.

5. Foundational and representative driven-dissipative Kerr literature,
   including Drummond and Walls, but only as clearly separated background.

6. Modern exact results for driven-dissipative nonlinear resonators, including
   Roberts and Clerk, again clearly separated from the closed eigenvalue problem.

7. Experimental realizations of single-mode Kerr physics sufficient to justify
   the physical relevance of the model. Prefer experiments directly involving
   single-photon Kerr nonlinearity, driven superconducting resonators, nonlinear
   cavities, or closely corresponding platforms.

8. Earlier references found in the bibliographies of the closest papers,
   especially papers predating the modern driven-dissipative literature.

The names above are search leads, not permission to create entries from memory.
Verify exact titles, authors, journal data, year, volume, pages or article number,
DOI, and arXiv identifiers from primary or authoritative sources.

Specific analytical questions
-----------------------------

For each close source, determine as far as the inspected text permits:

- What Hamiltonian is actually studied?
- Is it the exact Kerr Hamiltonian above, or a Duffing model reduced to it by
  RWA?
- Is the system closed or open at the stage where its eigenstates are studied?
- Are the reported energies ordinary eigenvalues, rotating-frame energies, or
  Floquet quasienergies?
- What approximation regime is assumed?
- Are the results exact, perturbative, semiclassical, WKB, Floquet-numerical, or
  based on Hamiltonian-matrix diagonalization?
- How are eigenstates represented?
- Does the paper use coherent-state amplitudes, Husimi functions, Bargmann
  functions, Wigner functions, or number-state coefficients?
- Does it analyze zeros, entire-function growth, Stokes sectors, connection
  coefficients, minimal recurrence solutions, or Bargmann–Fock normalizability?
- Does it derive a spectral condition without diagonalization?
- Does it contain the same differential equation or the same three-term
  recurrence as the present manuscript, possibly in different notation?
- Does it treat the degenerate DCHE surface corresponding to epsilon_D = 0?
- Does it contain images genuinely comparable to the proposed global plots of
  |Psi(z)|?

Do not identify a coherent-state overlap or Husimi amplitude with the
holomorphic Bargmann function without writing the exact relation, including the
Gaussian factor, complex conjugation convention, and normalization.

Search specifically for prior work combining any of:

    driven Kerr + Bargmann
    driven Kerr + entire function
    driven Kerr + Heun
    driven Kerr + double confluent Heun
    driven Kerr + recurrence + continued fraction
    driven Kerr + minimal solution
    driven Kerr + complex WKB
    driven Duffing + Bargmann
    quasienergy eigenstate + coherent state representation
    Kerr eigenfunction + zeros
    Kerr oscillator + Stokes phenomenon

Search results that merely mention these words separately are not evidence.

Deliverables
------------

Create or modify the following files.

1. docs/physical_literature_review.md

   Write a structured critical review containing:

   - laboratory-frame origin of the Hamiltonian;
   - rotating-frame transformation and RWA;
   - interpretation of omega_0 as a detuning parameter, with convention caveats;
   - interpretation of E as a rotating-frame energy or quasienergy;
   - closed-system spectral literature;
   - multiphoton-resonance and Floquet literature;
   - coherent-state, Husimi, and phase-space representations of eigenstates;
   - representative driven-dissipative background;
   - relevant experimental realizations;
   - comparison table for the closest prior work;
   - a subsection entitled “What appears not to have been done”;
   - a cautious assessment of the possible novelty of the present work;
   - unresolved questions and inaccessible sources.

   The comparison table should include at least:

   - source;
   - Hamiltonian/model;
   - closed or open;
   - method;
   - representation of states;
   - use of diagonalization;
   - relevance to the global Bargmann–Fock problem.

2. manuscript/references.bib

   Add only verified bibliography entries.

   Prefer DOI-bearing journal records and authoritative publisher metadata.
   Include arXiv identifiers where useful, but avoid duplicate journal and arXiv
   entries for the same work unless there is a documented reason.

   Use stable, descriptive citation keys compatible with the existing style.

   Do not invent page ranges, issue numbers, subtitles, initials, DOIs, or
   publication years.

3. manuscript/manuscript.tex

   Enrich the manuscript conservatively.

   A. Introduction

   Add a compact physical motivation and prior-art discussion that:

   - identifies the operator as the rotating-frame Hamiltonian of a coherently
     driven single-mode Kerr oscillator;
   - mentions its connection with the near-resonantly driven Duffing oscillator
     under RWA;
   - distinguishes the closed quasienergy problem from the much more extensively
     studied driven-dissipative stationary problem;
   - cites the closest verified studies of quasienergies and eigenstates;
   - states that coherent-state or phase-space plots of selected eigenstates have
     appeared previously where verified;
   - describes the present focus more narrowly: the global holomorphic
     Bargmann–Fock eigenproblem, analytic/quasi-analytic spectral conditions, and
     the complex-plane structure of eigenfunctions.

   B. Hamiltonian and Bargmann representation

   Add only the minimum physical clarification required to explain:

   - the laboratory-frame driven Hamiltonian;
   - the unitary rotating-frame transformation;
   - the RWA, if it is actually required by the chosen laboratory model;
   - the relation between cavity frequency, drive frequency, detuning, and the
     manuscript parameter omega_0;
   - the quasienergy interpretation and its convention dependence.

   Preserve the manuscript’s existing Hamiltonian and notation. Do not silently
   redefine omega_0, V, F, or E. If the current notation makes the physical
   interpretation ambiguous, explain the mapping in prose or in a short separate
   equation.

   C. Outlook

   Add a concise, cautious statement that future work will compare the global
   Bargmann functions and their zeros/modulus geometry with earlier
   coherent-state, Husimi, semiclassical, and Floquet descriptions.

   Mention complex WKB, Voros, Olver, Fedoryuk, Borel/Laplace ideas, or
   resurgence only if they are already part of the manuscript’s declared future
   programme or can be added without presenting unproved results as established
   conclusions.

Do not rewrite the mathematical derivations in Sections 3 and 4 during this
stage. Preserve all labels, equations, cross-references, notation, and the
accepted section ordering.

4. stage03_physical_literature.log

   Record reproducibly:

   - search date and timezone Europe/Warsaw;
   - databases, publisher sites, repositories, and citation trails used;
   - exact search terms;
   - sources inspected in full;
   - sources inspected partially;
   - inaccessible sources;
   - rejected false positives;
   - works excluded because they concern two-photon drive, multimode systems,
     Lindblad stationary states only, or unrelated uses of “Kerr”;
   - duplicate preprint/journal records;
   - unresolved bibliographic metadata;
   - unresolved mathematical or novelty questions;
   - searches that produced no relevant result.

5. stage03_physical_literature.diff

   Generate a complete reviewable patch containing all Stage 03 changes.

Source discipline
-----------------

Use primary research articles and authoritative publisher records wherever
possible.

Reviews may be used to discover terminology and citation trails, but not as the
sole evidence for a precise technical claim when the original source is
available.

Do not use:

- AI-generated summaries;
- search-result snippets as evidence;
- citation aggregators when publisher or primary records are available;
- titles or abstracts alone to infer detailed mathematical content.

If only an abstract is available, restrict claims to what the abstract actually
supports and mark the source as partially inspected.

If a source is inaccessible, record it as inaccessible. Do not claim that its
equations or methods were verified.

For every manuscript sentence asserting what a previous paper did, ensure that
the cited source was inspected sufficiently to support that assertion.

Novelty discipline
------------------

Do not write that the present work is “the first”, “novel”, or “previously
unknown” unless the evidence is exceptionally strong and the wording has been
explicitly justified in the review.

Prefer formulations such as:

- “We are not aware of...”
- “The literature inspected here appears to focus primarily on...”
- “In contrast, the present work addresses...”
- “To the best of our knowledge, subject to the limitations described in
  the literature review...”

Do not claim that plotting a state in the complex coherent-amplitude plane is
new. Maslova et al. and any other close predecessors must be compared explicitly
if the full text verifies such plots.

The potentially distinctive contribution should be described, provisionally, as
the combination of:

- the closed one-photon-driven Kerr eigenproblem;
- its global holomorphic Bargmann–Fock formulation;
- the degenerate double-confluent-Heun structure;
- a spectral condition not based on Hamiltonian-matrix diagonalization;
- asymptotic and Stokes analysis;
- global zeros and modulus geometry of the entire eigenfunctions.

This is a hypothesis to test against the literature, not a conclusion to assume.

Bibliographic and manuscript validation
---------------------------------------

Before finishing:

1. Check manuscript/references.bib for duplicate keys.

2. Run a real BibTeX/Biber syntax and data-model validation using an available
   tool.

3. Verify that every new citation key used in manuscript/manuscript.tex exists in
   manuscript/references.bib.

4. Verify that every newly added bibliography entry is discussed or classified
   in docs/physical_literature_review.md.

5. Check for bibliography entries duplicated under preprint and journal forms.

6. Compile the manuscript with its existing bibliography workflow.

7. Inspect the compilation log for:

   - undefined citations;
   - undefined references;
   - BibTeX/Biber errors;
   - LaTeX errors;
   - newly introduced warnings.

8. Inspect the generated PDF, especially the pages containing the Introduction,
   Hamiltonian discussion, Outlook, and references, to ensure that the additions
   are typographically sound.

9. Run:

       git diff --check
       git status --short

10. Inspect stage03_physical_literature.diff and verify that it matches the
    working tree.

Do not change the document class, bibliography system, or manuscript structure
merely to simplify compilation.

Do not stage or commit any changes.

Final report
------------

Report concisely:

- files created or modified;
- number of verified bibliography entries added;
- number of sources inspected in full and partially;
- inaccessible sources;
- the closest prior work found;
- whether the same Hamiltonian was found;
- whether the same Bargmann differential equation or coefficient recurrence was
  found;
- whether any non-diagonalization spectral condition was found;
- whether global Bargmann zeros or modulus geometry were studied previously;
- how coherent-state plots in earlier work differ from the present proposal;
- all unresolved novelty or bibliographic questions;
- manuscript compilation result;
- bibliography validation result;
- git diff --check result;
- final git status.

Do not present Stage 03 as complete if the closest sources have not been inspected
beyond their abstracts or if essential prior-art questions remain unresolved.

Do not stage.
Do not commit.
