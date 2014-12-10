#!/usr/bin/env python
#coding:utf-8

TLST = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def checkline(x, y, n, m):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    return True

def checkio(field):
    '''
    >>> checkio([\
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],\
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],\
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],\
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],\
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],\
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],\
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],\
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],\
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],\
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],\
])  
    [False, 0, 0]
    >>> checkio([\
    [0, 2, -1, -1, -1, -1, -1, -1, -1, -1],\
    [0, 2, -1, -1, -1, -1, -1, -1, -1, -1],\
    [0, 1, 1, 1, -1, -1, -1, -1, -1, -1],\
    [0, 0, 0, 1, -1, -1, -1, -1, -1, -1],\
    [0, 1, 1, 2, -1, -1, -1, -1, -1, -1],\
    [0, 1, -1, -1, -1, -1, -1, -1, -1, -1],\
    [0, 1, -1, -1, -1, -1, -1, -1, -1, -1],\
    [2, 1, -1, -1, -1, -1, -1, -1, -1, -1],\
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],\
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],\
])  
    [True, 0, 2]
    '''
    if field[0][0] == -1:
        return [False, 0, 0]
    
#    for x in field:
#        print (x)
    
    n, m = len(field), len(field[0])
    for i in range(n):
        for j in range(m):
            if 0 < field[i][j] < 9:
                count_mine, count_uncovered = 0, 0
                x, y = i, j
                temp_lst = []
                for t in TLST:
                    tx, ty = x + t[0], y+t[1]
                    if checkline(tx, ty, n, m):
                        count_mine += field[tx][ty] > 8
                        if field[tx][ty] == -1:
                            count_uncovered += 1
                            temp_lst.append([tx, ty])
                if count_uncovered:
                    if count_mine == field[x][y]:
                        return [False, temp_lst[0][0], temp_lst[0][1]]
                    if count_uncovered == (field[x][y] - count_mine):
                        return [True, temp_lst[0][0], temp_lst[0][1]]

#This part is using only for self-testing
if __name__ == '__main__':
    
#    import doctest
#    doctest.testmod()

    def check_is_win_referee(input_map):
        unopened = [1 for x in range(10) for y in range(10) if input_map[x][y] == -1]
        return not unopened

    def build_map(input_map, mine_map, row, col):
        opened = [(row, col)]
        while opened:
            i, j = opened.pop(0)
            neighs = [(i + x, j + y) for x, y in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
                      if 0 <= i + x < 10 and 0 <= j + y < 10]
            value = sum([mine_map[k][l] for k, l in neighs])
            input_map[i][j] = value
            if not value:
                for k, l in neighs:
                    if input_map[k][l] == -1 and (k, l) not in opened:
                        opened.append((k, l))
        return input_map

    def check_solution(func, mine_map):
        input_map = [[-1] * 10 for _ in range(10)]
        while True:

            is_mine, row, col = func([row[:] for row in input_map])  # using copy
#            print (is_mine, row, col)
            if input_map[row][col] != -1:
                print("You tried to uncover or mark already opened cell.")
                return False
            if is_mine and not mine_map[row][col]:
                print("You marked the wrong cell.")
                return False
            if not is_mine and mine_map[row][col]:
                print("You uncovered a mine. BANG!")
                return False
            if is_mine:
                input_map[row][col] = 9
            else:
                build_map(input_map, mine_map, row, col)
            if check_is_win_referee(input_map):
                return True
        return False
    
    '''
    check_solution(checkio, [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
        
    '''
    assert check_solution(checkio, [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]), "Simple"

    assert check_solution(checkio, [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]), "Gate"

    assert check_solution(checkio, [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]]), "Various"
