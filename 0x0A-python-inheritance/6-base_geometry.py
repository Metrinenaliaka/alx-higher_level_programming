#!/usr/bin/python3
"""inheritance"""


class BaseGeometry:
    """Base geometry class"""

    def area(self):
        """area function that is empty"""
        raise Exception('area() is not implemented')
