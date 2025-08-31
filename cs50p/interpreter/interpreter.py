""" interpreter.py
Author: TJ Tryon
Date: July 10, 2025

This program accepts a mathematical expression in the format of
x y z where x and z are numbers (integer or float, positive or negative),
and y is a mathematical operator (+, -, *, /, %, **).
The program interprets this expression and outputs the answer as a float.
"""


def get_expression():
    """
    Prompts the user for a mathematical expression and splits it into components.

    Returns:
        tuple: (float, str, float) representing the first number, the operator, and the second number.
    """
    expression = input("Input a mathematical expression (e.g., -3.5 ** 2): ")

    # Split only on the first two spaces to correctly handle negative numbers and multi-character operators
    parts = expression.strip().split(" ", 2)

    if len(parts) != 3:
        raise ValueError("Invalid input format. Please use: number operator number")

    x_str, operator, z_str = parts

    return float(x_str), operator, float(z_str)


def compute_expression(num1, operator, num2):
    """
    Computes the result of the mathematical expression.

    Args:
        num1 (float): First number.
        operator (str): Mathematical operator (+, -, *, /, %, **).
        num2 (float): Second number.

    Returns:
        float: Result of the calculation.
    """
    match operator:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2
        case "%":
            return num1 % num2
        case "**":
            return num1 ** num2
        case _:
            raise ValueError(f"Unsupported operator: {operator}")


def main():
    """
    Main program logic:
    - Gets a mathematical expression from the user.
    - Computes and prints the result as a float.
    """
    try:
        num1, operator, num2 = get_expression()
        answer = compute_expression(num1, operator, num2)
        print(f"{answer:.1f}")  # Print result rounded to 1 decimal places
    except Exception as e:
        print(f"Error: {e}")


# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
