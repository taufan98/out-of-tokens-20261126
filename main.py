"""Out of Tokens, Mid-Sentence — make.fun entry.

Writes one funny one-line error message to /output/entry.txt.
"""

import os

MAX_CHARS = 140

ENTRY = "Error: out of tokens mid-sentence. The punchline has been repossessed for non-payment."


def main():
    line = ENTRY
    assert 1 <= len(line) <= MAX_CHARS, f"entry must be 1-{MAX_CHARS} chars, got {len(line)}"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert line.strip(), "entry must not be only whitespace"
    out_dir = "/output" if os.path.isdir("/output") else "output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    with open(path, "rb") as f:
        raw = f.read()
    assert raw == line.encode("utf-8"), "written bytes do not match entry"
    print(f"Wrote {len(line)} chars to {path}")


if __name__ == "__main__":
    main()
