"""Meal time checker.

Author: TJ Tryon
Date: July 10, 2025

Given a time input in 24-hour format, this program alerts the user if it is mealtime.
Supports HH:MM, HHMM, or decimal hours.
All internal time is converted to decimal hours (e.g., 7.5 for 7:30).
"""


def user_time_input():
    """
    Prompt the user to input a time.

    Returns:
        str: The user's raw input as a string.
    """
    return input("What time is it? (Examples: 0700, 18:30, 7.5) ")


def convert(strtime):
    """
    Parse the input time string and convert it to decimal hours.

    Supported formats:
    - HH:MM (e.g., "18:30")
    - HHMM (e.g., "0730")
    - Decimal hours (e.g., "7.5")

    Args:
        strtime (str): The input time string.

    Returns:
        float: The decimal hour (e.g., 7.5 for "7:30").
    """
    time_input = strtime.strip().replace(" ", "")

    if ":" in time_input:
        # HH:MM format
        hours, minutes = time_input.split(":")
        return int(hours) + int(minutes) / 60

    elif "." in time_input:
        # Decimal hours format
        return float(time_input)

    elif time_input.isdigit() and len(time_input) in [3, 4]:
        # HHMM format
        hours = int(time_input[:-2])
        minutes = int(time_input[-2:])
        return hours + minutes / 60

    else:
        raise ValueError("Invalid time format. Use HH:MM, HHMM, or decimal hours.")


def print_mealtime(decimal_hour):
    """
    Print a message if the decimal hour matches a mealtime.

    Args:
        decimal_hour (float): The time in decimal hours.
    """
    if 7.0 <= decimal_hour < 8.0 or abs(decimal_hour - 8.0) < 0.01:
        print("Breakfast Time")
    elif 12.0 <= decimal_hour < 13.0 or abs(decimal_hour - 13.0) < 0.01:
        print("Lunch Time")
    elif 18.0 <= decimal_hour < 19.0 or abs(decimal_hour - 19.0) < 0.01:
        print("Dinner Time")
    else:
        print("It's not mealtime yet.")


def main():
    """
    Run the main program logic.

    Prompts the user for a time, converts it to decimal hours,
    and prints the corresponding mealtime message.
    """
    try:
        str_time = user_time_input()
        decimal_hour = convert(str_time)
        print_mealtime(decimal_hour)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
