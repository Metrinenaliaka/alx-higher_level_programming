#!/usr/bin/python3
"""appends to a file"""


def append_write(filename="", text=""):
    """
    Args:
        filename: file to be appended
        text: text to append
    """
    with open(filename, 'a', encoding="utf-8") as f:
        append_f = f.write(text)
        return append_f
