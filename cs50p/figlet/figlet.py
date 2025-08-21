""" figlet.py
Author: TJ Tryon
Date: 2025-07-15

This program prompts the user to input a string of text and prints it
in ASCII art using a Figlet font. It also accepts optional command-line arguments
to specify a font with "-f fontname" or "--font fontname".

Uses: pyfiglet.Figlet
"""

import sys
from pyfiglet import Figlet


def get_font_from_args():
    """
    Check command-line arguments for a specified font.

    Returns:
        str or None: The font name if valid and provided, else None.
    """
    if len(sys.argv) == 3 and sys.argv[1] in ("-f", "--font"):
        figlet = Figlet()
        if sys.argv[2] in figlet.getFonts():
            return sys.argv[2]
        else:
            sys.exit("Invalid font name.")
    elif len(sys.argv) > 1:
        sys.exit("Usage: figlet.py [-f fontname]")
    return None


def get_input():
    """
    Prompt the user for input text.

    Returns:
        str: The user's input string.
    """
    return input("Input: ").strip()


def print_output(text, font=None):
    """
    Render and print the input text using the specified Figlet font.

    Args:
        text (str): The input string to convert.
        font (str, optional): The Figlet font name. Uses default if None.
    """
    figlet = Figlet()
    if font:
        figlet.setFont(font=font)
    print("Output:\n")
    print(figlet.renderText(text))


def main():
    """
    Main program flow:
    - Check for optional font argument.
    - Get user input.
    - Print input in Figlet font.
    """
    font = get_font_from_args()
    user_input = get_input()
    print_output(user_input, font)


# Run the program if this script is executed directly
if __name__ == "__main__":
    main()
