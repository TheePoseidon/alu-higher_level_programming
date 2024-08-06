#!/usr/bin/python3
"""
- uses the GitHub API to display your id
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    auth = (username, password)

    reqs = requests.get(url, auth=auth)
    print(reqs.json().get("id"))
