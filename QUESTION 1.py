# QUESTION 1

def perfect(n):
    l_divisors = []                         # Empty list of proper divisors of n
    for divisor in range(1, n):
        if n % divisor == 0:                
            l_divisors.append(divisor)      # if divisor | n, then appending it to l_divisor
    if sum(l_divisors) == n:
        print('YES')
    else:
        print('NO')

# Driver Code
num = int(input('Enter no. to be checked : '))
perfect(num)
