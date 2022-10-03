import math
def isPP(n):
    a = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
    w = int(math.log2(n))
    N = [i for i in range(w+1)]
    for i in range(len(a)):
        if a[i] >= w:
            index = i
            break
    for i in range(2,int(pow(n,0.5))+1):
        for j in range(index+1):
            if pow(i,a[j]) == n:
                return(i,a[j])
    return None

print(isPP(216))
