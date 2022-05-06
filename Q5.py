# QUESTION 5

side1=round(float(input('Enter first side : ')))
side2=round(float(input('Enter second side : ')))
side3=round(float(input('Enter third side : ')))
a=side1+side2>side3
b=side2+side3>side1
c=side3+side1>side2
match a,b,c:
    case True,True,True:            # Checking for valid triangle case
        print('Yes')
    case (False,True|False,True|False)|(True,False,True|False)|(True,True,False):           # Checking for invalid triangle case
        print('No')
