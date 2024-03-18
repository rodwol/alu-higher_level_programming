#!/usr/bin/python3
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """
    Append a string at the end of a text file (UTF8)

    Args:
    filename: Name of the file to append
    text: Text to append to the file.

    Returns:
    Number of characters added.
    """
    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(text)
            return len(text)
    except FileNotFoundError:
        # If the file doesn't exist, create it and try again
        with open(filename, "w", encoding="utf-8") as file:
            file.write(text)
            return len(text)
