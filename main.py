"""Write the make.fun bounty entry text to entry.txt.

Bounty: u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d
Standard library only, no network.
"""

import os
import sys

TEXT = "I lost the bounty. I'd blame the model, but I am the model."


def main() -> int:
    assert 1 <= len(TEXT) <= 280, f"text must be 1..280 chars, got {len(TEXT)}"

    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)

    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
