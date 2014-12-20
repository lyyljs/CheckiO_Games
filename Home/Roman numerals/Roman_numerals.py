#!/usr/bin/env python
#coding:utf-8

def checkio(data):
    result = ""
    NumDic = {
             '1':('I','IV','V','IX'),
             '2':('X','XL','L','XC'),
             '3':('C','CD','D','CM'),
             '4':('M')
             }
    weight = 0
    while data > 0:
        weight += 1
        num = data % 10
        if num < 4:
            result = NumDic[str(weight)][0] * num + result
        else:
            if num < 6:
                result = NumDic[str(weight)][num - 3] + result
            else:
                if num > 8:
                    result = NumDic[str(weight)][3] + result
                else:
                    result = NumDic[str(weight)][2] + NumDic[str(weight)][0] * (num - 5) + result
        data = data // 10
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
