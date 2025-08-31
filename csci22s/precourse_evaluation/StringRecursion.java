/**
 * StringRecursion.java
 * Author: TJ Tryon
 * Date: 2025-08-29
 * Course: CSCI 22e - Data Structures
 * Problem Set: PS0 - Precourse Evaluation
 *
 * This program demonstrates recursive string manipulation techniques.
 * It includes methods for printing strings with spaces between characters
 * and weaving two strings together character by character.
 *
 * Data structures used:
 * - Strings (immutable character sequences)
 * - Recursive call stack (implicit data structure)
 *
 * Key algorithms:
 * - String recursion with base cases and recursive cases
 * - Character-by-character string processing
 * - String concatenation and manipulation
 *
 * Input: Strings for processing via recursive methods
 * Output: Formatted string output and woven string results
 */

public class StringRecursion
{
    /**
     * printWithSpaces prints the characters of a string separated by spaces.
     * Uses recursion to process each character individually.
     *
     * @param str The string to print with spaces (can be null or empty)
     */
    public static void printWithSpaces(String str)
    {
        // Base cases: null or empty string
        if (str == null || str.equals(""))
        {
            System.out.println();
            return;
        }

        // Base case: single character
        if (str.length() == 1)
        {
            System.out.print(str.charAt(0) + " ");
            return;
        }

        // Recursive case: print first character with space, then recurse
        System.out.print(str.charAt(0) + " ");
        printWithSpaces(str.substring(1));
    }

    /**
     * weave combines two strings by alternating their characters.
     * If one string is longer, its remaining characters are appended.
     *
     * @param str1 The first string to weave (cannot be null)
     * @param str2 The second string to weave (cannot be null)
     * @return A new string with characters woven together
     * @throws IllegalArgumentException if either parameter is null
     */
    public static String weave(String str1, String str2)
    {
        // Check for null parameters
        if (str1 == null || str2 == null)
        {
            throw new IllegalArgumentException("Neither string can be null");
        }

        // Base case: both strings are empty
        if (str1.equals("") && str2.equals(""))
        {
            return "";
        }

        // Base case: str1 is empty, return str2
        if (str1.equals(""))
        {
            return str2;
        }

        // Base case: str2 is empty, return str1
        if (str2.equals(""))
        {
            return str1;
        }

        // Recursive case: take first character from each string and weave the rest
        return str1.charAt(0) + "" + str2.charAt(0) + 
               weave(str1.substring(1), str2.substring(1));
    }

    /**
     * The main method runs when the program starts.
     * It tests both recursive methods with various input cases
     * to demonstrate their functionality.
     *
     * @param args Command line arguments (not used in this program)
     */
    public static void main(String[] args)
    {
        System.out.println("Testing printWithSpaces method:");
        System.out.println("================================");

        System.out.print("printWithSpaces(\"space\"): ");
        printWithSpaces("space");
        System.out.println();

        System.out.print("printWithSpaces(\"hello\"): ");
        printWithSpaces("hello");
        System.out.println();

        System.out.print("printWithSpaces(\"a\"): ");
        printWithSpaces("a");
        System.out.println();

        System.out.print("printWithSpaces(\"\"): ");
        printWithSpaces("");

        System.out.print("printWithSpaces(null): ");
        printWithSpaces(null);

        System.out.println("\nTesting weave method:");
        System.out.println("=====================");

        System.out.println("weave(\"aaaa\", \"bbbb\"): " + weave("aaaa", "bbbb"));
        System.out.println("weave(\"hello\", \"world\"): " + weave("hello", "world"));
        System.out.println("weave(\"recurse\", \"NOW\"): " + weave("recurse", "NOW"));
        System.out.println("weave(\"hello\", \"\"): " + weave("hello", ""));
        System.out.println("weave(\"\", \"world\"): " + weave("", "world"));
        System.out.println("weave(\"\", \"\"): " + weave("", ""));

        // Test exception case
        System.out.println("\nTesting null parameter exception:");
        try
        {
            weave(null, "test");
            System.out.println("ERROR: Exception should have been thrown!");
        } catch (IllegalArgumentException e)
        {
            System.out.println("Correctly threw exception for null parameter");
        }
    }
}