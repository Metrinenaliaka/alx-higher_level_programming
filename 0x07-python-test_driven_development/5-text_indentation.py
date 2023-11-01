#!/usr/bin/python3


def text_indentation(text):
    """
    displays text each on new line
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    length = len(text)
    flag = True
    for i in range(length):
        if flag and text[i].isspace():
            continue
        print(text[i], end='')
        if text[i] in ['.', '?', ':']:
            print("\n")
            flag = True
        else:
            flag = False
