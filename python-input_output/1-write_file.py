#!/usr/bin/python3
"""Defines a text file line-counting function."""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8)

    Args:
    filename: Name of the file to write
    text: Text to write to the file.

    Returns:
    Number of characters written.
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(text)
            return len(text)
    except FileNotFoundError:
        # If the file doesn't exist, create it and try again
        with open(filename, "x", encoding="utf-8") as file:
            file.write(text)
            return len(text)
