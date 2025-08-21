"""
test_numb3rs.py - Test Suite for IPv4 Address Validation

Author: TJ Tryon
Date: August 01, 2025

Usage: pytest test_numb3rs.py
Example: Run all tests to validate numb3rs.py functionality

This test suite validates the IPv4 address validation functionality in numb3rs.py.
Tests cover valid addresses, invalid ranges, leading zeros, wrong number of parts,
non-numeric content, empty parts, whitespace handling, and edge cases.
Designed to catch common implementation bugs.
"""

from numb3rs import validate


def test_valid_addresses():
    """
    Test valid IPv4 addresses that should return True.

    Tests standard valid formats including boundary values
    and common network addresses.
    """
    assert validate("192.168.1.1") == True      # typical local network address
    assert validate("0.0.0.0") == True          # minimum valid address
    assert validate("255.255.255.255") == True  # maximum valid address
    assert validate("127.0.0.1") == True        # localhost address
    assert validate("8.8.8.8") == True          # public DNS address


def test_invalid_addresses():
    """
    Test invalid IPv4 addresses with out-of-range octets.

    Tests addresses where one or more octets exceed the valid
    range of 0-255 for IPv4 addresses.
    """
    assert validate("256.100.100.100") == False  # first octet too high
    assert validate("192.168.1.256") == False    # last octet too high
    assert validate("123.456.78.90") == False    # second octet too high
    assert validate("192.168.1.-1") == False     # negative number invalid
    assert validate("192.168.01.1") == False     # leading zero invalid


def test_all_octets_range_validation():
    """
    Test that ALL octets are properly validated for 0-255 range.

    This catches bugs where only the first octet is checked.
    Tests each position (1st, 2nd, 3rd, 4th) with invalid values.
    """
    # Test 2nd octet out of range (catches "only first byte" bug)
    assert validate("100.256.50.50") == False    # 2nd octet = 256
    assert validate("100.300.50.50") == False    # 2nd octet = 300
    assert validate("100.999.50.50") == False    # 2nd octet = 999

    # Test 3rd octet out of range (catches "only first byte" bug)
    assert validate("100.100.256.50") == False   # 3rd octet = 256
    assert validate("100.100.300.50") == False   # 3rd octet = 300
    assert validate("100.100.999.50") == False   # 3rd octet = 999

    # Test 4th octet out of range (catches "only first byte" bug)
    assert validate("100.100.100.256") == False  # 4th octet = 256
    assert validate("100.100.100.300") == False  # 4th octet = 300
    assert validate("100.100.100.999") == False  # 4th octet = 999


def test_exactly_four_parts():
    """
    Test that exactly 4 parts are required.

    This catches bugs that accept 5-byte or other incorrect formats.
    Tests various combinations with wrong number of parts.
    """
    # Too few parts
    assert validate("192.168.1") == False        # only 3 parts
    assert validate("192.168") == False          # only 2 parts
    assert validate("192") == False              # only 1 part
    assert validate("1.2.3") == False            # only 3 parts
    assert validate("1.2") == False              # only 2 parts
    assert validate("1") == False                # only 1 part

    # Too many parts (catches "five-byte" bug)
    assert validate("192.168.1.1.1") == False    # 5 parts
    assert validate("1.2.3.4.5") == False        # 5 parts
    assert validate("1.2.3.4.5.6") == False      # 6 parts
    assert validate("192.168.1.1.1.1") == False  # 6 parts
    assert validate("10.10.10.10.10") == False   # 5 parts
    assert validate("255.255.255.255.255") == False  # 5 parts



def test_boundary_values():
    """
    Test boundary values for IPv4 octet ranges.

    Tests the minimum (0) and maximum (255) valid values,
    as well as values just outside the valid range for each position.
    """
    # Valid boundary values
    assert validate("0.0.0.0") == True       # minimum valid values
    assert validate("255.255.255.255") == True  # maximum valid values

    # Invalid boundary values in each position
    assert validate("300.0.0.0") == False    # 1st octet well above maximum
    assert validate("0.300.0.0") == False    # 2nd octet well above maximum
    assert validate("0.0.300.0") == False    # 3rd octet well above maximum
    assert validate("0.0.0.300") == False    # 4th octet well above maximum
