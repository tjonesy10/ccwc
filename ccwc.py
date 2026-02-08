import argparse
import os
import sys
from typing import Optional, Tuple


def count_from_bytes(data: bytes) -> Tuple[int, int, int, int]:
    """
    Returns: (lines, words, chars, bytes)
    - lines: number of '\n'
    - words: split on whitespace (like wc)
    - chars: decoded text length (best effort, utf-8 with replacement)
    - bytes: raw byte length
    """
    byte_count = len(data)
    line_count = data.count(b"\n")

    # Decode for word/char counting.
    # Using utf-8 with replacement keeps the program robust for "weird" bytes.
    text = data.decode("utf-8", errors="replace")

    # wc counts "words" as whitespace-separated tokens
    word_count = len(text.split())

    char_count = len(text)
    return line_count, word_count, char_count, byte_count


def read_input_bytes(filename: Optional[str]) -> Tuple[bytes, str]:
    """
    If filename is provided: read file as bytes.
    If not: read from stdin as bytes.
    Returns (data_bytes, label) where label is filename or empty string.
    """
    if filename:
        with open(filename, "rb") as f:
            return f.read(), filename

    # stdin (piped input)
    if hasattr(sys.stdin, "buffer"):
        return sys.stdin.buffer.read(), ""
    # fallback (rare)
    return sys.stdin.read().encode("utf-8", errors="replace"), ""


def main() -> int:
    parser = argparse.ArgumentParser(prog="ccwc", add_help=True)
    parser.add_argument("-c", action="store_true", help="print the byte counts")
    parser.add_argument("-l", action="store_true", help="print the newline counts")
    parser.add_argument("-w", action="store_true", help="print the word counts")
    parser.add_argument("-m", action="store_true", help="print the character counts")
    parser.add_argument("filename", nargs="?", help="file to read (optional; stdin if omitted)")
    args = parser.parse_args()

    data, label = read_input_bytes(args.filename)
    lines, words, chars, bytes_ = count_from_bytes(data)

    # Default mode: -l -w -c (like wc)
    no_flags = not (args.c or args.l or args.w or args.m)
    show_l = args.l or no_flags
    show_w = args.w or no_flags
    show_c = args.c or no_flags
    show_m = args.m

    parts = []
    if show_l:
        parts.append(f"{lines:7d}")
    if show_w:
        parts.append(f"{words:7d}")
    if show_c:
        parts.append(f"{bytes_:7d}")
    if show_m:
        parts.append(f"{chars:7d}")

    # Match wc style: counts then filename (if present)
    if label:
        print(" ".join(parts), label)
    else:
        print(" ".join(parts))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
