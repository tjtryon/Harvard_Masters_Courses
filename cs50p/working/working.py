"""
working.py - 12-hour to 24-hour Time Format Converter

Author: TJ Tryon
Date: August 01, 2025

Usage: python3 working.py
Example: Enter time range when prompted (e.g., "9:00 AM to 5:00 PM")

This program converts time ranges from 12-hour format to 24-hour format.
Handles various 12-hour formats with and without minutes specified.
Uses regular expressions to parse and validate time formats.
"""

import re
import sys


def main():
    """
    Main function that prompts user for time range and converts to 24-hour format.

    Prints the converted 24-hour format range or raises ValueError for invalid input.
    """
    print(convert(input("Hours: ")))


def convert(s):
    """
    Convert time range from 12-hour format to 24-hour format.

    Accepts various 12-hour formats and converts to 24-hour format.
    Validates that times are realistic and properly formatted.

    Args:
        s (str): Time range string in 12-hour format (e.g., "9:00 AM to 5:00 PM")

    Returns:
        str: Time range in 24-hour format (e.g., "09:00 to 17:00")

    Raises:
        ValueError: If input format is invalid or times are unrealistic
    """
    # Handle None and non-string input
    if not s or not isinstance(s, str):
        raise ValueError("Invalid input")

    # Strip whitespace
    s = s.strip()

    # Define regex pattern to match time range formats
    # (\d{1,2}) captures 1-2 digit hour
    # (?::(\d{2}))? optionally captures colon and 2-digit minutes
    # \s(AM|PM) captures space and AM/PM
    # \sto\s matches " to " exactly
    pattern = r'^(\d{1,2})(?::(\d{2}))?\s(AM|PM)\sto\s(\d{1,2})(?::(\d{2}))?\s(AM|PM)$'

    # Search for the pattern in the input string
    match = re.match(pattern, s)

    if not match:
        raise ValueError("Invalid format")

    # Extract matched groups
    start_hour_str, start_min_str, start_period, end_hour_str, end_min_str, end_period = match.groups()

    # Convert start time
    start_hour = int(start_hour_str)
    start_min = 0 if start_min_str is None else int(start_min_str)

    # Convert end time
    end_hour = int(end_hour_str)
    end_min = 0 if end_min_str is None else int(end_min_str)

    # Validate hours (1-12)
    if start_hour < 1 or start_hour > 12 or end_hour < 1 or end_hour > 12:
        raise ValueError("Invalid hour")

    # Validate minutes (0-59)
    if start_min < 0 or start_min > 59 or end_min < 0 or end_min > 59:
        raise ValueError("Invalid minutes")

    # Convert to 24-hour format
    start_24_hour = convert_hour_to_24(start_hour, start_period)
    end_24_hour = convert_hour_to_24(end_hour, end_period)

    # Format and return
    return f"{start_24_hour:02d}:{start_min:02d} to {end_24_hour:02d}:{end_min:02d}"


def convert_hour_to_24(hour, period):
    """
    Convert 12-hour format hour to 24-hour format.

    Args:
        hour (int): Hour in 12-hour format (1-12)
        period (str): "AM" or "PM"

    Returns:
        int: Hour in 24-hour format (0-23)
    """
    if period == "AM":
        if hour == 12:
            return 0  # 12 AM becomes 0
        else:
            return hour  # 1-11 AM stay the same
    else:  # PM
        if hour == 12:
            return 12  # 12 PM stays 12
        else:
            return hour + 12  # 1-11 PM become 13-23


# Prevent `main()` from running during pytest
if __name__ == "__main__" and "pytest" not in sys.modules:
    main()
