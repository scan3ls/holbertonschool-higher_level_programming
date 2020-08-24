#!/usr/bin/python3
""" module """


if __name__ == "__main__":
    from sys import argv
    import requests

    url = "http://0.0.0.0:5000/search_user"

    if len(argv) <= 1:
        q = ""
    else:
        q = argv[1]

    r = requests.post(url, data={'q': q})
    dictionary = r.json()
    if dictionary == {}:
        print("No result")
        exit()

    id = dictionary['id']
    name = dictionary['name']
    print("[{}] {}".format(id, name))
