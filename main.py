#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review — account B (Slothana).

Writes a single original line — an alien tourist's review of planet Earth —
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Deterministic: no network, no model calls, no randomness, no provider keys.
The line was authored fresh in-session and revised once (v1 -> v2) to fix the
subject of "acts surprised" (the locals, not the planet) and tighten the flow.
"""

import os

ENTRY = (
    "The locals keep tiny dinosaurs as pets, then act surprised when they "
    "scream at dawn. Adorable chaos \u2014 would be woken again. Four stars."
)

# The gate (RULES.txt): entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space. Fail loudly here rather than shipping an invalid line.
assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, gate needs 1-200"
assert ENTRY.strip(), "entry must not be only white space"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
