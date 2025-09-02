""" professor.py
Author: TJ Tryon
Date: 2025-07-15

This program prompts the user to choose a difficulty level (1–3),
generates 10 random math problems, and quizzes the user with up to
3 tries per question. It gives feedback and shows the final score.

Uses: random
"""

import random

num_problems = 10
max_tries = 3


def generate_integer(level):
    """
    Generate a random integer based on difficulty level.

    Args:
        level (int): The difficulty level (1, 2, or 3)

    Returns:
        int: A random integer within the appropriate range
    """
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Level must be 1, 2, or 3")


def get_level():
    """
    Prompt the user for a difficulty level (1–3).

    Returns:
        int: The validated difficulty level.
    """
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
        except ValueError:
            pass


def create_problem_list(level):
    """
    Create 10 random addition problems based on level.

    Args:
        level (int): The difficulty level (1–3).

    Returns:
        list: A list of 10 tuples (a, b).
    """
    problems = []
    for _ in range(num_problems):
        a = generate_integer(level)
        b = generate_integer(level)
        problems.append((a, b))
    return problems


def answer_problems(problems):
    """
    Ask user each problem. Allow up to 3 tries. Give feedback. Track score.

    Args:
        problems (list): A list of 10 (a, b) tuples.
    """
    score = 0
    for a, b in problems:
        for attempt in range(max_tries):
            try:
                guess = int(input(f"{a} + {b} = "))
                if guess == a + b:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
        else:
            print(f"{a} + {b} = {a + b}")
    print(f"Score: {score}")


def main():
    """
    Main program flow:
    - Ask for level
    - Generate problems
    - Run quiz and show score
    """
    level = get_level()
    problems = create_problem_list(level)
    answer_problems(problems)


# Run the program if this script is executed directly
if __name__ == "__main__":
    main()
