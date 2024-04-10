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
    trigger_chars = ['.', '?', ':']

    # Iterate through the text
    for char in text:
        print(char, end='')
        # Check if the character triggers a new line
        if char in trigger_chars:
            print("\n")
            # Skip the next two lines if they are newline characters
            while text[text.index(char)+1] == '\n':
                print("\n", end='')
                char = text[text.index(char)+1]
            # Skip the next two lines if they are spaces
            while text[text.index(char)+1] == ' ':
                char = text[text.index(char)+1]
        # If the character is a newline, ensure two newlines are added
        elif char == '\n':
            print("\n", end='')
            if text[text.index(char)+1] == '\n':
                print("\n", end='')
                char = text[text.index(char)+1]
