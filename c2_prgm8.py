import numpy as np
arr1=np.array([1,2,3,4,5])
print("1D array :")
print(arr1)
arr1=np.insert(arr1,2,6)
print("1D array after insertion:")
print(arr1)
arr2=np.array([[1,2,3],[4,5,6]])
print("2D array:")
print(arr2)
arr2=np.insert(arr2,1,[7,8,9],axis=0)
print("2D array after insertion;")
print(arr2)