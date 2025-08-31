""" bitcoin.py
Author: TJ Tryon
Date: 2025-07-15

This program accepts one command-line argument: the number of bitcoins to buy.
It then retrieves the current price of Bitcoin from the CoinCap v3 API using an API key,
multiplies the quantity by the price, and prints the total cost formatted to 4 decimal places.

Uses: requests, sys
"""

import requests
import sys

API_KEY = "85f8f86a9aae58a1ef7532baeeaf4ad3925b83813f0acd9c8e780f75c7317976"
API_URL = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}"


def convert_argv_to_float():
    """
    Convert the first command-line argument to a float.

    Returns:
        float: The number of bitcoins to buy.

    Exits:
        If the argument is missing or cannot be converted.
    """
    try:
        return float(sys.argv[1])
    except (IndexError, ValueError):
        sys.exit("Missing or invalid command-line argument. Usage: python bitcoin.py <number_of_bitcoins>")


def get_json_for_bitcoin():
    """
    Fetch the current price of Bitcoin in USD using the CoinCap API.

    Returns:
        dict: The parsed JSON data from the API.

    Exits:
        If the API request fails.
    """
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
    except requests.RequestException:
        sys.exit("Error: Could not retrieve Bitcoin price from API.")
    return response.json()


def parse_json_for_cost(json_data):
    """
    Extract the Bitcoin price in USD from the CoinCap API response.

    Args:
        json_data (dict): The JSON data returned by the API.

    Returns:
        float: The current price of 1 Bitcoin in USD.
    """
    try:
        return float(json_data["data"]["priceUsd"])
    except (KeyError, TypeError, ValueError):
        sys.exit("Error: Unexpected format in API response.")


def print_output(amount):
    """
    Print the total cost formatted to 4 decimal places with commas.

    Args:
        amount (float): The calculated total cost in USD.
    """
    print(f"${amount:,.4f}")


def main():
    """
    Main program flow:
    - Read quantity of Bitcoin to buy from argv
    - Fetch current Bitcoin price
    - Calculate total cost
    - Print result
    """
    quantity = convert_argv_to_float()
    json_cost = get_json_for_bitcoin()
    cost = parse_json_for_cost(json_cost)
    print_output(quantity * cost)


# Run the program if this script is executed directly
if __name__ == "__main__":
    main()
