#!/usr/bin/python3
"""A module to add all arguments to a Python list and save them to a file."""

import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def main():
    """
    Main function to add command line arguments to a list and save them to a file.

    Reads command line arguments, loads existing items from a JSON file if available,
    adds new items to the list, and saves the updated list to a JSON file.

    Usage:
        python script.py arg1 arg2 arg3 ...

    Note:
        - Existing items are loaded from "add_item.json" file.
        - The updated list is saved back to "add_item.json" file.
    """
    # Get command line arguments, excluding the script name
    arguments = sys.argv[1:]

    # Load existing items from file, if any
    try:
        existing_items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_items = []

    # Add new items to the list
    for arg in arguments:
        existing_items.append(arg)

    # Save the updated list to the file
    save_to_json_file(existing_items, "add_item.json")

if __name__ == "__main__":
    main()
