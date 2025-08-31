# Problem Set 1 - Palindrome

**Course:** CSCI 10b - Intermediate Computer Programming for Java II  
**Author:** TJ Tryon  
**Date:** August 30, 2025

## What This Program Does

This program checks if a sentence reads the same forwards and backwards (like "madam" or "A man, a plan, a canal: Panama"). It uses a clever recursive technique that compares the first and last letters, then checks the middle part the same way. The program is smart enough to ignore spaces, punctuation, and whether letters are uppercase or lowercase.

**Key Features:**
- Pure recursive algorithm with NO loops (as required)
- Ignores non-alphanumeric characters (punctuation, spaces)
- Case-insensitive comparison
- Handles complex sentences with mixed punctuation

## How to Run It

1. Open terminal in this folder
2. Type: `javac Palindrome.java`
3. Type: `java Palindrome`
4. Enter a sentence when prompted
5. The program will tell you if it's a palindrome or not

**Example Usage:**
```
Enter a sentence to check if it's a palindrome: A man, a plan, a canal: Panama

"A man, a plan, a canal: Panama"
IS a palindrome!
```

## What I Learned

- **Pure Recursion**: How to solve problems using only recursion without any loops (while, for, do-while)
- **Base Cases**: When to stop recursing (strings of length ≤ 1 are palindromes)
- **Recursive Cases**: How to break down the problem into smaller parts
- **String manipulation**: Using `substring()` to create smaller strings for recursion
- **Character analysis**: Using `Character.isLetterOrDigit()` to filter alphanumeric characters
- **Case handling**: Converting to lowercase for case-insensitive comparison
- **User input**: Using Scanner class for interactive programs
- **Edge case handling**: Managing empty strings and single characters

## Files in This Folder

- `Palindrome.java` - The main program that recursively checks if strings are palindromes
- `README.md` - This file explaining the assignment

## Assignment Requirements

- [x] **MUST use recursion** - NO while loops, for loops, or do-while loops allowed
- [x] Implement recursive isPalindrome(String s) method
- [x] Handle base case: strings of length ≤ 1 are palindromes
- [x] Implement recursive cases: skip non-alphanumeric characters, compare first/last
- [x] Ignore punctuation and spaces (use Character.isLetterOrDigit)
- [x] Handle case differences (convert to lowercase in main)
- [x] Create main method with user input using Scanner
- [x] Test with complex palindromes containing punctuation
- [x] Code follows proper style guidelines
- [x] All methods have clear documentation
- [x] Program compiles without errors
- [x] Program runs correctly with test cases

## Test Cases

| Input | Expected Output | Notes |
|-------|----------------|-------|
| "madam" | IS a palindrome! | Simple palindrome |
| "12321" | IS a palindrome! | Numeric palindrome |
| "hello" | is NOT a palindrome. | Regular word, not palindrome |
| "A man, a plan, a canal: Panama" | IS a palindrome! | Complex with punctuation |
| "Cigar? Toss it in a can, it is so tragic!" | IS a palindrome! | Example from assignment |
| "race a car" | is NOT a palindrome. | Similar letters but not palindrome |
| "Was it a rat I saw?" | IS a palindrome! | Classic palindrome sentence |

## Notes

### Recursive Algorithm Design (NO LOOPS!)

The palindrome checker uses a **pure recursive approach** with absolutely no loops:

1. **Base Case**: Strings of length 0 or 1 are always palindromes
2. **Recursive Cases**: 
   - If first character is not alphanumeric → recursively check `substring(1)`
   - If last character is not alphanumeric → recursively check `substring(0, length-1)`
   - If both are alphanumeric and different → return false
   - If both are alphanumeric and same → recursively check middle `substring(1, length-1)`

**Key Implementation Details:**

- **NO LOOPS**: Uses only recursive calls to skip non-alphanumeric characters
- **Character Filtering**: Uses `Character.isLetterOrDigit()` to identify alphanumeric characters
- **Case Normalization**: Converts input to lowercase in main method
- **String Processing**: Uses `substring()` operations for recursive calls
- **Pure Recursion**: Every iteration is handled by a recursive method call

**Why This Approach:**
The assignment explicitly prohibits using while, for, or do-while loops. The previous implementation violated this by using while loops to find alphanumeric characters. This version uses pure recursion to skip non-alphanumeric characters, making every step of the algorithm recursive.

**Algorithmic Complexity:**
- **Time Complexity**: O(n) where n is the length of the string
- **Space Complexity**: O(n) due to recursive call stack and substring creation

**Educational Value:**
This demonstrates how recursion can completely replace iterative constructs. Every problem that can be solved with loops can also be solved with recursion, though sometimes at the cost of additional memory usage for the call stack.

### Design Decisions

**Pure Recursion Requirement:** The assignment explicitly states "You may NOT use a while loop, for loop or do-while loop." This implementation strictly adheres to this requirement by using only recursive method calls to handle all string processing, including skipping non-alphanumeric characters.

**User Input:** Uses Scanner-based interactive input as required by the assignment specification for demonstrating the palindrome checker with various test cases.