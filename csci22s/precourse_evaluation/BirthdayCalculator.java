/**
 * BirthdayCalculator.java
 * Author: TJ Tryon
 * Date: 2025-08-29
 * Course: CSCI 22e - Data Structures
 * Problem Set: PS0 - Precourse Evaluation
 *
 * This program calculates and displays people's birthdays and ages
 * for the current year and any specified year. It demonstrates the
 * use of the Date and Person classes in a practical application.
 *
 * Data structures used:
 * - Arrays (for storing Person objects)
 * - Date objects (for representing dates)
 * - Person objects (for storing people's information)
 *
 * Key algorithms:
 * - User input processing and validation
 * - Birthday calculation for different years
 * - Age calculation on specific dates
 *
 * Input: Number of people, their names and birth dates, and a target year
 * Output: Birthday information and ages for current year and specified year
 */

import java.util.*;

public class BirthdayCalculator {
    /**
     * getPeople reads information for multiple people from user input.
     * Prompts for each person's name and date of birth, then creates
     * Person objects and stores them in an array.
     *
     * @param count The number of people to process
     * @param console The Scanner object for reading user input
     * @return An array of Person objects containing the entered information
     */
    public static Person[] getPeople(int count, Scanner console)
    {
        Person[] people = new Person[count];

        for (int i = 0; i < count; i++)
        {
            System.out.println("person " + (i + 1) + ": ");
            System.out.print("  name: ");
            String name = console.nextLine();

            System.out.print("  date of birth (m/d/yyyy): ");
            String dobString = console.nextLine();
            String[] dobComponents = dobString.split("/");
            int month = Integer.parseInt(dobComponents[0]);
            int day = Integer.parseInt(dobComponents[1]);
            int year = Integer.parseInt(dobComponents[2]);

            Date dob = new Date(month, day, year);
            people[i] = new Person(name, dob);
        }

        return people;
    }

    /**
     * printBirthdays displays birthday information for all people in the array.
     * For each person, shows their name, birthday date in the specified year,
     * and their age on that birthday.
     *
     * @param people An array of Person objects to process
     * @param year The year for which to calculate birthdays and ages
     */
    public static void printBirthdays(Person[] people, int year)
    {
        for (int i = 0; i < people.length; i++)
        {
            Person person = people[i];
            String name = person.getName();
            Date birthday = person.getBirthdayIn(year);
            int age = person.getAgeOn(birthday);

            System.out.println(name + ": " + birthday + " (age " + age + ")");
        }
    }

    /**
     * The main method runs when the program starts.
     * It prompts the user for people's information, then displays
     * their birthdays and ages for both the current year and
     * a user-specified year.
     *
     * @param args Command line arguments (not used in this program)
     */
    public static void main(String[] args)
    {
        Scanner console = new Scanner(System.in);

        /* Create a Date object for today. You don't need to understand this code.*/
        GregorianCalendar cal = new GregorianCalendar();
        Date today = new Date(cal.get(cal.MONTH) + 1, cal.get(cal.DAY_OF_MONTH), cal.get(cal.YEAR));

        System.out.println("Welcome to the Birthday Calculator!");
        System.out.println("Today is " + today + ".");
        System.out.println();

        // Get information about the people.
        System.out.print("How many people do you want to process? ");
        int numPeople = console.nextInt();
        console.nextLine();
        Person[] people = getPeople(numPeople, console);
        System.out.println();

        // Print out their birthdays this year.
        System.out.println("Here are their birthdays this year:");
        printBirthdays(people, today.getYear());
        System.out.println();

        // Print out their birthdays in some other year.
        System.out.print("Enter a year >= " + Date.MIN_YEAR + ": ");
        int otherYear = console.nextInt();
        System.out.println("Here are their birthdays in that year:");
        printBirthdays(people, otherYear);
    }
}
