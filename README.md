# Assume Breach

*A First Course in Defensive Security*, by Michael Borck.

A lean, open-access introduction for readers without a security background.
Twelve chapters build toward a self-contained fictional defender's dossier.
The core route needs no AI account, lab installation or game group.

## Reading and resources

- [Free online book](https://michael-borck.github.io/assume-breach/)
- [DeepWiki](https://deepwiki.com/michael-borck/assume-breach)
- [Book series](https://books.borck.education)
- `appendices/defender-dossier.qmd`: printed case inputs, worked reasoning,
  paper firewall tests and independent transfer task.
- `appendices/lab-environment.qmd`: optional practice boundaries.
- `appendices/further-reading.qmd`: primary-source trail.

The existing cover and chapter artwork are unchanged. Source chapters use
stable `chapters/01-...` through `chapters/12-...` filenames, not week numbers.
A course may map its schedule to them without the book requiring that course.

## Local build and checks

Requires Quarto and a LaTeX toolchain for PDF. From this repository:

```bash
python scripts/check_manuscript.py
quarto render --to html
```

From the parent books workspace, the publisher builds HTML from the live
source and PDF/EPUB from disposable preprocessed copies:

```bash
python book-publisher/publish.py --book ab --llm --preprocess --render
python book-publisher/tools/check_rendered_book.py assume-breach
```

Do not use the publisher's all-steps option merely to proof a revision;
publishing and source-control steps are separate actions. Generated
`_book/`, `_print_source/` and `llm.txt` are not manuscript sources.

## Editorial and publication status

The approved September 2026 developmental revision keeps the chapter order
and focuses on safety, accuracy and independent practice.
[EDITORIAL-REVISION.md](EDITORIAL-REVISION.md) records validation and remaining
human release gates. No ISBN has been assigned in local metadata; do not
treat a local render as an Amazon/KDP publication.

## Licence and assets

The author confirmed [Creative Commons Attribution 4.0 International
(CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) on 2026-09-15.
The author confirmed permission to use the existing artwork on 2026-09-15;
this is an author attestation, not an independent provenance audit.
Metadata and both copyright sources name that version. Do not copy third-party game cards, lecture images
or vendor materials into the book.
