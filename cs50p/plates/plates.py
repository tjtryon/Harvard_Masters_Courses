""" plates.py
Author: TJ Tryon
Date: July 12, 2025

This program takes an input for a proposed Massachusetts license plate and
verifies if it is in proper format per Massachusetts license plate format.
"""

import string


def get_plate():
    """
    Prompts the user for a License Plate input string.

    Returns:
        str: User-provided License Plate string.
    """
    return input("Plate: ")


def is_plate_valid(plate):
    """
    Validates the input plate string against Massachusetts license plate rules:

    1. Must be between 2 and 6 characters in length.
    2. Cannot contain spaces, punctuation, or special characters.
    3. If all letters or all digits, it's valid (unless it's exactly 2 digits).
    4. If mixed letters and digits:
       - All digits must follow all letters (e.g., ABC123 is valid, AB1C23 is not).
       - First digit (if present) must not be zero.
    5. Plate cannot be exactly two digits (e.g., "12" is invalid).

    Args:
        plate (str): The proposed license plate string.

    Returns:
        bool: True if all conditions are met, False otherwise.
    """
    # Rule 1: Length check
    if not (2 <= len(plate) <= 6):
        return False

    # Rule 2: No punctuation or spaces
    if any(c in string.punctuation or c.isspace() for c in plate):
        return False

    # Rule 5 (new): Disallow exactly two digits
    if len(plate) == 2 and plate.isdigit():
        return False

    # Rule 3: All letters or all digits
    if plate.isalpha() or plate.isdigit():
        return True

    # Rule 4 + 6: Mixed content (letters then digits), no leading 0
    has_letter = False
    has_digit = False
    digit_started = False

    for i, c in enumerate(plate):
        if c.isalpha():
            if digit_started:
                return False  # Found a letter after a digit
            has_letter = True
        elif c.isdigit():
            if not has_digit:
                # First digit seen; check if it’s '0'
                if c == '0':
                    return False  # Rule 6: First digit must not be '0'
            digit_started = True
            has_digit = True
        else:
            return False  # Non-alphanumeric char (just in case)

    return has_letter and has_digit


def print_plate_valid(validity):
    """
    Prints 'Valid' or 'Invalid' depending on plate validation.

    Args:
        validity (bool): Result of plate validation.
    """
    if validity:
        print("Valid")
    else:
        print("Invalid")


def main():
    """
    Main program flow:
    - Gets plate input from user.
    - Validates the plate.
    - Prints whether it's valid or not.
    """
    plate = get_plate()
    validity = is_plate_valid(plate)
    print_plate_valid(validity)


# Run the main program when executed directly
if __name__ == "__main__":
    main()
