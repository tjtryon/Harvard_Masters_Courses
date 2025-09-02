"""
lines.py - A Python Line Counter Program

Author: TJ Tryon
Date: August 01, 2025

Usage: python lines.py <filename.py>
Example: python lines.py my_program.py

This program counts the number of lines of code in a Python file.
It ignores blank lines and comment lines (lines that start with #).
"""

import sys  # This helps us work with command line arguments and exit the program
import os   # This helps us check if files exist on the computer


def main():
    """
    This is the main function that does all the work.
    It's like the "brain" of our program that controls everything.
    """
    # Step 1: Check if the user gave us exactly one filename
    # sys.argv is a list that contains the program name and any arguments
    # sys.argv[0] is always "lines.py", sys.argv[1] should be the filename
    # So we need exactly 2 things in the list (the program name + 1 filename)
    if len(sys.argv) != 2:
        sys.exit("Usage: python lines.py <filename.py>")

    # Step 2: Get the filename the user wants us to check
    filename = sys.argv[1]  # This gets the filename from the command line

    # Step 3: Make sure the filename ends with ".py"
    # We only want to count lines in Python files!
    if not filename.endswith('.py'):
        sys.exit("Error: File must have a .py extension")

    # Step 4: Make sure the file actually exists on the computer
    # It's like checking if a book is really on the shelf before trying to read it
    if not os.path.exists(filename):
        sys.exit(f"Error: File '{filename}' does not exist")

    # Step 5: Try to open and read the file
    # This is like opening a book and reading all the pages
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()  # This reads every line and puts them in a list
    except Exception as e:
        # If something goes wrong (like the file is locked), we stop and tell the user
        sys.exit(f"Error reading file: {e}")

    # Step 6: Set up our counter to keep track of code lines
    # Think of this like having a tally sheet to count things
    line_count = 0

    # Step 7: Look at each line in the file, one by one
    # This is like reading a book page by page
    for line in lines:
        # Clean up the line by removing extra spaces at the beginning and end
        # It's like trimming the edges off a piece of paper
        stripped_line = line.strip()

        # Rule 1: Skip blank lines (lines with nothing but spaces)
        # If there's nothing important on the line, we don't count it
        if not stripped_line:
            continue  # This means "skip this line and go to the next one"

        # Rule 2: Skip comment lines (lines that start with #)
        # Comments are notes for humans, not actual code that runs
        # It's like skipping the margin notes in a textbook
        if stripped_line.startswith('#'):
            continue  # Skip this line too

        # If we get here, this line has real code in it!
        # So we add 1 to our counter
        line_count += 1

    # Step 8: Show our final answer!
    # After counting all the code lines, we tell the user how many we found
    print(line_count)


# This special line makes sure our main() function runs when someone starts the program
# It's like saying "When someone double-clicks this program, start with the main function"
if __name__ == "__main__":
    main()
