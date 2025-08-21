""" grocery.py
Author: TJ Tryon
Date: July 14, 2025

This program prompts the user to input grocery list items and returns an alphabetized,
uppercase list of items, prefixed by the number of times the user inputted the item.
Press Ctrl+D to end input.
"""


def get_items():
    """
    Continuously prompts the user for grocery list items.
    Input is terminated using EOF (Ctrl+D)
    .
    Items must contain only letters and spaces.

    Returns:
        dict: A dictionary of items and their quantities.
    """
    grocery_list = {}

    while True:
        try:
            item = input().strip().lower()

            # Skip if the input contains invalid characters
            if not item or not all(c.isalpha() or c.isspace() for c in item):
                continue

            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1

        except EOFError:
            print()  # To move to next line cleanly
            break

    return grocery_list


def print_list(grocery_list):
    """
    Prints the grocery list in alphabetical order with quantities.
    Item names are printed in uppercase, preceded by their count.

    Args:
        grocery_list (dict): Dictionary of grocery items and quantities.
    """
    for item in sorted(grocery_list.keys()):
        print(f"{grocery_list[item]} {item.upper()}")


def main():
    """
    Main program flow:
    - Prompts the user for grocery items until EOF.
    - Builds and returns a dictionary of item counts.
    - Prints an alphabetized grocery list with item quantities.
    """
    grocery_list = get_items()
    print_list(grocery_list)


# Entry point of the script
if __name__ == "__main__":
    main()
