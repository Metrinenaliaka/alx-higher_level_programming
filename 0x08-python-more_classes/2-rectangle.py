#!/usr/bin/python3
"""
Defines A Rectangle with height and width
Args:
    height: int/float
    width: in/float
"""


class Rectangle:
    """class with private atrributes"""
    def __init__(self, width=0, height=0):
        """defining width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width"""
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """gets height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height"""
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """returns area of a triangle"""
        return self.width * self.height

    def perimeter(self):
        """returns paramete"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)
