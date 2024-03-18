#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """
    A class to represent a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student object with the given attributes.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student instance.

        Args:
            attrs (list, optional): A list of attribute names to retrieve.
                If provided, only attributes with names in this list will be included.
                If None, all attributes will be included. Defaults to None.

        Returns:
            dict: A dictionary containing the specified or all attributes of the student.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
