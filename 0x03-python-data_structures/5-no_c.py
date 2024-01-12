#!/usr/bin/env python3
def no_c(my_string):
    cop = ""
    for i in my_string:
        if i != "c" and i != "C":
            cop += i
    return cop
