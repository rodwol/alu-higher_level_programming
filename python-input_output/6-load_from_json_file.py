#!/usr/bin/python3
"""Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    Args:
    filename: Name of the JSON file to read from.

    Returns:
    Python object deserialized from the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
