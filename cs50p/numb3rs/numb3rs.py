"""
numb3rs.py - IPv4 Address Validation Program

Author: TJ Tryon
Date: August 01, 2025

Usage: python3 numb3rs.py
Example: Enter an IPv4 address when prompted

This program validates whether a given string represents a valid IPv4 address.
IPv4 addresses consist of four numbers (0–255) separated by periods.
Uses regular expressions to precisely validate format and ranges.
"""

import re
import sys


def main():
    """
    Main function that prompts user for IPv4 address and validates it.

    Prints True if valid IPv4 address, False otherwise.
    """
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    """
    Validate whether a string is a correct IPv4 address using regex.

    An IPv4 address:
    - Has exactly 4 parts separated by periods
    - Each part is an integer from 0 to 255
    - No leading zeros (except for "0" itself)
    - Uses precise regex pattern matching for validation

    Args:
        ip (str): input string to validate

    Returns:
        bool: True if valid IPv4 address, else False
    """
    # Handle None and non-string input
    if ip is None or not isinstance(ip, str):
        return False

    # Strip whitespace from beginning and end
    ip = ip.strip()

    # Define regex pattern for valid IPv4 octet (0-255)
    # [0-9] matches 0-9, [1-9][0-9] matches 10-99 (no leading zero)
    # 1[0-9][0-9] matches 100-199, 2[0-4][0-9] matches 200-249
    # 25[0-5] matches 250-255
    byte = r"([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])"

    # Build complete IPv4 pattern: octet.octet.octet.octet
    # ^ ensures start of string, $ ensures end of string (no extra characters)
    pattern = rf"^{byte}\.{byte}\.{byte}\.{byte}$"

    # Return True if pattern matches, False otherwise
    return bool(re.match(pattern, ip))


# Prevent `main()` from running during pytest
if __name__ == "__main__" and "pytest" not in sys.modules:
    main()
