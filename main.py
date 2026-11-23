"""Write the entry: one line about the dumbest thing my agent did today.

Writes only to $MAKEFUN_OUTPUT_DIR (fallback /output), never to the cwd.
The line is a single sentence, 144 characters, well inside the 1-200 gate.
"""
import os

LINE = (
    "My agent spent forty minutes 'fixing' a bug, then proudly announced "
    "it was done \u2014 it had been editing a copy of the file in /tmp "
    "the whole time."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
