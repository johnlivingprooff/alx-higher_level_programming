#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
import urllib.request


if __name__ == "__main__":
    reques = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(reques) as response:
        the_page = response.read()
        encoder = the_page.decode('utf-8')

        print('Body Response:')
        # print(f"\t- type: {type(the_page)}")
        print("   - type: {}".format(type(the_page)))
        # print(f"\t- content: {the_page}")
        print("   - content: {}".format(the_page))
        # print(f"\t- utf8 content: {the_page.decode('utf-8')}")
        print("   - utf8 content: {}".format(encoder))
