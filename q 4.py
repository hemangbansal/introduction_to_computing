# QUESTION 4

for i in range(9):
    if i <= 4:                  # increasing number of stars
        for j in range(i+1):
            print('*', end=' ')
    else:                       # decreasing number of stars
        for j in range(9-i):
            print('*', end=' ')
    print()                     # for new line
