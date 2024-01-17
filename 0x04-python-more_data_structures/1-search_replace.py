#!/usr/bin/python3
def search_replace(my_list, search, replace):
    matrix = my_list.copy()
    for i in range(len(matrix)):
        if matrix[i] == search:
            matrix[i] = replace
    return matrix
