""" extensions.py
Author: TJ Tryon
Date: July 10, 2025

This program checks the extension of a file inputted by a user and
prints out the corresponding MIME type.
"""

import os


def check_extension(extension):
    """
    Determines the MIME type given a file extension.

    Args:
        extension (str): The file extension, expected to be in lowercase without a dot.

    Returns:
        str: The MIME type as a string (e.g., "image/png").
             If the extension is unrecognized, returns "application/octet-stream".
    """

    # Determine MIME type using match-case
    match extension:
        case "gif" | "jpeg" | "png":
            return f"image/{extension}"
        case "pdf" | "zip":
            return f"application/{extension}"
        case "text":
            return "text/plain"
        case _:
            return "application/octet-stream"


def get_extension():
    """
    Prompts the user for a filename and extracts the file extension.

    Returns:
        str: The file extension (including the leading period),
             or an empty string if no extension is present.
    """
    file = input("filename? ")
    _, extension = os.path.splitext(file)

    return extension


def main():
    """
    Main program logic:
    - Prompts the user for a filename and extracts its extension.
    - Cleans the extension by stripping whitespace, converting to lowercase,
      and removing the leading period.
    - Normalizes common alternate extensions.
    - Determines and prints the corresponding MIME type.
    """
    extension = get_extension()
    extension = extension.strip().lower().replace(".", "")

    # Normalize common alternate forms of extensions
    if extension == "jpg":
        extension = "jpeg"
    if extension == "txt":
        extension = "text"

    # Get MIME type and print it
    mime_type = check_extension(extension)
    print(mime_type)


# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
