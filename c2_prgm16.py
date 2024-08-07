import numpy as np
A = np.array([[2, 1, -2],[3, 0, 1],[1, 1, -1]])
b = np.array([-3, 5, -2])
x = np.linalg.solve(A, b)
print("Matrix A:\n", A)
print("Vector b:\n", b)
print("Solution for x:\n", x)
