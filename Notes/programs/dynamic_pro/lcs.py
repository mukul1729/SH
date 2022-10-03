import math

#input
'''
axyb
abyxb
'''

a = input()
b = input()
def same(a,b):
    l = [[1 for i in range(len(b))] for j in range(len(a))]
    for i in range(1,len(a)):
        for j in range(1,len(b)):
            if a[i] == b[j]:
                l[i][j] = 1+l[i-1][j-1]
            else:
                l[i][j] = max(l[i][j-1],l[i-1][j])
    return l
def sol(a,b,l):
    s = []
    j,k = len(a),len(b)
    while l[j][k] > 0:
        if a[j-1] == b[k-1]:
            s.append(a[j-1])
            j-=1
            k-=1
        elif l[j-1][k]>=l[j][k-1]:
            j-=1
        else:
            k-=1
    return ''.join(reversed(s))
print(same(a,b))
print(sol(a,b,same(a,b)))
