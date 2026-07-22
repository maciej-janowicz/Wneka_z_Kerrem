Stage 03c — Compile and retain the current repository manuscript PDF

Work only with the current files in the actual repository. Do not reconstruct
the manuscript from uploaded copies, earlier diffs, or files in /tmp.

The Stage 03b source restoration has already been completed. This stage is only
for final verification and compilation; do not edit the manuscript or
bibliography unless compilation reveals a concrete blocking error.

1. Record:

       git status --short

2. Verify directly in the current repository source that:

   - Section 3 is “Basic operator-theoretic properties”;
   - Section 4 is the Liouville/DCHE section;
   - mathematical and physical citations are both present;
   - the bibliography command uses the intended references.bib database.

3. Compile from inside the manuscript directory, using the repository’s
   established complete LaTeX–BibTeX workflow. The final persistent output must
   be:

       manuscript/manuscript.pdf

   Do not generate the deliverable only in the repository root or in /tmp.
   Do not move the final PDF to /tmp.

4. Force a complete rebuild if necessary, so that the PDF is certainly generated
   from the current manuscript/manuscript.tex and manuscript/references.bib.

5. Inspect the final log for:

   - LaTeX errors;
   - BibTeX errors or warnings;
   - undefined citations;
   - undefined references;
   - multiply defined labels.

6. Inspect manuscript/manuscript.pdf itself:

   - report its page count, file size, and modification time;
   - extract its text and confirm the section order;
   - confirm that the printed bibliography contains both mathematical and
     physical references;
   - confirm that mathematical citation callouts occur in the body;
   - render and visually inspect every page for clipping, empty pages, broken
     equations, and bibliography-layout defects.

7. Check that manuscript/manuscript.pdf is newer than both:

       manuscript/manuscript.tex
       manuscript/references.bib

8. Verify that stage03b_mathematical_restoration.diff, not the earlier Stage 03
   physical-literature diff, contains the complete Stage 03b source changes.
   Do not regenerate it merely because the compiled PDF changed unless PDFs are
   intentionally tracked by the repository.

9. Run:

       git diff --check
       git status --short

Do not stage or commit anything.

In the final report give the exact path to the retained PDF and explicitly state
that it exists at manuscript/manuscript.pdf and was compiled from the current
repository sources.
