#!/usr/bin/env python
# coding: utf-8

def get_number(char):
    if char.isdigit() or char.isalpha():
        return int(char, base = 36)
    else:
        return -1

def checkio(str_number, radix):
    '''
    >>> checkio("AF", 16)
    175
    >>> checkio("101", 2)
    5
    >>> checkio("101", 5)
    26
    >>> checkio("Z", 36)
    35
    >>> checkio("AB", 10)
    -1
    '''
    try:
        return int(str_number, base = radix)
    except:
        return -1

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
#    import doctest
#    doctest.testmod()
#    '''
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A > 10"
#    '''
