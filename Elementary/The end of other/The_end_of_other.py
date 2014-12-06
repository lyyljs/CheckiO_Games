#!/usr/bin/env python
# coding:utf-8

def checkio(words_set):
    '''
    >>> checkio({"hello", "lo", "he"})
    True
    >>> checkio({"hello", "la", "hellow", "cow"})
    False
    >>> checkio({"walk", "duckwalk"})
    True
    >>> checkio({"one"}) 
    False
    >>> checkio({"helicopter", "li", "he"})
    False
    '''
    import re
    words = list(words_set)
    words.sort(key=len)
    for i in range(len(words)):
        re_word = re.compile(".+?" + words[i] + "$")
        for word in words[-i:]:
            if re_word.match(word):
                return True
    return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    '''
    assert checkio({"hello", "lo", "he"}) == True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
    assert checkio({"one"}) == False, "Only One"
    assert checkio({"helicopter", "li", "he"}) == False, "Only end"
    '''
