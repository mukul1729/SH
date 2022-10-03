
arr = [5,4,9,1,2,4,8,11,22,457,21,89,986]
for i in range(1,len(arr)):
    ele = arr[i]
    j = i
    while j>0 and arr[j-1]>ele:
        arr[j] = arr[j-1]
        j-=1
    arr[j] = ele
print(arr)
