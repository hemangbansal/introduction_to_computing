# QUESTION 3

import math as mt

side1 = float(input("Enter first side : "))
side2 = float(input("Enter second side : "))
side3 = float(input("Enter third side : "))
s = (side1+side2+side3)/2                                       # semi - perimeter
if side1+side2 > side3 and side2+side3 > side1 and side1+side3 > side2:     # checking condition for triangle to exist
    area = mt.sqrt((s*(s-side1)*(s-side2)*(s-side3)))           # heron's formula
    print('Area of the triangle =', area)
else:
    print('Invalid side lengths')
