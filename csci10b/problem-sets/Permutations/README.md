# Problem Set 1 - Permutations

**Course:** CSCI 10b - Intermediate Computer Programming for Java II  
**Author:** TJ Tryon  
**Date:** August 30, 2025

## What This Program Does

This program takes a string (like "ABC") and shows you all the different ways you can arrange those letters. It's like having letter tiles and figuring out every possible way to line them up. For example, with "ABC" you can make: ABC, ACB, BAC, BCA, CAB, and CBA - that's 6 different arrangements!

## How to Run It

1. Open terminal in this folder
2. Type: `javac Permutations.java`
3. Type: `java Permutations`
4. The program automatically shows permutations for "ABCD" as specified in the assignment

### Alternative Input Methods (Commented Out)

The program includes two alternative input handling approaches that are documented but commented out to comply with assignment specifications:

**Command Line Arguments (Commented Out):**
- Usage: `java Permutations "XYZ"` would generate permutations of "XYZ"
- Includes input validation and error handling
- Falls back to "ABCD" if invalid input provided

**User Prompting (Commented Out):**
- Interactively prompts user for string input using Scanner
- Provides user-friendly console interaction
- Handles empty input with default fallback to "ABCD"

**Sample Output (Current Implementation):**
```
Permutations of "ABCD" (as specified in assignment):
ABCD
ABDC
ACBD
ACDB
ADBC
ADCB
BACD
BADC
BCAD
BCDA
BDAC
BDCA
CABD
CADB
CBAD
CBDA
CDAB
CDBA
DABC
DACB
DBAC
DBCA
DCAB
DCBA
```

## What I Learned

- **Pure Recursion**: How to break complex problems into smaller, similar subproblems
- **Backtracking**: Making choices, exploring all possibilities, then undoing choices
- **Combinatorial Algorithms**: Understanding factorial growth (n! permutations for n characters)
- **String Manipulation**: Using substring operations to build and modify strings
- **Helper Methods**: Designing recursive methods with multiple parameters
- **Base Cases**: Knowing when to stop recursing (when no characters remain)
- **Recursive Strategy**: Dividing permutations into groups based on the first character
- **Algorithm Analysis**: Understanding time complexity O(n! * n) and space complexity O(n)

## Files in This Folder

- `Permutations.java` - The main program that recursively generates all string permutations
- `README.md` - This file explaining the assignment

## Assignment Requirements

- [x] **Create recursive method listPermutations(String s)** that prints all permutations
- [x] **Use the divide-and-conquer strategy** described in the assignment
- [x] **Group permutations by first character** (A permutations, B permutations, etc.)
- [x] **Generate all n! permutations** for an n-character string
- [x] **Demonstrate with "ABCD"** showing all 24 permutations as specified
- [x] **Create convincing main method** that follows assignment specifications exactly
- [x] **Document alternative input methods** (command line args and user prompting) but keep them commented out
- [x] **Handle edge cases** like empty strings and single characters
- [x] Code follows proper style guidelines
- [x] All methods have clear documentation
- [x] Program compiles without errors
- [x] Program runs correctly with test cases

## Test Cases

| Input | Expected Permutations | Count | Notes |
|-------|---------------------|-------|-------|
| "A" | A | 1 | Single character (1! = 1) |
| "AB" | AB, BA | 2 | Two characters (2! = 2) |
| "ABC" | ABC, ACB, BAC, BCA, CAB, CBA | 6 | Three characters (3! = 6) |
| "ABCD" | All 24 permutations | 24 | Assignment example (4! = 24) |
| "" | (empty) | 1 | Edge case: empty string |

## Notes

### Recursive Algorithm Strategy

The program follows the **divide-and-conquer approach** suggested in the assignment:

1. **Divide**: Split permutations into groups based on the first character
   - For "ABCD": Group A, Group B, Group C, Group D
2. **Conquer**: Each group = first char + all permutations of remaining chars
   - Group A = 'A' + all permutations of "BCD"
   - Group B = 'B' + all permutations of "ACD"
   - etc.
3. **Combine**: Print each completed permutation

### Implementation Details

**Public Interface:**
```java
listPermutations("ABCD");  // Generates all 24 permutations
```

**Recursive Helper:**
```java
listPermutations(prefix, remaining)
// Base case: remaining.length() == 0 → print prefix
// Recursive case: try each char in remaining as next choice
```

**Key Insights:**
- **Base Case**: When no characters remain, print the completed permutation
- **Recursive Case**: For each remaining character, choose it and recurse on the rest
- **Backtracking**: The recursion naturally backtracks to try all possibilities
- **Order**: Permutations are generated in lexicographic order within each group

### Mathematical Properties

- **Total Permutations**: n! (n factorial) for an n-character string
- **Time Complexity**: O(n! × n) - generating n! permutations, each taking O(n) time
- **Space Complexity**: O(n) - maximum recursion depth is n
- **Growth Rate**: Factorial growth means this becomes impractical for large strings (10! = 3.6 million)

### Educational Value

This assignment demonstrates how recursion elegantly solves combinatorial problems. The recursive structure mirrors the mathematical definition of permutations, making the algorithm both intuitive and mathematically sound. It also introduces concepts used in more advanced algorithms like backtracking and dynamic programming.

### Alternative Implementation Discussion

While the current implementation follows assignment specifications exactly by using "ABCD", the commented-out alternative approaches demonstrate important programming concepts:

**Command Line Arguments:** Shows how to handle runtime parameters, validate input, and provide flexible program behavior. This approach is common in professional software where configuration flexibility is important.

**User Interaction:** Demonstrates interactive programming using Scanner, input validation, and graceful error handling. This approach provides the best user experience for interactive applications.

**Design Philosophy:** Both alternatives include comprehensive error handling, input validation, and fallback behavior - demonstrating defensive programming practices that are essential in production code. The documentation of these approaches (even when unused) shows thoughtful consideration of different use cases and programming patterns.