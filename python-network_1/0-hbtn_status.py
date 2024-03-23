#!/usr/bin/python3
# fetches https://alu-intranet.hbtn.io/status
import urllib.request

url = 'https://alu-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as response:
    html = response.read()
print("Body response:")
print("\t- type:", type(html))
print("\t- content:", html)
print("\t- utf8 content:", html.decode('utf-8'))
