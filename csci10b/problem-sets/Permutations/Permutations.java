/**
 * Permutations.java
 * Author: TJ Tryon
 * Date: 2025-08-30
 * Course: CSCI 10b - Intermediate Computer Programming for Java II
 * Problem Set: PS1 - Permutations
 *
 * This program generates and prints all possible permutations of a given string using recursion.
 * It demonstrates the divide-and-conquer approach where each character can be chosen as the first
 * character, and then all permutations of the remaining characters are recursively generated.
 *
 * The recursive strategy works by:
 * 1. For each character in the string, choose it as the first character
 * 2. Recursively generate all permutations of the remaining characters
 * 3. Combine the chosen first character with each permutation of the remaining characters
 *
 * For example, "ABC" has 6 permutations: ABC, ACB, BAC, BCA, CAB, CBA
 * "ABCD" has 24 permutations (4! = 4 factorial)
 *
 * Key concepts used:
 * - Pure recursion with base cases and recursive cases
 * - String manipulation and substring operations
 * - Combinatorial algorithms and factorial growth
 * - Helper method design with multiple parameters
 * - Backtracking algorithmic approach
 *
 * Input: String parameter passed to listPermutations method (hardcoded as "ABCD" per assignment
 * specs) Output: All permutations of the input string printed to console, one per line
 */

public class Permutations {

    /**
     * The main method demonstrates the listPermutations method as specified in the assignment.
     * It uses a hardcoded string "ABCD" to generate permutations as per the problem set
     * requirements.
     *
     * Alternative implementations for dynamic input handling (both command line arguments and
     * user prompting) are provided below but commented out to maintain compliance with the
     * assignment specifications which explicitly require using "ABCD".
     *
     * Command Line Arguments Approach:
     * This approach would allow users to pass a string as a command line argument when running
     * the program, providing flexibility for testing with different strings. Implementation
     * includes input validation, error handling for invalid arguments, and fallback behavior.
     * Usage example: java Permutations "XYZ" would generate permutations of "XYZ"
     *
     * User Prompting Approach:
     * This approach would interactively prompt the user to enter a string during program
     * execution using Scanner for input. This provides the most user-friendly experience
     * by allowing runtime string specification without requiring command line knowledge.
     * It includes input validation and handles edge cases like empty input.
     *
     * Both approaches are educationally valuable and demonstrate different input handling
     * techniques in Java, but are commented out to follow assignment requirements exactly.
     *
     * @param args Command line arguments (not used per assignment specifications)
     */
    public static void main(String[] args)
    {
        // Assignment-compliant implementation: use "ABCD" as specified
        System.out.println("Permutations of \"ABCD\" (as specified in assignment):");
        listPermutations("ABCD");

        /*
         * Alternative implementation with command line argument parsing:
         * This approach would provide greater flexibility by allowing users to specify
         * the string for permutation generation at runtime via command line arguments.
         * It includes comprehensive error handling, input validation, and fallback
         * behavior when no arguments are provided.
         *
         * Benefits: Flexible testing, no code modification needed for different inputs
         * Usage: java Permutations "XYZ" would generate permutations of "XYZ"
         *
         * Commented out to maintain adherence to Problem Set 1 specifications
         * which explicitly require using "ABCD".
         *
        import java.util.Scanner;

        if (args.length > 0) {
            // Use command line argument if provided
            String inputString = args[0].toUpperCase().trim();

            if (inputString.length() > 0) {
                System.out.println("Generating permutations of \"" + inputString + "\" from command
        line argument:"); listPermutations(inputString); System.out.println("Total: " +
        factorial(inputString.length()) + " permutations"); } else { System.out.println("Error:
        Empty string provided. Using default \"ABCD\"."); listPermutations("ABCD");
            }
        } else {
            // Alternative implementation with user prompting:
            // This approach would interactively ask the user for input using Scanner,
            // providing the most user-friendly experience by allowing runtime string
            // specification through console input with validation and error handling.
            //
            // Benefits: Interactive, user-friendly, handles invalid input gracefully
            // Implementation includes input validation and retry logic for robustness

            Scanner scanner = new Scanner(System.in);
            System.out.print("Enter a string to generate permutations (or press Enter for default
        \"ABCD\"): "); String userInput = scanner.nextLine().trim();

            if (userInput.length() > 0) {
                String inputString = userInput.toUpperCase();
                System.out.println("Generating permutations of \"" + inputString + "\":");
                listPermutations(inputString);
                System.out.println("Total: " + factorial(inputString.length()) + " permutations");
            } else {
                System.out.println("No input provided. Using default \"ABCD\":");
                listPermutations("ABCD");
                System.out.println("Total: 24 permutations");
            }

            scanner.close();
        }
        */
    }

    /*
     * Helper method for calculating factorial (used in commented alternative implementations)
     * This method would support the dynamic input approaches by calculating the expected
     * number of permutations for validation and user feedback purposes.
     *
     * @param n The number to calculate factorial for
     * @return n factorial (n!)
     *
    private static int factorial(int n) {
        if (n <= 1) return 1;
        return n * factorial(n - 1);
    }
    */

    /**
     * Generates and prints all permutations of the given string using recursion.
     * This is the main public interface method that delegates to the recursive helper method.
     *
     * The algorithm works by considering each character as a potential first character,
     * then recursively generating all permutations of the remaining characters.
     *
     * Time Complexity: O(n! * n) where n is the string length
     * Space Complexity: O(n) for the recursion call stack
     *
     * @param s The string to generate permutations for
     */
    public static void listPermutations(String s)
    {
        listPermutations("", s);
    }

    /**
     * Recursive helper method that generates permutations using a prefix and remaining characters.
     * This method implements the core recursive algorithm for permutation generation.
     *
     * Base case: When no characters remain, print the completed permutation (prefix)
     * Recursive case: For each remaining character, add it to prefix and recurse with remaining
     * chars
     *
     * The recursive strategy follows the hint from the assignment:
     * - Divide permutations into groups based on the first character
     * - Each group consists of that first character + all permutations of remaining characters
     * - For "ABCD": group A + perms("BCD"), group B + perms("ACD"), etc.
     *
     * @param prefix The characters chosen so far to build the current permutation
     * @param remaining The characters still available to be chosen
     */
    private static void listPermutations(String prefix, String remaining)
    {
        // Base case: no more characters to choose, print the completed permutation
        if (remaining.length() == 0)
        {
            System.out.println(prefix);
        }
        else
        {
            // Recursive case: try each remaining character as the next choice
            for (int i = 0; i < remaining.length(); i++)
            {
                // Choose the character at position i
                char chosenChar = remaining.charAt(i);

                // Create new prefix by adding the chosen character
                String newPrefix = prefix + chosenChar;

                // Create new remaining string by removing the chosen character
                String newRemaining = remaining.substring(0, i) + remaining.substring(i + 1);

                // Recursively generate permutations with the new prefix and remaining characters
                listPermutations(newPrefix, newRemaining);
            }
        }
    }
}
