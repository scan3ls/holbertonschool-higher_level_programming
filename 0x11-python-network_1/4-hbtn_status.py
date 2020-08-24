#!/usr/bin/python3


if __name__ == "__main__":
    import requests

    r = requests.get('https://intranet.hbtn.io/status')
    content = r.content
    type_cont = type(content)
    print("Body response:")
    print("\t- type:", type_cont)
    print("\t- content", content)
    print("\t- utf8 content:", content.decode('UTF-8'))
