#!/usr/bin/python3
def weight_average(my_list=[]):
    avg = 0
    if my_list:
        sums = [tup[0] * tup[1] for tup in my_list]
        weights = [tup[1] for tup in my_list]

        avg = sum(sums) / sum(weights)

    return avg
