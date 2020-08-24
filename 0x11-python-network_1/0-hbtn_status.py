#!/usr/bin/python3
""" module """


def print_status(url=None):
    """ prints status of url """
    import urllib.request as req

    if url is None:
        return None

    with req.urlopen(url) as response:
        html = response.read()

    var_type = type(html)
    content = html
    utf8_cont = html.decode('UTF-8')
    print('\t- type:', var_type)
    print('\t- content:', content)
    print('\t- utf8 content:', utf8_cont)


if __name__ == "__main__":
    print_status('https://intranet.hbtn.io/status')
