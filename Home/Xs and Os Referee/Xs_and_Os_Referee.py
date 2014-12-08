#!/usr/bin/env python
# coding:utf-8

def checkio(game_result):
    '''
    >>> checkio([\
        "X.O",\
        "XX.",\
        "XOO"])
    'X'
    >>> checkio([\
        "OO.",\
        "XOX",\
        "XOX"])
    'O'
    >>> checkio([\
        "OOX",\
        "XXO",\
        "OXX"])
    'D'
    >>> checkio([\
        "O.X",\
        "XX.",\
        "XOO"])
    'X'
    '''
    temp_1 = ""
    temp_2 = ""
    for x in range(3):
        temp = ""
        temp_1 += game_result[x][x]
        temp_2 += game_result[x][2 - x]
        for y in range(3):
            temp += game_result[y][x]
        game_result.append(temp)
#        print(temp)
    game_result.append(temp_1)
    game_result.append(temp_2)
    for result in game_result:
        has_winner = True
        for ch in result:
            if ch != result[0] or ch == '.':
                has_winner = False
        if has_winner:
            return result[0]
    return "D"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    import doctest
    doctest.testmod()
    '''
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    '''
