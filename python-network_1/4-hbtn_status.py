#!/usr/bin/python3
"""
fetches https://alu-intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body response:")
    print("\t- type:", response.text.__class__)
    print("\t- content:", response.text)
