# QUESTION 3
 
import random

for i in range(1,11):                                           # i=iterator
    num1=random.randrange(1,11)
    num2=random.randrange(1,11)
    print('Question',i,':',str(num1)+' x '+str(num2))           # Question statement
    ans=int(input("Enter your answer : "))
    if ans==num1*num2:
        print('Right!')
    else:
        print('Wrong. The answer is',str(num1*num2)+'.')