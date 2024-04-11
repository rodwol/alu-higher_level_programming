#!/usr/bin/python3
"""
Module: Calculator
Provides functions for dividing elements in matrix
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Parameters:
        matrix (list of lists): The matrix to be divided.
            Each inner list represents a row of the matrix.
            Elements of the matrix must be integers or floats.
        div (int or float): The divisor by which to divide all elements of the matrix.

    Returns:
        list of lists: A new matrix where each element is the result of dividing
            the corresponding element of the input matrix by div.
            The result is rounded to 2 decimal places.

    Raises:
        TypeError: If the input matrix is not a list of lists, or if any element
            of the matrix is not an integer or float.
        TypeError: If each row of the matrix doesn't have the same size.
        TypeError: If the divisor is not a number.
        ZeroDivisionError: If the divisor is zero.
    """

    # Check if matrix is a list of lists and contains only integers or floats
    if not all(isinstance(row, list) for row in matrix) or \
       not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

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
