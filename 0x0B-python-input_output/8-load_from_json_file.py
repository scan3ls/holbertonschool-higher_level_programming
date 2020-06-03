#!/usr/bin/python3
"""What the hell is JSON"""

import json


def load_from_json_file(filename):
    """Does some JSONy things"""

    with open(filename, 'r') as f:
        data = json.load(f)

    return data
