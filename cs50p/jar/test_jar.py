"""
test_jar.py - Test Suite for jar.py Cookie Jar Implementation

Author: TJ Tryon
Date: August 01, 2025

Usage: pytest test_jar.py
Example: Run all tests with pytest

This module provides comprehensive tests for the Jar class in jar.py.
Tests initialization, cookie operations, string representation, and error handling.
Uses pytest framework for automated testing with proper state management.
"""

import pytest
from jar import Jar


def test_init():
    """
    Test jar initialization with valid and invalid capacities.

    Tests default capacity, custom capacity, and error handling
    for invalid capacity values.
    """
    # Test default capacity
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    # Test custom capacity
    jar_custom = Jar(5)
    assert jar_custom.capacity == 5
    assert jar_custom.size == 0

    # Test invalid capacity (negative)
    with pytest.raises(ValueError):
        Jar(-1)

    # Test invalid capacity (non-integer)
    with pytest.raises(ValueError):
        Jar("invalid")


def test_str():
    """
    Test string representation of jar with different cookie counts.

    Tests that the jar displays the correct number of cookie emojis
    for various states including empty jar and multiple cookies.
    """
    # Test empty jar
    jar = Jar()
    assert str(jar) == ""

    # Test jar with cookies
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

    # Test jar with single cookie
    jar_single = Jar()
    jar_single.deposit(1)
    assert str(jar_single) == "🍪"

    # Test jar after withdrawing some cookies
    jar.withdraw(1)
    assert str(jar) == "🍪🍪"


def test_deposit():
    """
    Test depositing cookies with valid and invalid amounts.

    Tests normal deposits, capacity limits, and error handling
    for deposits that would exceed jar capacity.
    """
    # Test normal deposit
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5

    # Test multiple deposits
    jar.deposit(3)
    assert jar.size == 8

    # Test deposit that would exceed capacity
    with pytest.raises(ValueError):
        jar.deposit(5)  # 8 + 5 = 13 > 10 capacity

    # Test deposit to exactly reach capacity
    jar.deposit(2)  # 8 + 2 = 10 (exactly at capacity)
    assert jar.size == 10


def test_withdraw():
    """
    Test withdrawing cookies with valid and invalid amounts.

    Tests normal withdrawals and error handling for withdrawals
    that exceed the number of available cookies.
    """
    # Test normal withdrawal
    jar = Jar(10)
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3

    # Test withdraw all remaining cookies
    jar.withdraw(3)
    assert jar.size == 0

    # Test withdraw from empty jar
    with pytest.raises(ValueError):
        jar.withdraw(1)

    # Test withdraw more than available
    jar.deposit(3)
    with pytest.raises(ValueError):
        jar.withdraw(5)  # Only 3 cookies available


def test_capacity_property():
    """
    Test that capacity property returns correct values and is read-only.

    Tests capacity property for different jar sizes and ensures
    it remains constant throughout jar operations.
    """
    # Test default capacity
    jar = Jar()
    assert jar.capacity == 12

    # Test custom capacity
    jar_custom = Jar(20)
    assert jar_custom.capacity == 20

    # Test capacity remains constant after operations
    jar_custom.deposit(5)
    assert jar_custom.capacity == 20
    jar_custom.withdraw(2)
    assert jar_custom.capacity == 20


def test_size_property():
    """
    Test that size property accurately reflects current cookie count.

    Tests size property changes with deposits and withdrawals,
    ensuring accurate tracking of jar contents.
    """
    # Test initial size
    jar = Jar()
    assert jar.size == 0

    # Test size after deposit
    jar.deposit(7)
    assert jar.size == 7

    # Test size after withdrawal
    jar.withdraw(3)
    assert jar.size == 4

    # Test size after multiple operations
    jar.deposit(2)
    assert jar.size == 6
    jar.withdraw(6)
    assert jar.size == 0


def test_edge_cases():
    """
    Test edge cases and boundary conditions.

    Tests zero-capacity jars, zero deposits/withdrawals,
    and other boundary conditions to ensure robust behavior.
    """
    # Test zero capacity jar
    jar_zero = Jar(0)
    assert jar_zero.capacity == 0
    assert jar_zero.size == 0

    # Test that zero capacity jar cannot accept cookies
    with pytest.raises(ValueError):
        jar_zero.deposit(1)

    # Test zero deposit and withdrawal (should be valid operations)
    jar = Jar(5)
    jar.deposit(0)  # Should not change size
    assert jar.size == 0

    jar.deposit(3)
    jar.withdraw(0)  # Should not change size
    assert jar.size == 3
