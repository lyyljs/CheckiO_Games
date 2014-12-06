#!/usr/bin/env python
# coding:utf-8

def get_Fibonacci():
    result = [0, 1, 2]
    i = 2
    while i < 30:
        temp = result[i-1] + result[i]
        result.append(temp)
        i += 1
    return result

def checkio(opacity):
    Fibonacci = get_Fibonacci()
    ghost_opacity = 10000
    year = 0
    while year <= 5000:           
        if year in Fibonacci:
            ghost_opacity -= year            
        else:
            ghost_opacity += 1
        if opacity == ghost_opacity:
            break 
        year += 1
    return year

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"
