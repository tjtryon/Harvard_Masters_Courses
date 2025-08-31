# Problem Set 1 - RecursivePrint

**Course:** CSCI 10b - Intermediate Computer Programming for Java II  
**Author:** TJ Tryon  
**Date:** August 30, 2025

## What This Program Does

This program takes any whole number (like 143 or -24549) and converts it into English words (like "one hundred forty three" or "minus twenty four thousand five hundred forty nine"). It works like a translator that turns digits into the words you would say out loud when reading the number.

**Extra Credit Features:**
- Handles the full range of 32-bit integers (up to 2.1 billion)
- Works with negative numbers including Integer.MIN_VALUE
- Uses pure recursion to break down large numbers into smaller parts

## How to Run It

### Compilation
1. Open terminal in this folder
2. Type: `javac RecursivePrint.java`

### Usage Options

**Option 1: Command Line Argument**
```bash
java RecursivePrint 143
java RecursivePrint -24549
java RecursivePrint 2147483647
```

**Option 2: Interactive Mode**
```bash
java RecursivePrint
# Program will prompt: "Please enter an integer to convert to words: "
# Enter your number and press Enter
```

### Sample Outputs

**Command Line Mode:**
```
$ java RecursivePrint 143
RecursivePrint - Converting Numbers to English Words
==================================================

Command line input: 143
Result: one hundred forty three
```

**Interactive Mode:**
```
$ java RecursivePrint
RecursivePrint - Converting Numbers to English Words
==================================================

Please enter an integer to convert to words: -24549
You entered: -24549
Result: minus twenty four thousand five hundred forty nine
```

**Error Handling:**
```
$ java RecursivePrint abc
Error: 'abc' is not a valid integer.
Usage: java RecursivePrint [integer]
Examples:
  java RecursivePrint 143
  java RecursivePrint -24549
  java RecursivePrint
```

## What I Learned

- **Pure Recursion**: How to break complex problems into smaller, similar subproblems
- **Base Cases**: When to stop recursing (numbers 0-19 use direct lookup)
- **Recursive Cases**: How to divide numbers by scale (billions, millions, thousands, hundreds)
- **Array Lookup**: Using arrays to store word mappings for efficient conversion
- **Integer Arithmetic**: Using division and modular arithmetic to extract digit groups
- **Edge Case Handling**: Managing zero, negative numbers, and Integer.MIN_VALUE overflow
- **Method Overloading**: Using helper methods with different parameter types (long vs int)
- **Command Line Processing**: Using `args.length` and `args[0]` to handle user arguments
- **Input Validation**: Using try-catch blocks to handle NumberFormatException
- **Interactive User Input**: Using Scanner to prompt users and validate input
- **Program Flow Control**: Implementing multiple execution modes (CLI, interactive)

## Files in This Folder

- `RecursivePrint.java` - The main program that recursively converts numbers to English words
- `README.md` - This file explaining the assignment

## Assignment Requirements

- [x] **Create recursive method printNumber(int n)** that converts numbers to English words
- [x] **Handle numbers less than one million** (basic requirement met)
- [x] **Support negative numbers** with "minus" prefix
- [x] **Extra Credit: Support up to Integer.MAX_VALUE** (2.1 billion range)
- [x] **Demonstrate with comprehensive main method** showing various test cases
- [x] **Use pure recursion** for number decomposition and word building
- [x] **Command line argument processing** with argc/argv validation
- [x] **Interactive user input** with error handling and re-prompting
- [x] **Input validation** for both command line and interactive modes
- [x] **Multiple execution modes** (CLI argument, interactive)
- [x] Code follows proper style guidelines
- [x] All methods have clear documentation
- [x] Program compiles without errors
- [x] Program runs correctly with test cases

## Test Cases

| Input | Expected Output | Notes |
|-------|----------------|-------|
| 143 | one hundred forty three | Assignment example |
| -24549 | minus twenty four thousand five hundred forty nine | Assignment example |
| 0 | zero | Edge case |
| 19 | nineteen | Base case boundary |
| 20 | twenty | Tens place start |
| 999 | nine hundred ninety nine | Hundreds boundary |
| 1000 | one thousand | Thousands start |
| 1000000 | one million | Millions start |
| 2147483647 | two billion one hundred forty seven million four hundred eighty three thousand six hundred forty seven | Integer.MAX_VALUE |
| -2147483648 | minus two billion one hundred forty seven million four hundred eighty three thousand six hundred forty eight | Integer.MIN_VALUE |

## Notes

### Recursive Algorithm Design

The program uses a **divide-and-conquer recursive approach**:

1. **Base Cases**: 
   - Zero returns "zero"
   - Numbers 1-19 use direct array lookup
   - Empty recursive calls (n=0) return immediately

2. **Recursive Cases**:
   - **20-99**: Print tens word, recursively handle ones
   - **100-999**: Print hundreds word, recursively handle remainder  
   - **1,000-999,999**: Print thousands group, recursively handle remainder
   - **1,000,000-999,999,999**: Print millions group, recursively handle remainder
   - **1,000,000,000+**: Print billions group, recursively handle remainder

### Extra Credit Implementation

**Challenge**: Support numbers up to Integer.MAX_VALUE (2,147,483,647)

**Solution**: Extended the recursive algorithm to handle billions place value and used `long` type in the helper method to handle Integer.MIN_VALUE overflow issue.

**Technical Details**:
- Uses word lookup arrays for efficiency
- Handles Integer.MIN_VALUE special case (can't convert to positive int)
- Supports full 32-bit integer range for 2 additional points

### Educational Value

This assignment demonstrates how recursion can elegantly handle hierarchical data structures (number place values). Each recursive call handles a smaller version of the same problem, making the solution both intuitive and mathematically sound.