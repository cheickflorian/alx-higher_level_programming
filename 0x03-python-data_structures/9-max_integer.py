#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    lg = my_list[0]
    for j in range(len(my_list)):
        if my_list[j] > lg:
            lg = my_list[j]
    return (lg)
