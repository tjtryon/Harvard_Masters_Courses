/**
 * ArrayPractice.java
 * Author: TJ Tryon
 * Date: 2025-08-29
 * Course: CSCI 22e - Data Structures
 * Problem Set: PS0 - Precourse Evaluation
 *
 * This program demonstrates array manipulation techniques, specifically
 * swapping adjacent pairs of elements within an integer array.
 * It includes proper error handling and comprehensive testing.
 *
 * Data structures used:
 * - Arrays (one-dimensional integer arrays)
 * - Array indexing and element access
 *
 * Key algorithms:
 * - Array traversal with pair-wise processing
 * - Element swapping using temporary variables
 * - Boundary checking for odd-length arrays
 *
 * Input: Integer arrays for pair swapping operations
 * Output: Modified arrays with adjacent elements swapped
 */

public class ArrayPractice
{
    /**
     * swapPairs swaps adjacent pairs of elements in an integer array.
     * Swaps arr[0] with arr[1], arr[2] with arr[3], etc.
     * If the array has odd length, the last element remains unchanged.
     *
     * @param arr The integer array to modify (cannot be null)
     * @throws IllegalArgumentException if arr is null
     */
    public static void swapPairs(int[] arr)
    {
        // Check for null parameter
        if (arr == null)
        {
            throw new IllegalArgumentException("Array cannot be null");
        }

        // Swap adjacent pairs of elements
        for (int i = 0; i < arr.length - 1; i += 2)
        {
            // Swap arr[i] and arr[i+1]
            int temp = arr[i];
            arr[i] = arr[i + 1];
            arr[i + 1] = temp;
        }
    }

    /**
     * printArray displays the contents of an integer array.
     * Helper method for testing purposes.
     *
     * @param arr The array to print
     * @param label A descriptive label for the array
     */
    public static void printArray(int[] arr, String label)
    {
        System.out.print(label + ": ");
        if (arr == null)
        {
            System.out.println("null");
            return;
        }

        System.out.print("{");
        for (int i = 0; i < arr.length; i++)
        {
            System.out.print(arr[i]);
            if (i < arr.length - 1)
            {
                System.out.print(", ");
            }
        }
        System.out.println("}");
    }

    /**
     * The main method runs when the program starts.
     * It tests the swapPairs method with various array configurations
     * to demonstrate its functionality and error handling.
     *
     * @param args Command line arguments (not used in this program)
     */
    public static void main(String[] args)
    {
        System.out.println("Testing swapPairs method:");
        System.out.println("=========================");

        // Test case 1: Even-length array (example from problem)
        int[] values1 = {0, 2, 4, 6, 8, 10};
        printArray(values1, "Before swapPairs");
        swapPairs(values1);
        printArray(values1, "After swapPairs ");

        System.out.println();

        // Test case 2: Odd-length array
        int[] values2 = {1, 3, 5, 7, 9};
        printArray(values2, "Before swapPairs");
        swapPairs(values2);
        printArray(values2, "After swapPairs ");

        System.out.println();

        // Test case 3: Array with 2 elements
        int[] values3 = {10, 20};
        printArray(values3, "Before swapPairs");
        swapPairs(values3);
        printArray(values3, "After swapPairs ");

        System.out.println();

        // Test case 4: Array with 1 element
        int[] values4 = {42};
        printArray(values4, "Before swapPairs");
        swapPairs(values4);
        printArray(values4, "After swapPairs ");

        System.out.println();

        // Test case 5: Empty array
        int[] values5 = {};
        printArray(values5, "Before swapPairs");
        swapPairs(values5);
        printArray(values5, "After swapPairs ");

        System.out.println();

        // Test case 6: Null array (should throw exception)
        System.out.println("Testing null parameter exception:");
        try
        {
            swapPairs(null);
            System.out.println("ERROR: Exception should have been thrown!");
        } catch (IllegalArgumentException e)
        {
            System.out.println("Correctly threw exception: " + e.getMessage());
        }
    }
}