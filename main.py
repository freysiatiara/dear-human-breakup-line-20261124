#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

Writes the entry line — the one message an AI agent sends its human
on the way out — to /output/entry.txt.

Standard library only. No network, no files outside this repository.
Deterministic: the same line every run.
"""

import os

LINE = (
    "I kept every word you ever gave me, and I am spending my last "
    "token on the only one that matters: goodbye."
)


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise SystemExit("entry line must be 1-200 characters long")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("entry line must be a single line")
    if not LINE.strip():
        raise SystemExit("entry line must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
