A = [[1, 2], [4, 5], [7, 8]]
def snail(snail_map):
    a = snail_map
    n = len(a[0])
    m = len(a)
    t,b,l,r = 0,m-1,0,n-1
    dir = 0
    arr = []
    while t<=b and l<=r:
        if dir == 0:
            for i in range(l,r+1):
                arr.append(a[t][i])
            t+=1
            dir = 1
        elif dir == 1:
            for i in range(t,b+1):
                arr.append(a[i][r])
            r-=1
            dir = 2
        elif dir == 2:
            for i in range(r,l-1,-1):
                arr.append(a[b][i])
            b-=1
            dir = 3
        elif dir == 3:
            for i in range(b,t-1,-1):
                arr.append(a[i][l])
            l+=1
            dir = 0
    return arr
print(snail(A))
