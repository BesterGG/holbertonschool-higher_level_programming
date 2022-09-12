#!/usr/bin/python3
from re import I


def print_matrix_integer(matrix=[[]]):
    for i in range(0, len(matrix)):
        for n in range(0, len(matrix[i])):
            print("{}".format(matrix[i][n]), end=' ')
        print()
