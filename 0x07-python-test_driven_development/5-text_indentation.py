#!/usr/bin/python3


def text_indentation(text):
    """
    displays text each on new line
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    length = len(text)
    for i in range(length):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print("\n")
