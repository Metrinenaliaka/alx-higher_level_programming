#!/usr/bin/python3
"""string rep in JSON"""


import json


def to_json_string(my_obj):
    """
    Args:
        my_obj: string to be rep
    """
    return (json.dumps(my_obj))
