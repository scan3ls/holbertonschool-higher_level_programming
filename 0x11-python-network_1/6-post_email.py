#!/usr/bin/python3
""" module """


if __name__ == "__main__":
    from sys import argv
    import requests

    url = argv[1]
    email = argv[2]

    payload = {
        'email': email
    }

    req = requests.post(url, data=payload)
    print(req.content.decode('UTF-8'))
