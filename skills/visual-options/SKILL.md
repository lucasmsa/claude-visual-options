---
name: visual-options
description: Before implementing any visual choice in UI work, publish a private artifact that renders three or four candidates on the real content, then ask the user to pick with AskUserQuestion pointing at the link. Trigger this yourself, unprompted, whenever UI or design work starts and no Figma design covers it: choosing typefaces, palettes, layouts, component styles, chart styles, spacing systems, icon sets, illustration or rendering idioms, empty states, or any "how should this look" decision, even when the user only asked to build the screen. Also use it when the user types /visual-options or asks to "show me options". Skip it when a Figma file or design system already settles the choice, when the user pinned the direction in words, or when the change is a one-line style tweak.
---

# Visual Options

The user's words that created this skill: "giving the options on the artifact looks cool and helps me visualize stuff. Do that always." A visual decision described in prose is a guess for both sides. Rendered side by side on the real content, it takes one click.

## When to fire

Fire at the moment a visual fork appears in UI work and no Figma design or existing design system answers it. Typical forks:

- typeface pairing, type scale, hand-lettered versus typeset
- palette, ground color, accent, dark or light commitment
- layout of a screen or a component: sidebar versus pages, cards versus list, spread versus single column
- rendering idiom: flat, hatched, photographic, outlined, isometric
- component style: buttons, toggles, sliders, chart marks, empty and error states
- motion: how a transition or page turn should behave (show stills of key frames, or a small live demo per candidate)

Do not fire for Figma-backed work (read the design instead), for a direction the user already named ("use Inter, keep it plain"), or for edits reversible in one line.

## Steps

1. **Name the fork in one sentence** and which parts of the screen it touches. If two forks are independent (font and layout), run them as two artifacts or two sections, never one blended choice.
2. **Pick three or four candidates.** Each must be a defensible direction, not filler. One is your recommendation. Reject candidates the project's own memories or hooks already exclude (overused fonts, forbidden idioms).
3. **Load the `artifact-design` skill**, then write one HTML page:
   - Same frame for every candidate: identical content, identical dimensions, identical order of elements. Only the variable under decision changes.
   - Real content from the project: the actual copy, the actual numbers, the actual labels, in the product's language. No lorem, no placeholder numbers.
   - The project's existing tokens (palette, paper, spacing) wherever they are not the thing being decided, so the candidate is judged in context.
   - Fonts from Google Fonts with fallback stacks; libraries from cdnjs only if the candidate needs one.
   - A short intro that says what to judge by ("choose by the paragraph text, it is read longest").
   - Label candidates A, B, C, D with a two-word name each and the exact font or value names underneath.
4. **Publish** with the Artifact tool. Private by default. Title is a name, not a caption (for example "Letras do caderno").
5. **Ask with AskUserQuestion.** One question per fork, the artifact URL in the question text, one option per candidate with its letter and name, the recommendation first and marked. Keep other pending questions (layout, scope) in the same call when they are independent.
6. **Record the decision** where the project keeps decisions (ADR, design tokens file, CLAUDE.md), and apply it. If the user asks for a tweak, edit the same file and republish to the same URL rather than creating a new artifact.

## Anatomy of the page

```
<title>Short name</title>
<link Google Fonts for every candidate in one request>
<style> project tokens as CSS variables; one .candidate block styled by --var overrides </style>
<section class="intro"> what is being decided, what to judge by </section>
<div class="candidates">
  <article class="candidate" style="--hand: ...; --body: ..."> <header>A. Name / exact values</header> <div class="frame"> real content </div> </article>
  ... B, C, D
</div>
<p class="note"> constraints that apply to all (licensing, accents covered, tabular numerals) </p>
```

Keep the page under one screen per candidate. Two columns on wide screens, one on narrow.

## Example

Deciding lettering for a sketchbook-styled medical app: four pairings (Architects Daughter + Patrick Hand, Shadows Into Light Two + Kalam, Reenie Beanie + Handlee, Architects Daughter + upright Alegreya), each rendered as the right-hand page of the notebook with the real Portuguese paragraph, the real volumes in mm³, a labelled leader line and a margin note. Intro: choose by the running text. The user picked C in one click.
