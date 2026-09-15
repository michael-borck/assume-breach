# Assume Breach: editorial revision record

Date: 2026-09-15. Revision based on source commit `deeb0f9`.
**Approved developmental revision implemented and locally validated.**
This is editorial closure, not release approval or a claim of KDP publication.

## What changed

The twelve chapters retain their order and stable filenames. The preface now
states observable book and part outcomes, minimal prerequisites and a solo,
no-install route. The new Harbour Community Centre dossier supplies every case
input, a complete worked answer and an independent changed-scenario assessment.
All twelve chapters contribute a timed paper task; three retain optional AI
extensions using fictional inputs only. The original games remain optional.

| Chapter | Main disposition |
|---|---|
| 1 Introduction | Contextual CIA trade-offs, qualified defence in depth, explicit permission and a seven-activity lifecycle |
| 2 Software and malware | Coordinated disclosure, qualified prevalence/Target claims and ransomware limits; malware definitions stay here |
| 3 Authentication | Password-hash cost, online/offline distinctions, NTLM limits, phishing-resistant MFA and permission/recovery tests |
| 4 Cryptography | Signatures versus encryption, trusted digests, authenticated key identity and authenticated encryption |
| 5 Risk | Bounded expected-loss calculation, sensitivity and non-financial limits; accountable risk acceptance |
| 6 Incident and recovery | Early triage and concurrent preservation, RTO/RPO tests, backup separation and disclosure limits |
| 7 Networks | Compact network primer, capture-point visibility, TLS identity and trust boundaries |
| 8 VPNs and firewalls | Full/split-tunnel scope; explicitly simplified first-match rules with positive and negative tests |
| 9 Web and privacy | Object-level authorisation failure; context-aware XSS prevention; distinct Australian/EU notification conditions |
| 10 Cybercrime | Evidence, economics and uncertain attribution; reduced repetition of chapter 2 |
| 11 Human factors | Qualified human/AI claims, independent verification and safe reporting practice |
| 12 The long game | One concise ending, solo capstone, explicit success criteria and a separate optional group game |

The optional lab appendix distinguishes NAT, host-only and internal networks,
does not present containers or snapshots as complete containment, and states
permission, synthetic-data and stop conditions. A further-reading appendix
provides a curated primary-source trail; consequential claims also have nearby
sources. This is educational material, not operational or legal advice.

README and chapter-outline inventories match the source. Broken author links
were replaced with verified public profile/catalogue links. Nested PDF/EPUB
downloads now resolve from chapter pages. Existing cover and illustrations
were not changed.

## Build-system repairs

The shared publisher now generates separate PDF/EPUB profiles with independent
output directories. EPUB retains the Markdown copyright content; PDF uses
the existing TeX copyright page without an extra empty copyright chapter.
The base configuration deliberately contains no chapter arrays, because Quarto
merges those arrays across profiles. Regression fixtures inspect the effective
Quarto configuration, not just the generated YAML.

The external-link helper no longer joins a URL used as a Markdown label to its
target. The publisher CLI now reports failed actions through its exit status.
These shared changes were exercised by the complete Assume Breach build;
other books were not rebuilt or published in this pass.

## Validation

- Eight Assume Breach source tests pass: configured order, local references and
  assets, practice boundaries, case budget/loss/recovery arithmetic, printed
  firewall behaviour, downloads and copyright configuration.
- Eleven publisher tests pass: five editorial-helper checks, three copyright
  profile fixtures and three CLI exit-status checks. Quarto inspection ran.
- CND's four and Prove's nine existing source tests still pass. Total: 32.
- HTML, PDF and EPUB build locally through the publisher. The PDF is 106 pages,
  6 × 9 inches. Its sole copyright occurrence is on physical page 2.
- Rendered validation reports zero errors: 19 HTML pages, 1,243 local
  targets/anchors, EPUB XML/spine order and ZIP integrity; 21 EPUB spine entries.
- In the initial revision scan of 35 manuscript URLs, 33 returned HTTP 200,
  including the FBI link
  on retry. CISA's ransomware guide and the Senate Target report returned 403
  to the automated client. That is an access restriction, not a dead-link
  verdict. The subsequently added official CC BY 4.0 page was also opened
  successfully when the author confirmed the version. Reachability does not
  establish factual accuracy.
- All twelve PDF chapter openings were checked in reading order from extracted
  text. Copyright and selected case/table/answer pages were visually inspected.
  The evidence table fits on one page and the transfer answer starts on its own
  print page. This is not a visual proofread of every page.
- Publishing metadata audit: zero errors or warnings; still
  `not-yet-published`, with no assigned ISBN/ASIN.

Approximate prose is 22,092 words across 19 configured files, compared with
22,203 across 17 at audit. Core chapters fell from 20,198 to 17,984 words
(about 11%) while the new worked case and resources supplied missing practice.
The scanner is a diagnostic, not an exact typesetter word count: it includes
some table metadata. The two remaining repeated-sentence findings are the
shared optional-AI introduction and safety boundary across three chapters.

## Fresh-reader acceptance test

Ask a reader unfamiliar with the manuscript to follow the solo route, without
author hints, an AI account, a game group or installed lab. Keep their notes
on unclear terms, missing inputs and any point where they need outside help.

After reading, have them attempt the weekend-programme transfer for 30–45
minutes without consulting the worked answer. They should submit the one-page
decision and then self-check against the eight printed criteria.

Pass: at least seven criteria, no unsafe action or invented input, no claim
that 130 minutes meets a 120-minute recovery target, and no unsupported
“ready” verdict. Record elapsed time, score, hints needed and the actual
decision. Repair a missing prerequisite or ambiguous input before release;
do not coach the reader into a pass. This test has **not** yet been conducted.

## Rights and release gates

The author confirmed permission to use the existing artwork on 2026-09-15.
This records the author's attestation, not an independent asset-provenance
audit. No creator, generation tool or third-party licence was inferred.

The author specified Creative Commons Attribution 4.0 International (CC BY 4.0)
on 2026-09-15. Quarto metadata, Markdown copyright, TeX copyright and README
now name that version; copyright pages link to the official licence. Source
checks guard this consistency. This closes the licence-version gate.

Still required: the fresh-reader attempt, the author's complete page-by-page
proof (including diagrams and citations), target-device/accessibility checks,
and separate release approval. The PDF is not tagged. Optional interactive
labs and third-party games were not executed.

No commit, push, hosted-book/chatbot deployment, cover redesign, KDP upload,
ISBN assignment or Amazon record change was performed for this revision.

## Repeat locally

From the parent books workspace:

```sh
python assume-breach/scripts/check_manuscript.py
python -m unittest discover -s book-publisher/tools -p 'test_*.py' -v
python book-publisher/publish.py --book ab --llm --preprocess --render
python book-publisher/tools/check_rendered_book.py assume-breach
python book-publisher/publish.py --book ab --audit
```

The optional network check is
`python book-publisher/tools/check_external_book_links.py assume-breach`.
The versioned audit snapshot in `book-publisher/audits/2026-09-15/books/ab/`
contains the plan, refreshed metrics and detailed external-link results.
