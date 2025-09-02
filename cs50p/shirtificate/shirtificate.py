"""
shirtificate.py - CS50 Shirtificate Generator

Author: TJ Tryon
Date: August 01, 2025

Usage: python3 shirtificate.py
Example: Enter your name when prompted to generate a personalized CS50 shirtificate

This program creates a PDF certificate featuring a CS50 shirt with the user's
name overlaid in white text. Uses fpdf2 library to generate the PDF with
proper formatting, centering, and layout matching the CS50 style.
Outputs to shirtificate.pdf in the current directory.
"""

from fpdf import FPDF
import sys


def main():
    """
    Main function that prompts for name and generates CS50 shirtificate PDF.

    Creates a personalized shirtificate with the user's name on a CS50 shirt
    and saves it as shirtificate.pdf in the current directory.
    """
    # Prompt user for their name
    name = input("Name: ").strip()

    if not name:
        sys.exit("Name cannot be empty")

    # Create the shirtificate PDF
    create_shirtificate(name)

    print("Shirtificate created successfully as shirtificate.pdf!")


def create_shirtificate(name):
    """
    Create a CS50 shirtificate PDF with the given name.

    Generates a PDF certificate featuring the CS50 shirt image with
    the user's name overlaid in white text, following the format
    specifications for portrait A4 layout.

    Args:
        name (str): Name to display on the shirtificate
    """
    # Create PDF with A4 portrait orientation
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Set title at top of page
    pdf.set_font("Arial", "B", 48)
    pdf.set_text_color(0, 0, 0)  # Black text
    pdf.cell(0, 60, "CS50 Shirtificate", align="C", ln=True)

    # Add shirt image (centered horizontally)
    # Image should be saved as "shirtificate.png" in the same directory
    try:
        # Calculate position to center the shirt image
        # Assuming shirt image is roughly 150mm wide when scaled
        shirt_width = 150
        shirt_x = (210 - shirt_width) / 2  # Center horizontally on A4 (210mm wide)
        shirt_y = pdf.get_y() + 10  # Position below title with some spacing

        # Insert the shirt image
        pdf.image("shirtificate.png", x=shirt_x, y=shirt_y, w=shirt_width)

    except FileNotFoundError:
        print("Error: shirtificate.png not found. Please save the shirt image as 'shirtificate.png' in the same directory.")
        sys.exit(1)

    # Add user's name on the shirt in white text
    pdf.set_font("Arial", "B", 24)
    pdf.set_text_color(255, 255, 255)  # White text

    # Position text in the center of the shirt
    # Adjust these values based on the actual shirt image dimensions and position
    text_y = shirt_y + 100  # Approximate center of shirt vertically

    # Calculate text width to center it properly
    text_width = pdf.get_string_width(f"{name} took CS50")
    text_x = (210 - text_width) / 2  # Center horizontally on page

    # Add the name text
    pdf.set_xy(text_x, text_y)
    pdf.cell(text_width, 10, f"{name} took CS50", align="C")

    # Save the PDF
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
