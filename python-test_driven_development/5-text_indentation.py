#!/usr/bin/python3
"""
Module: Printing

"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Parameters:
        text (str): The input text

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    trigger_chars = ['.', '?', ':']

    # Iterate through the text
    for i, char in enumerate(text):
        print(char, end='')

        # Check if the character triggers a new line
        if char in trigger_chars:
            print("\n")
            # Skip the next two lines if they are newline characters or spaces
            next_index = i + 1
            while next_index < len(text) and (text[next_index] == '\n' or text[next_index] == ' '):
                print(text[next_index], end='')
                next_index += 1
            print("\n")

        # If the character is a newline, ensure two newlines are added
        elif char == '\n':
            print("\n", end='')
            if i + 1 < len(text) and text[i + 1] == '\n':
                print("\n", end='')
