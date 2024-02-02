#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    return (sum(i * j for i, j in my_list) / sum(i for i, j in my_list))
