#!/usr/bin/python3
"""
Sends a request to the specified URL
and displays the value of the X-Request-Id variable 
found in the header of the response.
"""
import urllib.request
import sys


if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as response:
        x_request_id = response.getheader('X-Request-Id')

    print(x_request_id)
