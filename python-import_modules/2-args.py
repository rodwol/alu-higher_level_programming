#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    for i in range(1, len(argv)):
        if len(argv) == 0:
            print("0 arguments.")
        elif len(argv) == 1:
            print("1 argument:")
        else:
            print("{} arguments: ".format(len(argv) - 1))
            print("{}:{}".format(i, argv[i]))
