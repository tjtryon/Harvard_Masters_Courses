from cs50 import get_float

DOLLAR = 100
QUARTER = 25
DIME = 10
NICKEL = 5
PENNY = 1

# Function to prompt for change owed


def prompt_for_change_owed():
    while True:
        change_owed = get_float("Changed owed: ")

        # Check to see if input is valid
        if change_owed > 0:
            return change_owed


# Function to prompt for the number of coins in the change owed
def calculate_coins_needed(change_in_cents):

    # Treat coins as integers, convert dollars and cents
    change_in_cents *= DOLLAR

    coins = 0

    # Do this until there is no more change owed
    # If change_owed > 1, we can still take coins from it
    while change_in_cents >= PENNY:

        # Count quarters
        quarters = int(change_in_cents / QUARTER)

        # Remove quarters from change owed
        change_in_cents -= QUARTER * quarters

        # Count dimes
        dimes = int(change_in_cents / DIME)

        # Remove dimes from change owed
        change_in_cents -= DIME * dimes

        # Count nickels
        nickels = int((change_in_cents / NICKEL))

        # Remove nickles from change owed
        change_in_cents -= NICKEL * nickels

        # Count pennies
        pennies = int((change_in_cents / PENNY))

        # Remove pennies from change owed
        change_in_cents -= PENNY * pennies

    coins = quarters + dimes + nickels + pennies

    return coins


# Print the number of coins in the change owed
def display_coins(coins):
    print(f"{coins}")


# Main function calls the working functions
def main():
    # Get input for change owed
    change_owed = prompt_for_change_owed()

    # Call function to calculte how many coins of what denomination
    coins = calculate_coins_needed(change_owed)

    # Calls the function to print the results
    display_coins(coins)


# Calls the main function to start the program
main()
