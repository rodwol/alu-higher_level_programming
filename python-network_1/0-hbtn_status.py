#!/usr/bin/python3
"""
Script to fetch https://alu-intranet.hbtn.io/status using urllib package

"""
import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as url:
    s = url.read()
    req = "Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
    print(req.format(type(s), s, s.decode('utf-8')))
