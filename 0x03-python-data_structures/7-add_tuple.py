#!/usr/bin/env python3
def add_tuple(tuple_a=(), tuple_b=()):
    al = len(tuple_a)
    bl = len(tuple_b)
    if al < 2:
        if al == 0:
            tuple_a = 0, 0
        else:
            tuple_a = tuple_a[0], 0
    if bl < 2:
        if bl == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
