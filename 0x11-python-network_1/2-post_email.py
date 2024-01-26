#!/usr/bin/python3
'''displays body of response after sending POST request with email'''
import urllib.request
import sys

if __name__ == "__main__":
    headers = {'User-Agent': 'Chrome/91.0.4472.124 Safari/537.36'}
    url = sys.argv[1]
    mail = sys.argv[2]
    values = {'email': mail}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            info = response.read().decode('utf-8')
            print(info)
    except urllib.error.HTTPError as e:
        print("Error: {}".format(e))
