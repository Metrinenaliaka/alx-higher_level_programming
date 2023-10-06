#!/usr/bin/env python3
def no_c(my_string):
    new_string = str()
    for idx in my_string:
        if idx != 'c' and idx != 'C':
            new_string += idx
    return new_string
