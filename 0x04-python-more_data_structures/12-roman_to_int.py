#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    tot = 0
    number = 0
    digi = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    for x in reversed(roman_string):
        number = digi[x]
        tot += number if tot < number * 5 else -num
        return tot
