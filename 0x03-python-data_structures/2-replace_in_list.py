#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return None
    new_list_copy = my_list.copy()
    new_list_copy[idx] = element
    return new_list_copy
