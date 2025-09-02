""" game.py
Author: TJ Tryon
Date: 2025-07-15

This program prompts the user to input an integer game level,
generates a random number between 1 and that level, and lets the
user repeatedly guess the number. It gives feedback for each guess
("Too large!", "Too small!", or "Just right!").

It uses the following module: random
"""

import random


def get_level():
    """
    Prompt the user for a positive integer game level.

    Returns:
        int: The level provided by the user.
    """
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
        except ValueError:
            pass


def get_guess():
    """
    Prompt the user for a positive integer guess.

    Returns:
        int: The user's guess.
    """
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                return guess
        except ValueError:
            pass


def get_random(level):
    """
    Generate a random number between 1 and the given level.

    Args:
        level (int): The maximum value.

    Returns:
        int: The randomly generated target number.
    """
    return random.randint(1, level)


def play_game(random_int):
    """
    Run the guessing loop: prompt user until they guess correctly.

    Args:
        random_int (int): The target number to guess.
    """
    while True:
        guess = get_guess()
        if guess > random_int:
            print("Too large!")
        elif guess < random_int:
            print("Too small!")
        else:
            print("Just right!")
            break


def main():
    """
    Main program flow:
    - Get game level
    - Generate random number
    - Run game loop with repeated guesses
    """
    level = get_level()
    target = get_random(level)
    play_game(target)


# Run the program if this script is executed directly
if __name__ == "__main__":
    main()
