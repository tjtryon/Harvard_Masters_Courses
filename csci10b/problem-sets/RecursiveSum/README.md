# Problem Set 1 - RecursiveSum

**Course:** CSCI 10b - Intermediate Computer Programming for Java II  
**Author:** TJ Tryon  
**Date:** 2025-08-30  

## What This Program Does

This program adds up fractions that get smaller and smaller! It starts with 1, then adds 1/2, then adds 1/3, then 1/4, and keeps going. For example, if you tell it to add up the first 3 fractions, it calculates 1 + 1/2 + 1/3 = 1.833333. The program uses recursion (a method that calls itself) to do this math without using any loops.

## How to Run It

1. Open terminal in this folder
2. Type: `javac RecursiveSum.java`
3. Type: `java RecursiveSum`
4. Watch it show you different test cases and their results

## What I Learned

- **Pure Recursion**: How to solve problems using only recursion without any loops (for, while, do-while)
- **Mathematical Computation**: Working with reciprocals and the harmonic series (1 + 1/2 + 1/3 + ...)
- **Exception Handling**: Using IllegalArgumentException to validate input parameters
- **Base Cases**: Identifying when to stop recursing (n = 0 returns 0.0)
- **Recursive Cases**: How each recursive call builds on previous results (1/n + sumTo(n-1))
- **Floating-Point Arithmetic**: Working with double precision for accurate decimal calculations
- **Method Design**: Creating clear, well-documented methods with proper parameter validation

## Files in This Folder

- `RecursiveSum.java` - The main program that recursively calculates sums of reciprocals
- `README.md` - This file explaining the assignment

## Assignment Requirements

- [x] **Write recursive method sumTo(n)** that returns sum of first n reciprocals
- [x] **Use pure recursion only** - no loops (while, for, do-while) allowed
- [x] **Handle edge cases** - return 0.0 for n=0
- [x] **Throw IllegalArgumentException** for negative values of n
- [x] **Calculate correct mathematical results** (e.g., sumTo(2) = 1.5)
- [x] **Create convincing main method** with comprehensive test cases
- [x] Code follows proper style guidelines
- [x] All methods have clear documentation
- [x] Program compiles without errors
- [x] Program runs correctly with test cases

## Test Cases

| Input | Expected Output | Notes |
|-------|----------------|-------|
| sumTo(0) | 0.000000 | Base case - no reciprocals to sum |
| sumTo(1) | 1.000000 | Single reciprocal: 1/1 = 1.0 |
| sumTo(2) | 1.500000 | Two reciprocals: 1 + 1/2 = 1.5 |
| sumTo(3) | 1.833333 | Three reciprocals: 1 + 1/2 + 1/3 ≈ 1.833 |
| sumTo(4) | 2.083333 | Four reciprocals: adds 1/4 = 0.25 |
| sumTo(10) | 2.928968 | Tenth partial sum of harmonic series |
| sumTo(-1) | Exception | Throws IllegalArgumentException |
| sumTo(100) | 5.187378 | Large value demonstration |

**Sample Output:**
```
RecursiveSum - Computing Sum of Reciprocals
==========================================

Test 1 - Base case:
sumTo(0) = 0.000000
Expected: 0.000000

Test 3 - Two reciprocals:
sumTo(2) = 1.500000
Expected: 1.500000 (which is 1/1 + 1/2 = 1.0 + 0.5)
```

## Notes

**Mathematical Background:** This program computes partial sums of the harmonic series, which is a famous infinite series that grows very slowly but diverges (eventually reaches infinity). The harmonic series has important applications in mathematics, computer science, and physics.

**Recursive Strategy:** The algorithm works by recognizing that sumTo(n) = 1/n + sumTo(n-1). This breaks the problem down into smaller subproblems until reaching the base case.

**Performance:** Since each recursive call creates a new stack frame, this approach uses O(n) space for the call stack. For very large values of n, this could cause stack overflow, but it elegantly demonstrates the recursive approach.