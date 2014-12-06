#!/usr/bin/env python
# coding:utf-8

def checkio(first, second):
    '''
    >>> checkio("hello,world", "hello,earth") == "hello"
    True
    >>> checkio("one,two,three", "four,five,six") == ""
    True
    >>> checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two"
    True
    '''
    result = set(first.split(',')).intersection(second.split(','))
    result = list(result)
    result.sort()
    res_str = ""
    if result:
        res_str = result[0]
    if len(result) > 1:
        for x in result[1:]:
            res_str = res_str + ',' + x
    return res_str

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
#    import doctest
#    doctest.testmod()
#    '''
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
#    '''
