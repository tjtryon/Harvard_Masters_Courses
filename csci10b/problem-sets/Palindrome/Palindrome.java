/**
 * Palindrome.java
 * Author: TJ Tryon
 * Date: 2025-08-30
 * Course: CSCI 10b - Intermediate Computer Programming for Java II
 * Problem Set: PS1 - Palindrome
 *
 * This program determines whether a sentence is a palindrome using recursive techniques.
 * It ignores punctuation, spaces, and case differences when checking for palindromes.
 * The recursive algorithm follows the divide-and-conquer approach: compare first and last
 * alphanumeric characters, then recursively check the substring between them.
 *
 * ALTERNATIVE INPUT METHODS:
 * While the assignment specifies Scanner input, in production environments I would
 * typically implement command line argument processing for better automation and
 * testing capabilities. An alternative implementation using argv is included but
 * commented out to maintain strict compliance with assignment specifications.
 *
 * Command line arguments would provide several advantages:
 * - Batch processing capabilities for automated testing
 * - Integration with shell scripts and continuous integration systems
 * - Faster execution without interactive prompts
 * - Better suited for unit testing frameworks
 *
 * Key concepts used:
 * - Recursion with base cases and recursive cases
 * - String manipulation and character analysis
 * - Character class methods (isLetterOrDigit)
 * - Case conversion and string preprocessing
 * - User input with Scanner class
 * - Alternative: Command line argument processing (commented)
 *
 * Input: A string from the user via keyboard input (Scanner-based as per specs)
 * Output: Whether the string is a palindrome (true/false) and confirmation message
 */

import java.util.Scanner;

public class Palindrome {

    /**
     * The main method runs when the program starts.
     * It prompts the user for a string, converts it to lowercase for consistency,
     * then calls isPalindrome to check if it's a palindrome.
     *
     * Note: While the assignment specifies Scanner input, in production environments
     * I would normally implement command line argument processing for better automation,
     * testing capabilities, and integration with other systems. An alternative
     * implementation using argv is provided below but commented out to maintain
     * compliance with assignment specifications.
     *
     * @param args Command line arguments (not used per assignment specifications)
     */
    public static void main(String[] args)
    {
        // Assignment-compliant implementation: Scanner-based user input
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a sentence to check if it's a palindrome: ");
        String input = scanner.nextLine();

        // Convert to lowercase as allowed by the assignment
        String processedInput = input.toLowerCase();

        boolean result = isPalindrome(processedInput);

        System.out.println("\n\"" + input + "\"");
        if (result)
        {
            System.out.println("IS a palindrome!");
        }
        else
        {
            System.out.println("is NOT a palindrome.");
        }

        scanner.close();

        /*
         * In production code, I would implement command line argument processing
         * for better automation and testing capabilities. This approach provides
         * several significant advantages over interactive input:
         *
         * 1. Automation: Can be easily integrated into build scripts and CI/CD pipelines
         * 2. Batch Processing: Can test multiple palindromes without user interaction
         * 3. Performance: No waiting for user input, faster execution
         * 4. Testing: Unit tests can call the program programmatically
         * 5. Scripting: Shell scripts can pass arguments directly
         *
         * Alternative implementation with command line argument processing:
         * Usage: java Palindrome "sentence to check"
         * Example: java Palindrome "A man, a plan, a canal: Panama"
         *
         * This implementation is commented out to maintain strict adherence to
         * assignment specifications which require Scanner-based user input.
         *
        if (args.length > 0) {
            // Process all command line arguments as separate palindrome checks
            for (int i = 0; i < args.length; i++) {
                String input = args[i];
                String processedInput = input.toLowerCase();
                boolean result = isPalindrome(processedInput);

                System.out.println("Test " + (i + 1) + ": \"" + input + "\"");
                if (result) {
                    System.out.println("IS a palindrome!");
                } else {
                    System.out.println("is NOT a palindrome.");
                }
                System.out.println(); // Blank line between results
            }
        } else {
            // Fallback to interactive mode if no arguments provided
            System.out.println("No command line arguments provided.");
            System.out.println("Usage: java Palindrome \"sentence to check\"");
            System.out.println("Example: java Palindrome \"madam\" \"hello\" \"A man, a plan, a
        canal: Panama\""); System.out.println(); System.out.println("Falling back to interactive
        mode...");

            Scanner scanner = new Scanner(System.in);
            System.out.print("Enter a sentence to check if it's a palindrome: ");
            String input = scanner.nextLine();

            String processedInput = input.toLowerCase();
            boolean result = isPalindrome(processedInput);

            System.out.println("\n\"" + input + "\"");
            if (result) {
                System.out.println("IS a palindrome!");
            } else {
                System.out.println("is NOT a palindrome.");
            }

            scanner.close();
        }
        */
    }

    /**
     * isPalindrome determines whether a string is a palindrome using pure recursion.
     * It ignores punctuation and spaces, considering only alphanumeric characters.
     * This implementation uses NO loops - only recursion as required by the assignment.
     *
     * Base case: If string length <= 1, it's a palindrome
     * Recursive case: Skip non-alphanumeric characters recursively, compare first/last, recurse on
     * middle
     *
     * @param s The string to check for palindrome properties
     * @return true if the string is a palindrome, false otherwise
     */
    public static boolean isPalindrome(String s)
    {
        // Base case: strings of length 0 or 1 are palindromes
        if (s.length() <= 1)
        {
            return true;
        }

        // If first character is not alphanumeric, skip it recursively
        if (!Character.isLetterOrDigit(s.charAt(0)))
        {
            return isPalindrome(s.substring(1));
        }

        // If last character is not alphanumeric, skip it recursively
        if (!Character.isLetterOrDigit(s.charAt(s.length() - 1)))
        {
            return isPalindrome(s.substring(0, s.length() - 1));
        }

        // Both first and last characters are alphanumeric - compare them
        if (s.charAt(0) != s.charAt(s.length() - 1))
        {
            return false;
        }

        // First and last match - recursively check the middle substring
        return isPalindrome(s.substring(1, s.length() - 1));
    }

    /*
     * Alternative simple isPalindrome for testing basic cases without punctuation:
     * This version would work for simple cases like "madam" or "12321"
     *
     * public static boolean isPalindromeSimple(String s) {
     *     // Base case
     *     if (s.length() <= 1) {
     *         return true;
     *     }
     *
     *     // Compare first and last characters
     *     if (s.charAt(0) != s.charAt(s.length() - 1)) {
     *         return false;
     *     }
     *
     *     // Recursive case: check substring excluding first and last characters
     *     return isPalindromeSimple(s.substring(1, s.length() - 1));
     * }
     */
}
