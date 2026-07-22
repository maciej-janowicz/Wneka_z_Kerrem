Stage 03b — Restore the accepted mathematical structure and literature

The currently generated Stage 03a manuscript PDF is not acceptable.

Two defects must be corrected:

1. Sections 3 and 4 are in the wrong order.
2. The manuscript bibliography and citations contain the newly added physical
   literature but omit the mathematical literature identified and verified in
   the earlier mathematical literature-review stage.

Work only in the actual repository on this computer. Do not reconstruct the
manuscript from an uploaded copy, an old PDF, or a partial Stage 03 patch.

Before editing
--------------

1. Read all repository instructions.
2. Read the complete current versions of:

   - manuscript/manuscript.tex
   - manuscript/references.bib
   - all mathematical and physical literature-review files under docs/
   - all relevant earlier stage logs and diffs
   - zarys.md and dalsze_kierunki.md, if present
   - the relevant prompts under prompts/

3. Inspect git history and existing stage diffs when necessary to determine
   which verified mathematical references and citations were previously found.
4. Record the initial `git status --short`.
5. Do not discard or overwrite any unrelated user changes.

Required manuscript structure
-----------------------------

Restore and preserve the following logical order:

1. Introduction
2. Hamiltonian and Bargmann representation
3. Basic operator-theoretic properties
4. Liouville transformation and special-function form
5. Outlook

If the Liouville and double-confluent-Heun material is currently divided into
subsections or separate sections, preserve the mathematically sensible internal
division, but all of that material must follow the operator-theoretic section.

Move complete section blocks, including:

- propositions, lemmas, and theorems;
- proofs;
- equations;
- labels;
- surrounding explanatory text.

After moving them, verify all numbering and cross-references. Do not rewrite the
mathematical arguments merely to perform the reordering.

Mathematical bibliography and citations
---------------------------------------

Restore and integrate the source-verified mathematical literature identified
during the earlier literature-review stages.

This must include, where previously verified and genuinely relevant, literature
supporting the manuscript’s discussion of:

- Bargmann and Bargmann–Fock spaces;
- self-adjointness, relative boundedness, compact resolvent, and discrete
  spectrum;
- double-confluent Heun equations and the precise convention used;
- irregular singularities and formal local solutions;
- complex asymptotics and Stokes phenomena;
- the later programme involving complex WKB, including the verified work of
  authors such as Voros, Olver, Fedoryuk, Sibuya, or Wasow where appropriate.

Do not add names from this instruction automatically. Recover the exact verified
sources and metadata from the earlier literature-review documents, logs, diffs,
or authoritative primary sources.

For every restored bibliography entry:

1. verify the complete metadata;
2. add it to `manuscript/references.bib` without duplicating an existing entry;
3. cite it at a specific, appropriate place in `manuscript/manuscript.tex`;
4. ensure that the cited source actually supports the associated statement.

Do not create an uncited block of mathematical bibliography.

In particular, inspect whether citations are needed:

- when defining the Bargmann–Fock representation;
- around the Kato–Rellich argument and compact-resolvent conclusion;
- when introducing the canonical DCHE convention;
- when discussing irregular singularities, formal sectorial asymptotics, and
  Stokes data;
- in the Outlook when presenting the proposed WKB/Stokes programme.

Preserve the seven verified physical references and their existing citations
unless a concrete error is found.

Validation and compilation
--------------------------

After editing:

1. check for duplicate BibTeX keys and duplicate works;
2. verify that every citation key in the manuscript exists;
3. verify that every newly restored mathematical bibliography entry is cited;
4. run `git diff --check`;
5. compile the actual repository manuscript using its established complete
   LaTeX–bibliography workflow;
6. inspect the compilation log for errors, undefined citations, undefined
   references, and bibliography warnings;
7. inspect the generated PDF visually;
8. confirm explicitly from the PDF that:

   - Section 3 is “Basic operator-theoretic properties”;
   - Section 4 contains the Liouville/DCHE analysis;
   - the bibliography contains both mathematical and physical literature;
   - mathematical citations appear in the body of the manuscript.

Create or update:

- stage03b_mathematical_restoration.log
- stage03b_mathematical_restoration.diff

The log must record the sources from which the restored mathematical references
were recovered, all edits, validation commands, compilation result, PDF
inspection result, and final `git status --short`.

The diff must contain the complete Stage 03b patch, including new files, and
must agree with the final working tree.

Do not stage or commit anything.

Final report
------------

Report:

- the final section order;
- every mathematical reference restored or added;
- the manuscript locations at which each reference is cited;
- any earlier mathematical source that was rejected or could not be verified;
- the number of physical and mathematical bibliography entries;
- compilation and PDF-inspection results;
- `git diff --check`;
- final `git status --short`.

Do not declare Stage 03b complete unless the compiled PDF itself has the correct
section order and contains both physical and mathematical citations.
