#!/usr/bin/python3
"""Parameter Search"""
import requests
from sys import argv


if __name__ == "__main__":
    uri = "http://0.0.0.0:5000/search_user"
    q = argv[1] if len(argv) == 2 else ""

    data = {"q": q}
    resp = requests.post(uri, data)

    resp_type = resp.headers.get('content-type')
    if resp_type != "application/json":
        print("Not a valid JSON")
        exit()
    else:
        resp = resp.json()
    if len(resp) == 0:
        print("No result")
    else:
        print(f"[{resp['id']}] {resp['name']}")
