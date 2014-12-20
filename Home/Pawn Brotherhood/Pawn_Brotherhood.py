#!/usr/bin/env python
# coding:utf-8

def safe_pawns(pawns):
    result = 0
    for pawn in pawns:
        for i in range(-1, 2, 2):
            support_pawn = chr(ord(pawn[0]) + i) + str(int(pawn[1]) - 1)
            if support_pawn in pawns:
                result += 1
                break
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
