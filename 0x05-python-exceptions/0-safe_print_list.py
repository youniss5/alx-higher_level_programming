#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    z = 0
    try:
        while z is not x:
            print(my_list[z], end='')
            z += 1
    except IndexError:
        None
    print()
    return z
