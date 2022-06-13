# QUESTION 6

start = int(input('Enter the lower limit : '))    # lower limit of range
finish = int(input('Enter the upper limit : '))   # upper limit of range
for num in range(start, finish+1):               # num = no. to be checked
    count_divisor = 0
    for div in range(1, num+1):                  # div = no.to be checked as divisor of num
        if num % div == 0:
            count_divisor += 1
    if count_divisor == 2:                        # num will be prime if it has only 2 divisors i.e. 1 and num itself
        print(num)
