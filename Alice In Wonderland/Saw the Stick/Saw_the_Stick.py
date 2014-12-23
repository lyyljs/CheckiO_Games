#!/usr/bin/env python
#coding:utf-8

def get_triangular_numbers():
    number, i = 0, 1
    tri_numbers = []
    while number < 1000:
        number += i
        tri_numbers.append(number)
        i += 1
    return tri_numbers

def get_numbers(number, tri_numbers):
    result = []
    length = len(tri_numbers)
    for i in range(length):
        j, temp = i, [0, ]
        while temp[0] < number and j < length:
            temp[0] += tri_numbers[j]
            temp.append(tri_numbers[j])
            j += 1
        if temp[0] == number:
            return temp[1:]
    return result

def checkio(number):
    tri_numbers, result = [], []
    tri_numbers = get_triangular_numbers()
    result = get_numbers(number, tri_numbers)
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(64) == [15, 21, 28], "1st example"
    assert checkio(371) == [36, 45, 55, 66, 78, 91], "1st example"
    assert checkio(225) == [105, 120], "1st example"
    assert checkio(882) == [], "1st example"
