#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for sub_matrix in matrix:
        if len(sub_matrix) == 0:
            print()
        for x in range(len(sub_matrix)):
            print("{:d}".format(sub_matrix[x]),
                  end="\n" if x is len(sub_matrix) - 1 else " ")
