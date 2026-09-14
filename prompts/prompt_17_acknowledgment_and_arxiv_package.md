# Prompt 17 — Add the AI acknowledgment and build the arXiv submission package

Work in the repository root.

This is a narrowly scoped pre-finalization task. Do not rewrite, reorganize, shorten, or otherwise edit the scientific manuscript except for the acknowledgment section explicitly requested below and any strictly necessary path correction required to make the arXiv package self-contained and compilable.

Do not commit or push any changes.

## 1. Preliminary inspection

Before modifying anything:

1. Read the repository instructions, including `AGENTS.md` if present.
2. Inspect `git status --short` and preserve all pre-existing unrelated changes and untracked files.
3. Confirm that the canonical manuscript source exists at:

   ```text
   manuscript/manuscript.tex
   ```

4. Inspect the manuscript's bibliography command, all `\\includegraphics` commands, and any `\\input` or `\\include` dependencies.
5. Record the complete dependency inventory needed to compile the manuscript from source.

If the canonical source is missing or its dependencies cannot be identified unambiguously, stop without modifying the repository and report the problem.

## 2. Add the acknowledgment section

In:

```text
manuscript/manuscript.tex
```

insert the following unnumbered section immediately before the bibliography. Place it after the final substantive section or appendix material and before `\\bibliographystyle` and `\\bibliography`.

Use exactly this text, preserving paragraph structure and tool names:

```latex
\\section*{Acknowledgment}

During the preparation of this work, generative AI tools were used
in two distinct capacities. First, AI-assisted code generation
(ChatGPT Work, Claude Opus, Claude Code, and Codex) was used for creation
of Python routines; all final implementation was inspected and verified
by the author. Second, large language models (ChatGPT Work, Claude Opus)
were used to assist with prose editing and language refinement at the
manuscript stage. The author reviewed and took responsibility for all
content thus produced. No AI tool is listed as an author; the author
accepts full responsibility for the scientific content of this work,
consistent with both arXiv and the Journal of Mathematical Physics
policies.
```

Do not add this section to the table of contents and do not assign it a section number.

Do not alter the wording except for line wrapping required by the source format.

## 3. Rebuild and verify the canonical manuscript

Compile:

```text
manuscript/manuscript.tex
```

from the repository root using the project's established LaTeX toolchain. If no toolchain is documented, use `latexmk` with PDFLaTeX and sufficient passes to resolve the bibliography, citations, and cross-references.

Require:

- successful exit status;
- a rebuilt `manuscript/manuscript.pdf`;
- no LaTeX errors;
- no undefined citations or references;
- no multiply defined labels;
- no missing input files or figures.

Report all significant warnings and list any overfull boxes with their locations.

Visually inspect at least the page containing the new acknowledgment and the first bibliography page. Confirm that the heading, paragraph flow, page break, and bibliography transition render cleanly.

If repository instructions require synchronization of a noncanonical compatibility PDF, perform it only as required and document it explicitly.

## 4. Construct a self-contained arXiv source tree

Use the existing repository-root directory:

```text
arxiv/
```

Prepare within it a minimal, self-contained source package capable of compiling independently of the rest of the repository.

The package must contain at least:

- the canonical TeX source as `arxiv/manuscript.tex`;
- the bibliography database as `arxiv/manuscript.bib`, if used;
- the generated bibliography as `arxiv/manuscript.bbl`, so that the submission is not dependent on BibTeX being run by arXiv;
- every figure actually referenced by the TeX source;
- every additional local file actually required by `\\input`, `\\include`, custom style loading, or another explicit dependency.

Place figures under:

```text
arxiv/figures/
```

Preserve beneath `arxiv/figures/` whatever relative subdirectory structure is required by the existing `\\includegraphics` paths. Do not flatten filenames if doing so could break references or create collisions.

Prefer changing only the arXiv copy of `manuscript.tex` when dependency paths must be made package-local. Do not make arXiv-specific path rewrites in the canonical source unless they are also correct and desirable for the canonical build.

The arXiv copy must not depend on files outside `arxiv/`. Verify this explicitly.

Do not indiscriminately copy the entire repository, the entire `figures/` tree, downloaded reference papers, audit prompts, scripts, notebooks, backups, Git metadata, caches, or intermediate build products. Include only files necessary for the submission source to compile.

Do not include `.aux`, `.log`, `.out`, `.fls`, `.fdb_latexmk`, SyncTeX files, temporary renderings, Python files, notebooks, downloaded literature PDFs, or backup files in the submission archive. Do not include the compiled manuscript PDF in the source archive unless a genuine source dependency requires it.

The existing `arxiv/README.md` may remain in the working directory for repository documentation, but exclude it from the submission ZIP unless it is genuinely required for compilation.

## 5. Test the arXiv package in isolation

Compile `arxiv/manuscript.tex` from within `arxiv/`, using only files present under that directory.

Use an isolated temporary build directory or another method that proves the source tree does not accidentally resolve dependencies from the repository root. The test must not rely on `TEXINPUTS` paths pointing outside `arxiv/`.

Require:

- successful PDF generation;
- no missing figures or source files;
- no undefined citations or references;
- no multiply defined labels;
- no LaTeX errors.

Compare the isolated arXiv-build PDF with the rebuilt canonical PDF. Exact byte identity is not required because PDF metadata may differ, but confirm that page count, extracted text, references, and figure inventory agree. Visually inspect the title page, the new acknowledgment/bibliography transition, and every page containing figures.

If the isolated build fails, do not create or retain a submission ZIP described as ready. Diagnose and correct only package-local dependency or path problems, then repeat the test.

Remove temporary compilation products from `arxiv/` before packaging, except for the source files explicitly required above. The working `arxiv/` source tree and the ZIP contents must remain clean.

## 6. Create and validate the submission ZIP

Create in `arxiv/`:

```text
arxiv/kerr_cavity_arxiv_submission.zip
```

Build the archive from the validated submission files so that `manuscript.tex`, `manuscript.bbl`, `manuscript.bib` if included, and `figures/` occur at the archive root. Do not wrap them in an additional top-level `arxiv/` directory.

Ensure that the ZIP contains only the intended submission files and does not contain the ZIP itself.

Validate the archive by:

1. testing its integrity with `unzip -t` or an equivalent command;
2. listing its complete contents;
3. extracting it into a fresh temporary directory;
4. compiling the extracted `manuscript.tex` there without access to repository-local dependencies;
5. confirming the same clean-build conditions as in Section 5.

Compute and record the ZIP's SHA-256 checksum and byte size.

## 7. Audit artifacts

Create the following files directly in the repository root:

```text
prompt_17_acknowledgment_and_arxiv_package.log
prompt_17_acknowledgment_and_arxiv_package.diff
```

The `.log` file must contain:

- the initial relevant Git status;
- the exact manuscript edit;
- the canonical compilation command and result;
- the complete arXiv dependency inventory;
- every file copied into `arxiv/`, with source and destination paths;
- every arXiv-specific path change;
- the isolated compilation command and result;
- the complete ZIP member list;
- the archive integrity-test result;
- the extracted-archive compilation result;
- page-count and comparison results;
- significant warnings, if any;
- SHA-256 checksums for the canonical PDF, isolated arXiv-build PDF, and final ZIP;
- the final relevant Git status.

The `.diff` file must contain the final repository diff for this task. Since newly created binary files and untracked files may not be represented fully by ordinary `git diff`, supplement the diff with an explicit textual inventory and checksums where necessary. Do not stage files merely to generate the diff.

## 8. Final verification

Run:

```bash
git diff --check
git status --short
```

Confirm explicitly that:

- the acknowledgment occurs exactly once and immediately before the bibliography;
- the canonical manuscript compiles cleanly;
- the `arxiv/` source tree is self-contained;
- every referenced figure is included;
- no unnecessary private, research, audit, downloaded-literature, backup, or build-intermediate file is present in the ZIP;
- the ZIP passes its integrity test;
- the freshly extracted ZIP compiles cleanly;
- no unrelated pre-existing file was modified or removed;
- no commit or push was performed.

Finish with a concise summary giving the exact paths of the rebuilt canonical PDF, the self-contained arXiv source directory, the validated ZIP archive, and the two audit artifacts. Do not commit or push.
