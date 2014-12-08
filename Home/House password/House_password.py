#!/usr/bin/env python
#coding:utf-8

def checkio(data):
    if len(data) < 10:
        return False
    hasupper = False
    haslower = False
    hasdigit = False
    for ch in data:
        if ch.islower():
            haslower = True
        if ch.isupper():
            hasupper = True
        if ch.isdigit():
            hasdigit = True
    return haslower & hasupper & hasdigit

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
