#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for item in my_list:
            try:
                print("{:d}".format(item), end=" ")
                count += 1
                if count == x:
                    break
            except ValueError:
                pass
        print()
        return count
    except TypeError:
        print("Error: Cannot iterate over provided input.")
        return count
