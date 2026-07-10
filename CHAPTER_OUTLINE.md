# Chapter Outline & Build Blueprint — *Defence in Depth*

The blueprint for writing this book. Read before drafting a chapter.

## What this book is

The **pre-reading companion** for ISYS2012 Information Security. It carries the *knowledge*
layer so the 2-hour lecture can be spent on what a page can't do — live demonstrations, debate,
and polls. Design rationale is in the course repo: `docs/teaching-plan.md`.

- **Audience:** 2nd-year undergraduates, no prior security background. Keep the register
  accessible — explain, don't assume. (Contrast the postgrad register of *Substantiate, Don't
  Assume*.)
- **Spine:** *think like a defender* — understand the attack to remove what it needs; weigh
  every control's cost; never forget the human.
- **Rhythm:** read → discuss/see → do. Chapter *N* is read before Week *N*; the lecture is
  interactive; the lab is hands-on.

## Title — decided

**"Assume Breach"** / subtitle *"A First Course in Defensive Security"*. Deliberately a lean
*companion*, not a rival to Stallings/Whitman; the title carries the defensive-security stance
(assume the perimeter fails; build in depth, detect, contain, recover). It breaks the series'
two-clause beat ("X, Don't Y") on purpose — it's a stronger standalone security aphorism.
Directory is `assume-breach/`.

## The book is standalone; the course maps *to* it

**The book knows nothing about the course.** No week numbers, no lectures, labs, assessments,
or "the unit" in the text — so the course can change without the book drifting. Chapters are
numbered 1–11 in a pedagogical order that *parallels* a sensible teaching sequence, but that's
all. The week → chapter mapping lives in the **course repo** (`docs/teaching-plan.md`), not
here. That is the whole point of the decoupling.

## Chapter map

| Ch | File | Status | Parallels teaching week | Source deck |
|----|------|--------|-------------------------|-------------|
| 1 | `01-introduction.qmd` | **Written** | Wk 1 | week-01-introduction |
| 2 | `02-software-security-and-malware.qmd` | **Written** | Wk 2 | week-02 |
| 3 | `03-authentication-and-access.qmd` | **Written** | Wk 3 | week-03 |
| 4 | `04-cryptography.qmd` | **Written** | Wk 4 | week-04 |
| 5 | `05-risk-management.qmd` | **Written** | Wk 5 | week-05 |
| 6 | `06-incident-and-disaster-planning.qmd` | **Written** | Wk 6 | week-06 |
| 7 | `07-network-security.qmd` | **Written** (narration captured) | Wk 8 | week-08 |
| 8 | `08-vpn-and-firewalls.qmd` | **Written** (narration captured) | Wk 9 | week-09 |
| 9 | `09-web-security-and-data-protection.qmd` | **Written** | Wk 10 | week-10 |
| 10 | `10-cybercrime-and-botnets.qmd` | **Written** (reframed off stale stats) | Wk 11 | week-11 |
| 11 | `11-human-factors.qmd` | Skeleton | Wk 12 | week-12 |
| 12 | `12-the-long-game.qmd` | **Written** | Wk 13 (revision) | — (synthesis) |

Chapters 1–11 parallel Weeks 1–12 (teaching weeks skip 7, tuition-free, so from Chapter 7 on,
chapter = week − 1). **Chapter 12 is a synthesis/closing chapter** — no source deck; it joins
the whole book into one security lifecycle and pairs naturally with the Week 13 game capstone.
This offset lives only in the course map.

## Per-chapter template (standalone)

Every chapter follows the same shape (see the written Chapter 1):

1. Title (topic only — **no** "Week N") + one-line epigraph.
2. A short standalone lead-in (no "before the lecture", no lab reference).
3. **What this chapter covers** — 4–5 learning objectives.
4. The concept prose.
5. **Try it yourself** *(optional)* — a callout naming a *capability* to practise (never tool
   syntax), pointing to the practice-environment appendix.
6. **Play it** *(optional, only where a module fits)* — a `.callout-tip` pointing readers at
   the matching *Incident Zero* module for the experiential dimension (see below).
7. **Where this connects** — links to *other chapters by name* (never weeks or labs).
8. **Questions to consider** — 3 reflective/self-test questions.

### The "Play it" callouts (Incident Zero)

*Incident Zero* ([incidentzero.retroverse.studio](https://incidentzero.retroverse.studio/)) is
a free, print-and-play cooperative security game. Where a chapter's concept has a matching game
module, a **Play it** callout invites the reader to *experience* it — the applied-judgement
dimension a page can't give. Current placements: Hardening → Ch 2; Audit & Compliance → Ch 5;
Incident Response + Disaster Recovery → Ch 6; Network Building → Ch 7; Forensics → Ch 10; and
the **full campaign** → Ch 12 (the lifecycle capstone).

**Two rules (same discipline as everything else):**

- **Reference at a stable level.** Name the *module and the experience* plus the one landing
  link. **No card names or mechanics** — it's the playtest edition and those will change.
- **Licence: link and describe, never embed.** The book is CC BY; the game is CC BY-**NC-SA**.
  Linking and paraphrasing is fine; copying game text/cards in would drag ShareAlike +
  NonCommercial onto the book. Point at it; don't reproduce it.

Callouts are **optional enrichment** — the book stands alone if the reader never plays.

## Tools & demos policy (important — keeps the book durable)

**The concept chapters are tool-agnostic. No tool syntax, no "click here", no OS-specific
steps in the body.** Write what is true on any platform ("attackers crack salted hashes with
dictionary and brute-force attacks"), never "open L0phtCrack and click Run".

- **Where mechanics live:** *outside the book* — in the course's own lab worksheets and the
  Docker lab repos, which are environment-specific and freely swappable.
- **The book's only hooks to the hands-on:** the optional per-chapter **Try it yourself**
  callout (names a *capability* to practise) and the generic **practice-environment appendix**
  (`appendices/lab-environment.qmd`), which describes VMs/containers in general — not any one
  course's setup.
- **Why:** tools and environments change (VM → Docker, and beyond). A tool-agnostic book
  carries across without edits; a book full of screenshots and tool steps rots on day one.

### Environment direction (context for writing, not book content)

This offering: Windows XP VM (locked). Next: **Docker labs**, from the coordinator's existing
repos (`sec-utils`, `password-lab`, `forensics-docker-lab`, `ethical-hacking-docker-labs`),
which already provide web-GUI Wireshark/Autopsy and one-command bring-up. The one gap
(`iNetworkSimulator`, firewall lab) is replaced by **real `iptables`/`nftables` in a
container** — a better lab than the simulator. Write chapters so *none* of this shows through
in the concept text.

## Writing order

Write in chapter order, staying ahead of wherever the material is being used. Chapters 1–3
first, then keep pace. (If you're pacing against a course, the week → chapter map in the course
repo tells you which chapter is needed when.)

## ⚠️ Copyright cleanup (do on every chapter)

The source decks embed third-party material that **cannot** go into a CC BY book:
screenshots, news images, vendor cheat-sheets, book figures. On each chapter:

- Replace embedded screenshots with described examples or your own redrawn diagrams.
- Link out to cheat-sheets (they live in the course repo `labs/*/resources/`), don't embed.
- Rewrite case studies in your own words; cite sources rather than reproducing them.

This is the main cost of the conversion — budget for it.

## ⚠️ Refresh flags

- **Week 11** — malware-volume stats (2015/2017/2021) age every year. Highest priority.
- **Week 2** — examples 2007–2013; keep the genuinely historical, update the rest.
- **Week 4** — references 2000–2006; modernise.
- **Weeks 8 & 9** — decks rely on speaker notes; that narration must be written *into* the
  chapter or the pre-read won't stand alone. Week 9 is the heaviest.

## Later additions (parity with the series)

- `llm.txt` (for NotebookLM / podcast use) and a grounded `chatbot.html` — generate once the
  text stabilises; both reinforce the unit's "use AI to learn" stance.
- Cover image, favicon, PDF/LaTeX front matter, GitHub Pages deploy (`.github/workflows`).
- Link back from the course repo once published.

## Build & deploy

```bash
quarto preview        # while writing
quarto render         # HTML + PDF + EPUB → _book/
```

Publish to GitHub Pages as the other series books do (repo → `gh-pages`), then add the
public URL to the course README and the assessment specs.
