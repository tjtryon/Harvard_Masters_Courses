"""
test_seasons.py - Test Suite for seasons.py Age Calculator

Author: TJ Tryon
Date: August 01, 2025

Usage: pytest test_seasons.py
Example: Run all tests with pytest

This module provides comprehensive tests for the functions in seasons.py.
Tests date parsing, age calculation accuracy, and word conversion functionality.
Uses pytest framework for automated testing.
"""

import pytest
from datetime import date
from seasons import parse_date, calculate_minutes_since_birth, convert_to_words
import sys


def test_parse_date():
    """
    Test date parsing function for valid and invalid inputs.

    Tests that valid YYYY-MM-DD dates are parsed correctly and
    invalid formats trigger program exit via sys.exit().
    """
    # Test valid date parsing
    result = parse_date("1990-06-15")
    assert result == date(1990, 6, 15)

    # Test invalid date format triggers sys.exit
    with pytest.raises(SystemExit):
        parse_date("invalid-date")


def test_calculate_minutes_since_birth():
    """
    Test age calculation in minutes for different scenarios.

    Tests calculation accuracy with known date differences and
    verifies proper handling of leap years through date arithmetic.
    """
    # Test calculation with exactly 1 year (365 days)
    # From 2021-01-01 to 2022-01-01 = 365 days = 525,600 minutes
    birth_date = date(2021, 1, 1)

    import unittest.mock
    with unittest.mock.patch('seasons.date') as mock_date:
        mock_date.today.return_value = date(2022, 1, 1)
        mock_date.side_effect = lambda *args, **kw: date(*args, **kw)
        result = calculate_minutes_since_birth(birth_date)
        assert result == 525600  # Exactly one non-leap year in minutes

    # Test calculation with leap year included
    # From 2020-01-01 to 2021-01-01 = 366 days = 527,040 minutes (2020 is leap year)
    birth_date_leap = date(2020, 1, 1)
    with unittest.mock.patch('seasons.date') as mock_date:
        mock_date.today.return_value = date(2021, 1, 1)
        mock_date.side_effect = lambda *args, **kw: date(*args, **kw)
        result = calculate_minutes_since_birth(birth_date_leap)
        assert result == 527040  # One leap year in minutes
