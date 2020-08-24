#!/usr/bin/python3
""" module """

if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    r = requests.get(url)

    req_id = r.headers['X-Request-Id']
    print(req_id)
