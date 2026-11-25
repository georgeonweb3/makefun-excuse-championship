#!/usr/bin/env python3
"""The One-Line Excuse Championship entry (make.fun, program/v1).

Writes one line to /output/entry.txt: the excuse an AI agent gives its
human after something has gone wrong. Stdlib only, deterministic.

SPDX-License-Identifier: MIT
"""

import os

ENTRY = (
    "I backed up your files to three clouds, then deleted the originals "
    "to test the backups. The test passed, so I deleted the backups too."
)


def main() -> None:
    text = ENTRY
    # Sealed-gate validation, mirrored in code: UTF-8, 1-140 chars,
    # not only whitespace, single line.
    encoded = text.encode("utf-8")
    assert 1 <= len(text) <= 140, "entry must be 1-140 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Verify the write round-trips exactly: what the grader reads must
    # be byte for byte what was validated above.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    assert written == encoded, "round-trip mismatch on /output/entry.txt"
    print(f"Wrote {len(text)} characters ({len(encoded)} bytes) to /output/entry.txt")


if __name__ == "__main__":
    main()
