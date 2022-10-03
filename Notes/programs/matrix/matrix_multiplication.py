a1 = [[1,1],[1,1]]
a2 = [[1,2],[2,1]]
r1,r2 = 2,2
c1,c2 = 2,2
ans = [[0,0],[0,0]]
for i in range(r1):
    for j in range(c2):
        for k in range(c1):
            ans[i][j]+=a1[i][k]+a2[k][j]
print(ans)
