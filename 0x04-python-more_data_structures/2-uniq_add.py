#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    nonrepeat = set()
    for i in my_list:
        if isinstance(i, int):
            nonrepeat.add(i)
        result = sum(nonrepeat)
    return result
