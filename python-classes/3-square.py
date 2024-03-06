#!/usr/bin/python3
# define a class square
"""This module provides functionality realted to Square."""


class Square:
    """
    A class representing a square.

    Attributes:
        __size (int): The size of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square object.

        Args:
            size (int): The size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  # private instance attribute
    def area(self):
        return self.__size ** 2
