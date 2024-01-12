#!/usr/bin/env python3
def no_c(my_string):
    cop = f""
    for i in my_string:
        if i != "c" and i != "C":
            cop += f"{i}"
    return cop
