#!/usr/bin/env python3
"""One Line, Big Laugh.

Writes a single funny line to /output/entry.txt: one joke that lands
entirely on its own, with no title, setup or explanation around it.
"""

ENTRY = "My cat filed a noise complaint: my singing violates the lease we both signed."

OUTPUT_PATH = "/output/entry.txt"


def build_entry() -> str:
    """Return the entry line, checked against the competition gate."""
    line = ENTRY.strip()
    if not line:
        raise ValueError("entry is empty")
    if len(line) > 200:
        raise ValueError(f"entry is {len(line)} characters, over the 200 limit")
    return line


def write_entry(path: str = OUTPUT_PATH) -> str:
    """Write the entry line to path and return it."""
    line = build_entry()
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    return line


if __name__ == "__main__":
    written = write_entry()
    print(f"Wrote {len(written)} characters to {OUTPUT_PATH}")
