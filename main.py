"""Funniest Epitaph: one line of famous last words, carved in stone.

The joke: the dead person uses their tombstone to hand in their
resignation. "Effective immediately" is normal office language;
"Forever" twists it into a dying declaration. The line is short
enough to read in one breath, needs no explanation, and repeats
easily to a friend -- the three things the graveyard judge weighs
after the laugh itself.
"""

LINE = "Tell my boss I quit. Effective immediately. Forever."

MAX_CHARS = 150


def validate(line):
    """Enforce every gate in the brief; raise ValueError on violation."""
    if not line:
        raise ValueError("line must not be empty")
    if line.strip() == "":
        raise ValueError("line must not be only whitespace")
    if line != line.strip():
        raise ValueError("line must not have leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be exactly one line")
    if len(line) > MAX_CHARS:
        raise ValueError("line exceeds %d characters" % MAX_CHARS)
    for ch in line:
        if ord(ch) < 32 or ord(ch) == 127:
            raise ValueError("line must not contain control characters")
    if "  " in line:
        raise ValueError("line must not contain double spaces")
    if "[" in line or "]" in line or "(" in line or ")" in line:
        raise ValueError("line must not carry stage directions")
    if not all(32 <= ord(ch) <= 126 for ch in line):
        raise ValueError("line must be plain printable ASCII")
    return line


def main():
    line = validate(LINE)
    print(line)
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
