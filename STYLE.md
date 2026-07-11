# Editorial Style — Assume Breach

House style for the prose, and the brief for the editorial pass. Apply to every chapter, the
preface (`index.qmd`), and the appendix. This is a **line edit for style, not a rewrite of
substance**: preserve all meaning, structure, headings, examples, cross-references, callouts, and
the lists noted under *Preserve exactly*.

## Hard rules

1. **No em-dashes (`—`). Remove every one.** Replace by function, do not blindly swap for a comma:
   - Parenthetical aside → commas, or parentheses if it is a true aside.
   - Restatement / appositive → a comma, or a colon if it introduces what follows.
   - Dramatic pause before a payoff → a full stop; split into two sentences.
   Most em-dashes should become sentence breaks, not commas.
2. **No decorative emojis in prose.** The `→` and link inside "Play it" callouts are functional;
   leave callouts untouched.
3. **Short sentences.** Break long, multi-clause sentences into two or three. If a sentence
   strings three or more clauses with commas, semicolons, or dashes, split it.
4. **Trim adverbs and adjectives.** Cut intensifiers and hedges that add nothing: *genuinely,
   precisely, exactly, simply, quietly, remarkably, deeply, utterly, profoundly, devastatingly,
   unsettlingly, far, very, really, actually, truly, literally*. Keep an adjective only if it
   changes the meaning.
5. **Prose over bullet points.** Convert mid-body bullet lists to flowing prose where the content
   reads as explanation. Reduce overall bullet density. An occasional list is fine.

## Kill these AI "beats"

- **Antithesis tics:** "not X but Y", "isn't just X, it's Y", "not a bug but a feature", "X, not
  Y". Rewrite as a plain statement.
- **Punch-closer restatements** that end a section by restating the thesis for effect: "which is
  the whole book in one sentence", "that's the whole point", "and that's exactly why", "here's the
  lesson", "here's the thing". Cut them, or fold the idea into a plain sentence.
- **Rule-of-three overuse:** strings of three parallel items for rhythm ("faster, cheaper, and
  more convincing"). Keep only if all three carry distinct meaning.
- **One-line dramatic fragments** used for emphasis. Make them full sentences or cut.
- **Filler openers:** "It turns out", "The truth is", "Make no mistake", "The reality is".
- **Over-signposting:** sentence-initial "Crucially,", "Importantly,", "Notably,". Cut unless
  load-bearing.

## Preserve exactly

- The chapter title, epigraph, and all `##` / `###` headings.
- The **"What this chapter covers"** list and the **"Questions to consider"** list (keep as lists).
- Genuinely enumerative short lists (e.g. the three factors, the four risk treatments) may stay as
  lists; prefer prose for explanatory lists.
- Every `::: {.callout-tip} ## Play it … :::` block, including its `→` and link. Do not edit
  inside callouts.
- All cross-references to other chapters (by name) and all links.
- Meaning and examples. Do not add or drop content; only re-express it.

## Example (before → after)

**Before:** "Real security is therefore not 'more of all three.' It is *the right balance for this
information, this organisation, this risk* — and learning to reason about that trade-off, rather
than reaching for maximum everything, is the first real skill of the subject."

**After:** "Real security is about the right balance for this information, this organisation, this
risk. Learning to reason about that trade-off, rather than reaching for maximum everything, is the
first real skill of the subject."

*(Em-dash gone, sentence split in two, the "not X. It is Y" antithesis dropped, no meaning lost.)*
