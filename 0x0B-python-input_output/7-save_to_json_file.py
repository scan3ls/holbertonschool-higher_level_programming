#!/usr/bin/python3
"""What the hell is JSON"""

import json


def save_to_json_file(my_obj, filename):
    """Does some JSONy things"""

    with open(filename, 'w') as f:
        json.dump(my_obj, f)
