#!/usr/bin/python3
"""sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response."""
import requests
import sys


if __name__ == "__main__":
    uri = sys.argv[1]

    response = requests.get(uri)
    headr_id = response.headers.get('X-Request-Id')
    print(headr_id)
