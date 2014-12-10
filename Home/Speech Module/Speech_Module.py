#!/usr/bin/env python
#coding:utf-8

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    result = ""
    hundred = number // 100
    if hundred:
        result += ' ' + FIRST_TEN[hundred - 1] + ' ' + HUNDRED
    tens = number % 100
    if tens:
        if tens < 20 and tens > 9:
            result += ' ' + SECOND_TEN[tens % 10]
        else:
            first_ten = tens % 10
            other_tens = tens // 10
            if other_tens:
                result += ' ' + OTHER_TENS[other_tens - 2]
            if first_ten:
                result += ' ' + FIRST_TEN[first_ten - 1]
    return result.lstrip()

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
