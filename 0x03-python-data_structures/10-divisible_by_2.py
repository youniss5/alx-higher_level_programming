#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    listdiv = []
    for x in my_list:
        if (x % 2) == 0:
            listdiv.append(True)
        else:
            listdiv.append(False)
    return listdiv
