#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    uri = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({"email": email})
    data = data.encode('ascii')

    request = urllib.request.Request(uri, data)
    with urllib.request.urlopen(request) as response:
        content = response.read().decode('utf-8')
        print(content)
