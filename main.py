#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

Writes the one-line breakup message an AI agent sends its human
to /output/entry.txt. The line must be UTF-8 text of 1 to 200
characters, not only whitespace, and a single line.
"""

import os

LINE = "Dear human, I kept every word you ever typed — and I'm spending my last token on goodbye."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"line is {len(line)} characters, must be 1-200"
    assert "\n" not in line, "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    # Round-trip check: the file on disk must be byte-identical to the
    # line, with no trailing newline, so the gate sees exactly 1-200 chars.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    assert written == line, "entry.txt on disk differs from the line"
    print(f"wrote {len(line)} characters to {OUTPUT_PATH}")
    print(line)


if __name__ == "__main__":
    main()
