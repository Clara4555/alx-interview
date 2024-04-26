#!/usr/bin/python3
"""
2D matrix, rotate it 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """rotate 2D  matrix to 90 degrees clockwise
    Args:
        matrix (list[[list]]): a matrix
    """
    a = len(matrix)
    for b in range(int(a / 2)):
        y = (a - b - 1)
        for j in range(b, y):
            x = (a - 1 - j)
            # current number
            temp = matrix[b][j]
            # change top for lift
            matrix[b][j] = matrix[x][b]
            # change left for bottom
            matrix[x][b] = matrix[y][x]
            # change bottom for right
            matrix[y][x] = matrix[j][y]
            # change right for top
            matrix[j][y] = temp
