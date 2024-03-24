#!/usr/bin/python3
"""
Python script that fetches https://alu-intranet.hbtn.io/status
"""

import requests

if __name__ == '__main__':
    # URL to fetch
    url = 'https://alu-intranet.hbtn.io/status'

    # Check if the URL starts with 'https://', if not, prepend it
    if not url.startswith('https://'):
        url = "https://" + url

    # Send GET request to the URL
    response = requests.get(url)

    # Print information about the response
    print("Body response:")
    print("\t- type:", (type(response.text)))
    # Type of the response content
    print("\t- content:", (response.text))
    # Content of the response
