#!/usr/bin/env python
#coding:utf-8

class Queue():
    def __init__(self):
        self._queue = []
    
    def push(self, ch):
        try:
            self._queue.append(ch)
            return True
        except:
            return False

    def pop(self):
        try:
            return self._queue.pop(0)
        except:
            return ""

    def display(self):
        st = ""
        for ch in self._queue:
            st += ch
        return st

def letter_queue(commands):
    queue = Queue()
    for cmd in commands:
        command = cmd.split()
        command[0] = command[0].lower()
        methodToCall = getattr(queue, command[0])
        if len(command) > 1:
            methodToCall(command[1])
        else:
            methodToCall()
    return queue.display()
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"
