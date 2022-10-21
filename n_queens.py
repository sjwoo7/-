def n_queens (i, col):
    a = len(col) - 1
    #cnt=0
    if (prv (i, col)):
        if (i==a):
            print(col[1: a+1])
        else:
            for j in range(1, a+1):
                col[i+1] = j
                n_queens(i+1, col)


            

def prv (i, col):
    k=1
    flag = True
    while (k < i and flag):
        if (col[i] == col[k] or abs( col[i] - col[k]) == (i-k) ):
            flag=False
        k+=1
    return flag


a = input()
col = [0] * (a+1)
n_queens(0, col)


