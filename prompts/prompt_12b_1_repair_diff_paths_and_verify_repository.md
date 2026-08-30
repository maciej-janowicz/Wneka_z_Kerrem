# Prompt 12b_1 — repair audit-diff paths and verify the real repository state

Work in the repository root of `Wneka_z_Kerrem`. This is a strictly technical
audit-repair microstage following Prompt 12b. Do not regenerate or recolour the
figures, do not change `manuscript/manuscript.tex`, do not alter the mathematics
or prose, and do not rebuild the PDF unless a read-only verification reveals
that the canonical PDF is missing or inconsistent.

The 12b manuscript and figures have already been reviewed and accepted. The
only known defect is that the attached 12b `.diff` records all newly created
files except `manuscript/manuscript.tex` under erroneous paths beginning with

`tmp/12b_diff_new/`

instead of their actual repository-relative paths such as `figures/`,
`scripts/`, and `tests/`. Determine whether this defect exists only in the
generated audit artifact or also in the actual worktree, then repair the audit
trail without disturbing the accepted 12b result.

## 1. Establish the exact worktree state

Before changing anything, run and record:

```bash
pwd
git rev-parse --show-toplevel
git branch --show-current
git status --short
git status -sb
git ls-files --others --exclude-standard
```

Verify the existence and file type of every intended 12b path:

- `manuscript/manuscript.tex`
- `manuscript/manuscript.pdf`
- `scripts/12b_final_iterated_wkb_figures.py`
- `tests/test_12b_final_iterated_wkb_figures.py`
- `figures/12b_final_iterated_wkb/final_eta4p0_k2_branchR_domainturning_bright-phase-modulus.png`
- `figures/12b_final_iterated_wkb/final_eta4p0_k2_branchI_domainlocal_bright-banded-modulus.png`
- `figures/12b_final_iterated_wkb/final_eta0p25_k3_branchR_domainturning_bright-equalized.png`
- `figures/12b_final_iterated_wkb/final_eta0p25_k3_branchI_domainleft_bright-phase-modulus.png`
- `figures/12b_final_iterated_wkb/final_iterated_wkb_metadata.json`
- `figures/12b_final_iterated_wkb/previews/candidate_gallery.png`
- `prompt_12b_final_iterated_wkb_figures_and_manuscript_section.log`
- `prompt_12b_final_iterated_wkb_figures_and_manuscript_section.diff`

Use `git check-ignore -v` on these paths and report whether any intended file is
ignored. Do not silently force-add an ignored file.

Also inspect, without initially modifying, the exact directory
`tmp/12b_diff_new` if it exists. Establish:

- whether it is inside the repository;
- whether Git tracks or reports anything beneath it;
- whether it contains only the temporary snapshot used to construct the bad
  diff;
- whether every file there that resembles an intended 12b deliverable has a
  byte-identical counterpart at the correct repository path.

Use hashes or `cmp`, not filenames alone. If the directory contains anything
unique or uncertain, do not delete it; report the ambiguity and stop before any
cleanup.

## 2. Preserve the accepted scientific and visual result

Confirm by hashes that the four final PNGs and `manuscript/manuscript.tex` are
unchanged during 12b_1. Record before/after SHA-256 hashes in the log. Do not
edit any of them.

Perform quick read-only checks:

- the manuscript still references exactly the four intended PNG paths;
- the metadata sidecar lists exactly those four final PNGs;
- the two requested cases remain exactly `eta=4.0, k=2` and
  `eta=0.25, k=3`;
- `pdfinfo manuscript/manuscript.pdf` still reports 33 pages;
- the existing 12b log still reports 16 focused tests and 106 full-suite tests
  passing.

Do not rerun the four-minute full suite merely to repair an audit filename. Run
only a very small path/metadata check if useful. The accepted 12b test results
remain authoritative unless a file mismatch is discovered.

## 3. Deal safely with `tmp/12b_diff_new`

If and only if all of the following are true:

1. `tmp/12b_diff_new` exists inside the repository;
2. it is untracked and contains only the verified temporary 12b snapshot;
3. every relevant file is byte-identical to its correct-path counterpart or is
   an obsolete copy of the defective audit artifact;
4. no unique user data is present;

then remove exactly `tmp/12b_diff_new` after recording its inventory and hashes.
Do not use a broad glob, unresolved variable, repository-root deletion, or any
command that could affect another `tmp` directory. If any condition fails,
leave it untouched and explain why.

After the decision, run `git status --short` again and confirm that no intended
12b deliverable has disappeared.

## 4. Generate a correct, self-contained binary audit diff

Do not overwrite the defective 12b diff. Preserve it as evidence of the
original artifact-generation problem.

Create a new independent file:

`prompt_12b_1_repair_diff_paths_and_verify_repository.diff`

This new file must be a valid Git binary patch for the intended 12b changes,
with repository-relative headers. Its `diff --git` headers must use paths such
as:

```text
diff --git a/manuscript/manuscript.tex b/manuscript/manuscript.tex
diff --git a/figures/12b_final_iterated_wkb/... b/figures/12b_final_iterated_wkb/...
diff --git a/scripts/12b_final_iterated_wkb_figures.py b/scripts/12b_final_iterated_wkb_figures.py
diff --git a/tests/test_12b_final_iterated_wkb_figures.py b/tests/test_12b_final_iterated_wkb_figures.py
```

It must contain no header or payload path beginning with or containing:

- `tmp/12b_diff_new`
- an absolute filesystem path;
- the temporary directory used to build the corrected patch.

Include the intended 12b text change and all intended new 12b source/test/data
and figure files. Do not include unrelated 12a/12a_1 changes, caches, compiled
LaTeX auxiliaries, the uploaded prompt, or the new 12b_1 `.diff` itself. Follow
the repository's established convention about whether the rebuilt manuscript
PDF is included; do not change that convention merely for this repair.

Because new untracked files are not emitted by ordinary `git diff`, construct
the patch deliberately. A safe method is to concatenate:

1. `git diff --binary` for the tracked `manuscript/manuscript.tex` change;
2. one `git diff --no-index --binary /dev/null <repository-relative-file>`
   fragment for every intended new untracked file.

Run from the repository root and inspect every resulting header. If that method
does not yield exact `a/<repo-path>` and `b/<repo-path>` headers on this Git
version, use a temporary Git repository outside the project: commit a verified
baseline snapshot, overlay the intended final files at their repository-relative
paths, and run `git diff --binary` there. Do not repair paths with an unchecked
global text substitution over binary-patch content.

The 12b log may be included under its correct root-relative filename. Do not
include the defective 12b diff inside the corrected diff; that would recursively
bloat the audit and preserve the wrong headers as patch content.

## 5. Validate the corrected patch

Validation is the core of this microstage. At minimum:

1. list every `diff --git` header in the corrected patch;
2. assert that none contains `tmp/`, `12b_diff_new`, an absolute path, or `../`;
3. assert that every expected intended 12b file appears exactly once;
4. assert that no unrelated path appears;
5. run `git diff --check` on the real worktree;
6. test the patch in a disposable directory or temporary Git worktree against
   the correct pre-12b baseline if that baseline can be reconstructed safely;
7. after applying it there, compare hashes of the reconstructed 12b text,
   scripts, tests, metadata, and four PNGs with the real intended files.

If the precise pre-12b baseline cannot be reconstructed without disturbing the
worktree, do not fake the patch-application test. Perform all other structural
and hash validations and state that limitation explicitly.

Finally run:

```bash
git status -sb
```

Do not stage, commit, or push.

## 6. Independent 12b_1 report

Create:

`prompt_12b_1_repair_diff_paths_and_verify_repository.log`

The log must contain:

- initial and final Git status;
- diagnosis: audit-only defect versus real misplaced files;
- intended-path existence and ignore checks;
- inventory and disposition of `tmp/12b_diff_new`;
- before/after hashes proving no changes to the four final PNGs and manuscript
  source;
- all corrected `diff --git` headers;
- forbidden-path scan result;
- expected-path and unrelated-path validation;
- disposable patch-application/hash-test result, or the exact reason it could
  not safely be performed;
- `git diff --check` result;
- confirmation of the four manuscript references, metadata cases, and 33-page
  PDF;
- complete list of files created, removed, or otherwise affected by 12b_1;
- confirmation that no scientific text, figures, colour choices, thresholds,
  tests, or mathematical claims changed;
- one verdict:
  `12B AUDIT DIFF PATHS REPAIRED AND VERIFIED`,
  `REAL WORKTREE PATH PROBLEM FOUND`,
  `PARTIAL`, or `BLOCKED`, with a precise explanation.

This is an audit repair, not Stage 12c. The numerical hammer and its paintings
must remain exactly as accepted; only the Git signpost is to be straightened.
