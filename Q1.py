# QUESTION 1

s1='Python is a case sensitive language'

print(len(s1))   #a

print(s1[-1::-1])    #b

s2=s1[10:26]    #c
print(s2)

s3=s1.replace('a case sensitive','object oriented')     #d
print(s3)

print(s1.index('a'))    #e

s4=s1.strip().split()   #f
s4=''.join(s4)
print(s4)
