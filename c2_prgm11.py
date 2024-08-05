import numpy as np
x=np.array([[1,2,3],[4,5,6],[7,8,9]])
x_cube_multiply=np.multiply(x,np.multiply(x,x))
x_cube_operator=x*x*x
x_cube_power=np.power(x,3)
x_cube_double_star=x ** 3
identity_matrix=np.identity(x.shape[0])
x_power2=np.power(x,2)
x_power3=np.power(x,3)
x_power4=np.power(x,4)
print("Matrix is:\n",x)
print("Cubed matrix(multiply()):\n",x_cube_multiply)
print("Cubed matrix(*):\n",x_cube_operator)
print("Cubed matrix(power()):\n",x_cube_power)
print("Cubed matrix(**):\n",x_cube_double_star)
print("Identity matrix:\n",identity_matrix)
print("x^2:\n",x_power2)
print("x^3:\n",x_power3)
print("x^4:\n",x_power4)



