#!/usr/bin/python3
""" module """


def post_request():
    """ send post request to url with email """
    import urllib.request as req
    import urllib.parse as parse
    from sys import argv

    url = argv[1]
    email = argv[2]

    values = {
        'email': email
    }

    data = parse.urlencode(values)
    data = data.encode('ascii')
    request = req.Request(url, data)

    with req.urlopen(request) as response:
        page = response.read()
    page = page.decode('UTF-8')
    print(page)

if __name__ == "__main__":
    post_request()
