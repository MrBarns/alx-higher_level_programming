#!/usr/bin/python3
def list_division(my_list1, my_list2, list_length):
    result = []
    for ind in range(list_length):
        div = 0
        try:
            div = my_list1[ind] / my_list2[ind]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            result.append(div)

    return result
