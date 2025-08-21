"""
pizza.py - A CSV Table Display Program

Author: TJ Tryon
Date: August 01, 2025

Usage: python3 pizza.py <filename.csv>
Example: python3 pizza.py menu.csv

This program reads a CSV file and displays it as a formatted ASCII art table
using the tabulate library with grid formatting.
"""

import sys
import os
import csv
from tabulate import tabulate

def validate_arguments():
    """
    Check if the user provided exactly one command-line argument.

    Returns:
        str: The filename if valid

    Raises:
        SystemExit: If the wrong number of arguments is provided
    """
    # Check the number of command-line arguments
    # sys.argv contains [program_name, arg1, arg2, ...] so length should be 2
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 pizza.py <filename.csv>")

    # Return the filename argument
    return sys.argv[1]

def validate_filename(filename):
    """
    Check if the filename is valid (ends with .csv and exists).

    Args:
        filename (str): The name of the file to check

    Returns:
        str: The same filename if valid

    Raises:
        SystemExit: If the file doesn't end with .csv or doesn't exist
    """
    # Verify file has correct extension
    if not filename.endswith('.csv'):
        sys.exit("Error: File must have a .csv extension")

    # Verify file exists in the filesystem
    if not os.path.exists(filename):
        sys.exit(f"Error: File '{filename}' does not exist")

    return filename

def read_csv_file(filename):
    """
    Read data from a CSV file and return it as a list of lists.

    Args:
        filename (str): The name of the CSV file to read

    Returns:
        list: A list where each element is a list representing one row of the CSV

    Raises:
        SystemExit: If there's an error reading the file or if the file is empty
    """
    # Attempt to read the CSV file
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            # Initialize CSV reader to parse comma-separated values
            csv_reader = csv.reader(file)

            # Convert all rows to a list for processing
            data = list(csv_reader)

    except FileNotFoundError:
        sys.exit(f"Error: File '{filename}' not found")
    except PermissionError:
        sys.exit(f"Error: Permission denied to read '{filename}'")
    except UnicodeDecodeError:
        sys.exit(f"Error: Unable to decode '{filename}' as UTF-8 text")
    except csv.Error as e:
        sys.exit(f"Error: Invalid CSV format in '{filename}': {e}")
    except Exception as e:
        sys.exit(f"Error reading CSV file: {e}")

    # Validate that the file contains data
    if not data:
        sys.exit("Error: CSV file is empty")

    return data

def format_table(data):
    """
    Format CSV data as an ASCII art table using tabulate.

    Args:
        data (list): A list of lists where the first row contains headers
                    and remaining rows contain the table data

    Returns:
        str: A formatted table string ready for printing
    """
    # Extract header row and data rows
    # First row contains column headers, remaining rows contain data
    headers = data[0]
    rows = data[1:]

    # Generate formatted table using tabulate library
    # Grid format creates borders around all cells
    table = tabulate(rows, headers=headers, tablefmt="grid")

    return table

def main():
    """
    Main program execution function.
    Coordinates validation, file reading, and table formatting operations.
    """
    # Execute program workflow in logical sequence
    filename = validate_arguments()        # Validate command-line arguments
    validate_filename(filename)            # Verify file extension and existence
    data = read_csv_file(filename)         # Read CSV data into memory
    table = format_table(data)             # Format data as ASCII table

    # Output the formatted table
    print(table)

# Run the main function to start the program
if __name__ == "__main__":
    main()
