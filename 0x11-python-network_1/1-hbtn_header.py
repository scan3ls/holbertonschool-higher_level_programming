#!/usr/bin/python3
""" module """


def url_header():
    """ get url header and display X-Request-Id """
    import urllib.request as req
    from sys import argv

    url = argv[1]
    if url is None:
        return None

    with req.urlopen(url) as response:
        x_req_id = response.headers['X-Request-Id']
        html = response.read()

    print(x_req_id)


if __name__ == "__main__":
    url_header()
