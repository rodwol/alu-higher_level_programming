#!/usr/bin/python3
# a function that returns the list
"""Defines an object attribute lookup function."""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    """
    return dir(obj)
