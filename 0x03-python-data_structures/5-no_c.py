#!/usr/bin/env python3
def no_c(my_string):
    cop = ''.join(char for char in my_string if char not in ('c', 'C'))
    return cop
