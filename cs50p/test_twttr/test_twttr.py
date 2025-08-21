# test_twttr.py
"""
Author: TJ Tryon
Date: 2025-07-16

Unit tests for the shorten() function in twttr.py.
"""

import pytest
from twttr import shorten


@pytest.mark.parametrize("input_str,expected", [
    ("This is a test.", "Ths s  tst."),     # Normal sentence
    ("AEIOU aeiou", " "),                   # All vowels
    ("CS50 is cool!", "CS50 s cl!"),        # Mix with numbers and punctuation
    ("", ""),                               # Empty string
    ("Quick brown fox", "Qck brwn fx"),     # Mixed case
    ("   ", "   "),                         # Only spaces (Spaces stay)
])
def test_shorten_valid_cases(input_str, expected):
    """Test shorten() with various valid string inputs."""
    assert shorten(input_str) == expected
