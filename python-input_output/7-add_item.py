#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def add_items_to_list_and_save(arguments):
    """
    Adds all arguments to a Python list and saves them to a file.

    Args:
        arguments (list): A list of arguments to be added to the Python list.

    Returns:
        list: The updated list containing the arguments.
    """
    try:
        existing_items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_items = []

    existing_items.extend(arguments)

    save_to_json_file(existing_items, "add_item.json")

    return existing_items

if __name__ == "__main__":
    arguments = sys.argv[1:]
    updated_list = add_items_to_list_and_save(arguments)
    print("Updated list:", updated_list)
