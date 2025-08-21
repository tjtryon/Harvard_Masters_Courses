"""
response.py - Email Address Validator

Author: TJ Tryon
Date: August 01, 2025

Usage: python3 response.py
Example: Enter email address when prompted

This program validates email addresses for syntactic correctness using
the validators library from PyPI. Does not check if the domain actually
exists, only validates the format according to email syntax rules.
Prints "Valid" or "Invalid" based on the input.
"""

import validators


def main():
    """
    Main function that prompts user for email address and validates it.

    Uses the validators library to check email syntax and prints
    "Valid" or "Invalid" accordingly.
    """
    # Prompt user for email address
    email = input("Email: ")

    # Validate email syntax using validators library
    # validators.email() returns True for valid emails, False/ValidationFailure for invalid
    if validators.email(email):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
