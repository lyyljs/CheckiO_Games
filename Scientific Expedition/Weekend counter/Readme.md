Sofia has given you a schedule and two dates and told you she needs help planning her weekends. She has asked you to count each day of rest (Saturday and Sunday) starting from the initial date to final date. You should count the initial and final dates if they fall on a Saturday or Sunday.

The dates are given as datetime.date (Read about this module here). The result is an integer.

Input: Start and end date as datetime.date.

Output: The quantity of the rest days as an integer.

Example:

checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2

checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8

checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2


How it is used: Now is a good time to learn how to work with dates. These ideas here often come up in calendar apps, customer relation management software, automated messaging schedulers among many other things.

Precondition: start_date < end_date.
