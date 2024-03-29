#!/usr/bin/python3
"""
takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys

if __name__ == "__main__":

    try:
        rep = sys.argv[1]
    except IndexError:
        rep = ""

    data = {'q': rep}

    r = requests.post('http://0.0.0.0:5000/search_user', data=data)

    try:
        data = r.json()
        id = data.get('id')

        name = data.get('name')
        if id is None or name is None:
            print("No result")
        else:
            print("[{}] {}".format(id, name))
    except ValueError:
        print("Not a valid JSON")
