#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    ind = 0
    if not roman_string or type(roman_string) != str:
        return 0

    while ind < len(roman_string):
        curr = romans[roman_string[ind]]
        if ind == len(roman_string) - 1:
            nex = curr
        else:
            nex = romans[roman_string[ind + 1]]

        if nex > curr:
            total += nex - curr
            ind += 1
        else:
            total += curr

        ind += 1

    return total
