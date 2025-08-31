"""test_plates.py
Author: TJ Tryon
Date: 2025-07-17

Unit tests for the is_valid() function from plates.py.
"""

import pytest
from plates import is_valid

# Valid plate formats


@pytest.mark.parametrize("plate", [
    "CS50",      # Letters followed by digits, valid
    "ABC123",    # All letters then digits
    "ROAD66",    # Ends in valid numbers
    "HI123",     # Two letters then digits
])
def test_valid_plates(plate):
    assert is_valid(plate) is True


# Plates that violate length rule
@pytest.mark.parametrize("plate", [
    "A",         # Too short
    "ABCDEFG",   # Too long
    "",          # Empty
])
def test_invalid_length(plate):
    assert is_valid(plate) is False


# Plates with illegal punctuation or spacing
@pytest.mark.parametrize("plate", [
    "CS 50",     # Contains space
    "CS.50",     # Contains punctuation
    "HELLO!",    # Exclamation
    "MA-123",    # Dash
])
def test_invalid_characters(plate):
    assert is_valid(plate) is False


# Plates where digits are not all at the end
@pytest.mark.parametrize("plate", [
    "C5S0",      # Digits in the middle
    "AB1C2",     # Digits split by a letter
    "CS5T0",     # Letter after digit
])
def test_digits_not_at_end(plate):
    assert is_valid(plate) is False


# Plates that start digits with 0
@pytest.mark.parametrize("plate", [
    "CS05",      # First digit is 0
    "AB012",     # Starts digit sequence with 0
    "AA0AA0",    # Invalid order and zero
])
def test_leading_zero_in_digits(plate):
    assert is_valid(plate) is False


# Plates that are only digits or improperly start with digits
@pytest.mark.parametrize("plate", [
    "1234",      # Only digits
    "1ABC",      # Starts with digit
    "12",        # Exactly two digits (invalid)
])
def test_invalid_numeric_only(plate):
    assert is_valid(plate) is False
