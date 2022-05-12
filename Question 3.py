# Question 3
 
import math as mt

print('A :')
print((3+4)*5)              #(a)

print('B :')
n=float(input('Enter n : '))
print((n*(n-1))/2)          #(b)

print('C :')
r=float(input("Enter radius of circle : "))
print(4*(mt.pi)*(r**2))     #(c)

print('D :')
r1=float(input('Enter value of r : '))
a=float(input("Enter first angle : "))
b=float(input("Enter second angle : "))
print(mt.sqrt(r1*(mt.cos(a)**2)+(r1*(mt.sin(b)**2))))   #(d)

print('E :')
x1=float(input('Enter x1 : '))
x2=float(input('Enter x2 : '))
y1=float(input('Enter y1 : '))
y2=float(input('Enter y2 : '))
print((y2-y1)/(x2-x1))      #(e)