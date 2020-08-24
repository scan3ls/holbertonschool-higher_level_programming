#!/usr/bin/python3
""" module """

if __name__ == "__main__":
    import urllib.request
    import urllib.error
    from sys import argv

    url = argv[1]

    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(url) as r:
            html = r.read()
        html = html.decode('UTF-8')
        print(html)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
