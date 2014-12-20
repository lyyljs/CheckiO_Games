#!/usr/bin/env python
#coding:utf-8

def count_gold(pyramid):
    """
    Return max possible sum in a path from top to bottom
    """
    result = list(pyramid)
    n = len(pyramid)
    for i in range(1, n):
        m = len(pyramid[i])
        result[i] = list(result[i])
        for j in range(m):
            if j > 0 and j < m - 1:
                result[i][j] = pyramid[i][j] + max(result[i - 1][j - 1], result[i - 1][j])
            else:
                try:
                    result[i][j] = pyramid[i][j] + result[i - 1][j]
                except:
                    result[i][j] = pyramid[i][j] + result[i - 1][j - 1]
    return max(result[n - 1])


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_gold((
        (1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4),
        (3, 1, 3, 1, 3),
        (2, 2, 2, 2, 2, 2),
        (5, 6, 4, 5, 6, 4, 3)
    )) == 23, "First example"
    assert count_gold((
        (1,),
        (2, 1),
        (1, 2, 1),
        (1, 2, 1, 1),
        (1, 2, 1, 1, 1),
        (1, 2, 1, 1, 1, 1),
        (1, 2, 1, 1, 1, 1, 9)
    )) == 15, "Second example"
    assert count_gold((
        (9,),
        (2, 2),
        (3, 3, 3),
        (4, 4, 4, 4)
    )) == 18, "Third example"
