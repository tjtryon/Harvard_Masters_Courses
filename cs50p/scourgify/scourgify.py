"""
scourgify.py - A CSV Data Cleaning Program

Author: TJ Tryon
Date: August 01, 2025

Usage: python3 scourgify.py <input.csv> <output.csv>
Example: python3 scourgify.py before.csv after.csv

This program cleans CSV data by splitting combined names into separate
first and last name columns for better data formatting.
"""

import sys
import csv


def validate_arguments():
    """
    Check if the user provided exactly two command-line arguments.

    Returns:
        tuple: A tuple containing (input_filename, output_filename)

    Raises:
        SystemExit: If the wrong number of arguments is provided
    """
    # Check that exactly two filenames are provided
    # sys.argv contains [program_name, input_file, output_file]
    if len(sys.argv) != 3:
        sys.exit("Usage: python3 scourgify.py <input.csv> <output.csv>")

    # Return both filenames as a tuple
    return sys.argv[1], sys.argv[2]


def read_input_csv(input_filename):
    """
    Read the input CSV file and return the data as a list of dictionaries.

    Args:
        input_filename (str): Path to the input CSV file

    Returns:
        list: List of dictionaries, each representing a row with 'name' and 'house' keys

    Raises:
        SystemExit: If the file cannot be read or is improperly formatted
    """
    try:
        with open(input_filename, 'r', encoding='utf-8') as file:
            # Use DictReader to automatically handle headers
            # This creates dictionaries for each row using column names as keys
            reader = csv.DictReader(file)

            # Convert all rows to a list for processing
            data = list(reader)

    except FileNotFoundError:
        sys.exit(f"Error: Input file '{input_filename}' not found")
    except PermissionError:
        sys.exit(f"Error: Permission denied to read '{input_filename}'")
    except csv.Error as e:
        sys.exit(f"Error: Invalid CSV format in '{input_filename}': {e}")
    except Exception as e:
        sys.exit(f"Error reading input file: {e}")

    # Verify the file contains data
    if not data:
        sys.exit("Error: Input CSV file is empty")

    return data


def split_name(full_name):
    """
    Split a combined "last, first" name into separate first and last names.

    Args:
        full_name (str): Name in "last, first" format

    Returns:
        tuple: A tuple containing (first_name, last_name)

    Raises:
        ValueError: If the name format is invalid
    """
    # Remove any surrounding whitespace from the full name
    full_name = full_name.strip()

    # Split the name on comma to separate last and first names
    # Expected format: "last, first"
    if ',' not in full_name:
        raise ValueError(f"Name '{full_name}' is not in 'last, first' format")

    # Split on comma and clean up whitespace
    name_parts = full_name.split(',', 1)  # Split only on first comma

    if len(name_parts) != 2:
        raise ValueError(f"Name '{full_name}' is not in 'last, first' format")

    # Extract and clean the last and first names
    last_name = name_parts[0].strip()
    first_name = name_parts[1].strip()

    # Verify both names exist
    if not last_name or not first_name:
        raise ValueError(f"Name '{full_name}' contains empty first or last name")

    return first_name, last_name


def process_student_data(input_data):
    """
    Process the input data by splitting names into first and last components.

    Args:
        input_data (list): List of dictionaries with 'name' and 'house' keys

    Returns:
        list: List of dictionaries with 'first', 'last', and 'house' keys

    Raises:
        SystemExit: If any name cannot be properly split
    """
    processed_data = []

    # Process each student record
    for row_number, student in enumerate(input_data, start=2):  # Start at 2 for header row
        try:
            # Extract the combined name and house from current row
            combined_name = student.get('name', '').strip()
            house = student.get('house', '').strip()

            # Split the combined name into first and last names
            first_name, last_name = split_name(combined_name)

            # Create new record with separated names
            cleaned_record = {
                'first': first_name,
                'last': last_name,
                'house': house
            }

            processed_data.append(cleaned_record)

        except ValueError as e:
            sys.exit(f"Error processing row {row_number}: {e}")
        except KeyError as e:
            sys.exit(f"Error: Missing required column {e} in input file")

    return processed_data


def write_output_csv(output_filename, processed_data):
    """
    Write the processed data to the output CSV file.

    Args:
        output_filename (str): Path to the output CSV file
        processed_data (list): List of dictionaries with 'first', 'last', 'house' keys

    Raises:
        SystemExit: If the file cannot be written
    """
    try:
        with open(output_filename, 'w', newline='', encoding='utf-8') as file:
            # Define the column order for the output file
            fieldnames = ['first', 'last', 'house']

            # Create CSV writer with specified column headers
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Write the header row
            writer.writeheader()

            # Write all processed student records
            writer.writerows(processed_data)

    except PermissionError:
        sys.exit(f"Error: Permission denied to write '{output_filename}'")
    except Exception as e:
        sys.exit(f"Error writing output file: {e}")


def main():
    """
    Main program execution function.
    Coordinates the CSV cleaning process from input to output.
    """
    # Get and validate command-line arguments
    input_filename, output_filename = validate_arguments()

    # Read the input CSV data
    input_data = read_input_csv(input_filename)

    # Process the data by splitting names
    processed_data = process_student_data(input_data)

    # Write the cleaned data to output file
    write_output_csv(output_filename, processed_data)

    # Confirm successful completion
    print(
        f"Successfully processed {len(processed_data)} records from '{input_filename}' to '{output_filename}'")


# Run the main function to start the program
if __name__ == "__main__":
    main()
