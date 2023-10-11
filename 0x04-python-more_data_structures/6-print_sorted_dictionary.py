#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    s_keys = dict(sorted(a_dictionary.items()))
    for key, value in s_keys.items():
        print(f"{key} : {value}")
