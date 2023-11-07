#!/usr/bin/python3
"""opens file to read"""


def read_file(filename=""):
    """filename = file"""
    with open(filename, encoding='utf-8') as f:
        print(f.read())
