#!/usr/bin/python3
"""
1. Pascal's Triangle
"""


def generate_pascals_triangle(n):
    """Generate Pascal's triangle up to the nth row."""
    triangle = []
    if n > 0:
        for row_number in range(1, n + 1):
            row_values = []
            coefficient = 1
            for col_number in range(1, row_number + 1):
                row_values.append(coefficient)
                coefficient = coefficient * (row_number - col_number) // col_number
            triangle.append(row_values)
    return triangle
