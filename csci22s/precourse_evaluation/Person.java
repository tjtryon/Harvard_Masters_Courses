/**
 * Person.java
 * Author: TJ Tryon
 * Date: 2025-08-29
 * Course: CSCI 22e - Data Structures
 * Problem Set: PS0 - Precourse Evaluation
 *
 * This program provides a Person class that represents an individual person
 * with a name and date of birth. It includes methods for calculating ages
 * and determining birthdays in different years.
 *
 * Data structures used:
 * - Object fields (private instance variables)
 * - Date objects (composition relationship)
 *
 * Key algorithms:
 * - Age calculation based on dates
 * - Birthday determination for any given year
 * - String validation and null checking
 *
 * Input: Person name (String) and date of birth (Date object)
 * Output: Person information, ages, and birthday dates
 */

public class Person {
    // instance fields
    private String name;
    private Date dateOfBirth;

    /**
     * Person constructor creates a new Person object with validation.
     * Ensures the name is not null or empty and dateOfBirth is not null.
     *
     * @param name The person's name (cannot be null or empty)
     * @param dateOfBirth The person's date of birth (cannot be null)
     * @throws IllegalArgumentException if any parameter is invalid
     */
    public Person(String name, Date dateOfBirth)
    {
        if (name == null)
        {
            throw new IllegalArgumentException("Name cannot be null");
        }
        if (name.equals(""))
        {
            throw new IllegalArgumentException("Name cannot be empty");
        }
        if (dateOfBirth == null)
        {
            throw new IllegalArgumentException("Date of birth cannot be null");
        }

        this.name = name;
        this.dateOfBirth = dateOfBirth;
    }

    /**
     * getName returns this person's name.
     *
     * @return The person's name as a String
     */
    public String getName()
    {
        return name;
    }

    /**
     * getDOB returns this person's date of birth.
     *
     * @return The person's date of birth as a Date object
     */
    public Date getDOB()
    {
        return dateOfBirth;
    }

    /**
     * getBirthdayIn creates a Date for this person's birthday in a given year.
     * Uses the same month and day as the person's birth date.
     *
     * @param year The year for which to calculate the birthday
     * @return A Date object representing the birthday in the specified year
     */
    public Date getBirthdayIn(int year)
    {
        int birthMonth = dateOfBirth.getMonth();
        int birthDay = dateOfBirth.getDay();

        return new Date(birthMonth, birthDay, year);
    }

    /**
     * getAgeOn calculates this person's age on a specific date.
     * Takes into account whether the birthday has occurred yet in that year.
     *
     * @param date The date for which to calculate the age (cannot be null)
     * @return The person's age in years on the specified date
     * @throws IllegalArgumentException if date is null or before date of birth
     */
    public int getAgeOn(Date date)
    {
        if (date == null)
        {
            throw new IllegalArgumentException("Date cannot be null");
        }

        if (date.isBefore(dateOfBirth))
        {
            throw new IllegalArgumentException("Date cannot be before date of birth");
        }

        int age = date.getYear() - dateOfBirth.getYear();

        // Check if birthday has occurred yet this year
        Date birthdayThisYear = getBirthdayIn(date.getYear());

        if (date.isBefore(birthdayThisYear))
        {
            age--;
        }

        return age;
    }

    /**
     * toString returns a formatted string representation of this Person.
     * Format: "Name (born on DateString)"
     *
     * @return A formatted person description string
     */
    public String toString()
    {
        return name + " (born on " + dateOfBirth + ")";
    }
}