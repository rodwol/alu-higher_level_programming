#!/usr/bin/python3
def uppercase(str):
    change = ""
    for letters in str:
        if ord(letters) in range(97, 123):
            change = chr(ord(letters) - 32)
        elif letters == ' ':
            change = letters
            print("{}".format(change), end='')
