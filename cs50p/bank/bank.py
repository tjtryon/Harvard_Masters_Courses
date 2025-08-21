""" bank.py
Author: TJ Tryon
Date: July 10, 2025

This program checks the greeting the user receives at the bank
and uses Kramer's thoughts, on Seinfeld, to see if he gets money
for not getting a greeting of "hello".
"""


def check_greeting(greeting):
    """
    Determines the amount of money awarded based on the greeting provided.

    - If the greeting is "hello", the user gets $0.
    - If the greeting is one of several informal alternatives, the user gets $20.
    - For any other greeting, the user gets $100.

    Args:
        greeting (str): The user's greeting, expected to be in lowercase.

    Prints:
        The amount of money awarded.
    """
    match greeting:
        case "hello" | "hello, newman":
            print("$0")
        case "hey" | "howdy" | "hiya" | "how you doing?":
            print("$20")
        case _:
            print("$100")


def get_greeting():
    """
    Prompts the user for a greeting.
    """
    return input("Greeting? ")


def main():
    """
    Main program logic:
    - Prompts the user to enter a greeting.
    - Converts the greeting to lowercase and strips whitespace.
    - Checks the greeting and prints the corresponding reward.
    """
    greeting = get_greeting()
    check_greeting(str(greeting).strip().lower())


# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
