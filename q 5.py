# QUESTION 5

rows=int(input("Input the number of rows = "))
k=0                                 # k = iterator over letter ascii value
for i in range(rows):               # i = iterator over rows
    for j in range(i+1):            # j = iterator over columns
        if k>25:                    # if alphabet gets exhausted k=0 i.e. chr(65+0)='A' and so on
            k=0
        print(chr(65+k),end='')
        k+=1
    print()                         # for new line