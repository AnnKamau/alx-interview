#!/usr/bin/python3
"""
Rotate 2D Matrix
"""

def rotate_2d_matrix(matrix):
    """
    Rotate the matrix 90 degrees clockwise in-place.
    """
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            # Save the top element
            top = matrix[i][j]
            # Move the left element to the top
            matrix[i][j] = matrix[n - 1 - j][i]
            # Move the bottom element to the left
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            # Move the right element to the bottom
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            # Assign the saved top element to the right
            matrix[j][n - 1 - i] = top

# Example usage:
if __name__ == "__main__":
    matrix = [[1, 2, 3],
            [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)

