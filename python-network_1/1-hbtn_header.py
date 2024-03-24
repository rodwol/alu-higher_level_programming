#!/usr/bin/python3
# fetches https://alu-intranet.hbtn.io/status
import urllib
import sys


if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as response:
        x_request_id = response.getheader('X-Request-Id')

    print(x_request_id)
