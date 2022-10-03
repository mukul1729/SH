a = input("Enter amount charged and amount given and starting range seperated by ,")
x = a.split(',')
change = int(x[0])
start = int(x[1])
a = [2000,500,100,50,20,10,5,2,1]
d = {}
for p in range(0,len(a)):
    if a[p]==start:
        break
for x in range(p,len(a)):
    d[a[x]] = int(change/a[x])
    change = change - int(d[a[x]]*a[x])

print(d)
