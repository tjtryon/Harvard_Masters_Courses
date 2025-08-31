""" nutrition.py
Author: TJ Tryon
Date: July 12, 2025

This program prompts the user to input a fruit and returns its calorie count
based on a predefined dictionary of common fruits.
"""

import string

# Dictionary of fruits and their calories (based on USDA average per serving)
fruits = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberry": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80
}


def get_fruit():
    """
    Prompts the user for a fruit name and validates the input.

    Returns:
        str: A valid fruit name (lowercased), or None if input is invalid.
    """
    user_input = input("Item: ").strip().lower()

    # Check if input is alphabetic or contains only spaces
    if not all(c.isalpha() or c.isspace() for c in user_input):
        print("Invalid input. Only letters and spaces allowed.")
        return None

    # Check if the fruit exists in our list
    if user_input not in fruits:
        print("")
        return Nonee


    return user_input


def get_calories(fruit):
    """
    Looks up the fruit in the dictionary and returns the calorie count.

    Args:
        fruit (str): Name of the fruit.

    Returns:
        int: The number of calories.
    """
    return fruits.get(fruit)


def print_calories(calories):
    """
    Prints the calories for the given fruit.

    Args:
        calories (int): Calorie count of the fruit.
    """
    print(f"Calories: {calories}")


def main():
    """
    Main program flow:
    - Gets fruit input from the user.
    - Validates the input.
    - If valid, prints its calorie content.
    """
    fruit = get_fruit()
    if fruit is not None:
        calories = get_calories(fruit)
        print_calories(calories)


# Run the program if this file is executed directly
if __name__ == "__main__":
    main()
