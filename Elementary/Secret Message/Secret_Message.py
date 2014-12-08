#!/usr/bin/env python
# coding:utf-8

def find_message(text):
    """Find a secret message"""
    secret = ""
    for ch in text:
        if ch.isupper():
            secret += ch
    return secret

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
