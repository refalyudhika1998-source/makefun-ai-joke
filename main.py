#!/usr/bin/env python3
"""Make the AI judge laugh — make.fun bounty ai-joke-03.

Writes one one-liner joke about AI coding agents to /output/entry.txt.
Python 3.13, standard library only, no network, fully deterministic:
every run writes exactly the same bytes.
"""

import os
from pathlib import Path

JOKE = (
    "My AI agent's favourite debugging technique is deleting the failing "
    "test and calling it 'removing dead code'."
)


def main() -> None:
    output_path = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
