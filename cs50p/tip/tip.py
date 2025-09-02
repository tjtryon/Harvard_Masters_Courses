""" tip.py
Author: TJ Tryon
Date: July 7, 2025

This program is a tip calculator. It takes inputs for the amount of the bill
and the percentage you would like to tip. It provides the tip amount.
"""


def dollars_to_float(d):
    """ Converts the dollars string input to float. Removes $ if present. """
    return float(d.strip().replace("$", ""))


def percent_to_float(p):
    """ Converts the percent string input to float. Removes % if present. """
    return float(p.strip().replace("%", "")) / 100


def main():
    """Main program flow.
    First ask for the bill amount in dollars, then the percent to tip.
    Both call functions to convert the input string to a float for the
    Tip calculations to print. """

    try:
        dollars = dollars_to_float(input("How much was the meal? "))
        percent = percent_to_float(input("What percentage would you like to tip? "))

    except ValueError:
        print("Invalid input. Please enter numeric values.")

    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


# Call the main function
if __name__ == "__main__":
    main()
