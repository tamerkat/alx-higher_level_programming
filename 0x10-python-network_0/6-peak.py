#!/usr/bin/python3
def find_peak(list_of_integers):
    list_copy = list_of_integers.copy()
    list_copy.sort()
    peak = list_copy[0]
    return peak
