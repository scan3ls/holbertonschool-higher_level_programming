#!/usr/bin/python3
"""module"""


if __name__ == "__main__":
    import requests
    from sys import argv

    api = "https://api.github.com"
    username = argv[1]
    password = argv[2]

    path = "{}/users/{}".format(api, username)
    thing = requests.get(path)
    print(thing)
    d = thing.json()
    id = d['id']
    print(id)
