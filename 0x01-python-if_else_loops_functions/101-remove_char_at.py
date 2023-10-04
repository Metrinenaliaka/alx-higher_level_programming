#!/usr/bin/python3
def remove_char_at(str, t):
    if t < 0:
        return (str)
    return (str[:t] + str[t+1:])
