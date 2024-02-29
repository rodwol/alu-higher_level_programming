#!/usr/bin/python3
def uppercase(str):
    for letters in str:
        if ord(letters) in range(97, 123):
            change=chr(ord(letters) - 32)
            print("{}".format(change), end='')
        elif letters == ' ' or letters == '\n':
            print("{}".format(letters), end='')
        else:
            print("{}".format(letters), end='')
