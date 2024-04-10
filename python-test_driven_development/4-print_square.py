#!/usr/bin/python3
"""
Module: Print Square
Proovides function to print square in the form of #
"""


def print_square(size):
    """
    Print a square with the character #.

    Parameters:
        size = size(length)

    Return:
         None

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print('#' * size)
