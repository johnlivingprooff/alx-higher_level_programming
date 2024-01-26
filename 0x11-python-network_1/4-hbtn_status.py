#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status
Uses only the requests package
"""
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)

    print("Body response:")
    print("    - type: {}".format(type(response.text)))
    print("    - content: {}".format(response.text))