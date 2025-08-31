# Problem Set 1 - LowestGrade

**Course:** CSCI 10b - Intermediate Computer Programming for Java II  
**Author:** TJ Tryon  
**Date:** August 30, 2025

## What This Program Does

This program helps teachers by automatically removing the lowest homework score from a student's grades. It's like having a helpful calculator that finds the worst grade and drops it to help students, which is something many teachers do to be fair.

## How to Run It

1. Open terminal in this folder
2. Type: `javac LowestGrade.java`
3. Type: `java LowestGrade`
4. The program will automatically run test cases and show the results

**Example Output:**
```
Testing removeLowest method with predefined test cases:
====================================================
a = [90, 47, 55, 88]    // Removed 23 from [23, 90, 47, 55, 88]
b = [85]                // Single score kept unchanged
c = []                  // No scores provided
d = [59, 92, 93, 88, 47] // Removed one instance of 47 from duplicates
```

## What I Learned

- How to use variable arguments (varargs) with `int...` to accept different numbers of scores
- How to manipulate arrays by finding, removing, and copying elements
- How to handle special cases like empty arrays, single elements, and duplicate values
- How to build strings without using `Arrays.toString()` method
- How to design methods with clear responsibilities and good documentation
- The difference between demonstration code and production code with user input

## Files in This Folder

- `LowestGrade.java` - The main program that removes lowest scores from grade arrays
- `README.md` - This file explaining the assignment

## Assignment Requirements

- [x] Implement removeLowest method with varargs (int... scores)
- [x] Handle edge cases: empty input, single score, duplicate lowest scores
- [x] Implement arrayPrint method without Arrays.toString()
- [x] Create main method demonstrating all test cases
- [x] Return arrays with lowest score removed (keep single scores unchanged)
- [x] Code follows proper style guidelines
- [x] All methods have clear documentation
- [x] Program compiles without errors
- [x] Program runs correctly with test cases

## Test Cases

| Input | Expected Output | Notes |
|-------|----------------|-------|
| removeLowest(23, 90, 47, 55, 88) | [90, 47, 55, 88] | Removes lowest (23) |
| removeLowest(85) | [85] | Single score preserved |
| removeLowest() | [] | Empty input returns empty array |
| removeLowest(59, 92, 93, 47, 88, 47) | [59, 92, 93, 88, 47] | Removes first occurrence of duplicate lowest |

## Notes

### Design Decisions

**User Input Approach:** While the assignment focuses on demonstrating the `removeLowest` method with hardcoded test cases, a comprehensive user input implementation is included but commented out. In production environments, this would allow teachers to interactively enter grades for real-world use.

**Production Benefits of User Input:**
- Teachers could actually use this program with their grade books
- Handle varying numbers of grades per student dynamically
- Interactive prompts guide users through the process
- Input validation for reasonable grade ranges
- Better user experience with clear feedback

**Why Commented Out:** The assignment specification focuses on demonstrating specific test cases to verify correct algorithm implementation and edge case handling. The commented implementation showcases professional development practices while maintaining assignment compliance.

**Educational Value:** This demonstrates the difference between demonstration code (focused on algorithm verification) and production code (focused on user interaction), an important distinction in software development.