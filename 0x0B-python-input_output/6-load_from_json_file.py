#!/usr/bin/python3
"""create an obj from json"""


def load_from_json_file(filename):
    """filename file to be created"""

    import json
    with open(filename) as f:
        return (json.load(f))
