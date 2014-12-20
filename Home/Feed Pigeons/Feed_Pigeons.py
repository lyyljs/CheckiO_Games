#!/usr/bin/env python
# coding:utf-8

def checkio(number):
    i = 0
    sum = 0
    while number > 0:
        i += 1
        sum += i
        number -= sum
        
    if number < 0:
        sum -= i
        if i + number > 0:
            sum += i + number
    return sum

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
