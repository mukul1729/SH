# heap permute algorithm
def permute(s,k):
    if k == 0:
        print(s)
    else:
        for i in range(k+1):
            permute(s,k-1)
            if k%2 == 0:
                s[i],s[k] = s[k],s[i]
            else:
                s[0],s[k] = s[k],s[0]
print(permute(['A','B','C'],2))
