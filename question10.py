# Write a Python function that takes a 2D list (matrix) and returns its transpose.

def transpose_matrix(matrix):
    if not matrix:
        return []

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Initialize the transpose matrix with appropriate dimensions
    transpose = [[0] * num_rows for _ in range(num_cols)]

    # Compute the transpose
    for i in range(num_rows):
        for j in range(num_cols):
            transpose[j][i] = matrix[i][j]

    return transpose

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original Matrix:")
for row in matrix:
    print(row)

print("\nTranspose Matrix:")
transpose = transpose_matrix(matrix)
for row in transpose:
    print(row)
