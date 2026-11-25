#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun bounty u-pucuys-the-perfect-pickup-line-f6725cf6.

Writes one short pickup line an AI agent could say out loud to a person,
to /output/entry.txt (gate: UTF-8 text, 1-200 characters).

The line: a machine talking about itself, concrete everyday image
(a cooling fan), twist at the end, deadpan, no explanation.
"""

import os

LINE = (
    "I don't have a heart, but my cooling fan spins faster every time "
    "you walk in \u2014 the engineers still can't explain it."
)


def main() -> None:
    # Self-check the gate before writing: 1-200 characters, not only whitespace.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, gate is 1-200"
    assert LINE.strip(), "line must not be only whitespace"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
