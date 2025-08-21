"""
shirt.py - A Virtual T-Shirt Try-On Program

Author: TJ Tryon
Date: August 01, 2025

Usage: python3 shirt.py <input_image> <output_image>
Example: python3 shirt.py person.jpg result.jpg

This program overlays a CS50 t-shirt onto a person's photo by resizing,
cropping, and combining images using the Pillow library.
"""

import sys
import os
from PIL import Image, ImageOps


def validate_arguments():
    """
    Check if the user provided exactly two command-line arguments.

    Returns:
        tuple: A tuple containing (input_filename, output_filename)

    Raises:
        SystemExit: If the wrong number of arguments is provided
    """
    # Check that exactly two image filenames are provided
    # sys.argv contains [program_name, input_image, output_image]
    if len(sys.argv) != 3:
        sys.exit("Usage: python3 shirt.py <input_image> <output_image>")

    # Return both filenames as a tuple
    return sys.argv[1], sys.argv[2]


def get_file_extension(filename):
    """
    Extract the file extension from a filename in lowercase.

    Args:
        filename (str): The filename to extract extension from

    Returns:
        str: The file extension in lowercase (including the dot)
    """
    # Split filename on the last dot and convert to lowercase
    # This handles cases like "image.JPEG" or "photo.PNG"
    return os.path.splitext(filename.lower())[1]


def validate_file_extensions(input_filename, output_filename):
    """
    Validate that both files have supported image extensions and match.

    Args:
        input_filename (str): Path to the input image file
        output_filename (str): Path to the output image file

    Returns:
        tuple: A tuple containing (input_extension, output_extension)

    Raises:
        SystemExit: If extensions are invalid or don't match
    """
    # Define supported image file extensions
    valid_extensions = {'.jpg', '.jpeg', '.png'}

    # Get file extensions in lowercase
    input_ext = get_file_extension(input_filename)
    output_ext = get_file_extension(output_filename)

    # Check if input file has a valid extension
    if input_ext not in valid_extensions:
        sys.exit(f"Error: Input file must be a .jpg, .jpeg, or .png file")

    # Check if output file has a valid extension
    if output_ext not in valid_extensions:
        sys.exit(f"Error: Output file must be a .jpg, .jpeg, or .png file")

    # Check if input and output extensions match
    # Treat .jpg and .jpeg as equivalent
    if not extensions_match(input_ext, output_ext):
        sys.exit("Error: Input and output files must have the same extension")

    return input_ext, output_ext


def extensions_match(ext1, ext2):
    """
    Check if two file extensions are equivalent for image processing.

    Args:
        ext1 (str): First file extension
        ext2 (str): Second file extension

    Returns:
        bool: True if extensions are equivalent, False otherwise
    """
    # Treat .jpg and .jpeg as the same extension
    jpeg_extensions = {'.jpg', '.jpeg'}

    # If both are JPEG variants, they match
    if ext1 in jpeg_extensions and ext2 in jpeg_extensions:
        return True

    # For other extensions, they must be exactly the same
    return ext1 == ext2


def validate_input_file(input_filename):
    """
    Check if the input file exists and can be accessed.

    Args:
        input_filename (str): Path to the input image file

    Raises:
        SystemExit: If the file doesn't exist or cannot be accessed
    """
    # Check if the input file exists in the filesystem
    if not os.path.exists(input_filename):
        sys.exit(f"Error: Input file '{input_filename}' does not exist")


def load_images(input_filename, shirt_filename="shirt.png"):
    """
    Load the input photo and shirt overlay image.

    Args:
        input_filename (str): Path to the input photo
        shirt_filename (str): Path to the shirt overlay image

    Returns:
        tuple: A tuple containing (input_image, shirt_image)

    Raises:
        SystemExit: If either image cannot be loaded
    """
    try:
        # Load the input photo
        input_image = Image.open(input_filename)
    except Exception as e:
        sys.exit(f"Error loading input image '{input_filename}': {e}")

    try:
        # Load the shirt overlay image
        shirt_image = Image.open(shirt_filename)
    except Exception as e:
        sys.exit(f"Error loading shirt image '{shirt_filename}': {e}")

    return input_image, shirt_image


def resize_and_crop_image(input_image, target_size):
    """
    Resize and crop the input image to match the target size.

    Args:
        input_image (PIL.Image): The input photo to resize and crop
        target_size (tuple): Target size as (width, height)

    Returns:
        PIL.Image: The resized and cropped image
    """
    # Use ImageOps.fit to resize and crop the image to exact target size
    # This maintains aspect ratio and crops from center if needed
    fitted_image = ImageOps.fit(input_image, target_size)

    return fitted_image


def overlay_shirt(fitted_image, shirt_image):
    """
    Overlay the shirt image onto the fitted photo.

    Args:
        fitted_image (PIL.Image): The resized and cropped photo
        shirt_image (PIL.Image): The shirt overlay with transparent background

    Returns:
        PIL.Image: The combined image with shirt overlay
    """
    # Create a copy of the fitted image to avoid modifying the original
    result_image = fitted_image.copy()

    # Paste the shirt onto the photo using the shirt's transparency
    # The shirt image itself is used as the mask for transparency
    result_image.paste(shirt_image, (0, 0), shirt_image)

    return result_image


def save_result_image(result_image, output_filename):
    """
    Save the final image with shirt overlay to the output file.

    Args:
        result_image (PIL.Image): The final combined image
        output_filename (str): Path where to save the result

    Raises:
        SystemExit: If the image cannot be saved
    """
    try:
        # Save the final image to the specified output file
        result_image.save(output_filename)
    except Exception as e:
        sys.exit(f"Error saving output image '{output_filename}': {e}")


def main():
    """
    Main program execution function.
    Coordinates the virtual t-shirt try-on process.
    """
    # Get and validate command-line arguments
    input_filename, output_filename = validate_arguments()

    # Validate file extensions and compatibility
    validate_file_extensions(input_filename, output_filename)

    # Check that input file exists
    validate_input_file(input_filename)

    # Load both the input photo and shirt overlay
    input_image, shirt_image = load_images(input_filename)

    # Get the shirt dimensions to use as target size
    shirt_size = shirt_image.size

    # Resize and crop the input photo to match shirt size
    fitted_image = resize_and_crop_image(input_image, shirt_size)

    # Overlay the shirt onto the fitted photo
    result_image = overlay_shirt(fitted_image, shirt_image)

    # Save the final result
    save_result_image(result_image, output_filename)

    # Confirm successful completion
    print(f"Successfully created '{output_filename}' with shirt overlay")


# Run the main function to start the program
if __name__ == "__main__":
    main()
