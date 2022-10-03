def find_uniq(arr):
    r = arr[1] if (arr[0]==arr[1] or arr[1]==arr[2]) else arr[2]
    p = set(arr)
    p.remove(r)
    a = [x for x in p]
    return a[0]
print(find_uniq([2,2,2,9,2]))
