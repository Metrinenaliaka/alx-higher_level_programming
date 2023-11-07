#!/usr/bin/python3
"""
writes an Object to a text file, using a JSON representation
"""


def save_to_json_file(my_obj, filename):
    """save to json file
    Args
       my_obj
       filename
    """
    import json
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
