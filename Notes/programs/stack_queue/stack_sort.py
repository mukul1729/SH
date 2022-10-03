a = [44,1,4,3,7,2,99,78]
temp = [a.pop()]
while a:
    e = a.pop()
    while len(temp)>0 and temp[-1]>e:
        a.append(temp.pop())
    temp.append(e)
while temp:
    a.append(temp.pop())
print(a)
