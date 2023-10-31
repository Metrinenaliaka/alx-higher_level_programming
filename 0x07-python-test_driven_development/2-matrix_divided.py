#!/usr/bin/python3
"""
A function that divides elemnts of a matrix
args:
    matrix: list of lists of type int
    div: int
"""


def matrix_divided(matrix, div):
    n_matrix = []
    for row in matrix:
        for column in row:
            if not isinstance(column, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row1 = matrix[0]
    for rows in matrix[1:]:
        if rows != row1:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    n_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    return n_matrix
