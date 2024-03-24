#!/usr/bin/python3
"""
Script: github_user_id.py
takes GitHub credentials (username and personal access token)
uses Basic Authentication with the GitHub API to display the user's id
utilizes the requests and sys packages

"""

import requests
import sys


if __name__ == '__main__':
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]
    auth = (username, password)

    response = requests.get(url, auth=auth)

    if response.status_code == 200:
        user_data = response.json()
        print("User ID:", user_data['id']
    else:
        print("Error: Unable to retrieve user id")
        return None
