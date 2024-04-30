#!/usr/bin/python3
"""
    find the peak of list
"""


def find_peak(list_of_integers):
    """
        find the peak function
    """

    if len(list_of_integers) == 0:
        return None
    list_copy = list_of_integers.copy()
    list_copy.sort()
    peak = list_copy[0]
    return peak
