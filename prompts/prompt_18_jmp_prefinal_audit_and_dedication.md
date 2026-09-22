# Prompt 18 — Journal of Mathematical Physics pre-submission audit and dedication

Work in the Kerr-cavity repository. The last completed prompt was 17. This is a careful, independent pre-submission audit of the **current canonical manuscript** for the *Journal of Mathematical Physics* (JMP), followed by conservative corrections and a final build. Do not assume that the older stage-15 source or the arXiv package is still the canonical source.

## Initial state and protected work

Before editing, record `pwd`, `git status -sb`, `git log -1 --oneline --decorate`, `git status --porcelain=v1`, and the current diff. Identify the canonical `manuscript/manuscript.tex`, bibliography, figures, and the files created by prompts 16 and 17. Read the latest prompt-16/17 reports if available. The working tree may be dirty; preserve every pre-existing change. Never overwrite the canonical source from an older snapshot. Do not commit or push. Do not submit to JMP or alter the already submitted arXiv version or `arxiv/` package merely to make the journal version agree with it.

If the canonical target is ambiguous or a pre-existing change cannot safely be distinguished from your proposed edit, stop and report the conflict rather than guessing.

## The one requested authorial addition

Add the following exact dedication, once, in a restrained and readable position near the title/front matter, separate from the abstract and separate from the Acknowledgment section:

> To the memory of my Mother.

Do not expand or paraphrase it. Do not add biographical details. Preserve the existing AI-assistance acknowledgment from prompt 17 unless a verified journal policy requires a specific adjustment; explain any such adjustment and do not silently erase the disclosure. Check that the dedication is visible in the compiled PDF, is not accidentally incorporated into arXiv metadata, and does not break title-page layout. If the current class/template provides a suitable dedication mechanism, use it; otherwise use the smallest robust LaTeX construction. Do not duplicate it in the cover letter.

## Source-of-truth journal requirements

On the day of the audit, consult current **official AIP/JMP** pages, especially:

- <https://publishing.aip.org/resources/researchers/author-instructions/>
- <https://pubs.aip.org/aip/jmp>
- relevant linked AIP policies for authorship, AI use, data availability, accessibility, graphics, and submission ethics.

Record access dates and links in the report. Distinguish requirements for **initial submission** from production-stage formatting, and JMP-specific rules from general AIP guidance or another journal's length limits. AIP currently encourages the JMP-specific TeX template and says an initial submission needs a single compiled manuscript PDF; verify the live wording. Do not assert that a wholesale conversion to REVTeX or a particular page/word limit is mandatory without direct JMP/AIP evidence. If reformatting is genuinely necessary, make a focused recommendation and estimate the work; do not perform a risky whole-manuscript conversion without author approval.

## Scientific and mathematical audit — rigorous but proportionate

Read the entire current manuscript, including appendices, captions, bibliography, and the newly added acknowledgments. Review it as a conscientious JMP referee would, independently of the success claims in earlier audit logs. For every central result, inspect its hypotheses, statement, proof or derivation, and downstream uses. In particular:

- self-adjointness, domain/core, lower bound, compact resolvent, simplicity and ordering of eigenvalues;
- the normalized HeunWI/Whittaker–Ince formulation, recurrence, minimal-solution continued fraction, entireness-versus-Bargmann implication and exceptional `F=0` case;
- Liouville gauge, branches, endpoint classifications and local-versus-global connection claims;
- Volterra sectorial construction and claimed error bounds;
- Olver and Fedoryuk scalings, connection hypotheses, strong-drive coefficients and signs;
- weak-drive perturbation and multiplicative resummation, including nondegeneracy and zero-related qualifications;
- interpretation and reproducibility of figures, exploratory iteration portraits, and any newly added figures in prompts 16–17.

Verify dimensional consistency and the convention `\Delta=\omega_c-\omega_d` with `+\hbar\Delta N`, including every definition of dimensionless `\delta`. Check numbering, internal references, exact/formal/asymptotic/numerical/conjectural classifications, and whether abstract, introduction, conclusions and acknowledgments reflect what has actually been established. Do not treat numerical agreement or successful compilation as proof. If a substantive gap cannot be resolved with a short, demonstrably correct correction, **report it as a blocker with a precise location and counterargument/proof obligation**; do not invent a theorem, lower the claim silently, or bury the issue in stylistic edits.

Assess suitability for JMP: make the mathematical contribution, novelty relative to cited prior work, physical motivation, and boundaries of conjectural material legible to a mathematical-physics reader. Be honest without turning the article into a catalogue of failures. Do not gratuitously rewrite the author's voice, including deliberate passive constructions. No broad reorganization merely for taste.

## Bibliography, ethics and journal-facing completeness

Check that each material citation supports the nearby claim; verify uncertain bibliographical details against primary sources when possible and mark anything unverified. Distinguish established standard facts from original contributions; identify missing essential prior art without adding speculative citations. Check the arXiv preprint status and any previous dissemination for accurate disclosure, while avoiding invented identifiers or dates.

Apply the current AIP/JMP checklist to the actual paper, including:

- title, author name, affiliation and corresponding-author details (do not invent missing personal/institutional information);
- abstract in a single paragraph, appropriate scope and length, clear motivation/results/conclusion;
- section order, numbered pages, acknowledgments, author declarations, conflict-of-interest statement, author contributions if applicable, and data availability statement;
- figures and tables: numbered/cited/captioned, legible, accessible alt text under current AIP rules, and adequate provenance and reproducibility;
- appendix title and equation numbering;
- references, links/DOIs, and citation consistency;
- AI-assistance acknowledgment against current AIP policy, without listing AI as an author;
- whether the manuscript's numerical data and generating code warrant a repository or a specific data-availability statement rather than a false “no new data” declaration;
- source/PDF submission files, permissions, and any required author choices.

For declarations involving the author's actual affiliation, funding, conflicts, data/code-sharing choice, rights or consent, **do not guess**. Give the author an exact proposed wording only where the facts are known; otherwise flag a short, specific question or decision. Separate technical compliance from editorial judgment. Do not prepare or send a cover letter unless requested.

## Editing boundary

You are authorized to add the exact dedication and fix objectively demonstrable, local defects found by the audit. Preserve all existing author work, source files, figures and the arXiv submission. Do not change scientific claims by stealth, undertake new calculations without a defined need, generate replacement figures, or rework the document into a new template merely to satisfy a preference. For each manuscript edit, record the exact reason and the before/after text or equation. If the journal requires a substantive change or the scientific issue is debatable, report it for the author's decision rather than making it automatically.

## Build and visual verification

Use the repository's established build procedure. Compile from a clean **generated-artifact** state without deleting user files; run BibTeX and sufficient LaTeX passes. Inspect complete `.log`/`.blg` output for unresolved citations/references, duplicate labels, missing figures/packages, warnings and suspicious boxes. Run relevant existing tests or verification scripts selectively, and identify exactly what they do and do not establish. Review the final PDF visually, especially the title page/dedication, equations and figures affected by edits, declarations, appendices and bibliography. Confirm consistency of the final TeX and PDF and run `git diff --check`.

## Deliverables

At the repository root, produce:

```text
prompt_18_jmp_prefinal_audit_and_dedication.log
prompt_18_jmp_prefinal_audit_and_dedication.diff
```

The `.log` must include: initial and final Git status; official JMP/AIP requirements with access dates and links; a finding-by-finding table with severity (`blocking`, `important`, `optional`), precise source location, evidence, action taken or author decision needed; a separate concise mathematical-result status table; bibliography/ethics/accessibility/data checklist; every edit and its justification; build and test commands/results; PDF review; unresolved issues; and a final verdict: `READY FOR JMP SUBMISSION`, `READY AFTER AUTHOR DECISIONS`, or `NOT READY — BLOCKING ISSUES`.

The `.diff` should be the full current tracked patch from `git diff --binary`, with an explicit note that it may include pre-existing uncommitted work and does not contain untracked/ignored files. Additionally show a focused stage-18 change summary in the log so the author's changes are distinguishable from yours. Do not modify the Git index merely to manufacture a patch.

End with an actionable, short list of remaining author-side decisions and the exact files needed for an initial JMP submission. Do not commit, push, modify the arXiv version, upload files to the journal, or claim acceptance by editors.
