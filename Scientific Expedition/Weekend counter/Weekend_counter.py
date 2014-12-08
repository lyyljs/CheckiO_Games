#!/usr/bin/env python
# coding:utf-8

from datetime import date


def checkio(from_date, to_date):
    """
        Count the days of rest
    """
    total_days = to_date - from_date
    total_days = total_days.days + 1
    result = total_days // 7 * 2
    for i in range(from_date.weekday(), from_date.weekday() + total_days % 7):
        if i in [5, 6, 11]:
            result += 1
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"

