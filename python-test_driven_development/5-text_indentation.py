#!/usr/bin/python3
"""
Module: Printing

"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters
        Characters: ., ? and :

    Parameter:
        text = text(str)

    Return:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    Char = ['.', '?', ':']
    lines = ""
    current_line = ""

    for char in text:
        current_line += char
        if char in Char:
            lines += current_line.strip() + "\n\n"
            current_line = ""

    if current_line:
        lines += current_line.strip() + "\n"
