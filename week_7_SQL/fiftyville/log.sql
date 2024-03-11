-- Keep a log of any SQL queries you execute as you solve the mystery.
-- Execute .schema to see the db structure
-- Execute "SELECT * FROM crime scene reports;" to view reports
-- NOTE: Entry 295|2023|7|28|Humphrey Street| Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery.
-- Execute "SELECT * FROM interviews WHERE month = 7 and day = 28;" to find relevant interview transcripts
-- NOTE: Ruth states sometime within 10min of these thief left in car from bakery parking lot. CHECK seurity footage for cars leaving between 1005 and 1025.
-- NOTE: Eugene states thief seen earlier that morning withdrawing money on Leggett Street
-- NOTE: As thief left bakery they called someone, call was <1min, mentioned leaving on earliest flight tomorrow and asked person to book ticket.
-- Execute "SELECT * FROM atm_transactions WHERE month = 7 and day = 28 and atm_location = 'Leggett Street';" to view transactions
-- NOTE: 9 transactions total with 8 withdraws. No timestamps, will need to check accounts.
-- Execute "SELECT * FROM bank_accounts WHERE account_number IN
   --...> (SELECT account_number FROM atm_transactions WHERE month = 7 and day = 28 and atm_location = 'Leggett Street' and transaction_type = 'withdraw');"
    -- To see the person_id of who made transactions from that location.
-- NOTE: 8 person_id found.
-- EXECUTE "SELECT * FROM phone_calls WHERE month = 7 and day = 28 and duration < 60;" to find caller numbers
-- NOTE: Total of 9 calls identified
-- EXECUTE "SELECT * FROM bakery_security_logs WHERE day = 28 AND month = 7;" to find licence plates that match witness reports.
-- NOTE: A total of 8 vehicles exit between 1016 and 1023.

-- Execute the below command to try and isolate thief:
-- SELECT * FROM people WHERE id IN
--  (SELECT person_id FROM bank_accounts WHERE account_number IN
--  (SELECT account_number FROM atm_transactions WHERE month = 7 and day = 28 and atm_location = 'Leggett Street' and transaction_type = 'withdraw'))
--  AND phone_number IN (SELECT caller FROM phone_calls WHERE month = 7 and day = 28 and duration < 60)
--  AND license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE month = 7 and day = 28 and hour = 10 and minute > 15 and minute < 25);
-- NOTE: TWO MATCHES FOUND, Diana (ID 514354) and Bruce (ID 686048)

-- Execute "SELECT * FROM passengers WHERE passport_number = 3592750733 or passport_number = 5773159633;" hoping that we can isolate our list down to a single person.
-- NOTE: FOUR flights returned with Bruce taking flight 36 and Diana taking flights 18, 24 and 54.

-- Execute "SELECT * FROM flights WHERE id = 18 or id = 24 or id = 36 or id = 54;" to look at flights
-- NOTE: Only flight id 36 left on the morning of 29/7 and it was BRUCE. Now where is destination airport 4...

-- Execute "SELECT * from airports WHERE id = 4;"
-- Note: Bruce flew to LaGuardia Airport, New York City.

-- Execute "SELECT name FROM people WHERE phone_number = '(375) 555-8161';" to find the accomplice
-- NOTE: Bruce called Robin.
