#!/usr/bin/python3
#  a class MyList that inherits from list
"""Defines an inherited list class MyList."""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class.
    This class adds functionality to print the list in ascending sorted order.
    def print_sorted(self):
    """
    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
