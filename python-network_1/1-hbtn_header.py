#!/usr/bin/python3
# fetches https://alu-intranet.hbtn.io/status
import urllib.request

url = 'https://alu-intranet.hbtn.io/status'

request = urllib.request.Request(url)
with urllib.request.urlopen(request) as response:
    html = response.read()
print("Body response:")
print("\t- type: {}".format(html.__class__))
print("\t- content: {}".format(html))
print("\t- utf8 content: {}".format(html.decode('ascii')))
print("Body response:")
print("\t- type:", type(html))
print("\t- content:", html)
print("\t- utf8 content:", html.decode('utf-8'))
