""" fuel.py
Author: TJ Tryon
Date: July 13, 2025

This program prompts the user to input a fraction (like '3/4'),
validates it using the Fraction class from the fractions module,
converts it to a percentage, and prints it with special labels
for very low or high values ("E" and "F").
"""

from fractions import Fraction

def get_fraction():
    """
    Prompts the user for a valid fraction in the form X/Y.
    Continues to prompt until the user inputs a valid fraction
    between 0 and 1 inclusive (e.g., 1/2, 3/4).

    Returns:
        str: The user input string that is a valid fraction in range.
    """
    while True:
        try:
            fraction = input("Fraction: ").strip()
            numeric_fraction = Fraction(fraction)
            if 0 <= numeric_fraction <= 1:
                return fraction
            else:
                # Fraction is out of range; ignore and re-prompt
                pass
        except (ValueError, ZeroDivisionError):
            # Invalid input format or zero division; re-prompt
            print()
            break


def convert_fraction_percent(fraction):
    """
    Converts a string fraction to a percentage.

    Args:
        fraction (str): A string representing a valid fraction (e.g., "3/4").

    Returns:
        int: The percentage (e.g., 75 for "3/4").
    """
    numeric_fraction = Fraction(fraction)
    return round(float(numeric_fraction) * 100)


def print_percent(percent):
    """
    Prints the percentage result with special cases:
    - If percent <= 1, prints "E"
    - If percent >= 99, prints "F"
    - Otherwise, prints the percent with a % sign

    Args:
        percent (int): The percentage to be printed.
    """
    if percent <= 1:
        print("E")
    elif percent >= 99:
        print("F")
    else:
        print(f"{percent}%")


def main():
    """
    Main program workflow:
    1. Prompt user for a valid fraction.
    2. Convert the fraction to a percentage.
    3. Print the appropriate output based on the percent.
    """
    fraction = get_fraction()
    percent = convert_fraction_percent(fraction)
    print_percent(percent)


# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
