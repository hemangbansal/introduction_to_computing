# QUESTION 2

r = int(input('Enter range : '))
divisor = int(input("Enter divisor : "))
for test in range(1, r+1):
    if test % divisor == 0:
        print(test)
