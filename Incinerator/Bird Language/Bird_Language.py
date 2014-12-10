#!/usr/bin/env python
#coding:utf-8

VOWELS = "aeiouy"

def translate(phrase):
    got_consonant = False
    result = ""
    count = 0
    for ch in phrase:
        if ch is " ":
            got_consonant = False
            result += ch
            continue
        if ch in VOWELS:
            if got_consonant:
                got_consonant = False
                continue
            else:
                count += 1
                if count > 2:
                    count = 0
                    result += ch
        else:
            result += ch
            got_consonant = True
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
#    print(translate("hoooowe yyyooouuu duoooiiine"))
#    '''
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
#    '''
