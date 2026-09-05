# visual-options

A Claude Code plugin that stops Claude from picking a visual direction on your behalf. At any
visual fork in UI work, it publishes a private artifact rendering three or four real candidates
on your actual content, then asks you to choose.

A design decision described in prose is a guess for both sides. Rendered side by side on the
real thing, it takes one click.

## How it works

1. A `UserPromptSubmit` hook injects one standing instruction per session: at a visual fork, run
   `/visual-options` first, and say in one clause when you skip it. It re-arms after context
   compaction, carries no patterns and no classifier, and fails open.
2. The `visual-options` skill is the procedure. Claude names the fork, picks three or four
   defensible candidates, renders them in one page under an identical frame, and publishes it.
3. Every candidate uses your real copy, your real numbers, your real labels. No lorem, no
   placeholder data, and the project's existing tokens for everything not under decision.
4. Claude then asks with `AskUserQuestion`, one option per candidate, the artifact link in the
   question text.

## What it fires on

Typefaces, palettes, layout, component and chart styles, spacing systems, icon sets, rendering
idioms, empty states. Anything where "how should this look" has more than one defensible answer.

It stays quiet when a design file or an existing design system already settles the choice, when
you pinned the direction in words, or when the change is a one-line tweak.

## Install

```
/plugin marketplace add lucasmsa/claude-visual-options
/plugin install visual-options@lucasmsa-visual-options
```

Or drop `skills/visual-options` into `~/.claude/skills/` to use the skill without the hook.

## Licence

MIT
