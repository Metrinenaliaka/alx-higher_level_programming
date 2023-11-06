#!/usr/bin/python3
"""inheritance"""


class MyList(list):
    """class utilizing list class"""

    def __init__(self):
        """initializer for MyList"""
        pass

    def print_sorted(self):
        """print sorted list"""
        res = list.copy(self)
        list.sort(res)
        print(res)
