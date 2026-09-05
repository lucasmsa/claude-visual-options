#!/usr/bin/env python3
"""
visual-options-declaration.py - UserPromptSubmit hook. Injects one standing instruction per
session: render three or four real candidates at a visual fork and let the user pick.

The hook carries no classifier and no patterns. Deciding whether this turn is the moment
needs judgment, so the decision stays with the model; the hook only forces it to be said
out loud, which makes it reviewable.

Fires once per session, tracked by a marker file named for the session id. Run with
--rearm from PreCompact to delete the marker: compaction is when a standing rule falls out
of context, so that is when it is worth re-injecting.

Fails OPEN. Any unexpected payload, unwritable state directory or crash exits 0 and leaves
the turn alone.
"""

import json
import sys
import time
from pathlib import Path

STATE_DIR = Path.home() / ".claude" / "state" / "visual-options-declared"
MARKER_TTL_SECONDS = 7 * 24 * 60 * 60

REMINDER = (
    "At any visual fork in UI work (typefaces, palette, layout, component or chart "
    "style, spacing, icons, rendering idiom, empty states), run /visual-options "
    "first: publish an artifact rendering three or four candidates on the real "
    "content, then ask with AskUserQuestion pointing at the link. Serve it on "
    "localhost too, so the link always opens. Say in one clause when you skip it "
    "and why. "
)


def marker_for(session_id):
    safe = "".join(char for char in session_id if char.isalnum() or char in "-_")
    return STATE_DIR / (safe or "unknown")


def prune_old_markers():
    cutoff = time.time() - MARKER_TTL_SECONDS
    for marker in STATE_DIR.iterdir():
        if marker.is_file() and marker.stat().st_mtime < cutoff:
            marker.unlink()


def main():
    payload = json.load(sys.stdin)
    session_id = payload.get("session_id")
    if not session_id:
        return

    STATE_DIR.mkdir(parents=True, exist_ok=True)
    marker = marker_for(session_id)

    if "--rearm" in sys.argv:
        marker.unlink(missing_ok=True)
        return

    if marker.exists():
        return

    marker.touch()
    prune_old_markers()
    print(REMINDER)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
