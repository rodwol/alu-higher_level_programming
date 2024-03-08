#!/usr/bin/python3
# define a class square
"""This module provides functionality realted to Square."""


class Square:
    """
    A class representing a square.

    Attributes:
        __size (int): The size of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square object.

        Args:
            size : The size of the square.
        """
        self.__size = size
        self.__position = (0, 0)

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
        for j in range(0, self.__position[0]):
            if self.__position[1] > 0:
                print(" ")
        for i in range(0, self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tupil) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in value:
            if not isinstance(i, int) or i <= 0:
                raise TypeError(
                        "position must be a tuple of 2 positive integers"
                )
        self.__position = value
