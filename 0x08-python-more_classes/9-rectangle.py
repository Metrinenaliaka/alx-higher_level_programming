#!/usr/bin/python3
"""
Defines A Rectangle with height and width
Args:
    height: int
    width: int/float
"""


class Rectangle:
    """
    class with private atrributes
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        defining width and height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        gets width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets width
        """
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        gets height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets height
        """
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        returns area of a triangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        returns parameter
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """
        prints rectangle
        """
        if self.height == 0 or self.width == 0:
            return ''
        hashes = "{}".format(self.print_symbol) * self.width
        return ('\n'.join(hashes for i in range(self.height)))

    def __repr__(self):
        """
        prints rectangle
        """
        eval('Rectangle(self.width, self.height)')
        return (f"Rectangle({self.width}, {self.height})")

    def __del__(self):
        """
        instance del
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """
        compares two Rectangles
        Args
           rect_1
           rect_2
        Returns bigger rectangle or rect_1 if same
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        """
        Returns area of a square
        """
        return Rectangle(size, size)
