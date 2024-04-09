#!/usr/bin/python3
"""
Module: Calculator
Provides functions for mathematical operations
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Parameters:
        a (int/float): The first integer.
        b (int/float): The second integer.

    Returns:
        int: The sum of a and b.
    """
    a = int(a)
    b = int(b)
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return a+b
