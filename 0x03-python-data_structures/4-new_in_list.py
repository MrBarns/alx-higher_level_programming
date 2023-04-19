#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_cpy = my_list.copy()
    if (not my_list) | (idx < 0) | (idx >= len(my_list)):
        return list_cpy

    list_cpy[idx] = element
    return list_cpy
