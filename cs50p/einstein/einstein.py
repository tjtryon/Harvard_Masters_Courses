""" einstein.py
Author: TJ Tryon
Date: July 7, 2025

This program converts input mass in kg to energy in Joules using
Einstein's energy-mass equivalence equation, E = mc².
"""

# Speed of light in meters per second
speed_of_light = 3 * (10 ** 8)


def convert_mass_to_energy(mass):
    """Convert the input mass into energy using Einstein's equation."""
    return mass * (speed_of_light ** 2)


def get_mass_input():
    """Prompt the user for a valid non-negative mass input."""
    while True:
        try:
            mass = float(input("Enter the mass, in kg, to be converted to Joules: "))
            if mass < 0:
                print("Mass cannot be negative. Please enter a non-negative number.")
            else:
                return mass
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    """Main program flow."""
    mass = get_mass_input()
    energy = convert_mass_to_energy(mass)
    print(f"Energy (E) = {int(energy)} Joules")


# Call the main function
if __name__ == "__main__":
    main()
