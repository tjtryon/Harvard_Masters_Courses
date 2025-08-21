""" outdated.py
Author: TJ Tryon
Date: July 14, 2025

This program prompts the user to input a date in either MM/DD/YYYY or
"Month D, YYYY" format, and returns the date in ISO format: YYYY-MM-DD.
It uses the datetime module to parse and convert the date.
"""

from datetime import datetime


def get_date():
    """
    Continuously prompts the user for a date in middle-endian format:
    - MM/DD/YYYY
    - Month D, YYYY (e.g., July 14, 2025)

    Returns:
        str: A string representing the date in ISO format YYYY-MM-DD
    """
    while True:
        try:
            user_input = input("Date: ").strip()

            # Try parsing MM/DD/YYYY format
            try:
                dt = datetime.strptime(user_input, "%m/%d/%Y")
            except ValueError:
                # Try parsing Month D, YYYY format
                dt = datetime.strptime(user_input, "%B %d, %Y")

            return dt.strftime("%Y-%m-%d")

        except ValueError:
            # If both parsing attempts fail, reprompt
            continue


def print_date(formatted_date):
    """
    Prints the formatted ISO date.

    Args:
        formatted_date (str): A date string in YYYY-MM-DD format
    """
    print(formatted_date)


def main():
    """
    Main program flow:
    - Prompts the user for a date.
    - Converts it to ISO format.
    - Prints the result.
    """
    formatted_date = get_date()
    print_date(formatted_date)


# Run the program if this script is executed directly
if __name__ == "__main__":
    main()
