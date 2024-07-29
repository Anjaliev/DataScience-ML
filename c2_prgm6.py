import numpy as np
arr=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
excluding_1row=arr[1:]
excluding_last_col=arr[:,:-1]
column_1_2_in_row_2_3=arr[1:3,0:2]
column_2_3=arr[:,1:3]
elements_2_3_in_1row=arr[0,1:3]
desc_order=arr.ravel()[::-1][4:11]
print("Original array:",arr)
print("Element excluding 1st row:",excluding_1row)
print("Elements excluding last column:",excluding_last_col)
print("Elements of 1st & 2nd column in the 2nd & 3rd row:",column_1_2_in_row_2_3)
print("Elements of the 2nd& 3rd column:",column_2_3)
print("2nd & 3rd element of the 1st row:",elements_2_3_in_1row)
print("Elements from indices 4 to 10 in descending order:",desc_order)