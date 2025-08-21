""" emojize.py
Author: TJ Tryon
Date: 2025-07-15

This program prompts the user to input a string containing emoji shortcodes.
It then converts those shortcodes into actual emojis and prints the result.

It uses the following module: emoji
"""

import emoji


def get_input():
    """
    Prompt the user for input and return it.

    Returns:
        str: The user's input.
    """
    user_input = input("Input: ")
    return user_input.strip()


def convert_input(input_str):
    """
    Convert emoji shortcodes in the input string into emojis.

    Args:
        input_str (str): The user's input with emoji shortcodes (e.g., :thumbs_up:).

    Returns:
        str: The converted string with actual emoji characters.
    """
    return emoji.emojize(input_str, language="alias")


def print_output(output_str):
    """
    Print the final output to the console.

    Args:
        output_str (str): The converted string with emojis.
    """
    print(f"Output: {output_str}")


def main():
    """
    Main program flow.
    Ask user to input a string with emoji "codes",
    convert them to emojis, and print the result.
    """
    emoji_string = get_input()
    converted = convert_input(emoji_string)
    print_output(converted)


# Run the program if this script is executed directly
if __name__ == "__main__":
    main()
