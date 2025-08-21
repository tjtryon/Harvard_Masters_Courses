""" twttr.py
Author: TJ Tryon
Date: July 12, 2025

This program takes input as a string, strips the vowels, and re-prints the string.
"""


def get_user_input():
    """
    Prompt the user for a string input.

    Returns:
        str: The user input string.
    """
    return input("Input: ")


def strip_vowels(user_input):
    """
    Removes all vowels from the input string.

    Args:
        user_input (str): The original string entered by the user.

    Returns:
        str: The input string with all vowels removed.
    """
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    stripped_string = ""  # Initialize empty string to hold result

    for char in user_input:
        if char not in vowels:
            stripped_string += char  # Append non-vowel characters

    return stripped_string


def print_results(stripped_string):
    """
    Print the final string with vowels removed.

    Args:
        stripped_string (str): The cleaned string with vowels removed.
    """
    print(f"Output: {stripped_string}")


def main():
    """
    Main program logic:
    - Gets input from the user.
    - Strips vowels using strip_vowels().
    - Prints the final result.
    """
    user_input = get_user_input()
    stripped_vowels = strip_vowels(user_input)
    print_results(stripped_vowels.replace("  ", " "))


# Run the program if this file is executed directly
if __name__ == "__main__":
    main()
