#!/usr/bin/python3
# Script to send a request to a URL and display the body of the response
# If the HTTP status code is greater than or equal to 400, it prints an error code
# Uses the requests and sys packages
"""
Script: url_response.py
Description: This script takes a URL as input, sends a request to that URL using the requests package, 
             and displays the body of the response. If the HTTP status code is greater than or equal 
             to 400, it prints an error message with the status code. It utilizes only the requests 
             and sys packages.
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.text)

    if response.status_code >= 400:
        print("Error code:", response.status_code)
