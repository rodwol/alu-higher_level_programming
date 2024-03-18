#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys


from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def main():
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
