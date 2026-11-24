#!/usr/bin/env python3
"""Write the office-jokes one-liner entry to /output/entry.txt."""
import os
import sys

JOKE = "I told HR my job was soul-crushing, so they scheduled a collaborative workshop to crush it more efficiently."
OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Abort if the entry violates the one-liner constraints."""
    if not isinstance(text, str) or not text:
        raise ValueError("joke must be a non-empty string")
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line (no newline characters)")
    if text != text.strip():
        raise ValueError("joke must not have leading or trailing whitespace")
    # Ensure the text round-trips cleanly as UTF-8.
    text.encode("utf-8")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"joke length {len(text)} outside 1-200 characters")


def main() -> int:
    try:
        validate(JOKE)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(JOKE)
    os.chmod(OUTPUT_PATH, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
