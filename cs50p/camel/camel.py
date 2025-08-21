""" camel.py
Author: TJ Tryon
Date: July 12, 2025

This program takes an input in camelCase and outputs snake_case.
"""

# Uses re for the conversion from camelCase to snake_case
import re


def get_camel():
    """
    Prompts the user for a camelCase input string.

    Returns:
        str: User-provided camelCase string.
    """
    return input("camelCase: ")


def fix_camel(camel):
    """
    Converts a camelCase string to snake_case.
    Inserts underscores before uppercase letters, excluding the first character,
    then converts the entire string to lowercase.

    Args:
        camel (str): The camelCase input string.

    Returns:
        str: The snake_case equivalent string.
    """
    snake = re.sub(r'(?<!^)(?=[A-Z])', '_', camel)
    return snake.lower()


def print_snake(snake):
    """
    Outputs the converted snake_case string to the user.

    Args:
        snake (str): The snake_case version of the original string.
    """
    print(f"snake_case: {snake}")


def main():
    """
    Main program flow. Gets camelCase input, converts it to snake_case,
    and prints the result.
    """
    camel = get_camel()
    snake = fix_camel(camel)
    print_snake(snake)


# Run the program if executed directly
if __name__ == "__main__":
    main()
