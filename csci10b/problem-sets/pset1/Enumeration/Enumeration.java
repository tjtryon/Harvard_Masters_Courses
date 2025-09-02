/**
 * Enumeration.java
 * Author: TJ Tryon
 * Date: 2025-08-30
 * Course: CSCI 10b - Intermediate Computer Programming for Java II
 * Problem Set: PS1 - Enumeration
 *
 * This program prints out how many days are in each of the 12 months for a given year.
 *
 * Key concepts used:
 * - Enumerations (enum)
 * - Switch statements
 * - Leap year calculation
 * - Enhanced for loops
 *
 * Input: Year as integer parameter to daysInMonth method
 * Output: Number of days in each month for the specified year
 */

enum Months { JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC }

class Enumeration {

    /**
     * The main method runs when the program starts.
     * It iterates through all months and displays the days for year 2023 as specified
     * in the assignment requirements.
     *
     * Note: While a more robust implementation would accept command line arguments
     * for dynamic year input, the assignment specification requires displaying
     * results for year 2023. An alternative implementation using command line
     * arguments is provided below but commented out to maintain compliance.
     *
     * @param args Command line arguments (not used per assignment specifications)
     */
    public static void main(String[] args)
    {
        // Assignment-compliant implementation: hardcoded year 2023 as specified
        for (Months m : Months.values())
        {
            System.out.println(m + " 2023 has " + daysInMonth(m, 2023) + " days!");
        }

        /*
         * In any such program, I would be asking the user for the year to use for
         * the program logic. As the pset1 specifications do not have this as a feature
         * I have both implemented it, as well as commented it out, but as a programmer,
         * I would be remiss not to point this important detail and add the features
         * that can easily be made available for a production type of program, which
         * would allow for more easy unit tests, as well as program flexibility.
         * Alternative implementation with command line argument parsing:
         * This approach would provide greater flexibility by allowing users to
         * check any year for leap year calculations and month day counts.
         *
         * Commented out to maintain adherence to assignment specifications
         * which explicitly require displaying results for year 2023.
         *
        int year = 2023; // Default year if no argument provided

        if (args.length > 0) {
            try {
                year = Integer.parseInt(args[0]);
                if (year <= 0) {
                    System.out.println("Error: Year must be a positive integer");
                    return;
                }
            } catch (NumberFormatException e) {
                System.out.println("Error: Invalid year format. Usage: java Enumeration <year>");
                System.out.println("Using default year 2023");
            }
        }

        for (Months m : Months.values()) {
            System.out.println(m + " " + year + " has " + daysInMonth(m, year) + " days!");
        }
        */
    }

    /**
     * daysInMonth calculates the number of days in a given month for a specific year.
     * Handles leap year logic for February using the Gregorian calendar rules.
     *
     * @param m The month as an enum value (JAN through DEC)
     * @param year The year to calculate days for (any positive integer)
     * @return The number of days in the specified month and year
     */
    public static int daysInMonth(Months m, int year)
    {
        switch (m)
        {
            // Months with 31 days: January, March, May, July, August, October, December
            case JAN:
            case MAR:
            case MAY:
            case JUL:
            case AUG:
            case OCT:
            case DEC:
                return 31;

            // Months with 30 days: April, June, September, November
            case APR:
            case JUN:
            case SEP:
            case NOV:
                return 30;

            // February: depends on leap year calculation
            case FEB:
                /*
                 * Leap Year Rules (Gregorian Calendar):
                 * 1. If year is divisible by 4 → leap year
                 * 2. EXCEPT if year is divisible by 100 → not leap year
                 * 3. EXCEPT if year is divisible by 400 → leap year
                 *
                 * Examples:
                 * - 2024: divisible by 4, not by 100 → 29 days
                 * - 2100: divisible by 100, not by 400 → 28 days
                 * - 2000: divisible by 400 → 29 days
                 * - 2023: not divisible by 4 → 28 days
                 */
                if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0))
                {
                    return 29; // Leap year
                }
                else
                {
                    return 28; // Regular year
                }

            default:
                return 0; // Should never reach here with valid enum values
        }
    }
}
