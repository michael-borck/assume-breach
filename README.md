# Defence in Depth

*A First Course in Information Security for the Age of AI* — **provisional title**

An open-access Quarto book by **Michael Borck**, the pre-reading companion for ISYS2012
Information Security (2nd-year undergraduate). One chapter per teaching week: students read
chapter *N* before Week *N*'s lecture, so the lecture can be interactive (demos, debate, polls)
instead of transmission. Part of the [books.borck.education](https://books.borck.education)
series.

> ⚠️ **Scaffold.** Weeks 1–3 are seeded from the lecture decks; Weeks 4–6 and 8–12 are
> skeleton stubs marked with `*(Draft from …)*`. See `CHAPTER_OUTLINE.md` before writing.

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
