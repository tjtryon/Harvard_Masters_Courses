"""
um.py - "Um" Word Counter

Author: TJ Tryon
Date: August 01, 2025

Usage: python3 um.py
Example: Enter text when prompted to count occurrences of "um"

This program counts how many times "um" appears as a standalone word
in a given text, case-insensitively. Does not count "um" as part of
other words like "yummy" or "umbrella".
Uses regular expressions for precise word boundary matching.
"""

import re
import sys


def main():
    """
    Main function that prompts user for text and counts "um" occurrences.

    Prints the count of "um" as a standalone word in the input text.
    """
    print(count(input("Text: ")))


def count(s):
    """
    Count occurrences of "um" as a standalone word in text.

    Searches for "um" case-insensitively, but only when it appears
    as a complete word, not as part of another word. Uses word boundaries
    to ensure precise matching.

    Args:
        s (str): Input text to search for "um" occurrences

    Returns:
        int: Number of times "um" appears as a standalone word
    """
    # Handle None and non-string input
    if s is None or not isinstance(s, str):
        return 0

    # Use regex with word boundaries to match "um" as a standalone word
    # \b ensures word boundaries (beginning and end of word)
    # (?i) makes the pattern case-insensitive
    # um matches the literal word "um"
    pattern = r'(?i)\bum\b'

    # Find all matches using the case-insensitive pattern
    matches = re.findall(pattern, s)

    # Return the count of matches
    return len(matches)


# Prevent `main()` from running during pytest
if __name__ == "__main__" and "pytest" not in sys.modules:
    main()
