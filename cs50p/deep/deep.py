""" deep.py
Author: TJ Tryon
Date: July 10, 2025

This program checks to see if the user knows the Answer to the Great
Question of Life, the Universe, and Everything.
"""


def get_input():
    """
    Prompts the user to enter their answer to the Great Question.

    Returns:
        str: The user's input.
    """
    return input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")


def is_the_answer_correct(answer):
    """
    Checks if the given answer is correct. Accepts several variations:
    'forty two', 'forty-two', or '42' (as strings).

    Prints 'Yes' if correct, otherwise prints 'no'.

    Args:
        answer (str): The answer to check, expected to be in lowercase.
    """
    match answer:
        case "forty two" | "forty-two" | "42":
            print("Yes")
        case _:
            print("No")


def main():
    """
    Main program logic:
    - Prompts the user for an answer.
    - Converts the answer to lowercase for comparison.
    - Checks if the answer is correct.
    """
    user_answer = get_input()
    is_the_answer_correct(user_answer.strip().lower())


# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
