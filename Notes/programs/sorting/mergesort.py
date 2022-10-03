def merge(s1,s2):
    s = [0]*(len(s1)+len(s2))
    i,j = 0,0
    while i+j<len(s):
        if j == len(s2) or (i<len(s1) and s1[i]<s2[j]):
            s[i+j] = s1[i]
            i+=1
        else:
            s[i+j] = s2[j]
            j+=1
    return s

def mergesort(s):
    if len(s) == 1:
        return s
    else:
        n = len(s)
        mid = n//2
        s1 = s[0:mid]
        s2 = s[mid:]
        s1 = mergesort(s1)
        s2 = mergesort(s2)
        return merge(s1,s2)

s = [9,2,1,5,4,7,8]
print(mergesort(s))
