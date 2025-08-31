"""plates.py
Author: TJ Tryon
Date: July 16, 2025

This program checks if a proposed license plate is valid based on specific rules.
"""

import string


def is_valid(s):
    """
    Validates a license plate string according to these rules:
    1. Length must be between 2 and 6 characters.
    2. No punctuation or spaces.
    3. Numbers must come only at the end, and the first number must not be '0'.
    4. Cannot be exactly two digits.

    Args:
        s (str): The proposed license plate string.

    Returns:
        bool: True if valid, False otherwise.
    """
    # Rule 1: Length
    if not (2 <= len(s) <= 6):
        return False

    # Rule 2: No punctuation or spaces
    if any(c in string.punctuation or c.isspace() for c in s):
        return False

    # Rule 3 & 4: Letter(s) followed by digits, and first digit not 0
    digit_started = False
    for i, c in enumerate(s):
        if c.isdigit():
            if not digit_started:
                if c == '0':
                    return False
                digit_started = True
        elif digit_started:
            return False  # Letter found after digit

    return s[0:2].isalpha()  # First two must be letters


def main():
    """
    Main program flow:
    - Prompts user for plate input.
    - Validates using is_valid().
    - Prints "Valid" or "Invalid".
    """
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
