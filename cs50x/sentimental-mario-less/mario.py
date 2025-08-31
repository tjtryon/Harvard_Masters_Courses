from cs50 import get_int

# Ask user how high of a pyrimad
while True:
    height = get_int("Height: ")

    # Check to see if height is between 1 and 8
    if height > 0 and height <= 8:
        break

# Check for valid input
if height < 1 or height > 8:
    print("Expected integer")
    exit(1)

else:
    # Increment the rows to the next row
    for row in range(height):

        # Print the empty blocks before the #
        # Total number is height - row #
        for space in range(height - (row + 1)):
            print(" ", end="")

        # Print the full blocks
        # Total number is the row #
        for block in range(row + 1):
            print("#", end="")

        print()
