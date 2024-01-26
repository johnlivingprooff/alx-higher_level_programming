#!/usr/bin/python3
"""Error Codes"""
import urllib.request
import sys


if __name__ == "__main__":
    uri = sys.argv[1]

    try:
        with urllib.request.urlopen(uri) as response:
            content = response.read().decode('utf-8')
            print(content)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
