#!/usr/bin/python3
"""
Script to send a POST request to http://0.0.0.0:5000/search_user with a letter as a parameter.
Uses the requests and sys packages.
"""
import requests
import sys


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    url = "http://0.0.0.0:5000/search_user"
    data = {'q': letter}
    response = requests.post(url, data=data)

    try:
        result = response.json()
    except Exception:
        print("Not a valid JSON")
        exit()
    try:
        print("[{}] {}".format(result['id'], result['name']))
    except Exception:
        print("No result")
