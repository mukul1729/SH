
a = [5,6,9,1,2,4]
for i in range(len(a)):
    for j in range(1,len(a)-i):
        if a[j-1]>a[j]:
            a[j-1],a[j] = a[j],a[j-1]
print(a)

