#!/usr/bin/python3
#define a class square
"""This module provides functionality related to squares."""
class Square:
     """
    A class representing a square.

    Attributes:
        __size (int): The size of the square.
    """
    def __init__(self, size=0):
        #initialize objects of the class
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size #private instance attribute
