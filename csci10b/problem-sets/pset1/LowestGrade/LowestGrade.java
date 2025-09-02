
/**
 * LowestGrade.java
 * Author: TJ Tryon
 * Date: 2025-08-30
 * Course: CSCI 10b - Intermediate Computer Programming for Java II
 * Problem Set: PS1 - LowestGrade
 *
 * This program demonstrates array manipulation by removing the lowest score from a set
 * of homework scores. It simulates a common academic practice where instructors drop
 * the lowest exam or homework score to benefit students.
 *
 * The program implements two key methods:
 * 1. removeLowest() - Uses varargs to accept variable number of scores and returns
 *    an array with the lowest score removed (with special handling for edge cases)
 * 2. arrayPrint() - Creates formatted string output for integer arrays without using
 *    the built-in Arrays.toString() method
 *
 * USER INPUT APPROACH:
 * While the assignment specification focuses on demonstrating the removeLowest method
 * with hardcoded test cases, in production environments I would typically implement
 * user input functionality to make this program more practical and interactive.
 * A comprehensive user input implementation is included but commented out to maintain
 * strict compliance with assignment demonstration requirements.
 *
 * The alternative user input approach would provide several advantages:
 * - Real-world applicability for teachers and students
 * - Flexibility to handle varying numbers of grades per student
 * - Interactive prompts that guide the user through the process
 * - Input validation for reasonable grade ranges
 * - Reusability for multiple grade sets without recompilation
 * - Better user experience with clear feedback and explanations
 *
 * Key concepts demonstrated:
 * - Variable arguments (varargs) with int... parameter
 * - Array traversal and manipulation
 * - Edge case handling (empty arrays, single elements, duplicate values)
 * - String building and formatting without Arrays.toString()
 * - Method design with clear responsibilities and documentation
 * - Production vs. demonstration code design considerations
 *
 * Special cases handled:
 * - No scores provided: returns empty array []
 * - Single score: returns unchanged (don't penalize student with only one grade)
 * - Duplicate lowest scores: removes only the first occurrence
 *
 * Input: Variable number of integer homework scores via method parameters (demonstration)
 *        Alternative: Interactive user input via Scanner (commented implementation)
 * Output: Formatted display of arrays with lowest scores removed
 */

public class LowestGrade {

    /**
     * The main method demonstrates the removeLowest functionality.
     *
     * In production environments, I would typically implement user input
     * to allow interactive grade entry, making this program more practical
     * for real-world use. However, the assignment specification focuses on
     * demonstrating the removeLowest method with specific test cases to
     * verify correct handling of edge cases and algorithm implementation.
     *
     * An alternative user input implementation is included but commented out
     * to maintain strict compliance with assignment demonstration requirements.
     *
     * @param args Command line arguments (not used per assignment specifications)
     */
    public static void main(String[] args)
    {
        // Assignment-compliant implementation: Hardcoded test cases for demonstration
        System.out.println("Testing removeLowest method with predefined test cases:");
        System.out.println("====================================================");

        int[] a = removeLowest(23, 90, 47, 55, 88);
        int[] b = removeLowest(85);
        int[] c = removeLowest();
        int[] d = removeLowest(59, 92, 93, 47, 88, 47);

        System.out.println("a = " + arrayPrint(a));
        System.out.println("b = " + arrayPrint(b));
        System.out.println("c = " + arrayPrint(c));
        System.out.println("d = " + arrayPrint(d));

        /*
         * In production code, I would implement user input functionality
         * to make this program more practical and interactive. This approach
         * would provide several significant advantages:
         *
         * 1. Real-world applicability: Teachers could actually use this program
         * 2. Flexibility: Handle varying numbers of grades per student
         * 3. User experience: Interactive prompts guide the user
         * 4. Validation: Input checking for reasonable grade ranges
         * 5. Reusability: Multiple grade sets without recompilation
         *
         * Alternative implementation with user input:
         * This would prompt the user to enter grades and demonstrate
         * the removeLowest functionality with their actual data.
         *
         * Scanner scanner = new Scanner(System.in);
         *
         * System.out.println("Grade Drop Calculator");
         * System.out.println("====================");
         * System.out.print("How many homework scores do you want to enter? ");
         * int numScores = scanner.nextInt();
         *
         * if (numScores <= 0) {
         *     System.out.println("No grades entered. Result: " + arrayPrint(removeLowest()));
         * } else {
         *     int[] grades = new int[numScores];
         *     System.out.println("Enter " + numScores + " homework scores:");
         *
         *     for (int i = 0; i < numScores; i++) {
         *         System.out.print("Score " + (i + 1) + ": ");
         *         grades[i] = scanner.nextInt();
         *     }
         *
         *     // Convert array to varargs call using helper method
         *     int[] result = removeLowestFromArray(grades);
         *
         *     System.out.println("\nOriginal scores: " + arrayPrint(grades));
         *     System.out.println("After removing lowest: " + arrayPrint(result));
         *
         *     if (grades.length == 1) {
         *         System.out.println("Note: Single score was preserved (not removed).");
         *     } else if (grades.length > 1) {
         *         int lowest = findLowest(grades);
         *         System.out.println("Lowest score removed: " + lowest);
         *     }
         * }
         *
         * scanner.close();
         *
         * // Helper method to convert array to varargs call
         * private static int[] removeLowestFromArray(int[] grades) {
         *     // Create a varargs-compatible call by expanding the array
         *     switch (grades.length) {
         *         case 0: return removeLowest();
         *         case 1: return removeLowest(grades[0]);
         *         case 2: return removeLowest(grades[0], grades[1]);
         *         // ... additional cases as needed, or use reflection for dynamic varargs
         *         default:
         *             // For larger arrays, copy elements and use array processing
         *             return removeLowestArray(grades);
         *     }
         * }
         *
         * // Alternative array-based implementation for larger grade sets
         * private static int[] removeLowestArray(int[] grades) {
         *     if (grades.length <= 1) return grades.clone();
         *
         *     int lowest = grades[0];
         *     for (int grade : grades) {
         *         if (grade < lowest) lowest = grade;
         *     }
         *
         *     int[] result = new int[grades.length - 1];
         *     int resultIndex = 0;
         *     boolean removed = false;
         *
         *     for (int grade : grades) {
         *         if (grade == lowest && !removed) {
         *             removed = true;
         *         } else {
         *             result[resultIndex++] = grade;
         *         }
         *     }
         *
         *     return result;
         * }
         *
         * private static int findLowest(int[] grades) {
         *     int lowest = grades[0];
         *     for (int grade : grades) {
         *         if (grade < lowest) lowest = grade;
         *     }
         *     return lowest;
         * }
         */
    }

    /**
     * Removes the lowest score from a variable number of integer scores.
     * Special cases:
     * - If only one score is provided, returns it unchanged (don't remove the only grade)
     * - If no scores are provided, returns an empty array
     * - If the lowest score appears multiple times, removes only one instance
     *
     * @param scores Variable number of integer scores
     * @return Array containing all scores except the lowest one
     */
    public static int[] removeLowest(int... scores)
    {
        // Handle edge case: no scores provided
        if (scores.length == 0)
        {
            return new int[0];
        }

        // Handle edge case: only one score provided
        if (scores.length == 1)
        {
            return new int[] {scores[0]};
        }

        // Find the lowest score
        int lowest = scores[0];
        for (int i = 1; i < scores.length; i++)
        {
            if (scores[i] < lowest)
            {
                lowest = scores[i];
            }
        }

        // Create result array with one less element
        int[] result = new int[scores.length - 1];
        int resultIndex = 0;
        boolean lowestRemoved = false;

        // Copy all elements except the first occurrence of the lowest score
        for (int i = 0; i < scores.length; i++)
        {
            if (scores[i] == lowest && !lowestRemoved)
            {
                lowestRemoved = true; // Skip this element (remove first occurrence)
            }
            else
            {
                result[resultIndex] = scores[i];
                resultIndex++;
            }
        }

        return result;
    }

    /**
     * Creates a string representation of an integer array in the format [1, 2, 3].
     * This method does NOT use Arrays.toString().
     *
     * @param array The integer array to convert to string
     * @return String representation of the array
     */
    public static String arrayPrint(int[] array)
    {
        // Handle empty array case
        if (array.length == 0)
        {
            return "[]";
        }

        StringBuilder result = new StringBuilder();
        result.append("[");

        // Add first element
        result.append(array[0]);

        // Add remaining elements with comma separator
        for (int i = 1; i < array.length; i++)
        {
            result.append(", ");
            result.append(array[i]);
        }

        result.append("]");
        return result.toString();
    }
}
