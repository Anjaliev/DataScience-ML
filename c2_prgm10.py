import numpy as np
matrix_size=3
matrix=np.random.randint(10,20,size=(matrix_size,matrix_size))
print("Matrix is:\n",matrix)
if np.linalg.matrix_rank(matrix)==matrix_size:
    inverse_matrix=np.linalg.inv(matrix)
    print("Inverse matrix is:\n",inverse_matrix)
else:
    print("Rank less than size of matrix:")
rank=np.linalg.matrix_rank(matrix)
print("Rank of matrix:\n",rank)
determinant=np.linalg.det(matrix)
print('Determinant of a matrix:\n',determinant)
matrix1=matrix.flatten()
print("Matrix as 1D array:",matrix1)
eigenvalue,eigenvector=np.linalg.eig(matrix)
print("Eigen value:\n",eigenvalue)
print("Eigen vector;\n",eigenvector)
