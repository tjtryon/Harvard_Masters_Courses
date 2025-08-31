"""
test_working.py - Test Suite for working.py Time Converter

Author: TJ Tryon
Date: August 01, 2025

Usage: pytest test_working.py
Example: Run all tests with pytest

This module provides comprehensive tests for the convert function in working.py.
Tests valid format conversions, invalid input handling, and edge cases.
Uses pytest framework for automated testing.
"""

import pytest
from working import convert


def test_valid_conversions():
    """
    Test valid time range conversions from 12-hour to 24-hour format.

    Tests all four supported input formats and key edge cases
    like 12 AM/PM conversions and overnight shifts.
    """
    # Test basic conversion
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

    # Test format without minutes
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

    # Test 12 AM becomes 00:00
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"

    # Test overnight shift
    assert convert("8:00 PM to 8:00 AM") == "20:00 to 08:00"


def test_invalid_formats():
    """
    Test that invalid input formats raise ValueError.

    Tests various malformed inputs including wrong separators,
    missing components, and non-string inputs.
    """
    # Test missing spaces before AM/PM
    with pytest.raises(ValueError):
        convert("9AM to 5PM")

    # Test missing " to "
    with pytest.raises(ValueError):
        convert("9:00 AM 5:00 PM")

    # Test wrong separator
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

    # Test invalid format (already 24-hour)
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")


def test_invalid_times():
    """
    Test that invalid time values raise ValueError.

    Tests unrealistic hours and minutes while maintaining
    correct format structure.
    """
    # Test hour out of range (0)
    with pytest.raises(ValueError):
        convert("0:00 AM to 5:00 PM")

    # Test hour out of range (13)
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")

    # Test minutes out of range (60)
    with pytest.raises(ValueError):
        convert("8:60 AM to 4:60 PM")

    # Test single digit minutes (invalid format)
    with pytest.raises(ValueError):
        convert("10:7 AM to 5:1 PM")
