#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.

Usage: ./1-hbtn_header.py <URL>
"""
import sys
import urllib.request


if __name__ == "__main__":
    headers = {'User-Agent': 'Chrome/91.0.4472.124 Safari/537.36'}
    url = sys.argv[1]

    request = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(request) as response:
            print(dict(response.headers).get("X-Request-Id"))
    except urllib.error.HTTPError as e:
        print("Error: {}".format(e))
