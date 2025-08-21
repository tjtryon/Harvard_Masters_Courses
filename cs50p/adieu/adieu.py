""" adieu.py
Author: TJ Tryon
Date: 2025-07-15

This program prompts the user to input a list of names and returns that list
to main(). Main sends the list to convert_input() to create a formatted string
bidding each person Adieu: "Adieu, Adieu, to Liesel, Friedrich, and Louisa."
Note the Oxford comma. Finally, it prints the resulting string.

It uses the following module: inflect
"""

import inflect

def get_input():
    """
    Prompt the user for a list of names until EOF is entered.

    Returns:
        list: A list of names entered by the user.
    """
    names = []
    while True:
        try:
            names.append(input("Name: "))
        except EOFError:
            print()  # Clean newline after EOF
            break
    return names

def convert_input(names):
    """
    Convert a list of names into a single string using commas and an Oxford comma.

    Args:
        names (list): The list of names to format.

    Returns:
        str: A comma-separated string with "and" before the last item.
    """
    p = inflect.engine()
    return p.join(names)

def print_output(formatted_names):
    """
    Print the goodbye message using the formatted list of names.

    Args:
        formatted_names (str): A string of names, formatted with Oxford comma.
    """
    print(f"Adieu, adieu, to {formatted_names}")

def main():
    """
    Main program flow:
    - Get a list of names
    - Format them using Oxford comma and "and"
    - Print the goodbye message
    """
    names = get_input()
    goodbye_message = convert_input(names)
    print_output(goodbye_message)

# Run the program if this script is executed directly
if __name__ == "__main__":
    main()
