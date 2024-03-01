#!/usr/bin/python3
def raise_exception():
    try:
        raise TypeError("Intentional type exception raised")
    except TypeError as e:
        print("Exception:", e)
