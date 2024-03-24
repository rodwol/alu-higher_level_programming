#!/usr/bin/python3
"""A script that
- fetches https://alu-intranet.hbtn.io/status.
- uses urllib package
"""

import urllib.request

# Define the URL to fetch
url = 'https://intranet.hbtn.io/status'

# If the URL doesn't start with 'https://', prepend it.
if url.startswith('https://'):
    url = 'https://alu-intranet.hbtn.io/status'

# Check if the script is executed as the main program
if __name__ == '__main__':
    # Open the URL and get the response
    with urllib.request.urlopen(url) as res:
        # Read the content of the response
        content = res.read()
        
        # Print information about the response
        print("Body response:")
        print("\t- type: {}".format(type(content)))  # Print the type of content
        print("\t- content: {}".format(content))     # Print the content as bytes
        print("\t- utf8 content: {}".format(content.decode('utf-8')))  # Print the content as UTF-8 decoded string
