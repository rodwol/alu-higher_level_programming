#!/usr/bin/python3
"""This module provides functionality related to squares."""

class Square:
    """
    A class representing a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a new Square object with the given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size  # private instance attribute
