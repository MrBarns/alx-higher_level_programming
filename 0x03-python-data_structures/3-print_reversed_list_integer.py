#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        list_cpy = my_list.copy()
        while list_cpy:
            print("{:d}".format(list_cpy.pop()))
