#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(0, len(matrix)):
        for n in range(0, len(matrix[i])):
            if n < len(matrix[n]) - 1:
                print("{:d}".format(matrix[i][n]), end=' ')
            else:
                print("{:d}".format(matrix[i][n]), end='')
        print()
