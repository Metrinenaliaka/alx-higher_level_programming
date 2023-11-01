#!/usr/bin/python3


def print_square(size):
    """
    prints square with #
    Args:
        size: int
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
