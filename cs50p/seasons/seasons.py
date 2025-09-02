"""
seasons.py - Age Calculator in Minutes

Author: TJ Tryon
Date: August 01, 2025

Usage: python3 seasons.py
Example: Enter birth date in YYYY-MM-DD format when prompted

This program calculates how many minutes have passed since a user's birth date,
accounting for leap years. Outputs the result in English words like the song
from Rent. Assumes birth time and current time are both midnight for simplicity.
Uses Python's datetime module for accurate date calculations.
"""

from datetime import date
import sys
import inflect


def main():
    """
    Main function that prompts for birth date and calculates age in minutes.

    Gets user's birth date, calculates minutes lived, and prints the result
    in English words. Exits with error if date format is invalid.
    """
    # Prompt user for birth date
    birth_date_str = input("Date of Birth: ")

    # Parse and validate the birth date
    birth_date = parse_date(birth_date_str)

    # Calculate minutes lived since birth
    minutes_lived = calculate_minutes_since_birth(birth_date)

    # Convert to English words and print
    minutes_in_words = convert_to_words(minutes_lived)
    print(f"{minutes_in_words} minutes")


def parse_date(date_str):
    """
    Parse and validate date string in YYYY-MM-DD format.

    Args:
        date_str (str): Date string in YYYY-MM-DD format

    Returns:
        date: Parsed date object

    Exits:
        Program exits with error code 1 if date format is invalid
    """
    try:
        # Parse date string in YYYY-MM-DD format
        year, month, day = date_str.split('-')
        return date(int(year), int(month), int(day))
    except (ValueError, TypeError):
        # Exit if date format is invalid or date is impossible
        sys.exit("Invalid date format. Please use YYYY-MM-DD.")


def calculate_minutes_since_birth(birth_date):
    """
    Calculate total minutes lived since birth date.

    Uses datetime.date.today() to get current date and calculates
    the difference in days, then converts to minutes. Accounts for
    leap years automatically through Python's date arithmetic.

    Args:
        birth_date (date): Date of birth

    Returns:
        int: Total minutes lived, rounded to nearest integer
    """
    # Get today's date
    today = date.today()

    # Calculate difference in days
    days_lived = (today - birth_date).days

    # Convert days to minutes (24 hours * 60 minutes per hour)
    minutes_lived = days_lived * 24 * 60

    return round(minutes_lived)


def convert_to_words(number):
    """
    Convert integer to English words without 'and', with proper capitalization.

    Args:
        number (int): Number to convert to words

    Returns:
        str: Number expressed in English words, capitalized
    """
    # Create inflect engine for number-to-words conversion
    p = inflect.engine()

    # Convert number to words and remove 'and'
    words = p.number_to_words(number, andword='')

    # Capitalize the first letter
    return words.capitalize()


if __name__ == "__main__":
    main()
