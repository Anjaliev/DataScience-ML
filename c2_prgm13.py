import numpy as np
A=np.array([[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,2,28,29,30]])
print("Matrix A:\n",A)
B=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Matrix B:\n",B)
sub_matrix=A[:3,:3]
print("The sub matrix;\n",sub_matrix)
result=np.dot(sub_matrix,B)
print("Matrix after multiplication with the sub matrix of A and matrix B:\n",result)
A[:3,:3]=result
print("Matrix A after the operation:\n",A)