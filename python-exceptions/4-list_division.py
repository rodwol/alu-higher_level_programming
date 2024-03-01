#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    try:
        for i in range(list_length):
            try:
                if i < len(my_list_1) and i < len(my_list_2):
                    result_list.append(my_list_1[i] / my_list_2[i])
                else:
                    print("out of range")
                    result_list.append(0)
            except ZeroDivisionError:
                print("division by 0")
                result_list.append(0)
            except (TypeError, ValueError):
                print("wrong type")
                result_list.append(0)
    finally:
        return result_list
