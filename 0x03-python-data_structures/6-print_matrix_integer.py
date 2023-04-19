#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for element in matrix:
        if element:
            c = 1
            for num in element:
                if c < len(element):
                    end = " "
                else:
                    end = "\n"
                print("{:d}".format(num), end=end)
                c += 1

        else:
            print("")
