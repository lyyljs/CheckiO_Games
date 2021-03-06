#!/usr/bin/env python
#coding:utf-8

import math

def checkio(height, width):
    a, c = width / 2, height / 2
    v = 4 * math.pi / 3 * a ** 2 * c
    
    if a > c:
        e2 = 1 - c ** 2 / a ** 2
        e = e2 ** 0.5
        s = 2 * math.pi * a ** 2 * (1 + (1 - e2) / e * math.atanh(e)) 
    else:
        if a < c:
            e = (1 - a ** 2 / c ** 2) ** 0.5
            s = 2 * math.pi * a ** 2 * (1 + c / (a * e) * math.asin(e))
        else:
            s = 4 * math.pi * a ** 2
    
    return [math.ceil(v * 100) / 100, math.ceil(s * 100) / 100]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 2) == [8.38, 21.48], "Prolate spheroid"
    assert checkio(2, 2) == [4.19, 12.57], "Sphere"
    assert checkio(2, 4) == [16.76, 34.69], "Oblate spheroid"
