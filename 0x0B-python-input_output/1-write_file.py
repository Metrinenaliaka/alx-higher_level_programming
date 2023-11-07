#!/usr/bin/python3
"""writes information to a file"""


def write_file(filename="", text=""):
    """filename = file to be written to, text"""
    with open(filename, 'w', encoding='utf-8') as f_name:
        read_chars = f_name.write(text)
        return (read_chars)
