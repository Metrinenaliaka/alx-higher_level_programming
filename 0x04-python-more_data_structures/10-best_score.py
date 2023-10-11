#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        return max(zip(a_dictionary.values(), a_dictionary.keys()))[1]
