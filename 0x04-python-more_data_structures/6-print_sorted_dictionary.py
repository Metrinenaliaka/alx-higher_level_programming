#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    s_keys = sorted(a_dictionary.keys())
    for i in s_keys:
        value = a_dictionary[i]
        print(f"{i} : {value}")
