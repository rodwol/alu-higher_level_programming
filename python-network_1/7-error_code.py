#!/usr/bin/python3
"""
Script: url_response.py
This script takes a URL as input
sends a request to URL using the requests package
and displays the body of the response. If the HTTP status code is >= 400
it prints an error message with the status code.

"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
