#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    if len(my_string):
        for letter in my_string:
            if letter.casefold() != 'c':
                new_string += letter

    return new_string
