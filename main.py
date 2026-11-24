"""The funniest one-line warning label for a time machine, 120 characters or fewer.

The program writes exactly that line and nothing else to /output/entry.txt.
"""

import os

TEXT = "WARNING: Do not step on butterflies, do not meet yourself, and never invest in anything your future self regrets."


def main():
    assert 1 <= len(TEXT) <= 120, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
