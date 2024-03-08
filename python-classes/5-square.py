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
            size : The size of the square.
        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    i = 0

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(0, self.__size):
            print("#" * self.__size)
