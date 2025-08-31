""" bank.py
Author: TJ Tryon
Date: July 17, 2025

This program prompts for a greeting and returns an integer value based on:
- $0 if greeting starts with "hello"
- $20 if greeting starts with "h" but not "hello"
- $100 otherwise
"""


def main():
    """
    Main program logic:
    - Prompt user for a greeting.
    - Call value() with greeting.
    - Print the result.
    """
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")


def value(greeting):
    """
    Determine the amount of money awarded based on the greeting provided.

    Args:
        greeting (str): The user's greeting.

    Returns:
        int: The amount awarded:
             - 0 if it starts with "hello"
             - 20 if it starts with "h" but not "hello"
             - 100 otherwise
    """
    greeting = greeting.strip().lower()

    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
