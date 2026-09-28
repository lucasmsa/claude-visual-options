---
name: visual-options
description: Before implementing any visual choice in UI work, publish a private artifact that renders three or four candidates on the real content, then ask the user to pick with AskUserQuestion pointing at the link. When the piece carries identity (logo, app icon, hero, illustration, drawing, lettering, mascot, animation), the choice also offers the user's own hand: they draw or animate it, they sketch and the agent finishes, or the agent drafts an editable file they retouch. Trigger this yourself, unprompted, whenever UI or design work starts and no Figma design covers it: choosing typefaces, palettes, layouts, component styles, chart styles, spacing systems, icon sets, illustration or rendering idioms, empty states, logos, heroes, motion, or any "how should this look" decision, even when the user only asked to build the screen. Also use it when the user types /visual-options or asks to "show me options". Skip it when a Figma file or design system already settles the choice, when the user pinned the direction in words, or when the change is a one-line style tweak.
---

# Visual Options

The user's words that created this skill: "giving the options on the artifact looks cool and helps me visualize stuff. Do that always." A visual decision described in prose is a guess for both sides. Rendered side by side on the real content, it takes one click.

The second rule, added later: "sometimes I'll also want to get my hand on a drawing, logo, design, animation." Generated candidates are one way to fill a slot. The user's own hand is another, and for the pieces that carry a project's identity it is often the one they want. Offer it every time such a piece comes up; never assume the answer.

## When to fire

Fire at the moment a visual fork appears in UI work and no Figma design or existing design system answers it. Typical forks:

- typeface pairing, type scale, hand-lettered versus typeset
- palette, ground color, accent, dark or light commitment
- layout of a screen or a component: sidebar versus pages, cards versus list, spread versus single column
- rendering idiom: flat, hatched, photographic, outlined, isometric
- component style: buttons, toggles, sliders, chart marks, empty and error states
- motion: how a transition or page turn should behave (show stills of key frames, or a small live demo per candidate)
- identity pieces: logo, wordmark, app icon, favicon, hero, illustration, spot drawing, mascot, lettering, a signature animation

Do not fire for Figma-backed work (read the design instead), for a direction the user already named ("use Inter, keep it plain"), or for edits reversible in one line.

## Identity pieces: whose hand

A piece is an identity piece when a visitor would remember it or when it would appear outside the app (store listing, tab, social card, README). Logos, app icons, heroes, illustrations and signature motion are identity pieces. Buttons, spacing and chart marks are not.

For an identity piece, the question is two-sided: which direction, and who makes it. The AskUserQuestion call carries both, as options of one question:

- **A to D, generated**: the rendered candidates, as usual.
- **You make it**: the user draws, letters or animates it. The artifact shows an empty slot at the exact size, in context, with the brief (see below).
- **You sketch, I finish**: the user sends a rough (paper photo, napkin, Excalidraw, a few strokes on a tablet); the agent turns it into the production asset while keeping the user's line.
- **I draft, you retouch**: the agent builds candidate X as an editable source (layered SVG, Figma frame, Excalidraw file, Rive or Lottie file, a keyframe table) and the user edits it by hand.

Recommend by the piece: a generated candidate for supporting illustration and empty states, the user's hand for a personal project's logo, icon or hero unless the project's memories say otherwise. State the recommendation in the option label, as with any other fork.

If the user picks a hand-made option, the fork is not closed, it is waiting on them. Say so in one line, record it as an open item where the project tracks work, and keep building everything that does not depend on the piece, with a placeholder that is visibly a placeholder (an outlined box with its name and size), never a generated stand-in that could ship by accident.

### The brief

Give the brief inline in chat and on the artifact, never only as a file. It contains:

- **Canvas**: exact size and aspect ratio, safe area, the smallest size it must still read at (a 16 px favicon, a 29 pt settings icon, a phone-width hero), and whether it sits on light, dark or both.
- **Accepted formats**, easiest first: a phone photo of paper, PNG, SVG, an Excalidraw or Figma link, a Procreate export, a Rive or Lottie file, a video of a flipbook. Say which the agent can finish from and what it loses (a photo gets traced, so fine hatching may thicken).
- **Drop point**: an exact path in the repo or the scratchpad, or "paste it in the chat". Images sent in chat are read without asking.
- **Constraints that already hold**: palette tokens, stroke weight of neighbouring icons, platform rules (iOS icons are full-bleed squares, the system applies the mask; macOS icons keep their own shape and shadow), licensing if it reuses anything.
- **A starter file** when it saves the user setup time: an SVG or PNG template with the canvas, safe area and smallest-size preview drawn in, or a Figma or Excalidraw frame at the right bounds. Put it at the drop point.

### When the piece arrives

1. Open it and look at it before anything else.
2. Finish only what the chosen option asked for. "You make it" means clean up and export: background removal, crop to canvas, trace to SVG if the target needs vectors, size variants. It does not mean redrawing, straightening wobble, or swapping their colours. "You sketch, I finish" allows more, but the user's composition and line character stay.
3. Render it in context on the same artifact (republish to the same URL), in every place it will appear and at the smallest size, on light and dark ground.
4. Ask one AskUserQuestion: ship as is, adjust (say what), or redo by hand.
5. Keep the original the user sent next to the processed asset in the repo, so a later pass can go back to the source.

For animation, the editable artifact is the timing, not a video: keyframes, durations and easing as data (a config object, a Rive state machine, a Lottie file, CSS or SwiftUI keyframes) so the user can retime it without the agent.

## Steps

1. **Name the fork in one sentence** and which parts of the screen it touches. If two forks are independent (font and layout), run them as two artifacts or two sections, never one blended choice. Say whether it is an identity piece.
2. **Pick three or four candidates.** Each must be a defensible direction, not filler. One is your recommendation. Reject candidates the project's own memories, ADRs or hooks already exclude (overused fonts, forbidden idioms, a project that decided to use system styling).
3. **Load the `artifact-design` skill**, then write one HTML page:
   - Same frame for every candidate: identical content, identical dimensions, identical order of elements. Only the variable under decision changes.
   - Real content from the project: the actual copy, the actual numbers, the actual labels, in the product's language. No lorem, no placeholder numbers.
   - The project's existing tokens (palette, paper, spacing) wherever they are not the thing being decided, so the candidate is judged in context.
   - For a native app, render in the platform's idiom (SF, system colours, the real container shapes) or use screenshots from a running preview. A web page wearing native clothing misjudges the result.
   - Fonts from Google Fonts with fallback stacks; libraries from cdnjs only if the candidate needs one.
   - A short intro that says what to judge by ("choose by the paragraph text, it is read longest"; "choose by the 29 pt size, it is where the icon lives most").
   - Label candidates A, B, C, D with a two-word name each and the exact font or value names underneath.
   - For an identity piece, add the hand-made slot as the last frame: empty at the exact size, the brief beside it.
4. **Publish** with the Artifact tool. Private by default. Title is a name, not a caption (for example "Letras do caderno"). Serve it on localhost too, so the link always opens.
5. **Ask with AskUserQuestion** (request_user_input_async in Codex). One question per fork, the artifact URL in the question text, one option per candidate with its letter and name, the recommendation first and marked. For an identity piece, the hand-made options sit in the same question; the question allows four options, so drop to three generated candidates or fold the hybrids into one "Your hand" option and ask which mode in a follow-up. Keep other pending questions (layout, scope) in the same call when they are independent.
6. **Record the decision** where the project keeps decisions (ADR, design tokens file, CLAUDE.md), including who made the piece and where the source file lives, and apply it. If the user asks for a tweak, edit the same file and republish to the same URL rather than creating a new artifact.

## Anatomy of the page

```
<title>Short name</title>
<link Google Fonts for every candidate in one request>
<style> project tokens as CSS variables; one .candidate block styled by --var overrides </style>
<section class="intro"> what is being decided, what to judge by </section>
<div class="candidates">
  <article class="candidate" style="--hand: ...; --body: ..."> <header>A. Name / exact values</header> <div class="frame"> real content </div> </article>
  ... B, C, D
  <article class="candidate slot"> <header>Your hand</header> <div class="frame"> empty slot at exact size </div> <aside> the brief </aside> </article>
</div>
<p class="note"> constraints that apply to all (licensing, accents covered, tabular numerals, smallest size) </p>
```

Keep the page under one screen per candidate. Two columns on wide screens, one on narrow.

## Examples

Deciding lettering for a sketchbook-styled medical app: four pairings (Architects Daughter + Patrick Hand, Shadows Into Light Two + Kalam, Reenie Beanie + Handlee, Architects Daughter + upright Alegreya), each rendered as the right-hand page of the notebook with the real Portuguese paragraph, the real volumes in mm³, a labelled leader line and a margin note. Intro: choose by the running text. The user picked C in one click.

Shape of an identity fork, for an app icon on a personal native app: three generated marks rendered at 1024, 180, 60 and 29 pt on a home screen and in Settings, light and dark, plus an empty 1024 slot with the brief (full-bleed square, no text, reads at 29 pt, drop at `design/incoming/icon.png`, paper photo accepted). Options: "Your hand (Recommended)", A, B, C. If the user draws it, the traced result goes back into the same frames on the same URL before anything ships.
