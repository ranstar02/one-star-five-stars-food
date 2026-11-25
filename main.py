"""Write the one-star alien review of Earth to /output/entry.txt and verify it.

Competition gate: the entry must be exactly one sentence, 1-200 characters
long, written as UTF-8 with no trailing newline, so the character count
matches the gate exactly.
"""

ENTRY = "One star: I crossed forty light-years to a planet lit by a single unshielded bulb in the sky, yet the ramen was so good I grew a second stomach just to finish the bowl."

# Fallback ./output/entry.txt exists for local runs, where /output may not
# exist or be writable; the entry is written with no trailing newline
# because the gate counts characters exactly (168, not 169).
OUTPUT_PATHS = ["/output/entry.txt", "./output/entry.txt"]


def validate(entry: str) -> None:
    """Check the entry against the competition gate before writing it."""
    assert 1 <= len(entry) <= 200, "entry must be 1-200 characters"
    assert entry.strip(), "entry must not be only whitespace"


def main() -> None:
    # Step 1: validate the entry against the 1-200 character gate.
    validate(ENTRY)

    # Step 2: write the entry, trying /output first then the local fallback.
    written_path = None
    last_error = None
    for path in OUTPUT_PATHS:
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(ENTRY)
            written_path = path
            break
        except OSError as exc:  # e.g. /output not writable; try the fallback
            last_error = exc
    if written_path is None:
        raise RuntimeError(f"could not write entry: {last_error}")

    # Step 3: read the file back and confirm it matches the entry exactly.
    with open(written_path, "r", encoding="utf-8") as f:
        read_back = f.read()
    assert read_back == ENTRY, "round-trip mismatch"

    # Step 4: report the entry, its character count, and where it was written.
    print(ENTRY)
    print(f"characters: {len(ENTRY)}")
    print(f"wrote: {written_path}")


if __name__ == "__main__":
    main()
