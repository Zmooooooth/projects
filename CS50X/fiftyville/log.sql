-- Keep a log of any SQL queries you execute as you solve the mystery.
.schema
-- Report
SELECT * FROM crime_scene_reports WHERE street LIKE "%Humphrey Street%" AND month = 7 AND day = 28;
-- Interview
SELECT * FROM interviews WHERE year = 2023 AND month = 7 AND day = 28 AND (name = "Ruth" OR name =  "Eugene" OR name =  "Raymond") AND id > 159;
--Bakery
SELECT * from bakery_security_logs WHERE year = 2023 AND month = 7 AND day = 28 AND hour = 10 AND minute > 15 AND minute <36;
--Airport
SELECT * FROM airports WHERE city = "Fiftyville";
--flight
SELECT * from flights WHERE origin_airport_id = 8 AND year = 2023 AND month = 7 AND day = 29 ORDER BY hour ASC LIMIT 1;
-- ALL Passengers
SELECT * FROM passengers WHERE flight_id = 36;
-- WITHDRAWAL
SELECT * FROM atm_transactions WHERE year = 2023 AND month = 7 AND day = 28 AND atm_location LIKE "%Legget%" AND transaction_type = "withdraw";
-- DEST Airport
SELECT * FROM airports WHERE id =
(SELECT destination_airport_id from flights WHERE origin_airport_id = 8 AND year = 2023 AND month = 7 AND day = 29 ORDER BY hour ASC LIMIT 1);
-- Phone
SELECT * FROM phone_calls WHERE year = 2023 AND month = 7 AND day = 28 AND duration < 60;
-- Phone and License
SELECT * FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE year = 2023 AND month = 7 AND day = 28) AND license_plate IN (SELECT license_plate from bakery_security_logs WHERE year = 2023 AND month = 7 AND day = 28 AND hour = 10 AND minute > 15 AND minute <36);
-- Phone, License and Passport
SELECT * FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE year = 2023 AND month = 7 AND day = 28) AND license_plate IN (SELECT license_plate from bakery_security_logs WHERE year = 2023 AND month = 7 AND day = 28 AND hour = 10 AND minute > 15 AND minute <36) AND passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = 36);
-- The last two people
SELECT * FROM people WHERE id IN ( SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE year = 2023 AND month = 7 AND day = 28 AND atm_location LIKE "%Legget%" AND transaction_type = "withdraw")) AND phone_number IN (SELECT caller FROM phone_calls WHERE year = 2023 AND month = 7 AND day = 28) AND license_plate IN (SELECT license_plate from bakery_security_logs WHERE year = 2023 AND month = 7 AND day = 28 AND hour = 10 AND minute > 15 AND minute <36) AND passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = 36);
-- Validation
SELECT * FROM passengers JOIN people ON people.passport_number = passengers.passport_number WHERE flight_id = 36 AND (name = "Taylor" OR name ="Bruce");
--
SELECT * FROM people WHERE phone_number = (SELECT receiver FROM phone_calls WHERE year = 2023 AND month = 7 AND day = 28 AND duration < 60 AND caller = "(367) 555-5533");
