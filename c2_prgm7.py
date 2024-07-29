import numpy as np
matrix1=np.array([[1,2,3],[4,5,6],[7,8,9]])
matrix2=np.array([[9,8,7],[6,5,4],[3,2,1]])
matrix_add=matrix1+matrix2
matrix_sub=matrix1-matrix2
matrix_indi_mul=matrix1*matrix2
matrix_div=matrix1/matrix2
matrix_mul = np.dot(matrix1, matrix2)
matrix_transpose=np.transpose(matrix1)
diagonal_sum=np.trace(matrix1)
print("Matrix 1:\n",matrix1)
print("Matrix 2:\n",matrix2)
print("Addition of Matrix:\n",matrix_add)
print("Subtraction of matrix:\n",matrix_sub)
print("Multiply the individual elements:\n",matrix_indi_mul)
print("Matrix Division:\n",matrix_div)
print("Matrix Multiplication:\n",matrix_mul)
print("Transpose of a matrix:\n",matrix_transpose)
print("Sum of diagonal element:\n",diagonal_sum)