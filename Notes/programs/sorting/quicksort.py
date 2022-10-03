import time
def quick_sort(a):
    if len(a) <= 1: #len(a)<=1 because a can be []
        return a
    left,mid,right = [],[],[]
    for i in a:
        if i<a[-1]:
            left.append(i)
        elif i>a[-1]:
            right.append(i)
        else:
            mid.append(i)
    return quick_sort(left) + mid + quick_sort(right)

#inplace quicksort use no extra memory
def quicksort(s,a,b):
    if a>=b:
        return
    pivot = s[b]
    left = a
    right = b-1
    while left<=right:
        while left<=right and s[left]<pivot:
            left+=1
        while left<=right and s[right]>pivot:
            right-=1
        if left<=right:
            s[left],s[right] = s[right],s[left]
            left,right = left+1,right-1
    s[left],s[b] = s[b],s[left]
    quicksort(s,a,left-1)
    quicksort(s,left+1,b)


import random
s = [random.randint(1,100000) for i in range(10**5)]
t1 = time.time()
a,b = 0,len(s)-1
print(quicksort(s,a,b))
t2 = time.time()
print(t2-t1)

'''
0.6677041053771973
0.5228261947631836
'''
