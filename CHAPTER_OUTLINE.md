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

## Week ↔ chapter map

Chapters are named by **teaching week** to match the course repo (`lectures/`, `labs/`).
**There is no Week 7** (tuition-free) — the gap is intentional.

| Week | Chapter file | Status | Source deck |
|------|-------------|--------|-------------|
| 1 | `week-01-introduction.qmd` | **Seeded** | week-01-introduction-to-information-security |
| 2 | `week-02-software-security-and-malware.qmd` | **Seeded** ⚠️ refresh | week-02-software-security-and-malware |
| 3 | `week-03-authentication-and-access.qmd` | **Seeded** | week-03-authentication-and-access |
| 4 | `week-04-cryptography.qmd` | Skeleton ⚠️ refresh | week-04-cryptography |
| 5 | `week-05-risk-management.qmd` | Skeleton | week-05-risk-management |
| 6 | `week-06-incident-and-disaster-planning.qmd` | Skeleton | week-06-incident-and-disaster-planning |
| 8 | `week-08-network-security.qmd` | Skeleton ⚠️ narration | week-08-network-security |
| 9 | `week-09-vpn-and-firewalls.qmd` | Skeleton ⚠️ narration | week-09-vpn-and-firewalls |
| 10 | `week-10-web-security-and-data-protection.qmd` | Skeleton | week-10-web-security-and-data-protection |
| 11 | `week-11-cybercrime-and-botnets.qmd` | Skeleton ⚠️ refresh (worst) | week-11-cybercrime-and-botnets |
| 12 | `week-12-human-factors.qmd` | Skeleton | week-12-human-factors |

Week 13 is Revision — no chapter (or add a short closing chapter later).

## Per-chapter template

Every chapter follows the same shape (see the seeded Weeks 1–3):

1. Title + one-line epigraph.
2. "Before the lecture, read this chapter" + what the lab is.
3. **What this chapter covers** — 4–5 learning objectives (from the deck's Objectives slide).
4. The concept prose (written from the deck's flow).
5. **In the lab** — a callout naming the *capability* the lab exercises (not the tool syntax).
6. **Connects to** — forward/backward links to other weeks.
7. **Before the lecture** — 3 priming questions that double as the lecture's opening poll.

## Tools & demos policy (important — keeps the book durable)

**The concept chapters are tool-agnostic. No tool syntax, no "click here", no OS-specific
steps in the body.** Write what is true on any platform ("attackers crack salted hashes with
dictionary and brute-force attacks"), never "open L0phtCrack and click Run".

- **Where mechanics live:** the lab worksheets (course repo) and the Docker lab repos —
  environment-specific and freely swappable.
- **The book's only hooks to the hands-on:** the per-chapter **In the lab** callout (names a
  *capability*, links to the current lab) and the single **Lab Environment appendix**
  (`appendices/lab-environment.qmd`) — the one page that changes on migration.
- **Why:** the environment is moving VM → Docker. A tool-agnostic book carries across that
  change without edits; a book full of screenshots would rot on day one.

### Environment direction (context for writing, not book content)

This offering: Windows XP VM (locked). Next: **Docker labs**, from the coordinator's existing
repos (`sec-utils`, `password-lab`, `forensics-docker-lab`, `ethical-hacking-docker-labs`),
which already provide web-GUI Wireshark/Autopsy and one-command bring-up. The one gap
(`iNetworkSimulator`, firewall lab) is replaced by **real `iptables`/`nftables` in a
container** — a better lab than the simulator. Write chapters so *none* of this shows through
in the concept text.

## Writing order

Write **chapter N before Week N** — stay one or two chapters ahead of the cohort, as
*Substantiate* did. Weeks 1–3 first (start of semester), then keep pace.

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
