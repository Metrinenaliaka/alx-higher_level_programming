#!/usr/bin/python3
"""
script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
import requests
import sys

if __name__ == "__main__":

    user = sys.argv[1]
    pwd = sys.argv[2]
    r = requests.get("https://api.github.com/user",
                     auth=(user, pwd))
    data = r.json()
    id = data.get('id')
    print(id)
