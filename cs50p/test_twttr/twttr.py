# twttr.py
""" twttr.py
Author: TJ Tryon
Date: July 12, 2025

Takes input from the user and returns that same string with all vowels removed.
"""

def main():
    user_input = input("Input: ")
    print(f"Output: {shorten(user_input)}")


def shorten(word):
    """
    Removes all vowels from the input string.

    Args:
        word (str): The original string entered by the user.

    Returns:
        str: The input string with all vowels removed.
    """
    vowels = "AEIOUaeiou"
    return "".join(char for char in word if char not in vowels)


if __name__ == "__main__":
    main()
