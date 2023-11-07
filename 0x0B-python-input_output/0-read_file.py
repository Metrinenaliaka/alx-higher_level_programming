#!/usr/bin/python3
"""function reads from textfile"""


def read_file(filename=""):
    """filename = file to be opened"""
    with open("filename", encoding="utf-8") as myfile:
        read_file = myfile.read()
        print(read_file, end='')
