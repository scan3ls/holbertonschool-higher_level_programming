#!/usr/bin/python3
""" Add arguments to json file """

import sys

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

argv = sys.argv
argv.remove(argv[0])

try:
    new_object = list(load_from_json_file("add_item.json"))
except:
    new_object = []

for item in argv:
    new_object.append(item)

save_to_json_file(new_object, "add_item.json")
