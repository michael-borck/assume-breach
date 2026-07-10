# Assume Breach

*A First Course in Defensive Security*

An open-access Quarto book by **Michael Borck** — a lean, standalone first book on defensive
security for newcomers, not a comprehensive textbook. Eleven chapters in a deliberate order.
It reads on its own; a course can also assign it chapter by chapter (the course keeps the
week → chapter map, not the book). Part of the
[books.borck.education](https://books.borck.education) series.

> ⚠️ **Early draft.** Chapter 1 is a full pilot; Chapters 2–3 are seeded; Chapters 4–11 are
> skeleton stubs marked `*(Draft outline …)*`. The book is **standalone and tool-agnostic by
> design** — it names no course, week, lab, or tool syntax. See `CHAPTER_OUTLINE.md`.

## Structure

- `index.qmd` — Introduction: the defender's mindset, how the book works, the AI stance.
- `chapters/week-NN-*.qmd` — one chapter per teaching week (Week 7 is tuition-free; there is
  no Week 7 chapter — this is intentional).
- `CHAPTER_OUTLINE.md` — the blueprint: title decision, week↔chapter map, per-chapter status,
  and the writing/copyright/build notes. **Read this first.**
- `_quarto.yml` — book configuration (HTML / PDF / EPUB).

## Build

```bash
quarto preview       # live HTML preview while writing
quarto render        # build all formats into _book/
```

Requires [Quarto](https://quarto.org). No other dependencies for the HTML build; PDF needs a
LaTeX toolchain (TinyTeX: `quarto install tinytex`).

## Licence

Creative Commons Attribution (CC BY). The technical content is the coordinator's own writing;
**third-party images and cheat-sheets from the source lecture decks must not be pasted in** —
see the copyright note in `CHAPTER_OUTLINE.md`.
