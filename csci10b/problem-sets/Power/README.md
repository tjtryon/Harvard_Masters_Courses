# Problem Set 1 - Power

**Course:** CSCI 10b - Intermediate Computer Programming for Java II  
**Author:** TJ Tryon  
**Date:** 2025-08-30  

## What This Program Does

This program calculates mathematical powers (like 2^10 = 1024) using a super-smart recursive method. Instead of multiplying the number by itself many times, it uses a mathematical trick: when the exponent is even, it calculates the power of half the exponent and squares that result. This makes the program much faster, reducing the number of steps from over 1000 to just 12 when calculating something like 2^1024.

## How to Run It

1. Open terminal in this folder
2. Type: `javac Power.java`
3. Type: `java Power`
4. The program will show test cases and demonstrate the optimization with power(2.0, 1024)

## What I Learned

- Advanced recursion with mathematical optimization techniques
- Algorithm complexity analysis (O(n) vs O(log n) time complexity)
- Mathematical properties of exponentiation (x^n = (x^(n/2))^2 when n is even)
- Logarithmic vs recursive approaches for performance analysis
- Professional-grade input validation and error handling design
- Performance measurement and timing analysis
- Big O notation and algorithmic efficiency concepts

## Files in This Folder

- `Power.java` - The main program that implements optimized recursive power calculation
- `README.md` - This file explaining the assignment and optimization techniques

## Assignment Requirements

- [x] Modify power method to use x^n = (x^(n/2))^2 optimization for even exponents
- [x] Save result of x^(n/2) and square it (don't call power twice)
- [x] Compute x^(n/2) only once when n is even
- [x] Calculate total calls for power(foobar, 1024) - Answer: 12 calls
- [x] Include comprehensive analysis of O(n) to O(log n) improvement
- [x] Document logarithmic approach and why it's faster
- [x] Code follows proper style guidelines
- [x] All methods have clear documentation
- [x] Program compiles without errors
- [x] Program runs correctly with test cases

## Test Cases

| Input | Expected Output | Notes |
|-------|----------------|-------|
| power(2.0, 10) | 1024.0 | Standard test case |
| power(3.0, 4) | 81.0 | Even exponent optimization |
| power(5.0, 0) | 1.0 | Base case: any number^0 = 1 |
| power(2.0, -3) | 0.125 | Negative exponent: 1/8 = 0.125 |
| power(1.5, 8) | 25.62890625 | Decimal base with even exponent |
| power(x, 1024) | varies | **Call count: 12 total calls** |

**Optimization Demonstration:**
- **Original method**: O(n) = 1025 calls for power(x, 1024)
- **Optimized method**: O(log n) = 12 calls for power(x, 1024)
- **Improvement**: 99% reduction in function calls!

## Notes

**Key Algorithm Optimization:**

The core optimization uses the mathematical property:
- When n is even: x^n = (x^(n/2))^2
- When n is odd: x^n = x * x^(n-1)

**Call Count Analysis for power(foobar, 1024):**

Sequence: 1024 → 512 → 256 → 128 → 64 → 32 → 16 → 8 → 4 → 2 → 1 → 0

1. power(x, 1024) → calls power(x, 512)
2. power(x, 512) → calls power(x, 256)
3. power(x, 256) → calls power(x, 128)
4. power(x, 128) → calls power(x, 64)
5. power(x, 64) → calls power(x, 32)
6. power(x, 32) → calls power(x, 16)
7. power(x, 16) → calls power(x, 8)
8. power(x, 8) → calls power(x, 4)
9. power(x, 4) → calls power(x, 2)
10. power(x, 2) → calls power(x, 1)
11. power(x, 1) → calls power(x, 0)
12. power(x, 0) → base case, returns 1.0

**Total: 12 calls** (including initial call)

**Why Logarithms Would Be Faster:**
- **Math.log() approach**: O(1) constant time calculation
- **Recursive approach**: O(log n) time with function call overhead
- **Formula**: For powers of 2, calls ≈ log₂(n) + 2
- **Hardware optimization**: Built-in math functions are optimized at chip level
- **Educational value**: Manual analysis teaches algorithmic thinking

## Design Decisions

**Input Handling:** While production code would typically include command line argument parsing for dynamic base and exponent input, this implementation uses hardcoded test values to focus on the algorithmic optimization. The commented alternative implementation demonstrates professional input validation, error handling, and performance timing.

**Alternative Implementations:** The source code includes extensively commented alternatives for:
- Command line argument processing with comprehensive error handling
- Logarithmic call count calculation methods
- Performance timing and analysis features
- Production-grade input validation

These alternatives showcase industry-standard practices while maintaining focus on the core assignment requirements of recursive optimization and complexity analysis.