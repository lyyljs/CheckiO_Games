#!/usr/bin/env python
# coding:utf-8

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    '''
    >>> checkio("My name is ...")
    3
    >>> checkio("Hello world")
    0
    >>> checkio("A quantity of striped words.")
    1
    >>> checkio("Dog,cat,mouse,bird.Human.")
    3
    '''
    text = text.upper()
    import re, string
    words = re.split('[' + string.punctuation + ' ]', text)
    count = 0
    for word in words:
        is_striped = 0
        if len(word) > 1:
            is_striped = 1
            for x in re.split('[' + VOWELS + ']', word):
                if len(x) > 1:
                    is_striped = 0
            for x in re.split('[' + CONSONANTS + ']', word):
                if len(x) > 1:
                    is_striped = 0
        count += is_striped
    return count

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    import doctest
    doctest.testmod()
