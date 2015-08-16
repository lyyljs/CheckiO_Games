#!/usr/bin/env python
# coding:utf-8

def check_pangram(text):
    textSet = set()
    for ch in text.lower():
        if ch.islower():
            textSet.add(ch)
    if len(textSet) >= 26:
        return True
    return False

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
    assert not check_pangram("Six big devils from Japan quickly forgot how to walt.")
