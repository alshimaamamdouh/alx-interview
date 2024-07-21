#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate the matrix 90 degrees clockwise in-place.

    :param matrix: List[List[int]] -- a 2D list representing the matrix
    """
    n = len(matrix)

    # Rotate the matrix layer by layer
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            # Save the top element
            top = matrix[first][i]

            # Move left element to top
            matrix[first][i] = matrix[last - offset][first]

            # Move bottom element to left
            matrix[last - offset][first] = matrix[last][last - offset]

            # Move right element to bottom
            matrix[last][last - offset] = matrix[i][last]

            # Move top element to right
            matrix[i][last] = top
