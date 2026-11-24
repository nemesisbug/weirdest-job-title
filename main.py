#!/usr/bin/env python3
"""Weirdest Job Title entry.

Writes one job title to /output/entry.txt: the strangest believable
job title we could think of. Standard library only, no network,
no input files, no secrets.
"""

import os

TITLE = "Professional Apology Writer for Cats"

# The gate counts every character in the file, so the title itself must
# stay inside 1-60 characters; this one is 36.


def main() -> None:
    if not 1 <= len(TITLE) <= 60:
        raise SystemExit(f"title is {len(TITLE)} chars, gate needs 1-60")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TITLE)


if __name__ == "__main__":
    main()
