#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff = set()
    diff = set_1 ^ set_2
    return diff
