#!/usr/bin/python3
"""
Module: Calculator
Provides functions for dividing elements in matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Parameters:
        matrix: the matrix
        div: div

    Returns:
        matrix: a new matrix divided by div
    """
    if not all(isinstance(row, list) for row in matrix) or\
not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

    # Check if each row of the matrix has the same size
    row_sizes = [len(row) for row in matrix]
    if len(set(row_sizes)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements of the matrix by div, rounding to 2 decimal places
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return new_matrix
