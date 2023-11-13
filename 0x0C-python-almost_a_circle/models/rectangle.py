#!/usr/bin/python3
"""
child class to Base
"""
from models.base import Base
import sys


class Rectangle(Base):
    """
    inheritance from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializing attributes"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """gets width"""
        return self.__width

    @width.setter
    def width(self, value):
        """gets width"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format('width'))
        if value <= 0:
            raise ValueError("{} must be > 0".format('width'))
        self.__width = value

    @property
    def height(self):
        """gets height"""
        return self.__height

    @height.setter
    def height(self, value):
        """gets height"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format('height'))
        if value <= 0:
            raise ValueError("{} must be > 0".format('height'))
        self.__height = value

    @property
    def x(self):
        """gets x"""
        return self.__x

    @width.setter
    def x(self, value):
        """gets x"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format('x'))
        if value < 0:
            raise ValueError("{} must be >= 0".format('x'))
        self.__x = value

    @property
    def y(self):
        """gets y"""
        return self.__y

    @width.setter
    def y(self, value):
        """gets y"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format('y'))
        if value < 0:
            raise ValueError("{} must be >= 0".format('y'))
        self.__y = value

    def area(self):
        """defines area of rectangle"""
        res = self.width * self.height
        return res

    def display(self):
        """display a rectangle on stdout"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.x, end='')
            print('#' * self.width)

    def __str__(self):
        """string rep"""
        return ('[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.
                format(self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """assigns args to atts"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        """dictiobnary representation of rectangle"""
        my_dic = {}
        keys = ['id', 'width', 'height', 'x', 'y']

        for k in keys:
            my_dic[k] = getattr(self, k)
        return (my_dic)
