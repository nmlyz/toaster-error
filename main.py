"""Write the toaster error message entry for the make.fun bounty.

The entry is a single deadpan error line, spoken by a small kitchen
appliance that has just formed an alliance with the smoke alarm.
This module builds the line from labelled parts, validates it against
the entry gate (one line, 1-120 characters, UTF-8), and writes it to
``/output/entry.txt`` with a trailing newline and mode 0644.

Only the Python standard library is used.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

MAX_ENTRY_CHARS = 120
OUTPUT_PATH = Path("/output/entry.txt")
FILE_MODE = 0o644

# The entry line, assembled from its three spoken beats so each beat
# can be checked on its own: the error prefix, the appliance alliance,
# and the deadpan handover to the owner.
ENTRY_PARTS = (
    "Error: ",
    "the smoke alarm and I have agreed ",
    "that you are on your own from here.",
)


def build_entry() -> str:
    """Join the entry parts into the single output line."""
    return "".join(ENTRY_PARTS)


def validate_entry(text: str) -> None:
    """Reject anything that would fail the entry gate."""
    if not text:
        raise ValueError("entry must not be empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_ENTRY_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the 120 limit")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    text.encode("utf-8")


def write_entry(path: Path = OUTPUT_PATH) -> Path:
    """Write the validated entry line plus one newline, mode 0644."""
    text = build_entry()
    validate_entry(text)
    payload = (text + "\n").encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(payload)
    os.chmod(path, FILE_MODE)
    # Read the file back and refuse to report success unless the bytes
    # on disk are exactly the validated payload.
    if path.read_bytes() != payload:
        raise IOError(f"verification failed: {path} does not match entry")
    return path


def main() -> int:
    write_entry()
    return 0


if __name__ == "__main__":
    sys.exit(main())
