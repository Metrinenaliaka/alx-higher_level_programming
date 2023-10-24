#!/usr/bin/python3
"""
Defines class Square with private attribute size
"""


class Square:
    """
    class Square definition
    Args:
        size : size of a side in square
    """
    def __init__(self, size):
        """
        Initializes square
        """
        self.__size = size
