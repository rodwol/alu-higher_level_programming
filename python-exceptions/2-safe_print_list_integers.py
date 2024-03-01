def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for item in my_list[:x]:
            try:
                if isinstance(item, int):
                    print("{:d}".format(item), end=' ')
                    count += 1
            except ValueError:
                pass
    except TypeError:
        print("An exception occurred: x is larger than the length of my_list")
        raise
    print()
    return count
