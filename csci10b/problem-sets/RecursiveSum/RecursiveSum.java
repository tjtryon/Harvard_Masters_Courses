/**
 * RecursiveSum.java
 * Author: TJ Tryon
 * Date: 2025-08-30
 * Course: CSCI 10b - Intermediate Computer Programming for Java II
 * Problem Set: PS1 - RecursiveSum
 *
 * This program calculates the sum of the first n reciprocals using pure recursion.
 * It computes the mathematical expression: 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
 *
 * For example:
 * - sumTo(1) = 1.0
 * - sumTo(2) = 1.5 (which is 1 + 0.5)
 * - sumTo(3) = 1.833... (which is 1 + 0.5 + 0.333...)
 *
 * Key concepts used:
 * - Pure recursion with base cases and recursive cases
 * - Mathematical computation with floating-point arithmetic
 * - Exception handling with IllegalArgumentException
 * - Method design and parameter validation
 * - Reciprocal calculations (1/n)
 *
 * Input: Integer parameter n representing the number of reciprocals to sum
 * Output: Double value representing the sum of the first n reciprocals
 */

public class RecursiveSum {

    /**
     * The main method demonstrates the sumTo method with various test cases.
     * It shows the method working with different values and verifies the mathematical
     * correctness by displaying the sum of reciprocals for each test case.
     *
     * @param args Command line arguments (not used in this program)
     */
    public static void main(String[] args)
    {
        System.out.println("RecursiveSum - Computing Sum of Reciprocals");
        System.out.println("==========================================");
        System.out.println();

        // Test case 1: Base case n = 0 (should return 0.0)
        System.out.println("Test 1 - Base case:");
        System.out.printf("sumTo(0) = %.6f%n", sumTo(0));
        System.out.println("Expected: 0.000000");
        System.out.println();

        // Test case 2: Simple case n = 1 (should return 1.0)
        System.out.println("Test 2 - Single reciprocal:");
        System.out.printf("sumTo(1) = %.6f%n", sumTo(1));
        System.out.println("Expected: 1.000000 (which is 1/1)");
        System.out.println();

        // Test case 3: Two reciprocals n = 2 (should return 1.5)
        System.out.println("Test 3 - Two reciprocals:");
        System.out.printf("sumTo(2) = %.6f%n", sumTo(2));
        System.out.println("Expected: 1.500000 (which is 1/1 + 1/2 = 1.0 + 0.5)");
        System.out.println();

        // Test case 4: Three reciprocals n = 3
        System.out.println("Test 4 - Three reciprocals:");
        double result3 = sumTo(3);
        System.out.printf("sumTo(3) = %.6f%n", result3);
        System.out.println("Expected: 1.833333 (which is 1/1 + 1/2 + 1/3 ≈ 1.0 + 0.5 + 0.333333)");
        System.out.println();

        // Test case 5: Four reciprocals n = 4
        System.out.println("Test 5 - Four reciprocals:");
        double result4 = sumTo(4);
        System.out.printf("sumTo(4) = %.6f%n", result4);
        System.out.println("Expected: 2.083333 (which is 1 + 1/2 + 1/3 + 1/4)");
        System.out.println();

        // Test case 6: Larger value n = 10
        System.out.println("Test 6 - Ten reciprocals:");
        double result10 = sumTo(10);
        System.out.printf("sumTo(10) = %.6f%n", result10);
        System.out.println("Expected: ~2.928968 (harmonic series grows slowly)");
        System.out.println();

        // Test case 7: Exception handling for negative values
        System.out.println("Test 7 - Exception handling:");
        try
        {
            sumTo(-1);
            System.out.println("ERROR: Should have thrown IllegalArgumentException!");
        } catch (IllegalArgumentException e)
        {
            System.out.println("✓ Correctly threw IllegalArgumentException for n = -1");
            System.out.println("Exception message: " + e.getMessage());
        }
        System.out.println();

        // Test case 8: Large value to show convergence behavior
        System.out.println("Test 8 - Larger sequence:");
        double result100 = sumTo(100);
        System.out.printf("sumTo(100) = %.6f%n", result100);
        System.out.println("Note: This is the 100th partial sum of the harmonic series");

        System.out.println();
        System.out.println("All tests completed successfully!");
    }

    /**
     * Recursively calculates the sum of the first n reciprocals.
     * Computes the mathematical expression: 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
     *
     * This method uses pure recursion without any loops:
     * - Base case: If n = 0, return 0.0
     * - Base case: If n = 1, return 1.0 (which is 1/1)
     * - Recursive case: Return (1/n) + sumTo(n-1)
     *
     * Examples:
     * - sumTo(0) = 0.0
     * - sumTo(1) = 1.0
     * - sumTo(2) = 1.5 (which is 1/1 + 1/2 = 1.0 + 0.5)
     * - sumTo(3) = 1.833... (which is 1/1 + 1/2 + 1/3)
     *
     * @param n The number of reciprocals to sum (must be >= 0)
     * @return The sum of the first n reciprocals as a double
     * @throws IllegalArgumentException if n is negative
     */
    public static double sumTo(int n)
    {
        // Input validation: throw exception for negative values
        if (n < 0)
        {
            throw new IllegalArgumentException("Parameter n must be non-negative, but was: " + n);
        }

        // Base case: n = 0 returns 0.0
        if (n == 0)
        {
            return 0.0;
        }

        // Recursive case: add current reciprocal (1/n) to sum of previous reciprocals
        // This implements: 1/n + sumTo(n-1)
        return (1.0 / n) + sumTo(n - 1);
    }
}