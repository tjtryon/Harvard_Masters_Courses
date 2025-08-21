# 📘 Sample Problems

## 📘 Overview
The following sample problems offer a sense of the level of programming proficiency that is required of students who are planning to take **Computer Science E-22/S-22**.  
If you do not have the necessary level of proficiency, you may want to consider first taking **Computer Science E-10b**.

---

## 📘 Problem 1: Array Practice

📝 Write a method with the header:

```java
public static void swapPairs(int[] arr)
```

💻 This method swaps adjacent pairs in an array.  

Example:

```java
int[] values = {0, 2, 4, 6, 8, 10};
```

After calling `swapPairs(values)`:

```
{2, 0, 6, 4, 10, 8}
```

⚠️ Notes:
- In an odd-length array, the last element stays in place.  
- If `arr` is `null`, throw **IllegalArgumentException**.

---

## 📘 Problem 2: Object-Oriented Programming

🎯 Implement two classes:
- 📅 **Date**
- 👤 **Person**

And complete a client program using them.

---

### 🔹 Step 1: Starter Code
- 📝 Download `Date.java`.  
- Review constants and starter code.

---

### 🔹 Step 2: Static Helper Methods
Implement in `Date.java`:

1. **isLeapYear(int year)**  
   - Returns `true` if leap year, else `false`.  
   - Rules:
     - Divisible by 4 ✅
     - Divisible by 100 ❌ (unless divisible by 400 ✅)

   💻 Example:  
   - `1900` → not leap year  
   - `2000` → leap year  

2. **numDaysInMonth(int month, int year)**  
   - Returns number of days in month/year.  
   - Accounts for leap years.

   💻 Example:  
   - `numDaysInMonth(2, 2012)` → `29`

---

### 🔹 Step 3: Date Fields
- `month` (1–12)  
- `day`  
- `year`  

💻 Example (`11/28/2013`):

```
+----------------+
| month |   11   |
| day   |   28   |
| year  | 2013   |
+----------------+
```

---

### 🔹 Step 4: Date Constructor
Rules:  
- Year ≥ 1583  
- Month = 1–12  
- Day valid for month/year  
- ⚠️ Throw exception if invalid  

---

### 🔹 Step 5: Accessor Methods
- `getMonth()`  
- `getDay()`  
- `getYear()`  
- `monthName()` → `"November"`  
- `dayOfWeekName()` → `"Thursday"`  
- `toString()` → `"Thursday, November 28, 2013"`

---

### 🔹 Step 6: Comparison Methods
- `equals(Date d)`  
- `isBefore(Date d)`  
- `isAfter(Date d)`

---

### 🔹 Step 7: Person Class
Fields:  
- 👤 `name` (String)  
- 📅 `dob` (Date)  

💻 Example:

```java
Person kate = new Person("Kate Winslet", new Date(10, 5, 1975));
```

---

### 🔹 Step 8: Person Accessors
- `getName()`  
- `getDOB()`  
- `getBirthdayIn(int year)` → returns new Date with same month/day in given year  
- `getAgeOn(Date d)` → returns age in years, throws if date before DOB  
- `toString()` → `"Kate Winslet (born on Sunday, October 5, 1975)"`

---

### 🔹 Step 9: BirthdayCalculator Program
- Complete `printBirthdays` method.  
- Prints each person’s name, birthday, and age in given year.  

---

## 📘 Client Programs
📝 Provided for testing:

- `DateClient1.java` → tests parts 2, 4, 5  
- `DateClient2.java` → tests comparison methods  
- `PersonClient.java` → tests `Person`  
- `BirthdayCalculator.java` → final program

---

## 📘 Implementation Guidelines
- 🔒 Encapsulation  
- ♻️ Avoid redundant code  
- ✨ Use clean style (indentation, names, comments)

---

## 📘 Problem 3: Recursion and Strings

File: **StringRecursion.java**  
⚠️ Rules:
- Must use recursion (❌ no loops)  
- No global variables  

---

### 🔹 Method 1: printWithSpaces
```java
public static void printWithSpaces(String str)
```

💻 Example:  
`"space"` → `s p a c e`  

Special cases:  
- `null` or `""` → just print newline

---

### 🔹 Method 2: weave
```java
public static String weave(String str1, String str2)
```

💻 Examples:
- `weave("aaaa","bbbb")` → `"abababab"`  
- `weave("hello","world")` → `"hweolrllod"`  
- `weave("recurse","NOW")` → `"rNeOcWurse"`  

⚠️ Rules:
- Extra chars from longer string go at end.  
- Throw **IllegalArgumentException** if `null`.  
- Empty string returns the other string.

---

🕒 *Last updated: July 13, 2024*
