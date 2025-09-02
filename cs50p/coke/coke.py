""" coke.py
Author: TJ Tryon
Date: July 10, 2025

This program is a virtual coke machine change counting system. Cokes are $0.50.
It accepts coins (5, 10, or 25 cents) and returns any change over $0.50.
"""

price_of_coke = 50

def get_change():
    """
    Repeatedly prompts the user to insert coins until at least $0.50 (50 cents)
    has been inserted. Accepts only valid coin denominations: 5, 10, or 25 cents.

    Returns:
        int: The change owed to the user (0 if exact amount, or positive value if overpaid).
    """
    amount_due = price_of_coke

    while amount_due > 0:
        print(f"Amount due: {amount_due}")
        try:
            coin = int(input("Insert Coin (5, 10, 25): "))
            if coin in [5, 10, 25]:
                amount_due -= coin
            else:
                print("Invalid coin. Accepts only 5, 10, or 25 cents.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    return abs(amount_due)  # Always return a positive value (0 or change owed)


def give_change(change_owed):
    """
    Prints the amount of change to return to the user.

    Args:
        change_owed (int): The amount of change to return (in cents).
    """
    print(f"Change owed: {change_owed}")


def main():
    """
    Main program flow. Calls get_change() to collect coins,
    then give_change() to print the change (if any).
    """
    change_owed = get_change()
    give_change(change_owed)


# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
