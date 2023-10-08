#!/usr/bin/python3
def no_c(my_string):
    new_string = str()
    for ch in my_string:
        if (ch != 'C' and ch != 'c'):
            new_string = new_string + ch
    return (new_string)
