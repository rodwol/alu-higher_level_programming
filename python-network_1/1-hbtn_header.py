#!/usr/bin/python3
# fetches https://alu-intranet.hbtn.io/status
"""
Fetches the status of a given URL and prints the X-Request-Id header.
Usage: python3 script_name.py <URL>
"""

import urllib
import sys


if __name__ == '__main__':
    # Fetch the URL and retrieve the X-Request-Id header
    with urllib.request.urlopen(sys.argv[1]) as response:
        x_request_id = response.getheader('X-Request-Id')
    # Print the X-Request-Id header
    print(x_request_id)
