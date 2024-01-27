#!/usr/bin/python3
"""Error Codes"""
import requests
from sys import argv


if __name__ == "__main__":
    try:
        response = requests.get(argv[1])
        response.raise_for_status()
        print(response.text)
    except requests.HTTPError:
        print("Error code: {}".format(response.status_code))
