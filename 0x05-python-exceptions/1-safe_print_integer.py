#!/usr/bin/python3
def safe_print_integer(value):
    try:
        value = int(value):
            print("{:d}".format(value))
            return True
    except Exception as ValueError and TypeError:
        return False
