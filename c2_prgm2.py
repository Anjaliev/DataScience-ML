import numpy as np
print("23MCA016,Anjali E V")
arr=np.array([[1+2j,8+4j,4+8j],[5+8j,4+5j,6+9j]],dtype=complex)
print("2D array:")
print(arr)
r,c=arr.shape
print("Number of rows:",r)
print("Number of columns:",c)
dim=arr.ndim
print("dimensional of array:",dim)
reshape_arr=arr.reshape(3,2)
print("Reshaped array:")
print(reshape_arr)