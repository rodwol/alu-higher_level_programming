#!/usr/bin/python3
# takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.
"""Sends a request to the specified URL and displays the value of the X-Request-Id variable found in the header of the response.
"""

import urllib.request
import sys 

with urllib.request.urlopen(urllib.request.Request(sys.argv[1])) as response:
    x_request_id = response.headers.get("X-Request-Id")
print(x_request_id)
