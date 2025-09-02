# Problem Set 1 - RecTriangle.java

**Course:** CSCI 10b - Intermediate Computer Programming for Java II  
**Author:** TJ Tryon  
**Date:** 2025-08-29  

## What This Program Does

This program creates a triangular pattern using square brackets ([]). It uses recursion to print lines starting with the longest line at the top and getting shorter as it goes down. For example, with input 4, it prints 4 squares, then 3, then 2, then 1.

## How to Run It

1. Open terminal in this folder
2. Type: `javac RecTriangle.java`
3. Type: `java RecTriangle`
4. The program will automatically run with input 4 and display the triangle pattern

**Note:** Command line arguments are intentionally not implemented as the Problem Set 2 specification explicitly requires using `printTriangle(4)` with a hardcoded value.

## What I Learned

- How to use recursion to solve problems by breaking them into smaller parts
- How the order of operations in recursive methods affects output patterns
- How to modify recursive algorithms to produce different results (reversing output order)
- Understanding base cases and recursive calls in method design

## Files in This Folder

- `RecTriangle.java` - The main program that prints a reverse triangular pattern using recursion
- `README.md` - This file explaining the assignment

## Assignment Requirements

- [x] Modify the original printTriangle method to reverse the output pattern
- [x] Keep the method recursive (no loops for the main pattern)
- [x] Output should start with the longest line and decrease in size
- [x] Use printTriangle(4) as specified in assignment requirements
- [x] Code follows proper style guidelines
- [x] All methods have clear documentation
- [x] Program compiles without errors
- [x] Program runs correctly with test cases

## Test Cases

| Input | Expected Output | Notes |
|-------|----------------|-------|
| printTriangle(4) | [][][][]<br>[][][]<br>[][]<br>[] | Reverse triangular pattern |
| printTriangle(3) | [][][]<br>[][]<br>[] | Works with different input sizes |
| printTriangle(1) | [] | Base case with single square |

## Notes

**Key Insight:** The original method printed after the recursive call, creating an ascending pattern (small to large). By moving the print statements before the recursive call, we create a descending pattern (large to small). This demonstrates how the placement of operations relative to recursive calls affects the order of execution.

## Design Decisions

**Input Handling:** The assignment specification for Problem Set 2 explicitly states to use `printTriangle(4)` with a hardcoded value. While a more robust implementation would typically include command line argument parsing with input validation and error handling, this approach was intentionally not implemented to maintain strict compliance with the assignment requirements.

**Alternative Implementation:** The source code includes a commented-out alternative that demonstrates proper command line argument processing, including:
- `Integer.parseInt()` for string-to-integer conversion
- `NumberFormatException` handling for invalid input
- Input validation for positive integers
- User-friendly error messaging

This alternative showcases industry-standard practices for user input handling while preserving the assignment's required functionality.