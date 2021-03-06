#!/usr/bin/env python
# coding:utf-8

def checkio(number):
    number = bin(number)
    result = 0
    for i in number:
        if i == '1':
            result += 1
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4) == 1
    assert checkio(15) == 4
    assert checkio(1) == 1
    assert checkio(1022) == 9
