/**
 * RecursivePrint.java
 * Author: TJ Tryon
 * Date: 2025-08-30
 * Course: CSCI 10b - Intermediate Computer Programming for Java II
 * Problem Set: PS1 - RecursivePrint
 *
 * This program converts integers to their English word representation using pure recursion.
 * It can handle numbers from negative Integer.MAX_VALUE to positive Integer.MAX_VALUE,
 * including zero and all values up to 2.1 billion (extra credit implementation).
 *
 * The recursive algorithm breaks down large numbers into manageable chunks (billions,
 * millions, thousands, hundreds) and recursively converts each part, then combines
 * them with appropriate English scale words.
 *
 * Key concepts used:
 * - Pure recursive problem decomposition with base cases and recursive cases
 * - String manipulation and concatenation
 * - Integer division and modular arithmetic for digit extraction
 * - Array indexing for word lookup tables
 * - Negative number handling and edge case management
 * - Method overloading for internal helper methods
 *
 * EXTRA CREDIT: This implementation supports the full range of 32-bit integers
 * (up to Integer.MAX_VALUE = 2,147,483,647) for 2 additional points.
 *
 * Input: Integer values via command line arguments or interactive user input
 * Output: English word representation of numbers printed to console
 *
 * Usage:
 * - java RecursivePrint 143          (command line argument)
 * - java RecursivePrint             (prompts for user input)
 *
 * Examples:
 * - printNumber(143) outputs "one hundred forty three"
 * - printNumber(-24549) outputs "minus twenty four thousand five hundred forty nine"
 * - printNumber(2147483647) outputs "two billion one hundred forty seven million four hundred
 * eighty three thousand six hundred forty seven"
 */

import java.util.Scanner;

public class RecursivePrint {

    // Arrays for word lookup - used by recursive methods for efficient string building
    private static final String[] ONES = {
        "",         "one",     "two",     "three",     "four",     "five",    "six",
        "seven",    "eight",   "nine",    "ten",       "eleven",   "twelve",  "thirteen",
        "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"};

    private static final String[] TENS = {"",      "",      "twenty",  "thirty", "forty",
                                          "fifty", "sixty", "seventy", "eighty", "ninety"};

    /**
     * The main method handles command line arguments or prompts for user input.
     * It can run in two modes:
     * 1. Command line argument: java RecursivePrint 143
     * 2. Interactive mode: java RecursivePrint (prompts user for input)
     *
     * @param args Command line arguments - integer to convert
     */
    public static void main(String[] args)
    {
        System.out.println("RecursivePrint - Converting Numbers to English Words");
        System.out.println("==================================================");
        System.out.println();

        // Check if command line argument provided
        if (args.length > 0)
        {
            // Try to parse command line argument as integer
            try
            {
                int number = Integer.parseInt(args[0]);
                System.out.println("Command line input: " + number);
                System.out.print("Result: ");
                printNumber(number);
                System.out.println();
            } catch (NumberFormatException e)
            {
                System.out.println("Error: '" + args[0] + "' is not a valid integer.");
                System.out.println("Usage: java RecursivePrint [integer]");
                System.out.println("Examples:");
                System.out.println("  java RecursivePrint 143");
                System.out.println("  java RecursivePrint -24549");
                System.out.println("  java RecursivePrint");
            }
        }
        else
        {
            // No command line arguments - prompt for user input
            promptForUserInput();
        }
    }

    /**
     * Prompts the user to enter an integer and validates the input.
     * Continues prompting until a valid integer is entered.
     */
    private static void promptForUserInput()
    {
        Scanner scanner = new Scanner(System.in);

        while (true)
        {
            System.out.print("Please enter an integer to convert to words: ");
            String input = scanner.nextLine().trim();

            if (input.isEmpty())
            {
                System.out.println("Error: No input provided. Please enter a valid integer.");
                continue;
            }

            try
            {
                int number = Integer.parseInt(input);
                System.out.println("You entered: " + number);
                System.out.print("Result: ");
                printNumber(number);
                System.out.println();
                break;
            } catch (NumberFormatException e)
            {
                System.out.println("Error: '" + input + "' is not a valid integer.");
                System.out.println("Please enter a whole number (e.g., 143, -24549, 0).");
                System.out.println();
            }
        }

        scanner.close();
    }

    /**
     * Converts an integer to its English word representation and prints it.
     * This is the main public interface method that handles negative numbers
     * and delegates to the recursive helper method.
     *
     * Uses pure recursion to break down numbers into constituent parts and
     * convert each part to words. Supports the full range of 32-bit integers.
     *
     * @param n The integer to convert to words (any value from Integer.MIN_VALUE to
     *     Integer.MAX_VALUE)
     */
    public static void printNumber(int n)
    {
        if (n == 0)
        {
            System.out.print("zero");
            return;
        }

        if (n < 0)
        {
            System.out.print("minus ");
            // Handle Integer.MIN_VALUE overflow issue
            if (n == Integer.MIN_VALUE)
            {
                // Integer.MIN_VALUE = -2,147,483,648
                // Converting to positive would overflow, so handle specially
                printNumberRecursive(2147483648L);
            }
            else
            {
                printNumberRecursive(-n);
            }
        }
        else
        {
            printNumberRecursive(n);
        }
    }

    /**
     * Recursive helper method that converts positive numbers to English words.
     * This method implements the core recursive algorithm by breaking numbers
     * into billions, millions, thousands, and hundreds place values.
     *
     * Base case: Numbers 0-19 are handled directly from lookup array
     * Recursive cases: Numbers are divided by scale (billion, million, etc.)
     * and recursively processed for each significant digit group.
     *
     * @param n The positive number to convert (including support for long to handle
     *     Integer.MIN_VALUE)
     */
    private static void printNumberRecursive(long n)
    {
        if (n == 0)
        {
            return; // Base case for recursive calls
        }

        if (n < 20)
        {
            // Base case: direct lookup for 0-19
            System.out.print(ONES[(int) n]);
        }
        else if (n < 100)
        {
            // Tens place (20-99)
            System.out.print(TENS[(int) (n / 10)]);
            if (n % 10 != 0)
            {
                System.out.print(" ");
                printNumberRecursive(n % 10);
            }
        }
        else if (n < 1000)
        {
            // Hundreds place (100-999)
            printNumberRecursive(n / 100);
            System.out.print(" hundred");
            if (n % 100 != 0)
            {
                System.out.print(" ");
                printNumberRecursive(n % 100);
            }
        }
        else if (n < 1000000)
        {
            // Thousands place (1,000-999,999)
            printNumberRecursive(n / 1000);
            System.out.print(" thousand");
            if (n % 1000 != 0)
            {
                System.out.print(" ");
                printNumberRecursive(n % 1000);
            }
        }
        else if (n < 1000000000L)
        {
            // Millions place (1,000,000-999,999,999)
            printNumberRecursive(n / 1000000);
            System.out.print(" million");
            if (n % 1000000 != 0)
            {
                System.out.print(" ");
                printNumberRecursive(n % 1000000);
            }
        }
        else
        {
            // Billions place (1,000,000,000 and up)
            // This handles up to 2,147,483,647 (Integer.MAX_VALUE)
            printNumberRecursive(n / 1000000000L);
            System.out.print(" billion");
            if (n % 1000000000L != 0)
            {
                System.out.print(" ");
                printNumberRecursive(n % 1000000000L);
            }
        }
    }
}
