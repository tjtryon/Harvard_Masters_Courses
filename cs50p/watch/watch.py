"""
watch.py - YouTube URL Extractor from HTML

Author: TJ Tryon
Date: August 01, 2025

Usage: python3 watch.py
Example: Enter HTML content when prompted

This program extracts YouTube URLs from iframe elements in HTML content
and converts them to their shorter, shareable youtu.be format.
Uses regular expressions to parse HTML and extract YouTube embed URLs.
"""

import re
import sys


def main():
    """
    Main function that prompts user for HTML content and extracts YouTube URL.

    Prints the shareable youtu.be URL if found, None otherwise.
    """
    print(parse(input("HTML: ")))


def parse(s):
    """
    Extract YouTube URL from iframe src attribute and convert to youtu.be format.

    Searches for iframe elements with YouTube embed URLs in their src attributes
    and returns the equivalent shareable youtu.be URL. Handles multiple YouTube
    URL formats including http/https and with/without www subdomain.

    Args:
        s (str): HTML string to parse for YouTube URLs

    Returns:
        str: Shareable youtu.be URL if YouTube iframe found, else None
    """
    # Handle None and non-string input
    if s is None or not isinstance(s, str):
        return None

    # Define regex pattern to match iframe with YouTube embed URL
    # <iframe[^>]* matches iframe opening tag with any attributes
    # \ssrc=" matches whitespace followed by src attribute with opening quote
    # (https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)) captures full URL and video ID
    # " matches closing quote, [^>]*> matches rest of tag
    pattern = r'<iframe[^>]*\ssrc="(https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+))"[^>]*>'

    # Search for the pattern in the input string
    match = re.search(pattern, s)

    if match:
        # Extract the video ID from the second capture group
        video_id = match.group(2)
        # Return the shareable youtu.be format
        return f"https://youtu.be/{video_id}"

    # Return None if no YouTube iframe found
    return None


# Prevent `main()` from running during pytest
if __name__ == "__main__" and "pytest" not in sys.modules:
    main()
