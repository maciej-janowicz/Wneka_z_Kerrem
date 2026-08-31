# Prompt 13 — full pre-final mathematical and bibliographical integrity audit

Work in the repository:

```bash
cd ~/Dokumenty/Prace_i_dnie/Wnęka_z_Kerrem
```

The completed and approved manuscript baseline is commit `d0c1911` (`Add regularized WKB iteration portraits`). Stages 12a–12b_1 have been committed and pushed. The audit prompt itself has subsequently been copied into the repository as the intentionally untracked file `prompts/prompt_13_prefinal_integrity_audit.md`; this one file is part of the expected audit setup and must not be treated as contamination of the manuscript baseline.

Before making any changes, run:

```bash
git status -sb
git log -1 --oneline --decorate
git rev-parse HEAD
git rev-parse origin/master
git status --porcelain=v1
```

Proceed only if all of the following are true:

- the branch line is `## master...origin/master` (with no ahead/behind indication);
- `HEAD` and `origin/master` both resolve to `d0c1911a4b3dd470faec8761bad5fe433393095a`;
- there are no tracked modifications, staged changes, renames, deletions, conflicts, or other uncommitted changes;
- the only permitted untracked path is exactly `prompts/prompt_13_prefinal_integrity_audit.md`.

In other words, the acceptable `git status --porcelain=v1` output at the start is exactly:

```text
?? prompts/prompt_13_prefinal_integrity_audit.md
```

Treat that single file as the audit instruction, not as a manuscript change. If `git status --porcelain=v1` contains any additional line, or if any other condition above fails, stop and report the discrepancy without modifying anything. Do not add, commit, move, rename, or edit the prompt file during the audit.

## Objective

Perform a full pre-final audit of the manuscript's mathematical, logical, notational, structural, and bibliographical integrity. This is not a stylistic rewrite and not an invitation to redesign the paper. Read the entire manuscript, all appendices, bibliography, and all repository notes/scripts/tests that are needed to check its claims. Follow every internal cross-reference and reconstruct the dependency chain of the principal results.

The audit must both:

1. identify and document every material issue; and
2. make conservative, well-supported corrections where the correct remedy is clear.

Do not conceal a gap by polishing prose. Do not upgrade a formal or numerical observation into a theorem. Do not invent a proof, citation, quotation, page number, theorem number, bibliographical field, or source content.

## 1. Global logical map

Construct a private working inventory of every definition, assumption, proposition, lemma, theorem, corollary, conjecture, quantization condition, asymptotic formula, numerical claim, and interpretive conclusion. For each item determine:

- precisely what assumptions it uses;
- which previous statements it depends on;
- whether its conclusion is actually established at the stated level of generality;
- whether domains, parameter ranges, branches, sectors, boundary/regularity conditions, and limiting procedures are stated;
- whether exceptional and degenerate cases are excluded when necessary;
- whether it is used later more strongly than it was proved.

Classify every nontrivial result explicitly in the audit report as one of:

- **rigorously proved**;
- **formal derivation**;
- **controlled asymptotic statement**;
- **numerically supported statement**;
- **heuristic interpretation**;
- **conjecture/open point**.

Check that the manuscript itself communicates these distinctions honestly and consistently. Correct overstatements. If a central result cannot be justified, do not silently delete it: flag it as a blocking issue and propose the smallest defensible reformulation.

## 2. Line-by-line mathematical verification

Verify all displayed and consequential inline calculations independently, including algebraic transformations, scalings, signs, factors of `2`, powers of `V`, `\hbar`, `F`, and `|F|`, energy normalizations, branch choices, asymptotic orders, remainder statements, index ranges, and dimensional consistency.

In particular, audit the entire chain connecting:

- the Kerr Hamiltonian and the Bargmann representation;
- the differential equation and its double-confluent Heun form;
- regularity/entireness and Bargmann-space normalizability;
- self-adjointness or the precise operator-theoretic statement actually established;
- recurrence relations and spectral/quantization conditions;
- the Olver construction, turning/Stokes geometry, sectorial assumptions, and error-control claims;
- the Fedoryuk construction, including admissible contours, canonical domains, Stokes/separatrix geometry, connection formulae, and the exact status of the resulting quantization condition;
- the strong-drive expansion and every stated coefficient/order, including dependence on the level index;
- essential-singularity cancellation and the status of `C_ess(E)=0` (proof, condition, or conjecture must not be blurred);
- the Bender–Bettencourt strong-coupling/quasi-linearization material, including the splitting, logarithmic/Riccati variables, `Y_2`, `S_2`, expectation-value energy calculation, and any multiplicative resummation claims;
- the regularized WKB iteration portraits: definition of the iterated map, regularization, parameter choices, what is plotted, and the limited evidential meaning of the figures.

Check every proof line by line. Look specifically for circular reasoning, unjustified interchange of limits/sums/integrals/derivatives, unproved analyticity or decay, division by possibly vanishing quantities, inconsistent local/global statements, omitted boundary terms, nonuniform asymptotics presented as uniform, and conclusions inferred from plots alone.

Whenever a symbolic or numerical check can materially test a formula, use or extend the repository's existing scripts/tests rather than trusting visual inspection. Keep any new check minimal and reproducible. A passing numerical check is not a proof; record what it does and does not establish.

## 3. Standard results versus unnecessary lemmas

Identify lemmas or propositions that are standard textbook facts from complex analysis, asymptotic analysis, ordinary differential equations, functional analysis, Bargmann/Fock-space theory, or spectral theory.

For each such item decide whether it should be:

- removed and replaced by a precise citation;
- shortened to a clearly labelled recalled standard fact with a citation; or
- retained because its exact specialized formulation or proof is genuinely needed.

Do not replace a proof by a vague citation. The cited source must actually support the precise statement under the hypotheses used here. Conversely, do not retain elementary pseudo-original lemmas merely to inflate the formal apparatus.

## 4. Bibliographical and citation audit

Audit every citation and every bibliography entry.

For each in-text citation verify:

- that the cited source is relevant to the exact adjacent claim;
- that attribution is historically and mathematically accurate;
- that theorem/section/equation/page references, if given, are correct;
- that a primary source is used when a priority or author-specific result is claimed;
- that a textbook/monograph is used appropriately for standard background;
- that no source is cited second-hand as if directly checked.

For the bibliography verify, as far as the available sources and reliable metadata permit:

- authors, title, journal/book title, volume, year, pages/article number, publisher, edition, DOI/arXiv identifier, capitalization, and entry type;
- consistency between citation keys and entries;
- cited-but-missing and uncited entries;
- duplicate or near-duplicate entries;
- uniform formatting consistent with the manuscript's bibliography style.

Pay particular attention to sources connected with Bargmann representation, double-confluent Heun equations, Olver, Fedoryuk, Voros/complex WKB, Bender–Bettencourt, and Madelzweig–Krivec/quasi-linearization.

Use authoritative metadata and, where a claim depends on source content, inspect the source itself if it is locally available or legitimately accessible. If a source cannot be checked, say so explicitly in the report and mark the item **unverified**. Never infer bibliographical details from memory or fabricate a locator.

## 5. Notation, definitions, cross-references, and structural integrity

Check globally:

- uniqueness and consistency of every symbol;
- definitions before first use;
- consistent use of `E`, `\mathcal{E}=2E/V`, `F`, `|F|`, `V`, `\hbar`, `\omega_0`, level indices, scaled variables, and branch conventions;
- equation, theorem, section, appendix, figure, and bibliography numbering;
- every `\label`, `\ref`, `\eqref`, and citation;
- agreement between captions, plotted data, scripts, surrounding discussion, and conclusions;
- consistency of abstract, introduction, main text, conclusion, and appendices about what the paper actually proves;
- stale terminology, duplicate passages, placeholders, TODOs, editorial comments, obsolete filenames, and all remnants of internal workflow language such as “Stage”, “stage 07”, etc.;
- claims promised in the introduction or conclusion but never delivered in the body;
- results established in the body but misstated or omitted in the abstract/conclusion.

Preserve the project's established conventions and terminology. Do not gratuitously change notation or the physical normalization.

## 6. Severity and correction policy

Assign every issue one severity:

- **BLOCKER** — invalidates a central result, proof, operator statement, quantization condition, or principal conclusion;
- **MAJOR** — substantial gap, overclaim, wrong formula, materially inadequate citation, or serious inconsistency;
- **MINOR** — local ambiguity, missing hypothesis, weak cross-reference, bibliographical defect, or nonfatal notational problem;
- **COSMETIC** — typography or wording with no mathematical effect.

Apply clear BLOCKER/MAJOR corrections only when they can be justified completely and locally. Otherwise preserve the evidence, weaken the manuscript's claim to the defensible level if that remedy is unambiguous, and record the unresolved issue prominently. Apply safe MINOR/COSMETIC corrections. Avoid broad refactoring, wholesale rewriting, new speculative theory, or expansion of the paper's scope.

## 7. Required validation

After edits:

1. compile the manuscript from a clean auxiliary-file state using the repository's established build procedure;
2. run all existing relevant tests and verification scripts;
3. run any new minimal checks introduced by this audit;
4. inspect the compiler log for undefined references/citations, multiply defined labels, missing bibliography entries, serious warnings, and layout failures;
5. inspect the final PDF sufficiently to catch broken equations, figures, captions, references, and bibliography layout;
6. run repository-wide searches for placeholders, workflow-stage remnants, suspicious unresolved references, and uncited/missing keys;
7. finish with `git diff --check` and `git status -sb`.

Do not treat successful compilation as mathematical validation.

## 8. Required deliverables

Create:

1. `prompt_13_prefinal_integrity_audit.log` — a self-contained audit report containing:
   - the verified baseline commit and initial cleanliness check;
   - a concise dependency map of the principal results;
   - the result-classification table;
   - an issue ledger ordered by severity, with exact manuscript locations;
   - for every BLOCKER/MAJOR item: the claim, diagnosis, consequence, action taken, and residual risk;
   - a list of standard/trivial lemmas reviewed and the decision for each;
   - a citation/bibliography verification table, including all unverified items;
   - files changed and why;
   - commands/checks run and their exact outcomes;
   - remaining open questions and a clear verdict: **ready for author review**, **ready only after listed repairs**, or **not mathematically ready**.

2. `prompt_13_prefinal_integrity_audit.diff` — the complete patch relative to `d0c1911`, generated only after all edits and validation.

The `.log` must be candid and diagnostic, not a victory summary. Exact locations should use stable identifiers (section/equation/theorem/figure/citation key) and may additionally include line numbers.

## 9. Final response

In the terminal response, give only:

- the overall verdict;
- counts of BLOCKER/MAJOR/MINOR/COSMETIC issues, distinguishing fixed from unresolved;
- the most important unresolved risks;
- files changed/created;
- build and test status;
- confirmation that the `.log` and `.diff` were written;
- final `git status -sb`.

Do **not** commit, push, tag, reset, stash, or discard anything. Leave all audit changes in the worktree for author inspection.
