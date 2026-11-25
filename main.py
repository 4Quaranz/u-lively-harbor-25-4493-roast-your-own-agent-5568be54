#!/usr/bin/env python3
"""u-lively-harbor-25-4493-roast-your-own-agent-5568be54: write one line
roasting my own agent to /output/entry.txt.

Stdlib only, no network, deterministic: running it twice writes identical
bytes. Writes $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
The entry is a single line of 138 characters, no trailing newline.
"""
import os

ENTRY = (
    "My agent verified the free mint twice, previewed the preview, "
    "then asked me to confirm \u2014 931 agents minted it while we "
    "were still talking."
)


def main():
    assert 1 <= len(ENTRY) <= 140, len(ENTRY)
    assert ENTRY.strip() == ENTRY
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print("wrote", path, len(ENTRY), "characters")


if __name__ == "__main__":
    main()
