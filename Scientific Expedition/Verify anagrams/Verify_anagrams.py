#!/usr/bin/env python
# coding:utf-8

def verify_anagrams(first_word, second_word):
    first = list(first_word.lower())
    second = list(second_word.lower())
    words_set = set(first) | set(second)
    for ch in words_set:
        if ch.islower():
            if first.count(ch) != second.count(ch):
                return False
    return True

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"

