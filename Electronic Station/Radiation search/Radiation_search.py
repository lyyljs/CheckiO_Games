#!/usr/bin/env python
#coding:utf-8

NEIGHS = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def deep_search(x, y, matrix, unopened):
    n, m = len(matrix), len(matrix[0])
    count = 1
    for t in NEIGHS:
        tx, ty = x + t[0], y + t[1]
        if tx < 0 or ty < 0 or tx >= n or ty >= m or matrix[tx][ty] != matrix[x][y] or unopened[tx][ty] == 0:
            pass
        else:
            unopened[tx][ty] = 0
            count += deep_search(tx, ty, matrix, unopened)
    return count

def checkio(matrix):
    '''
    >>> checkio([\
        [1, 2, 3, 4, 5],\
        [1, 1, 1, 2, 3],\
        [1, 1, 1, 2, 2],\
        [1, 2, 2, 2, 1],\
        [1, 1, 1, 1, 1]\
    ])
    [14, 1]
    >>> checkio([\
        [2, 1, 2, 2, 2, 4],\
        [2, 5, 2, 2, 2, 2],\
        [2, 5, 4, 2, 2, 2],\
        [2, 5, 2, 2, 4, 2],\
        [2, 4, 2, 2, 2, 2],\
        [2, 2, 4, 4, 2, 2]\
    ])
    [19, 2]
    '''
    result = [0, 0]
    n, m = len(matrix), len(matrix[0])
    unopened = []
    for x in range(n):
        temp = []
        for y in range(m):
            temp.append(1)
        unopened.append(temp)
    i, j = 0, 0
    for i in range(n):
        for j in range(m):
            if unopened[i][j]:
                unopened[i][j] = 0
                temp = deep_search(i, j, matrix, unopened)
                if temp > result[0]:
                    result = [temp, matrix[i][j]]
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    '''
    assert checkio([
        [1, 2, 3, 4, 5],
        [1, 1, 1, 2, 3],
        [1, 1, 1, 2, 2],
        [1, 2, 2, 2, 1],
        [1, 1, 1, 1, 1]
    ]) == [14, 1], "14 of 1"

    assert checkio([
        [2, 1, 2, 2, 2, 4],
        [2, 5, 2, 2, 2, 2],
        [2, 5, 4, 2, 2, 2],
        [2, 5, 2, 2, 4, 2],
        [2, 4, 2, 2, 2, 2],
        [2, 2, 4, 4, 2, 2]
    ]) == [19, 2], '19 of 2'
    '''
