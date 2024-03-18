#!/usr/bin/python3
"""Defines a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """
    Serialize an object to a JSON formatted string.

    Args:
    my_obj: Any Python object.

    Returns:
    JSON formatted string representation of the object.
    """
    return json.dumps(my_obj)
