#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for ind in range(x):
        try:
            print("{:d}".format(my_list[ind]), end="")
        except (ValueError, TypeError):
            continue
        except IndexError:
            break
        else:
            count += 1

    print()
    return count
