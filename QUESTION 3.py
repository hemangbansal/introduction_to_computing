# QUESTION 3

def pascal(n):
    if n==1:
        print(1)
    else:
        l=[[1],[1,1]]               # first two rows
        for i in range(2,n):
            l.append([1,1])         # first and last positions of each row
            for j in range(1,i):
                l[i].insert(j,l[i-1][j-1]+l[i-1][j])        # adding two elements from previous row and inserting
        m=n-1
        for k in range(n):
            s=' '.join(list(map(str,l[k])))     # converting each row of numbers to string
            for _ in range(m):                  # number of beginning spaces in each row
                print(end=' ')
            print(s)
            m-=1                                # reducing number of beginning spaces in each row

# Driver Code
n=int(input())
pascal(n)