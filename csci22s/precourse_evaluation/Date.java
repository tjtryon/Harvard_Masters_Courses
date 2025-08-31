/**
 * Date.java
 * Author: TJ Tryon
 * Date: 2025-08-29
 * Course: CSCI 22e - Data Structures
 * Problem Set: PS0 - Precourse Evaluation
 *
 * This program provides a Date class that represents a single calendar date
 * with month, day, and year components. It includes validation, comparison
 * methods, and utility functions for working with dates.
 *
 * Data structures used:
 * - Arrays (for storing month names, day names, and days per month)
 * - Object fields (private instance variables)
 *
 * Key algorithms:
 * - Date validation (leap year calculation, month/day range checking)
 * - Date comparison (before/after/equals logic)
 * - Day of week calculation using mathematical formula
 *
 * Input: Month, day, and year integers for creating Date objects
 * Output: Formatted date strings and comparison results
 */

public class Date {
    // class constants
    public static final int MIN_YEAR = 1583;

    public static final String[] MONTH_NAMES = {
        "",     "January", "February",  "March",   "April",    "May",     "June",
        "July", "August",  "September", "October", "November", "December"};

    public static final String[] DAY_NAMES = {"Sunday",   "Monday", "Tuesday", "Wednesday",
                                              "Thursday", "Friday", "Saturday"};

    public static final int[] NUM_DAYS = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    /**
     * dayOfWeekNumber calculates the day of the week for a given date.
     * Uses a mathematical algorithm to determine the day number.
     *
     * @param month The month (1-12)
     * @param day The day of the month (1-31)
     * @param year The year (must be >= MIN_YEAR)
     * @return The day of the week (0=Sunday, 1=Monday, ..., 6=Saturday)
     */
    public static int dayOfWeekNumber(int month, int day, int year)
    {
        int[] monthCodes = {0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5};
        int centuryCode = (3 - ((year / 100) % 4)) * 2;
        int yearCode = (year % 100) + ((year % 100) / 4);
        int monthCode = monthCodes[month - 1];
        if (isLeapYear(year) && (month == 1 || month == 2))
        {
            monthCode--;
        }
        int dayOfWeek = (centuryCode + yearCode + monthCode + day) % 7;
        return dayOfWeek;
    }

    // static helper methods to be implemented

    /**
     * isLeapYear determines if a given year is a leap year.
     * Most years divisible by 4 are leap years, except years divisible by 100
     * but not divisible by 400.
     *
     * @param year The year to check
     * @return true if the year is a leap year, false otherwise
     */
    public static boolean isLeapYear(int year)
    {
        // Most years divisible by 4 are leap years
        // Exception: years divisible by 100 and not divisible by 400 are not leap years
        if (year % 400 == 0)
        {
            return true;
        }
        else if (year % 100 == 0)
        {
            return false;
        }
        else if (year % 4 == 0)
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    /**
     * numDaysInMonth calculates the number of days in a given month and year.
     * Takes into account leap years for February.
     *
     * @param month The month (1-12)
     * @param year The year (used for leap year calculation)
     * @return The number of days in the specified month
     */
    public static int numDaysInMonth(int month, int year)
    {
        int days = NUM_DAYS[month];

        // Check if it's February in a leap year
        if (month == 2 && isLeapYear(year))
        {
            days = 29;
        }

        return days;
    }

    // instance fields
    private int month;
    private int day;
    private int year;

    /**
     * Date constructor creates a new Date object with validation.
     * Ensures the date is valid according to calendar rules.
     *
     * @param month The month (1-12)
     * @param day The day of the month (1-31, depending on month)
     * @param year The year (must be >= MIN_YEAR)
     * @throws IllegalArgumentException if any parameter is invalid
     */
    public Date(int month, int day, int year)
    {
        // Validate year
        if (year < MIN_YEAR)
        {
            throw new IllegalArgumentException("Year must be >= " + MIN_YEAR);
        }

        // Validate month
        if (month < 1 || month > 12)
        {
            throw new IllegalArgumentException("Month must be between 1 and 12");
        }

        // Validate day
        int daysInMonth = numDaysInMonth(month, year);
        if (day < 1 || day > daysInMonth)
        {
            throw new IllegalArgumentException("Day must be between 1 and " + daysInMonth +
                                               " for month " + month);
        }

        this.month = month;
        this.day = day;
        this.year = year;
    }

    // accessor methods

    /**
     * getMonth returns the month component of this Date.
     *
     * @return The month (1-12)
     */
    public int getMonth()
    {
        return month;
    }

    /**
     * getDay returns the day component of this Date.
     *
     * @return The day of the month (1-31)
     */
    public int getDay()
    {
        return day;
    }

    /**
     * getYear returns the year component of this Date.
     *
     * @return The year
     */
    public int getYear()
    {
        return year;
    }

    /**
     * monthName returns the full name of this Date's month.
     *
     * @return The month name (e.g., "January", "February")
     */
    public String monthName()
    {
        return MONTH_NAMES[month];
    }

    /**
     * dayOfWeekName returns the name of the day of the week for this Date.
     *
     * @return The day name (e.g., "Monday", "Tuesday")
     */
    public String dayOfWeekName()
    {
        int dayNum = dayOfWeekNumber(month, day, year);
        return DAY_NAMES[dayNum];
    }

    /**
     * toString returns a formatted string representation of this Date.
     * Format: "DayName, MonthName day, year"
     *
     * @return A formatted date string
     */
    public String toString()
    {
        return dayOfWeekName() + ", " + monthName() + " " + day + ", " + year;
    }

    // comparison methods

    /**
     * equals determines if this Date is equivalent to another Date.
     * Two dates are equal if they have the same month, day, and year.
     *
     * @param other The Date to compare with (can be null)
     * @return true if dates are equal, false otherwise
     */
    public boolean equals(Date other)
    {
        if (other == null)
        {
            return false;
        }

        return (this.month == other.month && this.day == other.day && this.year == other.year);
    }

    /**
     * isBefore determines if this Date comes chronologically before another Date.
     *
     * @param other The Date to compare with (can be null)
     * @return true if this Date is before the other Date, false otherwise
     */
    public boolean isBefore(Date other)
    {
        if (other == null)
        {
            return false;
        }

        if (this.year < other.year)
        {
            return true;
        }
        else if (this.year > other.year)
        {
            return false;
        }

        // Years are equal, compare months
        if (this.month < other.month)
        {
            return true;
        }
        else if (this.month > other.month)
        {
            return false;
        }

        // Years and months are equal, compare days
        return this.day < other.day;
    }

    /**
     * isAfter determines if this Date comes chronologically after another Date.
     *
     * @param other The Date to compare with (can be null)
     * @return true if this Date is after the other Date, false otherwise
     */
    public boolean isAfter(Date other)
    {
        if (other == null)
        {
            return false;
        }

        return (!this.equals(other) && !this.isBefore(other));
    }
}