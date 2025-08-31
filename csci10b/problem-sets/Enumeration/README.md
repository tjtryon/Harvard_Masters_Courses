# Problem Set 1 - Enumeration

**Course:** CSCI 10b - Intermediate Computer Programming for Java II  
**Author:** TJ Tryon  
**Date:** 2025-08-30  

## What This Program Does

This program figures out how many days are in each month of the year 2023. It knows that some months have 30 days, some have 31 days, and February is special because it can have 28 or 29 days depending on if it's a leap year. The program uses Java enumerations to represent the 12 months and prints out the number of days for each one.

## How to Run It

1. Open terminal in this folder
2. Type: `javac Enumeration.java`
3. Type: `java Enumeration`
4. The program will automatically display the days in each month for year 2023

**Note:** Command line arguments are intentionally not implemented as the assignment specification explicitly requires displaying results for year 2023 with hardcoded values.

## What I Learned

- How to use enumerations (enum) to represent a fixed set of constants
- How to implement switch statements with multiple cases
- How to calculate leap years using modulo operations and logical operators
- How to use enhanced for loops to iterate through enum values
- Understanding the Gregorian calendar leap year rules

## Files in This Folder

- `Enumeration.java` - The main program that calculates and displays days in each month
- `README.md` - This file explaining the assignment

## Assignment Requirements

- [x] Create enum for the 12 months (JAN through DEC)
- [x] Implement daysInMonth method with switch statement
- [x] Handle 31-day months (JAN, MAR, MAY, JUL, AUG, OCT, DEC)
- [x] Handle 30-day months (APR, JUN, SEP, NOV)
- [x] Implement leap year logic for February
- [x] Use enhanced for loop to iterate through all months
- [x] Code follows proper style guidelines
- [x] All methods have clear documentation
- [x] Program compiles without errors
- [x] Program runs correctly with test cases

## Test Cases

| Input Year | February Days | Notes |
|------------|---------------|-------|
| 2023 | 28 days | Regular year (not divisible by 4) |
| 2024 | 29 days | Leap year (divisible by 4, not by 100) |
| 2100 | 28 days | Not leap year (divisible by 100, not by 400) |
| 2000 | 29 days | Leap year (divisible by 400) |

**Sample Output:**
```
JAN 2023 has 31 days!
FEB 2023 has 28 days!
MAR 2023 has 31 days!
APR 2023 has 30 days!
MAY 2023 has 31 days!
JUN 2023 has 30 days!
JUL 2023 has 31 days!
AUG 2023 has 31 days!
SEP 2023 has 30 days!
OCT 2023 has 31 days!
NOV 2023 has 30 days!
DEC 2023 has 31 days!
```

## Notes

**Key Programming Concepts:**

1. **Enumerations:** Using `enum Months` provides type safety and makes the code more readable than using integers or strings to represent months.

2. **Switch Statements:** The switch statement efficiently handles multiple cases by grouping months with the same number of days.

3. **Leap Year Algorithm:** The Gregorian calendar leap year rules are implemented using modulo operators:
   - `year % 4 == 0` checks divisibility by 4
   - `year % 100 != 0` excludes century years
   - `year % 400 == 0` includes every 400th year

4. **Enhanced For Loop:** `for (Months m : Months.values())` automatically iterates through all enum constants.

**Memory Device for Days in Months:** "Thirty days hath September, April, June, and November. All the rest have thirty-one, except February alone."

**Historical Note:** The leap year rules account for the fact that Earth's orbital period is approximately 365.2425 days, not exactly 365 days.

## Design Decisions

**Input Handling:** The assignment specification explicitly requires displaying the days in each month for year 2023. While a more flexible implementation would typically include command line argument parsing to allow users to check any year, this approach was intentionally not implemented to maintain strict compliance with the assignment requirements.

**Alternative Implementation:** The source code includes a commented-out alternative that demonstrates proper command line argument processing for year input, including:
- `Integer.parseInt()` for string-to-integer conversion
- `NumberFormatException` handling for invalid input
- Input validation for positive integers
- Default fallback to year 2023 if no argument provided
- User-friendly error messaging with usage instructions

This alternative showcases industry-standard practices for user input handling while preserving the assignment's required functionality. It would allow users to test the leap year logic with different years (e.g., `java Enumeration 2024` to see a leap year, or `java Enumeration 2100` to see a century year exception).