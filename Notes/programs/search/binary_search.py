# classic implementation
a = [1,4,7,9,10,34,76,89]
low = 0
high = len(a)-1
mid = (low+high)//2

element = 89
while low<=high:
    if a[mid]>element:
        high = mid-1
    elif a[mid]<element:
        low = mid+1
    else:
        print(mid)
        break
    mid = (low+high)//2

# Faster implementation
array = [1,4,8,9,20,73]
n = len(array)
k = 0
b = n//2
x = 73
while b>=1:
    while k+b<n and array[k+b]<=x:
        k+=b
    if array[k] == x:
        print('Found',k)
        break
    b//=2
