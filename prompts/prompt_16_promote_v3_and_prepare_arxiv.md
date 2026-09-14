# Prompt 16 — Promote the corrected v3 manuscript and prepare the arXiv workspace

Work in the repository root.

This is a narrowly scoped pre-finalization task. Do not rewrite, reorganize, shorten, or otherwise edit the scientific manuscript except for the single abstract clarification explicitly requested below and any strictly necessary path correction required for clean compilation.

Do not commit or push any changes.

## 1. Inspect the corrected v3 source files

The source directory is:

```text
manuscripts/
```

Note carefully that this directory name ends with `s`.

The exact source basename is:

```text
manuscript_scalony_1-10_12_09_2026_v3
```

Before copying, list:

- all regular files in `manuscripts/` having this exact basename and any extension;
- the existing files in the destination directory `manuscript/` that will be replaced.

If no files with the exact source basename exist, stop without modifying the repository and explain the problem.

## 2. Promote the v3 files to the canonical manuscript directory

Copy every regular file matching:

```text
manuscripts/manuscript_scalony_1-10_12_09_2026_v3.*
```

to:

```text
manuscript/
```

Rename the copied files to the canonical basename `manuscript`, while preserving each extension. Thus, for example:

```text
manuscripts/manuscript_scalony_1-10_12_09_2026_v3.tex
```

must replace:

```text
manuscript/manuscript.tex
```

and analogous `.bib`, `.pdf`, or other same-basename files must become `manuscript/manuscript.<extension>`.

Replacement of the old canonical files is intentional. Do not delete unrelated files from either directory.

After copying, verify byte-for-byte identity between every source file and its corresponding destination file before making the abstract edit.

## 3. Clarify the abstract

In:

```text
manuscript/manuscript.tex
```

modify the abstract so that the continued-fraction spectral characterization and the simplicity statement are explicitly restricted to non-zero drive.

The resulting sentence should read naturally and include the exact phrase:

```text
for non-zero drive
```

A preferred minimal formulation is:

```latex
For non-zero drive, a minimal-solution continued fraction gives an exact
scalar spectral condition $\Xi(E)=0$, with every eigenvalue simple.
```

Do not make any other scientific or stylistic change to the manuscript.

## 4. Check compilation

Compile the new canonical source:

```text
manuscript/manuscript.tex
```

from the repository root, using the project's established LaTeX toolchain if one is documented. Otherwise use `latexmk` with PDFLaTeX and sufficient passes to resolve the bibliography and cross-references.

If the canonical source contains a bibliography or another dependency still pointing unnecessarily to the versioned file in `manuscripts/`, update only that dependency path to the corresponding canonical file in `manuscript/`, provided the copied canonical dependency exists. Record this separately as a strictly necessary build-path correction.

A clean compilation means:

- successful exit status;
- generated `manuscript/manuscript.pdf`;
- no LaTeX errors;
- no undefined citations;
- no undefined references;
- no multiply defined labels;
- no missing figures or input files.

Report significant remaining warnings. Do not silently describe the compilation as clean if any of the conditions above fails.

Do not treat ordinary, harmless typography warnings as fatal, but list any overfull boxes with their locations.

## 5. Create the arXiv staging directory

Create the following directory in the repository root:

```text
arxiv/
```

This will later contain the self-contained preprint source and figures intended for submission to arXiv.

At this stage, do not package or copy the preprint into it. Do not create an arXiv tarball. If an empty directory would not be represented in Git, add:

```text
arxiv/README.md
```

containing only a short statement that this directory is reserved for the future self-contained arXiv submission package. Do not add speculative submission instructions.

## 6. Verification and audit artifacts

Verify at the end:

```bash
git status --short
git diff --check
```

Also confirm:

- which exact source files were found;
- which files were copied and renamed;
- that the old canonical files were replaced;
- that `manuscript/manuscript.tex` contains `for non-zero drive` in the abstract;
- that `manuscript/manuscript.pdf` was rebuilt successfully;
- that `arxiv/` exists;
- that no unrelated file was modified;
- that no commit or push was performed.

Create the following two audit artifacts directly in the repository root:

```text
prompt_16_promote_v3_and_prepare_arxiv.log
prompt_16_promote_v3_and_prepare_arxiv.diff
```

The `.log` file must contain:

- the exact commands or operations performed;
- the copied-file inventory;
- the compilation command;
- the compilation result and relevant warnings;
- the final verification results.

The `.diff` file must contain the final repository diff for this task. Because overwritten binary PDFs may not have a textual diff, explicitly list their paths and checksums in the log.

Finish with a concise summary of changes, compilation status, warnings, and the exact output paths. Do not commit or push.
