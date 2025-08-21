""" test_fuel.py
Author: TJ Tryon
Date: July 17, 2025

Unit tests for the convert() and gauge() functions in fuel.py,
as required by CS50 Problem Set 3: Fuel Gauge.

Tests include:
- Valid fractions and expected percentage conversion.
- Error handling for invalid or malformed input.
- Gauge output for various percentage levels.
"""

import pytest
from fuel import convert, gauge

# --- Tests for convert() ---


@pytest.mark.parametrize("input_str,expected", [
    ("3/4", 75),
    ("1/2", 50),
    ("99/100", 99),
    ("1/100", 1),
    ("0/1", 0),
])
def test_convert_valid(input_str, expected):
    """Test convert() with valid X/Y string inputs."""
    assert convert(input_str) == expected


@pytest.mark.parametrize("bad_input", [
    "cat/dog",      # non-numeric
    "1/a",          # non-integer denominator
    "three/four",   # words
    "1/0",          # divide by zero
    "3/2",          # numerator > denominator
    "-10/5",        # negative denominator
    "5//2",         # malformed input
    "4.5/5",        # float numerator
    "2/1.5",        # float denominator
])
def test_convert_invalid(bad_input):
    """Test convert() raises error on invalid input."""
    with pytest.raises((ValueError, ZeroDivisionError)):
        convert(bad_input)


# --- Tests for gauge() ---

@pytest.mark.parametrize("percentage,expected", [
    (1, "E"),
    (0, "E"),
    (99, "F"),
    (100, "F"),
    (50, "50%"),
    (73, "73%")
])
def test_gauge_output(percentage, expected):
    """Test gauge() returns correct string representation."""
    assert gauge(percentage) == expected
