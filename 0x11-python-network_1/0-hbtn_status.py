#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
import urllib.request


if __name__ == "__main__":
    reques = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(reques) as response:
        the_page = response.read()

        print('Body Response:')
        print(f"\t- type: {type(the_page)}")
        print(f"\t- content: {the_page}")
        print(f"\t- utf8 content: {the_page.decode('utf-8')}")
