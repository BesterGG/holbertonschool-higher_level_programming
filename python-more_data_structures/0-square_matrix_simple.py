#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nm = []
    for i in matrix:
        nm.append(list(map(lambda x:x * x, i)))
    return nm
