#!/usr/bin/python3
def roman_to_int(roman_string):
    if not type(roman_string) is str:
        return 0

    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    num = 0

    for i in reversed(roman_string):
        num = roman_numerals[i]
        total += num if total < num * 5 else -num
    return total
