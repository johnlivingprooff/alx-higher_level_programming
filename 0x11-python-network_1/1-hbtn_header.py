#!/usr/bin/python3
"""sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response."""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        headr_id = response.getheader('X-Request-Id')
        print(headr_id)
