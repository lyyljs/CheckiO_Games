#!/usr/bin/env python
# coding:utf-8

def checkio(data):
    '''
    >>> checkio([[1, 2, 3],\
                    [4, 5, 6],\
                    [7, 8, 9]])
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    >>> checkio([[1, 4, 3],\
                    [8, 2, 6],\
                    [7, 8, 3],\
                    [4, 9, 6],\
                    [7, 8, 1]])
    [[1, 8, 7, 4, 7], [4, 2, 8, 9, 8], [3, 6, 3, 6, 1]]
    '''
    result = []
    n = len(data)
    m = len(data[0])
    for i in range(m):
        temp = []
        for j in range(n):
            temp.append(data[j][i])
        result.append(temp)
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    assert checkio([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]) == [[1, 4, 7],
                                    [2, 5, 8],
                                    [3, 6, 9]], "Square matrix"
    assert checkio([[1, 4, 3],
                    [8, 2, 6],
                    [7, 8, 3],
                    [4, 9, 6],
                    [7, 8, 1]]) == [[1, 8, 7, 4, 7],
                                    [4, 2, 8, 9, 8],
                                    [3, 6, 3, 6, 1]], "Rectangle matrix"
    
