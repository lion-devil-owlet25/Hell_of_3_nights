import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("Inverse:\n", np.linalg.inv(A))
print("Rank:", np.linalg.matrix_rank(A))
print("Transpose:\n", A.T)
print("Multiplication:\n", np.dot(A, B))
print("Determinant:", np.linalg.det(A))

