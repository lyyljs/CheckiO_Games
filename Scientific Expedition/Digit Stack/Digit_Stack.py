#!/usr/bin/env python
# coding:utf-8

class DigitStack():
    '''
    >>> digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",\
                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"])
    8
    >>> digit_stack(["POP", "POP"])
    0
    >>> digit_stack(["PUSH 9", "PUSH 9", "POP"])
    9
    >>> digit_stack([])
    0
    '''
    def __init__(self):
        self._stack = []
    
    def push(self, num):
        try:
            num = int(num)
            self._stack.append(num)
            return num
        except:
            return -1
    
    def pop(self):
        try:
            return self._stack.pop()
        except:
            return 0
    
    def peek(self):
        try:
            return self._stack[-1]
        except:
            return 0

def digit_stack(commands):
    stack = DigitStack()
    result = 0
    for command in commands:
        command = command.lower()
        command = command.split(' ')
        methodToCall = getattr(stack, command[0])
        if len(command) > 1:
            methodToCall(command[1])
        else:
            result += methodToCall()
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
