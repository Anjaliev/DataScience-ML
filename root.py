import math
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
d = b**2 - 4*a*c
if d > 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print(f"Roots are: {round(root1, 2)} and {round(root2, 2)}")
elif d == 0:
    root = -b / (2*a)
    print(f"Root is: {round(root, 2)}")
else:
    real_part = -b / (2*a)
    img_part = math.sqrt(abs(d)) / (2*a)
    root1 = complex(real_part, img_part)
    root2 = complex(real_part, -img_part)
    print(f"Roots are: {round(root1.real, 2)} + {round(root1.imag, 2)}i and {round(root2.real, 2)} - {round(root2.imag, 2)}i")
