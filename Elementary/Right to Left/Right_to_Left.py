#!/usr/bin/env python
# coding:utf-8

def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    result = ""
    for phrase in phrases:
        if result != "":
            result = result + ","
        words = phrase.split("right")
        temp = words[0]
        for word in words[1:]:
            temp += "left"
            temp += word
        result += temp
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
