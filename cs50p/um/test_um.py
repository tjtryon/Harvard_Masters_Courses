"""
test_um.py - Test Suite for um.py Word Counter

Author: TJ Tryon
Date: August 01, 2025

Usage: pytest test_um.py
Example: Run all tests with pytest

This module provides comprehensive tests for the count function in um.py.
Tests word boundary detection, case sensitivity, edge cases, and invalid inputs.
Uses pytest framework for automated testing.
"""

import pytest
from um import count


def test_standalone_um():
    """
    Test counting "um" when it appears as a standalone word.

    Tests basic functionality with "um" appearing as complete words
    separated by punctuation and whitespace.
    """
    # Test "um" with punctuation boundaries - should be 1
    assert count("hello, um, world") == 1

    # Test "um" at word boundaries without requiring spaces - should be 1
    assert count("um.") == 1


def test_case_insensitive():
    """
    Test case-insensitive matching of "um".

    Tests that "um" is counted regardless of capitalization
    while maintaining word boundary requirements.
    """
    # Test uppercase - should be 1
    assert count("UM") == 1

    # Test mixed case in sentence - should be 1
    assert count("Um, yes") == 1


def test_no_substring_matches():
    """
    Test that "um" within other words is not counted.

    Tests that substrings containing "um" do not trigger false positives
    when "um" is not a standalone word.
    """
    # Test "um" as part of other words - should be 0
    assert count("yummy") == 0

    # Test "um" at start of word - should be 0
    assert count("umbrella") == 0
