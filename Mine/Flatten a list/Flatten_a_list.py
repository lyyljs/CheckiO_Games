def flat_list(array):
    '''
    >>> flat_list([1, 2, 3])
    [1, 2, 3]
    >>> flat_list([1, [2, 2, 2], 4])
    [1, 2, 2, 2, 4]
    >>> flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]])
    [2, 4, 5, 6, 6, 6, 6, 6, 7]
    >>> flat_list([-1, [1, [-2], 1], -1])
    [-1, 1, -2, 1, -1]
    '''
    a = str(array)
    r = []
    import re
    for i in re.findall('\d+|-\d+', a):
        r.append(int(i))
    return r
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()


