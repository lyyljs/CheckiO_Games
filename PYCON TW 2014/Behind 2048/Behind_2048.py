#!/usr/bin/env python
# coding:utf-8

GAMEOVER =  [['G', 'A', 'M', 'E'],
                                                   ['O', 'V', 'E', 'R'],
                                                   ['G', 'A', 'M', 'E'],
                                                   ['O', 'V', 'E', 'R']]

YOUWIN = [['U', 'W', 'I', 'N'],
                                                      ['U', 'W', 'I', 'N'],
                                                      ['U', 'W', 'I', 'N'],
                                                      ['U', 'W', 'I', 'N']]

def insert2toEnd(state):
    i = 3
    while i >= 0:
        j = 3
        while j >= 0:
            if state[i][j] == 0:
                state[i][j] = 2
                return state
            j -= 1
        i -=1
    return GAMEOVER

def rightMove(state):
    for i in range(4):
        j = 3
        #merge
        while j >= 0:
            while state[i][j] == 0:
                j -= 1
                if j <= 0:
                    break
            k = j - 1
            while k >= 0:
                if state[i][k] > 0:
                    if state[i][j] == state[i][k]:
                        state[i][j] *= 2
                        state[i][k] = 0
                        j = k
                    break
                k -= 1
            j -= 1
        #get order
        temp = []
        while 0 in state[i]:
            state[i].remove(0)
            temp.append(0)
        state[i] = temp + state[i]
    return state

def leftMove(state):
    for i in range(4):
        j = 0
        #merge
        while j < 4:
            while state[i][j] == 0:
                j += 1
                if j >= 3:
                    break
            k = j + 1
            while k < 4:
                if state[i][k] > 0:
                    if state[i][j] == state[i][k]:
                        state[i][j] *= 2
                        state[i][k] = 0
                        j = k
                    break
                k += 1
            j += 1
        #get order
        temp = []
        while 0 in state[i]:
            state[i].remove(0)
            temp.append(0)
        state[i] = state[i] + temp
    return state

def upMove(state):
    for i in range(4):
        j = 0
        #merge
        while j < 4:
            while state[j][i] == 0:
                j += 1
                if j >= 3:
                    break
            k = j + 1
            while k < 4:
                if state[k][i] > 0:
                    if state[j][i] == state[k][i]:
                        state[j][i] *= 2
                        state[k][i] = 0
                        j = k
                    break
                k += 1
            j += 1
        #get order
        j = 0
        while j < 3:
            if state[j][i] == 0:
                k = j + 1
                while state[k][i] == 0:
                    if k >= 3:
                        break
                    k += 1
                state[j][i] = state[k][i]
                state[k][i] = 0
            j += 1
    return state

def downMove(state):
    for i in range(4):
        #print('before:',  state)
        j = 3
        #merge
        while j >= 0:
            while state[j][i] == 0:
                j -= 1
                if j <= 0:
                    break
            k = j - 1 
            while k >= 0:
                if state[k][i] > 0:
                    if state[j][i] == state[k][i]:
                        state[j][i] *= 2
                        state[k][i] = 0
                        j = k
                    break
                k -= 1
            j -= 1
        #get order
        j = 3
        while j > 0:
            if state[j][i] == 0:
                k = j - 1
                #print('after if j:',  j)
                while state[k][i] == 0:
                    if k <= 0:
                        break
                    k -= 1
                state[j][i] = state[k][i]
                #print('k: ', k ,  '; i:',  i,  '; j: ',  j)
                state[k][i] = 0
            j -= 1
            #print(state)
        #print('after:',  state)
    return state

def move2048(state, move):
    if move == "right":
        state = rightMove(state)
    elif move == "left":
        state = leftMove(state)
    elif move == "up":
        state = upMove(state)
    else:
        state = downMove(state)
    #check success
    for i in range(4):
        for j in range(4):
            if state[i][j] == 2048:
                return YOUWIN
    state = insert2toEnd(state)
    return state


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    test1 = move2048([[4, 0, 0, 0],
                     [0, 4, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 8, 8]], 'right')
    assert test1 == [[0, 0, 0, 4],
                                                 [0, 0, 0, 4],
                                                 [0, 0, 0, 0],
                                                 [0, 0, 2, 16]], "Simple right"
    assert move2048([[2, 0, 2, 2],
                     [0, 4, 4, 4],
                     [8, 8, 8, 16],
                     [0, 0, 0, 0]], 'right') == [[0, 0, 2, 4],
                                                 [0, 0, 4, 8],
                                                 [0, 8, 16, 16],
                                                 [0, 0, 0, 2]], "Three merging"
    assert move2048([[2, 0, 2, 4],
                     [0, 4, 4, 4],
                     [8, 8, 8, 16],
                     [0, 0, 0, 0]], 'down') == [[0, 0, 0, 0],
                                                 [0, 0, 2, 2],
                                                 [2, 4, 4, 8],
                                                 [8, 8, 8, 16]], "Three merging"
    assert move2048([[2, 0, 2, 2],
                     [0, 4, 4, 4],
                     [8, 8, 8, 16],
                     [0, 0, 0, 0]], 'left') == [[4, 2, 0, 0],
                                                 [8, 4, 0, 0],
                                                 [16, 8, 16, 0],
                                                 [0, 0, 0, 2]], "Three merging"
    assert move2048([[256, 0, 256, 4],
                     [16, 8, 8, 0],
                     [32, 32, 32, 32],
                     [4, 4, 2, 2]], 'right') == [[0, 0, 512, 4],
                                                 [0, 0, 16, 16],
                                                 [0, 0, 64, 64],
                                                 [0, 2, 8, 4]], "All right"
    assert move2048([[2, 4, 8, 16],
                     [32, 64, 128, 256],
                     [512, 1024, 2, 4],
                     [8, 16, 32, 64]], 'left') == [['G', 'A', 'M', 'E'],
                                                   ['O', 'V', 'E', 'R'],
                                                   ['G', 'A', 'M', 'E'],
                                                   ['O', 'V', 'E', 'R']], "Nobody moves!"
    assert move2048([[0, 2, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 2, 0, 0]], 'up') == [[0, 4, 0, 0],
                                              [0, 0, 0, 0],
                                              [0, 0, 0, 0],
                                              [0, 0, 0, 2]], "Start. Move Up!"
    assert move2048([[4, 4, 0, 0],
                     [0, 4, 1024, 0],
                     [0, 256, 0, 256],
                     [0, 1024, 1024, 8]], 'down') ==[['U', 'W', 'I', 'N'],
                                                      ['U', 'W', 'I', 'N'],
                                                      ['U', 'W', 'I', 'N'],
                                                      ['U', 'W', 'I', 'N']]
