Stage 03d — Additive recovery of the physical literature review

Objective

Recover the physically oriented part of the literature review that is missingfrom the current compiled manuscript, while preserving the complete currentmathematical manuscript and all other existing content.

Work only in the actual repository on this computer. Do not reconstruct themanuscript from uploaded copies, temporary files, an old PDF, or a partial patch.

Absolute add-only protection of the manuscript

The following rule has priority over every other instruction in this prompt:

Absolutely nothing may be removed from the existingmanuscript/manuscript.tex. You may only add new material to it.

Treat the current committed version of manuscript/manuscript.tex as animmutable baseline. In that file:

do not delete any character, word, citation, equation, paragraph, comment,command, label, environment, section, or bibliography instruction;

do not replace, rewrite, shorten, rephrase, correct, reorder, or move anyexisting text;

do not change existing whitespace or line wrapping;

do not rename any symbol, label, citation key, section, or file;

do not modify an existing sentence merely to insert a citation into it;

do not resolve a conflict by choosing one version and discarding another;

do not use a formatter or any command that mechanically rewrites the file.

The only permitted changes to manuscript/manuscript.tex are insertions of newlines at carefully selected locations. If an existing statement needsqualification, add a new sentence or paragraph after it. If an existingstatement needs a citation, add a new supporting sentence containing thatcitation rather than editing the existing sentence.

Before editing, make an exact temporary baseline copy or record the blob/hash ofthe current file. After editing, verify mechanically that the complete baselineis a subsequence of the final file, byte for byte and in the same order. Alsoinspect the file-specific diff:

git diff -- manuscript/manuscript.tex

Every changed line in that diff must be an added line. If the diff contains evenone line beginning with - other than the standard diff header ---, stop andundo only your Stage 03d manuscript edits, then reapply them additively. Do notfinish the stage while any deletion from manuscript/manuscript.tex remains.

This add-only rule applies even if you find an obvious typographical,bibliographic, structural, mathematical, or physical error. Record such anerror in the log for a later stage; do not correct it now if correction wouldalter or remove existing manuscript content.

Before editing

Read all repository instructions, including AGENTS.md.

Record the initial:

git status --short
git log --oneline --decorate -n 15

Read the complete current versions of:

manuscript/manuscript.tex;

manuscript/references.bib;

all relevant files under docs/;

the Stage 03, 03a, 03b, and 03c prompts, logs, and diffs;

zarys.md and dalsze_kierunki.md, if present.

Inspect git history, earlier commits, and earlier Stage 03 patches to identifyprecisely which verified physical-literature paragraphs and citations werepresent before they disappeared.

Determine why they are absent from the current manuscript. Record the causeif it can be established from repository evidence.

Create stage03d_physics_recovery.log immediately and maintain it throughoutthe work. Record the baseline manuscript hash and the exact recovery sources.

Do not discard, overwrite, stage, or commit any existing user changes.

Recovery scope

Recover, by additive insertion, the previously verified physical discussionrelevant to the closed, coherently one-photon-driven Kerr oscillator. Therestored material should cover, to the extent supported by the earlier verifiedreview:

the physical origin and standard use of the model;

the laboratory-frame Hamiltonian, transformation to the rotating frame, androtating-wave approximation, but only where these were previously verified;

the relation between cavity frequency, drive frequency, detuning, and thecurrent manuscript parameter;

the quasienergy interpretation and its convention dependence;

the closest verified prior work, especially Maslova et al. if the full sourcesupports the comparison;

prior numerical diagonalization, coherent-state or phase-spacerepresentations, semiclassical or Floquet treatments, where verified;

the distinction between those earlier results and the present programme:the global holomorphic Bargmann–Fock eigenproblem, analytic or quasi-analyticspectral conditions without Hamiltonian-matrix diagonalization, asymptoticand Stokes analysis, and the global zeros and modulus geometry of the entireeigenfunctions;

a concise and cautious outlook connecting the future global Bargmannanalysis with earlier coherent-state, Husimi, semiclassical, and Floquetdescriptions.

Recover only statements supported by sources that were actually inspectedsufficiently in the earlier review. Do not turn an earlier tentative conclusioninto a stronger claim.

Do not claim that plotting a state on the complex coherent-amplitude plane isnew. Do not make a priority claim. Prefer cautious formulations such as:

“The literature inspected here appears to focus primarily on...”

“In contrast, the present work addresses...”

“We are not aware of...”

“No priority claim for this programme is made here.”

Notation and physical conventions

Preserve all notation already present in the current manuscript. Do not silentlyredefine omega_0, V, F, E, or any other symbol.

For the present stage:

retain the current manuscript notation omega_0;

retain the identity

[\omega_0=\omega_c-\omega_d;]

if both energy and frequency detuning conventions must be discussed,distinguish them explicitly:

[-\Delta_E N,\qquad \Delta_E=\hbar(\omega_d-\omega_c),]

and

[-\hbar\Delta_\omega N,\qquad\Delta_\omega=\omega_d-\omega_c;]

do not yet rename omega_0 to Delta;

note only in the log, if useful, that a later separate stage may adopt(\Delta=\omega_c-\omega_d) while retaining the plus sign in(+\hbar\Delta N).

In Polish work notes use “wzbudzany” or “sterowany”, not “napędzany”, and“wirujący układ odniesienia”, not “rama”. The English manuscript may use“driven” and “rotating frame”.

Bibliography

Preserve every existing entry in manuscript/references.bib. Do not delete,replace, or rename existing bibliography entries in this stage.

Restore any missing, previously verified physical references additively. Beforeadding an entry:

recover its verified metadata from the earlier review, log, diff, or anauthoritative primary/publisher record;

confirm that the same work is not already present under another key;

use the previously established citation key where possible;

cite it in a newly added sentence or paragraph in the manuscript;

ensure that the citation supports the associated claim.

Preserve all mathematical references and citations already present. The finalbibliography and manuscript must contain both the mathematical and physicalliterature.

Do not add uncited bibliography entries. Do not infer detailed content fromtitles, abstracts, search snippets, AI summaries, or citation aggregators.

If an earlier physical source cannot now be verified, record it as unresolvedand do not add a stronger manuscript claim.

Placement and structure

Insert the recovered physical material at logically appropriate points, mostlikely in the Introduction, the Hamiltonian/Bargmann discussion, and theOutlook. Do not create redundant duplicate paragraphs if equivalent physicalmaterial is already present.

Preserve the current accepted section order exactly. In particular, preserve:

Introduction;

Hamiltonian and Bargmann representation;

Basic operator-theoretic properties;

Liouville transformation and special-function form;

Outlook;

or the exact expanded version of this accepted order currently present in therepository.

Do not move existing section blocks. Do not rewrite mathematical derivations,proofs, equations, propositions, lemmas, theorems, labels, or cross-references.All Stage 03d manuscript work must consist solely of additive insertions.

Validation

After editing:

mechanically verify the add-only preservation of the complete baselinemanuscript/manuscript.tex;

inspect:

git diff -- manuscript/manuscript.tex

and confirm explicitly that it contains no deleted manuscript-content lines;

check that the accepted section order remains unchanged;

check manuscript/references.bib for duplicate keys and duplicate works;

verify that every citation key used in the manuscript exists;

verify that every newly added bibliography entry is cited;

verify that all pre-existing mathematical citations and bibliography entriesremain present;

run real BibTeX/Biber syntax and data-model validation using the repository'sestablished tools;

run:

git diff --check

Compilation and PDF inspection

Codeks must perform the compilation in this stage. Compile only the actualrepository source, using the repository's established completeLaTeX–bibliography workflow.

The final persistent output must be:

manuscript/manuscript.pdf

Force a complete rebuild if necessary. Do not use an uploaded manuscript, anold reconstructed source, a repository-root copy, or a file in /tmp as thedeliverable. Do not move the final PDF to /tmp.

Inspect the compilation log for:

LaTeX errors;

BibTeX/Biber errors or warnings;

undefined citations;

undefined references;

multiply defined labels;

newly introduced warnings.

Inspect manuscript/manuscript.pdf itself:

report its page count, size, and modification time;

verify that it is newer than manuscript/manuscript.tex andmanuscript/references.bib;

extract its text and confirm the accepted section order;

confirm that the recovered physical discussion is visibly present;

confirm that physical citation callouts occur in the manuscript body;

confirm that the printed bibliography contains both physical andmathematical literature;

render and visually inspect every page for clipping, blank pages, brokenequations, displaced headings, and bibliography-layout defects.

Do not declare Stage 03d complete merely because LaTeX returned exit statuszero. The generated PDF itself must pass these checks.

Reproducibility files

Create and maintain:

stage03d_physics_recovery.log;

stage03d_physics_recovery.diff.

The log must contain:

initial and final git status;

current date and timezone;

baseline manuscript hash;

exact commits, diffs, logs, and review files used for recovery;

the identified cause of the disappearance, if established;

every restored physical source and manuscript insertion;

unresolved sources or claims;

add-only preservation checks and their exact results;

bibliography validation commands and results;

compilation commands and results;

PDF metadata and visual-inspection result;

git diff --check result.

Generate the complete reviewable Stage 03d diff only after substantive editing,validation, compilation, and PDF inspection are complete. Ensure that itcontains all Stage 03d source and documentation changes, including newuntracked text files, without using git add.

The generated diff must agree with the final working tree. If the repositorynormally tracks manuscript/manuscript.pdf, include its changed status in thereport; do not attempt to encode the binary PDF manually into a textual patch.

Final checks and report

Run:

git diff --check
git status --short

Do not stage or commit anything.

Report concisely:

the cause of the missing physical material, if established;

every physical paragraph or topic restored and its insertion location;

every physical reference restored or added;

all unresolved physical or bibliographic questions;

confirmation that all pre-existing manuscript content was preserved byte forbyte and in order;

confirmation that the manuscript-specific diff contains additions only;

final section order;

counts of physical and mathematical bibliography entries;

bibliography and citation validation results;

compilation result;

the exact retained PDF path, metadata, and visual-inspection result;

git diff --check result;

final git status --short.

Do not report Stage 03d as complete if:

any pre-existing content of manuscript/manuscript.tex was deleted, changed,moved, or reordered;

the physical discussion is still absent from the compiled PDF;

mathematical literature or citations disappeared;

the bibliography does not contain both mathematical and physical sources;

essential citations or references remain undefined;

the retained manuscript/manuscript.pdf was not compiled from the currentrepository sources.
