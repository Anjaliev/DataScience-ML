import numpy as np
A=np.array([[5,27,32],[14,53,62],[67,88,19]])
U,S,Vt=np.linalg.svd(A)
A_hat=U@np.diag(S)@Vt
print("Original matrix A:\n",A)
print("Singular values:\n",S)
print("Reconstructed matrix A_hat:\n",A_hat)