#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    k_delete = []
    for key, val in a_dictionary.items():
        if val == value:
            k_delete.append(key)
    for key in k_delete:
        del a_dictionary[key]
    return a_dictionary
