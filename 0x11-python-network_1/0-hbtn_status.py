#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""

import urllib.request

if __name__ == "__main__":
    """fetches url"""
    url = "https://alx-intranet.hbtn.io/status"
    # headers = {'User-Agent': 'Chrome/91.0.4472.124 Safari/537.36'}
    r = urllib.request.Request(url)

    with urllib.request.urlopen(r) as response:
        info = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(info)))
        print("\t- content: {}".format(info))
        info = info.decode('utf-8')
        print("\t- utf8 content: {}".format(info))
