-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Get the database schema
.schema

-- Find any crime scene reports about a duck, list the Month, Day, Year
SELECT month, day, year, description FROM crime_scene_reports WHERE description LIKE '%duck%';
-- Results:
| 7     | 28  | 2024 | Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery.
Interviews were conducted today with three witnesses who were present at the time – each of their
interview transcripts mentions the bakery. |

-- Get the interviews of the three witnesses
select name, transcript from interviews where transcript LIKE '%bakery%' AND month = "7" AND day = '28' AND year = '2024';
-- Results:
-- | Ruth    | Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery
--    parking lot and drive away. If you have security footage from the bakery parking lot, you might
--    want to look for cars that left the parking lot in that time frame.                                                          |
-- | Eugene  | I don't know the thief's name, but it was someone I recognized. Earlier this morning,
--    before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief
--    there withdrawing some money.                                                                                                 |
-- | Raymond | As the thief was leaving the bakery, they called someone who talked to them for less
--    than a minute. In the call, I heard the thief say that they were planning to take the earliest
--    flightout of Fiftyville tomorrow. The thief then asked the person on the other end of the phone
--    to purchase the flight ticket. |

-- Check bakery security logs for 10 minutes after the theft
select activity, license_plate from bakery_security_logs WHERE month = '7' AND day = '28' AND year = '2024' AND hour = '10' AND minute >=15 AND minute <= 25;
-- Results:
| exit     | 5P2BI95       |
| exit     | 94KL13X       |
| exit     | 6P58WS2       |
| exit     | 4328GD8       |
| exit     | G412CB7       |
| exit     | L93JTIZ       |
| exit     | 322W7JE       |
| exit     | 0NTHK55       |

-- Find out who left the bakery within 10 minutes of the theft
SELECT bakery_security_logs.hour, bakery_security_logs.minute, bakery_security_logs.activity,
    bakery_security_logs.license_plate, people.name
FROM bakery_security_logs
JOIN people ON bakery_security_logs.license_plate = people.license_plate
WHERE month = '7' AND day = '28' AND year = '2024' AND hour = '10' AND minute >=15 AND minute <= 25;
-- Results:
| 10   | 16     | exit     | 5P2BI95       | Vanessa |
| 10   | 18     | exit     | 94KL13X       | Bruce   |
| 10   | 18     | exit     | 6P58WS2       | Barry   |
| 10   | 19     | exit     | 4328GD8       | Luca    |
| 10   | 20     | exit     | G412CB7       | Sofia   |
| 10   | 21     | exit     | L93JTIZ       | Iman    |
| 10   | 23     | exit     | 322W7JE       | Diana   |
| 10   | 23     | exit     | 0NTHK55       | Kelsey  |

-- ATM Transaction Withdraw from Leggett Street
SELECT people.name, atm_transactions.atm_location,
atm_transactions.transaction_type, atm_transactions.account_number from atm_transactions
JOIN bank_accounts ON bank_accounts.account_number = atm_transactions.account_number
JOIN people ON bank_accounts.person_id = people.id
WHERE atm_transactions.month = '7' AND atm_transactions.day = '28' AND atm_transactions.year = '2024'
AND atm_transactions.atm_location = 'Leggett Street' AND atm_transactions.transaction_type = 'withdraw';
-- Results
| Bruce   | Leggett Street | withdraw         | 49610011       |
| Diana   | Leggett Street | withdraw         | 26013199       |
| Brooke  | Leggett Street | withdraw         | 16153065       |
| Kenny   | Leggett Street | withdraw         | 28296815       |
| Iman    | Leggett Street | withdraw         | 25506511       |
| Luca    | Leggett Street | withdraw         | 28500762       |
| Taylor  | Leggett Street | withdraw         | 76054385       |
| Benista | Leggett Street | withdraw         | 81061156       |

-- Who made a phone call when leaving the bakery
SELECT phone_calls.caller, c.name, phone_calls.receiver, r.name, phone_calls.duration
FROM phone_calls
JOIN people AS c ON c.phone_number = phone_calls.caller
JOIN people AS r ON r.phone_number = phone_calls.receiver
WHERE phone_calls.month = '7' AND phone_calls.day = '28' AND phone_calls.year = '2024'
AND duration < '60';
-- Results:
|     caller     |  name   |    receiver    |    name    | duration |
+----------------+---------+----------------+------------+----------+
| (130) 555-0289 | Sofia   | (996) 555-8899 | Jack       | 51       |
| (499) 555-9472 | Kelsey  | (892) 555-8872 | Larry      | 36       |
| (367) 555-5533 | Bruce   | (375) 555-8161 | Robin      | 45       |
| (499) 555-9472 | Kelsey  | (717) 555-1342 | Melissa    | 50       |
| (286) 555-6063 | Taylor  | (676) 555-6554 | James      | 43       |
| (770) 555-1861 | Diana   | (725) 555-3243 | Philip     | 49       |
| (031) 555-6622 | Carina  | (910) 555-3251 | Jacqueline | 38       |
| (826) 555-1652 | Kenny   | (066) 555-9701 | Doris      | 55       |
| (338) 555-6650 | Benista | (704) 555-2131 | Anna       | 54       |

-- So far, only Bruce and Diana match the information of the thief from the interview
-- Now to find out who was flying, and where
SELECT people.name, flights.hour, flights.minute, o.full_name, d.full_name FROM people
JOIN passengers ON people.passport_number = passengers.passport_number
JOIN flights ON passengers.flight_id = flights.id
JOIN airports AS o ON o.id = flights.origin_airport_id
JOIN airports AS d ON d.id = flights.destination_airport_id
WHERE flights.month = '7' AND flights.day = '29' AND flights.year = '2024'
AND o.full_name = 'Fiftyville Regional Airport' ORDER BY hour ASC, minute ASC;
-- Results:
+-----------+------+--------+-----------------------------+-------------------------------------+
|   name    | hour | minute |          full_name          |              full_name              |
+-----------+------+--------+-----------------------------+-------------------------------------+
| Doris     | 8    | 20     | Fiftyville Regional Airport | LaGuardia Airport                   |
| Sofia     | 8    | 20     | Fiftyville Regional Airport | LaGuardia Airport                   |
| Bruce     | 8    | 20     | Fiftyville Regional Airport | LaGuardia Airport                   |
| Edward    | 8    | 20     | Fiftyville Regional Airport | LaGuardia Airport                   |
| Kelsey    | 8    | 20     | Fiftyville Regional Airport | LaGuardia Airport                   |
| Taylor    | 8    | 20     | Fiftyville Regional Airport | LaGuardia Airport                   |
| Kenny     | 8    | 20     | Fiftyville Regional Airport | LaGuardia Airport                   |
| Luca      | 8    | 20     | Fiftyville Regional Airport | LaGuardia Airport                   |
| Daniel    | 9    | 30     | Fiftyville Regional Airport | O'Hare International Airport        |
| Carol     | 9    | 30     | Fiftyville Regional Airport | O'Hare International Airport        |
| Rebecca   | 9    | 30     | Fiftyville Regional Airport | O'Hare International Airport        |
| Sophia    | 9    | 30     | Fiftyville Regional Airport | O'Hare International Airport        |
| Heather   | 9    | 30     | Fiftyville Regional Airport | O'Hare International Airport        |
| Marilyn   | 9    | 30     | Fiftyville Regional Airport | O'Hare International Airport        |
| Dennis    | 12   | 15     | Fiftyville Regional Airport | San Francisco International Airport |
| Jose      | 12   | 15     | Fiftyville Regional Airport | San Francisco International Airport |
| Jennifer  | 12   | 15     | Fiftyville Regional Airport | San Francisco International Airport |
| Brandon   | 12   | 15     | Fiftyville Regional Airport | San Francisco International Airport |
| Matthew   | 12   | 15     | Fiftyville Regional Airport | San Francisco International Airport |
| Emily     | 12   | 15     | Fiftyville Regional Airport | San Francisco International Airport |
| Douglas   | 12   | 15     | Fiftyville Regional Airport | San Francisco International Airport |
| Jordan    | 12   | 15     | Fiftyville Regional Airport | San Francisco International Airport |
| Richard   | 15   | 20     | Fiftyville Regional Airport | Tokyo International Airport         |
| Thomas    | 15   | 20     | Fiftyville Regional Airport | Tokyo International Airport         |
| Brooke    | 15   | 20     | Fiftyville Regional Airport | Tokyo International Airport         |
| Larry     | 15   | 20     | Fiftyville Regional Airport | Tokyo International Airport         |
| Steven    | 15   | 20     | Fiftyville Regional Airport | Tokyo International Airport         |
| John      | 15   | 20     | Fiftyville Regional Airport | Tokyo International Airport         |
| Pamela    | 15   | 20     | Fiftyville Regional Airport | Tokyo International Airport         |
| Melissa   | 15   | 20     | Fiftyville Regional Airport | Tokyo International Airport         |
| Gloria    | 16   | 0      | Fiftyville Regional Airport | Logan International Airport         |
| Kristina  | 16   | 0      | Fiftyville Regional Airport | Logan International Airport         |
| Douglas   | 16   | 0      | Fiftyville Regional Airport | Logan International Airport         |
| Diana     | 16   | 0      | Fiftyville Regional Airport | Logan International Airport         |
| Christian | 16   | 0      | Fiftyville Regional Airport | Logan International Airport         |
| Michael   | 16   | 0      | Fiftyville Regional Airport | Logan International Airport         |
| Ethan     | 16   | 0      | Fiftyville Regional Airport | Logan International Airport         |
| Charles   | 16   | 0      | Fiftyville Regional Airport | Logan International Airport         |


-- Bruce is the only one who matches all queries, phone call was with Robin, his acomplace
