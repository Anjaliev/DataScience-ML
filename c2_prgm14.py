import  numpy as np
A=np.array([[1,2,3],[4,5,6],[7,8,9]])
B=np.array([[9,8,7],[6,5,4],[3,2,1]])
C=np.array([[10,5,9],[20,15,19],[30,2,29]])
result=np.dot(np.dot(A,B),C)
print("Matrix A:\n",A)
print("Matrix B:\n",B)
print("Matrix C:\n",C)
print("Result of(A*B)*C:\n",result)