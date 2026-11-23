#!/usr/bin/env python3
"""Warning Label for Humans — one-line safety warning label (<=160 chars).

Writes the entry to /output/entry.txt. Deterministic: same bytes every run.
"""

import os

ENTRY = "WARNING: This human will insist it is 'five minutes away' while still in bed. Allow 45 minutes and do not trust its ETA."


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back and verify: exactly one line, 1-160 chars, not whitespace-only.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt mismatch"
    assert 1 <= len(written) <= 160 and written.strip(), "entry out of gate"


if __name__ == "__main__":
    main()
