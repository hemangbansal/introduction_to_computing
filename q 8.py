# QUESTION 8

l_pos=[]                # list of positive numbers
l_neg=[]                # list of negative numbers
l_odd=[]                # list of odd numbers
l_even=[]               # list of even numbers

for i in range(10):
    num=int(input())        # input number
    if num>0:
        l_pos.append(num)
    if num<0:
        l_neg.append(num)
    if num%2==1:
        l_odd.append(num)
    if num%2==0:
        l_even.append(num)

d_pos={}                # dictionary of positive numbers
d_neg={}                # dictionary of negative numbers
d_odd={}                # dictionary of odd numbers
d_even={}               # dictionary of even numbers

l_all = [l_pos,l_neg,l_odd,l_even]      # list of all lists
d_all = [d_pos,d_neg,d_odd,d_even]      # list of all dictionaries

for i in range(4):          # 4 = len(l_all)
    for j in l_all[i]:      # j = element of individual list
        if j in d_all[i]:   # counting number of occurence of elements in each list
            d_all[i][j]+=1
        else:
            d_all[i][j]=1

print(l_pos,d_pos)
print(l_neg,d_neg)
print(l_odd,d_odd)
print(l_even,d_even)