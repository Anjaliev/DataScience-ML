import numpy as np
arr1=np.array([1,2,3,4,5])
dia_matrix1=np.diag(arr1)
print("1D array;\n",arr1)
print("Diagonal matrix:\n",dia_matrix1)
arr2=np.array([[1,2,3],[4,5,6],[7,8,9]])
dia_matrix2=np.diag(arr2)
print("2D array:\n",arr2)
print("Diagonal Matrix;\n",dia_matrix2)
arr3_non_square=np.array([[1,2,3],[4,5,6]])
dia_non_square=np.diag(arr3_non_square)
print("2D non Square matrix:\n",arr3_non_square)
print("Diagonal matrix:\n",dia_non_square)
