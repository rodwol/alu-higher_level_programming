#!/usr/bin/python3
"""
Module: Display name

"""

def say_my_name(first_name, last_name=""):
    """
    Prints the given first and last name

    Args:
        first_name: the first name to be printed
        last_name: the last name to be printed

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}.".format(first_name, last_name))
