# Question 2

exp = input("Enter mathematical expression in 'a'operation'b' format : ")

oprns = ['+', '-', '*', '/']     # valid operations

cnt_op = 0                       # count of operator

for i in oprns:
    if i in exp:
        idx = exp.index(i)       # idx=index of operator
        num1 = int(exp[0:idx])                            
        num2 = int(exp[(idx+1):])

        cnt_op += 1

if cnt_op == 1:
    oprn = exp[idx]

    if oprn == '+':
        print(num1+num2)
    elif oprn == '-':
        print(num1-num2)
    elif oprn == '*':
        print(num1*num2)
    elif oprn == '/':
        print(num1/num2)

else:
    print('Invalid expression')
