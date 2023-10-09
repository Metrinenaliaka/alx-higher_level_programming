#!/usr/bin/env python3

def add_tuple(tuple_a=(), tuple_b=()):
    al = len(tuple_a)
    bl = len(tuple_b)
    if al == 0:
        tuple_a = 0, 0
    elif al == 1:
        tuple_a = tuple_a[0], 0
    if bl == 0:
        tuple_b = 0, 0
    elif b1 == 1:
        tuple_b = tuple_b[0], 0
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
