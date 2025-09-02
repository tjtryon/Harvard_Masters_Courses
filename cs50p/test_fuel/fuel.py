"""fuel.py
Author: TJ Tryon
Date: July 13, 2025

This program converts a fuel fraction to a percentage and
displays a fuel gauge representation using special cases for empty and full.
"""

def main():
    """
    Main program logic:
    - Prompts the user for a fraction input.
    - Converts to percent using convert().
    - Displays gauge result using gauge().
    """
    while True:
        try:
            fraction = input("Fraction: ")
            percent = convert(fraction)
            print(gauge(percent))
            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    """
    Converts a string in X/Y format to a percentage.

    Args:
        fraction (str): The input string in the form X/Y.

    Returns:
        int: The integer percentage (rounded).

    Raises:
        ValueError: If X or Y is not an integer or if X > Y.
        ZeroDivisionError: If Y == 0.
    """
    try:
        x_str, y_str = fraction.split("/")
        x = int(x_str)
        y = int(y_str)

        if y == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        if x > y:
            raise ValueError("Numerator cannot be greater than denominator.")

        return round((x / y) * 100)

    except (ValueError, ZeroDivisionError):
        raise


def gauge(percentage):
    """
    Returns the fuel level gauge string based on percent.

    Args:
        percentage (int): The percentage to evaluate.

    Returns:
        str: "E" if <= 1, "F" if >= 99, otherwise "Z%" where Z is percentage.
    """
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
