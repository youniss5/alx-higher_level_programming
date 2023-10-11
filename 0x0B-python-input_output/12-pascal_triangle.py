#!/usr/bin/python3
""" pascal triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    tri = [[1]]
    while len(tri) != n:
        tr = tri[-1]
        tm = [1]
        for x in range(len(tr) - 1):
            tm.append(tr[x] + tr[x + 1])
        tm.append(1)
        tri.append(tm)
    return tri
