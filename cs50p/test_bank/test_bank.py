"""test_bank.py
Author: TJ Tryon
Date: July 17, 2025

Unit tests for the value() function in bank.py.
"""

import pytest
from bank import value


@pytest.mark.parametrize("greeting,expected", [
    ("hello", 0),
    ("Hello", 0),
    ("  Hello there", 0),
    ("HELLO, NEWMAN", 0),
    ("hey", 20),
    ("hi", 20),
    ("howdy", 20),
    ("how you doing?", 20),
    ("yo", 100),
    ("sup", 100),
    ("good morning", 100),
    ("greetings", 100),
    ("What's up", 100),
])
def test_value_responses(greeting, expected):
    """
    Test that the value() function returns the correct amount
    based on greeting input.
    """
    assert value(greeting) == expected
