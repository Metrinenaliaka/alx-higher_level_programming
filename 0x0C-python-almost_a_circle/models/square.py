#!/usr/bin/python3
"""
class inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    All atts inherited from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        same attributes from Rectangle
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns string"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """returns size"""
        return (self.width)

    @size.setter
    def size(self, value):
        """
        set size
        Args
           value - size to set to
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns arguments to each attribute"""
        if args:
            keys = ['id', 'size', 'x', 'y']
            for k, v in zip(keys, args):
                setattr(self, k, v)
        else:
            if kwargs is not None:
                for k, v in kwargs.items():
                    setattr(self, k, v)

    def to_dictionary(self):
        """dictiobnary representation of square"""
        my_dic = {}
        keys = ['id', 'size', 'x', 'y']

        for k in keys:
            my_dic[k] = getattr(self, k)
        return my_dic
