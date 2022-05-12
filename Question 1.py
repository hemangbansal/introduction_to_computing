# Question 1

num = int(input())        # decimal number
rem = 0                   # repeated remainder
add = 0                   # step addend to bin_num
i = 0                     # iterator
bin_num = 0               # binary number
while num > 0:
    rem = num % 2
    add = rem*(10**i)     # multiplying rem to place value
    bin_num += add
    num = num//2
    i += 1
print(bin_num)