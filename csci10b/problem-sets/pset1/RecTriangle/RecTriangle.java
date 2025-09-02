/**
 * RecTriangle.java
 * Author: TJ Tryon
 * Date: 2025-08-30
 * Course: CSCI 10b - Intermediate Computer Programming for Java II
 * Problem Set: PS1 - RecTriangle
 *
 * This program prints a reverse triangular pattern using recursion.
 *
 * Key concepts used:
 * - Recursion
 * - Method design
 * - Base cases
 * - Output formatting
 *
 * Input: Integer parameter representing the size of the largest triangle row
 * Output: Reverse triangular pattern printed to console using [] symbols
 */

public class RecTriangle {

    /**
     * The main method runs when the program starts.
     * It calls printTriangle with a hardcoded value as specified in the assignment.
     *
     * Note: The assignment specification explicitly requires printTriangle(4),
     * rather than dynamic input handling. An alternative implementation using
     * command line arguments is provided below but commented out to maintain
     * compliance with the problem set requirements.
     *
     * @param args Command line arguments (not used per assignment specifications)
     */
    public static void main(String[] args)
    {
        // Assignment-compliant implementation: hardcoded value as specified
        printTriangle(4);

        /*
         * In CS50x, we had a very similar project, except we used command line
         * arguement to get the "height". I would normally, I would implement
         * thi approach, but the specs on the pset1 said to use printTriangle(4).
         * In the event I misred the instructions, I wanted to include this portion,
         * though commented out.
         *
         * Alternative implementation with command line argument parsing:
         * This approach would provide greater flexibility and user interaction
         * by accepting runtime input validation and dynamic triangle sizing.
         *
         * Commented out to maintain adherence to Problem Set 2 specifications
         * which explicitly state to use printTriangle(4).
         *
        if (args.length > 0) {
            try {
                int size = Integer.parseInt(args[0]);
                if (size > 0) {
                    printTriangle(size);
                } else {
                    System.out.println("Error: Triangle size must be positive integer");
                }
            } catch (NumberFormatException e) {
                System.out.println("Error: Invalid integer format. Usage: java RecTriangle <size>");
            }
        } else {
            System.out.println("No arguments provided. Using default size of 4.");
            printTriangle(4);
        }
        */
    }

    /**
     * printTriangle prints a reverse triangular pattern using recursion.
     * It starts with s squares and decreases by one each row until reaching zero.
     *
     * @param s The number of squares to print on the current row
     */
    public static void printTriangle(int s)
    {
        if (s < 1)
            return;

        for (int i = 0; i < s; i++)
        {
            System.out.print("[]");
        }

        System.out.println();
        printTriangle(s - 1);
    }
}
