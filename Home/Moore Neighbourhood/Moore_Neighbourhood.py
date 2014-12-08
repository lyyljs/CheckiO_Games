#!/usr/bin/env python
#coding:utf-8

def count_neighbours(grid, row, col):
    '''
    >>> count_neighbours(((1, 0, 0, 1, 0),\
                          (0, 1, 0, 0, 0),\
                          (0, 0, 1, 0, 1),\
                          (1, 0, 0, 0, 0),\
                          (0, 0, 1, 0, 0),), 1, 2)
    3
    >>> count_neighbours(((1, 0, 0, 1, 0),\
                          (0, 1, 0, 0, 0),\
                          (0, 0, 1, 0, 1),\
                          (1, 0, 0, 0, 0),\
                          (0, 0, 1, 0, 0),), 0, 0)
    1
    >>> count_neighbours(((1, 1, 1),\
                          (1, 1, 1),\
                          (1, 1, 1),), 0, 2)
    3
    >>> count_neighbours(((0, 0, 0),\
                          (0, 1, 0),\
                          (0, 0, 0),), 1, 1)
    0
    '''
    count = 0
    for fx in range(-1, 2):
        for fy in range(-1, 2):
            x = row + fx
            y = col + fy
#            print('1:', x, y)
#            print('len:', len(grid), len(grid[0]))
            if (x >= 0) & (y >= 0) & (x < len(grid)) & (y < len(grid[0])):
#                print (x, y)
                count += grid[x][y]
    count -= grid[row][col]
    return count


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    import doctest
    doctest.testmod()
    '''
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
    '''
