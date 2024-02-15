import json
import os

script_directory = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(script_directory, 'key.json')


def get_api_key():
    with open(path, 'r') as api_key:
        key = json.load(api_key)
    return str(key['key'])
