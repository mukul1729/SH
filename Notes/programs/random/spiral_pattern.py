rows,cols=(100,100)
a = [[0 for x in range(rows)] for y in range(cols)] 
t=int(input())
x=0
for z in range(t):
    p=int(input())
    for i in range(0,((p-1)*2)+1):
        for j in range(0,(p)):
            for k in range(0,(p)):
                if j+k==i:
                    x=x+1
                    a[j][k]=x                   

    for i in range(0,p):
        for j in range(0,p):
            print(a[i][j],end='\t')
        print()

    x=0
    print()
