#!/usr/bin/env python
#coding:utf-8

def checkio(number):
    result = 1
    if number == 0: 
        return 0
    while number>0:
        ops = number % 10
        number = number // 10
        if ops:
            result = result * ops
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
