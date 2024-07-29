import numpy as np
even_arr=np.arange(2,31,2)
slice_arr=even_arr[2:9:2]
last3_arr=even_arr[-3:]
alternate_arr=even_arr[ : :2]
last3_alt_arr=alternate_arr[-3: :]
print("Original array:",even_arr)
print("2 to 8 with intervel 2:",slice_arr)
print("Last 3 element:",last3_arr)
print("Alternate element with intervel 2:",alternate_arr)
print("Last 3 alternate element:",last3_alt_arr)