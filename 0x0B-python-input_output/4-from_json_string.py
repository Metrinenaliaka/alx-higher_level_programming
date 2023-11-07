#!/usr/bin/python3
"""from json to obj"""


import json


def from_json_string(my_str):
    """
    Args:
        my_str: string to be returned
    """
    return (json.loads(my_str))
