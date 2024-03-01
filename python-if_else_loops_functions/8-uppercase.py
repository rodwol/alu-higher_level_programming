#!/usr/bin/python3
def uppercase(str):
    for letters in str:
        if ord(letters) in range(97, 123):
            change = chr(ord(letters) - 32)
            print("{}".format(change), end='')
        else:
            print("{}".format(letters, ' ', '\n'), end='')
