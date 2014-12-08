#!/usr/bin/env python
# coding:utf-8

OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

class Operations():
    def conjunction(self, x, y):
        return x & y
    
    def disjunction(self, x, y):
        return x | y
    
    def implication(self, x, y):
        return x <= y
    
    def exclusive(self, x, y):
        return x ^ y
    
    def equivalence(self, x, y):
        return x == y

def boolean(x, y, operation):
    methodToCall = getattr(Operations, operation)
    return methodToCall(None, x, y)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"
