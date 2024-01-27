#!/usr/bin/python3
"""API"""
import requests
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    token = argv[2]
    uri = f"https://api.github.com/users/{username}"

    response = requests.get(uri, auth=(username, token))

    if response.status_code == 200:
        resp_json = response.json()
        print(resp_json['id'])
    else:
        print("None")
