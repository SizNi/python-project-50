import json


def true_json(value):
    result = json.dumps(value, indent=4)
    return result
