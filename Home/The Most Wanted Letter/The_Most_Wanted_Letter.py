#!/usr/bin/env python
# coding:utf-8

def checkio(text):
    text = text.lower()
    max_count = 0
    most_letter = ''
    text = list(text)
    text_set = set(text)
    for x in text_set:
        if x.islower():
            temp_count = text.count(x)
            if temp_count >= max_count:
                if temp_count == max_count:
                    if x < most_letter:
                        most_letter = x
                else:
                    max_count = temp_count
                    most_letter = x
    return most_letter

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
