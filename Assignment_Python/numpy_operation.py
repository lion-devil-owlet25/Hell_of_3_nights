import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# a) Inverse of a matrix
print("Inverse:\n", np.linalg.inv(A))

# b) Rank of a matrix
print("Rank:", np.linalg.matrix_rank(A))

# c) Transpose
print("Transpose:\n", A.T)

# d) Multiplication
print("Multiplication:\n", np.dot(A, B))

# e) Determinant
print("Determinant:", np.linalg.det(A))

