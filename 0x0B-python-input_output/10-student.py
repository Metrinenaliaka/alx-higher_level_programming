#!/usr/bin/python3
"""class student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """args: first_name, last_name, age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation
        of a Student instance
        """
        if attrs is not None:
            a_dict = {}
            for i in attrs:
                if i in self.__dict__:
                    a_dict[i] = self.__dict__[i]
            return a_dict
        return self.__dict__
